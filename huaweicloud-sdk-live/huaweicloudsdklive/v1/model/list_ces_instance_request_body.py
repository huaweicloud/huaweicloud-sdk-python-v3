# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCesInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'query': 'list[ListCesInstanceRequestBodyQuery]',
        'start': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'namespace': 'namespace',
        'query': 'query',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, namespace=None, query=None, start=None, limit=None):
        r"""ListCesInstanceRequestBody

        The model defined in huaweicloud sdk

        :param namespace: 命名空间
        :type namespace: str
        :param query: 查询信息
        :type query: list[:class:`huaweicloudsdklive.v1.ListCesInstanceRequestBodyQuery`]
        :param start: 查询开始偏移
        :type start: int
        :param limit: 查询限制
        :type limit: int
        """
        
        

        self._namespace = None
        self._query = None
        self._start = None
        self._limit = None
        self.discriminator = None

        self.namespace = namespace
        self.query = query
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def namespace(self):
        r"""Gets the namespace of this ListCesInstanceRequestBody.

        命名空间

        :return: The namespace of this ListCesInstanceRequestBody.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListCesInstanceRequestBody.

        命名空间

        :param namespace: The namespace of this ListCesInstanceRequestBody.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def query(self):
        r"""Gets the query of this ListCesInstanceRequestBody.

        查询信息

        :return: The query of this ListCesInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdklive.v1.ListCesInstanceRequestBodyQuery`]
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this ListCesInstanceRequestBody.

        查询信息

        :param query: The query of this ListCesInstanceRequestBody.
        :type query: list[:class:`huaweicloudsdklive.v1.ListCesInstanceRequestBodyQuery`]
        """
        self._query = query

    @property
    def start(self):
        r"""Gets the start of this ListCesInstanceRequestBody.

        查询开始偏移

        :return: The start of this ListCesInstanceRequestBody.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ListCesInstanceRequestBody.

        查询开始偏移

        :param start: The start of this ListCesInstanceRequestBody.
        :type start: int
        """
        self._start = start

    @property
    def limit(self):
        r"""Gets the limit of this ListCesInstanceRequestBody.

        查询限制

        :return: The limit of this ListCesInstanceRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCesInstanceRequestBody.

        查询限制

        :param limit: The limit of this ListCesInstanceRequestBody.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListCesInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
