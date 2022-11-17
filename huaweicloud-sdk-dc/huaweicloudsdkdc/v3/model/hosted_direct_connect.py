# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostedDirectConnect:

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
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'bandwidth': 'int',
        'location': 'str',
        'peer_location': 'str',
        'hosting_id': 'str',
        'provider': 'str',
        'admin_state_up': 'bool',
        'vlan': 'int',
        'status': 'str',
        'apply_time': 'str',
        'create_time': 'str',
        'provider_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'bandwidth': 'bandwidth',
        'location': 'location',
        'peer_location': 'peer_location',
        'hosting_id': 'hosting_id',
        'provider': 'provider',
        'admin_state_up': 'admin_state_up',
        'vlan': 'vlan',
        'status': 'status',
        'apply_time': 'apply_time',
        'create_time': 'create_time',
        'provider_status': 'provider_status'
    }

    def __init__(self, id=None, tenant_id=None, name=None, description=None, bandwidth=None, location=None, peer_location=None, hosting_id=None, provider=None, admin_state_up=None, vlan=None, status=None, apply_time=None, create_time=None, provider_status=None):
        """HostedDirectConnect

        The model defined in huaweicloud sdk

        :param id: 托管专线ID
        :type id: str
        :param tenant_id: 实例所属项目ID。
        :type tenant_id: str
        :param name: 物理专线名字
        :type name: str
        :param description: 物理专线的描述信息
        :type description: str
        :param bandwidth: 物理专线接入带宽，单位Mbps。
        :type bandwidth: int
        :param location: 专线的接入位置信息
        :type location: str
        :param peer_location: 物理专线对端所在的物理位置，省/市/街道或IDC名字。
        :type peer_location: str
        :param hosting_id: hosted物理专线对应的hosting物理专线的ID
        :type hosting_id: str
        :param provider: 专线线路的提供商
        :type provider: str
        :param admin_state_up: 管理状态：true或false
        :type admin_state_up: bool
        :param vlan: hosted物理专线预分配的vlan。
        :type vlan: int
        :param status: 操作状态，合法值是：ACTIVE， ERROR，PENDING_CREATE，PENDING_UPDATE。ACTIVE：虚拟网关正常ERROR： 虚拟网关异常PENDING_CREATE：创建中PENDING_UPDATE：更新中
        :type status: str
        :param apply_time: 物理专线申请时间
        :type apply_time: str
        :param create_time: 物理专线创建时间
        :type create_time: str
        :param provider_status: 物理专线的运营商操作状态，合法值是：ACTIVE， DOWN
        :type provider_status: str
        """
        
        

        self._id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._bandwidth = None
        self._location = None
        self._peer_location = None
        self._hosting_id = None
        self._provider = None
        self._admin_state_up = None
        self._vlan = None
        self._status = None
        self._apply_time = None
        self._create_time = None
        self._provider_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if location is not None:
            self.location = location
        if peer_location is not None:
            self.peer_location = peer_location
        if hosting_id is not None:
            self.hosting_id = hosting_id
        if provider is not None:
            self.provider = provider
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if vlan is not None:
            self.vlan = vlan
        if status is not None:
            self.status = status
        if apply_time is not None:
            self.apply_time = apply_time
        if create_time is not None:
            self.create_time = create_time
        if provider_status is not None:
            self.provider_status = provider_status

    @property
    def id(self):
        """Gets the id of this HostedDirectConnect.

        托管专线ID

        :return: The id of this HostedDirectConnect.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostedDirectConnect.

        托管专线ID

        :param id: The id of this HostedDirectConnect.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this HostedDirectConnect.

        实例所属项目ID。

        :return: The tenant_id of this HostedDirectConnect.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this HostedDirectConnect.

        实例所属项目ID。

        :param tenant_id: The tenant_id of this HostedDirectConnect.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this HostedDirectConnect.

        物理专线名字

        :return: The name of this HostedDirectConnect.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostedDirectConnect.

        物理专线名字

        :param name: The name of this HostedDirectConnect.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this HostedDirectConnect.

        物理专线的描述信息

        :return: The description of this HostedDirectConnect.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HostedDirectConnect.

        物理专线的描述信息

        :param description: The description of this HostedDirectConnect.
        :type description: str
        """
        self._description = description

    @property
    def bandwidth(self):
        """Gets the bandwidth of this HostedDirectConnect.

        物理专线接入带宽，单位Mbps。

        :return: The bandwidth of this HostedDirectConnect.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this HostedDirectConnect.

        物理专线接入带宽，单位Mbps。

        :param bandwidth: The bandwidth of this HostedDirectConnect.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def location(self):
        """Gets the location of this HostedDirectConnect.

        专线的接入位置信息

        :return: The location of this HostedDirectConnect.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this HostedDirectConnect.

        专线的接入位置信息

        :param location: The location of this HostedDirectConnect.
        :type location: str
        """
        self._location = location

    @property
    def peer_location(self):
        """Gets the peer_location of this HostedDirectConnect.

        物理专线对端所在的物理位置，省/市/街道或IDC名字。

        :return: The peer_location of this HostedDirectConnect.
        :rtype: str
        """
        return self._peer_location

    @peer_location.setter
    def peer_location(self, peer_location):
        """Sets the peer_location of this HostedDirectConnect.

        物理专线对端所在的物理位置，省/市/街道或IDC名字。

        :param peer_location: The peer_location of this HostedDirectConnect.
        :type peer_location: str
        """
        self._peer_location = peer_location

    @property
    def hosting_id(self):
        """Gets the hosting_id of this HostedDirectConnect.

        hosted物理专线对应的hosting物理专线的ID

        :return: The hosting_id of this HostedDirectConnect.
        :rtype: str
        """
        return self._hosting_id

    @hosting_id.setter
    def hosting_id(self, hosting_id):
        """Sets the hosting_id of this HostedDirectConnect.

        hosted物理专线对应的hosting物理专线的ID

        :param hosting_id: The hosting_id of this HostedDirectConnect.
        :type hosting_id: str
        """
        self._hosting_id = hosting_id

    @property
    def provider(self):
        """Gets the provider of this HostedDirectConnect.

        专线线路的提供商

        :return: The provider of this HostedDirectConnect.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this HostedDirectConnect.

        专线线路的提供商

        :param provider: The provider of this HostedDirectConnect.
        :type provider: str
        """
        self._provider = provider

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this HostedDirectConnect.

        管理状态：true或false

        :return: The admin_state_up of this HostedDirectConnect.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this HostedDirectConnect.

        管理状态：true或false

        :param admin_state_up: The admin_state_up of this HostedDirectConnect.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def vlan(self):
        """Gets the vlan of this HostedDirectConnect.

        hosted物理专线预分配的vlan。

        :return: The vlan of this HostedDirectConnect.
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this HostedDirectConnect.

        hosted物理专线预分配的vlan。

        :param vlan: The vlan of this HostedDirectConnect.
        :type vlan: int
        """
        self._vlan = vlan

    @property
    def status(self):
        """Gets the status of this HostedDirectConnect.

        操作状态，合法值是：ACTIVE， ERROR，PENDING_CREATE，PENDING_UPDATE。ACTIVE：虚拟网关正常ERROR： 虚拟网关异常PENDING_CREATE：创建中PENDING_UPDATE：更新中

        :return: The status of this HostedDirectConnect.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HostedDirectConnect.

        操作状态，合法值是：ACTIVE， ERROR，PENDING_CREATE，PENDING_UPDATE。ACTIVE：虚拟网关正常ERROR： 虚拟网关异常PENDING_CREATE：创建中PENDING_UPDATE：更新中

        :param status: The status of this HostedDirectConnect.
        :type status: str
        """
        self._status = status

    @property
    def apply_time(self):
        """Gets the apply_time of this HostedDirectConnect.

        物理专线申请时间

        :return: The apply_time of this HostedDirectConnect.
        :rtype: str
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this HostedDirectConnect.

        物理专线申请时间

        :param apply_time: The apply_time of this HostedDirectConnect.
        :type apply_time: str
        """
        self._apply_time = apply_time

    @property
    def create_time(self):
        """Gets the create_time of this HostedDirectConnect.

        物理专线创建时间

        :return: The create_time of this HostedDirectConnect.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this HostedDirectConnect.

        物理专线创建时间

        :param create_time: The create_time of this HostedDirectConnect.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def provider_status(self):
        """Gets the provider_status of this HostedDirectConnect.

        物理专线的运营商操作状态，合法值是：ACTIVE， DOWN

        :return: The provider_status of this HostedDirectConnect.
        :rtype: str
        """
        return self._provider_status

    @provider_status.setter
    def provider_status(self, provider_status):
        """Sets the provider_status of this HostedDirectConnect.

        物理专线的运营商操作状态，合法值是：ACTIVE， DOWN

        :param provider_status: The provider_status of this HostedDirectConnect.
        :type provider_status: str
        """
        self._provider_status = provider_status

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
        if not isinstance(other, HostedDirectConnect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
