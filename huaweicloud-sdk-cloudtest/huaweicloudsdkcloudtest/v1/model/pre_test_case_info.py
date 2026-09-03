# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreTestCaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_template': 'AlertTemplate',
        'enable': 'str',
        'test_cases': 'list[TestCaseBasicInfo]'
    }

    attribute_map = {
        'alert_template': 'alert_template',
        'enable': 'enable',
        'test_cases': 'testCases'
    }

    def __init__(self, alert_template=None, enable=None, test_cases=None):
        r"""PreTestCaseInfo

        The model defined in huaweicloud sdk

        :param alert_template: 
        :type alert_template: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        :param enable: 0 关闭，1开启
        :type enable: str
        :param test_cases: 用例列表
        :type test_cases: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseBasicInfo`]
        """
        
        

        self._alert_template = None
        self._enable = None
        self._test_cases = None
        self.discriminator = None

        if alert_template is not None:
            self.alert_template = alert_template
        if enable is not None:
            self.enable = enable
        if test_cases is not None:
            self.test_cases = test_cases

    @property
    def alert_template(self):
        r"""Gets the alert_template of this PreTestCaseInfo.

        :return: The alert_template of this PreTestCaseInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        """
        return self._alert_template

    @alert_template.setter
    def alert_template(self, alert_template):
        r"""Sets the alert_template of this PreTestCaseInfo.

        :param alert_template: The alert_template of this PreTestCaseInfo.
        :type alert_template: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        """
        self._alert_template = alert_template

    @property
    def enable(self):
        r"""Gets the enable of this PreTestCaseInfo.

        0 关闭，1开启

        :return: The enable of this PreTestCaseInfo.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this PreTestCaseInfo.

        0 关闭，1开启

        :param enable: The enable of this PreTestCaseInfo.
        :type enable: str
        """
        self._enable = enable

    @property
    def test_cases(self):
        r"""Gets the test_cases of this PreTestCaseInfo.

        用例列表

        :return: The test_cases of this PreTestCaseInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseBasicInfo`]
        """
        return self._test_cases

    @test_cases.setter
    def test_cases(self, test_cases):
        r"""Sets the test_cases of this PreTestCaseInfo.

        用例列表

        :param test_cases: The test_cases of this PreTestCaseInfo.
        :type test_cases: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseBasicInfo`]
        """
        self._test_cases = test_cases

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PreTestCaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
