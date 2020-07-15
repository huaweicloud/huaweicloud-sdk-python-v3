# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateInstanceResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'datastore': 'CreateInstanceDatastoreResult',
        'name': 'str',
        'created': 'str',
        'status': 'str',
        'region': 'str',
        'availability_zone': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'disk_encryption_id': 'str',
        'mode': 'str',
        'flavor': 'list[CreateInstanceFlavorResult]',
        'storage': 'CreateInstanceStorageResult',
        'backup_strategy': 'CreateInstanceBackupStrategyResult',
        'enterprise_project_id': 'str',
        'ssl_option': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'datastore': 'datastore',
        'name': 'name',
        'created': 'created',
        'status': 'status',
        'region': 'region',
        'availability_zone': 'availability_zone',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'disk_encryption_id': 'disk_encryption_id',
        'mode': 'mode',
        'flavor': 'flavor',
        'storage': 'storage',
        'backup_strategy': 'backup_strategy',
        'enterprise_project_id': 'enterprise_project_id',
        'ssl_option': 'ssl_option',
        'job_id': 'job_id'
    }

    def __init__(self, id=None, datastore=None, name=None, created=None, status=None, region=None, availability_zone=None, vpc_id=None, subnet_id=None, security_group_id=None, disk_encryption_id=None, mode=None, flavor=None, storage=None, backup_strategy=None, enterprise_project_id=None, ssl_option=None, job_id=None):
        """CreateInstanceResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._id = None
        self._datastore = None
        self._name = None
        self._created = None
        self._status = None
        self._region = None
        self._availability_zone = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._disk_encryption_id = None
        self._mode = None
        self._flavor = None
        self._storage = None
        self._backup_strategy = None
        self._enterprise_project_id = None
        self._ssl_option = None
        self._job_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if datastore is not None:
            self.datastore = datastore
        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if status is not None:
            self.status = status
        if region is not None:
            self.region = region
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if disk_encryption_id is not None:
            self.disk_encryption_id = disk_encryption_id
        if mode is not None:
            self.mode = mode
        if flavor is not None:
            self.flavor = flavor
        if storage is not None:
            self.storage = storage
        if backup_strategy is not None:
            self.backup_strategy = backup_strategy
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ssl_option is not None:
            self.ssl_option = ssl_option
        if job_id is not None:
            self.job_id = job_id

    @property
    def id(self):
        """Gets the id of this CreateInstanceResponse.

        实例ID。

        :return: The id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateInstanceResponse.

        实例ID。

        :param id: The id of this CreateInstanceResponse.
        :type: str
        """
        self._id = id

    @property
    def datastore(self):
        """Gets the datastore of this CreateInstanceResponse.


        :return: The datastore of this CreateInstanceResponse.
        :rtype: CreateInstanceDatastoreResult
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this CreateInstanceResponse.


        :param datastore: The datastore of this CreateInstanceResponse.
        :type: CreateInstanceDatastoreResult
        """
        self._datastore = datastore

    @property
    def name(self):
        """Gets the name of this CreateInstanceResponse.

        实例名称，与请求参数相同。

        :return: The name of this CreateInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstanceResponse.

        实例名称，与请求参数相同。

        :param name: The name of this CreateInstanceResponse.
        :type: str
        """
        self._name = name

    @property
    def created(self):
        """Gets the created of this CreateInstanceResponse.

        创建时间为本地时间，格式为“yyyy-mm-dd hh:mm:ss”。

        :return: The created of this CreateInstanceResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CreateInstanceResponse.

        创建时间为本地时间，格式为“yyyy-mm-dd hh:mm:ss”。

        :param created: The created of this CreateInstanceResponse.
        :type: str
        """
        self._created = created

    @property
    def status(self):
        """Gets the status of this CreateInstanceResponse.

        实例状态，取值为“creating”。

        :return: The status of this CreateInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateInstanceResponse.

        实例状态，取值为“creating”。

        :param status: The status of this CreateInstanceResponse.
        :type: str
        """
        self._status = status

    @property
    def region(self):
        """Gets the region of this CreateInstanceResponse.

        区域ID，与请求参数相同。

        :return: The region of this CreateInstanceResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateInstanceResponse.

        区域ID，与请求参数相同。

        :param region: The region of this CreateInstanceResponse.
        :type: str
        """
        self._region = region

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateInstanceResponse.

        可用区ID，与请求参数相同。

        :return: The availability_zone of this CreateInstanceResponse.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateInstanceResponse.

        可用区ID，与请求参数相同。

        :param availability_zone: The availability_zone of this CreateInstanceResponse.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def vpc_id(self):
        """Gets the vpc_id of this CreateInstanceResponse.

        虚拟私有云ID，与请求参数相同。

        :return: The vpc_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this CreateInstanceResponse.

        虚拟私有云ID，与请求参数相同。

        :param vpc_id: The vpc_id of this CreateInstanceResponse.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateInstanceResponse.

        子网ID，与请求参数相同。

        :return: The subnet_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateInstanceResponse.

        子网ID，与请求参数相同。

        :param subnet_id: The subnet_id of this CreateInstanceResponse.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this CreateInstanceResponse.

        实例所属的安全组ID，与请求参数相同。

        :return: The security_group_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this CreateInstanceResponse.

        实例所属的安全组ID，与请求参数相同。

        :param security_group_id: The security_group_id of this CreateInstanceResponse.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def disk_encryption_id(self):
        """Gets the disk_encryption_id of this CreateInstanceResponse.

        磁盘加密的密钥ID，与请求参数相同。

        :return: The disk_encryption_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._disk_encryption_id

    @disk_encryption_id.setter
    def disk_encryption_id(self, disk_encryption_id):
        """Sets the disk_encryption_id of this CreateInstanceResponse.

        磁盘加密的密钥ID，与请求参数相同。

        :param disk_encryption_id: The disk_encryption_id of this CreateInstanceResponse.
        :type: str
        """
        self._disk_encryption_id = disk_encryption_id

    @property
    def mode(self):
        """Gets the mode of this CreateInstanceResponse.

        实例类型，与请求参数相同。

        :return: The mode of this CreateInstanceResponse.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this CreateInstanceResponse.

        实例类型，与请求参数相同。

        :param mode: The mode of this CreateInstanceResponse.
        :type: str
        """
        self._mode = mode

    @property
    def flavor(self):
        """Gets the flavor of this CreateInstanceResponse.

        实例规格详情，与请求参数相同。

        :return: The flavor of this CreateInstanceResponse.
        :rtype: list[CreateInstanceFlavorResult]
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this CreateInstanceResponse.

        实例规格详情，与请求参数相同。

        :param flavor: The flavor of this CreateInstanceResponse.
        :type: list[CreateInstanceFlavorResult]
        """
        self._flavor = flavor

    @property
    def storage(self):
        """Gets the storage of this CreateInstanceResponse.


        :return: The storage of this CreateInstanceResponse.
        :rtype: CreateInstanceStorageResult
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this CreateInstanceResponse.


        :param storage: The storage of this CreateInstanceResponse.
        :type: CreateInstanceStorageResult
        """
        self._storage = storage

    @property
    def backup_strategy(self):
        """Gets the backup_strategy of this CreateInstanceResponse.


        :return: The backup_strategy of this CreateInstanceResponse.
        :rtype: CreateInstanceBackupStrategyResult
        """
        return self._backup_strategy

    @backup_strategy.setter
    def backup_strategy(self, backup_strategy):
        """Sets the backup_strategy of this CreateInstanceResponse.


        :param backup_strategy: The backup_strategy of this CreateInstanceResponse.
        :type: CreateInstanceBackupStrategyResult
        """
        self._backup_strategy = backup_strategy

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateInstanceResponse.

        企业项目ID。取值为“0”，表示为default企业项目。

        :return: The enterprise_project_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateInstanceResponse.

        企业项目ID。取值为“0”，表示为default企业项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceResponse.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ssl_option(self):
        """Gets the ssl_option of this CreateInstanceResponse.

        SSL开关选项，与请求参数相同。

        :return: The ssl_option of this CreateInstanceResponse.
        :rtype: str
        """
        return self._ssl_option

    @ssl_option.setter
    def ssl_option(self, ssl_option):
        """Sets the ssl_option of this CreateInstanceResponse.

        SSL开关选项，与请求参数相同。

        :param ssl_option: The ssl_option of this CreateInstanceResponse.
        :type: str
        """
        self._ssl_option = ssl_option

    @property
    def job_id(self):
        """Gets the job_id of this CreateInstanceResponse.

        创建实例的工作流ID。

        :return: The job_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateInstanceResponse.

        创建实例的工作流ID。

        :param job_id: The job_id of this CreateInstanceResponse.
        :type: str
        """
        self._job_id = job_id

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
        if not isinstance(other, CreateInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
