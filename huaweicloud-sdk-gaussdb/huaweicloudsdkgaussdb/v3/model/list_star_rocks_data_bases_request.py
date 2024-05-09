# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStarRocksDataBasesRequest:

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
        'limit': 'str',
        'offset': 'str',
        'database_name': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset',
        'database_name': 'database_name'
    }

    def __init__(self, x_language=None, instance_id=None, limit=None, offset=None, database_name=None):
        """ListStarRocksDataBasesRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param instance_id: StarRocks实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param limit: 查询记录数
        :type limit: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: str
        :param database_name: 查询的数据库名称，支持模糊搜索。
        :type database_name: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._limit = None
        self._offset = None
        self._database_name = None
        self.discriminator = None

        self.x_language = x_language
        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if database_name is not None:
            self.database_name = database_name

    @property
    def x_language(self):
        """Gets the x_language of this ListStarRocksDataBasesRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this ListStarRocksDataBasesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListStarRocksDataBasesRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this ListStarRocksDataBasesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListStarRocksDataBasesRequest.

        StarRocks实例ID，严格匹配UUID规则。

        :return: The instance_id of this ListStarRocksDataBasesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListStarRocksDataBasesRequest.

        StarRocks实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this ListStarRocksDataBasesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListStarRocksDataBasesRequest.

        查询记录数

        :return: The limit of this ListStarRocksDataBasesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListStarRocksDataBasesRequest.

        查询记录数

        :param limit: The limit of this ListStarRocksDataBasesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListStarRocksDataBasesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListStarRocksDataBasesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListStarRocksDataBasesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListStarRocksDataBasesRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def database_name(self):
        """Gets the database_name of this ListStarRocksDataBasesRequest.

        查询的数据库名称，支持模糊搜索。

        :return: The database_name of this ListStarRocksDataBasesRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListStarRocksDataBasesRequest.

        查询的数据库名称，支持模糊搜索。

        :param database_name: The database_name of this ListStarRocksDataBasesRequest.
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
        if not isinstance(other, ListStarRocksDataBasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
