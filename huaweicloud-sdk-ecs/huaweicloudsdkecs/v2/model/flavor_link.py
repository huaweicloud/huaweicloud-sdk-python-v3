# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorLink:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'href': 'str',
        'rel': 'str',
        'type': 'str'
    }

    attribute_map = {
        'href': 'href',
        'rel': 'rel',
        'type': 'type'
    }

    def __init__(self, href=None, rel=None, type=None):
        """FlavorLink

        The model defined in huaweicloud sdk

        :param href: 对应快捷链接。
        :type href: str
        :param rel: 快捷链接标记名称。
        :type rel: str
        :param type: 快捷链接类型，当前接口未使用，缺省值为null。
        :type type: str
        """
        
        

        self._href = None
        self._rel = None
        self._type = None
        self.discriminator = None

        self.href = href
        self.rel = rel
        self.type = type

    @property
    def href(self):
        """Gets the href of this FlavorLink.

        对应快捷链接。

        :return: The href of this FlavorLink.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this FlavorLink.

        对应快捷链接。

        :param href: The href of this FlavorLink.
        :type href: str
        """
        self._href = href

    @property
    def rel(self):
        """Gets the rel of this FlavorLink.

        快捷链接标记名称。

        :return: The rel of this FlavorLink.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this FlavorLink.

        快捷链接标记名称。

        :param rel: The rel of this FlavorLink.
        :type rel: str
        """
        self._rel = rel

    @property
    def type(self):
        """Gets the type of this FlavorLink.

        快捷链接类型，当前接口未使用，缺省值为null。

        :return: The type of this FlavorLink.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FlavorLink.

        快捷链接类型，当前接口未使用，缺省值为null。

        :param type: The type of this FlavorLink.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, FlavorLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
