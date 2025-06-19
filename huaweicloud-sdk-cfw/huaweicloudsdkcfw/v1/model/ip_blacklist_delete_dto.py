# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpBlacklistDeleteDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'effect_scope': 'list[int]'
    }

    attribute_map = {
        'effect_scope': 'effect_scope'
    }

    def __init__(self, effect_scope=None):
        r"""IpBlacklistDeleteDto

        The model defined in huaweicloud sdk

        :param effect_scope: 指定生效范围，1指定生效范围为EIP进行删除,2指定生效范围为NAT进行删除，1,2生效范围为EIP和NAT进行删除
        :type effect_scope: list[int]
        """
        
        

        self._effect_scope = None
        self.discriminator = None

        if effect_scope is not None:
            self.effect_scope = effect_scope

    @property
    def effect_scope(self):
        r"""Gets the effect_scope of this IpBlacklistDeleteDto.

        指定生效范围，1指定生效范围为EIP进行删除,2指定生效范围为NAT进行删除，1,2生效范围为EIP和NAT进行删除

        :return: The effect_scope of this IpBlacklistDeleteDto.
        :rtype: list[int]
        """
        return self._effect_scope

    @effect_scope.setter
    def effect_scope(self, effect_scope):
        r"""Sets the effect_scope of this IpBlacklistDeleteDto.

        指定生效范围，1指定生效范围为EIP进行删除,2指定生效范围为NAT进行删除，1,2生效范围为EIP和NAT进行删除

        :param effect_scope: The effect_scope of this IpBlacklistDeleteDto.
        :type effect_scope: list[int]
        """
        self._effect_scope = effect_scope

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
        if not isinstance(other, IpBlacklistDeleteDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
