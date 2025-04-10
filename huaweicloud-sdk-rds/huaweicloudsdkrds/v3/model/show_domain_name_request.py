# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainNameRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'dns_type': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'dns_type': 'dns_type',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, dns_type=None, x_language=None):
        r"""ShowDomainNameRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param dns_type: 实例域名类型，当前只支持private。
        :type dns_type: str
        :param x_language: 语言
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._dns_type = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.dns_type = dns_type
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowDomainNameRequest.

        实例ID。

        :return: The instance_id of this ShowDomainNameRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowDomainNameRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowDomainNameRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def dns_type(self):
        r"""Gets the dns_type of this ShowDomainNameRequest.

        实例域名类型，当前只支持private。

        :return: The dns_type of this ShowDomainNameRequest.
        :rtype: str
        """
        return self._dns_type

    @dns_type.setter
    def dns_type(self, dns_type):
        r"""Sets the dns_type of this ShowDomainNameRequest.

        实例域名类型，当前只支持private。

        :param dns_type: The dns_type of this ShowDomainNameRequest.
        :type dns_type: str
        """
        self._dns_type = dns_type

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowDomainNameRequest.

        语言

        :return: The x_language of this ShowDomainNameRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowDomainNameRequest.

        语言

        :param x_language: The x_language of this ShowDomainNameRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowDomainNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
