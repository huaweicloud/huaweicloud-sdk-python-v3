# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeNodeDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_node_id': 'str',
        'name': 'str',
        'state': 'str',
        'instance_id': 'str',
        'space_id': 'str',
        'type': 'str',
        'resource_ids': 'list[str]',
        'resource_spec_types': 'list[str]',
        'ips': 'list[str]',
        'create_time': 'str'
    }

    attribute_map = {
        'edge_node_id': 'edge_node_id',
        'name': 'name',
        'state': 'state',
        'instance_id': 'instance_id',
        'space_id': 'space_id',
        'type': 'type',
        'resource_ids': 'resource_ids',
        'resource_spec_types': 'resource_spec_types',
        'ips': 'ips',
        'create_time': 'create_time'
    }

    def __init__(self, edge_node_id=None, name=None, state=None, instance_id=None, space_id=None, type=None, resource_ids=None, resource_spec_types=None, ips=None, create_time=None):
        """EdgeNodeDTO

        The model defined in huaweicloud sdk

        :param edge_node_id: 边缘节点ID
        :type edge_node_id: str
        :param name: 边缘节点名称
        :type name: str
        :param state: 边缘节点状态 UNINSTALLED|INSTALLED|OFFLINE|ONLINE|DELETING|FROZEN
        :type state: str
        :param instance_id: 实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。
        :type instance_id: str
        :param space_id: 资源空间id，对应IOTDA云服务接口参数中的app_id。
        :type space_id: str
        :param type: 节点所属资源类型：advanced|standard
        :type type: str
        :param resource_ids: 节点所购买的资源类型的列表
        :type resource_ids: list[str]
        :param resource_spec_types: 节点所购买的资源类型的列表
        :type resource_spec_types: list[str]
        :param ips: 边缘节点ip列表
        :type ips: list[str]
        :param create_time: 边缘节点创建时间
        :type create_time: str
        """
        
        

        self._edge_node_id = None
        self._name = None
        self._state = None
        self._instance_id = None
        self._space_id = None
        self._type = None
        self._resource_ids = None
        self._resource_spec_types = None
        self._ips = None
        self._create_time = None
        self.discriminator = None

        if edge_node_id is not None:
            self.edge_node_id = edge_node_id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if instance_id is not None:
            self.instance_id = instance_id
        if space_id is not None:
            self.space_id = space_id
        if type is not None:
            self.type = type
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if resource_spec_types is not None:
            self.resource_spec_types = resource_spec_types
        if ips is not None:
            self.ips = ips
        if create_time is not None:
            self.create_time = create_time

    @property
    def edge_node_id(self):
        """Gets the edge_node_id of this EdgeNodeDTO.

        边缘节点ID

        :return: The edge_node_id of this EdgeNodeDTO.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        """Sets the edge_node_id of this EdgeNodeDTO.

        边缘节点ID

        :param edge_node_id: The edge_node_id of this EdgeNodeDTO.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def name(self):
        """Gets the name of this EdgeNodeDTO.

        边缘节点名称

        :return: The name of this EdgeNodeDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EdgeNodeDTO.

        边缘节点名称

        :param name: The name of this EdgeNodeDTO.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        """Gets the state of this EdgeNodeDTO.

        边缘节点状态 UNINSTALLED|INSTALLED|OFFLINE|ONLINE|DELETING|FROZEN

        :return: The state of this EdgeNodeDTO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EdgeNodeDTO.

        边缘节点状态 UNINSTALLED|INSTALLED|OFFLINE|ONLINE|DELETING|FROZEN

        :param state: The state of this EdgeNodeDTO.
        :type state: str
        """
        self._state = state

    @property
    def instance_id(self):
        """Gets the instance_id of this EdgeNodeDTO.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this EdgeNodeDTO.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this EdgeNodeDTO.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this EdgeNodeDTO.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def space_id(self):
        """Gets the space_id of this EdgeNodeDTO.

        资源空间id，对应IOTDA云服务接口参数中的app_id。

        :return: The space_id of this EdgeNodeDTO.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this EdgeNodeDTO.

        资源空间id，对应IOTDA云服务接口参数中的app_id。

        :param space_id: The space_id of this EdgeNodeDTO.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def type(self):
        """Gets the type of this EdgeNodeDTO.

        节点所属资源类型：advanced|standard

        :return: The type of this EdgeNodeDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EdgeNodeDTO.

        节点所属资源类型：advanced|standard

        :param type: The type of this EdgeNodeDTO.
        :type type: str
        """
        self._type = type

    @property
    def resource_ids(self):
        """Gets the resource_ids of this EdgeNodeDTO.

        节点所购买的资源类型的列表

        :return: The resource_ids of this EdgeNodeDTO.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this EdgeNodeDTO.

        节点所购买的资源类型的列表

        :param resource_ids: The resource_ids of this EdgeNodeDTO.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def resource_spec_types(self):
        """Gets the resource_spec_types of this EdgeNodeDTO.

        节点所购买的资源类型的列表

        :return: The resource_spec_types of this EdgeNodeDTO.
        :rtype: list[str]
        """
        return self._resource_spec_types

    @resource_spec_types.setter
    def resource_spec_types(self, resource_spec_types):
        """Sets the resource_spec_types of this EdgeNodeDTO.

        节点所购买的资源类型的列表

        :param resource_spec_types: The resource_spec_types of this EdgeNodeDTO.
        :type resource_spec_types: list[str]
        """
        self._resource_spec_types = resource_spec_types

    @property
    def ips(self):
        """Gets the ips of this EdgeNodeDTO.

        边缘节点ip列表

        :return: The ips of this EdgeNodeDTO.
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this EdgeNodeDTO.

        边缘节点ip列表

        :param ips: The ips of this EdgeNodeDTO.
        :type ips: list[str]
        """
        self._ips = ips

    @property
    def create_time(self):
        """Gets the create_time of this EdgeNodeDTO.

        边缘节点创建时间

        :return: The create_time of this EdgeNodeDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this EdgeNodeDTO.

        边缘节点创建时间

        :param create_time: The create_time of this EdgeNodeDTO.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, EdgeNodeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
