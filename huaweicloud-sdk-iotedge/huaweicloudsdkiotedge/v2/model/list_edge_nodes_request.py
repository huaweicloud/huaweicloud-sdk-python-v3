# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeNodesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'state': 'str',
        'type': 'str',
        'instance_id': 'str',
        'space_id': 'str',
        'node_ids': 'list[str]',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'name': 'name',
        'state': 'state',
        'type': 'type',
        'instance_id': 'instance_id',
        'space_id': 'space_id',
        'node_ids': 'node_ids',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, name=None, state=None, type=None, instance_id=None, space_id=None, node_ids=None, offset=None, limit=None):
        """ListEdgeNodesRequest

        The model defined in huaweicloud sdk

        :param name: 节点名称
        :type name: str
        :param state: 节点状态,OFFLINE|ONLINE|UNINSTALLED|INSTALLED|DELETING|UPGRADING
        :type state: str
        :param type: 节点所属资源类型，advanced|standard
        :type type: str
        :param instance_id: 实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。
        :type instance_id: str
        :param space_id: 资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，可以携带该参数查询指定资源空间下的设备列表，不携带该参数则会查询该用户下所有设备列表。
        :type space_id: str
        :param node_ids: 节点id列表,查询ID在给的节点ID列表内的节点信息
        :type node_ids: list[str]
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: int
        :param limit: 每页记录数，默认值为10，取值区间为1-1000
        :type limit: int
        """
        
        

        self._name = None
        self._state = None
        self._type = None
        self._instance_id = None
        self._space_id = None
        self._node_ids = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type
        if instance_id is not None:
            self.instance_id = instance_id
        if space_id is not None:
            self.space_id = space_id
        if node_ids is not None:
            self.node_ids = node_ids
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def name(self):
        """Gets the name of this ListEdgeNodesRequest.

        节点名称

        :return: The name of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEdgeNodesRequest.

        节点名称

        :param name: The name of this ListEdgeNodesRequest.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        """Gets the state of this ListEdgeNodesRequest.

        节点状态,OFFLINE|ONLINE|UNINSTALLED|INSTALLED|DELETING|UPGRADING

        :return: The state of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListEdgeNodesRequest.

        节点状态,OFFLINE|ONLINE|UNINSTALLED|INSTALLED|DELETING|UPGRADING

        :param state: The state of this ListEdgeNodesRequest.
        :type state: str
        """
        self._state = state

    @property
    def type(self):
        """Gets the type of this ListEdgeNodesRequest.

        节点所属资源类型，advanced|standard

        :return: The type of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListEdgeNodesRequest.

        节点所属资源类型，advanced|standard

        :param type: The type of this ListEdgeNodesRequest.
        :type type: str
        """
        self._type = type

    @property
    def instance_id(self):
        """Gets the instance_id of this ListEdgeNodesRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListEdgeNodesRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this ListEdgeNodesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def space_id(self):
        """Gets the space_id of this ListEdgeNodesRequest.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，可以携带该参数查询指定资源空间下的设备列表，不携带该参数则会查询该用户下所有设备列表。

        :return: The space_id of this ListEdgeNodesRequest.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this ListEdgeNodesRequest.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，可以携带该参数查询指定资源空间下的设备列表，不携带该参数则会查询该用户下所有设备列表。

        :param space_id: The space_id of this ListEdgeNodesRequest.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def node_ids(self):
        """Gets the node_ids of this ListEdgeNodesRequest.

        节点id列表,查询ID在给的节点ID列表内的节点信息

        :return: The node_ids of this ListEdgeNodesRequest.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        """Sets the node_ids of this ListEdgeNodesRequest.

        节点id列表,查询ID在给的节点ID列表内的节点信息

        :param node_ids: The node_ids of this ListEdgeNodesRequest.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def offset(self):
        """Gets the offset of this ListEdgeNodesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ListEdgeNodesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEdgeNodesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ListEdgeNodesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEdgeNodesRequest.

        每页记录数，默认值为10，取值区间为1-1000

        :return: The limit of this ListEdgeNodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEdgeNodesRequest.

        每页记录数，默认值为10，取值区间为1-1000

        :param limit: The limit of this ListEdgeNodesRequest.
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
        if not isinstance(other, ListEdgeNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
