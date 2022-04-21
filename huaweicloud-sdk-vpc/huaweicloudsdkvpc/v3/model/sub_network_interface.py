# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubNetworkInterface:

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
        'virsubnet_id': 'str',
        'private_ip_address': 'str',
        'ipv6_ip_address': 'str',
        'mac_address': 'str',
        'parent_device_id': 'str',
        'parent_id': 'str',
        'description': 'str',
        'vpc_id': 'str',
        'vlan_id': 'int',
        'security_groups': 'list[str]',
        'tags': 'list[str]',
        'project_id': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'virsubnet_id': 'virsubnet_id',
        'private_ip_address': 'private_ip_address',
        'ipv6_ip_address': 'ipv6_ip_address',
        'mac_address': 'mac_address',
        'parent_device_id': 'parent_device_id',
        'parent_id': 'parent_id',
        'description': 'description',
        'vpc_id': 'vpc_id',
        'vlan_id': 'vlan_id',
        'security_groups': 'security_groups',
        'tags': 'tags',
        'project_id': 'project_id',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, virsubnet_id=None, private_ip_address=None, ipv6_ip_address=None, mac_address=None, parent_device_id=None, parent_id=None, description=None, vpc_id=None, vlan_id=None, security_groups=None, tags=None, project_id=None, created_at=None):
        """SubNetworkInterface

        The model defined in huaweicloud sdk

        :param id: 功能说明：辅助弹性网卡的唯一标识 取值范围：带(-)的标准UUID
        :type id: str
        :param virsubnet_id: 功能说明：虚拟子网ID 取值范围：标准UUID
        :type virsubnet_id: str
        :param private_ip_address: 功能说明：辅助弹性网卡的私有IPv4地址 取值范围：必须在虚拟子网的网段内，不填则随机在虚拟子网网段内随机分配
        :type private_ip_address: str
        :param ipv6_ip_address: 功能说明：辅助弹性网卡的IPv6地址
        :type ipv6_ip_address: str
        :param mac_address: 功能说明：辅助弹性网卡的mac地址 取值范围：合法的mac地址，系统随机分配
        :type mac_address: str
        :param parent_device_id: 功能说明：设备ID 取值范围：标准UUID 
        :type parent_device_id: str
        :param parent_id: 功能说明：宿主网络接口的ID 取值范围：标准UUID
        :type parent_id: str
        :param description: 功能说明：辅助弹性网卡的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param vpc_id: 功能说明：辅助弹性网卡所属的VPC_ID 取值范围：标准UUID
        :type vpc_id: str
        :param vlan_id: 功能说明：辅助弹性网卡的VLAN ID 取值范围：1-4094 约束：同一个宿主网络接口下唯一
        :type vlan_id: int
        :param security_groups: 功能说明：安全组的ID列表；例如：\&quot;security_groups\&quot;: [\&quot;a0608cbf-d047-4f54-8b28-cd7b59853fff\&quot;] 取值范围：默认值为系统默认安全组
        :type security_groups: list[str]
        :param tags: 功能说明：辅助弹性网卡的标签列表
        :type tags: list[str]
        :param project_id: 功能说明：辅助弹性网卡所属项目ID
        :type project_id: str
        :param created_at: 功能说明：辅助弹性网卡的创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        """
        
        

        self._id = None
        self._virsubnet_id = None
        self._private_ip_address = None
        self._ipv6_ip_address = None
        self._mac_address = None
        self._parent_device_id = None
        self._parent_id = None
        self._description = None
        self._vpc_id = None
        self._vlan_id = None
        self._security_groups = None
        self._tags = None
        self._project_id = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.virsubnet_id = virsubnet_id
        self.private_ip_address = private_ip_address
        self.ipv6_ip_address = ipv6_ip_address
        self.mac_address = mac_address
        self.parent_device_id = parent_device_id
        self.parent_id = parent_id
        self.description = description
        self.vpc_id = vpc_id
        self.vlan_id = vlan_id
        self.security_groups = security_groups
        self.tags = tags
        self.project_id = project_id
        self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this SubNetworkInterface.

        功能说明：辅助弹性网卡的唯一标识 取值范围：带(-)的标准UUID

        :return: The id of this SubNetworkInterface.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubNetworkInterface.

        功能说明：辅助弹性网卡的唯一标识 取值范围：带(-)的标准UUID

        :param id: The id of this SubNetworkInterface.
        :type id: str
        """
        self._id = id

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this SubNetworkInterface.

        功能说明：虚拟子网ID 取值范围：标准UUID

        :return: The virsubnet_id of this SubNetworkInterface.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this SubNetworkInterface.

        功能说明：虚拟子网ID 取值范围：标准UUID

        :param virsubnet_id: The virsubnet_id of this SubNetworkInterface.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this SubNetworkInterface.

        功能说明：辅助弹性网卡的私有IPv4地址 取值范围：必须在虚拟子网的网段内，不填则随机在虚拟子网网段内随机分配

        :return: The private_ip_address of this SubNetworkInterface.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this SubNetworkInterface.

        功能说明：辅助弹性网卡的私有IPv4地址 取值范围：必须在虚拟子网的网段内，不填则随机在虚拟子网网段内随机分配

        :param private_ip_address: The private_ip_address of this SubNetworkInterface.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def ipv6_ip_address(self):
        """Gets the ipv6_ip_address of this SubNetworkInterface.

        功能说明：辅助弹性网卡的IPv6地址

        :return: The ipv6_ip_address of this SubNetworkInterface.
        :rtype: str
        """
        return self._ipv6_ip_address

    @ipv6_ip_address.setter
    def ipv6_ip_address(self, ipv6_ip_address):
        """Sets the ipv6_ip_address of this SubNetworkInterface.

        功能说明：辅助弹性网卡的IPv6地址

        :param ipv6_ip_address: The ipv6_ip_address of this SubNetworkInterface.
        :type ipv6_ip_address: str
        """
        self._ipv6_ip_address = ipv6_ip_address

    @property
    def mac_address(self):
        """Gets the mac_address of this SubNetworkInterface.

        功能说明：辅助弹性网卡的mac地址 取值范围：合法的mac地址，系统随机分配

        :return: The mac_address of this SubNetworkInterface.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this SubNetworkInterface.

        功能说明：辅助弹性网卡的mac地址 取值范围：合法的mac地址，系统随机分配

        :param mac_address: The mac_address of this SubNetworkInterface.
        :type mac_address: str
        """
        self._mac_address = mac_address

    @property
    def parent_device_id(self):
        """Gets the parent_device_id of this SubNetworkInterface.

        功能说明：设备ID 取值范围：标准UUID 

        :return: The parent_device_id of this SubNetworkInterface.
        :rtype: str
        """
        return self._parent_device_id

    @parent_device_id.setter
    def parent_device_id(self, parent_device_id):
        """Sets the parent_device_id of this SubNetworkInterface.

        功能说明：设备ID 取值范围：标准UUID 

        :param parent_device_id: The parent_device_id of this SubNetworkInterface.
        :type parent_device_id: str
        """
        self._parent_device_id = parent_device_id

    @property
    def parent_id(self):
        """Gets the parent_id of this SubNetworkInterface.

        功能说明：宿主网络接口的ID 取值范围：标准UUID

        :return: The parent_id of this SubNetworkInterface.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this SubNetworkInterface.

        功能说明：宿主网络接口的ID 取值范围：标准UUID

        :param parent_id: The parent_id of this SubNetworkInterface.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def description(self):
        """Gets the description of this SubNetworkInterface.

        功能说明：辅助弹性网卡的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this SubNetworkInterface.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubNetworkInterface.

        功能说明：辅助弹性网卡的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this SubNetworkInterface.
        :type description: str
        """
        self._description = description

    @property
    def vpc_id(self):
        """Gets the vpc_id of this SubNetworkInterface.

        功能说明：辅助弹性网卡所属的VPC_ID 取值范围：标准UUID

        :return: The vpc_id of this SubNetworkInterface.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this SubNetworkInterface.

        功能说明：辅助弹性网卡所属的VPC_ID 取值范围：标准UUID

        :param vpc_id: The vpc_id of this SubNetworkInterface.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vlan_id(self):
        """Gets the vlan_id of this SubNetworkInterface.

        功能说明：辅助弹性网卡的VLAN ID 取值范围：1-4094 约束：同一个宿主网络接口下唯一

        :return: The vlan_id of this SubNetworkInterface.
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this SubNetworkInterface.

        功能说明：辅助弹性网卡的VLAN ID 取值范围：1-4094 约束：同一个宿主网络接口下唯一

        :param vlan_id: The vlan_id of this SubNetworkInterface.
        :type vlan_id: int
        """
        self._vlan_id = vlan_id

    @property
    def security_groups(self):
        """Gets the security_groups of this SubNetworkInterface.

        功能说明：安全组的ID列表；例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"] 取值范围：默认值为系统默认安全组

        :return: The security_groups of this SubNetworkInterface.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this SubNetworkInterface.

        功能说明：安全组的ID列表；例如：\"security_groups\": [\"a0608cbf-d047-4f54-8b28-cd7b59853fff\"] 取值范围：默认值为系统默认安全组

        :param security_groups: The security_groups of this SubNetworkInterface.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def tags(self):
        """Gets the tags of this SubNetworkInterface.

        功能说明：辅助弹性网卡的标签列表

        :return: The tags of this SubNetworkInterface.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SubNetworkInterface.

        功能说明：辅助弹性网卡的标签列表

        :param tags: The tags of this SubNetworkInterface.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def project_id(self):
        """Gets the project_id of this SubNetworkInterface.

        功能说明：辅助弹性网卡所属项目ID

        :return: The project_id of this SubNetworkInterface.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SubNetworkInterface.

        功能说明：辅助弹性网卡所属项目ID

        :param project_id: The project_id of this SubNetworkInterface.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this SubNetworkInterface.

        功能说明：辅助弹性网卡的创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this SubNetworkInterface.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SubNetworkInterface.

        功能说明：辅助弹性网卡的创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this SubNetworkInterface.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, SubNetworkInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
