# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRewriteUrlConfig:

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
        """CreateRewriteUrlConfig

        The model defined in huaweicloud sdk

        :param host: url重写的主机名。字符串只能包含英文字母、数字、“-”、“.”，必须以字母、数字开头。默认值${host}表示继承原值（即与被重写请求保持一致）。
        :type host: str
        :param path: url重定向的路径。默认值${path}表示继承原值（即与被重写请求保持一致）。 只能包含英文字母、数字、_~&#39;;@^-%#&amp;$.*+?,&#x3D;!:|\\/()，且必须以\&quot;/\&quot;开头。其中$1-$9会匹配请求url通配符星号(*)，当正则匹配分组小于指定数字，则$指定数字结果为空。$后面跟字母，匹配结果均为空，直到下一个特殊字符出现，例如$abc#123，则匹配结果为#123；$后面跟特殊字符则直接输出特殊字符，例如$#匹配结果为$#.
        :type path: str
        :param query: url重定向的查询字符串。默认${query}表示继承原值（即与被重写请求保持一致）。 只能包含英文字母、数字和特殊字符：!$&amp;&#39;()*+,-./:;&#x3D;?@^_&#x60;。字母区分大小写。其中$1-$9会匹配请求url通配符星号（*），当正则匹配分组小于指定数字，则$指定数字结果为空。$后面跟字母，匹配结果均为空，直到下一个特殊字符出现，例如$abc#123，则匹配结果为#123；$后面跟特殊字符则直接输出特殊字符，例如$#匹配结果为$#
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
        """Gets the host of this CreateRewriteUrlConfig.

        url重写的主机名。字符串只能包含英文字母、数字、“-”、“.”，必须以字母、数字开头。默认值${host}表示继承原值（即与被重写请求保持一致）。

        :return: The host of this CreateRewriteUrlConfig.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CreateRewriteUrlConfig.

        url重写的主机名。字符串只能包含英文字母、数字、“-”、“.”，必须以字母、数字开头。默认值${host}表示继承原值（即与被重写请求保持一致）。

        :param host: The host of this CreateRewriteUrlConfig.
        :type host: str
        """
        self._host = host

    @property
    def path(self):
        """Gets the path of this CreateRewriteUrlConfig.

        url重定向的路径。默认值${path}表示继承原值（即与被重写请求保持一致）。 只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:|\\/()，且必须以\"/\"开头。其中$1-$9会匹配请求url通配符星号(*)，当正则匹配分组小于指定数字，则$指定数字结果为空。$后面跟字母，匹配结果均为空，直到下一个特殊字符出现，例如$abc#123，则匹配结果为#123；$后面跟特殊字符则直接输出特殊字符，例如$#匹配结果为$#.

        :return: The path of this CreateRewriteUrlConfig.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CreateRewriteUrlConfig.

        url重定向的路径。默认值${path}表示继承原值（即与被重写请求保持一致）。 只能包含英文字母、数字、_~';@^-%#&$.*+?,=!:|\\/()，且必须以\"/\"开头。其中$1-$9会匹配请求url通配符星号(*)，当正则匹配分组小于指定数字，则$指定数字结果为空。$后面跟字母，匹配结果均为空，直到下一个特殊字符出现，例如$abc#123，则匹配结果为#123；$后面跟特殊字符则直接输出特殊字符，例如$#匹配结果为$#.

        :param path: The path of this CreateRewriteUrlConfig.
        :type path: str
        """
        self._path = path

    @property
    def query(self):
        """Gets the query of this CreateRewriteUrlConfig.

        url重定向的查询字符串。默认${query}表示继承原值（即与被重写请求保持一致）。 只能包含英文字母、数字和特殊字符：!$&'()*+,-./:;=?@^_`。字母区分大小写。其中$1-$9会匹配请求url通配符星号（*），当正则匹配分组小于指定数字，则$指定数字结果为空。$后面跟字母，匹配结果均为空，直到下一个特殊字符出现，例如$abc#123，则匹配结果为#123；$后面跟特殊字符则直接输出特殊字符，例如$#匹配结果为$#

        :return: The query of this CreateRewriteUrlConfig.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this CreateRewriteUrlConfig.

        url重定向的查询字符串。默认${query}表示继承原值（即与被重写请求保持一致）。 只能包含英文字母、数字和特殊字符：!$&'()*+,-./:;=?@^_`。字母区分大小写。其中$1-$9会匹配请求url通配符星号（*），当正则匹配分组小于指定数字，则$指定数字结果为空。$后面跟字母，匹配结果均为空，直到下一个特殊字符出现，例如$abc#123，则匹配结果为#123；$后面跟特殊字符则直接输出特殊字符，例如$#匹配结果为$#

        :param query: The query of this CreateRewriteUrlConfig.
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
        if not isinstance(other, CreateRewriteUrlConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
