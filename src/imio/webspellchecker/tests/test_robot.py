from plone.testing import layered

from pkg_resources import parse_version
import robotsuite
import unittest
from plone import api

from ..testing import IMIO_WEBSPELLCHECKER_ACCEPTANCE_TESTING

HAS_PLONE5 = parse_version(api.env.plone_version()) >= parse_version('5.0b2')


# TODO: add tests for CKE, check collective.ckeditor to have multiple profiles
def test_suite():
    filename = 'robot/plone4.robot'
    if HAS_PLONE5:
        filename = 'robot/plone5.robot'
    return unittest.TestSuite(
        [
            layered(
                robotsuite.RobotTestSuite(filename),
                layer=IMIO_WEBSPELLCHECKER_ACCEPTANCE_TESTING
            ),
        ]
    )
