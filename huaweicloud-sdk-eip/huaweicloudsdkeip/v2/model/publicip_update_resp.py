# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicipUpdateResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bandwidth_id': 'str',
        'bandwidth_name': 'str',
        'bandwidth_share_type': 'str',
        'bandwidth_size': 'int',
        'create_time': 'datetime',
        'enterprise_project_id': 'str',
        'id': 'str',
        'port_id': 'str',
        'private_ip_address': 'str',
        'profile': 'ProfileResp',
        'public_ip_address': 'str',
        'status': 'str',
        'tenant_id': 'str',
        'type': 'str',
        'public_ipv6_address': 'str',
        'ip_version': 'int',
        'alias': 'str'
    }

    attribute_map = {
        'bandwidth_id': 'bandwidth_id',
        'bandwidth_name': 'bandwidth_name',
        'bandwidth_share_type': 'bandwidth_share_type',
        'bandwidth_size': 'bandwidth_size',
        'create_time': 'create_time',
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'port_id': 'port_id',
        'private_ip_address': 'private_ip_address',
        'profile': 'profile',
        'public_ip_address': 'public_ip_address',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'type': 'type',
        'public_ipv6_address': 'public_ipv6_address',
        'ip_version': 'ip_version',
        'alias': 'alias'
    }

    def __init__(self, bandwidth_id=None, bandwidth_name=None, bandwidth_share_type=None, bandwidth_size=None, create_time=None, enterprise_project_id=None, id=None, port_id=None, private_ip_address=None, profile=None, public_ip_address=None, status=None, tenant_id=None, type=None, public_ipv6_address=None, ip_version=None, alias=None):
        """PublicipUpdateResp

        The model defined in huaweicloud sdk

        :param bandwidth_id: 弹性公网IP对应带宽ID
        :type bandwidth_id: str
        :param bandwidth_name: 带宽名称
        :type bandwidth_name: str
        :param bandwidth_share_type: 表示共享带宽或者独享带宽  取值范围：PER，WHOLE。  WHOLE表示共享带宽  PER表示独享带宽  约束：其中IPv6暂不支持WHOLE类型带宽。
        :type bandwidth_share_type: str
        :param bandwidth_size: 带宽大小，单位为Mbit/s。
        :type bandwidth_size: int
        :param create_time: 弹性公网IP申请时间（UTC）
        :type create_time: datetime
        :param enterprise_project_id: 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建弹性公网IP时，给弹性公网IP绑定企业项目ID。
        :type enterprise_project_id: str
        :param id: 弹性公网IP唯一标识
        :type id: str
        :param port_id: 功能说明：端口id。  约束：只有绑定了的弹性公网IP查询才会返回该参数
        :type port_id: str
        :param private_ip_address: 功能说明：绑定弹性公网IP的私有IP地址  约束：只有绑定了的弹性公网IP查询才会返回该参数
        :type private_ip_address: str
        :param profile: 
        :type profile: :class:`huaweicloudsdkeip.v2.ProfileResp`
        :param public_ip_address: IPv4时是申请到的弹性公网IP地址，IPv6时是IPv6地址对应的IPv4地址
        :type public_ip_address: str
        :param status: 功能说明：弹性公网IP的状态  取值范围：冻结FREEZED，绑定失败BIND_ERROR，绑定中BINDING，释放中PENDING_DELETE， 创建中PENDING_CREATE，创建中NOTIFYING，释放中NOTIFY_DELETE，更新中PENDING_UPDATE， 未绑定DOWN ，绑定ACTIVE，绑定ELB，绑定VPN，失败ERROR。
        :type status: str
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param type: 弹性公网IP的类型
        :type type: str
        :param public_ipv6_address: IPv4时无此字段，IPv6时为申请到的弹性公网IP地址
        :type public_ipv6_address: str
        :param ip_version: IP版本信息，取值范围是4和6  4：表示IPv4  6：表示IPv6
        :type ip_version: int
        :param alias: 功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type alias: str
        """
        
        

        self._bandwidth_id = None
        self._bandwidth_name = None
        self._bandwidth_share_type = None
        self._bandwidth_size = None
        self._create_time = None
        self._enterprise_project_id = None
        self._id = None
        self._port_id = None
        self._private_ip_address = None
        self._profile = None
        self._public_ip_address = None
        self._status = None
        self._tenant_id = None
        self._type = None
        self._public_ipv6_address = None
        self._ip_version = None
        self._alias = None
        self.discriminator = None

        if bandwidth_id is not None:
            self.bandwidth_id = bandwidth_id
        if bandwidth_name is not None:
            self.bandwidth_name = bandwidth_name
        if bandwidth_share_type is not None:
            self.bandwidth_share_type = bandwidth_share_type
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if create_time is not None:
            self.create_time = create_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if id is not None:
            self.id = id
        if port_id is not None:
            self.port_id = port_id
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if profile is not None:
            self.profile = profile
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
        if alias is not None:
            self.alias = alias

    @property
    def bandwidth_id(self):
        """Gets the bandwidth_id of this PublicipUpdateResp.

        弹性公网IP对应带宽ID

        :return: The bandwidth_id of this PublicipUpdateResp.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        """Sets the bandwidth_id of this PublicipUpdateResp.

        弹性公网IP对应带宽ID

        :param bandwidth_id: The bandwidth_id of this PublicipUpdateResp.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def bandwidth_name(self):
        """Gets the bandwidth_name of this PublicipUpdateResp.

        带宽名称

        :return: The bandwidth_name of this PublicipUpdateResp.
        :rtype: str
        """
        return self._bandwidth_name

    @bandwidth_name.setter
    def bandwidth_name(self, bandwidth_name):
        """Sets the bandwidth_name of this PublicipUpdateResp.

        带宽名称

        :param bandwidth_name: The bandwidth_name of this PublicipUpdateResp.
        :type bandwidth_name: str
        """
        self._bandwidth_name = bandwidth_name

    @property
    def bandwidth_share_type(self):
        """Gets the bandwidth_share_type of this PublicipUpdateResp.

        表示共享带宽或者独享带宽  取值范围：PER，WHOLE。  WHOLE表示共享带宽  PER表示独享带宽  约束：其中IPv6暂不支持WHOLE类型带宽。

        :return: The bandwidth_share_type of this PublicipUpdateResp.
        :rtype: str
        """
        return self._bandwidth_share_type

    @bandwidth_share_type.setter
    def bandwidth_share_type(self, bandwidth_share_type):
        """Sets the bandwidth_share_type of this PublicipUpdateResp.

        表示共享带宽或者独享带宽  取值范围：PER，WHOLE。  WHOLE表示共享带宽  PER表示独享带宽  约束：其中IPv6暂不支持WHOLE类型带宽。

        :param bandwidth_share_type: The bandwidth_share_type of this PublicipUpdateResp.
        :type bandwidth_share_type: str
        """
        self._bandwidth_share_type = bandwidth_share_type

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this PublicipUpdateResp.

        带宽大小，单位为Mbit/s。

        :return: The bandwidth_size of this PublicipUpdateResp.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this PublicipUpdateResp.

        带宽大小，单位为Mbit/s。

        :param bandwidth_size: The bandwidth_size of this PublicipUpdateResp.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def create_time(self):
        """Gets the create_time of this PublicipUpdateResp.

        弹性公网IP申请时间（UTC）

        :return: The create_time of this PublicipUpdateResp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PublicipUpdateResp.

        弹性公网IP申请时间（UTC）

        :param create_time: The create_time of this PublicipUpdateResp.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PublicipUpdateResp.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建弹性公网IP时，给弹性公网IP绑定企业项目ID。

        :return: The enterprise_project_id of this PublicipUpdateResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PublicipUpdateResp.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建弹性公网IP时，给弹性公网IP绑定企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this PublicipUpdateResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this PublicipUpdateResp.

        弹性公网IP唯一标识

        :return: The id of this PublicipUpdateResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicipUpdateResp.

        弹性公网IP唯一标识

        :param id: The id of this PublicipUpdateResp.
        :type id: str
        """
        self._id = id

    @property
    def port_id(self):
        """Gets the port_id of this PublicipUpdateResp.

        功能说明：端口id。  约束：只有绑定了的弹性公网IP查询才会返回该参数

        :return: The port_id of this PublicipUpdateResp.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this PublicipUpdateResp.

        功能说明：端口id。  约束：只有绑定了的弹性公网IP查询才会返回该参数

        :param port_id: The port_id of this PublicipUpdateResp.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this PublicipUpdateResp.

        功能说明：绑定弹性公网IP的私有IP地址  约束：只有绑定了的弹性公网IP查询才会返回该参数

        :return: The private_ip_address of this PublicipUpdateResp.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this PublicipUpdateResp.

        功能说明：绑定弹性公网IP的私有IP地址  约束：只有绑定了的弹性公网IP查询才会返回该参数

        :param private_ip_address: The private_ip_address of this PublicipUpdateResp.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def profile(self):
        """Gets the profile of this PublicipUpdateResp.


        :return: The profile of this PublicipUpdateResp.
        :rtype: :class:`huaweicloudsdkeip.v2.ProfileResp`
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this PublicipUpdateResp.


        :param profile: The profile of this PublicipUpdateResp.
        :type profile: :class:`huaweicloudsdkeip.v2.ProfileResp`
        """
        self._profile = profile

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this PublicipUpdateResp.

        IPv4时是申请到的弹性公网IP地址，IPv6时是IPv6地址对应的IPv4地址

        :return: The public_ip_address of this PublicipUpdateResp.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this PublicipUpdateResp.

        IPv4时是申请到的弹性公网IP地址，IPv6时是IPv6地址对应的IPv4地址

        :param public_ip_address: The public_ip_address of this PublicipUpdateResp.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def status(self):
        """Gets the status of this PublicipUpdateResp.

        功能说明：弹性公网IP的状态  取值范围：冻结FREEZED，绑定失败BIND_ERROR，绑定中BINDING，释放中PENDING_DELETE， 创建中PENDING_CREATE，创建中NOTIFYING，释放中NOTIFY_DELETE，更新中PENDING_UPDATE， 未绑定DOWN ，绑定ACTIVE，绑定ELB，绑定VPN，失败ERROR。

        :return: The status of this PublicipUpdateResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PublicipUpdateResp.

        功能说明：弹性公网IP的状态  取值范围：冻结FREEZED，绑定失败BIND_ERROR，绑定中BINDING，释放中PENDING_DELETE， 创建中PENDING_CREATE，创建中NOTIFYING，释放中NOTIFY_DELETE，更新中PENDING_UPDATE， 未绑定DOWN ，绑定ACTIVE，绑定ELB，绑定VPN，失败ERROR。

        :param status: The status of this PublicipUpdateResp.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        """Gets the tenant_id of this PublicipUpdateResp.

        项目ID

        :return: The tenant_id of this PublicipUpdateResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this PublicipUpdateResp.

        项目ID

        :param tenant_id: The tenant_id of this PublicipUpdateResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this PublicipUpdateResp.

        弹性公网IP的类型

        :return: The type of this PublicipUpdateResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PublicipUpdateResp.

        弹性公网IP的类型

        :param type: The type of this PublicipUpdateResp.
        :type type: str
        """
        self._type = type

    @property
    def public_ipv6_address(self):
        """Gets the public_ipv6_address of this PublicipUpdateResp.

        IPv4时无此字段，IPv6时为申请到的弹性公网IP地址

        :return: The public_ipv6_address of this PublicipUpdateResp.
        :rtype: str
        """
        return self._public_ipv6_address

    @public_ipv6_address.setter
    def public_ipv6_address(self, public_ipv6_address):
        """Sets the public_ipv6_address of this PublicipUpdateResp.

        IPv4时无此字段，IPv6时为申请到的弹性公网IP地址

        :param public_ipv6_address: The public_ipv6_address of this PublicipUpdateResp.
        :type public_ipv6_address: str
        """
        self._public_ipv6_address = public_ipv6_address

    @property
    def ip_version(self):
        """Gets the ip_version of this PublicipUpdateResp.

        IP版本信息，取值范围是4和6  4：表示IPv4  6：表示IPv6

        :return: The ip_version of this PublicipUpdateResp.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this PublicipUpdateResp.

        IP版本信息，取值范围是4和6  4：表示IPv4  6：表示IPv6

        :param ip_version: The ip_version of this PublicipUpdateResp.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def alias(self):
        """Gets the alias of this PublicipUpdateResp.

        功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The alias of this PublicipUpdateResp.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this PublicipUpdateResp.

        功能说明：弹性公网IP名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param alias: The alias of this PublicipUpdateResp.
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
        if not isinstance(other, PublicipUpdateResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
