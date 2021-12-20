# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import re

import pytest

import turvallisuusneuvonta.csaf.product as product


def test_product_empty():
    assert isinstance(product.ProductTree(), product.ProductTree)


def test_product_positional_text():
    message = '__init__() takes 1 positional argument but 3 were given'
    with pytest.raises(TypeError, match=re.escape(message)):
        _ = product.ProductTree('positional', 'text')  # type: ignore


def test_product_relationship():
    pr_ref_other = product.ReferenceTokenForProductInstance(value='acme-101')
    pr_ref_self = product.ReferenceTokenForProductInstance(value='acme-112')
    pr_id = pr_ref_self
    pr_ids = product.ListOfProductIds(product_ids=[pr_ref_self, pr_ref_other])
    assert pr_ref_other in pr_ids.product_ids
    product.FullProductName.update_forward_refs()
    pr_name = product.FullProductName(name='wun', product_id=pr_id)
    data = {
        'category': product.RelationshipCategory.installed_with,
        'full_product_name': pr_name,
        'product_reference': pr_ref_self,
        'relates_to_product_reference': pr_ref_other,
    }
    rel = product.Relationship(**data)
    assert rel.category == product.RelationshipCategory.installed_with
