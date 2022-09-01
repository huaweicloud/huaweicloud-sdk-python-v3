# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkInstance:

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
        'name': 'str',
        'description': 'str',
        'domain_id': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'type': 'str',
        'cloud_connection_id': 'str',
        'instance_id': 'str',
        'instance_domain_id': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'cidrs': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'domain_id': 'domain_id',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'type': 'type',
        'cloud_connection_id': 'cloud_connection_id',
        'instance_id': 'instance_id',
        'instance_domain_id': 'instance_domain_id',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'cidrs': 'cidrs'
    }

    def __init__(self, id=None, name=None, description=None, domain_id=None, status=None, created_at=None, updated_at=None, type=None, cloud_connection_id=None, instance_id=None, instance_domain_id=None, region_id=None, project_id=None, cidrs=None):
        """NetworkInstance

        The model defined in huaweicloud sdk

        :param id: 网络实例的ID。
        :type id: str
        :param name: 网络实例的名字。
        :type name: str
        :param description: 网络实例的描述。
        :type description: str
        :param domain_id: 帐号ID。
        :type domain_id: str
        :param status: 网络实例的状态。 - ACTIVE：处理成功。 - PENDING：处理中。 - ERROR：处理失败。
        :type status: str
        :param created_at: 网络实例的创建时间。 UTC时间格式，yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 网络实例的更新时间。 UTC时间格式，yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        :param type: 网络实例的类型。 - VPC：虚拟私有云。 - VGW：虚拟网关。
        :type type: str
        :param cloud_connection_id: 云连接实例ID。
        :type cloud_connection_id: str
        :param instance_id: 网络实例的ID。
        :type instance_id: str
        :param instance_domain_id: 网络实例所属账户ID。
        :type instance_domain_id: str
        :param region_id: 网络实例所在Region的ID。
        :type region_id: str
        :param project_id: 网络实例所在租户的项目ID。
        :type project_id: str
        :param cidrs: 网络实例发布的网段路由列表。
        :type cidrs: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._domain_id = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._type = None
        self._cloud_connection_id = None
        self._instance_id = None
        self._instance_domain_id = None
        self._region_id = None
        self._project_id = None
        self._cidrs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if domain_id is not None:
            self.domain_id = domain_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if type is not None:
            self.type = type
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_domain_id is not None:
            self.instance_domain_id = instance_domain_id
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if cidrs is not None:
            self.cidrs = cidrs

    @property
    def id(self):
        """Gets the id of this NetworkInstance.

        网络实例的ID。

        :return: The id of this NetworkInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkInstance.

        网络实例的ID。

        :param id: The id of this NetworkInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NetworkInstance.

        网络实例的名字。

        :return: The name of this NetworkInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetworkInstance.

        网络实例的名字。

        :param name: The name of this NetworkInstance.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this NetworkInstance.

        网络实例的描述。

        :return: The description of this NetworkInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NetworkInstance.

        网络实例的描述。

        :param description: The description of this NetworkInstance.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        """Gets the domain_id of this NetworkInstance.

        帐号ID。

        :return: The domain_id of this NetworkInstance.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this NetworkInstance.

        帐号ID。

        :param domain_id: The domain_id of this NetworkInstance.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def status(self):
        """Gets the status of this NetworkInstance.

        网络实例的状态。 - ACTIVE：处理成功。 - PENDING：处理中。 - ERROR：处理失败。

        :return: The status of this NetworkInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NetworkInstance.

        网络实例的状态。 - ACTIVE：处理成功。 - PENDING：处理中。 - ERROR：处理失败。

        :param status: The status of this NetworkInstance.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this NetworkInstance.

        网络实例的创建时间。 UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this NetworkInstance.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NetworkInstance.

        网络实例的创建时间。 UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this NetworkInstance.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NetworkInstance.

        网络实例的更新时间。 UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this NetworkInstance.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NetworkInstance.

        网络实例的更新时间。 UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this NetworkInstance.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def type(self):
        """Gets the type of this NetworkInstance.

        网络实例的类型。 - VPC：虚拟私有云。 - VGW：虚拟网关。

        :return: The type of this NetworkInstance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NetworkInstance.

        网络实例的类型。 - VPC：虚拟私有云。 - VGW：虚拟网关。

        :param type: The type of this NetworkInstance.
        :type type: str
        """
        self._type = type

    @property
    def cloud_connection_id(self):
        """Gets the cloud_connection_id of this NetworkInstance.

        云连接实例ID。

        :return: The cloud_connection_id of this NetworkInstance.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        """Sets the cloud_connection_id of this NetworkInstance.

        云连接实例ID。

        :param cloud_connection_id: The cloud_connection_id of this NetworkInstance.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def instance_id(self):
        """Gets the instance_id of this NetworkInstance.

        网络实例的ID。

        :return: The instance_id of this NetworkInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this NetworkInstance.

        网络实例的ID。

        :param instance_id: The instance_id of this NetworkInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_domain_id(self):
        """Gets the instance_domain_id of this NetworkInstance.

        网络实例所属账户ID。

        :return: The instance_domain_id of this NetworkInstance.
        :rtype: str
        """
        return self._instance_domain_id

    @instance_domain_id.setter
    def instance_domain_id(self, instance_domain_id):
        """Sets the instance_domain_id of this NetworkInstance.

        网络实例所属账户ID。

        :param instance_domain_id: The instance_domain_id of this NetworkInstance.
        :type instance_domain_id: str
        """
        self._instance_domain_id = instance_domain_id

    @property
    def region_id(self):
        """Gets the region_id of this NetworkInstance.

        网络实例所在Region的ID。

        :return: The region_id of this NetworkInstance.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this NetworkInstance.

        网络实例所在Region的ID。

        :param region_id: The region_id of this NetworkInstance.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        """Gets the project_id of this NetworkInstance.

        网络实例所在租户的项目ID。

        :return: The project_id of this NetworkInstance.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NetworkInstance.

        网络实例所在租户的项目ID。

        :param project_id: The project_id of this NetworkInstance.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def cidrs(self):
        """Gets the cidrs of this NetworkInstance.

        网络实例发布的网段路由列表。

        :return: The cidrs of this NetworkInstance.
        :rtype: list[str]
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        """Sets the cidrs of this NetworkInstance.

        网络实例发布的网段路由列表。

        :param cidrs: The cidrs of this NetworkInstance.
        :type cidrs: list[str]
        """
        self._cidrs = cidrs

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
        if not isinstance(other, NetworkInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
