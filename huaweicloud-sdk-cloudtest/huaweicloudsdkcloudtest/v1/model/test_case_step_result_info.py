# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseStepResultInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'actual_result': 'str',
        'expect_result': 'str',
        'test_step': 'str'
    }

    attribute_map = {
        'result': 'result',
        'actual_result': 'actual_result',
        'expect_result': 'expect_result',
        'test_step': 'test_step'
    }

    def __init__(self, result=None, actual_result=None, expect_result=None, test_step=None):
        r"""TestCaseStepResultInfo

        The model defined in huaweicloud sdk

        :param result: 步骤结果值
        :type result: str
        :param actual_result: 步骤实际结果
        :type actual_result: str
        :param expect_result: 步骤期望结果
        :type expect_result: str
        :param test_step: 用例操作步骤
        :type test_step: str
        """
        
        

        self._result = None
        self._actual_result = None
        self._expect_result = None
        self._test_step = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if actual_result is not None:
            self.actual_result = actual_result
        if expect_result is not None:
            self.expect_result = expect_result
        if test_step is not None:
            self.test_step = test_step

    @property
    def result(self):
        r"""Gets the result of this TestCaseStepResultInfo.

        步骤结果值

        :return: The result of this TestCaseStepResultInfo.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this TestCaseStepResultInfo.

        步骤结果值

        :param result: The result of this TestCaseStepResultInfo.
        :type result: str
        """
        self._result = result

    @property
    def actual_result(self):
        r"""Gets the actual_result of this TestCaseStepResultInfo.

        步骤实际结果

        :return: The actual_result of this TestCaseStepResultInfo.
        :rtype: str
        """
        return self._actual_result

    @actual_result.setter
    def actual_result(self, actual_result):
        r"""Sets the actual_result of this TestCaseStepResultInfo.

        步骤实际结果

        :param actual_result: The actual_result of this TestCaseStepResultInfo.
        :type actual_result: str
        """
        self._actual_result = actual_result

    @property
    def expect_result(self):
        r"""Gets the expect_result of this TestCaseStepResultInfo.

        步骤期望结果

        :return: The expect_result of this TestCaseStepResultInfo.
        :rtype: str
        """
        return self._expect_result

    @expect_result.setter
    def expect_result(self, expect_result):
        r"""Sets the expect_result of this TestCaseStepResultInfo.

        步骤期望结果

        :param expect_result: The expect_result of this TestCaseStepResultInfo.
        :type expect_result: str
        """
        self._expect_result = expect_result

    @property
    def test_step(self):
        r"""Gets the test_step of this TestCaseStepResultInfo.

        用例操作步骤

        :return: The test_step of this TestCaseStepResultInfo.
        :rtype: str
        """
        return self._test_step

    @test_step.setter
    def test_step(self, test_step):
        r"""Sets the test_step of this TestCaseStepResultInfo.

        用例操作步骤

        :param test_step: The test_step of this TestCaseStepResultInfo.
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
        if not isinstance(other, TestCaseStepResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
