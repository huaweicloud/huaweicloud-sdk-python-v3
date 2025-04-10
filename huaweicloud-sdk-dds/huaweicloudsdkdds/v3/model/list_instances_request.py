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
        'id': 'str',
        'name': 'str',
        'mode': 'str',
        'datastore_type': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'tags': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'mode': 'mode',
        'datastore_type': 'datastore_type',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'offset': 'offset',
        'limit': 'limit',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, mode=None, datastore_type=None, vpc_id=None, subnet_id=None, offset=None, limit=None, tags=None):
        r"""ListInstancesRequest

        The model defined in huaweicloud sdk

        :param id: 实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。
        :type id: str
        :param name: 实例名称。 如果name以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的name精确匹配查询。 - “*”为系统保留字符，不能只传入该字符。
        :type name: str
        :param mode: 实例类型。 - 取值为“Sharding”，表示集群实例。 - 取值为“ReplicaSet”，表示副本集实例。 - 取值为“Single”，表示单节点实例。
        :type mode: str
        :param datastore_type: 数据库版本类型。取值为“DDS-Community”。
        :type datastore_type: str
        :param vpc_id: 虚拟私有云ID。可登录虚拟私有云控制台界面，获取DDS实例所在虚拟私有云的ID。
        :type vpc_id: str
        :param subnet_id: 子网的网络ID。可登录虚拟私有云控制台界面，获取DDS实例所在虚拟私有云下子网的网络ID。
        :type subnet_id: str
        :param offset: 索引位置偏移量，表示从指定project ID下最新的实例创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的实例信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新的实例创建时间对应的实例开始查询。
        :type offset: int
        :param limit: 查询实例个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。
        :type limit: int
        :param tags: 根据实例标签键值对进行查询。{key}表示标签键，{value}表示标签值，最多包含20组。key不可以为空或重复，value可以为空。如果同时使用多个标签键值对进行查询，中间使用逗号分隔开，表示查询同时包含指定标签键值对的实例。
        :type tags: str
        """
        
        

        self._id = None
        self._name = None
        self._mode = None
        self._datastore_type = None
        self._vpc_id = None
        self._subnet_id = None
        self._offset = None
        self._limit = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if mode is not None:
            self.mode = mode
        if datastore_type is not None:
            self.datastore_type = datastore_type
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
    def id(self):
        r"""Gets the id of this ListInstancesRequest.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :return: The id of this ListInstancesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListInstancesRequest.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :param id: The id of this ListInstancesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListInstancesRequest.

        实例名称。 如果name以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的name精确匹配查询。 - “*”为系统保留字符，不能只传入该字符。

        :return: The name of this ListInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInstancesRequest.

        实例名称。 如果name以“*”起始，表示按照“*”后面的值模糊匹配，否则，按照实际填写的name精确匹配查询。 - “*”为系统保留字符，不能只传入该字符。

        :param name: The name of this ListInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def mode(self):
        r"""Gets the mode of this ListInstancesRequest.

        实例类型。 - 取值为“Sharding”，表示集群实例。 - 取值为“ReplicaSet”，表示副本集实例。 - 取值为“Single”，表示单节点实例。

        :return: The mode of this ListInstancesRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ListInstancesRequest.

        实例类型。 - 取值为“Sharding”，表示集群实例。 - 取值为“ReplicaSet”，表示副本集实例。 - 取值为“Single”，表示单节点实例。

        :param mode: The mode of this ListInstancesRequest.
        :type mode: str
        """
        self._mode = mode

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ListInstancesRequest.

        数据库版本类型。取值为“DDS-Community”。

        :return: The datastore_type of this ListInstancesRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ListInstancesRequest.

        数据库版本类型。取值为“DDS-Community”。

        :param datastore_type: The datastore_type of this ListInstancesRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListInstancesRequest.

        虚拟私有云ID。可登录虚拟私有云控制台界面，获取DDS实例所在虚拟私有云的ID。

        :return: The vpc_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListInstancesRequest.

        虚拟私有云ID。可登录虚拟私有云控制台界面，获取DDS实例所在虚拟私有云的ID。

        :param vpc_id: The vpc_id of this ListInstancesRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ListInstancesRequest.

        子网的网络ID。可登录虚拟私有云控制台界面，获取DDS实例所在虚拟私有云下子网的网络ID。

        :return: The subnet_id of this ListInstancesRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ListInstancesRequest.

        子网的网络ID。可登录虚拟私有云控制台界面，获取DDS实例所在虚拟私有云下子网的网络ID。

        :param subnet_id: The subnet_id of this ListInstancesRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInstancesRequest.

        索引位置偏移量，表示从指定project ID下最新的实例创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的实例信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新的实例创建时间对应的实例开始查询。

        :return: The offset of this ListInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstancesRequest.

        索引位置偏移量，表示从指定project ID下最新的实例创建时间开始，按时间的先后顺序偏移offset条数据后查询对应的实例信息。 取值大于或等于0。不传该参数时，查询偏移量默认为0，表示从最新的实例创建时间对应的实例开始查询。

        :param offset: The offset of this ListInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstancesRequest.

        查询实例个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。

        :return: The limit of this ListInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstancesRequest.

        查询实例个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。

        :param limit: The limit of this ListInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def tags(self):
        r"""Gets the tags of this ListInstancesRequest.

        根据实例标签键值对进行查询。{key}表示标签键，{value}表示标签值，最多包含20组。key不可以为空或重复，value可以为空。如果同时使用多个标签键值对进行查询，中间使用逗号分隔开，表示查询同时包含指定标签键值对的实例。

        :return: The tags of this ListInstancesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListInstancesRequest.

        根据实例标签键值对进行查询。{key}表示标签键，{value}表示标签值，最多包含20组。key不可以为空或重复，value可以为空。如果同时使用多个标签键值对进行查询，中间使用逗号分隔开，表示查询同时包含指定标签键值对的实例。

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
