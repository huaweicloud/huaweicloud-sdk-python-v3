# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeExtendedWeakPasswordRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extended_weak_password': 'list[str]'
    }

    attribute_map = {
        'extended_weak_password': 'extended_weak_password'
    }

    def __init__(self, extended_weak_password=None):
        r"""ChangeExtendedWeakPasswordRequestInfo

        The model defined in huaweicloud sdk

        :param extended_weak_password: **参数解释**: 自定义弱口令，选填，可编辑 **取值范围**: 最小值0，最大值300 
        :type extended_weak_password: list[str]
        """
        
        

        self._extended_weak_password = None
        self.discriminator = None

        if extended_weak_password is not None:
            self.extended_weak_password = extended_weak_password

    @property
    def extended_weak_password(self):
        r"""Gets the extended_weak_password of this ChangeExtendedWeakPasswordRequestInfo.

        **参数解释**: 自定义弱口令，选填，可编辑 **取值范围**: 最小值0，最大值300 

        :return: The extended_weak_password of this ChangeExtendedWeakPasswordRequestInfo.
        :rtype: list[str]
        """
        return self._extended_weak_password

    @extended_weak_password.setter
    def extended_weak_password(self, extended_weak_password):
        r"""Sets the extended_weak_password of this ChangeExtendedWeakPasswordRequestInfo.

        **参数解释**: 自定义弱口令，选填，可编辑 **取值范围**: 最小值0，最大值300 

        :param extended_weak_password: The extended_weak_password of this ChangeExtendedWeakPasswordRequestInfo.
        :type extended_weak_password: list[str]
        """
        self._extended_weak_password = extended_weak_password

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
        if not isinstance(other, ChangeExtendedWeakPasswordRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
