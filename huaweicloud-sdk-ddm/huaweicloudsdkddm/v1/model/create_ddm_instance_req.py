# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDdmInstanceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'available_zones': 'list[str]',
        'node_num': 'int',
        'engine_version': 'str',
        'flavor_ref': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'param_group_id': 'str',
        'enterprise_project_id': 'str',
        'time_zone': 'str',
        'admin_user_name': 'str',
        'admin_user_password': 'str',
        'charge_info': 'object'
    }

    attribute_map = {
        'name': 'name',
        'available_zones': 'available_zones',
        'node_num': 'node_num',
        'engine_version': 'engine_version',
        'flavor_ref': 'flavor_ref',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'param_group_id': 'param_group_id',
        'enterprise_project_id': 'enterprise_project_id',
        'time_zone': 'time_zone',
        'admin_user_name': 'admin_user_name',
        'admin_user_password': 'admin_user_password',
        'charge_info': 'charge_info'
    }

    def __init__(self, name=None, available_zones=None, node_num=None, engine_version=None, flavor_ref=None, vpc_id=None, subnet_id=None, security_group_id=None, param_group_id=None, enterprise_project_id=None, time_zone=None, admin_user_name=None, admin_user_password=None, charge_info=None):
        r"""CreateDdmInstanceReq

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param available_zones: 可用区。
        :type available_zones: list[str]
        :param node_num: 节点数量。
        :type node_num: int
        :param engine_version: 引擎版本。
        :type engine_version: str
        :param flavor_ref: 规格。
        :type flavor_ref: str
        :param vpc_id: 虚拟私有云id。
        :type vpc_id: str
        :param subnet_id: 子网id。
        :type subnet_id: str
        :param security_group_id: 安全组id。
        :type security_group_id: str
        :param param_group_id: 参数组id。
        :type param_group_id: str
        :param enterprise_project_id: 企业项目id。
        :type enterprise_project_id: str
        :param time_zone: 时区。
        :type time_zone: str
        :param admin_user_name: 账号。
        :type admin_user_name: str
        :param admin_user_password: 密码。
        :type admin_user_password: str
        :param charge_info: 付费信息。
        :type charge_info: object
        """
        
        

        self._name = None
        self._available_zones = None
        self._node_num = None
        self._engine_version = None
        self._flavor_ref = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._param_group_id = None
        self._enterprise_project_id = None
        self._time_zone = None
        self._admin_user_name = None
        self._admin_user_password = None
        self._charge_info = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if available_zones is not None:
            self.available_zones = available_zones
        if node_num is not None:
            self.node_num = node_num
        if engine_version is not None:
            self.engine_version = engine_version
        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if param_group_id is not None:
            self.param_group_id = param_group_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if time_zone is not None:
            self.time_zone = time_zone
        if admin_user_name is not None:
            self.admin_user_name = admin_user_name
        if admin_user_password is not None:
            self.admin_user_password = admin_user_password
        if charge_info is not None:
            self.charge_info = charge_info

    @property
    def name(self):
        r"""Gets the name of this CreateDdmInstanceReq.

        实例名称。

        :return: The name of this CreateDdmInstanceReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDdmInstanceReq.

        实例名称。

        :param name: The name of this CreateDdmInstanceReq.
        :type name: str
        """
        self._name = name

    @property
    def available_zones(self):
        r"""Gets the available_zones of this CreateDdmInstanceReq.

        可用区。

        :return: The available_zones of this CreateDdmInstanceReq.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this CreateDdmInstanceReq.

        可用区。

        :param available_zones: The available_zones of this CreateDdmInstanceReq.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def node_num(self):
        r"""Gets the node_num of this CreateDdmInstanceReq.

        节点数量。

        :return: The node_num of this CreateDdmInstanceReq.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this CreateDdmInstanceReq.

        节点数量。

        :param node_num: The node_num of this CreateDdmInstanceReq.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def engine_version(self):
        r"""Gets the engine_version of this CreateDdmInstanceReq.

        引擎版本。

        :return: The engine_version of this CreateDdmInstanceReq.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this CreateDdmInstanceReq.

        引擎版本。

        :param engine_version: The engine_version of this CreateDdmInstanceReq.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this CreateDdmInstanceReq.

        规格。

        :return: The flavor_ref of this CreateDdmInstanceReq.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this CreateDdmInstanceReq.

        规格。

        :param flavor_ref: The flavor_ref of this CreateDdmInstanceReq.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateDdmInstanceReq.

        虚拟私有云id。

        :return: The vpc_id of this CreateDdmInstanceReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateDdmInstanceReq.

        虚拟私有云id。

        :param vpc_id: The vpc_id of this CreateDdmInstanceReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CreateDdmInstanceReq.

        子网id。

        :return: The subnet_id of this CreateDdmInstanceReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CreateDdmInstanceReq.

        子网id。

        :param subnet_id: The subnet_id of this CreateDdmInstanceReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this CreateDdmInstanceReq.

        安全组id。

        :return: The security_group_id of this CreateDdmInstanceReq.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this CreateDdmInstanceReq.

        安全组id。

        :param security_group_id: The security_group_id of this CreateDdmInstanceReq.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def param_group_id(self):
        r"""Gets the param_group_id of this CreateDdmInstanceReq.

        参数组id。

        :return: The param_group_id of this CreateDdmInstanceReq.
        :rtype: str
        """
        return self._param_group_id

    @param_group_id.setter
    def param_group_id(self, param_group_id):
        r"""Sets the param_group_id of this CreateDdmInstanceReq.

        参数组id。

        :param param_group_id: The param_group_id of this CreateDdmInstanceReq.
        :type param_group_id: str
        """
        self._param_group_id = param_group_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateDdmInstanceReq.

        企业项目id。

        :return: The enterprise_project_id of this CreateDdmInstanceReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateDdmInstanceReq.

        企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this CreateDdmInstanceReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def time_zone(self):
        r"""Gets the time_zone of this CreateDdmInstanceReq.

        时区。

        :return: The time_zone of this CreateDdmInstanceReq.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this CreateDdmInstanceReq.

        时区。

        :param time_zone: The time_zone of this CreateDdmInstanceReq.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def admin_user_name(self):
        r"""Gets the admin_user_name of this CreateDdmInstanceReq.

        账号。

        :return: The admin_user_name of this CreateDdmInstanceReq.
        :rtype: str
        """
        return self._admin_user_name

    @admin_user_name.setter
    def admin_user_name(self, admin_user_name):
        r"""Sets the admin_user_name of this CreateDdmInstanceReq.

        账号。

        :param admin_user_name: The admin_user_name of this CreateDdmInstanceReq.
        :type admin_user_name: str
        """
        self._admin_user_name = admin_user_name

    @property
    def admin_user_password(self):
        r"""Gets the admin_user_password of this CreateDdmInstanceReq.

        密码。

        :return: The admin_user_password of this CreateDdmInstanceReq.
        :rtype: str
        """
        return self._admin_user_password

    @admin_user_password.setter
    def admin_user_password(self, admin_user_password):
        r"""Sets the admin_user_password of this CreateDdmInstanceReq.

        密码。

        :param admin_user_password: The admin_user_password of this CreateDdmInstanceReq.
        :type admin_user_password: str
        """
        self._admin_user_password = admin_user_password

    @property
    def charge_info(self):
        r"""Gets the charge_info of this CreateDdmInstanceReq.

        付费信息。

        :return: The charge_info of this CreateDdmInstanceReq.
        :rtype: object
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this CreateDdmInstanceReq.

        付费信息。

        :param charge_info: The charge_info of this CreateDdmInstanceReq.
        :type charge_info: object
        """
        self._charge_info = charge_info

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateDdmInstanceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
