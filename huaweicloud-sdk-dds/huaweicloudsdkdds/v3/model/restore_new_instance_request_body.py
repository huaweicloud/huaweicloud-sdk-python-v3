# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreNewInstanceRequestBody:

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
        'availability_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'password': 'str',
        'disk_encryption_id': 'str',
        'configurations': 'list[RestoreNewInstanceConfigurationsOption]',
        'flavor': 'list[RestoreNewInstanceFlavorOption]',
        'backup_strategy': 'BackupStrategy',
        'enterprise_project_id': 'str',
        'ssl_option': 'str',
        'dss_pool_id': 'str',
        'server_group_policies': 'list[str]',
        'restore_point': 'RestorePoint',
        'charge_info': 'ChargeInfoOption'
    }

    attribute_map = {
        'name': 'name',
        'availability_zone': 'availability_zone',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'password': 'password',
        'disk_encryption_id': 'disk_encryption_id',
        'configurations': 'configurations',
        'flavor': 'flavor',
        'backup_strategy': 'backup_strategy',
        'enterprise_project_id': 'enterprise_project_id',
        'ssl_option': 'ssl_option',
        'dss_pool_id': 'dss_pool_id',
        'server_group_policies': 'server_group_policies',
        'restore_point': 'restore_point',
        'charge_info': 'charge_info'
    }

    def __init__(self, name=None, availability_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, password=None, disk_encryption_id=None, configurations=None, flavor=None, backup_strategy=None, enterprise_project_id=None, ssl_option=None, dss_pool_id=None, server_group_policies=None, restore_point=None, charge_info=None):
        """RestoreNewInstanceRequestBody

        The model defined in huaweicloud sdk

        :param name: 实例名称。用于表示实例的名称，用于表示实例的名称，允许和已有名称重复。 取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。
        :type name: str
        :param availability_zone: 可用区ID，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。
        :type availability_zone: str
        :param vpc_id: 虚拟私有云ID。获取方法请参见《虚拟私有云API参考》中“VPC”的内容。 取值：非空，字符长度校验，严格UUID正则校验。
        :type vpc_id: str
        :param subnet_id: 子网ID。获取方法请参见《虚拟私有云API参考》中“子网”的内容。
        :type subnet_id: str
        :param security_group_id: 指定实例所属的安全组ID。 获取方法请参见《虚拟私有云API参考》中“安全组”的内容。
        :type security_group_id: str
        :param password: 数据库密码。 取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_&#x3D;+?的组合。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。
        :type password: str
        :param disk_encryption_id: 磁盘加密时的密钥ID，严格UUID正则校验。 不传该参数时，表示不进行磁盘加密。
        :type disk_encryption_id: str
        :param configurations: 参数组配置信息。
        :type configurations: list[:class:`huaweicloudsdkdds.v3.RestoreNewInstanceConfigurationsOption`]
        :param flavor: 实例规格详情。
        :type flavor: list[:class:`huaweicloudsdkdds.v3.RestoreNewInstanceFlavorOption`]
        :param backup_strategy: 
        :type backup_strategy: :class:`huaweicloudsdkdds.v3.BackupStrategy`
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param ssl_option: SSL开关选项。 取值： - 取“0”，表示DDS实例默认不启用SSL连接。 - 取“1”，表示DDS实例默认启用SSL连接。 - 不传该参数时，默认启用SSL连接。
        :type ssl_option: str
        :param dss_pool_id: 创建新实例所在专属存储池ID，仅专属云创建实例时有效。
        :type dss_pool_id: str
        :param server_group_policies: 创建新实例设置云服务器组关联的策略名称列表，仅专属云创建实例时有效。 取值    - 取“anti-affinity”，表示DDS实例开启反亲和部署，反亲和部署是出于高可用性考虑，将您的Primary、Secondary和Hidden节点分别创建在不同的物理机上。当前仅支持该值，不传该值默认不开启反亲和部署。
        :type server_group_policies: list[str]
        :param restore_point: 
        :type restore_point: :class:`huaweicloudsdkdds.v3.RestorePoint`
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkdds.v3.ChargeInfoOption`
        """
        
        

        self._name = None
        self._availability_zone = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._password = None
        self._disk_encryption_id = None
        self._configurations = None
        self._flavor = None
        self._backup_strategy = None
        self._enterprise_project_id = None
        self._ssl_option = None
        self._dss_pool_id = None
        self._server_group_policies = None
        self._restore_point = None
        self._charge_info = None
        self.discriminator = None

        self.name = name
        self.availability_zone = availability_zone
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        if password is not None:
            self.password = password
        if disk_encryption_id is not None:
            self.disk_encryption_id = disk_encryption_id
        if configurations is not None:
            self.configurations = configurations
        self.flavor = flavor
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ssl_option is not None:
            self.ssl_option = ssl_option
        if dss_pool_id is not None:
            self.dss_pool_id = dss_pool_id
        if server_group_policies is not None:
            self.server_group_policies = server_group_policies
        self.restore_point = restore_point
        if charge_info is not None:
            self.charge_info = charge_info

    @property
    def name(self):
        """Gets the name of this RestoreNewInstanceRequestBody.

        实例名称。用于表示实例的名称，用于表示实例的名称，允许和已有名称重复。 取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。

        :return: The name of this RestoreNewInstanceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RestoreNewInstanceRequestBody.

        实例名称。用于表示实例的名称，用于表示实例的名称，允许和已有名称重复。 取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。

        :param name: The name of this RestoreNewInstanceRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def availability_zone(self):
        """Gets the availability_zone of this RestoreNewInstanceRequestBody.

        可用区ID，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :return: The availability_zone of this RestoreNewInstanceRequestBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this RestoreNewInstanceRequestBody.

        可用区ID，请参见[地区和终端节点](https://developer.huaweicloud.com/endpoint)。

        :param availability_zone: The availability_zone of this RestoreNewInstanceRequestBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this RestoreNewInstanceRequestBody.

        虚拟私有云ID。获取方法请参见《虚拟私有云API参考》中“VPC”的内容。 取值：非空，字符长度校验，严格UUID正则校验。

        :return: The vpc_id of this RestoreNewInstanceRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this RestoreNewInstanceRequestBody.

        虚拟私有云ID。获取方法请参见《虚拟私有云API参考》中“VPC”的内容。 取值：非空，字符长度校验，严格UUID正则校验。

        :param vpc_id: The vpc_id of this RestoreNewInstanceRequestBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this RestoreNewInstanceRequestBody.

        子网ID。获取方法请参见《虚拟私有云API参考》中“子网”的内容。

        :return: The subnet_id of this RestoreNewInstanceRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this RestoreNewInstanceRequestBody.

        子网ID。获取方法请参见《虚拟私有云API参考》中“子网”的内容。

        :param subnet_id: The subnet_id of this RestoreNewInstanceRequestBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this RestoreNewInstanceRequestBody.

        指定实例所属的安全组ID。 获取方法请参见《虚拟私有云API参考》中“安全组”的内容。

        :return: The security_group_id of this RestoreNewInstanceRequestBody.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this RestoreNewInstanceRequestBody.

        指定实例所属的安全组ID。 获取方法请参见《虚拟私有云API参考》中“安全组”的内容。

        :param security_group_id: The security_group_id of this RestoreNewInstanceRequestBody.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def password(self):
        """Gets the password of this RestoreNewInstanceRequestBody.

        数据库密码。 取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The password of this RestoreNewInstanceRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RestoreNewInstanceRequestBody.

        数据库密码。 取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param password: The password of this RestoreNewInstanceRequestBody.
        :type password: str
        """
        self._password = password

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this RestoreNewInstanceRequestBody.

        磁盘加密时的密钥ID，严格UUID正则校验。 不传该参数时，表示不进行磁盘加密。

        :return: The disk_encryption_id of this RestoreNewInstanceRequestBody.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this RestoreNewInstanceRequestBody.

        磁盘加密时的密钥ID，严格UUID正则校验。 不传该参数时，表示不进行磁盘加密。

        :param disk_encryption_id: The disk_encryption_id of this RestoreNewInstanceRequestBody.
        :type disk_encryption_id: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def configurations(self):
        """Gets the configurations of this RestoreNewInstanceRequestBody.

        参数组配置信息。

        :return: The configurations of this RestoreNewInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdkdds.v3.RestoreNewInstanceConfigurationsOption`]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """Sets the configurations of this RestoreNewInstanceRequestBody.

        参数组配置信息。

        :param configurations: The configurations of this RestoreNewInstanceRequestBody.
        :type configurations: list[:class:`huaweicloudsdkdds.v3.RestoreNewInstanceConfigurationsOption`]
        """
        self._configurations = configurations

    @property
    def flavor(self):
        """Gets the flavor of this RestoreNewInstanceRequestBody.

        实例规格详情。

        :return: The flavor of this RestoreNewInstanceRequestBody.
        :rtype: list[:class:`huaweicloudsdkdds.v3.RestoreNewInstanceFlavorOption`]
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this RestoreNewInstanceRequestBody.

        实例规格详情。

        :param flavor: The flavor of this RestoreNewInstanceRequestBody.
        :type flavor: list[:class:`huaweicloudsdkdds.v3.RestoreNewInstanceFlavorOption`]
        """
        self._flavor = flavor

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this RestoreNewInstanceRequestBody.


        :return: The backup_strategy of this RestoreNewInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkdds.v3.BackupStrategy`
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this RestoreNewInstanceRequestBody.


        :param backup_strategy: The backup_strategy of this RestoreNewInstanceRequestBody.
        :type backup_strategy: :class:`huaweicloudsdkdds.v3.BackupStrategy`
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this RestoreNewInstanceRequestBody.

        企业项目ID。

        :return: The enterprise_project_id of this RestoreNewInstanceRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this RestoreNewInstanceRequestBody.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this RestoreNewInstanceRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ssl_option(self):
        """Gets the ssl_option of this RestoreNewInstanceRequestBody.

        SSL开关选项。 取值： - 取“0”，表示DDS实例默认不启用SSL连接。 - 取“1”，表示DDS实例默认启用SSL连接。 - 不传该参数时，默认启用SSL连接。

        :return: The ssl_option of this RestoreNewInstanceRequestBody.
        :rtype: str
        """
        return self._ssl_option

    @ssl_option.setter
    def ssl_option(self, ssl_option):
        """Sets the ssl_option of this RestoreNewInstanceRequestBody.

        SSL开关选项。 取值： - 取“0”，表示DDS实例默认不启用SSL连接。 - 取“1”，表示DDS实例默认启用SSL连接。 - 不传该参数时，默认启用SSL连接。

        :param ssl_option: The ssl_option of this RestoreNewInstanceRequestBody.
        :type ssl_option: str
        """
        self._ssl_option = ssl_option

    @property
    def dss_pool_id(self):
        """Gets the dss_pool_id of this RestoreNewInstanceRequestBody.

        创建新实例所在专属存储池ID，仅专属云创建实例时有效。

        :return: The dss_pool_id of this RestoreNewInstanceRequestBody.
        :rtype: str
        """
        return self._dss_pool_id

    @dss_pool_id.setter
    def dss_pool_id(self, dss_pool_id):
        """Sets the dss_pool_id of this RestoreNewInstanceRequestBody.

        创建新实例所在专属存储池ID，仅专属云创建实例时有效。

        :param dss_pool_id: The dss_pool_id of this RestoreNewInstanceRequestBody.
        :type dss_pool_id: str
        """
        self._dss_pool_id = dss_pool_id

    @property
    def server_group_policies(self):
        """Gets the server_group_policies of this RestoreNewInstanceRequestBody.

        创建新实例设置云服务器组关联的策略名称列表，仅专属云创建实例时有效。 取值    - 取“anti-affinity”，表示DDS实例开启反亲和部署，反亲和部署是出于高可用性考虑，将您的Primary、Secondary和Hidden节点分别创建在不同的物理机上。当前仅支持该值，不传该值默认不开启反亲和部署。

        :return: The server_group_policies of this RestoreNewInstanceRequestBody.
        :rtype: list[str]
        """
        return self._server_group_policies

    @server_group_policies.setter
    def server_group_policies(self, server_group_policies):
        """Sets the server_group_policies of this RestoreNewInstanceRequestBody.

        创建新实例设置云服务器组关联的策略名称列表，仅专属云创建实例时有效。 取值    - 取“anti-affinity”，表示DDS实例开启反亲和部署，反亲和部署是出于高可用性考虑，将您的Primary、Secondary和Hidden节点分别创建在不同的物理机上。当前仅支持该值，不传该值默认不开启反亲和部署。

        :param server_group_policies: The server_group_policies of this RestoreNewInstanceRequestBody.
        :type server_group_policies: list[str]
        """
        self._server_group_policies = server_group_policies

    @property
    def restore_point(self):
        """Gets the restore_point of this RestoreNewInstanceRequestBody.


        :return: The restore_point of this RestoreNewInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkdds.v3.RestorePoint`
        """
        return self._restore_point

    @restore_point.setter
    def restore_point(self, restore_point):
        """Sets the restore_point of this RestoreNewInstanceRequestBody.


        :param restore_point: The restore_point of this RestoreNewInstanceRequestBody.
        :type restore_point: :class:`huaweicloudsdkdds.v3.RestorePoint`
        """
        self._restore_point = restore_point

    @property
    def charge_info(self):
        """Gets the charge_info of this RestoreNewInstanceRequestBody.


        :return: The charge_info of this RestoreNewInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkdds.v3.ChargeInfoOption`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        """Sets the charge_info of this RestoreNewInstanceRequestBody.


        :param charge_info: The charge_info of this RestoreNewInstanceRequestBody.
        :type charge_info: :class:`huaweicloudsdkdds.v3.ChargeInfoOption`
        """
        self._charge_info = charge_info

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
        if not isinstance(other, RestoreNewInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
