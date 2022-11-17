# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRdsInstanceAliasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alias': 'str'
    }

    attribute_map = {
        'alias': 'alias'
    }

    def __init__(self, alias=None):
        """UpdateRdsInstanceAliasRequest

        The model defined in huaweicloud sdk

        :param alias: 长度可在0~64个字符之间，由字母、数字、汉字、英文句号、下划线、中划线组成。
        :type alias: str
        """
        
        

        self._alias = None
        self.discriminator = None

        self.alias = alias

    @property
    def alias(self):
        """Gets the alias of this UpdateRdsInstanceAliasRequest.

        长度可在0~64个字符之间，由字母、数字、汉字、英文句号、下划线、中划线组成。

        :return: The alias of this UpdateRdsInstanceAliasRequest.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this UpdateRdsInstanceAliasRequest.

        长度可在0~64个字符之间，由字母、数字、汉字、英文句号、下划线、中划线组成。

        :param alias: The alias of this UpdateRdsInstanceAliasRequest.
        :type alias: str
        """
        self._alias = alias

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
        if not isinstance(other, UpdateRdsInstanceAliasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
