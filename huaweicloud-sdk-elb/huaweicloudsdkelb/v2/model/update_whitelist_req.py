# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWhitelistReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_whitelist': 'bool',
        'whitelist': 'str'
    }

    attribute_map = {
        'enable_whitelist': 'enable_whitelist',
        'whitelist': 'whitelist'
    }

    def __init__(self, enable_whitelist=None, whitelist=None):
        """UpdateWhitelistReq

        The model defined in huaweicloud sdk

        :param enable_whitelist: 是否开启白名单访问控制开关。true：开启；false：关闭
        :type enable_whitelist: bool
        :param whitelist: 白名单IP列表。可以是ip，例如192.168.10.123；也可以是一个网段，例如192.168.10.1/24；不同的值之间用逗号分隔
        :type whitelist: str
        """
        
        

        self._enable_whitelist = None
        self._whitelist = None
        self.discriminator = None

        if enable_whitelist is not None:
            self.enable_whitelist = enable_whitelist
        if whitelist is not None:
            self.whitelist = whitelist

    @property
    def enable_whitelist(self):
        """Gets the enable_whitelist of this UpdateWhitelistReq.

        是否开启白名单访问控制开关。true：开启；false：关闭

        :return: The enable_whitelist of this UpdateWhitelistReq.
        :rtype: bool
        """
        return self._enable_whitelist

    @enable_whitelist.setter
    def enable_whitelist(self, enable_whitelist):
        """Sets the enable_whitelist of this UpdateWhitelistReq.

        是否开启白名单访问控制开关。true：开启；false：关闭

        :param enable_whitelist: The enable_whitelist of this UpdateWhitelistReq.
        :type enable_whitelist: bool
        """
        self._enable_whitelist = enable_whitelist

    @property
    def whitelist(self):
        """Gets the whitelist of this UpdateWhitelistReq.

        白名单IP列表。可以是ip，例如192.168.10.123；也可以是一个网段，例如192.168.10.1/24；不同的值之间用逗号分隔

        :return: The whitelist of this UpdateWhitelistReq.
        :rtype: str
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this UpdateWhitelistReq.

        白名单IP列表。可以是ip，例如192.168.10.123；也可以是一个网段，例如192.168.10.1/24；不同的值之间用逗号分隔

        :param whitelist: The whitelist of this UpdateWhitelistReq.
        :type whitelist: str
        """
        self._whitelist = whitelist

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
        if not isinstance(other, UpdateWhitelistReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
