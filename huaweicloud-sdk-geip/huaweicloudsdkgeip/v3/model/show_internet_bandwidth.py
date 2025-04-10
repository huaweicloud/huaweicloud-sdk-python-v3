# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInternetBandwidth:

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
        'ratio_95peak': 'int',
        'billing_info': 'str',
        'freezen_info': 'str',
        'domain_id': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'is_pre_paid': 'bool',
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
        'ratio_95peak': 'ratio_95peak',
        'billing_info': 'billing_info',
        'freezen_info': 'freezen_info',
        'domain_id': 'domain_id',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'is_pre_paid': 'is_pre_paid',
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'lock_infos': 'lock_infos'
    }

    def __init__(self, id=None, name=None, isp=None, ingress_size=None, access_site=None, size=None, description=None, charge_mode=None, ratio_95peak=None, billing_info=None, freezen_info=None, domain_id=None, status=None, created_at=None, updated_at=None, is_pre_paid=None, tags=None, sys_tags=None, enterprise_project_id=None, type=None, lock_infos=None):
        r"""ShowInternetBandwidth

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
        :param ratio_95peak: 增强95保底率
        :type ratio_95peak: int
        :param billing_info: 订单信息
        :type billing_info: str
        :param freezen_info: 冻结原因
        :type freezen_info: str
        :param domain_id: - 租户账号ID，获取租户账号ID请参见[租户账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)
        :type domain_id: str
        :param status: 状态
        :type status: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param is_pre_paid: 是否包周期
        :type is_pre_paid: bool
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
        self._ratio_95peak = None
        self._billing_info = None
        self._freezen_info = None
        self._domain_id = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._is_pre_paid = None
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
        if isp is not None:
            self.isp = isp
        if ingress_size is not None:
            self.ingress_size = ingress_size
        if access_site is not None:
            self.access_site = access_site
        if size is not None:
            self.size = size
        if description is not None:
            self.description = description
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if ratio_95peak is not None:
            self.ratio_95peak = ratio_95peak
        if billing_info is not None:
            self.billing_info = billing_info
        if freezen_info is not None:
            self.freezen_info = freezen_info
        if domain_id is not None:
            self.domain_id = domain_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if is_pre_paid is not None:
            self.is_pre_paid = is_pre_paid
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
        r"""Gets the id of this ShowInternetBandwidth.

        全域公网带宽的ID

        :return: The id of this ShowInternetBandwidth.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowInternetBandwidth.

        全域公网带宽的ID

        :param id: The id of this ShowInternetBandwidth.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowInternetBandwidth.

        - 功能说明：全域公网带宽名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this ShowInternetBandwidth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowInternetBandwidth.

        - 功能说明：全域公网带宽名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this ShowInternetBandwidth.
        :type name: str
        """
        self._name = name

    @property
    def isp(self):
        r"""Gets the isp of this ShowInternetBandwidth.

        全域弹性公网IP所属线路

        :return: The isp of this ShowInternetBandwidth.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        r"""Sets the isp of this ShowInternetBandwidth.

        全域弹性公网IP所属线路

        :param isp: The isp of this ShowInternetBandwidth.
        :type isp: str
        """
        self._isp = isp

    @property
    def ingress_size(self):
        r"""Gets the ingress_size of this ShowInternetBandwidth.

        全域公网带宽大小（入云方向）

        :return: The ingress_size of this ShowInternetBandwidth.
        :rtype: int
        """
        return self._ingress_size

    @ingress_size.setter
    def ingress_size(self, ingress_size):
        r"""Sets the ingress_size of this ShowInternetBandwidth.

        全域公网带宽大小（入云方向）

        :param ingress_size: The ingress_size of this ShowInternetBandwidth.
        :type ingress_size: int
        """
        self._ingress_size = ingress_size

    @property
    def access_site(self):
        r"""Gets the access_site of this ShowInternetBandwidth.

        接入点信息

        :return: The access_site of this ShowInternetBandwidth.
        :rtype: str
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        r"""Sets the access_site of this ShowInternetBandwidth.

        接入点信息

        :param access_site: The access_site of this ShowInternetBandwidth.
        :type access_site: str
        """
        self._access_site = access_site

    @property
    def size(self):
        r"""Gets the size of this ShowInternetBandwidth.

        全域公网带宽大小（出云方向）

        :return: The size of this ShowInternetBandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowInternetBandwidth.

        全域公网带宽大小（出云方向）

        :param size: The size of this ShowInternetBandwidth.
        :type size: int
        """
        self._size = size

    @property
    def description(self):
        r"""Gets the description of this ShowInternetBandwidth.

        - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。

        :return: The description of this ShowInternetBandwidth.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowInternetBandwidth.

        - 功能说明：用户自定义的资源描述 - 约束：   - 值的长度最大512字符，由数字、字母、中文、_(下划线)、-（中划线）、.（点）组成。

        :param description: The description of this ShowInternetBandwidth.
        :type description: str
        """
        self._description = description

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this ShowInternetBandwidth.

        计费模式

        :return: The charge_mode of this ShowInternetBandwidth.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this ShowInternetBandwidth.

        计费模式

        :param charge_mode: The charge_mode of this ShowInternetBandwidth.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def ratio_95peak(self):
        r"""Gets the ratio_95peak of this ShowInternetBandwidth.

        增强95保底率

        :return: The ratio_95peak of this ShowInternetBandwidth.
        :rtype: int
        """
        return self._ratio_95peak

    @ratio_95peak.setter
    def ratio_95peak(self, ratio_95peak):
        r"""Sets the ratio_95peak of this ShowInternetBandwidth.

        增强95保底率

        :param ratio_95peak: The ratio_95peak of this ShowInternetBandwidth.
        :type ratio_95peak: int
        """
        self._ratio_95peak = ratio_95peak

    @property
    def billing_info(self):
        r"""Gets the billing_info of this ShowInternetBandwidth.

        订单信息

        :return: The billing_info of this ShowInternetBandwidth.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        r"""Sets the billing_info of this ShowInternetBandwidth.

        订单信息

        :param billing_info: The billing_info of this ShowInternetBandwidth.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def freezen_info(self):
        r"""Gets the freezen_info of this ShowInternetBandwidth.

        冻结原因

        :return: The freezen_info of this ShowInternetBandwidth.
        :rtype: str
        """
        return self._freezen_info

    @freezen_info.setter
    def freezen_info(self, freezen_info):
        r"""Sets the freezen_info of this ShowInternetBandwidth.

        冻结原因

        :param freezen_info: The freezen_info of this ShowInternetBandwidth.
        :type freezen_info: str
        """
        self._freezen_info = freezen_info

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowInternetBandwidth.

        - 租户账号ID，获取租户账号ID请参见[租户账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)

        :return: The domain_id of this ShowInternetBandwidth.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowInternetBandwidth.

        - 租户账号ID，获取租户账号ID请参见[租户账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)

        :param domain_id: The domain_id of this ShowInternetBandwidth.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def status(self):
        r"""Gets the status of this ShowInternetBandwidth.

        状态

        :return: The status of this ShowInternetBandwidth.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowInternetBandwidth.

        状态

        :param status: The status of this ShowInternetBandwidth.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowInternetBandwidth.

        创建时间

        :return: The created_at of this ShowInternetBandwidth.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowInternetBandwidth.

        创建时间

        :param created_at: The created_at of this ShowInternetBandwidth.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowInternetBandwidth.

        更新时间

        :return: The updated_at of this ShowInternetBandwidth.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowInternetBandwidth.

        更新时间

        :param updated_at: The updated_at of this ShowInternetBandwidth.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def is_pre_paid(self):
        r"""Gets the is_pre_paid of this ShowInternetBandwidth.

        是否包周期

        :return: The is_pre_paid of this ShowInternetBandwidth.
        :rtype: bool
        """
        return self._is_pre_paid

    @is_pre_paid.setter
    def is_pre_paid(self, is_pre_paid):
        r"""Sets the is_pre_paid of this ShowInternetBandwidth.

        是否包周期

        :param is_pre_paid: The is_pre_paid of this ShowInternetBandwidth.
        :type is_pre_paid: bool
        """
        self._is_pre_paid = is_pre_paid

    @property
    def tags(self):
        r"""Gets the tags of this ShowInternetBandwidth.

        全域公网带宽标签

        :return: The tags of this ShowInternetBandwidth.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowInternetBandwidth.

        全域公网带宽标签

        :param tags: The tags of this ShowInternetBandwidth.
        :type tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ShowInternetBandwidth.

        系统标签

        :return: The sys_tags of this ShowInternetBandwidth.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ShowInternetBandwidth.

        系统标签

        :param sys_tags: The sys_tags of this ShowInternetBandwidth.
        :type sys_tags: list[:class:`huaweicloudsdkgeip.v3.Tag`]
        """
        self._sys_tags = sys_tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowInternetBandwidth.

        - 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。 - 创建全域弹性公网IP时，给全域弹性公网IP绑定企业项目ID。 - 不指定该参数时，默认值是 0 - 关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :return: The enterprise_project_id of this ShowInternetBandwidth.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowInternetBandwidth.

        - 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。 - 创建全域弹性公网IP时，给全域弹性公网IP绑定企业项目ID。 - 不指定该参数时，默认值是 0 - 关于企业项目ID的获取及企业项目特性的详细信息，请参见[《企业管理用户指南》](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)。

        :param enterprise_project_id: The enterprise_project_id of this ShowInternetBandwidth.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this ShowInternetBandwidth.

        全域公网带宽类型

        :return: The type of this ShowInternetBandwidth.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowInternetBandwidth.

        全域公网带宽类型

        :param type: The type of this ShowInternetBandwidth.
        :type type: str
        """
        self._type = type

    @property
    def lock_infos(self):
        r"""Gets the lock_infos of this ShowInternetBandwidth.

        全域公网带宽资源的锁状态

        :return: The lock_infos of this ShowInternetBandwidth.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.LockInfo`]
        """
        return self._lock_infos

    @lock_infos.setter
    def lock_infos(self, lock_infos):
        r"""Sets the lock_infos of this ShowInternetBandwidth.

        全域公网带宽资源的锁状态

        :param lock_infos: The lock_infos of this ShowInternetBandwidth.
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
        if not isinstance(other, ShowInternetBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
