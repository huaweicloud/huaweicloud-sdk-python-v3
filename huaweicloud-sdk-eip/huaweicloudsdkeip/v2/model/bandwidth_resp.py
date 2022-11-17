# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_type': 'str',
        'billing_info': 'str',
        'charge_mode': 'str',
        'id': 'str',
        'name': 'str',
        'publicip_info': 'list[PublicipInfoResp]',
        'share_type': 'str',
        'size': 'int',
        'tenant_id': 'str',
        'enterprise_project_id': 'str',
        'status': 'str',
        'enable_bandwidth_rules': 'bool',
        'rule_quota': 'int',
        'bandwidth_rules': 'list[BandWidthRules]',
        'created_at': 'str',
        'updated_at': 'str',
        'public_border_group': 'str'
    }

    attribute_map = {
        'bandwidth_type': 'bandwidth_type',
        'billing_info': 'billing_info',
        'charge_mode': 'charge_mode',
        'id': 'id',
        'name': 'name',
        'publicip_info': 'publicip_info',
        'share_type': 'share_type',
        'size': 'size',
        'tenant_id': 'tenant_id',
        'enterprise_project_id': 'enterprise_project_id',
        'status': 'status',
        'enable_bandwidth_rules': 'enable_bandwidth_rules',
        'rule_quota': 'rule_quota',
        'bandwidth_rules': 'bandwidth_rules',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, bandwidth_type=None, billing_info=None, charge_mode=None, id=None, name=None, publicip_info=None, share_type=None, size=None, tenant_id=None, enterprise_project_id=None, status=None, enable_bandwidth_rules=None, rule_quota=None, bandwidth_rules=None, created_at=None, updated_at=None, public_border_group=None):
        """BandwidthResp

        The model defined in huaweicloud sdk

        :param bandwidth_type: 功能说明：带宽类型，共享带宽默认为share。  取值范围：share，bgp，telcom，sbgp等。  share：共享带宽  bgp：动态bgp  telcom ：联通  sbgp：静态bgp
        :type bandwidth_type: str
        :param billing_info: 功能说明：账单信息  如果billinginfo不为空，说明是包周期的带宽
        :type billing_info: str
        :param charge_mode: 功能说明：按流量计费,按带宽计费还是按增强型95计费。  取值范围：bandwidth，traffic，95peak_plus(按增强型95计费)不返回或者为空时表示是bandwidth。  约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%。
        :type charge_mode: str
        :param id: 功能说明：带宽唯一标识
        :type id: str
        :param name: 功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param publicip_info: 功能说明：带宽对应的弹性公网IP信息  约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP
        :type publicip_info: list[:class:`huaweicloudsdkeip.v2.PublicipInfoResp`]
        :param share_type: 功能说明：带宽类型，标识是否是共享带宽  取值范围：WHOLE，PER  WHOLE表示共享带宽；PER，表示独享带宽
        :type share_type: str
        :param size: 功能说明：带宽大小  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。
        :type size: int
        :param tenant_id: 功能说明：用户所属租户ID
        :type tenant_id: str
        :param enterprise_project_id: 企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建带宽时，给带宽绑定企业项目ID。
        :type enterprise_project_id: str
        :param status: 功能说明：带宽的状态  取值范围：  FREEZED：冻结  NORMAL：正常
        :type status: str
        :param enable_bandwidth_rules: 功能说明：是否开启企业级qos，仅共享带宽支持开启。（该字段仅在上海1局点返回）
        :type enable_bandwidth_rules: bool
        :param rule_quota: 功能说明：带宽支持的最大分组规则数。（该字段仅在上海1局点返回）
        :type rule_quota: int
        :param bandwidth_rules: 功能说明：带宽规则对象（该字段仅在上海1局点返回）
        :type bandwidth_rules: list[:class:`huaweicloudsdkeip.v2.BandWidthRules`]
        :param created_at: 功能说明：资源创建时间，UTC时间  格式： yyyy-MM-ddTHH:mm:ss
        :type created_at: str
        :param updated_at: 功能说明：资源更新时间，UTC时间  格式： yyyy-MM-ddTHH:mm:ss
        :type updated_at: str
        :param public_border_group: 功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：共享带宽只能绑定与该字段相同的publicip
        :type public_border_group: str
        """
        
        

        self._bandwidth_type = None
        self._billing_info = None
        self._charge_mode = None
        self._id = None
        self._name = None
        self._publicip_info = None
        self._share_type = None
        self._size = None
        self._tenant_id = None
        self._enterprise_project_id = None
        self._status = None
        self._enable_bandwidth_rules = None
        self._rule_quota = None
        self._bandwidth_rules = None
        self._created_at = None
        self._updated_at = None
        self._public_border_group = None
        self.discriminator = None

        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type
        if billing_info is not None:
            self.billing_info = billing_info
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if publicip_info is not None:
            self.publicip_info = publicip_info
        if share_type is not None:
            self.share_type = share_type
        if size is not None:
            self.size = size
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if status is not None:
            self.status = status
        if enable_bandwidth_rules is not None:
            self.enable_bandwidth_rules = enable_bandwidth_rules
        if rule_quota is not None:
            self.rule_quota = rule_quota
        if bandwidth_rules is not None:
            self.bandwidth_rules = bandwidth_rules
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this BandwidthResp.

        功能说明：带宽类型，共享带宽默认为share。  取值范围：share，bgp，telcom，sbgp等。  share：共享带宽  bgp：动态bgp  telcom ：联通  sbgp：静态bgp

        :return: The bandwidth_type of this BandwidthResp.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this BandwidthResp.

        功能说明：带宽类型，共享带宽默认为share。  取值范围：share，bgp，telcom，sbgp等。  share：共享带宽  bgp：动态bgp  telcom ：联通  sbgp：静态bgp

        :param bandwidth_type: The bandwidth_type of this BandwidthResp.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

    @property
    def billing_info(self):
        """Gets the billing_info of this BandwidthResp.

        功能说明：账单信息  如果billinginfo不为空，说明是包周期的带宽

        :return: The billing_info of this BandwidthResp.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this BandwidthResp.

        功能说明：账单信息  如果billinginfo不为空，说明是包周期的带宽

        :param billing_info: The billing_info of this BandwidthResp.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def charge_mode(self):
        """Gets the charge_mode of this BandwidthResp.

        功能说明：按流量计费,按带宽计费还是按增强型95计费。  取值范围：bandwidth，traffic，95peak_plus(按增强型95计费)不返回或者为空时表示是bandwidth。  约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%。

        :return: The charge_mode of this BandwidthResp.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this BandwidthResp.

        功能说明：按流量计费,按带宽计费还是按增强型95计费。  取值范围：bandwidth，traffic，95peak_plus(按增强型95计费)不返回或者为空时表示是bandwidth。  约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%。

        :param charge_mode: The charge_mode of this BandwidthResp.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def id(self):
        """Gets the id of this BandwidthResp.

        功能说明：带宽唯一标识

        :return: The id of this BandwidthResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BandwidthResp.

        功能说明：带宽唯一标识

        :param id: The id of this BandwidthResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BandwidthResp.

        功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this BandwidthResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BandwidthResp.

        功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this BandwidthResp.
        :type name: str
        """
        self._name = name

    @property
    def publicip_info(self):
        """Gets the publicip_info of this BandwidthResp.

        功能说明：带宽对应的弹性公网IP信息  约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP

        :return: The publicip_info of this BandwidthResp.
        :rtype: list[:class:`huaweicloudsdkeip.v2.PublicipInfoResp`]
        """
        return self._publicip_info

    @publicip_info.setter
    def publicip_info(self, publicip_info):
        """Sets the publicip_info of this BandwidthResp.

        功能说明：带宽对应的弹性公网IP信息  约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP

        :param publicip_info: The publicip_info of this BandwidthResp.
        :type publicip_info: list[:class:`huaweicloudsdkeip.v2.PublicipInfoResp`]
        """
        self._publicip_info = publicip_info

    @property
    def share_type(self):
        """Gets the share_type of this BandwidthResp.

        功能说明：带宽类型，标识是否是共享带宽  取值范围：WHOLE，PER  WHOLE表示共享带宽；PER，表示独享带宽

        :return: The share_type of this BandwidthResp.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this BandwidthResp.

        功能说明：带宽类型，标识是否是共享带宽  取值范围：WHOLE，PER  WHOLE表示共享带宽；PER，表示独享带宽

        :param share_type: The share_type of this BandwidthResp.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def size(self):
        """Gets the size of this BandwidthResp.

        功能说明：带宽大小  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。

        :return: The size of this BandwidthResp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BandwidthResp.

        功能说明：带宽大小  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。

        :param size: The size of this BandwidthResp.
        :type size: int
        """
        self._size = size

    @property
    def tenant_id(self):
        """Gets the tenant_id of this BandwidthResp.

        功能说明：用户所属租户ID

        :return: The tenant_id of this BandwidthResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this BandwidthResp.

        功能说明：用户所属租户ID

        :param tenant_id: The tenant_id of this BandwidthResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this BandwidthResp.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建带宽时，给带宽绑定企业项目ID。

        :return: The enterprise_project_id of this BandwidthResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this BandwidthResp.

        企业项目ID。最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。  创建带宽时，给带宽绑定企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this BandwidthResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def status(self):
        """Gets the status of this BandwidthResp.

        功能说明：带宽的状态  取值范围：  FREEZED：冻结  NORMAL：正常

        :return: The status of this BandwidthResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BandwidthResp.

        功能说明：带宽的状态  取值范围：  FREEZED：冻结  NORMAL：正常

        :param status: The status of this BandwidthResp.
        :type status: str
        """
        self._status = status

    @property
    def enable_bandwidth_rules(self):
        """Gets the enable_bandwidth_rules of this BandwidthResp.

        功能说明：是否开启企业级qos，仅共享带宽支持开启。（该字段仅在上海1局点返回）

        :return: The enable_bandwidth_rules of this BandwidthResp.
        :rtype: bool
        """
        return self._enable_bandwidth_rules

    @enable_bandwidth_rules.setter
    def enable_bandwidth_rules(self, enable_bandwidth_rules):
        """Sets the enable_bandwidth_rules of this BandwidthResp.

        功能说明：是否开启企业级qos，仅共享带宽支持开启。（该字段仅在上海1局点返回）

        :param enable_bandwidth_rules: The enable_bandwidth_rules of this BandwidthResp.
        :type enable_bandwidth_rules: bool
        """
        self._enable_bandwidth_rules = enable_bandwidth_rules

    @property
    def rule_quota(self):
        """Gets the rule_quota of this BandwidthResp.

        功能说明：带宽支持的最大分组规则数。（该字段仅在上海1局点返回）

        :return: The rule_quota of this BandwidthResp.
        :rtype: int
        """
        return self._rule_quota

    @rule_quota.setter
    def rule_quota(self, rule_quota):
        """Sets the rule_quota of this BandwidthResp.

        功能说明：带宽支持的最大分组规则数。（该字段仅在上海1局点返回）

        :param rule_quota: The rule_quota of this BandwidthResp.
        :type rule_quota: int
        """
        self._rule_quota = rule_quota

    @property
    def bandwidth_rules(self):
        """Gets the bandwidth_rules of this BandwidthResp.

        功能说明：带宽规则对象（该字段仅在上海1局点返回）

        :return: The bandwidth_rules of this BandwidthResp.
        :rtype: list[:class:`huaweicloudsdkeip.v2.BandWidthRules`]
        """
        return self._bandwidth_rules

    @bandwidth_rules.setter
    def bandwidth_rules(self, bandwidth_rules):
        """Sets the bandwidth_rules of this BandwidthResp.

        功能说明：带宽规则对象（该字段仅在上海1局点返回）

        :param bandwidth_rules: The bandwidth_rules of this BandwidthResp.
        :type bandwidth_rules: list[:class:`huaweicloudsdkeip.v2.BandWidthRules`]
        """
        self._bandwidth_rules = bandwidth_rules

    @property
    def created_at(self):
        """Gets the created_at of this BandwidthResp.

        功能说明：资源创建时间，UTC时间  格式： yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this BandwidthResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BandwidthResp.

        功能说明：资源创建时间，UTC时间  格式： yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this BandwidthResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this BandwidthResp.

        功能说明：资源更新时间，UTC时间  格式： yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this BandwidthResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BandwidthResp.

        功能说明：资源更新时间，UTC时间  格式： yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this BandwidthResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def public_border_group(self):
        """Gets the public_border_group of this BandwidthResp.

        功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：共享带宽只能绑定与该字段相同的publicip

        :return: The public_border_group of this BandwidthResp.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this BandwidthResp.

        功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：共享带宽只能绑定与该字段相同的publicip

        :param public_border_group: The public_border_group of this BandwidthResp.
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
        if not isinstance(other, BandwidthResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
