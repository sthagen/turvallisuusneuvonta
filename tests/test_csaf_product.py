# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import re

import pytest

import turvallisuusneuvonta.csaf.product as product


def test_product_empty():
    assert isinstance(product.ProductTree(), product.ProductTree)


def test_product_text():
    message = '__init__() takes 1 positional argument but 3 were given'
    with pytest.raises(TypeError, match=re.escape(message)):
        _ = product.ProductTree('some', 'text')
