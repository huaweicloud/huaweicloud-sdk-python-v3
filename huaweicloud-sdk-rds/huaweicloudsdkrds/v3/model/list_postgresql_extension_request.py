# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPostgresqlExtensionRequest:

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
        'database_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'database_name': 'database_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, instance_id=None, database_name=None, offset=None, limit=None):
        """ListPostgresqlExtensionRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param database_name: 数据库名称。
        :type database_name: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: int
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._database_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.database_name = database_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListPostgresqlExtensionRequest.

        语言

        :return: The x_language of this ListPostgresqlExtensionRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListPostgresqlExtensionRequest.

        语言

        :param x_language: The x_language of this ListPostgresqlExtensionRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListPostgresqlExtensionRequest.

        实例ID。

        :return: The instance_id of this ListPostgresqlExtensionRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListPostgresqlExtensionRequest.

        实例ID。

        :param instance_id: The instance_id of this ListPostgresqlExtensionRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def database_name(self):
        """Gets the database_name of this ListPostgresqlExtensionRequest.

        数据库名称。

        :return: The database_name of this ListPostgresqlExtensionRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListPostgresqlExtensionRequest.

        数据库名称。

        :param database_name: The database_name of this ListPostgresqlExtensionRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def offset(self):
        """Gets the offset of this ListPostgresqlExtensionRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListPostgresqlExtensionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPostgresqlExtensionRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListPostgresqlExtensionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPostgresqlExtensionRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListPostgresqlExtensionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPostgresqlExtensionRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListPostgresqlExtensionRequest.
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
        if not isinstance(other, ListPostgresqlExtensionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
