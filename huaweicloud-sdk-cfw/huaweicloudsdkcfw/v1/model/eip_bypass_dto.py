# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EipBypassDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bypass_operation': 'int'
    }

    attribute_map = {
        'bypass_operation': 'bypass_operation'
    }

    def __init__(self, bypass_operation=None):
        r"""EipBypassDto

        The model defined in huaweicloud sdk

        :param bypass_operation: 防护操作类型，1表示一键关闭防护，0表示一键恢复防护
        :type bypass_operation: int
        """
        
        

        self._bypass_operation = None
        self.discriminator = None

        self.bypass_operation = bypass_operation

    @property
    def bypass_operation(self):
        r"""Gets the bypass_operation of this EipBypassDto.

        防护操作类型，1表示一键关闭防护，0表示一键恢复防护

        :return: The bypass_operation of this EipBypassDto.
        :rtype: int
        """
        return self._bypass_operation

    @bypass_operation.setter
    def bypass_operation(self, bypass_operation):
        r"""Sets the bypass_operation of this EipBypassDto.

        防护操作类型，1表示一键关闭防护，0表示一键恢复防护

        :param bypass_operation: The bypass_operation of this EipBypassDto.
        :type bypass_operation: int
        """
        self._bypass_operation = bypass_operation

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
        if not isinstance(other, EipBypassDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
