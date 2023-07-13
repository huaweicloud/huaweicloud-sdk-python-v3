# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGaussMySqlInstancesRequest:

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
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'datastore_type': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'private_ip': 'str',
        'readonly_private_ip': 'str',
        'proxy_ip': 'str',
        'offset': 'int',
        'limit': 'int',
        'tags': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'datastore_type': 'datastore_type',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'private_ip': 'private_ip',
        'readonly_private_ip': 'readonly_private_ip',
        'proxy_ip': 'proxy_ip',
        'offset': 'offset',
        'limit': 'limit',
        'tags': 'tags'
    }

    def __init__(self, x_language=None, id=None, name=None, type=None, datastore_type=None, vpc_id=None, subnet_id=None, private_ip=None, readonly_private_ip=None, proxy_ip=None, offset=None, limit=None, tags=None):
        """ListGaussMySqlInstancesRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param id: 实例ID。 “\\*”为系统保留字符，如果id是以“\\*”起始，表示按照“\\*”后面的值模糊匹配，否则，按照id精确匹配查询。不能只传入“\\*”。
        :type id: str
        :param name: 实例名称。  “\\*”为系统保留字符，如果name是以“\\*”起始，表示按照“\\*”后面的值模糊匹配，否则，按照name精确匹配查询。不能只传入“\\*”。
        :type name: str
        :param type: 按照实例类型查询。目前仅支持Cluster。
        :type type: str
        :param datastore_type: 数据库类型，现在只支持gaussdb-mysql。
        :type datastore_type: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID信息。
        :type subnet_id: str
        :param private_ip: 读写内网IP。
        :type private_ip: str
        :param readonly_private_ip: 读内网IP。
        :type readonly_private_ip: str
        :param proxy_ip: 读写分离IP。
        :type proxy_ip: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param tags: 根据实例标签键值对进行查询。 - {key}表示标签键。 - {value}表示标签值。  如果同时使用多个标签键值对进行查询，中间使用逗号分隔开，表示查询同时包含指定标签键值对的实例。key不能重复，key之间是与的关系。
        :type tags: str
        """
        
        

        self._x_language = None
        self._id = None
        self._name = None
        self._type = None
        self._datastore_type = None
        self._vpc_id = None
        self._subnet_id = None
        self._private_ip = None
        self._readonly_private_ip = None
        self._proxy_ip = None
        self._offset = None
        self._limit = None
        self._tags = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if private_ip is not None:
            self.private_ip = private_ip
        if readonly_private_ip is not None:
            self.readonly_private_ip = readonly_private_ip
        if proxy_ip is not None:
            self.proxy_ip = proxy_ip
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if tags is not None:
            self.tags = tags

    @property
    def x_language(self):
        """Gets the x_language of this ListGaussMySqlInstancesRequest.

        语言。

        :return: The x_language of this ListGaussMySqlInstancesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListGaussMySqlInstancesRequest.

        语言。

        :param x_language: The x_language of this ListGaussMySqlInstancesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def id(self):
        """Gets the id of this ListGaussMySqlInstancesRequest.

        实例ID。 “\\*”为系统保留字符，如果id是以“\\*”起始，表示按照“\\*”后面的值模糊匹配，否则，按照id精确匹配查询。不能只传入“\\*”。

        :return: The id of this ListGaussMySqlInstancesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListGaussMySqlInstancesRequest.

        实例ID。 “\\*”为系统保留字符，如果id是以“\\*”起始，表示按照“\\*”后面的值模糊匹配，否则，按照id精确匹配查询。不能只传入“\\*”。

        :param id: The id of this ListGaussMySqlInstancesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListGaussMySqlInstancesRequest.

        实例名称。  “\\*”为系统保留字符，如果name是以“\\*”起始，表示按照“\\*”后面的值模糊匹配，否则，按照name精确匹配查询。不能只传入“\\*”。

        :return: The name of this ListGaussMySqlInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListGaussMySqlInstancesRequest.

        实例名称。  “\\*”为系统保留字符，如果name是以“\\*”起始，表示按照“\\*”后面的值模糊匹配，否则，按照name精确匹配查询。不能只传入“\\*”。

        :param name: The name of this ListGaussMySqlInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ListGaussMySqlInstancesRequest.

        按照实例类型查询。目前仅支持Cluster。

        :return: The type of this ListGaussMySqlInstancesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListGaussMySqlInstancesRequest.

        按照实例类型查询。目前仅支持Cluster。

        :param type: The type of this ListGaussMySqlInstancesRequest.
        :type type: str
        """
        self._type = type

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ListGaussMySqlInstancesRequest.

        数据库类型，现在只支持gaussdb-mysql。

        :return: The datastore_type of this ListGaussMySqlInstancesRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ListGaussMySqlInstancesRequest.

        数据库类型，现在只支持gaussdb-mysql。

        :param datastore_type: The datastore_type of this ListGaussMySqlInstancesRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListGaussMySqlInstancesRequest.

        虚拟私有云ID。

        :return: The vpc_id of this ListGaussMySqlInstancesRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListGaussMySqlInstancesRequest.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this ListGaussMySqlInstancesRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ListGaussMySqlInstancesRequest.

        子网的网络ID信息。

        :return: The subnet_id of this ListGaussMySqlInstancesRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ListGaussMySqlInstancesRequest.

        子网的网络ID信息。

        :param subnet_id: The subnet_id of this ListGaussMySqlInstancesRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def private_ip(self):
        """Gets the private_ip of this ListGaussMySqlInstancesRequest.

        读写内网IP。

        :return: The private_ip of this ListGaussMySqlInstancesRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ListGaussMySqlInstancesRequest.

        读写内网IP。

        :param private_ip: The private_ip of this ListGaussMySqlInstancesRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def readonly_private_ip(self):
        """Gets the readonly_private_ip of this ListGaussMySqlInstancesRequest.

        读内网IP。

        :return: The readonly_private_ip of this ListGaussMySqlInstancesRequest.
        :rtype: str
        """
        return self._readonly_private_ip

    @readonly_private_ip.setter
    def readonly_private_ip(self, readonly_private_ip):
        """Sets the readonly_private_ip of this ListGaussMySqlInstancesRequest.

        读内网IP。

        :param readonly_private_ip: The readonly_private_ip of this ListGaussMySqlInstancesRequest.
        :type readonly_private_ip: str
        """
        self._readonly_private_ip = readonly_private_ip

    @property
    def proxy_ip(self):
        """Gets the proxy_ip of this ListGaussMySqlInstancesRequest.

        读写分离IP。

        :return: The proxy_ip of this ListGaussMySqlInstancesRequest.
        :rtype: str
        """
        return self._proxy_ip

    @proxy_ip.setter
    def proxy_ip(self, proxy_ip):
        """Sets the proxy_ip of this ListGaussMySqlInstancesRequest.

        读写分离IP。

        :param proxy_ip: The proxy_ip of this ListGaussMySqlInstancesRequest.
        :type proxy_ip: str
        """
        self._proxy_ip = proxy_ip

    @property
    def offset(self):
        """Gets the offset of this ListGaussMySqlInstancesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListGaussMySqlInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListGaussMySqlInstancesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListGaussMySqlInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListGaussMySqlInstancesRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListGaussMySqlInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListGaussMySqlInstancesRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListGaussMySqlInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def tags(self):
        """Gets the tags of this ListGaussMySqlInstancesRequest.

        根据实例标签键值对进行查询。 - {key}表示标签键。 - {value}表示标签值。  如果同时使用多个标签键值对进行查询，中间使用逗号分隔开，表示查询同时包含指定标签键值对的实例。key不能重复，key之间是与的关系。

        :return: The tags of this ListGaussMySqlInstancesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListGaussMySqlInstancesRequest.

        根据实例标签键值对进行查询。 - {key}表示标签键。 - {value}表示标签值。  如果同时使用多个标签键值对进行查询，中间使用逗号分隔开，表示查询同时包含指定标签键值对的实例。key不能重复，key之间是与的关系。

        :param tags: The tags of this ListGaussMySqlInstancesRequest.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ListGaussMySqlInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
