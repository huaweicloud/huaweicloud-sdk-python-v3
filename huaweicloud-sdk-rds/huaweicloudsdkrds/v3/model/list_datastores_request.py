# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatastoresRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'database_name': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'database_name': 'database_name'
    }

    def __init__(self, x_language=None, database_name=None):
        """ListDatastoresRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param database_name: 数据库引擎。支持的引擎如下，不区分大小写： MySQL PostgreSQL SQLServer
        :type database_name: str
        """
        
        

        self._x_language = None
        self._database_name = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.database_name = database_name

    @property
    def x_language(self):
        """Gets the x_language of this ListDatastoresRequest.

        语言

        :return: The x_language of this ListDatastoresRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListDatastoresRequest.

        语言

        :param x_language: The x_language of this ListDatastoresRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def database_name(self):
        """Gets the database_name of this ListDatastoresRequest.

        数据库引擎。支持的引擎如下，不区分大小写： MySQL PostgreSQL SQLServer

        :return: The database_name of this ListDatastoresRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListDatastoresRequest.

        数据库引擎。支持的引擎如下，不区分大小写： MySQL PostgreSQL SQLServer

        :param database_name: The database_name of this ListDatastoresRequest.
        :type database_name: str
        """
        self._database_name = database_name

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
        if not isinstance(other, ListDatastoresRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
