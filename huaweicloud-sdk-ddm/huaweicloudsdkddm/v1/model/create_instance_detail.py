# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceDetail:

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
        'flavor_id': 'str',
        'node_num': 'int',
        'engine_id': 'str',
        'enterprise_project_id': 'str',
        'available_zones': 'list[str]',
        'vpc_id': 'str',
        'security_group_id': 'str',
        'subnet_id': 'str',
        'param_group_id': 'str',
        'time_zone': 'str',
        'admin_user_name': 'str',
        'admin_user_password': 'str'
    }

    attribute_map = {
        'name': 'name',
        'flavor_id': 'flavor_id',
        'node_num': 'node_num',
        'engine_id': 'engine_id',
        'enterprise_project_id': 'enterprise_project_id',
        'available_zones': 'available_zones',
        'vpc_id': 'vpc_id',
        'security_group_id': 'security_group_id',
        'subnet_id': 'subnet_id',
        'param_group_id': 'param_group_id',
        'time_zone': 'time_zone',
        'admin_user_name': 'admin_user_name',
        'admin_user_password': 'admin_user_password'
    }

    def __init__(self, name=None, flavor_id=None, node_num=None, engine_id=None, enterprise_project_id=None, available_zones=None, vpc_id=None, security_group_id=None, subnet_id=None, param_group_id=None, time_zone=None, admin_user_name=None, admin_user_password=None):
        """CreateInstanceDetail

        The model defined in huaweicloud sdk

        :param name: DDM实例名称，命名要求如下。 - 长度为4-64个字符。 - 必须以字母开头。 - 可以包含字母、数字、中划线，不能包含其它特殊字符。
        :type name: str
        :param flavor_id: 规格ID。
        :type flavor_id: str
        :param node_num: 节点个数。
        :type node_num: int
        :param engine_id: 引擎ID。
        :type engine_id: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param available_zones: 可用区code。取值非空，请参见地区和终端节点(https://developer.huaweicloud.com/endpoint?DDM)。
        :type available_zones: list[str]
        :param vpc_id: 虚拟私有云的ID。
        :type vpc_id: str
        :param security_group_id: 安全组ID。
        :type security_group_id: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param param_group_id: 参数组ID.
        :type param_group_id: str
        :param time_zone: UTC时区。默认为UTC。取值范围：\&quot;UTC\&quot;,\&quot;UTC-12:00\&quot;,\&quot;UTC-11:00\&quot;,\&quot;UTC-10:00\&quot;,\&quot;UTC-09:00\&quot;, \&quot;UTC-08:00\&quot;, \&quot;UTC-07:00\&quot;, \&quot;UTC-06:00\&quot;, \&quot;UTC-05:00\&quot;, \&quot;UTC-04:00\&quot;, \&quot;UTC-03:00\&quot;, \&quot;UTC-02:00\&quot;, \&quot;UTC-01:00\&quot;, \&quot;UTC+01:00\&quot;, \&quot;UTC+02:00\&quot;, \&quot;UTC+03:00\&quot;, \&quot;UTC+04:00\&quot;, \&quot;UTC+05:00\&quot;, \&quot;UTC+06:00\&quot;, \&quot;UTC+07:00\&quot;, \&quot;UTC+08:00\&quot;, \&quot;UTC+09:00\&quot;, \&quot;UTC+10:00\&quot;, \&quot;UTC+11:00\&quot;, \&quot;UTC+12:00\&quot;
        :type time_zone: str
        :param admin_user_name: 管理员账号用户名。 - 长度为1-32个字符。 - 必须以字母开头。 - 可以包含字母，数字、下划线，不能包含其它特殊字符。
        :type admin_user_name: str
        :param admin_user_password: 管理员账号密码。 - 长度为8~32位。 - 必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_&#x3D;+?的组合。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。
        :type admin_user_password: str
        """
        
        

        self._name = None
        self._flavor_id = None
        self._node_num = None
        self._engine_id = None
        self._enterprise_project_id = None
        self._available_zones = None
        self._vpc_id = None
        self._security_group_id = None
        self._subnet_id = None
        self._param_group_id = None
        self._time_zone = None
        self._admin_user_name = None
        self._admin_user_password = None
        self.discriminator = None

        self.name = name
        self.flavor_id = flavor_id
        self.node_num = node_num
        self.engine_id = engine_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.available_zones = available_zones
        self.vpc_id = vpc_id
        self.security_group_id = security_group_id
        self.subnet_id = subnet_id
        if param_group_id is not None:
            self.param_group_id = param_group_id
        if time_zone is not None:
            self.time_zone = time_zone
        if admin_user_name is not None:
            self.admin_user_name = admin_user_name
        if admin_user_password is not None:
            self.admin_user_password = admin_user_password

    @property
    def name(self):
        """Gets the name of this CreateInstanceDetail.

        DDM实例名称，命名要求如下。 - 长度为4-64个字符。 - 必须以字母开头。 - 可以包含字母、数字、中划线，不能包含其它特殊字符。

        :return: The name of this CreateInstanceDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstanceDetail.

        DDM实例名称，命名要求如下。 - 长度为4-64个字符。 - 必须以字母开头。 - 可以包含字母、数字、中划线，不能包含其它特殊字符。

        :param name: The name of this CreateInstanceDetail.
        :type name: str
        """
        self._name = name

    @property
    def flavor_id(self):
        """Gets the flavor_id of this CreateInstanceDetail.

        规格ID。

        :return: The flavor_id of this CreateInstanceDetail.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        """Sets the flavor_id of this CreateInstanceDetail.

        规格ID。

        :param flavor_id: The flavor_id of this CreateInstanceDetail.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def node_num(self):
        """Gets the node_num of this CreateInstanceDetail.

        节点个数。

        :return: The node_num of this CreateInstanceDetail.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this CreateInstanceDetail.

        节点个数。

        :param node_num: The node_num of this CreateInstanceDetail.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def engine_id(self):
        """Gets the engine_id of this CreateInstanceDetail.

        引擎ID。

        :return: The engine_id of this CreateInstanceDetail.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """Sets the engine_id of this CreateInstanceDetail.

        引擎ID。

        :param engine_id: The engine_id of this CreateInstanceDetail.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateInstanceDetail.

        企业项目ID。

        :return: The enterprise_project_id of this CreateInstanceDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateInstanceDetail.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def available_zones(self):
        """Gets the available_zones of this CreateInstanceDetail.

        可用区code。取值非空，请参见地区和终端节点(https://developer.huaweicloud.com/endpoint?DDM)。

        :return: The available_zones of this CreateInstanceDetail.
        :rtype: list[str]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this CreateInstanceDetail.

        可用区code。取值非空，请参见地区和终端节点(https://developer.huaweicloud.com/endpoint?DDM)。

        :param available_zones: The available_zones of this CreateInstanceDetail.
        :type available_zones: list[str]
        """
        self._available_zones = available_zones

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateInstanceDetail.

        虚拟私有云的ID。

        :return: The vpc_id of this CreateInstanceDetail.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateInstanceDetail.

        虚拟私有云的ID。

        :param vpc_id: The vpc_id of this CreateInstanceDetail.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateInstanceDetail.

        安全组ID。

        :return: The security_group_id of this CreateInstanceDetail.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateInstanceDetail.

        安全组ID。

        :param security_group_id: The security_group_id of this CreateInstanceDetail.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateInstanceDetail.

        子网ID。

        :return: The subnet_id of this CreateInstanceDetail.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateInstanceDetail.

        子网ID。

        :param subnet_id: The subnet_id of this CreateInstanceDetail.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def param_group_id(self):
        """Gets the param_group_id of this CreateInstanceDetail.

        参数组ID.

        :return: The param_group_id of this CreateInstanceDetail.
        :rtype: str
        """
        return self._param_group_id

    @param_group_id.setter
    def param_group_id(self, param_group_id):
        """Sets the param_group_id of this CreateInstanceDetail.

        参数组ID.

        :param param_group_id: The param_group_id of this CreateInstanceDetail.
        :type param_group_id: str
        """
        self._param_group_id = param_group_id

    @property
    def time_zone(self):
        """Gets the time_zone of this CreateInstanceDetail.

        UTC时区。默认为UTC。取值范围：\"UTC\",\"UTC-12:00\",\"UTC-11:00\",\"UTC-10:00\",\"UTC-09:00\", \"UTC-08:00\", \"UTC-07:00\", \"UTC-06:00\", \"UTC-05:00\", \"UTC-04:00\", \"UTC-03:00\", \"UTC-02:00\", \"UTC-01:00\", \"UTC+01:00\", \"UTC+02:00\", \"UTC+03:00\", \"UTC+04:00\", \"UTC+05:00\", \"UTC+06:00\", \"UTC+07:00\", \"UTC+08:00\", \"UTC+09:00\", \"UTC+10:00\", \"UTC+11:00\", \"UTC+12:00\"

        :return: The time_zone of this CreateInstanceDetail.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this CreateInstanceDetail.

        UTC时区。默认为UTC。取值范围：\"UTC\",\"UTC-12:00\",\"UTC-11:00\",\"UTC-10:00\",\"UTC-09:00\", \"UTC-08:00\", \"UTC-07:00\", \"UTC-06:00\", \"UTC-05:00\", \"UTC-04:00\", \"UTC-03:00\", \"UTC-02:00\", \"UTC-01:00\", \"UTC+01:00\", \"UTC+02:00\", \"UTC+03:00\", \"UTC+04:00\", \"UTC+05:00\", \"UTC+06:00\", \"UTC+07:00\", \"UTC+08:00\", \"UTC+09:00\", \"UTC+10:00\", \"UTC+11:00\", \"UTC+12:00\"

        :param time_zone: The time_zone of this CreateInstanceDetail.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def admin_user_name(self):
        """Gets the admin_user_name of this CreateInstanceDetail.

        管理员账号用户名。 - 长度为1-32个字符。 - 必须以字母开头。 - 可以包含字母，数字、下划线，不能包含其它特殊字符。

        :return: The admin_user_name of this CreateInstanceDetail.
        :rtype: str
        """
        return self._admin_user_name

    @admin_user_name.setter
    def admin_user_name(self, admin_user_name):
        """Sets the admin_user_name of this CreateInstanceDetail.

        管理员账号用户名。 - 长度为1-32个字符。 - 必须以字母开头。 - 可以包含字母，数字、下划线，不能包含其它特殊字符。

        :param admin_user_name: The admin_user_name of this CreateInstanceDetail.
        :type admin_user_name: str
        """
        self._admin_user_name = admin_user_name

    @property
    def admin_user_password(self):
        """Gets the admin_user_password of this CreateInstanceDetail.

        管理员账号密码。 - 长度为8~32位。 - 必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The admin_user_password of this CreateInstanceDetail.
        :rtype: str
        """
        return self._admin_user_password

    @admin_user_password.setter
    def admin_user_password(self, admin_user_password):
        """Sets the admin_user_password of this CreateInstanceDetail.

        管理员账号密码。 - 长度为8~32位。 - 必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param admin_user_password: The admin_user_password of this CreateInstanceDetail.
        :type admin_user_password: str
        """
        self._admin_user_password = admin_user_password

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
        if not isinstance(other, CreateInstanceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
