# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestcasePlanVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'testcase_uri': 'str',
        'testcase_number': 'str',
        'plans': 'list[TestPlanVo]'
    }

    attribute_map = {
        'testcase_uri': 'testcase_uri',
        'testcase_number': 'testcase_number',
        'plans': 'plans'
    }

    def __init__(self, testcase_uri=None, testcase_number=None, plans=None):
        r"""TestcasePlanVo

        The model defined in huaweicloud sdk

        :param testcase_uri: 测试用例URI
        :type testcase_uri: str
        :param testcase_number: 测试用例用例编号
        :type testcase_number: str
        :param plans: 测试计划信息
        :type plans: list[:class:`huaweicloudsdkcloudtest.v1.TestPlanVo`]
        """
        
        

        self._testcase_uri = None
        self._testcase_number = None
        self._plans = None
        self.discriminator = None

        if testcase_uri is not None:
            self.testcase_uri = testcase_uri
        if testcase_number is not None:
            self.testcase_number = testcase_number
        if plans is not None:
            self.plans = plans

    @property
    def testcase_uri(self):
        r"""Gets the testcase_uri of this TestcasePlanVo.

        测试用例URI

        :return: The testcase_uri of this TestcasePlanVo.
        :rtype: str
        """
        return self._testcase_uri

    @testcase_uri.setter
    def testcase_uri(self, testcase_uri):
        r"""Sets the testcase_uri of this TestcasePlanVo.

        测试用例URI

        :param testcase_uri: The testcase_uri of this TestcasePlanVo.
        :type testcase_uri: str
        """
        self._testcase_uri = testcase_uri

    @property
    def testcase_number(self):
        r"""Gets the testcase_number of this TestcasePlanVo.

        测试用例用例编号

        :return: The testcase_number of this TestcasePlanVo.
        :rtype: str
        """
        return self._testcase_number

    @testcase_number.setter
    def testcase_number(self, testcase_number):
        r"""Sets the testcase_number of this TestcasePlanVo.

        测试用例用例编号

        :param testcase_number: The testcase_number of this TestcasePlanVo.
        :type testcase_number: str
        """
        self._testcase_number = testcase_number

    @property
    def plans(self):
        r"""Gets the plans of this TestcasePlanVo.

        测试计划信息

        :return: The plans of this TestcasePlanVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestPlanVo`]
        """
        return self._plans

    @plans.setter
    def plans(self, plans):
        r"""Sets the plans of this TestcasePlanVo.

        测试计划信息

        :param plans: The plans of this TestcasePlanVo.
        :type plans: list[:class:`huaweicloudsdkcloudtest.v1.TestPlanVo`]
        """
        self._plans = plans

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TestcasePlanVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
