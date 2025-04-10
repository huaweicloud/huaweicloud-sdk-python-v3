# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProxyConfigurationsRequest:

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
        'instance_id': 'str',
        'proxy_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'name': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'proxy_id': 'proxy_id',
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name'
    }

    def __init__(self, x_language=None, instance_id=None, proxy_id=None, limit=None, offset=None, name=None):
        r"""ShowProxyConfigurationsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param proxy_id: 数据库代理ID。
        :type proxy_id: str
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param name: 参数名称，为空则全量查询。
        :type name: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._proxy_id = None
        self._limit = None
        self._offset = None
        self._name = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.proxy_id = proxy_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowProxyConfigurationsRequest.

        语言。

        :return: The x_language of this ShowProxyConfigurationsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowProxyConfigurationsRequest.

        语言。

        :param x_language: The x_language of this ShowProxyConfigurationsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowProxyConfigurationsRequest.

        实例ID。

        :return: The instance_id of this ShowProxyConfigurationsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowProxyConfigurationsRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowProxyConfigurationsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def proxy_id(self):
        r"""Gets the proxy_id of this ShowProxyConfigurationsRequest.

        数据库代理ID。

        :return: The proxy_id of this ShowProxyConfigurationsRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        r"""Sets the proxy_id of this ShowProxyConfigurationsRequest.

        数据库代理ID。

        :param proxy_id: The proxy_id of this ShowProxyConfigurationsRequest.
        :type proxy_id: str
        """
        self._proxy_id = proxy_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowProxyConfigurationsRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ShowProxyConfigurationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowProxyConfigurationsRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ShowProxyConfigurationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowProxyConfigurationsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ShowProxyConfigurationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowProxyConfigurationsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ShowProxyConfigurationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        r"""Gets the name of this ShowProxyConfigurationsRequest.

        参数名称，为空则全量查询。

        :return: The name of this ShowProxyConfigurationsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowProxyConfigurationsRequest.

        参数名称，为空则全量查询。

        :param name: The name of this ShowProxyConfigurationsRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ShowProxyConfigurationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
