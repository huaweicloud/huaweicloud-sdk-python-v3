# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalServiceCaseStep:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expect_result': 'str',
        'test_step': 'str'
    }

    attribute_map = {
        'expect_result': 'expect_result',
        'test_step': 'test_step'
    }

    def __init__(self, expect_result=None, test_step=None):
        """ExternalServiceCaseStep

        The model defined in huaweicloud sdk

        :param expect_result: 测试用例预期结果信息，长度为[0-500]位字符
        :type expect_result: str
        :param test_step: 测试步骤描述信息，长度为[0-500]位字符
        :type test_step: str
        """
        
        

        self._expect_result = None
        self._test_step = None
        self.discriminator = None

        if expect_result is not None:
            self.expect_result = expect_result
        if test_step is not None:
            self.test_step = test_step

    @property
    def expect_result(self):
        """Gets the expect_result of this ExternalServiceCaseStep.

        测试用例预期结果信息，长度为[0-500]位字符

        :return: The expect_result of this ExternalServiceCaseStep.
        :rtype: str
        """
        return self._expect_result

    @expect_result.setter
    def expect_result(self, expect_result):
        """Sets the expect_result of this ExternalServiceCaseStep.

        测试用例预期结果信息，长度为[0-500]位字符

        :param expect_result: The expect_result of this ExternalServiceCaseStep.
        :type expect_result: str
        """
        self._expect_result = expect_result

    @property
    def test_step(self):
        """Gets the test_step of this ExternalServiceCaseStep.

        测试步骤描述信息，长度为[0-500]位字符

        :return: The test_step of this ExternalServiceCaseStep.
        :rtype: str
        """
        return self._test_step

    @test_step.setter
    def test_step(self, test_step):
        """Sets the test_step of this ExternalServiceCaseStep.

        测试步骤描述信息，长度为[0-500]位字符

        :param test_step: The test_step of this ExternalServiceCaseStep.
        :type test_step: str
        """
        self._test_step = test_step

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
        if not isinstance(other, ExternalServiceCaseStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
