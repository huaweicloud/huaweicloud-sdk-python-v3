# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'test_data': 'str',
        'test_rule_express': 'str'
    }

    attribute_map = {
        'test_data': 'test_data',
        'test_rule_express': 'test_rule_express'
    }

    def __init__(self, test_data=None, test_rule_express=None):
        r"""DebugRuleRequestBody

        The model defined in huaweicloud sdk

        :param test_data: 测试的被规则执行的数据
        :type test_data: str
        :param test_rule_express: 测试的规则
        :type test_rule_express: str
        """
        
        

        self._test_data = None
        self._test_rule_express = None
        self.discriminator = None

        if test_data is not None:
            self.test_data = test_data
        if test_rule_express is not None:
            self.test_rule_express = test_rule_express

    @property
    def test_data(self):
        r"""Gets the test_data of this DebugRuleRequestBody.

        测试的被规则执行的数据

        :return: The test_data of this DebugRuleRequestBody.
        :rtype: str
        """
        return self._test_data

    @test_data.setter
    def test_data(self, test_data):
        r"""Sets the test_data of this DebugRuleRequestBody.

        测试的被规则执行的数据

        :param test_data: The test_data of this DebugRuleRequestBody.
        :type test_data: str
        """
        self._test_data = test_data

    @property
    def test_rule_express(self):
        r"""Gets the test_rule_express of this DebugRuleRequestBody.

        测试的规则

        :return: The test_rule_express of this DebugRuleRequestBody.
        :rtype: str
        """
        return self._test_rule_express

    @test_rule_express.setter
    def test_rule_express(self, test_rule_express):
        r"""Sets the test_rule_express of this DebugRuleRequestBody.

        测试的规则

        :param test_rule_express: The test_rule_express of this DebugRuleRequestBody.
        :type test_rule_express: str
        """
        self._test_rule_express = test_rule_express

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
        if not isinstance(other, DebugRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
