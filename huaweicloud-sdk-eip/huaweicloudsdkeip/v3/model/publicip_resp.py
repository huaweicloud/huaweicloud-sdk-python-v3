# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicipResp:

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
        'project_id': 'str',
        'ip_version': 'int',
        'public_ip_address': 'str',
        'public_ipv6_address': 'str',
        'status': 'str',
        'description': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'type': 'str',
        'vnic': 'VnicResp',
        'bandwidth': 'BandwidthResp',
        'enterprise_project_id': 'str',
        'billing_info': 'str',
        'lock_status': 'str',
        'associate_instance_type': 'str',
        'associate_instance_id': 'str',
        'publicip_pool_id': 'str',
        'publicip_pool_name': 'str',
        'alias': 'str',
        'public_border_group': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'ip_version': 'ip_version',
        'public_ip_address': 'public_ip_address',
        'public_ipv6_address': 'public_ipv6_address',
        'status': 'status',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'type': 'type',
        'vnic': 'vnic',
        'bandwidth': 'bandwidth',
        'enterprise_project_id': 'enterprise_project_id',
        'billing_info': 'billing_info',
        'lock_status': 'lock_status',
        'associate_instance_type': 'associate_instance_type',
        'associate_instance_id': 'associate_instance_id',
        'publicip_pool_id': 'publicip_pool_id',
        'publicip_pool_name': 'publicip_pool_name',
        'alias': 'alias',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, id=None, project_id=None, ip_version=None, public_ip_address=None, public_ipv6_address=None, status=None, description=None, created_at=None, updated_at=None, type=None, vnic=None, bandwidth=None, enterprise_project_id=None, billing_info=None, lock_status=None, associate_instance_type=None, associate_instance_id=None, publicip_pool_id=None, publicip_pool_name=None, alias=None, public_border_group=None):
        """PublicipResp

        The model defined in huaweicloud sdk

        :param id: - 功能说明：弹性公网IP的唯一标识
        :type id: str
        :param project_id: - 功能说明：项目ID
        :type project_id: str
        :param ip_version: - 功能说明: 弹性公网IP版本号 - 取值范围: 4、6   - 4表示公网IP地址为public_ip_address地址   - 6表示公网IP地址为public_ipv6_address地址
        :type ip_version: int
        :param public_ip_address: - 功能说明: 弹性公网IPv4地址
        :type public_ip_address: str
        :param public_ipv6_address: - 功能说明: 弹性公网IPv6地址
        :type public_ipv6_address: str
        :param status: - 功能说明：弹性公网IP的状态 - 取值范围：FREEZED，DOWN，ACTIVE，ERROR。   - FREEZED表示弹性公网IP处于冻结状态   - DOWN表示弹性公网IP未绑定实例   - ACTIVE表示弹性公网IP绑定实例，正在使用中   - ERROR表示弹性公网IP状态异常
        :type status: str
        :param description: - 功能说明：弹性公网IP的描述信息 - 约束：用户以自定义方式标识资源，系统不感知
        :type description: str
        :param created_at: - 功能说明：弹性公网IP的创建时间 - 约束：UTC时间格式（2018-12-25T10:07:24Z）
        :type created_at: str
        :param updated_at: - 功能说明：弹性公网IP最近的更新时间 - 约束：UTC时间格式（2018-12-25T10:09:20Z）
        :type updated_at: str
        :param type: - 功能说明：弹性公网IP的类型 - 取值范围：EIP，DUALSTACK
        :type type: str
        :param vnic: 
        :type vnic: :class:`huaweicloudsdkeip.v3.VnicResp`
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkeip.v3.BandwidthResp`
        :param enterprise_project_id: - 功能说明：弹性公网IP的企业项目ID
        :type enterprise_project_id: str
        :param billing_info: - 功能说明：弹性公网IP的订单信息 - 约束：包周期才会有订单信息，按需资源此字段为空
        :type billing_info: str
        :param lock_status: - 功能说明：记录弹性公网IP当前的冻结状态 - 约束：metadata类型，标识欠费冻结、公安冻结
        :type lock_status: str
        :param associate_instance_type: - 功能说明：弹性公网IP绑定的实例类型 - 取值范围：PORT、NATGW、ELB、ELBV1、VPN 
        :type associate_instance_type: str
        :param associate_instance_id: - 功能说明：弹性公网IP绑定的实例ID
        :type associate_instance_id: str
        :param publicip_pool_id: - 功能说明：弹性公网IP所属网络的ID。publicip_pool_name对应的网络ID
        :type publicip_pool_id: str
        :param publicip_pool_name: - 功能说明：弹性公网IP的网络类型， 包括公共池类型，如5_bgp/5_sbgp...，和用户购买的专属池。专属池见publcip_pool相关接口
        :type publicip_pool_name: str
        :param alias: - 功能说明：弹性公网IP别名
        :type alias: str
        :param public_border_group: - 功能说明：中心还是边缘。中心CENTER，边缘为各边缘az名称
        :type public_border_group: str
        """
        
        

        self._id = None
        self._project_id = None
        self._ip_version = None
        self._public_ip_address = None
        self._public_ipv6_address = None
        self._status = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._type = None
        self._vnic = None
        self._bandwidth = None
        self._enterprise_project_id = None
        self._billing_info = None
        self._lock_status = None
        self._associate_instance_type = None
        self._associate_instance_id = None
        self._publicip_pool_id = None
        self._publicip_pool_name = None
        self._alias = None
        self._public_border_group = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if ip_version is not None:
            self.ip_version = ip_version
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if public_ipv6_address is not None:
            self.public_ipv6_address = public_ipv6_address
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if type is not None:
            self.type = type
        if vnic is not None:
            self.vnic = vnic
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if billing_info is not None:
            self.billing_info = billing_info
        if lock_status is not None:
            self.lock_status = lock_status
        if associate_instance_type is not None:
            self.associate_instance_type = associate_instance_type
        if associate_instance_id is not None:
            self.associate_instance_id = associate_instance_id
        if publicip_pool_id is not None:
            self.publicip_pool_id = publicip_pool_id
        if publicip_pool_name is not None:
            self.publicip_pool_name = publicip_pool_name
        if alias is not None:
            self.alias = alias
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def id(self):
        """Gets the id of this PublicipResp.

        - 功能说明：弹性公网IP的唯一标识

        :return: The id of this PublicipResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicipResp.

        - 功能说明：弹性公网IP的唯一标识

        :param id: The id of this PublicipResp.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this PublicipResp.

        - 功能说明：项目ID

        :return: The project_id of this PublicipResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PublicipResp.

        - 功能说明：项目ID

        :param project_id: The project_id of this PublicipResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ip_version(self):
        """Gets the ip_version of this PublicipResp.

        - 功能说明: 弹性公网IP版本号 - 取值范围: 4、6   - 4表示公网IP地址为public_ip_address地址   - 6表示公网IP地址为public_ipv6_address地址

        :return: The ip_version of this PublicipResp.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this PublicipResp.

        - 功能说明: 弹性公网IP版本号 - 取值范围: 4、6   - 4表示公网IP地址为public_ip_address地址   - 6表示公网IP地址为public_ipv6_address地址

        :param ip_version: The ip_version of this PublicipResp.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this PublicipResp.

        - 功能说明: 弹性公网IPv4地址

        :return: The public_ip_address of this PublicipResp.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this PublicipResp.

        - 功能说明: 弹性公网IPv4地址

        :param public_ip_address: The public_ip_address of this PublicipResp.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def public_ipv6_address(self):
        """Gets the public_ipv6_address of this PublicipResp.

        - 功能说明: 弹性公网IPv6地址

        :return: The public_ipv6_address of this PublicipResp.
        :rtype: str
        """
        return self._public_ipv6_address

    @public_ipv6_address.setter
    def public_ipv6_address(self, public_ipv6_address):
        """Sets the public_ipv6_address of this PublicipResp.

        - 功能说明: 弹性公网IPv6地址

        :param public_ipv6_address: The public_ipv6_address of this PublicipResp.
        :type public_ipv6_address: str
        """
        self._public_ipv6_address = public_ipv6_address

    @property
    def status(self):
        """Gets the status of this PublicipResp.

        - 功能说明：弹性公网IP的状态 - 取值范围：FREEZED，DOWN，ACTIVE，ERROR。   - FREEZED表示弹性公网IP处于冻结状态   - DOWN表示弹性公网IP未绑定实例   - ACTIVE表示弹性公网IP绑定实例，正在使用中   - ERROR表示弹性公网IP状态异常

        :return: The status of this PublicipResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PublicipResp.

        - 功能说明：弹性公网IP的状态 - 取值范围：FREEZED，DOWN，ACTIVE，ERROR。   - FREEZED表示弹性公网IP处于冻结状态   - DOWN表示弹性公网IP未绑定实例   - ACTIVE表示弹性公网IP绑定实例，正在使用中   - ERROR表示弹性公网IP状态异常

        :param status: The status of this PublicipResp.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this PublicipResp.

        - 功能说明：弹性公网IP的描述信息 - 约束：用户以自定义方式标识资源，系统不感知

        :return: The description of this PublicipResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PublicipResp.

        - 功能说明：弹性公网IP的描述信息 - 约束：用户以自定义方式标识资源，系统不感知

        :param description: The description of this PublicipResp.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this PublicipResp.

        - 功能说明：弹性公网IP的创建时间 - 约束：UTC时间格式（2018-12-25T10:07:24Z）

        :return: The created_at of this PublicipResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PublicipResp.

        - 功能说明：弹性公网IP的创建时间 - 约束：UTC时间格式（2018-12-25T10:07:24Z）

        :param created_at: The created_at of this PublicipResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PublicipResp.

        - 功能说明：弹性公网IP最近的更新时间 - 约束：UTC时间格式（2018-12-25T10:09:20Z）

        :return: The updated_at of this PublicipResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PublicipResp.

        - 功能说明：弹性公网IP最近的更新时间 - 约束：UTC时间格式（2018-12-25T10:09:20Z）

        :param updated_at: The updated_at of this PublicipResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def type(self):
        """Gets the type of this PublicipResp.

        - 功能说明：弹性公网IP的类型 - 取值范围：EIP，DUALSTACK

        :return: The type of this PublicipResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PublicipResp.

        - 功能说明：弹性公网IP的类型 - 取值范围：EIP，DUALSTACK

        :param type: The type of this PublicipResp.
        :type type: str
        """
        self._type = type

    @property
    def vnic(self):
        """Gets the vnic of this PublicipResp.

        :return: The vnic of this PublicipResp.
        :rtype: :class:`huaweicloudsdkeip.v3.VnicResp`
        """
        return self._vnic

    @vnic.setter
    def vnic(self, vnic):
        """Sets the vnic of this PublicipResp.

        :param vnic: The vnic of this PublicipResp.
        :type vnic: :class:`huaweicloudsdkeip.v3.VnicResp`
        """
        self._vnic = vnic

    @property
    def bandwidth(self):
        """Gets the bandwidth of this PublicipResp.

        :return: The bandwidth of this PublicipResp.
        :rtype: :class:`huaweicloudsdkeip.v3.BandwidthResp`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this PublicipResp.

        :param bandwidth: The bandwidth of this PublicipResp.
        :type bandwidth: :class:`huaweicloudsdkeip.v3.BandwidthResp`
        """
        self._bandwidth = bandwidth

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PublicipResp.

        - 功能说明：弹性公网IP的企业项目ID

        :return: The enterprise_project_id of this PublicipResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PublicipResp.

        - 功能说明：弹性公网IP的企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this PublicipResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def billing_info(self):
        """Gets the billing_info of this PublicipResp.

        - 功能说明：弹性公网IP的订单信息 - 约束：包周期才会有订单信息，按需资源此字段为空

        :return: The billing_info of this PublicipResp.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this PublicipResp.

        - 功能说明：弹性公网IP的订单信息 - 约束：包周期才会有订单信息，按需资源此字段为空

        :param billing_info: The billing_info of this PublicipResp.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def lock_status(self):
        """Gets the lock_status of this PublicipResp.

        - 功能说明：记录弹性公网IP当前的冻结状态 - 约束：metadata类型，标识欠费冻结、公安冻结

        :return: The lock_status of this PublicipResp.
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        """Sets the lock_status of this PublicipResp.

        - 功能说明：记录弹性公网IP当前的冻结状态 - 约束：metadata类型，标识欠费冻结、公安冻结

        :param lock_status: The lock_status of this PublicipResp.
        :type lock_status: str
        """
        self._lock_status = lock_status

    @property
    def associate_instance_type(self):
        """Gets the associate_instance_type of this PublicipResp.

        - 功能说明：弹性公网IP绑定的实例类型 - 取值范围：PORT、NATGW、ELB、ELBV1、VPN 

        :return: The associate_instance_type of this PublicipResp.
        :rtype: str
        """
        return self._associate_instance_type

    @associate_instance_type.setter
    def associate_instance_type(self, associate_instance_type):
        """Sets the associate_instance_type of this PublicipResp.

        - 功能说明：弹性公网IP绑定的实例类型 - 取值范围：PORT、NATGW、ELB、ELBV1、VPN 

        :param associate_instance_type: The associate_instance_type of this PublicipResp.
        :type associate_instance_type: str
        """
        self._associate_instance_type = associate_instance_type

    @property
    def associate_instance_id(self):
        """Gets the associate_instance_id of this PublicipResp.

        - 功能说明：弹性公网IP绑定的实例ID

        :return: The associate_instance_id of this PublicipResp.
        :rtype: str
        """
        return self._associate_instance_id

    @associate_instance_id.setter
    def associate_instance_id(self, associate_instance_id):
        """Sets the associate_instance_id of this PublicipResp.

        - 功能说明：弹性公网IP绑定的实例ID

        :param associate_instance_id: The associate_instance_id of this PublicipResp.
        :type associate_instance_id: str
        """
        self._associate_instance_id = associate_instance_id

    @property
    def publicip_pool_id(self):
        """Gets the publicip_pool_id of this PublicipResp.

        - 功能说明：弹性公网IP所属网络的ID。publicip_pool_name对应的网络ID

        :return: The publicip_pool_id of this PublicipResp.
        :rtype: str
        """
        return self._publicip_pool_id

    @publicip_pool_id.setter
    def publicip_pool_id(self, publicip_pool_id):
        """Sets the publicip_pool_id of this PublicipResp.

        - 功能说明：弹性公网IP所属网络的ID。publicip_pool_name对应的网络ID

        :param publicip_pool_id: The publicip_pool_id of this PublicipResp.
        :type publicip_pool_id: str
        """
        self._publicip_pool_id = publicip_pool_id

    @property
    def publicip_pool_name(self):
        """Gets the publicip_pool_name of this PublicipResp.

        - 功能说明：弹性公网IP的网络类型， 包括公共池类型，如5_bgp/5_sbgp...，和用户购买的专属池。专属池见publcip_pool相关接口

        :return: The publicip_pool_name of this PublicipResp.
        :rtype: str
        """
        return self._publicip_pool_name

    @publicip_pool_name.setter
    def publicip_pool_name(self, publicip_pool_name):
        """Sets the publicip_pool_name of this PublicipResp.

        - 功能说明：弹性公网IP的网络类型， 包括公共池类型，如5_bgp/5_sbgp...，和用户购买的专属池。专属池见publcip_pool相关接口

        :param publicip_pool_name: The publicip_pool_name of this PublicipResp.
        :type publicip_pool_name: str
        """
        self._publicip_pool_name = publicip_pool_name

    @property
    def alias(self):
        """Gets the alias of this PublicipResp.

        - 功能说明：弹性公网IP别名

        :return: The alias of this PublicipResp.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this PublicipResp.

        - 功能说明：弹性公网IP别名

        :param alias: The alias of this PublicipResp.
        :type alias: str
        """
        self._alias = alias

    @property
    def public_border_group(self):
        """Gets the public_border_group of this PublicipResp.

        - 功能说明：中心还是边缘。中心CENTER，边缘为各边缘az名称

        :return: The public_border_group of this PublicipResp.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this PublicipResp.

        - 功能说明：中心还是边缘。中心CENTER，边缘为各边缘az名称

        :param public_border_group: The public_border_group of this PublicipResp.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

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
        if not isinstance(other, PublicipResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
