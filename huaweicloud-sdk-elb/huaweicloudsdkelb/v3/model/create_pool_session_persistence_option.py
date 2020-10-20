# coding: utf-8

import pprint
import re

import six





class CreatePoolSessionPersistenceOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cookie_name': 'str',
        'type': 'str',
        'persistence_timeout': 'int'
    }

    attribute_map = {
        'cookie_name': 'cookie_name',
        'type': 'type',
        'persistence_timeout': 'persistence_timeout'
    }

    def __init__(self, cookie_name=None, type=None, persistence_timeout=None):
        """CreatePoolSessionPersistenceOption - a model defined in huaweicloud sdk"""
        
        

        self._cookie_name = None
        self._type = None
        self._persistence_timeout = None
        self.discriminator = None

        if cookie_name is not None:
            self.cookie_name = cookie_name
        self.type = type
        if persistence_timeout is not None:
            self.persistence_timeout = persistence_timeout

    @property
    def cookie_name(self):
        """Gets the cookie_name of this CreatePoolSessionPersistenceOption.

        cookie名称。 只有当type为APP_COOKIE时才支持。 格式要求：仅支持字母数字-_. 

        :return: The cookie_name of this CreatePoolSessionPersistenceOption.
        :rtype: str
        """
        return self._cookie_name

    @cookie_name.setter
    def cookie_name(self, cookie_name):
        """Sets the cookie_name of this CreatePoolSessionPersistenceOption.

        cookie名称。 只有当type为APP_COOKIE时才支持。 格式要求：仅支持字母数字-_. 

        :param cookie_name: The cookie_name of this CreatePoolSessionPersistenceOption.
        :type: str
        """
        self._cookie_name = cookie_name

    @property
    def type(self):
        """Gets the type of this CreatePoolSessionPersistenceOption.

        描述：类型，可以为SOURCE_IP、HTTP_COOKIE、APP_COOKIE。   约束：   1、当pool的protocol为TCP、UDP、QUIC时，只按SOURCE_IP生效；   2、当pool的protocol为HTTP、HTTPS时，只按HTTP_COOKIE、APP_COOKIE生效。  

        :return: The type of this CreatePoolSessionPersistenceOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreatePoolSessionPersistenceOption.

        描述：类型，可以为SOURCE_IP、HTTP_COOKIE、APP_COOKIE。   约束：   1、当pool的protocol为TCP、UDP、QUIC时，只按SOURCE_IP生效；   2、当pool的protocol为HTTP、HTTPS时，只按HTTP_COOKIE、APP_COOKIE生效。  

        :param type: The type of this CreatePoolSessionPersistenceOption.
        :type: str
        """
        self._type = type

    @property
    def persistence_timeout(self):
        """Gets the persistence_timeout of this CreatePoolSessionPersistenceOption.

        会话保持的时间。当type为APP_COOKIE时不生效。 适用范围：如果pool的protocol为TCP、UDP和QUIC则范围为[1,60]（分钟），默认值1；如果pool的protocol为HTTP和HTTPS则范围为[1,1440]（分钟），默认值1440。

        :return: The persistence_timeout of this CreatePoolSessionPersistenceOption.
        :rtype: int
        """
        return self._persistence_timeout

    @persistence_timeout.setter
    def persistence_timeout(self, persistence_timeout):
        """Sets the persistence_timeout of this CreatePoolSessionPersistenceOption.

        会话保持的时间。当type为APP_COOKIE时不生效。 适用范围：如果pool的protocol为TCP、UDP和QUIC则范围为[1,60]（分钟），默认值1；如果pool的protocol为HTTP和HTTPS则范围为[1,1440]（分钟），默认值1440。

        :param persistence_timeout: The persistence_timeout of this CreatePoolSessionPersistenceOption.
        :type: int
        """
        self._persistence_timeout = persistence_timeout

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreatePoolSessionPersistenceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
