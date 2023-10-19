# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetwork:

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
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'domain_id': 'str',
        'state': 'CentralNetworkStateEnum',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'planes': 'list[CentralNetworkPlane]',
        'er_instances': 'list[CentralNetworkErInstance]',
        'connections': 'list[CentralNetworkConnectionInfo]',
        'default_plane_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'domain_id': 'domain_id',
        'state': 'state',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'planes': 'planes',
        'er_instances': 'er_instances',
        'connections': 'connections',
        'default_plane_id': 'default_plane_id'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, updated_at=None, domain_id=None, state=None, enterprise_project_id=None, tags=None, planes=None, er_instances=None, connections=None, default_plane_id=None):
        """CentralNetwork

        The model defined in huaweicloud sdk

        :param id: 资源ID标识符。
        :type id: str
        :param name: 实例名字。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param domain_id: 实例所属帐号ID。
        :type domain_id: str
        :param state: 
        :type state: :class:`huaweicloudsdkcc.v3.CentralNetworkStateEnum`
        :param enterprise_project_id: 实例所属企业项目ID。
        :type enterprise_project_id: str
        :param tags: 实例标签。
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        :param planes: 中心网平面列表。
        :type planes: list[:class:`huaweicloudsdkcc.v3.CentralNetworkPlane`]
        :param er_instances: 中心网ER实例列表。
        :type er_instances: list[:class:`huaweicloudsdkcc.v3.CentralNetworkErInstance`]
        :param connections: 中心网ER连接列表。
        :type connections: list[:class:`huaweicloudsdkcc.v3.CentralNetworkConnectionInfo`]
        :param default_plane_id: 资源ID标识符。
        :type default_plane_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._domain_id = None
        self._state = None
        self._enterprise_project_id = None
        self._tags = None
        self._planes = None
        self._er_instances = None
        self._connections = None
        self._default_plane_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.domain_id = domain_id
        self.state = state
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if planes is not None:
            self.planes = planes
        if er_instances is not None:
            self.er_instances = er_instances
        if connections is not None:
            self.connections = connections
        if default_plane_id is not None:
            self.default_plane_id = default_plane_id

    @property
    def id(self):
        """Gets the id of this CentralNetwork.

        资源ID标识符。

        :return: The id of this CentralNetwork.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CentralNetwork.

        资源ID标识符。

        :param id: The id of this CentralNetwork.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CentralNetwork.

        实例名字。

        :return: The name of this CentralNetwork.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CentralNetwork.

        实例名字。

        :param name: The name of this CentralNetwork.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CentralNetwork.

        实例描述。不支持 <>。

        :return: The description of this CentralNetwork.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CentralNetwork.

        实例描述。不支持 <>。

        :param description: The description of this CentralNetwork.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this CentralNetwork.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this CentralNetwork.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CentralNetwork.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this CentralNetwork.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CentralNetwork.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this CentralNetwork.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CentralNetwork.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this CentralNetwork.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def domain_id(self):
        """Gets the domain_id of this CentralNetwork.

        实例所属帐号ID。

        :return: The domain_id of this CentralNetwork.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CentralNetwork.

        实例所属帐号ID。

        :param domain_id: The domain_id of this CentralNetwork.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def state(self):
        """Gets the state of this CentralNetwork.

        :return: The state of this CentralNetwork.
        :rtype: :class:`huaweicloudsdkcc.v3.CentralNetworkStateEnum`
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CentralNetwork.

        :param state: The state of this CentralNetwork.
        :type state: :class:`huaweicloudsdkcc.v3.CentralNetworkStateEnum`
        """
        self._state = state

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CentralNetwork.

        实例所属企业项目ID。

        :return: The enterprise_project_id of this CentralNetwork.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CentralNetwork.

        实例所属企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CentralNetwork.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this CentralNetwork.

        实例标签。

        :return: The tags of this CentralNetwork.
        :rtype: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CentralNetwork.

        实例标签。

        :param tags: The tags of this CentralNetwork.
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        self._tags = tags

    @property
    def planes(self):
        """Gets the planes of this CentralNetwork.

        中心网平面列表。

        :return: The planes of this CentralNetwork.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetworkPlane`]
        """
        return self._planes

    @planes.setter
    def planes(self, planes):
        """Sets the planes of this CentralNetwork.

        中心网平面列表。

        :param planes: The planes of this CentralNetwork.
        :type planes: list[:class:`huaweicloudsdkcc.v3.CentralNetworkPlane`]
        """
        self._planes = planes

    @property
    def er_instances(self):
        """Gets the er_instances of this CentralNetwork.

        中心网ER实例列表。

        :return: The er_instances of this CentralNetwork.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetworkErInstance`]
        """
        return self._er_instances

    @er_instances.setter
    def er_instances(self, er_instances):
        """Sets the er_instances of this CentralNetwork.

        中心网ER实例列表。

        :param er_instances: The er_instances of this CentralNetwork.
        :type er_instances: list[:class:`huaweicloudsdkcc.v3.CentralNetworkErInstance`]
        """
        self._er_instances = er_instances

    @property
    def connections(self):
        """Gets the connections of this CentralNetwork.

        中心网ER连接列表。

        :return: The connections of this CentralNetwork.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetworkConnectionInfo`]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this CentralNetwork.

        中心网ER连接列表。

        :param connections: The connections of this CentralNetwork.
        :type connections: list[:class:`huaweicloudsdkcc.v3.CentralNetworkConnectionInfo`]
        """
        self._connections = connections

    @property
    def default_plane_id(self):
        """Gets the default_plane_id of this CentralNetwork.

        资源ID标识符。

        :return: The default_plane_id of this CentralNetwork.
        :rtype: str
        """
        return self._default_plane_id

    @default_plane_id.setter
    def default_plane_id(self, default_plane_id):
        """Sets the default_plane_id of this CentralNetwork.

        资源ID标识符。

        :param default_plane_id: The default_plane_id of this CentralNetwork.
        :type default_plane_id: str
        """
        self._default_plane_id = default_plane_id

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
        if not isinstance(other, CentralNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
