from test import conftest

import msgspec
import pytest
from pydantic import ValidationError

import turvallisuusneuvonta.csaf.document as document


def _subs(count: int) -> str:
    """DRY."""
    return f'{count} validation error{"" if count == 1 else "s"} for Document'


def test_meta_doc_none():
    with pytest.raises(ValidationError, match=_subs(5)) as err:
        _ = document.Document()  # type: ignore
    for prop in ('category', 'csaf_version', 'publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  Field required' in str(err.value)


def test_meta_doc_category_empty():
    with pytest.raises(ValidationError, match=_subs(5)) as err:
        _ = document.Document(category='')  # type: ignore
    hint = 'String should have at least 1 character'
    assert f'\ncategory\n  {hint}' in str(err.value)
    for prop in ('csaf_version', 'publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  Field required' in str(err.value)


def test_meta_doc_csaf_version_wrong():
    with pytest.raises(ValidationError, match=_subs(4)) as err:
        _ = document.Document(**conftest.META_WRONG_VERSION)  # type: ignore
    hint = "Input should be '2.0'"
    assert f'\ncsaf_version\n  {hint}' in str(err.value)
    for prop in ('publisher', 'title', 'tracking'):
        assert f'\n{prop}\n  Field required' in str(err.value)


def test_meta_doc_publisher_empty():
    with pytest.raises(ValidationError, match=_subs(5)) as err:
        _ = document.Document(**conftest.META_EMPTY_PUBLISHER)  # type: ignore
    for prop in ('title', 'tracking'):
        assert f'\n{prop}\n  Field required' in str(err.value)
    host = 'publisher'
    for prop in ('category', 'name', 'namespace'):
        assert f'\n{host}.{prop}\n  Field required' in str(err.value)


def test_meta_doc_title_empty():
    with pytest.raises(ValidationError, match=_subs(2)) as err:
        _ = document.Document(**conftest.META_EMPTY_TITLE)  # type: ignore
    hint = 'String should have at least 1 character'
    assert f'\ntitle\n  {hint}' in str(err.value)
    for prop in ('tracking',):
        assert f'\n{prop}\n  Field required' in str(err.value)


def test_meta_doc_tracking_empty():
    with pytest.raises(ValidationError, match=_subs(6)) as err:
        _ = document.Document(**conftest.META_EMPTY_TRACKING)  # type: ignore
    host = 'tracking'
    for prop in ('current_release_date', 'id', 'initial_release_date', 'revision_history', 'status', 'version'):
        assert f'\n{host}.{prop}\n  Field required' in str(err.value)


def test_meta_doc_ok_if_spammy():
    meta_doc = document.Document(**conftest.META_OK)  # type: ignore
    strip_me = msgspec.json.decode(meta_doc.model_dump_json())
    conftest._strip_and_iso_grace(strip_me)
    assert strip_me == conftest.META_OK
