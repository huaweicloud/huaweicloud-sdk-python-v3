# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgenciesV5Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'path_prefix': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'path_prefix': 'path_prefix'
    }

    def __init__(self, limit=None, marker=None, path_prefix=None):
        r"""ListAgenciesV5Request

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量，范围为1到200条，默认为100条。
        :type limit: int
        :param marker: 分页标记，长度为4到400个字符，只包含字母、数字、\&quot;+\&quot;、\&quot;/\&quot;、\&quot;&#x3D;\&quot;、\&quot;-\&quot;和\&quot;_\&quot;的字符串。
        :type marker: str
        :param path_prefix: 资源路径前缀，由若干段字符串拼接而成，每段先包含一个或多个字母、数字、\&quot;.\&quot;、\&quot;,\&quot;、\&quot;+\&quot;、\&quot;@\&quot;、\&quot;&#x3D;\&quot;、\&quot;_\&quot;或\&quot;-\&quot;，并以\&quot;/\&quot;结尾，例如\&quot;foo/bar/\&quot;。
        :type path_prefix: str
        """
        
        

        self._limit = None
        self._marker = None
        self._path_prefix = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if path_prefix is not None:
            self.path_prefix = path_prefix

    @property
    def limit(self):
        r"""Gets the limit of this ListAgenciesV5Request.

        每页显示的条目数量，范围为1到200条，默认为100条。

        :return: The limit of this ListAgenciesV5Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAgenciesV5Request.

        每页显示的条目数量，范围为1到200条，默认为100条。

        :param limit: The limit of this ListAgenciesV5Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListAgenciesV5Request.

        分页标记，长度为4到400个字符，只包含字母、数字、\"+\"、\"/\"、\"=\"、\"-\"和\"_\"的字符串。

        :return: The marker of this ListAgenciesV5Request.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAgenciesV5Request.

        分页标记，长度为4到400个字符，只包含字母、数字、\"+\"、\"/\"、\"=\"、\"-\"和\"_\"的字符串。

        :param marker: The marker of this ListAgenciesV5Request.
        :type marker: str
        """
        self._marker = marker

    @property
    def path_prefix(self):
        r"""Gets the path_prefix of this ListAgenciesV5Request.

        资源路径前缀，由若干段字符串拼接而成，每段先包含一个或多个字母、数字、\".\"、\",\"、\"+\"、\"@\"、\"=\"、\"_\"或\"-\"，并以\"/\"结尾，例如\"foo/bar/\"。

        :return: The path_prefix of this ListAgenciesV5Request.
        :rtype: str
        """
        return self._path_prefix

    @path_prefix.setter
    def path_prefix(self, path_prefix):
        r"""Sets the path_prefix of this ListAgenciesV5Request.

        资源路径前缀，由若干段字符串拼接而成，每段先包含一个或多个字母、数字、\".\"、\",\"、\"+\"、\"@\"、\"=\"、\"_\"或\"-\"，并以\"/\"结尾，例如\"foo/bar/\"。

        :param path_prefix: The path_prefix of this ListAgenciesV5Request.
        :type path_prefix: str
        """
        self._path_prefix = path_prefix

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
        if not isinstance(other, ListAgenciesV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
