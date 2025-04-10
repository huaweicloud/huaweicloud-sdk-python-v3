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
        'status': 'int',
        'tags': 'str'
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
        'status': 'status',
        'tags': 'tags'
    }

    def __init__(self, fw_instance_id=None, resource_id=None, name=None, fw_instance_name=None, enterprise_project_id=None, ha_type=None, charge_mode=None, service_type=None, engine_type=None, flavor=None, status=None, tags=None):
        r"""FirewallInstanceVO

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙实例id，创建云防火墙后用于标记防火墙由系统自动生成的id。
        :type fw_instance_id: str
        :param resource_id: 资源id，与防火墙实例id fw_instance_id相同
        :type resource_id: str
        :param name: 创建防火墙时的时间戳
        :type name: str
        :param fw_instance_name: 防火墙名称
        :type fw_instance_name: str
        :param enterprise_project_id: 企业项目id，用户支持企业项目后，由企业项目生成的id。
        :type enterprise_project_id: str
        :param ha_type: 集群类型，包含主备（0）和集群（1）两种方式，主备模式包含四个节点，2个主节点构成集群，剩余两个节点为主节点的备节点，集群模式仅拉起两个节点作为集群。
        :type ha_type: int
        :param charge_mode: 计费模式 0：包年/包月 1：按需
        :type charge_mode: int
        :param service_type: 防火墙防护类型，目前仅支持0，互联网防护。
        :type service_type: int
        :param engine_type: 引擎类型，0：自研引擎 1：山石引擎 3：天融信引擎
        :type engine_type: int
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkcfw.v1.Flavor`
        :param status: 防火墙状态列表，包括-1：等待支付，0：创建中，1：删除中，2：运行中，3：升级中，4：删除完成：5：冻结中，6：创建失败，7：删除失败，8：冻结失败，9：存储中，10：存储失败，11：升级失败
        :type status: int
        :param tags: 标签列表，标签键值map转化的json字符串，如\&quot;{\\\&quot;key\\\&quot;:\\\&quot;value\\\&quot;}\&quot;
        :type tags: str
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
        self._tags = None
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
        if tags is not None:
            self.tags = tags

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this FirewallInstanceVO.

        防火墙实例id，创建云防火墙后用于标记防火墙由系统自动生成的id。

        :return: The fw_instance_id of this FirewallInstanceVO.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this FirewallInstanceVO.

        防火墙实例id，创建云防火墙后用于标记防火墙由系统自动生成的id。

        :param fw_instance_id: The fw_instance_id of this FirewallInstanceVO.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this FirewallInstanceVO.

        资源id，与防火墙实例id fw_instance_id相同

        :return: The resource_id of this FirewallInstanceVO.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this FirewallInstanceVO.

        资源id，与防火墙实例id fw_instance_id相同

        :param resource_id: The resource_id of this FirewallInstanceVO.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def name(self):
        r"""Gets the name of this FirewallInstanceVO.

        创建防火墙时的时间戳

        :return: The name of this FirewallInstanceVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FirewallInstanceVO.

        创建防火墙时的时间戳

        :param name: The name of this FirewallInstanceVO.
        :type name: str
        """
        self._name = name

    @property
    def fw_instance_name(self):
        r"""Gets the fw_instance_name of this FirewallInstanceVO.

        防火墙名称

        :return: The fw_instance_name of this FirewallInstanceVO.
        :rtype: str
        """
        return self._fw_instance_name

    @fw_instance_name.setter
    def fw_instance_name(self, fw_instance_name):
        r"""Sets the fw_instance_name of this FirewallInstanceVO.

        防火墙名称

        :param fw_instance_name: The fw_instance_name of this FirewallInstanceVO.
        :type fw_instance_name: str
        """
        self._fw_instance_name = fw_instance_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this FirewallInstanceVO.

        企业项目id，用户支持企业项目后，由企业项目生成的id。

        :return: The enterprise_project_id of this FirewallInstanceVO.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this FirewallInstanceVO.

        企业项目id，用户支持企业项目后，由企业项目生成的id。

        :param enterprise_project_id: The enterprise_project_id of this FirewallInstanceVO.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ha_type(self):
        r"""Gets the ha_type of this FirewallInstanceVO.

        集群类型，包含主备（0）和集群（1）两种方式，主备模式包含四个节点，2个主节点构成集群，剩余两个节点为主节点的备节点，集群模式仅拉起两个节点作为集群。

        :return: The ha_type of this FirewallInstanceVO.
        :rtype: int
        """
        return self._ha_type

    @ha_type.setter
    def ha_type(self, ha_type):
        r"""Sets the ha_type of this FirewallInstanceVO.

        集群类型，包含主备（0）和集群（1）两种方式，主备模式包含四个节点，2个主节点构成集群，剩余两个节点为主节点的备节点，集群模式仅拉起两个节点作为集群。

        :param ha_type: The ha_type of this FirewallInstanceVO.
        :type ha_type: int
        """
        self._ha_type = ha_type

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this FirewallInstanceVO.

        计费模式 0：包年/包月 1：按需

        :return: The charge_mode of this FirewallInstanceVO.
        :rtype: int
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this FirewallInstanceVO.

        计费模式 0：包年/包月 1：按需

        :param charge_mode: The charge_mode of this FirewallInstanceVO.
        :type charge_mode: int
        """
        self._charge_mode = charge_mode

    @property
    def service_type(self):
        r"""Gets the service_type of this FirewallInstanceVO.

        防火墙防护类型，目前仅支持0，互联网防护。

        :return: The service_type of this FirewallInstanceVO.
        :rtype: int
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this FirewallInstanceVO.

        防火墙防护类型，目前仅支持0，互联网防护。

        :param service_type: The service_type of this FirewallInstanceVO.
        :type service_type: int
        """
        self._service_type = service_type

    @property
    def engine_type(self):
        r"""Gets the engine_type of this FirewallInstanceVO.

        引擎类型，0：自研引擎 1：山石引擎 3：天融信引擎

        :return: The engine_type of this FirewallInstanceVO.
        :rtype: int
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this FirewallInstanceVO.

        引擎类型，0：自研引擎 1：山石引擎 3：天融信引擎

        :param engine_type: The engine_type of this FirewallInstanceVO.
        :type engine_type: int
        """
        self._engine_type = engine_type

    @property
    def flavor(self):
        r"""Gets the flavor of this FirewallInstanceVO.

        :return: The flavor of this FirewallInstanceVO.
        :rtype: :class:`huaweicloudsdkcfw.v1.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this FirewallInstanceVO.

        :param flavor: The flavor of this FirewallInstanceVO.
        :type flavor: :class:`huaweicloudsdkcfw.v1.Flavor`
        """
        self._flavor = flavor

    @property
    def status(self):
        r"""Gets the status of this FirewallInstanceVO.

        防火墙状态列表，包括-1：等待支付，0：创建中，1：删除中，2：运行中，3：升级中，4：删除完成：5：冻结中，6：创建失败，7：删除失败，8：冻结失败，9：存储中，10：存储失败，11：升级失败

        :return: The status of this FirewallInstanceVO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FirewallInstanceVO.

        防火墙状态列表，包括-1：等待支付，0：创建中，1：删除中，2：运行中，3：升级中，4：删除完成：5：冻结中，6：创建失败，7：删除失败，8：冻结失败，9：存储中，10：存储失败，11：升级失败

        :param status: The status of this FirewallInstanceVO.
        :type status: int
        """
        self._status = status

    @property
    def tags(self):
        r"""Gets the tags of this FirewallInstanceVO.

        标签列表，标签键值map转化的json字符串，如\"{\\\"key\\\":\\\"value\\\"}\"

        :return: The tags of this FirewallInstanceVO.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this FirewallInstanceVO.

        标签列表，标签键值map转化的json字符串，如\"{\\\"key\\\":\\\"value\\\"}\"

        :param tags: The tags of this FirewallInstanceVO.
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
        if not isinstance(other, FirewallInstanceVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
