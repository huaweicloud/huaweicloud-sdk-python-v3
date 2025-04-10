# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseStepInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'test_step': 'str',
        'expect_result': 'str',
        'step_actual': 'str',
        'step_result': 'str'
    }

    attribute_map = {
        'test_step': 'test_step',
        'expect_result': 'expect_result',
        'step_actual': 'step_actual',
        'step_result': 'step_result'
    }

    def __init__(self, test_step=None, expect_result=None, step_actual=None, step_result=None):
        r"""TestCaseStepInfo

        The model defined in huaweicloud sdk

        :param test_step: 测试步骤
        :type test_step: str
        :param expect_result: 预期结果
        :type expect_result: str
        :param step_actual: 步骤的实际结果
        :type step_actual: str
        :param step_result: 步骤结果
        :type step_result: str
        """
        
        

        self._test_step = None
        self._expect_result = None
        self._step_actual = None
        self._step_result = None
        self.discriminator = None

        if test_step is not None:
            self.test_step = test_step
        if expect_result is not None:
            self.expect_result = expect_result
        if step_actual is not None:
            self.step_actual = step_actual
        if step_result is not None:
            self.step_result = step_result

    @property
    def test_step(self):
        r"""Gets the test_step of this TestCaseStepInfo.

        测试步骤

        :return: The test_step of this TestCaseStepInfo.
        :rtype: str
        """
        return self._test_step

    @test_step.setter
    def test_step(self, test_step):
        r"""Sets the test_step of this TestCaseStepInfo.

        测试步骤

        :param test_step: The test_step of this TestCaseStepInfo.
        :type test_step: str
        """
        self._test_step = test_step

    @property
    def expect_result(self):
        r"""Gets the expect_result of this TestCaseStepInfo.

        预期结果

        :return: The expect_result of this TestCaseStepInfo.
        :rtype: str
        """
        return self._expect_result

    @expect_result.setter
    def expect_result(self, expect_result):
        r"""Sets the expect_result of this TestCaseStepInfo.

        预期结果

        :param expect_result: The expect_result of this TestCaseStepInfo.
        :type expect_result: str
        """
        self._expect_result = expect_result

    @property
    def step_actual(self):
        r"""Gets the step_actual of this TestCaseStepInfo.

        步骤的实际结果

        :return: The step_actual of this TestCaseStepInfo.
        :rtype: str
        """
        return self._step_actual

    @step_actual.setter
    def step_actual(self, step_actual):
        r"""Sets the step_actual of this TestCaseStepInfo.

        步骤的实际结果

        :param step_actual: The step_actual of this TestCaseStepInfo.
        :type step_actual: str
        """
        self._step_actual = step_actual

    @property
    def step_result(self):
        r"""Gets the step_result of this TestCaseStepInfo.

        步骤结果

        :return: The step_result of this TestCaseStepInfo.
        :rtype: str
        """
        return self._step_result

    @step_result.setter
    def step_result(self, step_result):
        r"""Sets the step_result of this TestCaseStepInfo.

        步骤结果

        :param step_result: The step_result of this TestCaseStepInfo.
        :type step_result: str
        """
        self._step_result = step_result

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
        if not isinstance(other, TestCaseStepInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
