# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_state': 'str',
        'ingress_size': 'int',
        'rule_quota': 'int',
        'ratio_95peak_plus': 'int',
        'enable_bandwidth_rules': 'bool',
        'bandwidth_rules': 'list[BandWidthRules]',
        'public_border_group': 'str',
        'bandwidth_type': 'str',
        'billinginfo': 'str',
        'id': 'str',
        'name': 'str',
        'publicip_info': 'list[PublicipInfoResponseBody]',
        'type': 'str',
        'size': 'int',
        'project_id': 'str',
        'tags': 'list[str]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'admin_state': 'admin_state',
        'ingress_size': 'ingress_size',
        'rule_quota': 'rule_quota',
        'ratio_95peak_plus': 'ratio_95peak_plus',
        'enable_bandwidth_rules': 'enable_bandwidth_rules',
        'bandwidth_rules': 'bandwidth_rules',
        'public_border_group': 'public_border_group',
        'bandwidth_type': 'bandwidth_type',
        'billinginfo': 'billinginfo',
        'id': 'id',
        'name': 'name',
        'publicip_info': 'publicip_info',
        'type': 'type',
        'size': 'size',
        'project_id': 'project_id',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, admin_state=None, ingress_size=None, rule_quota=None, ratio_95peak_plus=None, enable_bandwidth_rules=None, bandwidth_rules=None, public_border_group=None, bandwidth_type=None, billinginfo=None, id=None, name=None, publicip_info=None, type=None, size=None, project_id=None, tags=None, created_at=None, updated_at=None):
        r"""BandwidthResponseBody

        The model defined in huaweicloud sdk

        :param admin_state: - 功能说明：带宽状态 - 取值范围：normal，freezed
        :type admin_state: str
        :param ingress_size: - 功能说明：入网大小，单位Mbit/s
        :type ingress_size: int
        :param rule_quota: - 功能说明：规则数值，最低阈值可调节
        :type rule_quota: int
        :param ratio_95peak_plus: - 功能说明：增强型95带宽保底率，最低保底率为20
        :type ratio_95peak_plus: int
        :param enable_bandwidth_rules: - 功能说明：带宽分组使能，表明开启带宽分组限速功能。
        :type enable_bandwidth_rules: bool
        :param bandwidth_rules: - 功能说明：带宽规则对象（该字段仅在上海1局点返回）
        :type bandwidth_rules: list[:class:`huaweicloudsdkeip.v3.BandWidthRules`]
        :param public_border_group: - 功能说明：带宽AZ属性，表征中心和边缘。中心带宽默认为center
        :type public_border_group: str
        :param bandwidth_type: - 功能说明：带宽类型，共享带宽默认为share。 - 取值范围：share，bgp，telcom，sbgp等。  share：共享带宽；  bgp：动态bgp；  telcom ：联通；  sbgp：静态bgp。
        :type bandwidth_type: str
        :param billinginfo: - 功能说明：账单信息，
        :type billinginfo: str
        :param id: - 功能说明：带宽唯一标识
        :type id: str
        :param name: - 功能说明：带宽名称 - 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param publicip_info: - 功能说明：带宽对应的弹性公网IP信息 - 约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP
        :type publicip_info: list[:class:`huaweicloudsdkeip.v3.PublicipInfoResponseBody`]
        :param type: - 功能说明：带宽类型，标识是否是共享带宽 - 取值范围：WHOLE，PER。  WHOLE表示共享带宽；PER表示独享带宽
        :type type: str
        :param size: - 功能说明：带宽大小 - 取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。
        :type size: int
        :param project_id: - 功能说明：用户所属项目ID
        :type project_id: str
        :param tags: - 功能说明：\&quot;公网EIP标签\&quot;
        :type tags: list[str]
        :param created_at: - 功能说明：资源创建时间，采用UTC时间，格式：YYYY-MM-DDTHH:MM:SS
        :type created_at: datetime
        :param updated_at: - 功能说明：资源更新时间，采用UTC时间，格式：YYYY-MM-DDTHH:MM:SS
        :type updated_at: datetime
        """
        
        

        self._admin_state = None
        self._ingress_size = None
        self._rule_quota = None
        self._ratio_95peak_plus = None
        self._enable_bandwidth_rules = None
        self._bandwidth_rules = None
        self._public_border_group = None
        self._bandwidth_type = None
        self._billinginfo = None
        self._id = None
        self._name = None
        self._publicip_info = None
        self._type = None
        self._size = None
        self._project_id = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if admin_state is not None:
            self.admin_state = admin_state
        if ingress_size is not None:
            self.ingress_size = ingress_size
        if rule_quota is not None:
            self.rule_quota = rule_quota
        if ratio_95peak_plus is not None:
            self.ratio_95peak_plus = ratio_95peak_plus
        if enable_bandwidth_rules is not None:
            self.enable_bandwidth_rules = enable_bandwidth_rules
        if bandwidth_rules is not None:
            self.bandwidth_rules = bandwidth_rules
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type
        if billinginfo is not None:
            self.billinginfo = billinginfo
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if publicip_info is not None:
            self.publicip_info = publicip_info
        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        if project_id is not None:
            self.project_id = project_id
        if tags is not None:
            self.tags = tags
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def admin_state(self):
        r"""Gets the admin_state of this BandwidthResponseBody.

        - 功能说明：带宽状态 - 取值范围：normal，freezed

        :return: The admin_state of this BandwidthResponseBody.
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        r"""Sets the admin_state of this BandwidthResponseBody.

        - 功能说明：带宽状态 - 取值范围：normal，freezed

        :param admin_state: The admin_state of this BandwidthResponseBody.
        :type admin_state: str
        """
        self._admin_state = admin_state

    @property
    def ingress_size(self):
        r"""Gets the ingress_size of this BandwidthResponseBody.

        - 功能说明：入网大小，单位Mbit/s

        :return: The ingress_size of this BandwidthResponseBody.
        :rtype: int
        """
        return self._ingress_size

    @ingress_size.setter
    def ingress_size(self, ingress_size):
        r"""Sets the ingress_size of this BandwidthResponseBody.

        - 功能说明：入网大小，单位Mbit/s

        :param ingress_size: The ingress_size of this BandwidthResponseBody.
        :type ingress_size: int
        """
        self._ingress_size = ingress_size

    @property
    def rule_quota(self):
        r"""Gets the rule_quota of this BandwidthResponseBody.

        - 功能说明：规则数值，最低阈值可调节

        :return: The rule_quota of this BandwidthResponseBody.
        :rtype: int
        """
        return self._rule_quota

    @rule_quota.setter
    def rule_quota(self, rule_quota):
        r"""Sets the rule_quota of this BandwidthResponseBody.

        - 功能说明：规则数值，最低阈值可调节

        :param rule_quota: The rule_quota of this BandwidthResponseBody.
        :type rule_quota: int
        """
        self._rule_quota = rule_quota

    @property
    def ratio_95peak_plus(self):
        r"""Gets the ratio_95peak_plus of this BandwidthResponseBody.

        - 功能说明：增强型95带宽保底率，最低保底率为20

        :return: The ratio_95peak_plus of this BandwidthResponseBody.
        :rtype: int
        """
        return self._ratio_95peak_plus

    @ratio_95peak_plus.setter
    def ratio_95peak_plus(self, ratio_95peak_plus):
        r"""Sets the ratio_95peak_plus of this BandwidthResponseBody.

        - 功能说明：增强型95带宽保底率，最低保底率为20

        :param ratio_95peak_plus: The ratio_95peak_plus of this BandwidthResponseBody.
        :type ratio_95peak_plus: int
        """
        self._ratio_95peak_plus = ratio_95peak_plus

    @property
    def enable_bandwidth_rules(self):
        r"""Gets the enable_bandwidth_rules of this BandwidthResponseBody.

        - 功能说明：带宽分组使能，表明开启带宽分组限速功能。

        :return: The enable_bandwidth_rules of this BandwidthResponseBody.
        :rtype: bool
        """
        return self._enable_bandwidth_rules

    @enable_bandwidth_rules.setter
    def enable_bandwidth_rules(self, enable_bandwidth_rules):
        r"""Sets the enable_bandwidth_rules of this BandwidthResponseBody.

        - 功能说明：带宽分组使能，表明开启带宽分组限速功能。

        :param enable_bandwidth_rules: The enable_bandwidth_rules of this BandwidthResponseBody.
        :type enable_bandwidth_rules: bool
        """
        self._enable_bandwidth_rules = enable_bandwidth_rules

    @property
    def bandwidth_rules(self):
        r"""Gets the bandwidth_rules of this BandwidthResponseBody.

        - 功能说明：带宽规则对象（该字段仅在上海1局点返回）

        :return: The bandwidth_rules of this BandwidthResponseBody.
        :rtype: list[:class:`huaweicloudsdkeip.v3.BandWidthRules`]
        """
        return self._bandwidth_rules

    @bandwidth_rules.setter
    def bandwidth_rules(self, bandwidth_rules):
        r"""Sets the bandwidth_rules of this BandwidthResponseBody.

        - 功能说明：带宽规则对象（该字段仅在上海1局点返回）

        :param bandwidth_rules: The bandwidth_rules of this BandwidthResponseBody.
        :type bandwidth_rules: list[:class:`huaweicloudsdkeip.v3.BandWidthRules`]
        """
        self._bandwidth_rules = bandwidth_rules

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this BandwidthResponseBody.

        - 功能说明：带宽AZ属性，表征中心和边缘。中心带宽默认为center

        :return: The public_border_group of this BandwidthResponseBody.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this BandwidthResponseBody.

        - 功能说明：带宽AZ属性，表征中心和边缘。中心带宽默认为center

        :param public_border_group: The public_border_group of this BandwidthResponseBody.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def bandwidth_type(self):
        r"""Gets the bandwidth_type of this BandwidthResponseBody.

        - 功能说明：带宽类型，共享带宽默认为share。 - 取值范围：share，bgp，telcom，sbgp等。  share：共享带宽；  bgp：动态bgp；  telcom ：联通；  sbgp：静态bgp。

        :return: The bandwidth_type of this BandwidthResponseBody.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        r"""Sets the bandwidth_type of this BandwidthResponseBody.

        - 功能说明：带宽类型，共享带宽默认为share。 - 取值范围：share，bgp，telcom，sbgp等。  share：共享带宽；  bgp：动态bgp；  telcom ：联通；  sbgp：静态bgp。

        :param bandwidth_type: The bandwidth_type of this BandwidthResponseBody.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

    @property
    def billinginfo(self):
        r"""Gets the billinginfo of this BandwidthResponseBody.

        - 功能说明：账单信息，

        :return: The billinginfo of this BandwidthResponseBody.
        :rtype: str
        """
        return self._billinginfo

    @billinginfo.setter
    def billinginfo(self, billinginfo):
        r"""Sets the billinginfo of this BandwidthResponseBody.

        - 功能说明：账单信息，

        :param billinginfo: The billinginfo of this BandwidthResponseBody.
        :type billinginfo: str
        """
        self._billinginfo = billinginfo

    @property
    def id(self):
        r"""Gets the id of this BandwidthResponseBody.

        - 功能说明：带宽唯一标识

        :return: The id of this BandwidthResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BandwidthResponseBody.

        - 功能说明：带宽唯一标识

        :param id: The id of this BandwidthResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BandwidthResponseBody.

        - 功能说明：带宽名称 - 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this BandwidthResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BandwidthResponseBody.

        - 功能说明：带宽名称 - 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this BandwidthResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def publicip_info(self):
        r"""Gets the publicip_info of this BandwidthResponseBody.

        - 功能说明：带宽对应的弹性公网IP信息 - 约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP

        :return: The publicip_info of this BandwidthResponseBody.
        :rtype: list[:class:`huaweicloudsdkeip.v3.PublicipInfoResponseBody`]
        """
        return self._publicip_info

    @publicip_info.setter
    def publicip_info(self, publicip_info):
        r"""Sets the publicip_info of this BandwidthResponseBody.

        - 功能说明：带宽对应的弹性公网IP信息 - 约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP

        :param publicip_info: The publicip_info of this BandwidthResponseBody.
        :type publicip_info: list[:class:`huaweicloudsdkeip.v3.PublicipInfoResponseBody`]
        """
        self._publicip_info = publicip_info

    @property
    def type(self):
        r"""Gets the type of this BandwidthResponseBody.

        - 功能说明：带宽类型，标识是否是共享带宽 - 取值范围：WHOLE，PER。  WHOLE表示共享带宽；PER表示独享带宽

        :return: The type of this BandwidthResponseBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BandwidthResponseBody.

        - 功能说明：带宽类型，标识是否是共享带宽 - 取值范围：WHOLE，PER。  WHOLE表示共享带宽；PER表示独享带宽

        :param type: The type of this BandwidthResponseBody.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this BandwidthResponseBody.

        - 功能说明：带宽大小 - 取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。

        :return: The size of this BandwidthResponseBody.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BandwidthResponseBody.

        - 功能说明：带宽大小 - 取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。

        :param size: The size of this BandwidthResponseBody.
        :type size: int
        """
        self._size = size

    @property
    def project_id(self):
        r"""Gets the project_id of this BandwidthResponseBody.

        - 功能说明：用户所属项目ID

        :return: The project_id of this BandwidthResponseBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BandwidthResponseBody.

        - 功能说明：用户所属项目ID

        :param project_id: The project_id of this BandwidthResponseBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tags(self):
        r"""Gets the tags of this BandwidthResponseBody.

        - 功能说明：\"公网EIP标签\"

        :return: The tags of this BandwidthResponseBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BandwidthResponseBody.

        - 功能说明：\"公网EIP标签\"

        :param tags: The tags of this BandwidthResponseBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def created_at(self):
        r"""Gets the created_at of this BandwidthResponseBody.

        - 功能说明：资源创建时间，采用UTC时间，格式：YYYY-MM-DDTHH:MM:SS

        :return: The created_at of this BandwidthResponseBody.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this BandwidthResponseBody.

        - 功能说明：资源创建时间，采用UTC时间，格式：YYYY-MM-DDTHH:MM:SS

        :param created_at: The created_at of this BandwidthResponseBody.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this BandwidthResponseBody.

        - 功能说明：资源更新时间，采用UTC时间，格式：YYYY-MM-DDTHH:MM:SS

        :return: The updated_at of this BandwidthResponseBody.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this BandwidthResponseBody.

        - 功能说明：资源更新时间，采用UTC时间，格式：YYYY-MM-DDTHH:MM:SS

        :param updated_at: The updated_at of this BandwidthResponseBody.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, BandwidthResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
