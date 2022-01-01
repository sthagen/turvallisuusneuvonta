from typing import Dict, List, Tuple, no_type_check

import jmespath

import turvallisuusneuvonta.csaf.core.rules.mandatory.acyclic_product_ids as acy_product_ids  # type: ignore
import turvallisuusneuvonta.csaf.core.rules.mandatory.consistent_product_status as con_pro_sta  # type: ignore
import turvallisuusneuvonta.csaf.core.rules.mandatory.defined_group_ids as def_gro_ids  # type: ignore
import turvallisuusneuvonta.csaf.core.rules.mandatory.defined_product_ids as def_pro_ids  # type: ignore
import turvallisuusneuvonta.csaf.core.rules.mandatory.unique_group_ids as uni_gro_ids  # type: ignore
import turvallisuusneuvonta.csaf.core.rules.mandatory.unique_product_ids as uni_pro_ids  # type: ignore

TOPICS = (
    acy_product_ids,
    con_pro_sta,
    def_gro_ids,
    def_pro_ids,
    uni_gro_ids,
    uni_pro_ids,
)

TOPIC_MAP = {topic.TOPIC: topic.PATHS for topic in TOPICS}


@no_type_check
def exists(document: dict, claims: Dict[str, List[str]]) -> Tuple[Tuple[str, str, bool]]:
    """Verify the existence and return tuple of triplets with claim, path and result."""
    return tuple(
        (claim, path, bool(jmespath.search(path, document))) for claim, paths in claims.items() for path in paths
    )
