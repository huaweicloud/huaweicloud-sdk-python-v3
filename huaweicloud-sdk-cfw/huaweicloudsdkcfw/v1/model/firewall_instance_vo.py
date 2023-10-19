# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FirewallInstanceVO:

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
        'resource_id': 'str',
        'name': 'str',
        'fw_instance_name': 'str',
        'enterprise_project_id': 'str',
        'ha_type': 'int',
        'charge_mode': 'int',
        'service_type': 'int',
        'engine_type': 'int',
        'flavor': 'Flavor',
        'status': 'int'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'resource_id': 'resource_id',
        'name': 'name',
        'fw_instance_name': 'fw_instance_name',
        'enterprise_project_id': 'enterprise_project_id',
        'ha_type': 'ha_type',
        'charge_mode': 'charge_mode',
        'service_type': 'service_type',
        'engine_type': 'engine_type',
        'flavor': 'flavor',
        'status': 'status'
    }

    def __init__(self, fw_instance_id=None, resource_id=None, name=None, fw_instance_name=None, enterprise_project_id=None, ha_type=None, charge_mode=None, service_type=None, engine_type=None, flavor=None, status=None):
        """FirewallInstanceVO

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。默认情况下，fw_instance_Id为空时，返回帐号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。
        :type fw_instance_id: str
        :param resource_id: 资源id
        :type resource_id: str
        :param name: 防火墙创建时间戳
        :type name: str
        :param fw_instance_name: 防火墙名称
        :type fw_instance_name: str
        :param enterprise_project_id: 企业项目id，用户支持企业项目后，由企业项目生成的id。
        :type enterprise_project_id: str
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
        :param status: 防火墙状态列表，包括-1：等待支付，0：创建中，1，删除中，2：运行中，3：升级中，4：删除完成：5：冻结中，6：创建失败，7：删除失败，8：冻结失败，9：存储中，10：存储失败，11：升级失败
        :type status: int
        """
        
        

        self._fw_instance_id = None
        self._resource_id = None
        self._name = None
        self._fw_instance_name = None
        self._enterprise_project_id = None
        self._ha_type = None
        self._charge_mode = None
        self._service_type = None
        self._engine_type = None
        self._flavor = None
        self._status = None
        self.discriminator = None

        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id
        if resource_id is not None:
            self.resource_id = resource_id
        if name is not None:
            self.name = name
        if fw_instance_name is not None:
            self.fw_instance_name = fw_instance_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
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
        if status is not None:
            self.status = status

    @property
    def fw_instance_id(self):
        """Gets the fw_instance_id of this FirewallInstanceVO.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。默认情况下，fw_instance_Id为空时，返回帐号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。

        :return: The fw_instance_id of this FirewallInstanceVO.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        """Sets the fw_instance_id of this FirewallInstanceVO.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。默认情况下，fw_instance_Id为空时，返回帐号下第一个墙的信息；fw_instance_Id非空时，返回与fw_instance_Id对应墙的信息。

        :param fw_instance_id: The fw_instance_id of this FirewallInstanceVO.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def resource_id(self):
        """Gets the resource_id of this FirewallInstanceVO.

        资源id

        :return: The resource_id of this FirewallInstanceVO.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this FirewallInstanceVO.

        资源id

        :param resource_id: The resource_id of this FirewallInstanceVO.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def name(self):
        """Gets the name of this FirewallInstanceVO.

        防火墙创建时间戳

        :return: The name of this FirewallInstanceVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FirewallInstanceVO.

        防火墙创建时间戳

        :param name: The name of this FirewallInstanceVO.
        :type name: str
        """
        self._name = name

    @property
    def fw_instance_name(self):
        """Gets the fw_instance_name of this FirewallInstanceVO.

        防火墙名称

        :return: The fw_instance_name of this FirewallInstanceVO.
        :rtype: str
        """
        return self._fw_instance_name

    @fw_instance_name.setter
    def fw_instance_name(self, fw_instance_name):
        """Sets the fw_instance_name of this FirewallInstanceVO.

        防火墙名称

        :param fw_instance_name: The fw_instance_name of this FirewallInstanceVO.
        :type fw_instance_name: str
        """
        self._fw_instance_name = fw_instance_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this FirewallInstanceVO.

        企业项目id，用户支持企业项目后，由企业项目生成的id。

        :return: The enterprise_project_id of this FirewallInstanceVO.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this FirewallInstanceVO.

        企业项目id，用户支持企业项目后，由企业项目生成的id。

        :param enterprise_project_id: The enterprise_project_id of this FirewallInstanceVO.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ha_type(self):
        """Gets the ha_type of this FirewallInstanceVO.

        集群类型

        :return: The ha_type of this FirewallInstanceVO.
        :rtype: int
        """
        return self._ha_type

    @ha_type.setter
    def ha_type(self, ha_type):
        """Sets the ha_type of this FirewallInstanceVO.

        集群类型

        :param ha_type: The ha_type of this FirewallInstanceVO.
        :type ha_type: int
        """
        self._ha_type = ha_type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this FirewallInstanceVO.

        计费模式 0：包年/包月 1：按需

        :return: The charge_mode of this FirewallInstanceVO.
        :rtype: int
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this FirewallInstanceVO.

        计费模式 0：包年/包月 1：按需

        :param charge_mode: The charge_mode of this FirewallInstanceVO.
        :type charge_mode: int
        """
        self._charge_mode = charge_mode

    @property
    def service_type(self):
        """Gets the service_type of this FirewallInstanceVO.

        服务类型

        :return: The service_type of this FirewallInstanceVO.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this FirewallInstanceVO.

        服务类型

        :param service_type: The service_type of this FirewallInstanceVO.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def engine_type(self):
        """Gets the engine_type of this FirewallInstanceVO.

        引擎类型

        :return: The engine_type of this FirewallInstanceVO.
        :rtype: int
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this FirewallInstanceVO.

        引擎类型

        :param engine_type: The engine_type of this FirewallInstanceVO.
        :type engine_type: int
        """
        self._engine_type = engine_type

    @property
    def flavor(self):
        """Gets the flavor of this FirewallInstanceVO.

        :return: The flavor of this FirewallInstanceVO.
        :rtype: :class:`huaweicloudsdkcfw.v1.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this FirewallInstanceVO.

        :param flavor: The flavor of this FirewallInstanceVO.
        :type flavor: :class:`huaweicloudsdkcfw.v1.Flavor`
        """
        self._flavor = flavor

    @property
    def status(self):
        """Gets the status of this FirewallInstanceVO.

        防火墙状态列表，包括-1：等待支付，0：创建中，1，删除中，2：运行中，3：升级中，4：删除完成：5：冻结中，6：创建失败，7：删除失败，8：冻结失败，9：存储中，10：存储失败，11：升级失败

        :return: The status of this FirewallInstanceVO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FirewallInstanceVO.

        防火墙状态列表，包括-1：等待支付，0：创建中，1，删除中，2：运行中，3：升级中，4：删除完成：5：冻结中，6：创建失败，7：删除失败，8：冻结失败，9：存储中，10：存储失败，11：升级失败

        :param status: The status of this FirewallInstanceVO.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, FirewallInstanceVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
