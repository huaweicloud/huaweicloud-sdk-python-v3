# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetFirewallInstanceResponseRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'name': 'str',
        'ha_type': 'int',
        'charge_mode': 'int',
        'service_type': 'int',
        'engine_type': 'int',
        'flavor': 'Flavor',
        'protect_objects': 'list[ProtectObjectVO]',
        'status': 'int',
        'is_old_firewall_instance': 'bool',
        'is_available_obs': 'bool',
        'is_support_threat_tags': 'bool',
        'support_ipv6': 'bool',
        'feature_toggle': 'dict(str, bool)',
        'resources': 'list[FirewallInstanceResource]',
        'fw_instance_name': 'str',
        'enterprise_project_id': 'str',
        'resource_id': 'str',
        'support_url_filtering': 'bool',
        'tags': 'str'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'name': 'name',
        'ha_type': 'ha_type',
        'charge_mode': 'charge_mode',
        'service_type': 'service_type',
        'engine_type': 'engine_type',
        'flavor': 'flavor',
        'protect_objects': 'protect_objects',
        'status': 'status',
        'is_old_firewall_instance': 'is_old_firewall_instance',
        'is_available_obs': 'is_available_obs',
        'is_support_threat_tags': 'is_support_threat_tags',
        'support_ipv6': 'support_ipv6',
        'feature_toggle': 'feature_toggle',
        'resources': 'resources',
        'fw_instance_name': 'fw_instance_name',
        'enterprise_project_id': 'enterprise_project_id',
        'resource_id': 'resource_id',
        'support_url_filtering': 'support_url_filtering',
        'tags': 'tags'
    }

    def __init__(self, fw_instance_id=None, name=None, ha_type=None, charge_mode=None, service_type=None, engine_type=None, flavor=None, protect_objects=None, status=None, is_old_firewall_instance=None, is_available_obs=None, is_support_threat_tags=None, support_ipv6=None, feature_toggle=None, resources=None, fw_instance_name=None, enterprise_project_id=None, resource_id=None, support_url_filtering=None, tags=None):
        r"""GetFirewallInstanceResponseRecord

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id。，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，默认情况下，fw_instance_Id为空时，返回账号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。
        :type fw_instance_id: str
        :param name: 防火墙名称
        :type name: str
        :param ha_type: 集群类型，包含主备（0）和集群（1）两种方式，主备模式包含四个节点，2个主节点构成集群，剩余两个节点为主节点的备节点，集群模式仅拉起两个节点作为集群。
        :type ha_type: int
        :param charge_mode: 计费模式 0：包年/包月 1：按需
        :type charge_mode: int
        :param service_type: 防火墙防护类型，目前仅支持0，互联网防护
        :type service_type: int
        :param engine_type: 引擎类型，0：自研引擎 1：山石引擎 3：天融信引擎
        :type engine_type: int
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkcfw.v1.Flavor`
        :param protect_objects: 防护对象列表
        :type protect_objects: list[:class:`huaweicloudsdkcfw.v1.ProtectObjectVO`]
        :param status: 防火墙状态列表，包括-1：等待支付，0：创建中，1，删除中，2：运行中，3：升级中，4：删除完成：5：冻结中，6：创建失败，7：删除失败，8：冻结失败，9：存储中，10：存储失败，11：升级失败
        :type status: int
        :param is_old_firewall_instance: 是否为旧引擎，true表示是，false表示不是
        :type is_old_firewall_instance: bool
        :param is_available_obs: 是否支持obs，true表示是，false表示不是
        :type is_available_obs: bool
        :param is_support_threat_tags: 是否支持威胁情报标签，true表示是，false表示不是
        :type is_support_threat_tags: bool
        :param support_ipv6: 是否支持ipv6，true表示是，false表示不是
        :type support_ipv6: bool
        :param feature_toggle: 特性开关，boolean值为true表示是，false表示否
        :type feature_toggle: dict(str, bool)
        :param resources: 防火墙资源列表
        :type resources: list[:class:`huaweicloudsdkcfw.v1.FirewallInstanceResource`]
        :param fw_instance_name: 防火墙名称
        :type fw_instance_name: str
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        :param resource_id: 防火墙资源id，同fw_instance_id
        :type resource_id: str
        :param support_url_filtering: 是否支持url过滤，true表示是，false表示不是
        :type support_url_filtering: bool
        :param tags: 标签列表，标签键值map转化的json字符串，如\&quot;{\\\&quot;key\\\&quot;:\\\&quot;value\\\&quot;}\&quot;
        :type tags: str
        """
        
        

        self._fw_instance_id = None
        self._name = None
        self._ha_type = None
        self._charge_mode = None
        self._service_type = None
        self._engine_type = None
        self._flavor = None
        self._protect_objects = None
        self._status = None
        self._is_old_firewall_instance = None
        self._is_available_obs = None
        self._is_support_threat_tags = None
        self._support_ipv6 = None
        self._feature_toggle = None
        self._resources = None
        self._fw_instance_name = None
        self._enterprise_project_id = None
        self._resource_id = None
        self._support_url_filtering = None
        self._tags = None
        self.discriminator = None

        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id
        if name is not None:
            self.name = name
        if ha_type is not None:
            self.ha_type = ha_type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if service_type is not None:
            self.service_type = service_type
        if engine_type is not None:
            self.engine_type = engine_type
        if flavor is not None:
            self.flavor = flavor
        if protect_objects is not None:
            self.protect_objects = protect_objects
        if status is not None:
            self.status = status
        if is_old_firewall_instance is not None:
            self.is_old_firewall_instance = is_old_firewall_instance
        if is_available_obs is not None:
            self.is_available_obs = is_available_obs
        if is_support_threat_tags is not None:
            self.is_support_threat_tags = is_support_threat_tags
        if support_ipv6 is not None:
            self.support_ipv6 = support_ipv6
        if feature_toggle is not None:
            self.feature_toggle = feature_toggle
        if resources is not None:
            self.resources = resources
        if fw_instance_name is not None:
            self.fw_instance_name = fw_instance_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if resource_id is not None:
            self.resource_id = resource_id
        if support_url_filtering is not None:
            self.support_url_filtering = support_url_filtering
        if tags is not None:
            self.tags = tags

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this GetFirewallInstanceResponseRecord.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id。，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，默认情况下，fw_instance_Id为空时，返回账号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。

        :return: The fw_instance_id of this GetFirewallInstanceResponseRecord.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this GetFirewallInstanceResponseRecord.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id。，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，默认情况下，fw_instance_Id为空时，返回账号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。

        :param fw_instance_id: The fw_instance_id of this GetFirewallInstanceResponseRecord.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def name(self):
        r"""Gets the name of this GetFirewallInstanceResponseRecord.

        防火墙名称

        :return: The name of this GetFirewallInstanceResponseRecord.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetFirewallInstanceResponseRecord.

        防火墙名称

        :param name: The name of this GetFirewallInstanceResponseRecord.
        :type name: str
        """
        self._name = name

    @property
    def ha_type(self):
        r"""Gets the ha_type of this GetFirewallInstanceResponseRecord.

        集群类型，包含主备（0）和集群（1）两种方式，主备模式包含四个节点，2个主节点构成集群，剩余两个节点为主节点的备节点，集群模式仅拉起两个节点作为集群。

        :return: The ha_type of this GetFirewallInstanceResponseRecord.
        :rtype: int
        """
        return self._ha_type

    @ha_type.setter
    def ha_type(self, ha_type):
        r"""Sets the ha_type of this GetFirewallInstanceResponseRecord.

        集群类型，包含主备（0）和集群（1）两种方式，主备模式包含四个节点，2个主节点构成集群，剩余两个节点为主节点的备节点，集群模式仅拉起两个节点作为集群。

        :param ha_type: The ha_type of this GetFirewallInstanceResponseRecord.
        :type ha_type: int
        """
        self._ha_type = ha_type

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this GetFirewallInstanceResponseRecord.

        计费模式 0：包年/包月 1：按需

        :return: The charge_mode of this GetFirewallInstanceResponseRecord.
        :rtype: int
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this GetFirewallInstanceResponseRecord.

        计费模式 0：包年/包月 1：按需

        :param charge_mode: The charge_mode of this GetFirewallInstanceResponseRecord.
        :type charge_mode: int
        """
        self._charge_mode = charge_mode

    @property
    def service_type(self):
        r"""Gets the service_type of this GetFirewallInstanceResponseRecord.

        防火墙防护类型，目前仅支持0，互联网防护

        :return: The service_type of this GetFirewallInstanceResponseRecord.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this GetFirewallInstanceResponseRecord.

        防火墙防护类型，目前仅支持0，互联网防护

        :param service_type: The service_type of this GetFirewallInstanceResponseRecord.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def engine_type(self):
        r"""Gets the engine_type of this GetFirewallInstanceResponseRecord.

        引擎类型，0：自研引擎 1：山石引擎 3：天融信引擎

        :return: The engine_type of this GetFirewallInstanceResponseRecord.
        :rtype: int
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this GetFirewallInstanceResponseRecord.

        引擎类型，0：自研引擎 1：山石引擎 3：天融信引擎

        :param engine_type: The engine_type of this GetFirewallInstanceResponseRecord.
        :type engine_type: int
        """
        self._engine_type = engine_type

    @property
    def flavor(self):
        r"""Gets the flavor of this GetFirewallInstanceResponseRecord.

        :return: The flavor of this GetFirewallInstanceResponseRecord.
        :rtype: :class:`huaweicloudsdkcfw.v1.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this GetFirewallInstanceResponseRecord.

        :param flavor: The flavor of this GetFirewallInstanceResponseRecord.
        :type flavor: :class:`huaweicloudsdkcfw.v1.Flavor`
        """
        self._flavor = flavor

    @property
    def protect_objects(self):
        r"""Gets the protect_objects of this GetFirewallInstanceResponseRecord.

        防护对象列表

        :return: The protect_objects of this GetFirewallInstanceResponseRecord.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ProtectObjectVO`]
        """
        return self._protect_objects

    @protect_objects.setter
    def protect_objects(self, protect_objects):
        r"""Sets the protect_objects of this GetFirewallInstanceResponseRecord.

        防护对象列表

        :param protect_objects: The protect_objects of this GetFirewallInstanceResponseRecord.
        :type protect_objects: list[:class:`huaweicloudsdkcfw.v1.ProtectObjectVO`]
        """
        self._protect_objects = protect_objects

    @property
    def status(self):
        r"""Gets the status of this GetFirewallInstanceResponseRecord.

        防火墙状态列表，包括-1：等待支付，0：创建中，1，删除中，2：运行中，3：升级中，4：删除完成：5：冻结中，6：创建失败，7：删除失败，8：冻结失败，9：存储中，10：存储失败，11：升级失败

        :return: The status of this GetFirewallInstanceResponseRecord.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetFirewallInstanceResponseRecord.

        防火墙状态列表，包括-1：等待支付，0：创建中，1，删除中，2：运行中，3：升级中，4：删除完成：5：冻结中，6：创建失败，7：删除失败，8：冻结失败，9：存储中，10：存储失败，11：升级失败

        :param status: The status of this GetFirewallInstanceResponseRecord.
        :type status: int
        """
        self._status = status

    @property
    def is_old_firewall_instance(self):
        r"""Gets the is_old_firewall_instance of this GetFirewallInstanceResponseRecord.

        是否为旧引擎，true表示是，false表示不是

        :return: The is_old_firewall_instance of this GetFirewallInstanceResponseRecord.
        :rtype: bool
        """
        return self._is_old_firewall_instance

    @is_old_firewall_instance.setter
    def is_old_firewall_instance(self, is_old_firewall_instance):
        r"""Sets the is_old_firewall_instance of this GetFirewallInstanceResponseRecord.

        是否为旧引擎，true表示是，false表示不是

        :param is_old_firewall_instance: The is_old_firewall_instance of this GetFirewallInstanceResponseRecord.
        :type is_old_firewall_instance: bool
        """
        self._is_old_firewall_instance = is_old_firewall_instance

    @property
    def is_available_obs(self):
        r"""Gets the is_available_obs of this GetFirewallInstanceResponseRecord.

        是否支持obs，true表示是，false表示不是

        :return: The is_available_obs of this GetFirewallInstanceResponseRecord.
        :rtype: bool
        """
        return self._is_available_obs

    @is_available_obs.setter
    def is_available_obs(self, is_available_obs):
        r"""Sets the is_available_obs of this GetFirewallInstanceResponseRecord.

        是否支持obs，true表示是，false表示不是

        :param is_available_obs: The is_available_obs of this GetFirewallInstanceResponseRecord.
        :type is_available_obs: bool
        """
        self._is_available_obs = is_available_obs

    @property
    def is_support_threat_tags(self):
        r"""Gets the is_support_threat_tags of this GetFirewallInstanceResponseRecord.

        是否支持威胁情报标签，true表示是，false表示不是

        :return: The is_support_threat_tags of this GetFirewallInstanceResponseRecord.
        :rtype: bool
        """
        return self._is_support_threat_tags

    @is_support_threat_tags.setter
    def is_support_threat_tags(self, is_support_threat_tags):
        r"""Sets the is_support_threat_tags of this GetFirewallInstanceResponseRecord.

        是否支持威胁情报标签，true表示是，false表示不是

        :param is_support_threat_tags: The is_support_threat_tags of this GetFirewallInstanceResponseRecord.
        :type is_support_threat_tags: bool
        """
        self._is_support_threat_tags = is_support_threat_tags

    @property
    def support_ipv6(self):
        r"""Gets the support_ipv6 of this GetFirewallInstanceResponseRecord.

        是否支持ipv6，true表示是，false表示不是

        :return: The support_ipv6 of this GetFirewallInstanceResponseRecord.
        :rtype: bool
        """
        return self._support_ipv6

    @support_ipv6.setter
    def support_ipv6(self, support_ipv6):
        r"""Sets the support_ipv6 of this GetFirewallInstanceResponseRecord.

        是否支持ipv6，true表示是，false表示不是

        :param support_ipv6: The support_ipv6 of this GetFirewallInstanceResponseRecord.
        :type support_ipv6: bool
        """
        self._support_ipv6 = support_ipv6

    @property
    def feature_toggle(self):
        r"""Gets the feature_toggle of this GetFirewallInstanceResponseRecord.

        特性开关，boolean值为true表示是，false表示否

        :return: The feature_toggle of this GetFirewallInstanceResponseRecord.
        :rtype: dict(str, bool)
        """
        return self._feature_toggle

    @feature_toggle.setter
    def feature_toggle(self, feature_toggle):
        r"""Sets the feature_toggle of this GetFirewallInstanceResponseRecord.

        特性开关，boolean值为true表示是，false表示否

        :param feature_toggle: The feature_toggle of this GetFirewallInstanceResponseRecord.
        :type feature_toggle: dict(str, bool)
        """
        self._feature_toggle = feature_toggle

    @property
    def resources(self):
        r"""Gets the resources of this GetFirewallInstanceResponseRecord.

        防火墙资源列表

        :return: The resources of this GetFirewallInstanceResponseRecord.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.FirewallInstanceResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this GetFirewallInstanceResponseRecord.

        防火墙资源列表

        :param resources: The resources of this GetFirewallInstanceResponseRecord.
        :type resources: list[:class:`huaweicloudsdkcfw.v1.FirewallInstanceResource`]
        """
        self._resources = resources

    @property
    def fw_instance_name(self):
        r"""Gets the fw_instance_name of this GetFirewallInstanceResponseRecord.

        防火墙名称

        :return: The fw_instance_name of this GetFirewallInstanceResponseRecord.
        :rtype: str
        """
        return self._fw_instance_name

    @fw_instance_name.setter
    def fw_instance_name(self, fw_instance_name):
        r"""Sets the fw_instance_name of this GetFirewallInstanceResponseRecord.

        防火墙名称

        :param fw_instance_name: The fw_instance_name of this GetFirewallInstanceResponseRecord.
        :type fw_instance_name: str
        """
        self._fw_instance_name = fw_instance_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this GetFirewallInstanceResponseRecord.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this GetFirewallInstanceResponseRecord.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this GetFirewallInstanceResponseRecord.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this GetFirewallInstanceResponseRecord.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this GetFirewallInstanceResponseRecord.

        防火墙资源id，同fw_instance_id

        :return: The resource_id of this GetFirewallInstanceResponseRecord.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this GetFirewallInstanceResponseRecord.

        防火墙资源id，同fw_instance_id

        :param resource_id: The resource_id of this GetFirewallInstanceResponseRecord.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def support_url_filtering(self):
        r"""Gets the support_url_filtering of this GetFirewallInstanceResponseRecord.

        是否支持url过滤，true表示是，false表示不是

        :return: The support_url_filtering of this GetFirewallInstanceResponseRecord.
        :rtype: bool
        """
        return self._support_url_filtering

    @support_url_filtering.setter
    def support_url_filtering(self, support_url_filtering):
        r"""Sets the support_url_filtering of this GetFirewallInstanceResponseRecord.

        是否支持url过滤，true表示是，false表示不是

        :param support_url_filtering: The support_url_filtering of this GetFirewallInstanceResponseRecord.
        :type support_url_filtering: bool
        """
        self._support_url_filtering = support_url_filtering

    @property
    def tags(self):
        r"""Gets the tags of this GetFirewallInstanceResponseRecord.

        标签列表，标签键值map转化的json字符串，如\"{\\\"key\\\":\\\"value\\\"}\"

        :return: The tags of this GetFirewallInstanceResponseRecord.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this GetFirewallInstanceResponseRecord.

        标签列表，标签键值map转化的json字符串，如\"{\\\"key\\\":\\\"value\\\"}\"

        :param tags: The tags of this GetFirewallInstanceResponseRecord.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, GetFirewallInstanceResponseRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
