# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Authentification:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_name': 'str',
        'record_type': 'str',
        'record_value': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'record_name': 'record_name',
        'record_type': 'record_type',
        'record_value': 'record_value',
        'domain': 'domain'
    }

    def __init__(self, record_name=None, record_type=None, record_value=None, domain=None):
        """Authentification

        The model defined in huaweicloud sdk

        :param record_name: 域名校验值名字。
        :type record_name: str
        :param record_type: 域名校验值类型。
        :type record_type: str
        :param record_value: 域名校验值。
        :type record_value: str
        :param domain: 校验值对应的域名。
        :type domain: str
        """
        
        

        self._record_name = None
        self._record_type = None
        self._record_value = None
        self._domain = None
        self.discriminator = None

        if record_name is not None:
            self.record_name = record_name
        if record_type is not None:
            self.record_type = record_type
        if record_value is not None:
            self.record_value = record_value
        if domain is not None:
            self.domain = domain

    @property
    def record_name(self):
        """Gets the record_name of this Authentification.

        域名校验值名字。

        :return: The record_name of this Authentification.
        :rtype: str
        """
        return self._record_name

    @record_name.setter
    def record_name(self, record_name):
        """Sets the record_name of this Authentification.

        域名校验值名字。

        :param record_name: The record_name of this Authentification.
        :type record_name: str
        """
        self._record_name = record_name

    @property
    def record_type(self):
        """Gets the record_type of this Authentification.

        域名校验值类型。

        :return: The record_type of this Authentification.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this Authentification.

        域名校验值类型。

        :param record_type: The record_type of this Authentification.
        :type record_type: str
        """
        self._record_type = record_type

    @property
    def record_value(self):
        """Gets the record_value of this Authentification.

        域名校验值。

        :return: The record_value of this Authentification.
        :rtype: str
        """
        return self._record_value

    @record_value.setter
    def record_value(self, record_value):
        """Sets the record_value of this Authentification.

        域名校验值。

        :param record_value: The record_value of this Authentification.
        :type record_value: str
        """
        self._record_value = record_value

    @property
    def domain(self):
        """Gets the domain of this Authentification.

        校验值对应的域名。

        :return: The domain of this Authentification.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Authentification.

        校验值对应的域名。

        :param domain: The domain of this Authentification.
        :type domain: str
        """
        self._domain = domain

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
        if not isinstance(other, Authentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
