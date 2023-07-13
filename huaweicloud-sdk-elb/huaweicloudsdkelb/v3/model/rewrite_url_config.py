# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RewriteUrlConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host': 'str',
        'path': 'str',
        'query': 'str'
    }

    attribute_map = {
        'host': 'host',
        'path': 'path',
        'query': 'query'
    }

    def __init__(self, host=None, path=None, query=None):
        """RewriteUrlConfig

        The model defined in huaweicloud sdk

        :param host: url host
        :type host: str
        :param path: url路径
        :type path: str
        :param query: url查询字符串
        :type query: str
        """
        
        

        self._host = None
        self._path = None
        self._query = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if path is not None:
            self.path = path
        if query is not None:
            self.query = query

    @property
    def host(self):
        """Gets the host of this RewriteUrlConfig.

        url host

        :return: The host of this RewriteUrlConfig.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this RewriteUrlConfig.

        url host

        :param host: The host of this RewriteUrlConfig.
        :type host: str
        """
        self._host = host

    @property
    def path(self):
        """Gets the path of this RewriteUrlConfig.

        url路径

        :return: The path of this RewriteUrlConfig.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this RewriteUrlConfig.

        url路径

        :param path: The path of this RewriteUrlConfig.
        :type path: str
        """
        self._path = path

    @property
    def query(self):
        """Gets the query of this RewriteUrlConfig.

        url查询字符串

        :return: The query of this RewriteUrlConfig.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this RewriteUrlConfig.

        url查询字符串

        :param query: The query of this RewriteUrlConfig.
        :type query: str
        """
        self._query = query

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
        if not isinstance(other, RewriteUrlConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
