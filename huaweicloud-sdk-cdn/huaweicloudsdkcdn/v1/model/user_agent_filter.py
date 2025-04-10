# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserAgentFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'value': 'str',
        'ua_list': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'ua_list': 'ua_list'
    }

    def __init__(self, type=None, value=None, ua_list=None):
        r"""UserAgentFilter

        The model defined in huaweicloud sdk

        :param type: UA黑白名单类型 off：关闭UA黑白名单; black：UA黑名单; white：UA白名单;
        :type type: str
        :param value: 配置UA黑白名单，当type&#x3D;off时，非必传。最多配置10条规则，单条规则不超过100个字符，多条规则用“,”分割。
        :type value: str
        :param ua_list: 配置UA黑白名单，当type&#x3D;off时，非必传。最多配置10条规则，单条规则不超过100个字符,同时配置value和ua_list时，ua_list生效。 
        :type ua_list: list[str]
        """
        
        

        self._type = None
        self._value = None
        self._ua_list = None
        self.discriminator = None

        self.type = type
        if value is not None:
            self.value = value
        if ua_list is not None:
            self.ua_list = ua_list

    @property
    def type(self):
        r"""Gets the type of this UserAgentFilter.

        UA黑白名单类型 off：关闭UA黑白名单; black：UA黑名单; white：UA白名单;

        :return: The type of this UserAgentFilter.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UserAgentFilter.

        UA黑白名单类型 off：关闭UA黑白名单; black：UA黑名单; white：UA白名单;

        :param type: The type of this UserAgentFilter.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this UserAgentFilter.

        配置UA黑白名单，当type=off时，非必传。最多配置10条规则，单条规则不超过100个字符，多条规则用“,”分割。

        :return: The value of this UserAgentFilter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this UserAgentFilter.

        配置UA黑白名单，当type=off时，非必传。最多配置10条规则，单条规则不超过100个字符，多条规则用“,”分割。

        :param value: The value of this UserAgentFilter.
        :type value: str
        """
        self._value = value

    @property
    def ua_list(self):
        r"""Gets the ua_list of this UserAgentFilter.

        配置UA黑白名单，当type=off时，非必传。最多配置10条规则，单条规则不超过100个字符,同时配置value和ua_list时，ua_list生效。 

        :return: The ua_list of this UserAgentFilter.
        :rtype: list[str]
        """
        return self._ua_list

    @ua_list.setter
    def ua_list(self, ua_list):
        r"""Sets the ua_list of this UserAgentFilter.

        配置UA黑白名单，当type=off时，非必传。最多配置10条规则，单条规则不超过100个字符,同时配置value和ua_list时，ua_list生效。 

        :param ua_list: The ua_list of this UserAgentFilter.
        :type ua_list: list[str]
        """
        self._ua_list = ua_list

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
        if not isinstance(other, UserAgentFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
