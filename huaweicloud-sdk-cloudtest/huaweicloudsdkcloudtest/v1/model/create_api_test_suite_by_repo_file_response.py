# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateApiTestSuiteByRepoFileResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'testsuite_id': 'str',
        'testcase_ids': 'list[str]'
    }

    attribute_map = {
        'testsuite_id': 'testsuite_id',
        'testcase_ids': 'testcase_ids'
    }

    def __init__(self, testsuite_id=None, testcase_ids=None):
        """CreateApiTestSuiteByRepoFileResponse - a model defined in huaweicloud sdk"""
        
        super(CreateApiTestSuiteByRepoFileResponse, self).__init__()

        self._testsuite_id = None
        self._testcase_ids = None
        self.discriminator = None

        if testsuite_id is not None:
            self.testsuite_id = testsuite_id
        if testcase_ids is not None:
            self.testcase_ids = testcase_ids

    @property
    def testsuite_id(self):
        """Gets the testsuite_id of this CreateApiTestSuiteByRepoFileResponse.

        生成的测试套的id

        :return: The testsuite_id of this CreateApiTestSuiteByRepoFileResponse.
        :rtype: str
        """
        return self._testsuite_id

    @testsuite_id.setter
    def testsuite_id(self, testsuite_id):
        """Sets the testsuite_id of this CreateApiTestSuiteByRepoFileResponse.

        生成的测试套的id

        :param testsuite_id: The testsuite_id of this CreateApiTestSuiteByRepoFileResponse.
        :type: str
        """
        self._testsuite_id = testsuite_id

    @property
    def testcase_ids(self):
        """Gets the testcase_ids of this CreateApiTestSuiteByRepoFileResponse.

        生成的测试用例id列表

        :return: The testcase_ids of this CreateApiTestSuiteByRepoFileResponse.
        :rtype: list[str]
        """
        return self._testcase_ids

    @testcase_ids.setter
    def testcase_ids(self, testcase_ids):
        """Sets the testcase_ids of this CreateApiTestSuiteByRepoFileResponse.

        生成的测试用例id列表

        :param testcase_ids: The testcase_ids of this CreateApiTestSuiteByRepoFileResponse.
        :type: list[str]
        """
        self._testcase_ids = testcase_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateApiTestSuiteByRepoFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other