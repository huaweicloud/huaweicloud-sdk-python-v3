# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalConfigRuleCompliance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_name': 'str',
        'status': 'str',
        'control_id': 'str'
    }

    attribute_map = {
        'rule_name': 'rule_name',
        'status': 'status',
        'control_id': 'control_id'
    }

    def __init__(self, rule_name=None, status=None, control_id=None):
        r"""ExternalConfigRuleCompliance

        The model defined in huaweicloud sdk

        :param rule_name: 合规规则。
        :type rule_name: str
        :param status: 合规状态。
        :type status: str
        :param control_id: 外部规则ID。
        :type control_id: str
        """
        
        

        self._rule_name = None
        self._status = None
        self._control_id = None
        self.discriminator = None

        if rule_name is not None:
            self.rule_name = rule_name
        if status is not None:
            self.status = status
        if control_id is not None:
            self.control_id = control_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this ExternalConfigRuleCompliance.

        合规规则。

        :return: The rule_name of this ExternalConfigRuleCompliance.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this ExternalConfigRuleCompliance.

        合规规则。

        :param rule_name: The rule_name of this ExternalConfigRuleCompliance.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def status(self):
        r"""Gets the status of this ExternalConfigRuleCompliance.

        合规状态。

        :return: The status of this ExternalConfigRuleCompliance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExternalConfigRuleCompliance.

        合规状态。

        :param status: The status of this ExternalConfigRuleCompliance.
        :type status: str
        """
        self._status = status

    @property
    def control_id(self):
        r"""Gets the control_id of this ExternalConfigRuleCompliance.

        外部规则ID。

        :return: The control_id of this ExternalConfigRuleCompliance.
        :rtype: str
        """
        return self._control_id

    @control_id.setter
    def control_id(self, control_id):
        r"""Sets the control_id of this ExternalConfigRuleCompliance.

        外部规则ID。

        :param control_id: The control_id of this ExternalConfigRuleCompliance.
        :type control_id: str
        """
        self._control_id = control_id

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
        if not isinstance(other, ExternalConfigRuleCompliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
