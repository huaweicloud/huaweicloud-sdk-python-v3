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
        'x_language': 'str',
        'connection_id': 'str',
        'db_type': 'str',
        'name': 'str',
        'inst_id': 'str',
        'ip': 'str',
        'description': 'str',
        'create_time': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'fetch_all': 'bool',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'connection_id': 'connection_id',
        'db_type': 'db_type',
        'name': 'name',
        'inst_id': 'inst_id',
        'ip': 'ip',
        'description': 'description',
        'create_time': 'create_time',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'fetch_all': 'fetch_all',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, x_language=None, connection_id=None, db_type=None, name=None, inst_id=None, ip=None, description=None, create_time=None, enterprise_project_id=None, offset=None, limit=None, fetch_all=None, sort_key=None, sort_dir=None):
        r"""ListConnectionsRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param connection_id: 连接ID。
        :type connection_id: str
        :param db_type: 连接类型。 - mysql - oracle - postgresql - mongodb
        :type db_type: str
        :param name: 连接名称，忽略大小写。
        :type name: str
        :param inst_id: 云上数据库实例ID。
        :type inst_id: str
        :param ip: 连接IP。
        :type ip: str
        :param description: 连接描述。
        :type description: str
        :param create_time: 时间区间用“，”分割。示例：2024-05-17T07:46:00.414Z,2024-05-20T07:46:00.999Z。
        :type create_time: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param offset: 偏移量，默认值为0，表示查询该偏移量后面的记录。
        :type offset: int
        :param limit: 查询返回记录的数量限制，默认值为10。
        :type limit: int
        :param fetch_all: 值为“true”时会使得offset和limit参数失效并返回所有记录。
        :type fetch_all: bool
        :param sort_key: 返回结果按该关键字排序，默认为“created_at”。
        :type sort_key: str
        :param sort_dir: 降序或升序（分别对应desc和asc，默认为“desc”）。
        :type sort_dir: str
        """
        
        

        self._x_language = None
        self._connection_id = None
        self._db_type = None
        self._name = None
        self._inst_id = None
        self._ip = None
        self._description = None
        self._create_time = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._fetch_all = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if connection_id is not None:
            self.connection_id = connection_id
        if db_type is not None:
            self.db_type = db_type
        if name is not None:
            self.name = name
        if inst_id is not None:
            self.inst_id = inst_id
        if ip is not None:
            self.ip = ip
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if fetch_all is not None:
            self.fetch_all = fetch_all
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

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

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ListConnectionsRequest.

        连接ID。

        :return: The connection_id of this ListConnectionsRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ListConnectionsRequest.

        连接ID。

        :param connection_id: The connection_id of this ListConnectionsRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def db_type(self):
        r"""Gets the db_type of this ListConnectionsRequest.

        连接类型。 - mysql - oracle - postgresql - mongodb

        :return: The db_type of this ListConnectionsRequest.
        :rtype: str
        """
        return self._db_type

    @db_type.setter
    def db_type(self, db_type):
        r"""Sets the db_type of this ListConnectionsRequest.

        连接类型。 - mysql - oracle - postgresql - mongodb

        :param db_type: The db_type of this ListConnectionsRequest.
        :type db_type: str
        """
        self._db_type = db_type

    @property
    def name(self):
        r"""Gets the name of this ListConnectionsRequest.

        连接名称，忽略大小写。

        :return: The name of this ListConnectionsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListConnectionsRequest.

        连接名称，忽略大小写。

        :param name: The name of this ListConnectionsRequest.
        :type name: str
        """
        self._name = name

    @property
    def inst_id(self):
        r"""Gets the inst_id of this ListConnectionsRequest.

        云上数据库实例ID。

        :return: The inst_id of this ListConnectionsRequest.
        :rtype: str
        """
        return self._inst_id

    @inst_id.setter
    def inst_id(self, inst_id):
        r"""Sets the inst_id of this ListConnectionsRequest.

        云上数据库实例ID。

        :param inst_id: The inst_id of this ListConnectionsRequest.
        :type inst_id: str
        """
        self._inst_id = inst_id

    @property
    def ip(self):
        r"""Gets the ip of this ListConnectionsRequest.

        连接IP。

        :return: The ip of this ListConnectionsRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ListConnectionsRequest.

        连接IP。

        :param ip: The ip of this ListConnectionsRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def description(self):
        r"""Gets the description of this ListConnectionsRequest.

        连接描述。

        :return: The description of this ListConnectionsRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListConnectionsRequest.

        连接描述。

        :param description: The description of this ListConnectionsRequest.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this ListConnectionsRequest.

        时间区间用“，”分割。示例：2024-05-17T07:46:00.414Z,2024-05-20T07:46:00.999Z。

        :return: The create_time of this ListConnectionsRequest.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListConnectionsRequest.

        时间区间用“，”分割。示例：2024-05-17T07:46:00.414Z,2024-05-20T07:46:00.999Z。

        :param create_time: The create_time of this ListConnectionsRequest.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListConnectionsRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ListConnectionsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListConnectionsRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListConnectionsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListConnectionsRequest.

        偏移量，默认值为0，表示查询该偏移量后面的记录。

        :return: The offset of this ListConnectionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListConnectionsRequest.

        偏移量，默认值为0，表示查询该偏移量后面的记录。

        :param offset: The offset of this ListConnectionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListConnectionsRequest.

        查询返回记录的数量限制，默认值为10。

        :return: The limit of this ListConnectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListConnectionsRequest.

        查询返回记录的数量限制，默认值为10。

        :param limit: The limit of this ListConnectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def fetch_all(self):
        r"""Gets the fetch_all of this ListConnectionsRequest.

        值为“true”时会使得offset和limit参数失效并返回所有记录。

        :return: The fetch_all of this ListConnectionsRequest.
        :rtype: bool
        """
        return self._fetch_all

    @fetch_all.setter
    def fetch_all(self, fetch_all):
        r"""Sets the fetch_all of this ListConnectionsRequest.

        值为“true”时会使得offset和limit参数失效并返回所有记录。

        :param fetch_all: The fetch_all of this ListConnectionsRequest.
        :type fetch_all: bool
        """
        self._fetch_all = fetch_all

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListConnectionsRequest.

        返回结果按该关键字排序，默认为“created_at”。

        :return: The sort_key of this ListConnectionsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListConnectionsRequest.

        返回结果按该关键字排序，默认为“created_at”。

        :param sort_key: The sort_key of this ListConnectionsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListConnectionsRequest.

        降序或升序（分别对应desc和asc，默认为“desc”）。

        :return: The sort_dir of this ListConnectionsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListConnectionsRequest.

        降序或升序（分别对应desc和asc，默认为“desc”）。

        :param sort_dir: The sort_dir of this ListConnectionsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
