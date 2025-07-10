# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigRuleCompliance:

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
        'region': 'str',
        'control_id': 'str'
    }

    attribute_map = {
        'rule_name': 'rule_name',
        'status': 'status',
        'region': 'region',
        'control_id': 'control_id'
    }

    def __init__(self, rule_name=None, status=None, region=None, control_id=None):
        r"""ConfigRuleCompliance

        The model defined in huaweicloud sdk

        :param rule_name: 合规规则。
        :type rule_name: str
        :param status: 合规状态。
        :type status: str
        :param region: 区域信息。
        :type region: str
        :param control_id: 控制策略ID。
        :type control_id: str
        """
        
        

        self._rule_name = None
        self._status = None
        self._region = None
        self._control_id = None
        self.discriminator = None

        if rule_name is not None:
            self.rule_name = rule_name
        if status is not None:
            self.status = status
        if region is not None:
            self.region = region
        if control_id is not None:
            self.control_id = control_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this ConfigRuleCompliance.

        合规规则。

        :return: The rule_name of this ConfigRuleCompliance.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this ConfigRuleCompliance.

        合规规则。

        :param rule_name: The rule_name of this ConfigRuleCompliance.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def status(self):
        r"""Gets the status of this ConfigRuleCompliance.

        合规状态。

        :return: The status of this ConfigRuleCompliance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ConfigRuleCompliance.

        合规状态。

        :param status: The status of this ConfigRuleCompliance.
        :type status: str
        """
        self._status = status

    @property
    def region(self):
        r"""Gets the region of this ConfigRuleCompliance.

        区域信息。

        :return: The region of this ConfigRuleCompliance.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ConfigRuleCompliance.

        区域信息。

        :param region: The region of this ConfigRuleCompliance.
        :type region: str
        """
        self._region = region

    @property
    def control_id(self):
        r"""Gets the control_id of this ConfigRuleCompliance.

        控制策略ID。

        :return: The control_id of this ConfigRuleCompliance.
        :rtype: str
        """
        return self._control_id

    @control_id.setter
    def control_id(self, control_id):
        r"""Sets the control_id of this ConfigRuleCompliance.

        控制策略ID。

        :param control_id: The control_id of this ConfigRuleCompliance.
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
        if not isinstance(other, ConfigRuleCompliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
