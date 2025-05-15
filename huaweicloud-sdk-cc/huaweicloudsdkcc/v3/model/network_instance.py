# coding: utf-8

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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'cloud_connection_id': 'str',
        'instance_id': 'str',
        'instance_domain_id': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'status': 'str',
        'type': 'str',
        'cidrs': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'domain_id': 'domain_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'cloud_connection_id': 'cloud_connection_id',
        'instance_id': 'instance_id',
        'instance_domain_id': 'instance_domain_id',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'status': 'status',
        'type': 'type',
        'cidrs': 'cidrs'
    }

    def __init__(self, id=None, name=None, description=None, domain_id=None, created_at=None, updated_at=None, cloud_connection_id=None, instance_id=None, instance_domain_id=None, region_id=None, project_id=None, status=None, type=None, cidrs=None):
        r"""NetworkInstance

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param domain_id: 实例所属账号ID。
        :type domain_id: str
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param cloud_connection_id: 云连接实例ID。
        :type cloud_connection_id: str
        :param instance_id: 网络实例（VPC，VGW）的ID。
        :type instance_id: str
        :param instance_domain_id: 网络实例（VPC，VGW）所属账号ID。
        :type instance_domain_id: str
        :param region_id: RegionID。
        :type region_id: str
        :param project_id: 实例所属项目ID。
        :type project_id: str
        :param status: 网络实例的状态。 - ACTIVE：处理成功。 - PENDING：处理中。 - ERROR：处理失败。
        :type status: str
        :param type: 网络实例的类型。 - vpc：虚拟私有云。 - vgw：虚拟网关。
        :type type: str
        :param cidrs: 网络实例发布的网段路由列表。
        :type cidrs: list[str]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._domain_id = None
        self._created_at = None
        self._updated_at = None
        self._cloud_connection_id = None
        self._instance_id = None
        self._instance_domain_id = None
        self._region_id = None
        self._project_id = None
        self._status = None
        self._type = None
        self._cidrs = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.domain_id = domain_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.cloud_connection_id = cloud_connection_id
        self.instance_id = instance_id
        if instance_domain_id is not None:
            self.instance_domain_id = instance_domain_id
        self.region_id = region_id
        self.project_id = project_id
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if cidrs is not None:
            self.cidrs = cidrs

    @property
    def id(self):
        r"""Gets the id of this NetworkInstance.

        实例ID。

        :return: The id of this NetworkInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NetworkInstance.

        实例ID。

        :param id: The id of this NetworkInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this NetworkInstance.

        实例名称。

        :return: The name of this NetworkInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NetworkInstance.

        实例名称。

        :param name: The name of this NetworkInstance.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this NetworkInstance.

        实例描述。不支持 <>。

        :return: The description of this NetworkInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this NetworkInstance.

        实例描述。不支持 <>。

        :param description: The description of this NetworkInstance.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        r"""Gets the domain_id of this NetworkInstance.

        实例所属账号ID。

        :return: The domain_id of this NetworkInstance.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this NetworkInstance.

        实例所属账号ID。

        :param domain_id: The domain_id of this NetworkInstance.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def created_at(self):
        r"""Gets the created_at of this NetworkInstance.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this NetworkInstance.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this NetworkInstance.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this NetworkInstance.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this NetworkInstance.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this NetworkInstance.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this NetworkInstance.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this NetworkInstance.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def cloud_connection_id(self):
        r"""Gets the cloud_connection_id of this NetworkInstance.

        云连接实例ID。

        :return: The cloud_connection_id of this NetworkInstance.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        r"""Sets the cloud_connection_id of this NetworkInstance.

        云连接实例ID。

        :param cloud_connection_id: The cloud_connection_id of this NetworkInstance.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this NetworkInstance.

        网络实例（VPC，VGW）的ID。

        :return: The instance_id of this NetworkInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this NetworkInstance.

        网络实例（VPC，VGW）的ID。

        :param instance_id: The instance_id of this NetworkInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_domain_id(self):
        r"""Gets the instance_domain_id of this NetworkInstance.

        网络实例（VPC，VGW）所属账号ID。

        :return: The instance_domain_id of this NetworkInstance.
        :rtype: str
        """
        return self._instance_domain_id

    @instance_domain_id.setter
    def instance_domain_id(self, instance_domain_id):
        r"""Sets the instance_domain_id of this NetworkInstance.

        网络实例（VPC，VGW）所属账号ID。

        :param instance_domain_id: The instance_domain_id of this NetworkInstance.
        :type instance_domain_id: str
        """
        self._instance_domain_id = instance_domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this NetworkInstance.

        RegionID。

        :return: The region_id of this NetworkInstance.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this NetworkInstance.

        RegionID。

        :param region_id: The region_id of this NetworkInstance.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        r"""Gets the project_id of this NetworkInstance.

        实例所属项目ID。

        :return: The project_id of this NetworkInstance.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this NetworkInstance.

        实例所属项目ID。

        :param project_id: The project_id of this NetworkInstance.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        r"""Gets the status of this NetworkInstance.

        网络实例的状态。 - ACTIVE：处理成功。 - PENDING：处理中。 - ERROR：处理失败。

        :return: The status of this NetworkInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NetworkInstance.

        网络实例的状态。 - ACTIVE：处理成功。 - PENDING：处理中。 - ERROR：处理失败。

        :param status: The status of this NetworkInstance.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this NetworkInstance.

        网络实例的类型。 - vpc：虚拟私有云。 - vgw：虚拟网关。

        :return: The type of this NetworkInstance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NetworkInstance.

        网络实例的类型。 - vpc：虚拟私有云。 - vgw：虚拟网关。

        :param type: The type of this NetworkInstance.
        :type type: str
        """
        self._type = type

    @property
    def cidrs(self):
        r"""Gets the cidrs of this NetworkInstance.

        网络实例发布的网段路由列表。

        :return: The cidrs of this NetworkInstance.
        :rtype: list[str]
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        r"""Sets the cidrs of this NetworkInstance.

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
