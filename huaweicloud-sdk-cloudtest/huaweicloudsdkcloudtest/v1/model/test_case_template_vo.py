# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseTemplateVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_template_id': 'str',
        'testcase_id': 'str'
    }

    attribute_map = {
        'alert_template_id': 'alertTemplateId',
        'testcase_id': 'testcase_id'
    }

    def __init__(self, alert_template_id=None, testcase_id=None):
        r"""TestCaseTemplateVo

        The model defined in huaweicloud sdk

        :param alert_template_id: 用例对应的告警模板id
        :type alert_template_id: str
        :param testcase_id: 测试用例id
        :type testcase_id: str
        """
        
        

        self._alert_template_id = None
        self._testcase_id = None
        self.discriminator = None

        if alert_template_id is not None:
            self.alert_template_id = alert_template_id
        if testcase_id is not None:
            self.testcase_id = testcase_id

    @property
    def alert_template_id(self):
        r"""Gets the alert_template_id of this TestCaseTemplateVo.

        用例对应的告警模板id

        :return: The alert_template_id of this TestCaseTemplateVo.
        :rtype: str
        """
        return self._alert_template_id

    @alert_template_id.setter
    def alert_template_id(self, alert_template_id):
        r"""Sets the alert_template_id of this TestCaseTemplateVo.

        用例对应的告警模板id

        :param alert_template_id: The alert_template_id of this TestCaseTemplateVo.
        :type alert_template_id: str
        """
        self._alert_template_id = alert_template_id

    @property
    def testcase_id(self):
        r"""Gets the testcase_id of this TestCaseTemplateVo.

        测试用例id

        :return: The testcase_id of this TestCaseTemplateVo.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        r"""Sets the testcase_id of this TestCaseTemplateVo.

        测试用例id

        :param testcase_id: The testcase_id of this TestCaseTemplateVo.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

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
        if not isinstance(other, TestCaseTemplateVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
