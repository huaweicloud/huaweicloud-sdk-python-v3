# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEipBandwidthsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'marker': 'str',
        'id': 'str',
        'bandwidth_type': 'str',
        'name': 'str',
        'name_like': 'str',
        'tenant_id': 'str',
        'ingress_size': 'str',
        'admin_state': 'str',
        'billing_info': 'str',
        'tags': 'str',
        'enable_bandwidth_rules': 'str',
        'rule_quota': 'int',
        'public_border_group': 'str',
        'charge_mode': 'str',
        'size': 'str',
        'type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'bandwidth_type': 'bandwidth_type',
        'name': 'name',
        'name_like': 'name_like',
        'tenant_id': 'tenant_id',
        'ingress_size': 'ingress_size',
        'admin_state': 'admin_state',
        'billing_info': 'billing_info',
        'tags': 'tags',
        'enable_bandwidth_rules': 'enable_bandwidth_rules',
        'rule_quota': 'rule_quota',
        'public_border_group': 'public_border_group',
        'charge_mode': 'charge_mode',
        'size': 'size',
        'type': 'type'
    }

    def __init__(self, limit=None, marker=None, id=None, bandwidth_type=None, name=None, name_like=None, tenant_id=None, ingress_size=None, admin_state=None, billing_info=None, tags=None, enable_bandwidth_rules=None, rule_quota=None, public_border_group=None, charge_mode=None, size=None, type=None):
        """ListEipBandwidthsRequest

        The model defined in huaweicloud sdk

        :param limit: - 功能说明：每页返回的个数 - 取值范围：取值范围：1~[2000]，其中2000为局点差异项，具体取值由局点决定
        :type limit: str
        :param marker: - 功能说明：分页查询起始的资源ID，为空时为查询第一页
        :type marker: str
        :param id: - 功能说明：带宽唯一标识
        :type id: str
        :param bandwidth_type: - 功能说明：带宽类型，共享带宽默认为share。 - 取值范围：share，bgp，telcom，sbgp等。   - share：共享带宽   - bgp：动态bgp   - telcom ：联通   - sbgp：静态bgp
        :type bandwidth_type: str
        :param name: - 功能说明：宽带名称，按照宽带名称过滤
        :type name: str
        :param name_like: - 功能说明：根据宽带名称模糊查询过滤
        :type name_like: str
        :param tenant_id: - 功能说明：根据tenant_id过滤
        :type tenant_id: str
        :param ingress_size: - 功能说明：根据入云大小过滤
        :type ingress_size: str
        :param admin_state: - 功能说明：根据宽带状态过滤
        :type admin_state: str
        :param billing_info: - 功能说明：根据计费信息过滤
        :type billing_info: str
        :param tags: - 功能说明：根据标签过滤
        :type tags: str
        :param enable_bandwidth_rules: - 功能说明：根据是否带宽分组使能过滤 - 取值范围：true、false
        :type enable_bandwidth_rules: str
        :param rule_quota: - 功能说明：根据规则数值过滤
        :type rule_quota: int
        :param public_border_group: - 功能说明：根据站点信息过滤
        :type public_border_group: str
        :param charge_mode: - 功能说明：按流量计费,按带宽计费还是按增强型95计费 - 取值范围：bandwidth（按带宽计费），traffic（按流量计费），95peak_plus（按增强型95计费），不返回或者为空时表示是bandwidth - 约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%
        :type charge_mode: str
        :param size: - 功能说明：带宽大小。共享带宽的大小有最小值限制，默认为5M，可能因局点不同而不同。 - 取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。   调整带宽时的最小单位会根据带宽范围不同存在差异。 - 小于等于300Mbit/s：默认最小单位为1Mbit/s。 - 300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。 - 大于1000Mbit/s：默认最小单位为500Mbit/s。
        :type size: str
        :param type: - 功能说明：带宽类型，标识是否是共享带宽 - 取值范围：WHOLE，PER。   - WHOLE表示共享带宽   - PER表示独享带宽
        :type type: str
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._bandwidth_type = None
        self._name = None
        self._name_like = None
        self._tenant_id = None
        self._ingress_size = None
        self._admin_state = None
        self._billing_info = None
        self._tags = None
        self._enable_bandwidth_rules = None
        self._rule_quota = None
        self._public_border_group = None
        self._charge_mode = None
        self._size = None
        self._type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type
        if name is not None:
            self.name = name
        if name_like is not None:
            self.name_like = name_like
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if ingress_size is not None:
            self.ingress_size = ingress_size
        if admin_state is not None:
            self.admin_state = admin_state
        if billing_info is not None:
            self.billing_info = billing_info
        if tags is not None:
            self.tags = tags
        if enable_bandwidth_rules is not None:
            self.enable_bandwidth_rules = enable_bandwidth_rules
        if rule_quota is not None:
            self.rule_quota = rule_quota
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type

    @property
    def limit(self):
        """Gets the limit of this ListEipBandwidthsRequest.

        - 功能说明：每页返回的个数 - 取值范围：取值范围：1~[2000]，其中2000为局点差异项，具体取值由局点决定

        :return: The limit of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEipBandwidthsRequest.

        - 功能说明：每页返回的个数 - 取值范围：取值范围：1~[2000]，其中2000为局点差异项，具体取值由局点决定

        :param limit: The limit of this ListEipBandwidthsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListEipBandwidthsRequest.

        - 功能说明：分页查询起始的资源ID，为空时为查询第一页

        :return: The marker of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListEipBandwidthsRequest.

        - 功能说明：分页查询起始的资源ID，为空时为查询第一页

        :param marker: The marker of this ListEipBandwidthsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListEipBandwidthsRequest.

        - 功能说明：带宽唯一标识

        :return: The id of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListEipBandwidthsRequest.

        - 功能说明：带宽唯一标识

        :param id: The id of this ListEipBandwidthsRequest.
        :type id: str
        """
        self._id = id

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this ListEipBandwidthsRequest.

        - 功能说明：带宽类型，共享带宽默认为share。 - 取值范围：share，bgp，telcom，sbgp等。   - share：共享带宽   - bgp：动态bgp   - telcom ：联通   - sbgp：静态bgp

        :return: The bandwidth_type of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this ListEipBandwidthsRequest.

        - 功能说明：带宽类型，共享带宽默认为share。 - 取值范围：share，bgp，telcom，sbgp等。   - share：共享带宽   - bgp：动态bgp   - telcom ：联通   - sbgp：静态bgp

        :param bandwidth_type: The bandwidth_type of this ListEipBandwidthsRequest.
        :type bandwidth_type: str
        """
        self._bandwidth_type = bandwidth_type

    @property
    def name(self):
        """Gets the name of this ListEipBandwidthsRequest.

        - 功能说明：宽带名称，按照宽带名称过滤

        :return: The name of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEipBandwidthsRequest.

        - 功能说明：宽带名称，按照宽带名称过滤

        :param name: The name of this ListEipBandwidthsRequest.
        :type name: str
        """
        self._name = name

    @property
    def name_like(self):
        """Gets the name_like of this ListEipBandwidthsRequest.

        - 功能说明：根据宽带名称模糊查询过滤

        :return: The name_like of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._name_like

    @name_like.setter
    def name_like(self, name_like):
        """Sets the name_like of this ListEipBandwidthsRequest.

        - 功能说明：根据宽带名称模糊查询过滤

        :param name_like: The name_like of this ListEipBandwidthsRequest.
        :type name_like: str
        """
        self._name_like = name_like

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ListEipBandwidthsRequest.

        - 功能说明：根据tenant_id过滤

        :return: The tenant_id of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ListEipBandwidthsRequest.

        - 功能说明：根据tenant_id过滤

        :param tenant_id: The tenant_id of this ListEipBandwidthsRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def ingress_size(self):
        """Gets the ingress_size of this ListEipBandwidthsRequest.

        - 功能说明：根据入云大小过滤

        :return: The ingress_size of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._ingress_size

    @ingress_size.setter
    def ingress_size(self, ingress_size):
        """Sets the ingress_size of this ListEipBandwidthsRequest.

        - 功能说明：根据入云大小过滤

        :param ingress_size: The ingress_size of this ListEipBandwidthsRequest.
        :type ingress_size: str
        """
        self._ingress_size = ingress_size

    @property
    def admin_state(self):
        """Gets the admin_state of this ListEipBandwidthsRequest.

        - 功能说明：根据宽带状态过滤

        :return: The admin_state of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this ListEipBandwidthsRequest.

        - 功能说明：根据宽带状态过滤

        :param admin_state: The admin_state of this ListEipBandwidthsRequest.
        :type admin_state: str
        """
        self._admin_state = admin_state

    @property
    def billing_info(self):
        """Gets the billing_info of this ListEipBandwidthsRequest.

        - 功能说明：根据计费信息过滤

        :return: The billing_info of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this ListEipBandwidthsRequest.

        - 功能说明：根据计费信息过滤

        :param billing_info: The billing_info of this ListEipBandwidthsRequest.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def tags(self):
        """Gets the tags of this ListEipBandwidthsRequest.

        - 功能说明：根据标签过滤

        :return: The tags of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListEipBandwidthsRequest.

        - 功能说明：根据标签过滤

        :param tags: The tags of this ListEipBandwidthsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def enable_bandwidth_rules(self):
        """Gets the enable_bandwidth_rules of this ListEipBandwidthsRequest.

        - 功能说明：根据是否带宽分组使能过滤 - 取值范围：true、false

        :return: The enable_bandwidth_rules of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._enable_bandwidth_rules

    @enable_bandwidth_rules.setter
    def enable_bandwidth_rules(self, enable_bandwidth_rules):
        """Sets the enable_bandwidth_rules of this ListEipBandwidthsRequest.

        - 功能说明：根据是否带宽分组使能过滤 - 取值范围：true、false

        :param enable_bandwidth_rules: The enable_bandwidth_rules of this ListEipBandwidthsRequest.
        :type enable_bandwidth_rules: str
        """
        self._enable_bandwidth_rules = enable_bandwidth_rules

    @property
    def rule_quota(self):
        """Gets the rule_quota of this ListEipBandwidthsRequest.

        - 功能说明：根据规则数值过滤

        :return: The rule_quota of this ListEipBandwidthsRequest.
        :rtype: int
        """
        return self._rule_quota

    @rule_quota.setter
    def rule_quota(self, rule_quota):
        """Sets the rule_quota of this ListEipBandwidthsRequest.

        - 功能说明：根据规则数值过滤

        :param rule_quota: The rule_quota of this ListEipBandwidthsRequest.
        :type rule_quota: int
        """
        self._rule_quota = rule_quota

    @property
    def public_border_group(self):
        """Gets the public_border_group of this ListEipBandwidthsRequest.

        - 功能说明：根据站点信息过滤

        :return: The public_border_group of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this ListEipBandwidthsRequest.

        - 功能说明：根据站点信息过滤

        :param public_border_group: The public_border_group of this ListEipBandwidthsRequest.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ListEipBandwidthsRequest.

        - 功能说明：按流量计费,按带宽计费还是按增强型95计费 - 取值范围：bandwidth（按带宽计费），traffic（按流量计费），95peak_plus（按增强型95计费），不返回或者为空时表示是bandwidth - 约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%

        :return: The charge_mode of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ListEipBandwidthsRequest.

        - 功能说明：按流量计费,按带宽计费还是按增强型95计费 - 取值范围：bandwidth（按带宽计费），traffic（按流量计费），95peak_plus（按增强型95计费），不返回或者为空时表示是bandwidth - 约束：只有共享带宽支持95peak_plus（按增强型95计费），按增强型95计费时需要指定保底百分比，默认是20%

        :param charge_mode: The charge_mode of this ListEipBandwidthsRequest.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def size(self):
        """Gets the size of this ListEipBandwidthsRequest.

        - 功能说明：带宽大小。共享带宽的大小有最小值限制，默认为5M，可能因局点不同而不同。 - 取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。   调整带宽时的最小单位会根据带宽范围不同存在差异。 - 小于等于300Mbit/s：默认最小单位为1Mbit/s。 - 300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。 - 大于1000Mbit/s：默认最小单位为500Mbit/s。

        :return: The size of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListEipBandwidthsRequest.

        - 功能说明：带宽大小。共享带宽的大小有最小值限制，默认为5M，可能因局点不同而不同。 - 取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。   调整带宽时的最小单位会根据带宽范围不同存在差异。 - 小于等于300Mbit/s：默认最小单位为1Mbit/s。 - 300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。 - 大于1000Mbit/s：默认最小单位为500Mbit/s。

        :param size: The size of this ListEipBandwidthsRequest.
        :type size: str
        """
        self._size = size

    @property
    def type(self):
        """Gets the type of this ListEipBandwidthsRequest.

        - 功能说明：带宽类型，标识是否是共享带宽 - 取值范围：WHOLE，PER。   - WHOLE表示共享带宽   - PER表示独享带宽

        :return: The type of this ListEipBandwidthsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListEipBandwidthsRequest.

        - 功能说明：带宽类型，标识是否是共享带宽 - 取值范围：WHOLE，PER。   - WHOLE表示共享带宽   - PER表示独享带宽

        :param type: The type of this ListEipBandwidthsRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListEipBandwidthsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
