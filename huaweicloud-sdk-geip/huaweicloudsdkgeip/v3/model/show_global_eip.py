# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGlobalEip:

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
        'domain_id': 'str',
        'access_site': 'str',
        'geip_pool_name': 'str',
        'isp': 'str',
        'ip_version': 'int',
        'ip_address': 'str',
        'ipv6_address': 'str',
        'freezen': 'bool',
        'freezen_info': 'str',
        'polluted': 'bool',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'internet_bandwidth_info': 'InternetBandwidthInfo',
        'global_connection_bandwidth_info': 'GlobalConnectionBandwidthInfo',
        'associate_instance_info': 'InstanceInfo',
        'is_pre_paid': 'bool',
        'tags': 'list[Tag]',
        'sys_tags': 'list[Tag]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'domain_id': 'domain_id',
        'access_site': 'access_site',
        'geip_pool_name': 'geip_pool_name',
        'isp': 'isp',
        'ip_version': 'ip_version',
        'ip_address': 'ip_address',
        'ipv6_address': 'ipv6_address',
        'freezen': 'freezen',
        'freezen_info': 'freezen_info',
        'polluted': 'polluted',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'internet_bandwidth_info': 'internet_bandwidth_info',
        'global_connection_bandwidth_info': 'global_connection_bandwidth_info',
        'associate_instance_info': 'associate_instance_info',
        'is_pre_paid': 'is_pre_paid',
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, description=None, domain_id=None, access_site=None, geip_pool_name=None, isp=None, ip_version=None, ip_address=None, ipv6_address=None, freezen=None, freezen_info=None, polluted=None, status=None, created_at=None, updated_at=None, internet_bandwidth_info=None, global_connection_bandwidth_info=None, associate_instance_info=None, is_pre_paid=None, tags=None, sys_tags=None, enterprise_project_id=None):
        """ShowGlobalEip

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param name: 资源名称
        :type name: str
        :param description: 用户自定义的资源描述
        :type description: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param access_site: 接入点信息
        :type access_site: str
        :param geip_pool_name: 全域弹性公网IP池子名称
        :type geip_pool_name: str
        :param isp: 线路
        :type isp: str
        :param ip_version: IPv4或IPv6
        :type ip_version: int
        :param ip_address: IPv4地址
        :type ip_address: str
        :param ipv6_address: IPv6地址
        :type ipv6_address: str
        :param freezen: 是否冻结
        :type freezen: bool
        :param freezen_info: 冻结原因
        :type freezen_info: str
        :param polluted: 是否污染
        :type polluted: bool
        :param status: 状态
        :type status: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param internet_bandwidth_info: 
        :type internet_bandwidth_info: :class:`huaweicloudsdkgeip.v3.InternetBandwidthInfo`
        :param global_connection_bandwidth_info: 
        :type global_connection_bandwidth_info: :class:`huaweicloudsdkgeip.v3.GlobalConnectionBandwidthInfo`
        :param associate_instance_info: 
        :type associate_instance_info: :class:`huaweicloudsdkgeip.v3.InstanceInfo`
        :param is_pre_paid: 是否包周期
        :type is_pre_paid: bool
        :param tags: 全域弹性公网IP标签
        :type tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        :param sys_tags: 系统标签
        :type sys_tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        :param enterprise_project_id: 资源的企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._domain_id = None
        self._access_site = None
        self._geip_pool_name = None
        self._isp = None
        self._ip_version = None
        self._ip_address = None
        self._ipv6_address = None
        self._freezen = None
        self._freezen_info = None
        self._polluted = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._internet_bandwidth_info = None
        self._global_connection_bandwidth_info = None
        self._associate_instance_info = None
        self._is_pre_paid = None
        self._tags = None
        self._sys_tags = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if domain_id is not None:
            self.domain_id = domain_id
        if access_site is not None:
            self.access_site = access_site
        if geip_pool_name is not None:
            self.geip_pool_name = geip_pool_name
        if isp is not None:
            self.isp = isp
        if ip_version is not None:
            self.ip_version = ip_version
        if ip_address is not None:
            self.ip_address = ip_address
        if ipv6_address is not None:
            self.ipv6_address = ipv6_address
        if freezen is not None:
            self.freezen = freezen
        if freezen_info is not None:
            self.freezen_info = freezen_info
        if polluted is not None:
            self.polluted = polluted
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if internet_bandwidth_info is not None:
            self.internet_bandwidth_info = internet_bandwidth_info
        if global_connection_bandwidth_info is not None:
            self.global_connection_bandwidth_info = global_connection_bandwidth_info
        if associate_instance_info is not None:
            self.associate_instance_info = associate_instance_info
        if is_pre_paid is not None:
            self.is_pre_paid = is_pre_paid
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this ShowGlobalEip.

        ID

        :return: The id of this ShowGlobalEip.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowGlobalEip.

        ID

        :param id: The id of this ShowGlobalEip.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowGlobalEip.

        资源名称

        :return: The name of this ShowGlobalEip.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowGlobalEip.

        资源名称

        :param name: The name of this ShowGlobalEip.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowGlobalEip.

        用户自定义的资源描述

        :return: The description of this ShowGlobalEip.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowGlobalEip.

        用户自定义的资源描述

        :param description: The description of this ShowGlobalEip.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowGlobalEip.

        租户ID

        :return: The domain_id of this ShowGlobalEip.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowGlobalEip.

        租户ID

        :param domain_id: The domain_id of this ShowGlobalEip.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def access_site(self):
        """Gets the access_site of this ShowGlobalEip.

        接入点信息

        :return: The access_site of this ShowGlobalEip.
        :rtype: str
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        """Sets the access_site of this ShowGlobalEip.

        接入点信息

        :param access_site: The access_site of this ShowGlobalEip.
        :type access_site: str
        """
        self._access_site = access_site

    @property
    def geip_pool_name(self):
        """Gets the geip_pool_name of this ShowGlobalEip.

        全域弹性公网IP池子名称

        :return: The geip_pool_name of this ShowGlobalEip.
        :rtype: str
        """
        return self._geip_pool_name

    @geip_pool_name.setter
    def geip_pool_name(self, geip_pool_name):
        """Sets the geip_pool_name of this ShowGlobalEip.

        全域弹性公网IP池子名称

        :param geip_pool_name: The geip_pool_name of this ShowGlobalEip.
        :type geip_pool_name: str
        """
        self._geip_pool_name = geip_pool_name

    @property
    def isp(self):
        """Gets the isp of this ShowGlobalEip.

        线路

        :return: The isp of this ShowGlobalEip.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ShowGlobalEip.

        线路

        :param isp: The isp of this ShowGlobalEip.
        :type isp: str
        """
        self._isp = isp

    @property
    def ip_version(self):
        """Gets the ip_version of this ShowGlobalEip.

        IPv4或IPv6

        :return: The ip_version of this ShowGlobalEip.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ShowGlobalEip.

        IPv4或IPv6

        :param ip_version: The ip_version of this ShowGlobalEip.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def ip_address(self):
        """Gets the ip_address of this ShowGlobalEip.

        IPv4地址

        :return: The ip_address of this ShowGlobalEip.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ShowGlobalEip.

        IPv4地址

        :param ip_address: The ip_address of this ShowGlobalEip.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def ipv6_address(self):
        """Gets the ipv6_address of this ShowGlobalEip.

        IPv6地址

        :return: The ipv6_address of this ShowGlobalEip.
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """Sets the ipv6_address of this ShowGlobalEip.

        IPv6地址

        :param ipv6_address: The ipv6_address of this ShowGlobalEip.
        :type ipv6_address: str
        """
        self._ipv6_address = ipv6_address

    @property
    def freezen(self):
        """Gets the freezen of this ShowGlobalEip.

        是否冻结

        :return: The freezen of this ShowGlobalEip.
        :rtype: bool
        """
        return self._freezen

    @freezen.setter
    def freezen(self, freezen):
        """Sets the freezen of this ShowGlobalEip.

        是否冻结

        :param freezen: The freezen of this ShowGlobalEip.
        :type freezen: bool
        """
        self._freezen = freezen

    @property
    def freezen_info(self):
        """Gets the freezen_info of this ShowGlobalEip.

        冻结原因

        :return: The freezen_info of this ShowGlobalEip.
        :rtype: str
        """
        return self._freezen_info

    @freezen_info.setter
    def freezen_info(self, freezen_info):
        """Sets the freezen_info of this ShowGlobalEip.

        冻结原因

        :param freezen_info: The freezen_info of this ShowGlobalEip.
        :type freezen_info: str
        """
        self._freezen_info = freezen_info

    @property
    def polluted(self):
        """Gets the polluted of this ShowGlobalEip.

        是否污染

        :return: The polluted of this ShowGlobalEip.
        :rtype: bool
        """
        return self._polluted

    @polluted.setter
    def polluted(self, polluted):
        """Sets the polluted of this ShowGlobalEip.

        是否污染

        :param polluted: The polluted of this ShowGlobalEip.
        :type polluted: bool
        """
        self._polluted = polluted

    @property
    def status(self):
        """Gets the status of this ShowGlobalEip.

        状态

        :return: The status of this ShowGlobalEip.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowGlobalEip.

        状态

        :param status: The status of this ShowGlobalEip.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this ShowGlobalEip.

        创建时间

        :return: The created_at of this ShowGlobalEip.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowGlobalEip.

        创建时间

        :param created_at: The created_at of this ShowGlobalEip.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShowGlobalEip.

        更新时间

        :return: The updated_at of this ShowGlobalEip.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShowGlobalEip.

        更新时间

        :param updated_at: The updated_at of this ShowGlobalEip.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def internet_bandwidth_info(self):
        """Gets the internet_bandwidth_info of this ShowGlobalEip.

        :return: The internet_bandwidth_info of this ShowGlobalEip.
        :rtype: :class:`huaweicloudsdkgeip.v3.InternetBandwidthInfo`
        """
        return self._internet_bandwidth_info

    @internet_bandwidth_info.setter
    def internet_bandwidth_info(self, internet_bandwidth_info):
        """Sets the internet_bandwidth_info of this ShowGlobalEip.

        :param internet_bandwidth_info: The internet_bandwidth_info of this ShowGlobalEip.
        :type internet_bandwidth_info: :class:`huaweicloudsdkgeip.v3.InternetBandwidthInfo`
        """
        self._internet_bandwidth_info = internet_bandwidth_info

    @property
    def global_connection_bandwidth_info(self):
        """Gets the global_connection_bandwidth_info of this ShowGlobalEip.

        :return: The global_connection_bandwidth_info of this ShowGlobalEip.
        :rtype: :class:`huaweicloudsdkgeip.v3.GlobalConnectionBandwidthInfo`
        """
        return self._global_connection_bandwidth_info

    @global_connection_bandwidth_info.setter
    def global_connection_bandwidth_info(self, global_connection_bandwidth_info):
        """Sets the global_connection_bandwidth_info of this ShowGlobalEip.

        :param global_connection_bandwidth_info: The global_connection_bandwidth_info of this ShowGlobalEip.
        :type global_connection_bandwidth_info: :class:`huaweicloudsdkgeip.v3.GlobalConnectionBandwidthInfo`
        """
        self._global_connection_bandwidth_info = global_connection_bandwidth_info

    @property
    def associate_instance_info(self):
        """Gets the associate_instance_info of this ShowGlobalEip.

        :return: The associate_instance_info of this ShowGlobalEip.
        :rtype: :class:`huaweicloudsdkgeip.v3.InstanceInfo`
        """
        return self._associate_instance_info

    @associate_instance_info.setter
    def associate_instance_info(self, associate_instance_info):
        """Sets the associate_instance_info of this ShowGlobalEip.

        :param associate_instance_info: The associate_instance_info of this ShowGlobalEip.
        :type associate_instance_info: :class:`huaweicloudsdkgeip.v3.InstanceInfo`
        """
        self._associate_instance_info = associate_instance_info

    @property
    def is_pre_paid(self):
        """Gets the is_pre_paid of this ShowGlobalEip.

        是否包周期

        :return: The is_pre_paid of this ShowGlobalEip.
        :rtype: bool
        """
        return self._is_pre_paid

    @is_pre_paid.setter
    def is_pre_paid(self, is_pre_paid):
        """Sets the is_pre_paid of this ShowGlobalEip.

        是否包周期

        :param is_pre_paid: The is_pre_paid of this ShowGlobalEip.
        :type is_pre_paid: bool
        """
        self._is_pre_paid = is_pre_paid

    @property
    def tags(self):
        """Gets the tags of this ShowGlobalEip.

        全域弹性公网IP标签

        :return: The tags of this ShowGlobalEip.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowGlobalEip.

        全域弹性公网IP标签

        :param tags: The tags of this ShowGlobalEip.
        :type tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ShowGlobalEip.

        系统标签

        :return: The sys_tags of this ShowGlobalEip.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ShowGlobalEip.

        系统标签

        :param sys_tags: The sys_tags of this ShowGlobalEip.
        :type sys_tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        self._sys_tags = sys_tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowGlobalEip.

        资源的企业项目id

        :return: The enterprise_project_id of this ShowGlobalEip.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowGlobalEip.

        资源的企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ShowGlobalEip.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowGlobalEip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
