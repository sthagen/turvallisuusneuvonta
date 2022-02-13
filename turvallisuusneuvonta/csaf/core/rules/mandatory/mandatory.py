from typing import Dict, List, Tuple, no_type_check

import jmespath

import turvallisuusneuvonta.csaf.core.rules.mandatory.acyclic_product_ids as acy_product_ids  # type: ignore
import turvallisuusneuvonta.csaf.core.rules.mandatory.consistent_product_status as con_pro_sta  # type: ignore
import turvallisuusneuvonta.csaf.core.rules.mandatory.defined_group_ids as def_gro_ids  # type: ignore
import turvallisuusneuvonta.csaf.core.rules.mandatory.defined_product_ids as def_pro_ids  # type: ignore
import turvallisuusneuvonta.csaf.core.rules.mandatory.translator_and_source_lang as tra_and_sou_lan  # type: ignore
import turvallisuusneuvonta.csaf.core.rules.mandatory.unique_group_ids as uni_gro_ids  # type: ignore
import turvallisuusneuvonta.csaf.core.rules.mandatory.unique_product_ids as uni_pro_ids  # type: ignore
import turvallisuusneuvonta.csaf.core.rules.mandatory.valid_category_name as val_cat_nam  # type: ignore

TOPICS = (
    acy_product_ids,
    con_pro_sta,
    def_gro_ids,
    def_pro_ids,
    tra_and_sou_lan,
    uni_gro_ids,
    uni_pro_ids,
    val_cat_nam,
)

TOPIC_MAP = {topic.TOPIC: topic.PATHS for topic in TOPICS}


@no_type_check
def is_valid(document: dict) -> bool:
    """Complete validation of all mandatory rules.

    This is a spike - we throw it away when all rules are in and back comes something maintainable.
    """
    if not is_valid_category(document):
        return False

    if jmespath.search(tra_and_sou_lan.TRIGGER_JMES_PATH, document) == tra_and_sou_lan.TRIGGER_VALUE:
        if not is_valid_translator(document):
            return False

    defined_prod_ids = jmespath.search(def_pro_ids.TRIGGER_JMES_PATH, document)
    if defined_prod_ids is None:
        defined_prod_ids = []
    known_prod_ids = set(defined_prod_ids)
    for path in def_pro_ids.CONDITION_JMES_PATHS:
        claim_prod_ids = jmespath.search(path, document)
        if claim_prod_ids is not None:
            if any(claim_prod_id not in known_prod_ids for claim_prod_id in claim_prod_ids):
                return False

    defined_group_ids = jmespath.search(def_gro_ids.TRIGGER_JMES_PATH, document)
    if defined_group_ids is None:
        defined_group_ids = []
    known_group_ids = set(defined_group_ids)
    for path in def_gro_ids.CONDITION_JMES_PATHS:
        claim_group_ids = jmespath.search(path, document)
        if claim_group_ids is not None:
            if any(claim_group_id not in known_group_ids for cl_seq in claim_group_ids for claim_group_id in cl_seq):
                return False

    return NotImplemented


@no_type_check
def exists(document: dict, claims: Dict[str, List[str]]) -> Tuple[Tuple[str, str, bool]]:
    """Verify the existence and return tuple of triplets with claim, path and result."""
    return tuple(
        (claim, path, bool(jmespath.search(path, document))) for claim, paths in claims.items() for path in paths
    )


@no_type_check
def must_skip(document: dict, path: str, skip_these: Tuple[str, ...]) -> Tuple[str, str, bool]:
    """Verify any skips and return tuple of triplets with claim, path and result."""
    value = jmespath.search(path, document)
    return value, path, any(value == skip for skip in skip_these)


@no_type_check
def is_valid_category(document: dict) -> bool:
    """Verify category value."""
    return val_cat_nam.is_valid(jmespath.search(val_cat_nam.CONDITION_JMES_PATH, document))


@no_type_check
def is_valid_translator(document: dict) -> bool:
    """Verify source_lang value is present for translator."""
    if jmespath.search(tra_and_sou_lan.TRIGGER_JMES_PATH, document) != tra_and_sou_lan.TRIGGER_VALUE:
        return False
    return bool(jmespath.search(tra_and_sou_lan.CONDITION_JMES_PATH, document))
