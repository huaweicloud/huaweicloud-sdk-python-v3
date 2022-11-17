# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterDetailInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'ClusterDetailInstanceFlavor',
        'volume': 'ClusterDetailInstanceVolume',
        'status': 'str',
        'actions': 'list[str]',
        'type': 'str',
        'id': 'str',
        'name': 'str',
        'is_frozen': 'str',
        'components': 'str',
        'config_status': 'str',
        'role': 'str',
        'group': 'str',
        'links': 'list[ClusterLinks]',
        'params_group_id': 'str',
        'public_ip': 'str',
        'manage_ip': 'str',
        'traffic_ip': 'str',
        'shard_id': 'str',
        'manage_fix_ip': 'str',
        'private_ip': 'str',
        'internal_ip': 'str',
        'resource': 'list[Resource]'
    }

    attribute_map = {
        'flavor': 'flavor',
        'volume': 'volume',
        'status': 'status',
        'actions': 'actions',
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'is_frozen': 'isFrozen',
        'components': 'components',
        'config_status': 'config_status',
        'role': 'role',
        'group': 'group',
        'links': 'links',
        'params_group_id': 'paramsGroupId',
        'public_ip': 'publicIp',
        'manage_ip': 'manageIp',
        'traffic_ip': 'trafficIp',
        'shard_id': 'shard_id',
        'manage_fix_ip': 'manage_fix_ip',
        'private_ip': 'private_ip',
        'internal_ip': 'internal_ip',
        'resource': 'resource'
    }

    def __init__(self, flavor=None, volume=None, status=None, actions=None, type=None, id=None, name=None, is_frozen=None, components=None, config_status=None, role=None, group=None, links=None, params_group_id=None, public_ip=None, manage_ip=None, traffic_ip=None, shard_id=None, manage_fix_ip=None, private_ip=None, internal_ip=None, resource=None):
        """ClusterDetailInstance

        The model defined in huaweicloud sdk

        :param flavor: 
        :type flavor: :class:`huaweicloudsdkcdm.v1.ClusterDetailInstanceFlavor`
        :param volume: 
        :type volume: :class:`huaweicloudsdkcdm.v1.ClusterDetailInstanceVolume`
        :param status: 节点状态： - 100：创建中。 - 200：正常。 - 300：失败。 - 303：创建失败。 - 400：已删除。 - 800：冻结。
        :type status: str
        :param actions: 节点操作状态列表： - REBOOTING：重启中。 - RESTORING：恢复中。 - REBOOT_FAILURE：重启失败。
        :type actions: list[str]
        :param type: 节点类型，只支持一种类型“cdm”。
        :type type: str
        :param id: 节点的虚拟机ID。
        :type id: str
        :param name: 节点的虚拟机名称。
        :type name: str
        :param is_frozen: 节点是否冻结：0：否。1：是。
        :type is_frozen: str
        :param components: 组件
        :type components: str
        :param config_status: 节点配置状态（查询集群列表时为null）： - In-Sync：配置已同步。 - Applying：配置中。 - Sync-Failure：配置失败。
        :type config_status: str
        :param role: 实例角色
        :type role: str
        :param group: 分组
        :type group: str
        :param links: 链接信息（查询集群列表时返回值为null）
        :type links: list[:class:`huaweicloudsdkcdm.v1.ClusterLinks`]
        :param params_group_id: 组件分组id
        :type params_group_id: str
        :param public_ip: 公网ip
        :type public_ip: str
        :param manage_ip: 管理ip
        :type manage_ip: str
        :param traffic_ip: 流量ip
        :type traffic_ip: str
        :param shard_id: 分片id
        :type shard_id: str
        :param manage_fix_ip: 管理修复ip
        :type manage_fix_ip: str
        :param private_ip: 私有ip
        :type private_ip: str
        :param internal_ip: 内部ip
        :type internal_ip: str
        :param resource: 资源信息（查询集群列表时返回值为null）
        :type resource: list[:class:`huaweicloudsdkcdm.v1.Resource`]
        """
        
        

        self._flavor = None
        self._volume = None
        self._status = None
        self._actions = None
        self._type = None
        self._id = None
        self._name = None
        self._is_frozen = None
        self._components = None
        self._config_status = None
        self._role = None
        self._group = None
        self._links = None
        self._params_group_id = None
        self._public_ip = None
        self._manage_ip = None
        self._traffic_ip = None
        self._shard_id = None
        self._manage_fix_ip = None
        self._private_ip = None
        self._internal_ip = None
        self._resource = None
        self.discriminator = None

        self.flavor = flavor
        self.volume = volume
        self.status = status
        if actions is not None:
            self.actions = actions
        self.type = type
        self.id = id
        self.name = name
        self.is_frozen = is_frozen
        if components is not None:
            self.components = components
        if config_status is not None:
            self.config_status = config_status
        if role is not None:
            self.role = role
        if group is not None:
            self.group = group
        if links is not None:
            self.links = links
        if params_group_id is not None:
            self.params_group_id = params_group_id
        if public_ip is not None:
            self.public_ip = public_ip
        if manage_ip is not None:
            self.manage_ip = manage_ip
        if traffic_ip is not None:
            self.traffic_ip = traffic_ip
        if shard_id is not None:
            self.shard_id = shard_id
        if manage_fix_ip is not None:
            self.manage_fix_ip = manage_fix_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if internal_ip is not None:
            self.internal_ip = internal_ip
        if resource is not None:
            self.resource = resource

    @property
    def flavor(self):
        """Gets the flavor of this ClusterDetailInstance.

        :return: The flavor of this ClusterDetailInstance.
        :rtype: :class:`huaweicloudsdkcdm.v1.ClusterDetailInstanceFlavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ClusterDetailInstance.

        :param flavor: The flavor of this ClusterDetailInstance.
        :type flavor: :class:`huaweicloudsdkcdm.v1.ClusterDetailInstanceFlavor`
        """
        self._flavor = flavor

    @property
    def volume(self):
        """Gets the volume of this ClusterDetailInstance.

        :return: The volume of this ClusterDetailInstance.
        :rtype: :class:`huaweicloudsdkcdm.v1.ClusterDetailInstanceVolume`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this ClusterDetailInstance.

        :param volume: The volume of this ClusterDetailInstance.
        :type volume: :class:`huaweicloudsdkcdm.v1.ClusterDetailInstanceVolume`
        """
        self._volume = volume

    @property
    def status(self):
        """Gets the status of this ClusterDetailInstance.

        节点状态： - 100：创建中。 - 200：正常。 - 300：失败。 - 303：创建失败。 - 400：已删除。 - 800：冻结。

        :return: The status of this ClusterDetailInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterDetailInstance.

        节点状态： - 100：创建中。 - 200：正常。 - 300：失败。 - 303：创建失败。 - 400：已删除。 - 800：冻结。

        :param status: The status of this ClusterDetailInstance.
        :type status: str
        """
        self._status = status

    @property
    def actions(self):
        """Gets the actions of this ClusterDetailInstance.

        节点操作状态列表： - REBOOTING：重启中。 - RESTORING：恢复中。 - REBOOT_FAILURE：重启失败。

        :return: The actions of this ClusterDetailInstance.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ClusterDetailInstance.

        节点操作状态列表： - REBOOTING：重启中。 - RESTORING：恢复中。 - REBOOT_FAILURE：重启失败。

        :param actions: The actions of this ClusterDetailInstance.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def type(self):
        """Gets the type of this ClusterDetailInstance.

        节点类型，只支持一种类型“cdm”。

        :return: The type of this ClusterDetailInstance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClusterDetailInstance.

        节点类型，只支持一种类型“cdm”。

        :param type: The type of this ClusterDetailInstance.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        """Gets the id of this ClusterDetailInstance.

        节点的虚拟机ID。

        :return: The id of this ClusterDetailInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterDetailInstance.

        节点的虚拟机ID。

        :param id: The id of this ClusterDetailInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ClusterDetailInstance.

        节点的虚拟机名称。

        :return: The name of this ClusterDetailInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterDetailInstance.

        节点的虚拟机名称。

        :param name: The name of this ClusterDetailInstance.
        :type name: str
        """
        self._name = name

    @property
    def is_frozen(self):
        """Gets the is_frozen of this ClusterDetailInstance.

        节点是否冻结：0：否。1：是。

        :return: The is_frozen of this ClusterDetailInstance.
        :rtype: str
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this ClusterDetailInstance.

        节点是否冻结：0：否。1：是。

        :param is_frozen: The is_frozen of this ClusterDetailInstance.
        :type is_frozen: str
        """
        self._is_frozen = is_frozen

    @property
    def components(self):
        """Gets the components of this ClusterDetailInstance.

        组件

        :return: The components of this ClusterDetailInstance.
        :rtype: str
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this ClusterDetailInstance.

        组件

        :param components: The components of this ClusterDetailInstance.
        :type components: str
        """
        self._components = components

    @property
    def config_status(self):
        """Gets the config_status of this ClusterDetailInstance.

        节点配置状态（查询集群列表时为null）： - In-Sync：配置已同步。 - Applying：配置中。 - Sync-Failure：配置失败。

        :return: The config_status of this ClusterDetailInstance.
        :rtype: str
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        """Sets the config_status of this ClusterDetailInstance.

        节点配置状态（查询集群列表时为null）： - In-Sync：配置已同步。 - Applying：配置中。 - Sync-Failure：配置失败。

        :param config_status: The config_status of this ClusterDetailInstance.
        :type config_status: str
        """
        self._config_status = config_status

    @property
    def role(self):
        """Gets the role of this ClusterDetailInstance.

        实例角色

        :return: The role of this ClusterDetailInstance.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ClusterDetailInstance.

        实例角色

        :param role: The role of this ClusterDetailInstance.
        :type role: str
        """
        self._role = role

    @property
    def group(self):
        """Gets the group of this ClusterDetailInstance.

        分组

        :return: The group of this ClusterDetailInstance.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ClusterDetailInstance.

        分组

        :param group: The group of this ClusterDetailInstance.
        :type group: str
        """
        self._group = group

    @property
    def links(self):
        """Gets the links of this ClusterDetailInstance.

        链接信息（查询集群列表时返回值为null）

        :return: The links of this ClusterDetailInstance.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.ClusterLinks`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ClusterDetailInstance.

        链接信息（查询集群列表时返回值为null）

        :param links: The links of this ClusterDetailInstance.
        :type links: list[:class:`huaweicloudsdkcdm.v1.ClusterLinks`]
        """
        self._links = links

    @property
    def params_group_id(self):
        """Gets the params_group_id of this ClusterDetailInstance.

        组件分组id

        :return: The params_group_id of this ClusterDetailInstance.
        :rtype: str
        """
        return self._params_group_id

    @params_group_id.setter
    def params_group_id(self, params_group_id):
        """Sets the params_group_id of this ClusterDetailInstance.

        组件分组id

        :param params_group_id: The params_group_id of this ClusterDetailInstance.
        :type params_group_id: str
        """
        self._params_group_id = params_group_id

    @property
    def public_ip(self):
        """Gets the public_ip of this ClusterDetailInstance.

        公网ip

        :return: The public_ip of this ClusterDetailInstance.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ClusterDetailInstance.

        公网ip

        :param public_ip: The public_ip of this ClusterDetailInstance.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def manage_ip(self):
        """Gets the manage_ip of this ClusterDetailInstance.

        管理ip

        :return: The manage_ip of this ClusterDetailInstance.
        :rtype: str
        """
        return self._manage_ip

    @manage_ip.setter
    def manage_ip(self, manage_ip):
        """Sets the manage_ip of this ClusterDetailInstance.

        管理ip

        :param manage_ip: The manage_ip of this ClusterDetailInstance.
        :type manage_ip: str
        """
        self._manage_ip = manage_ip

    @property
    def traffic_ip(self):
        """Gets the traffic_ip of this ClusterDetailInstance.

        流量ip

        :return: The traffic_ip of this ClusterDetailInstance.
        :rtype: str
        """
        return self._traffic_ip

    @traffic_ip.setter
    def traffic_ip(self, traffic_ip):
        """Sets the traffic_ip of this ClusterDetailInstance.

        流量ip

        :param traffic_ip: The traffic_ip of this ClusterDetailInstance.
        :type traffic_ip: str
        """
        self._traffic_ip = traffic_ip

    @property
    def shard_id(self):
        """Gets the shard_id of this ClusterDetailInstance.

        分片id

        :return: The shard_id of this ClusterDetailInstance.
        :rtype: str
        """
        return self._shard_id

    @shard_id.setter
    def shard_id(self, shard_id):
        """Sets the shard_id of this ClusterDetailInstance.

        分片id

        :param shard_id: The shard_id of this ClusterDetailInstance.
        :type shard_id: str
        """
        self._shard_id = shard_id

    @property
    def manage_fix_ip(self):
        """Gets the manage_fix_ip of this ClusterDetailInstance.

        管理修复ip

        :return: The manage_fix_ip of this ClusterDetailInstance.
        :rtype: str
        """
        return self._manage_fix_ip

    @manage_fix_ip.setter
    def manage_fix_ip(self, manage_fix_ip):
        """Sets the manage_fix_ip of this ClusterDetailInstance.

        管理修复ip

        :param manage_fix_ip: The manage_fix_ip of this ClusterDetailInstance.
        :type manage_fix_ip: str
        """
        self._manage_fix_ip = manage_fix_ip

    @property
    def private_ip(self):
        """Gets the private_ip of this ClusterDetailInstance.

        私有ip

        :return: The private_ip of this ClusterDetailInstance.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ClusterDetailInstance.

        私有ip

        :param private_ip: The private_ip of this ClusterDetailInstance.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def internal_ip(self):
        """Gets the internal_ip of this ClusterDetailInstance.

        内部ip

        :return: The internal_ip of this ClusterDetailInstance.
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        """Sets the internal_ip of this ClusterDetailInstance.

        内部ip

        :param internal_ip: The internal_ip of this ClusterDetailInstance.
        :type internal_ip: str
        """
        self._internal_ip = internal_ip

    @property
    def resource(self):
        """Gets the resource of this ClusterDetailInstance.

        资源信息（查询集群列表时返回值为null）

        :return: The resource of this ClusterDetailInstance.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.Resource`]
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this ClusterDetailInstance.

        资源信息（查询集群列表时返回值为null）

        :param resource: The resource of this ClusterDetailInstance.
        :type resource: list[:class:`huaweicloudsdkcdm.v1.Resource`]
        """
        self._resource = resource

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
        if not isinstance(other, ClusterDetailInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
