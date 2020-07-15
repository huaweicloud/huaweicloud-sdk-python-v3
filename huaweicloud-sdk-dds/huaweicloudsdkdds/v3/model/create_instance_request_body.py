# coding: utf-8

import pprint
import re

import six





class CreateInstanceRequestBody:


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
        'datastore': 'CreateInstanceDatastoreOption',
        'region': 'str',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'password': 'str',
        'disk_encryption_id': 'str',
        'mode': 'str',
        'flavor': 'list[CreateInstanceFlavorOption]',
        'storage': 'CreateInstanceStorageOption',
        'backup_strategy': 'CreateInstanceBackupStrategyOption',
        'enterprise_project_id': 'str',
        'ssl_option': 'str'
    }

    attribute_map = {
        'name': 'name',
        'datastore': 'datastore',
        'region': 'region',
        'availability_zone': 'availability_zone',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'password': 'password',
        'disk_encryption_id': 'disk_encryption_id',
        'mode': 'mode',
        'flavor': 'flavor',
        'storage': 'storage',
        'backup_strategy': 'backup_strategy',
        'enterprise_project_id': 'enterprise_project_id',
        'ssl_option': 'ssl_option'
    }

    def __init__(self, name=None, datastore=None, region=None, availability_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, password=None, disk_encryption_id=None, mode=None, flavor=None, storage=None, backup_strategy=None, enterprise_project_id=None, ssl_option=None):
        """CreateInstanceRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._datastore = None
        self._region = None
        self._availability_zone = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._password = None
        self._disk_encryption_id = None
        self._mode = None
        self._flavor = None
        self._storage = None
        self._backup_strategy = None
        self._enterprise_project_id = None
        self._ssl_option = None
        self.discriminator = None

        self.name = name
        self.datastore = datastore
        self.region = region
        self.availability_zone = availability_zone
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.password = password
        if disk_encryption_id is not None:
            self.disk_encryption_id = disk_encryption_id
        self.mode = mode
        self.flavor = flavor
        if storage is not None:
            self.storage = storage
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ssl_option is not None:
            self.ssl_option = ssl_option

    @property
    def name(self):
        """Gets the name of this CreateInstanceRequestBody.

        实例名称。用于表示实例的名称，用于表示实例的名称，同一租户下，同类型的实例名唯一。 取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。

        :return: The name of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstanceRequestBody.

        实例名称。用于表示实例的名称，用于表示实例的名称，同一租户下，同类型的实例名唯一。 取值范围：长度为4~64位，必须以字母开头（A~Z或a~z），区分大小写，可以包含字母、数字（0~9）、中划线（-）或者下划线（_），不能包含其他特殊字符。

        :param name: The name of this CreateInstanceRequestBody.
        :type: str
        """
        self._name = name

    @property
    def datastore(self):
        """Gets the datastore of this CreateInstanceRequestBody.


        :return: The datastore of this CreateInstanceRequestBody.
        :rtype: CreateInstanceDatastoreOption
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this CreateInstanceRequestBody.


        :param datastore: The datastore of this CreateInstanceRequestBody.
        :type: CreateInstanceDatastoreOption
        """
        self._datastore = datastore

    @property
    def region(self):
        """Gets the region of this CreateInstanceRequestBody.

        区域ID。

        :return: The region of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateInstanceRequestBody.

        区域ID。

        :param region: The region of this CreateInstanceRequestBody.
        :type: str
        """
        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateInstanceRequestBody.

        可用区ID。

        :return: The availability_zone of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateInstanceRequestBody.

        可用区ID。

        :param availability_zone: The availability_zone of this CreateInstanceRequestBody.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateInstanceRequestBody.

        虚拟私有云ID。获取方法请参见《虚拟私有云API参考》中“VPC”的内容。 取值：非空，字符长度校验，严格UUID正则校验。

        :return: The vpc_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateInstanceRequestBody.

        虚拟私有云ID。获取方法请参见《虚拟私有云API参考》中“VPC”的内容。 取值：非空，字符长度校验，严格UUID正则校验。

        :param vpc_id: The vpc_id of this CreateInstanceRequestBody.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateInstanceRequestBody.

        子网ID。获取方法请参见《虚拟私有云API参考》中“子网”的内容。

        :return: The subnet_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateInstanceRequestBody.

        子网ID。获取方法请参见《虚拟私有云API参考》中“子网”的内容。

        :param subnet_id: The subnet_id of this CreateInstanceRequestBody.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateInstanceRequestBody.

        指定实例所属的安全组ID。 获取方法请参见《虚拟私有云API参考》中“安全组”的内容。

        :return: The security_group_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateInstanceRequestBody.

        指定实例所属的安全组ID。 获取方法请参见《虚拟私有云API参考》中“安全组”的内容。

        :param security_group_id: The security_group_id of this CreateInstanceRequestBody.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def password(self):
        """Gets the password of this CreateInstanceRequestBody.

        数据库密码。 取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The password of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateInstanceRequestBody.

        数据库密码。 取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。 建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param password: The password of this CreateInstanceRequestBody.
        :type: str
        """
        self._password = password

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this CreateInstanceRequestBody.

        磁盘加密时的密钥ID，严格UUID正则校验。仅支持社区版引擎。 不传该参数时，表示不进行磁盘加密。

        :return: The disk_encryption_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this CreateInstanceRequestBody.

        磁盘加密时的密钥ID，严格UUID正则校验。仅支持社区版引擎。 不传该参数时，表示不进行磁盘加密。

        :param disk_encryption_id: The disk_encryption_id of this CreateInstanceRequestBody.
        :type: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def mode(self):
        """Gets the mode of this CreateInstanceRequestBody.

        实例类型。支持集群、副本集、以及单节点。 取值   - Sharding   - ReplicaSet   - Single

        :return: The mode of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this CreateInstanceRequestBody.

        实例类型。支持集群、副本集、以及单节点。 取值   - Sharding   - ReplicaSet   - Single

        :param mode: The mode of this CreateInstanceRequestBody.
        :type: str
        """
        self._mode = mode

    @property
    def flavor(self):
        """Gets the flavor of this CreateInstanceRequestBody.

        实例规格详情。

        :return: The flavor of this CreateInstanceRequestBody.
        :rtype: list[CreateInstanceFlavorOption]
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this CreateInstanceRequestBody.

        实例规格详情。

        :param flavor: The flavor of this CreateInstanceRequestBody.
        :type: list[CreateInstanceFlavorOption]
        """
        self._flavor = flavor

    @property
    def storage(self):
        """Gets the storage of this CreateInstanceRequestBody.


        :return: The storage of this CreateInstanceRequestBody.
        :rtype: CreateInstanceStorageOption
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this CreateInstanceRequestBody.


        :param storage: The storage of this CreateInstanceRequestBody.
        :type: CreateInstanceStorageOption
        """
        self._storage = storage

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this CreateInstanceRequestBody.


        :return: The backup_strategy of this CreateInstanceRequestBody.
        :rtype: CreateInstanceBackupStrategyOption
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this CreateInstanceRequestBody.


        :param backup_strategy: The backup_strategy of this CreateInstanceRequestBody.
        :type: CreateInstanceBackupStrategyOption
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateInstanceRequestBody.

        企业项目ID。

        :return: The enterprise_project_id of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateInstanceRequestBody.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceRequestBody.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ssl_option(self):
        """Gets the ssl_option of this CreateInstanceRequestBody.

        SSL开关选项。 取值： - 取“0”，表示DDS实例默认不启用SSL连接。 - 取“1”，表示DDS实例默认启用SSL连接。 - 不传该参数时，默认启用SSL连接。

        :return: The ssl_option of this CreateInstanceRequestBody.
        :rtype: str
        """
        return self._ssl_option

    @ssl_option.setter
    def ssl_option(self, ssl_option):
        """Sets the ssl_option of this CreateInstanceRequestBody.

        SSL开关选项。 取值： - 取“0”，表示DDS实例默认不启用SSL连接。 - 取“1”，表示DDS实例默认启用SSL连接。 - 不传该参数时，默认启用SSL连接。

        :param ssl_option: The ssl_option of this CreateInstanceRequestBody.
        :type: str
        """
        self._ssl_option = ssl_option

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
