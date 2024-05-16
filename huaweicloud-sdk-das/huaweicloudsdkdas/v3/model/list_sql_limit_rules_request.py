# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlLimitRulesRequest:

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
        'offset': 'int',
        'limit': 'int',
        'datastore_type': 'str',
        'database_name': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'datastore_type': 'datastore_type',
        'database_name': 'database_name',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, datastore_type=None, database_name=None, x_language=None):
        """ListSqlLimitRulesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param offset: 偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param datastore_type: 数据库类型
        :type datastore_type: str
        :param database_name: 数据库名（PostgreSQL必填）
        :type database_name: str
        :param x_language: 语言
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._datastore_type = None
        self._database_name = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.datastore_type = datastore_type
        if database_name is not None:
            self.database_name = database_name
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListSqlLimitRulesRequest.

        实例ID

        :return: The instance_id of this ListSqlLimitRulesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListSqlLimitRulesRequest.

        实例ID

        :param instance_id: The instance_id of this ListSqlLimitRulesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListSqlLimitRulesRequest.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListSqlLimitRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSqlLimitRulesRequest.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListSqlLimitRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSqlLimitRulesRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListSqlLimitRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSqlLimitRulesRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListSqlLimitRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ListSqlLimitRulesRequest.

        数据库类型

        :return: The datastore_type of this ListSqlLimitRulesRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ListSqlLimitRulesRequest.

        数据库类型

        :param datastore_type: The datastore_type of this ListSqlLimitRulesRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def database_name(self):
        """Gets the database_name of this ListSqlLimitRulesRequest.

        数据库名（PostgreSQL必填）

        :return: The database_name of this ListSqlLimitRulesRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListSqlLimitRulesRequest.

        数据库名（PostgreSQL必填）

        :param database_name: The database_name of this ListSqlLimitRulesRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def x_language(self):
        """Gets the x_language of this ListSqlLimitRulesRequest.

        语言

        :return: The x_language of this ListSqlLimitRulesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListSqlLimitRulesRequest.

        语言

        :param x_language: The x_language of this ListSqlLimitRulesRequest.
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
        if not isinstance(other, ListSqlLimitRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
