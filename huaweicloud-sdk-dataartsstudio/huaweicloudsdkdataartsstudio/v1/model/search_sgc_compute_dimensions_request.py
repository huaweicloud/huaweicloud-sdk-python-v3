# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchSgcComputeDimensionsRequest:

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
        'workspace_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'node_creator_name': 'str',
        'type': 'int',
        'node_type': 'str',
        'order_by': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'node_creator_name': 'node_creator_name',
        'type': 'type',
        'node_type': 'node_type',
        'order_by': 'order_by'
    }

    def __init__(self, instance_id=None, workspace_id=None, offset=None, limit=None, name=None, node_creator_name=None, type=None, node_type=None, order_by=None):
        r"""SearchSgcComputeDimensionsRequest

        The model defined in huaweicloud sdk

        :param instance_id: DataArts Studio实例ID。
        :type instance_id: str
        :param workspace_id: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace_id: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 返回数据条数，表示页大小
        :type limit: int
        :param name: 节点实例名称或脚本名称
        :type name: str
        :param node_creator_name: 节点实例创建者name
        :type node_creator_name: str
        :param type: 类型，0表示节点实例,1表示脚本,2表示节点的测试运行,成本管理页面对于0和2的情况均展示为节点实例
        :type type: int
        :param node_type: 节点类型，HIVE SQL, SparkSQL, Spark, Flink SQL, MRS Flink Job, DWS SQL为支持的枚举节点类型
        :type node_type: str
        :param order_by: 排序规则，示例priority ASC表示按照优先级升序排序,priority DESC表示按照优先级降序排序
        :type order_by: str
        """
        
        

        self._instance_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._node_creator_name = None
        self._type = None
        self._node_type = None
        self._order_by = None
        self.discriminator = None

        self.instance_id = instance_id
        self.workspace_id = workspace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if node_creator_name is not None:
            self.node_creator_name = node_creator_name
        if type is not None:
            self.type = type
        if node_type is not None:
            self.node_type = node_type
        if order_by is not None:
            self.order_by = order_by

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SearchSgcComputeDimensionsRequest.

        DataArts Studio实例ID。

        :return: The instance_id of this SearchSgcComputeDimensionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SearchSgcComputeDimensionsRequest.

        DataArts Studio实例ID。

        :param instance_id: The instance_id of this SearchSgcComputeDimensionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this SearchSgcComputeDimensionsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace_id of this SearchSgcComputeDimensionsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this SearchSgcComputeDimensionsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace_id: The workspace_id of this SearchSgcComputeDimensionsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this SearchSgcComputeDimensionsRequest.

        偏移量

        :return: The offset of this SearchSgcComputeDimensionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SearchSgcComputeDimensionsRequest.

        偏移量

        :param offset: The offset of this SearchSgcComputeDimensionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this SearchSgcComputeDimensionsRequest.

        返回数据条数，表示页大小

        :return: The limit of this SearchSgcComputeDimensionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SearchSgcComputeDimensionsRequest.

        返回数据条数，表示页大小

        :param limit: The limit of this SearchSgcComputeDimensionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this SearchSgcComputeDimensionsRequest.

        节点实例名称或脚本名称

        :return: The name of this SearchSgcComputeDimensionsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SearchSgcComputeDimensionsRequest.

        节点实例名称或脚本名称

        :param name: The name of this SearchSgcComputeDimensionsRequest.
        :type name: str
        """
        self._name = name

    @property
    def node_creator_name(self):
        r"""Gets the node_creator_name of this SearchSgcComputeDimensionsRequest.

        节点实例创建者name

        :return: The node_creator_name of this SearchSgcComputeDimensionsRequest.
        :rtype: str
        """
        return self._node_creator_name

    @node_creator_name.setter
    def node_creator_name(self, node_creator_name):
        r"""Sets the node_creator_name of this SearchSgcComputeDimensionsRequest.

        节点实例创建者name

        :param node_creator_name: The node_creator_name of this SearchSgcComputeDimensionsRequest.
        :type node_creator_name: str
        """
        self._node_creator_name = node_creator_name

    @property
    def type(self):
        r"""Gets the type of this SearchSgcComputeDimensionsRequest.

        类型，0表示节点实例,1表示脚本,2表示节点的测试运行,成本管理页面对于0和2的情况均展示为节点实例

        :return: The type of this SearchSgcComputeDimensionsRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SearchSgcComputeDimensionsRequest.

        类型，0表示节点实例,1表示脚本,2表示节点的测试运行,成本管理页面对于0和2的情况均展示为节点实例

        :param type: The type of this SearchSgcComputeDimensionsRequest.
        :type type: int
        """
        self._type = type

    @property
    def node_type(self):
        r"""Gets the node_type of this SearchSgcComputeDimensionsRequest.

        节点类型，HIVE SQL, SparkSQL, Spark, Flink SQL, MRS Flink Job, DWS SQL为支持的枚举节点类型

        :return: The node_type of this SearchSgcComputeDimensionsRequest.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this SearchSgcComputeDimensionsRequest.

        节点类型，HIVE SQL, SparkSQL, Spark, Flink SQL, MRS Flink Job, DWS SQL为支持的枚举节点类型

        :param node_type: The node_type of this SearchSgcComputeDimensionsRequest.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def order_by(self):
        r"""Gets the order_by of this SearchSgcComputeDimensionsRequest.

        排序规则，示例priority ASC表示按照优先级升序排序,priority DESC表示按照优先级降序排序

        :return: The order_by of this SearchSgcComputeDimensionsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this SearchSgcComputeDimensionsRequest.

        排序规则，示例priority ASC表示按照优先级升序排序,priority DESC表示按照优先级降序排序

        :param order_by: The order_by of this SearchSgcComputeDimensionsRequest.
        :type order_by: str
        """
        self._order_by = order_by

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
        if not isinstance(other, SearchSgcComputeDimensionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
