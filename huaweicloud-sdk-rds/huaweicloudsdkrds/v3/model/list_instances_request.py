# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesRequest:

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
        'eps_id': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
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
        'eps_id': 'eps_id',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'offset': 'offset',
        'limit': 'limit',
        'tags': 'tags'
    }

    def __init__(self, x_language=None, id=None, name=None, type=None, datastore_type=None, eps_id=None, vpc_id=None, subnet_id=None, offset=None, limit=None, tags=None):
        r"""ListInstancesRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param id: 实例ID。  “\\*”为系统保留字符，如果id是以“\\*”起始，表示按照\\*后面的值模糊匹配，否则，按照id精确匹配查询。不能只传入“\\*”。
        :type id: str
        :param name: 实例名称。  “\\*”为系统保留字符，如果name是以“\\*”起始，表示按照\\*后面的值模糊匹配，否则，按照name精确匹配查询。不能只传入“\\*”。
        :type name: str
        :param type: 按照实例类型查询。取值Single、Ha、Replica，分别对应于单实例、主备实例和只读实例。
        :type type: str
        :param datastore_type: 数据库类型，区分大小写。 - MySQL - PostgreSQL - SQLServer - MariaDB
        :type datastore_type: str
        :param eps_id: 企业项目id。
        :type eps_id: str
        :param vpc_id: 虚拟私有云ID。
        :type vpc_id: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param tags: 根据实例标签键值对进行查询。 {key}表示标签键，不可以为空或重复。最大长度127个unicode字符。key不能为空或者空字符串，不能为空格，使用之前先trim前后半角空格。不能包含+/?#&amp;&#x3D;,%特殊字符。 {value}表示标签值，可以为空。最大长度255个unicode字符，使用之前先trim 前后半角空格。不能包含+/?#&amp;&#x3D;,%特殊字符。如果value为空，则表示any_value（查询任意value）。 如果同时使用多个标签键值对进行查询，中间使用逗号分隔开，最多包含10组。
        :type tags: str
        """
        
        

        self._x_language = None
        self._id = None
        self._name = None
        self._type = None
        self._datastore_type = None
        self._eps_id = None
        self._vpc_id = None
        self._subnet_id = None
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
        if eps_id is not None:
            self.eps_id = eps_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if tags is not None:
            self.tags = tags

    @property
    def x_language(self):
        r"""Gets the x_language of this ListInstancesRequest.

        语言

        :return: The x_language of this ListInstancesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListInstancesRequest.

        语言

        :param x_language: The x_language of this ListInstancesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def id(self):
        r"""Gets the id of this ListInstancesRequest.

        实例ID。  “\\*”为系统保留字符，如果id是以“\\*”起始，表示按照\\*后面的值模糊匹配，否则，按照id精确匹配查询。不能只传入“\\*”。

        :return: The id of this ListInstancesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListInstancesRequest.

        实例ID。  “\\*”为系统保留字符，如果id是以“\\*”起始，表示按照\\*后面的值模糊匹配，否则，按照id精确匹配查询。不能只传入“\\*”。

        :param id: The id of this ListInstancesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListInstancesRequest.

        实例名称。  “\\*”为系统保留字符，如果name是以“\\*”起始，表示按照\\*后面的值模糊匹配，否则，按照name精确匹配查询。不能只传入“\\*”。

        :return: The name of this ListInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInstancesRequest.

        实例名称。  “\\*”为系统保留字符，如果name是以“\\*”起始，表示按照\\*后面的值模糊匹配，否则，按照name精确匹配查询。不能只传入“\\*”。

        :param name: The name of this ListInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ListInstancesRequest.

        按照实例类型查询。取值Single、Ha、Replica，分别对应于单实例、主备实例和只读实例。

        :return: The type of this ListInstancesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListInstancesRequest.

        按照实例类型查询。取值Single、Ha、Replica，分别对应于单实例、主备实例和只读实例。

        :param type: The type of this ListInstancesRequest.
        :type type: str
        """
        self._type = type

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ListInstancesRequest.

        数据库类型，区分大小写。 - MySQL - PostgreSQL - SQLServer - MariaDB

        :return: The datastore_type of this ListInstancesRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ListInstancesRequest.

        数据库类型，区分大小写。 - MySQL - PostgreSQL - SQLServer - MariaDB

        :param datastore_type: The datastore_type of this ListInstancesRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def eps_id(self):
        r"""Gets the eps_id of this ListInstancesRequest.

        企业项目id。

        :return: The eps_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this ListInstancesRequest.

        企业项目id。

        :param eps_id: The eps_id of this ListInstancesRequest.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListInstancesRequest.

        虚拟私有云ID。

        :return: The vpc_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListInstancesRequest.

        虚拟私有云ID。

        :param vpc_id: The vpc_id of this ListInstancesRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ListInstancesRequest.

        子网ID。

        :return: The subnet_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ListInstancesRequest.

        子网ID。

        :param subnet_id: The subnet_id of this ListInstancesRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInstancesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstancesRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstancesRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstancesRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def tags(self):
        r"""Gets the tags of this ListInstancesRequest.

        根据实例标签键值对进行查询。 {key}表示标签键，不可以为空或重复。最大长度127个unicode字符。key不能为空或者空字符串，不能为空格，使用之前先trim前后半角空格。不能包含+/?#&=,%特殊字符。 {value}表示标签值，可以为空。最大长度255个unicode字符，使用之前先trim 前后半角空格。不能包含+/?#&=,%特殊字符。如果value为空，则表示any_value（查询任意value）。 如果同时使用多个标签键值对进行查询，中间使用逗号分隔开，最多包含10组。

        :return: The tags of this ListInstancesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListInstancesRequest.

        根据实例标签键值对进行查询。 {key}表示标签键，不可以为空或重复。最大长度127个unicode字符。key不能为空或者空字符串，不能为空格，使用之前先trim前后半角空格。不能包含+/?#&=,%特殊字符。 {value}表示标签值，可以为空。最大长度255个unicode字符，使用之前先trim 前后半角空格。不能包含+/?#&=,%特殊字符。如果value为空，则表示any_value（查询任意value）。 如果同时使用多个标签键值对进行查询，中间使用逗号分隔开，最多包含10组。

        :param tags: The tags of this ListInstancesRequest.
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
        if not isinstance(other, ListInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
