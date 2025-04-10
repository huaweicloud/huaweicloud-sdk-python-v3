# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditRuleRisksRequest:

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
        'name': 'str',
        'risk_levels': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'name': 'name',
        'risk_levels': 'risk_levels'
    }

    def __init__(self, instance_id=None, name=None, risk_levels=None):
        r"""ListAuditRuleRisksRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。可在查询实例列表接口的ID字段获取。
        :type instance_id: str
        :param name: 风险名称
        :type name: str
        :param risk_levels: 风险级别 - LOW - MEDIUM - HIGH - NO_RISK
        :type risk_levels: str
        """
        
        

        self._instance_id = None
        self._name = None
        self._risk_levels = None
        self.discriminator = None

        self.instance_id = instance_id
        if name is not None:
            self.name = name
        if risk_levels is not None:
            self.risk_levels = risk_levels

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListAuditRuleRisksRequest.

        实例ID。可在查询实例列表接口的ID字段获取。

        :return: The instance_id of this ListAuditRuleRisksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListAuditRuleRisksRequest.

        实例ID。可在查询实例列表接口的ID字段获取。

        :param instance_id: The instance_id of this ListAuditRuleRisksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this ListAuditRuleRisksRequest.

        风险名称

        :return: The name of this ListAuditRuleRisksRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAuditRuleRisksRequest.

        风险名称

        :param name: The name of this ListAuditRuleRisksRequest.
        :type name: str
        """
        self._name = name

    @property
    def risk_levels(self):
        r"""Gets the risk_levels of this ListAuditRuleRisksRequest.

        风险级别 - LOW - MEDIUM - HIGH - NO_RISK

        :return: The risk_levels of this ListAuditRuleRisksRequest.
        :rtype: str
        """
        return self._risk_levels

    @risk_levels.setter
    def risk_levels(self, risk_levels):
        r"""Sets the risk_levels of this ListAuditRuleRisksRequest.

        风险级别 - LOW - MEDIUM - HIGH - NO_RISK

        :param risk_levels: The risk_levels of this ListAuditRuleRisksRequest.
        :type risk_levels: str
        """
        self._risk_levels = risk_levels

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
        if not isinstance(other, ListAuditRuleRisksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
