# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'test_result': 'str'
    }

    attribute_map = {
        'test_result': 'test_result'
    }

    def __init__(self, test_result=None):
        """DebugRuleResponse

        The model defined in huaweicloud sdk

        :param test_result: 规则测试输出结果
        :type test_result: str
        """
        
        super(DebugRuleResponse, self).__init__()

        self._test_result = None
        self.discriminator = None

        if test_result is not None:
            self.test_result = test_result

    @property
    def test_result(self):
        """Gets the test_result of this DebugRuleResponse.

        规则测试输出结果

        :return: The test_result of this DebugRuleResponse.
        :rtype: str
        """
        return self._test_result

    @test_result.setter
    def test_result(self, test_result):
        """Sets the test_result of this DebugRuleResponse.

        规则测试输出结果

        :param test_result: The test_result of this DebugRuleResponse.
        :type test_result: str
        """
        self._test_result = test_result

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
        if not isinstance(other, DebugRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
