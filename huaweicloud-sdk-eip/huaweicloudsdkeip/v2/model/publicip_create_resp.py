# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicipCreateResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_size': 'int',
        'create_time': 'datetime',
        'id': 'str',
        'public_ip_address': 'str',
        'status': 'str',
        'tenant_id': 'str',
        'type': 'str',
        'public_ipv6_address': 'str',
        'ip_version': 'int',
        'enterprise_project_id': 'str',
        'alias': 'str'
    }

    attribute_map = {
        'bandwidth_size': 'bandwidth_size',
        'create_time': 'create_time',
        'id': 'id',
        'public_ip_address': 'public_ip_address',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'type': 'type',
        'public_ipv6_address': 'public_ipv6_address',
        'ip_version': 'ip_version',
        'enterprise_project_id': 'enterprise_project_id',
        'alias': 'alias'
    }

    def __init__(self, bandwidth_size=None, create_time=None, id=None, public_ip_address=None, status=None, tenant_id=None, type=None, public_ipv6_address=None, ip_version=None, enterprise_project_id=None, alias=None):
        """PublicipCreateResp

        The model defined in huaweicloud sdk

        :param bandwidth_size: 带宽大小，单位为Mbit/s。
        :type bandwidth_size: int
        :param create_time: 弹性公网IP申请时间（UTC时间）
        :type create_time: datetime
        :param id: 弹性公网IP唯一标识
        :type id: str
        :param public_ip_address: IPv4时是申请到的弹性公网IP地址，IPv6时是IPv6地址对应的IPv4地址
        :type public_ip_address: str
        :param status: 功能说明：弹性公网IP的状态  取值范围：冻结FREEZED，绑定失败BIND_ERROR，绑定中BINDING，释放中PENDING_DELETE， 创建中PENDING_CREATE，创建中NOTIFYING，释放中NOTIFY_DELETE，更新中PENDING_UPDATE， 未绑定DOWN ，绑定ACTIVE，绑定ELB，绑定VPN，失败ERROR。
        :type status: str
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param type: 功能说明：弹性IP弹性公网IP的类型  取值范围：5_telcom（电信），5_union（联通），5_bgp（全动态BGP），5_sbgp（静态BGP），5_ipv6  东北-大连：5_telcom、5_union  华南-广州：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp、5_ipv6  亚太-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  约束：必须是系统具体支持的类型publicip_id为IPv4端口，所以\&quot;publicip_type\&quot;字段未给定时，默认为5_bgp。
        :type type: str
        :param public_ipv6_address: IPv4时无此字段，IPv6时为申请到的弹性公网IP地址
        :type public_ipv6_address: str
        :param ip_version: IP版本信息，取值范围是4和6
        :type ip_version: int
        :param enterprise_project_id: 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建弹性公网IP时，给弹性公网IP绑定企业项目ID。
        :type enterprise_project_id: str
        :param alias: 功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type alias: str
        """
        
        

        self._bandwidth_size = None
        self._create_time = None
        self._id = None
        self._public_ip_address = None
        self._status = None
        self._tenant_id = None
        self._type = None
        self._public_ipv6_address = None
        self._ip_version = None
        self._enterprise_project_id = None
        self._alias = None
        self.discriminator = None

        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if create_time is not None:
            self.create_time = create_time
        if id is not None:
            self.id = id
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type
        if public_ipv6_address is not None:
            self.public_ipv6_address = public_ipv6_address
        if ip_version is not None:
            self.ip_version = ip_version
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if alias is not None:
            self.alias = alias

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this PublicipCreateResp.

        带宽大小，单位为Mbit/s。

        :return: The bandwidth_size of this PublicipCreateResp.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this PublicipCreateResp.

        带宽大小，单位为Mbit/s。

        :param bandwidth_size: The bandwidth_size of this PublicipCreateResp.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def create_time(self):
        """Gets the create_time of this PublicipCreateResp.

        弹性公网IP申请时间（UTC时间）

        :return: The create_time of this PublicipCreateResp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PublicipCreateResp.

        弹性公网IP申请时间（UTC时间）

        :param create_time: The create_time of this PublicipCreateResp.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def id(self):
        """Gets the id of this PublicipCreateResp.

        弹性公网IP唯一标识

        :return: The id of this PublicipCreateResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicipCreateResp.

        弹性公网IP唯一标识

        :param id: The id of this PublicipCreateResp.
        :type id: str
        """
        self._id = id

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this PublicipCreateResp.

        IPv4时是申请到的弹性公网IP地址，IPv6时是IPv6地址对应的IPv4地址

        :return: The public_ip_address of this PublicipCreateResp.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this PublicipCreateResp.

        IPv4时是申请到的弹性公网IP地址，IPv6时是IPv6地址对应的IPv4地址

        :param public_ip_address: The public_ip_address of this PublicipCreateResp.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def status(self):
        """Gets the status of this PublicipCreateResp.

        功能说明：弹性公网IP的状态  取值范围：冻结FREEZED，绑定失败BIND_ERROR，绑定中BINDING，释放中PENDING_DELETE， 创建中PENDING_CREATE，创建中NOTIFYING，释放中NOTIFY_DELETE，更新中PENDING_UPDATE， 未绑定DOWN ，绑定ACTIVE，绑定ELB，绑定VPN，失败ERROR。

        :return: The status of this PublicipCreateResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PublicipCreateResp.

        功能说明：弹性公网IP的状态  取值范围：冻结FREEZED，绑定失败BIND_ERROR，绑定中BINDING，释放中PENDING_DELETE， 创建中PENDING_CREATE，创建中NOTIFYING，释放中NOTIFY_DELETE，更新中PENDING_UPDATE， 未绑定DOWN ，绑定ACTIVE，绑定ELB，绑定VPN，失败ERROR。

        :param status: The status of this PublicipCreateResp.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this PublicipCreateResp.

        项目ID

        :return: The tenant_id of this PublicipCreateResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this PublicipCreateResp.

        项目ID

        :param tenant_id: The tenant_id of this PublicipCreateResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this PublicipCreateResp.

        功能说明：弹性IP弹性公网IP的类型  取值范围：5_telcom（电信），5_union（联通），5_bgp（全动态BGP），5_sbgp（静态BGP），5_ipv6  东北-大连：5_telcom、5_union  华南-广州：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp、5_ipv6  亚太-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  约束：必须是系统具体支持的类型publicip_id为IPv4端口，所以\"publicip_type\"字段未给定时，默认为5_bgp。

        :return: The type of this PublicipCreateResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PublicipCreateResp.

        功能说明：弹性IP弹性公网IP的类型  取值范围：5_telcom（电信），5_union（联通），5_bgp（全动态BGP），5_sbgp（静态BGP），5_ipv6  东北-大连：5_telcom、5_union  华南-广州：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp、5_ipv6  亚太-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  约束：必须是系统具体支持的类型publicip_id为IPv4端口，所以\"publicip_type\"字段未给定时，默认为5_bgp。

        :param type: The type of this PublicipCreateResp.
        :type type: str
        """
        self._type = type

    @property
    def public_ipv6_address(self):
        """Gets the public_ipv6_address of this PublicipCreateResp.

        IPv4时无此字段，IPv6时为申请到的弹性公网IP地址

        :return: The public_ipv6_address of this PublicipCreateResp.
        :rtype: str
        """
        return self._public_ipv6_address

    @public_ipv6_address.setter
    def public_ipv6_address(self, public_ipv6_address):
        """Sets the public_ipv6_address of this PublicipCreateResp.

        IPv4时无此字段，IPv6时为申请到的弹性公网IP地址

        :param public_ipv6_address: The public_ipv6_address of this PublicipCreateResp.
        :type public_ipv6_address: str
        """
        self._public_ipv6_address = public_ipv6_address

    @property
    def ip_version(self):
        """Gets the ip_version of this PublicipCreateResp.

        IP版本信息，取值范围是4和6

        :return: The ip_version of this PublicipCreateResp.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this PublicipCreateResp.

        IP版本信息，取值范围是4和6

        :param ip_version: The ip_version of this PublicipCreateResp.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PublicipCreateResp.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建弹性公网IP时，给弹性公网IP绑定企业项目ID。

        :return: The enterprise_project_id of this PublicipCreateResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PublicipCreateResp.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建弹性公网IP时，给弹性公网IP绑定企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this PublicipCreateResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def alias(self):
        """Gets the alias of this PublicipCreateResp.

        功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The alias of this PublicipCreateResp.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this PublicipCreateResp.

        功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param alias: The alias of this PublicipCreateResp.
        :type alias: str
        """
        self._alias = alias

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
        if not isinstance(other, PublicipCreateResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
