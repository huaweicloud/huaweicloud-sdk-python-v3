# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateInternetBandwidth:

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
        'isp': 'str',
        'ingress_size': 'int',
        'access_site': 'str',
        'size': 'int',
        'description': 'str',
        'charge_mode': 'str',
        'domain_id': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'ret_status': 'str',
        'tags': 'list[Tag]',
        'sys_tags': 'list[Tag]',
        'enterprise_project_id': 'str',
        'type': 'str',
        'lock_infos': 'list[LockInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'isp': 'isp',
        'ingress_size': 'ingress_size',
        'access_site': 'access_site',
        'size': 'size',
        'description': 'description',
        'charge_mode': 'charge_mode',
        'domain_id': 'domain_id',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'ret_status': 'ret_status',
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'lock_infos': 'lock_infos'
    }

    def __init__(self, id=None, name=None, isp=None, ingress_size=None, access_site=None, size=None, description=None, charge_mode=None, domain_id=None, status=None, created_at=None, updated_at=None, ret_status=None, tags=None, sys_tags=None, enterprise_project_id=None, type=None, lock_infos=None):
        """BatchCreateInternetBandwidth

        The model defined in huaweicloud sdk

        :param id: 全域公网带宽的ID
        :type id: str
        :param name: - 功能说明：全域公网带宽名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param isp: 全域弹性公网IP所属线路
        :type isp: str
        :param ingress_size: 全域公网带宽大小（入云方向）
        :type ingress_size: int
        :param access_site: 接入点信息
        :type access_site: str
        :param size: 全域公网带宽大小（出云方向）
        :type size: int
        :param description: - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。
        :type description: str
        :param charge_mode: 计费模式
        :type charge_mode: str
        :param domain_id: - 租户账号ID，获取租户账号ID请参见[租户账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)
        :type domain_id: str
        :param status: 状态
        :type status: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param ret_status: 是否创建成功标识，取值：successful、failed。
        :type ret_status: str
        :param tags: 全域公网带宽标签
        :type tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        :param sys_tags: 系统标签
        :type sys_tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        :param enterprise_project_id: - 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。 - 创建全域弹性公网IP时，给全域弹性公网IP绑定企业项目ID。 - 不指定该参数时，默认值是 0 - 关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。
        :type enterprise_project_id: str
        :param type: 全域公网带宽类型
        :type type: str
        :param lock_infos: 全域公网带宽资源的锁状态
        :type lock_infos: list[:class:`huaweicloudsdkgeip.v3.LockInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._isp = None
        self._ingress_size = None
        self._access_site = None
        self._size = None
        self._description = None
        self._charge_mode = None
        self._domain_id = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._ret_status = None
        self._tags = None
        self._sys_tags = None
        self._enterprise_project_id = None
        self._type = None
        self._lock_infos = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        self.isp = isp
        if ingress_size is not None:
            self.ingress_size = ingress_size
        self.access_site = access_site
        self.size = size
        if description is not None:
            self.description = description
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if domain_id is not None:
            self.domain_id = domain_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if ret_status is not None:
            self.ret_status = ret_status
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        if lock_infos is not None:
            self.lock_infos = lock_infos

    @property
    def id(self):
        """Gets the id of this BatchCreateInternetBandwidth.

        全域公网带宽的ID

        :return: The id of this BatchCreateInternetBandwidth.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchCreateInternetBandwidth.

        全域公网带宽的ID

        :param id: The id of this BatchCreateInternetBandwidth.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BatchCreateInternetBandwidth.

        - 功能说明：全域公网带宽名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this BatchCreateInternetBandwidth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchCreateInternetBandwidth.

        - 功能说明：全域公网带宽名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this BatchCreateInternetBandwidth.
        :type name: str
        """
        self._name = name

    @property
    def isp(self):
        """Gets the isp of this BatchCreateInternetBandwidth.

        全域弹性公网IP所属线路

        :return: The isp of this BatchCreateInternetBandwidth.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this BatchCreateInternetBandwidth.

        全域弹性公网IP所属线路

        :param isp: The isp of this BatchCreateInternetBandwidth.
        :type isp: str
        """
        self._isp = isp

    @property
    def ingress_size(self):
        """Gets the ingress_size of this BatchCreateInternetBandwidth.

        全域公网带宽大小（入云方向）

        :return: The ingress_size of this BatchCreateInternetBandwidth.
        :rtype: int
        """
        return self._ingress_size

    @ingress_size.setter
    def ingress_size(self, ingress_size):
        """Sets the ingress_size of this BatchCreateInternetBandwidth.

        全域公网带宽大小（入云方向）

        :param ingress_size: The ingress_size of this BatchCreateInternetBandwidth.
        :type ingress_size: int
        """
        self._ingress_size = ingress_size

    @property
    def access_site(self):
        """Gets the access_site of this BatchCreateInternetBandwidth.

        接入点信息

        :return: The access_site of this BatchCreateInternetBandwidth.
        :rtype: str
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        """Sets the access_site of this BatchCreateInternetBandwidth.

        接入点信息

        :param access_site: The access_site of this BatchCreateInternetBandwidth.
        :type access_site: str
        """
        self._access_site = access_site

    @property
    def size(self):
        """Gets the size of this BatchCreateInternetBandwidth.

        全域公网带宽大小（出云方向）

        :return: The size of this BatchCreateInternetBandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BatchCreateInternetBandwidth.

        全域公网带宽大小（出云方向）

        :param size: The size of this BatchCreateInternetBandwidth.
        :type size: int
        """
        self._size = size

    @property
    def description(self):
        """Gets the description of this BatchCreateInternetBandwidth.

        - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。

        :return: The description of this BatchCreateInternetBandwidth.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BatchCreateInternetBandwidth.

        - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。

        :param description: The description of this BatchCreateInternetBandwidth.
        :type description: str
        """
        self._description = description

    @property
    def charge_mode(self):
        """Gets the charge_mode of this BatchCreateInternetBandwidth.

        计费模式

        :return: The charge_mode of this BatchCreateInternetBandwidth.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this BatchCreateInternetBandwidth.

        计费模式

        :param charge_mode: The charge_mode of this BatchCreateInternetBandwidth.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def domain_id(self):
        """Gets the domain_id of this BatchCreateInternetBandwidth.

        - 租户账号ID，获取租户账号ID请参见[租户账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)

        :return: The domain_id of this BatchCreateInternetBandwidth.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this BatchCreateInternetBandwidth.

        - 租户账号ID，获取租户账号ID请参见[租户账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)

        :param domain_id: The domain_id of this BatchCreateInternetBandwidth.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def status(self):
        """Gets the status of this BatchCreateInternetBandwidth.

        状态

        :return: The status of this BatchCreateInternetBandwidth.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchCreateInternetBandwidth.

        状态

        :param status: The status of this BatchCreateInternetBandwidth.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this BatchCreateInternetBandwidth.

        创建时间

        :return: The created_at of this BatchCreateInternetBandwidth.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BatchCreateInternetBandwidth.

        创建时间

        :param created_at: The created_at of this BatchCreateInternetBandwidth.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this BatchCreateInternetBandwidth.

        更新时间

        :return: The updated_at of this BatchCreateInternetBandwidth.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BatchCreateInternetBandwidth.

        更新时间

        :param updated_at: The updated_at of this BatchCreateInternetBandwidth.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def ret_status(self):
        """Gets the ret_status of this BatchCreateInternetBandwidth.

        是否创建成功标识，取值：successful、failed。

        :return: The ret_status of this BatchCreateInternetBandwidth.
        :rtype: str
        """
        return self._ret_status

    @ret_status.setter
    def ret_status(self, ret_status):
        """Sets the ret_status of this BatchCreateInternetBandwidth.

        是否创建成功标识，取值：successful、failed。

        :param ret_status: The ret_status of this BatchCreateInternetBandwidth.
        :type ret_status: str
        """
        self._ret_status = ret_status

    @property
    def tags(self):
        """Gets the tags of this BatchCreateInternetBandwidth.

        全域公网带宽标签

        :return: The tags of this BatchCreateInternetBandwidth.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BatchCreateInternetBandwidth.

        全域公网带宽标签

        :param tags: The tags of this BatchCreateInternetBandwidth.
        :type tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        """Gets the sys_tags of this BatchCreateInternetBandwidth.

        系统标签

        :return: The sys_tags of this BatchCreateInternetBandwidth.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this BatchCreateInternetBandwidth.

        系统标签

        :param sys_tags: The sys_tags of this BatchCreateInternetBandwidth.
        :type sys_tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        self._sys_tags = sys_tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this BatchCreateInternetBandwidth.

        - 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。 - 创建全域弹性公网IP时，给全域弹性公网IP绑定企业项目ID。 - 不指定该参数时，默认值是 0 - 关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :return: The enterprise_project_id of this BatchCreateInternetBandwidth.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this BatchCreateInternetBandwidth.

        - 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。 - 创建全域弹性公网IP时，给全域弹性公网IP绑定企业项目ID。 - 不指定该参数时，默认值是 0 - 关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :param enterprise_project_id: The enterprise_project_id of this BatchCreateInternetBandwidth.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        """Gets the type of this BatchCreateInternetBandwidth.

        全域公网带宽类型

        :return: The type of this BatchCreateInternetBandwidth.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchCreateInternetBandwidth.

        全域公网带宽类型

        :param type: The type of this BatchCreateInternetBandwidth.
        :type type: str
        """
        self._type = type

    @property
    def lock_infos(self):
        """Gets the lock_infos of this BatchCreateInternetBandwidth.

        全域公网带宽资源的锁状态

        :return: The lock_infos of this BatchCreateInternetBandwidth.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.LockInfo`]
        """
        return self._lock_infos

    @lock_infos.setter
    def lock_infos(self, lock_infos):
        """Sets the lock_infos of this BatchCreateInternetBandwidth.

        全域公网带宽资源的锁状态

        :param lock_infos: The lock_infos of this BatchCreateInternetBandwidth.
        :type lock_infos: list[:class:`huaweicloudsdkgeip.v3.LockInfo`]
        """
        self._lock_infos = lock_infos

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
        if not isinstance(other, BatchCreateInternetBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
