# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuditRuleRiskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'risk_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'risk_id': 'risk_id'
    }

    def __init__(self, instance_id=None, risk_id=None):
        r"""ShowAuditRuleRiskRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。可在查询实例列表接口的ID字段获取。
        :type instance_id: str
        :param risk_id: 风险规则ID。可在查询风险规则策略接口的ID字段获取。
        :type risk_id: str
        """
        
        

        self._instance_id = None
        self._risk_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.risk_id = risk_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowAuditRuleRiskRequest.

        实例ID。可在查询实例列表接口的ID字段获取。

        :return: The instance_id of this ShowAuditRuleRiskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowAuditRuleRiskRequest.

        实例ID。可在查询实例列表接口的ID字段获取。

        :param instance_id: The instance_id of this ShowAuditRuleRiskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def risk_id(self):
        r"""Gets the risk_id of this ShowAuditRuleRiskRequest.

        风险规则ID。可在查询风险规则策略接口的ID字段获取。

        :return: The risk_id of this ShowAuditRuleRiskRequest.
        :rtype: str
        """
        return self._risk_id

    @risk_id.setter
    def risk_id(self, risk_id):
        r"""Sets the risk_id of this ShowAuditRuleRiskRequest.

        风险规则ID。可在查询风险规则策略接口的ID字段获取。

        :param risk_id: The risk_id of this ShowAuditRuleRiskRequest.
        :type risk_id: str
        """
        self._risk_id = risk_id

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
        if not isinstance(other, ShowAuditRuleRiskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
