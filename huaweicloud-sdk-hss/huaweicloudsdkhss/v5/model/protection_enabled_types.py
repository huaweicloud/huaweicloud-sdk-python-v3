# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectionEnabledTypes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_type': 'str'
    }

    attribute_map = {
        'protect_type': 'protect_type'
    }

    def __init__(self, protect_type=None):
        r"""ProtectionEnabledTypes

        The model defined in huaweicloud sdk

        :param protect_type: **参数解释**: 防护类型 **取值范围**: - host：主机 - container：容器 - application：应用 - serverless：Serverless 
        :type protect_type: str
        """
        
        

        self._protect_type = None
        self.discriminator = None

        if protect_type is not None:
            self.protect_type = protect_type

    @property
    def protect_type(self):
        r"""Gets the protect_type of this ProtectionEnabledTypes.

        **参数解释**: 防护类型 **取值范围**: - host：主机 - container：容器 - application：应用 - serverless：Serverless 

        :return: The protect_type of this ProtectionEnabledTypes.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        r"""Sets the protect_type of this ProtectionEnabledTypes.

        **参数解释**: 防护类型 **取值范围**: - host：主机 - container：容器 - application：应用 - serverless：Serverless 

        :param protect_type: The protect_type of this ProtectionEnabledTypes.
        :type protect_type: str
        """
        self._protect_type = protect_type

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
        if not isinstance(other, ProtectionEnabledTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
