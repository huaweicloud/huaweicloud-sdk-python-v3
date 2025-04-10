# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigNasTarget:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, name=None, type=None, url=None):
        r"""ConfigNasTarget

        The model defined in huaweicloud sdk

        :param name: nas 配置名
        :type name: str
        :param type: nas 配置协议类型
        :type type: str
        :param url: nas 配置 ip
        :type url: str
        """
        
        

        self._name = None
        self._type = None
        self._url = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.url = url

    @property
    def name(self):
        r"""Gets the name of this ConfigNasTarget.

        nas 配置名

        :return: The name of this ConfigNasTarget.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConfigNasTarget.

        nas 配置名

        :param name: The name of this ConfigNasTarget.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ConfigNasTarget.

        nas 配置协议类型

        :return: The type of this ConfigNasTarget.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConfigNasTarget.

        nas 配置协议类型

        :param type: The type of this ConfigNasTarget.
        :type type: str
        """
        self._type = type

    @property
    def url(self):
        r"""Gets the url of this ConfigNasTarget.

        nas 配置 ip

        :return: The url of this ConfigNasTarget.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ConfigNasTarget.

        nas 配置 ip

        :param url: The url of this ConfigNasTarget.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, ConfigNasTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
