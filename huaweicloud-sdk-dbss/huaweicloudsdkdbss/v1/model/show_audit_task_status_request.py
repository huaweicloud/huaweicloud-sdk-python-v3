# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuditTaskStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'busi_type': 'str'
    }

    attribute_map = {
        'busi_type': 'busi_type'
    }

    def __init__(self, busi_type=None):
        r"""ShowAuditTaskStatusRequest

        The model defined in huaweicloud sdk

        :param busi_type: **参数解释**： 业务类型。 **约束限制**： 不涉及 **取值范围**：   - audit：审计实例    - risk：风险 **默认取值**： 不涉及 
        :type busi_type: str
        """
        
        

        self._busi_type = None
        self.discriminator = None

        self.busi_type = busi_type

    @property
    def busi_type(self):
        r"""Gets the busi_type of this ShowAuditTaskStatusRequest.

        **参数解释**： 业务类型。 **约束限制**： 不涉及 **取值范围**：   - audit：审计实例    - risk：风险 **默认取值**： 不涉及 

        :return: The busi_type of this ShowAuditTaskStatusRequest.
        :rtype: str
        """
        return self._busi_type

    @busi_type.setter
    def busi_type(self, busi_type):
        r"""Sets the busi_type of this ShowAuditTaskStatusRequest.

        **参数解释**： 业务类型。 **约束限制**： 不涉及 **取值范围**：   - audit：审计实例    - risk：风险 **默认取值**： 不涉及 

        :param busi_type: The busi_type of this ShowAuditTaskStatusRequest.
        :type busi_type: str
        """
        self._busi_type = busi_type

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
        if not isinstance(other, ShowAuditTaskStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
