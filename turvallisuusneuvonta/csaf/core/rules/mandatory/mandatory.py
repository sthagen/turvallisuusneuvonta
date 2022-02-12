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
    """Complete validation of all mandatory rules."""
    if not is_valid_category(document):
        return False
    if jmespath.search('document.publisher.category', document) == 'translator':
        if not is_valid_translator(document):
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
    return val_cat_nam.is_valid(jmespath.search('document.category', document))


@no_type_check
def is_valid_translator(document: dict) -> bool:
    """Verify source_lang value is present for translator."""
    if jmespath.search('document.publisher.category', document) != 'translator':
        return False
    return bool(jmespath.search('document.source_lang', document))
