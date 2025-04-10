# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConnectionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition': 'str',
        'offset': 'int',
        'limit': 'int',
        'network_type': 'str',
        'datastore_type': 'str',
        'connection_type': 'str',
        'instance_id': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'offset': 'offset',
        'limit': 'limit',
        'network_type': 'network_type',
        'datastore_type': 'datastore_type',
        'connection_type': 'connection_type',
        'instance_id': 'instance_id',
        'x_language': 'X-Language'
    }

    def __init__(self, condition=None, offset=None, limit=None, network_type=None, datastore_type=None, connection_type=None, instance_id=None, x_language=None):
        r"""ListConnectionsRequest

        The model defined in huaweicloud sdk

        :param condition: 数据库实例地址/实例名称/备注等关键字
        :type condition: str
        :param offset: 偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为200。
        :type limit: int
        :param network_type: 数据库来源
        :type network_type: str
        :param datastore_type: 数据库引擎。
        :type datastore_type: str
        :param connection_type: 连接类型，NORMAL-创建的连接，SHARE-他人共享给我的连接。
        :type connection_type: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        """
        
        

        self._condition = None
        self._offset = None
        self._limit = None
        self._network_type = None
        self._datastore_type = None
        self._connection_type = None
        self._instance_id = None
        self._x_language = None
        self.discriminator = None

        if condition is not None:
            self.condition = condition
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if network_type is not None:
            self.network_type = network_type
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if connection_type is not None:
            self.connection_type = connection_type
        if instance_id is not None:
            self.instance_id = instance_id
        if x_language is not None:
            self.x_language = x_language

    @property
    def condition(self):
        r"""Gets the condition of this ListConnectionsRequest.

        数据库实例地址/实例名称/备注等关键字

        :return: The condition of this ListConnectionsRequest.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this ListConnectionsRequest.

        数据库实例地址/实例名称/备注等关键字

        :param condition: The condition of this ListConnectionsRequest.
        :type condition: str
        """
        self._condition = condition

    @property
    def offset(self):
        r"""Gets the offset of this ListConnectionsRequest.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListConnectionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListConnectionsRequest.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListConnectionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListConnectionsRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为200。

        :return: The limit of this ListConnectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListConnectionsRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为200。

        :param limit: The limit of this ListConnectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def network_type(self):
        r"""Gets the network_type of this ListConnectionsRequest.

        数据库来源

        :return: The network_type of this ListConnectionsRequest.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this ListConnectionsRequest.

        数据库来源

        :param network_type: The network_type of this ListConnectionsRequest.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ListConnectionsRequest.

        数据库引擎。

        :return: The datastore_type of this ListConnectionsRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ListConnectionsRequest.

        数据库引擎。

        :param datastore_type: The datastore_type of this ListConnectionsRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def connection_type(self):
        r"""Gets the connection_type of this ListConnectionsRequest.

        连接类型，NORMAL-创建的连接，SHARE-他人共享给我的连接。

        :return: The connection_type of this ListConnectionsRequest.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        r"""Sets the connection_type of this ListConnectionsRequest.

        连接类型，NORMAL-创建的连接，SHARE-他人共享给我的连接。

        :param connection_type: The connection_type of this ListConnectionsRequest.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListConnectionsRequest.

        实例ID。

        :return: The instance_id of this ListConnectionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListConnectionsRequest.

        实例ID。

        :param instance_id: The instance_id of this ListConnectionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListConnectionsRequest.

        请求语言类型。

        :return: The x_language of this ListConnectionsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListConnectionsRequest.

        请求语言类型。

        :param x_language: The x_language of this ListConnectionsRequest.
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
        if not isinstance(other, ListConnectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
