# coding: utf-8

import pprint
import re

import six





class CreateTestCaseInPlanRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_id': 'int',
        'testcase_id_list': 'list[str]'
    }

    attribute_map = {
        'service_id': 'service_id',
        'testcase_id_list': 'testcase_id_list'
    }

    def __init__(self, service_id=None, testcase_id_list=None):
        """CreateTestCaseInPlanRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._service_id = None
        self._testcase_id_list = None
        self.discriminator = None

        self.service_id = service_id
        self.testcase_id_list = testcase_id_list

    @property
    def service_id(self):
        """Gets the service_id of this CreateTestCaseInPlanRequestBody.

        注册结果返回的服务id

        :return: The service_id of this CreateTestCaseInPlanRequestBody.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this CreateTestCaseInPlanRequestBody.

        注册结果返回的服务id

        :param service_id: The service_id of this CreateTestCaseInPlanRequestBody.
        :type: int
        """
        self._service_id = service_id

    @property
    def testcase_id_list(self):
        """Gets the testcase_id_list of this CreateTestCaseInPlanRequestBody.

        计划下包含的用例个数，数组长度小于50个，只能包含一种测试类型

        :return: The testcase_id_list of this CreateTestCaseInPlanRequestBody.
        :rtype: list[str]
        """
        return self._testcase_id_list

    @testcase_id_list.setter
    def testcase_id_list(self, testcase_id_list):
        """Sets the testcase_id_list of this CreateTestCaseInPlanRequestBody.

        计划下包含的用例个数，数组长度小于50个，只能包含一种测试类型

        :param testcase_id_list: The testcase_id_list of this CreateTestCaseInPlanRequestBody.
        :type: list[str]
        """
        self._testcase_id_list = testcase_id_list

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
        if not isinstance(other, CreateTestCaseInPlanRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
