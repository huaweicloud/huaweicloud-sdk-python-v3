# coding: utf-8

import re
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
        'support_ipv6': 'bool',
        'feature_toggle': 'dict(str, bool)',
        'resources': 'list[FirewallInstanceResource]'
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
        'support_ipv6': 'support_ipv6',
        'feature_toggle': 'feature_toggle',
        'resources': 'resources'
    }

    def __init__(self, fw_instance_id=None, name=None, ha_type=None, charge_mode=None, service_type=None, engine_type=None, flavor=None, protect_objects=None, status=None, is_old_firewall_instance=None, support_ipv6=None, feature_toggle=None, resources=None):
        """GetFirewallInstanceResponseRecord

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。
        :type fw_instance_id: str
        :param name: 防火墙名称
        :type name: str
        :param ha_type: 集群类型
        :type ha_type: int
        :param charge_mode: 计费模式 0：包年/包月 1：按需
        :type charge_mode: int
        :param service_type: 服务类型
        :type service_type: int
        :param engine_type: 引擎类型
        :type engine_type: int
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkcfw.v1.Flavor`
        :param protect_objects: 防护对象列表
        :type protect_objects: list[:class:`huaweicloudsdkcfw.v1.ProtectObjectVO`]
        :param status: 防火墙状态列表，包括-1：等待支付，0：创建中，1，删除中，2：运行中，3：升级中，4：删除完成：5：冻结中，6：创建失败，7：删除失败，8：冻结失败，9：存储中，10：存储失败，11：升级失败
        :type status: int
        :param is_old_firewall_instance: 是否为旧引擎，true表示是，false表示不是
        :type is_old_firewall_instance: bool
        :param support_ipv6: 是否支持ipv6，true表示是，false表示不是
        :type support_ipv6: bool
        :param feature_toggle: 特性开关，boolean值为true表示是，false表示否
        :type feature_toggle: dict(str, bool)
        :param resources: 防火墙资源列表
        :type resources: list[:class:`huaweicloudsdkcfw.v1.FirewallInstanceResource`]
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
        self._support_ipv6 = None
        self._feature_toggle = None
        self._resources = None
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
        if support_ipv6 is not None:
            self.support_ipv6 = support_ipv6
        if feature_toggle is not None:
            self.feature_toggle = feature_toggle
        if resources is not None:
            self.resources = resources

    @property
    def fw_instance_id(self):
        """Gets the fw_instance_id of this GetFirewallInstanceResponseRecord.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。

        :return: The fw_instance_id of this GetFirewallInstanceResponseRecord.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        """Sets the fw_instance_id of this GetFirewallInstanceResponseRecord.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。

        :param fw_instance_id: The fw_instance_id of this GetFirewallInstanceResponseRecord.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def name(self):
        """Gets the name of this GetFirewallInstanceResponseRecord.

        防火墙名称

        :return: The name of this GetFirewallInstanceResponseRecord.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetFirewallInstanceResponseRecord.

        防火墙名称

        :param name: The name of this GetFirewallInstanceResponseRecord.
        :type name: str
        """
        self._name = name

    @property
    def ha_type(self):
        """Gets the ha_type of this GetFirewallInstanceResponseRecord.

        集群类型

        :return: The ha_type of this GetFirewallInstanceResponseRecord.
        :rtype: int
        """
        return self._ha_type

    @ha_type.setter
    def ha_type(self, ha_type):
        """Sets the ha_type of this GetFirewallInstanceResponseRecord.

        集群类型

        :param ha_type: The ha_type of this GetFirewallInstanceResponseRecord.
        :type ha_type: int
        """
        self._ha_type = ha_type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this GetFirewallInstanceResponseRecord.

        计费模式 0：包年/包月 1：按需

        :return: The charge_mode of this GetFirewallInstanceResponseRecord.
        :rtype: int
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this GetFirewallInstanceResponseRecord.

        计费模式 0：包年/包月 1：按需

        :param charge_mode: The charge_mode of this GetFirewallInstanceResponseRecord.
        :type charge_mode: int
        """
        self._charge_mode = charge_mode

    @property
    def service_type(self):
        """Gets the service_type of this GetFirewallInstanceResponseRecord.

        服务类型

        :return: The service_type of this GetFirewallInstanceResponseRecord.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this GetFirewallInstanceResponseRecord.

        服务类型

        :param service_type: The service_type of this GetFirewallInstanceResponseRecord.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def engine_type(self):
        """Gets the engine_type of this GetFirewallInstanceResponseRecord.

        引擎类型

        :return: The engine_type of this GetFirewallInstanceResponseRecord.
        :rtype: int
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this GetFirewallInstanceResponseRecord.

        引擎类型

        :param engine_type: The engine_type of this GetFirewallInstanceResponseRecord.
        :type engine_type: int
        """
        self._engine_type = engine_type

    @property
    def flavor(self):
        """Gets the flavor of this GetFirewallInstanceResponseRecord.

        :return: The flavor of this GetFirewallInstanceResponseRecord.
        :rtype: :class:`huaweicloudsdkcfw.v1.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this GetFirewallInstanceResponseRecord.

        :param flavor: The flavor of this GetFirewallInstanceResponseRecord.
        :type flavor: :class:`huaweicloudsdkcfw.v1.Flavor`
        """
        self._flavor = flavor

    @property
    def protect_objects(self):
        """Gets the protect_objects of this GetFirewallInstanceResponseRecord.

        防护对象列表

        :return: The protect_objects of this GetFirewallInstanceResponseRecord.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ProtectObjectVO`]
        """
        return self._protect_objects

    @protect_objects.setter
    def protect_objects(self, protect_objects):
        """Sets the protect_objects of this GetFirewallInstanceResponseRecord.

        防护对象列表

        :param protect_objects: The protect_objects of this GetFirewallInstanceResponseRecord.
        :type protect_objects: list[:class:`huaweicloudsdkcfw.v1.ProtectObjectVO`]
        """
        self._protect_objects = protect_objects

    @property
    def status(self):
        """Gets the status of this GetFirewallInstanceResponseRecord.

        防火墙状态列表，包括-1：等待支付，0：创建中，1，删除中，2：运行中，3：升级中，4：删除完成：5：冻结中，6：创建失败，7：删除失败，8：冻结失败，9：存储中，10：存储失败，11：升级失败

        :return: The status of this GetFirewallInstanceResponseRecord.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetFirewallInstanceResponseRecord.

        防火墙状态列表，包括-1：等待支付，0：创建中，1，删除中，2：运行中，3：升级中，4：删除完成：5：冻结中，6：创建失败，7：删除失败，8：冻结失败，9：存储中，10：存储失败，11：升级失败

        :param status: The status of this GetFirewallInstanceResponseRecord.
        :type status: int
        """
        self._status = status

    @property
    def is_old_firewall_instance(self):
        """Gets the is_old_firewall_instance of this GetFirewallInstanceResponseRecord.

        是否为旧引擎，true表示是，false表示不是

        :return: The is_old_firewall_instance of this GetFirewallInstanceResponseRecord.
        :rtype: bool
        """
        return self._is_old_firewall_instance

    @is_old_firewall_instance.setter
    def is_old_firewall_instance(self, is_old_firewall_instance):
        """Sets the is_old_firewall_instance of this GetFirewallInstanceResponseRecord.

        是否为旧引擎，true表示是，false表示不是

        :param is_old_firewall_instance: The is_old_firewall_instance of this GetFirewallInstanceResponseRecord.
        :type is_old_firewall_instance: bool
        """
        self._is_old_firewall_instance = is_old_firewall_instance

    @property
    def support_ipv6(self):
        """Gets the support_ipv6 of this GetFirewallInstanceResponseRecord.

        是否支持ipv6，true表示是，false表示不是

        :return: The support_ipv6 of this GetFirewallInstanceResponseRecord.
        :rtype: bool
        """
        return self._support_ipv6

    @support_ipv6.setter
    def support_ipv6(self, support_ipv6):
        """Sets the support_ipv6 of this GetFirewallInstanceResponseRecord.

        是否支持ipv6，true表示是，false表示不是

        :param support_ipv6: The support_ipv6 of this GetFirewallInstanceResponseRecord.
        :type support_ipv6: bool
        """
        self._support_ipv6 = support_ipv6

    @property
    def feature_toggle(self):
        """Gets the feature_toggle of this GetFirewallInstanceResponseRecord.

        特性开关，boolean值为true表示是，false表示否

        :return: The feature_toggle of this GetFirewallInstanceResponseRecord.
        :rtype: dict(str, bool)
        """
        return self._feature_toggle

    @feature_toggle.setter
    def feature_toggle(self, feature_toggle):
        """Sets the feature_toggle of this GetFirewallInstanceResponseRecord.

        特性开关，boolean值为true表示是，false表示否

        :param feature_toggle: The feature_toggle of this GetFirewallInstanceResponseRecord.
        :type feature_toggle: dict(str, bool)
        """
        self._feature_toggle = feature_toggle

    @property
    def resources(self):
        """Gets the resources of this GetFirewallInstanceResponseRecord.

        防火墙资源列表

        :return: The resources of this GetFirewallInstanceResponseRecord.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.FirewallInstanceResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this GetFirewallInstanceResponseRecord.

        防火墙资源列表

        :param resources: The resources of this GetFirewallInstanceResponseRecord.
        :type resources: list[:class:`huaweicloudsdkcfw.v1.FirewallInstanceResource`]
        """
        self._resources = resources

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
