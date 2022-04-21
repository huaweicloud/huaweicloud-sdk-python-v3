# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNetworkInstance:

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
        'description': 'str',
        'type': 'str',
        'instance_id': 'str',
        'instance_domain_id': 'str',
        'project_id': 'str',
        'region_id': 'str',
        'cloud_connection_id': 'str',
        'cidrs': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'instance_id': 'instance_id',
        'instance_domain_id': 'instance_domain_id',
        'project_id': 'project_id',
        'region_id': 'region_id',
        'cloud_connection_id': 'cloud_connection_id',
        'cidrs': 'cidrs'
    }

    def __init__(self, name=None, description=None, type=None, instance_id=None, instance_domain_id=None, project_id=None, region_id=None, cloud_connection_id=None, cidrs=None):
        """CreateNetworkInstance

        The model defined in huaweicloud sdk

        :param name: 网络实例的名字。
        :type name: str
        :param description: 网络实例的描述。
        :type description: str
        :param type: 添加到云连接网络实例的类型。|- VPC：虚拟私有云。 VGW：虚拟网关。 ER：虚拟路由器。
        :type type: str
        :param instance_id: 添加到云连接网络实例的ID，VPC或者VGW的ID。
        :type instance_id: str
        :param instance_domain_id: VPC或者VGW的账户ID。
        :type instance_domain_id: str
        :param project_id: VPC或者VGW的项目ID。
        :type project_id: str
        :param region_id: VPC或者VGW的RegionID。
        :type region_id: str
        :param cloud_connection_id: 云连接实例ID。
        :type cloud_connection_id: str
        :param cidrs: VPC或者VGW发布的网段路由列表，ER场景不需要此字段。
        :type cidrs: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._instance_id = None
        self._instance_domain_id = None
        self._project_id = None
        self._region_id = None
        self._cloud_connection_id = None
        self._cidrs = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.type = type
        self.instance_id = instance_id
        if instance_domain_id is not None:
            self.instance_domain_id = instance_domain_id
        self.project_id = project_id
        self.region_id = region_id
        self.cloud_connection_id = cloud_connection_id
        self.cidrs = cidrs

    @property
    def name(self):
        """Gets the name of this CreateNetworkInstance.

        网络实例的名字。

        :return: The name of this CreateNetworkInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNetworkInstance.

        网络实例的名字。

        :param name: The name of this CreateNetworkInstance.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateNetworkInstance.

        网络实例的描述。

        :return: The description of this CreateNetworkInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateNetworkInstance.

        网络实例的描述。

        :param description: The description of this CreateNetworkInstance.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this CreateNetworkInstance.

        添加到云连接网络实例的类型。|- VPC：虚拟私有云。 VGW：虚拟网关。 ER：虚拟路由器。

        :return: The type of this CreateNetworkInstance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateNetworkInstance.

        添加到云连接网络实例的类型。|- VPC：虚拟私有云。 VGW：虚拟网关。 ER：虚拟路由器。

        :param type: The type of this CreateNetworkInstance.
        :type type: str
        """
        self._type = type

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateNetworkInstance.

        添加到云连接网络实例的ID，VPC或者VGW的ID。

        :return: The instance_id of this CreateNetworkInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateNetworkInstance.

        添加到云连接网络实例的ID，VPC或者VGW的ID。

        :param instance_id: The instance_id of this CreateNetworkInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_domain_id(self):
        """Gets the instance_domain_id of this CreateNetworkInstance.

        VPC或者VGW的账户ID。

        :return: The instance_domain_id of this CreateNetworkInstance.
        :rtype: str
        """
        return self._instance_domain_id

    @instance_domain_id.setter
    def instance_domain_id(self, instance_domain_id):
        """Sets the instance_domain_id of this CreateNetworkInstance.

        VPC或者VGW的账户ID。

        :param instance_domain_id: The instance_domain_id of this CreateNetworkInstance.
        :type instance_domain_id: str
        """
        self._instance_domain_id = instance_domain_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateNetworkInstance.

        VPC或者VGW的项目ID。

        :return: The project_id of this CreateNetworkInstance.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateNetworkInstance.

        VPC或者VGW的项目ID。

        :param project_id: The project_id of this CreateNetworkInstance.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        """Gets the region_id of this CreateNetworkInstance.

        VPC或者VGW的RegionID。

        :return: The region_id of this CreateNetworkInstance.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateNetworkInstance.

        VPC或者VGW的RegionID。

        :param region_id: The region_id of this CreateNetworkInstance.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def cloud_connection_id(self):
        """Gets the cloud_connection_id of this CreateNetworkInstance.

        云连接实例ID。

        :return: The cloud_connection_id of this CreateNetworkInstance.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        """Sets the cloud_connection_id of this CreateNetworkInstance.

        云连接实例ID。

        :param cloud_connection_id: The cloud_connection_id of this CreateNetworkInstance.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def cidrs(self):
        """Gets the cidrs of this CreateNetworkInstance.

        VPC或者VGW发布的网段路由列表，ER场景不需要此字段。

        :return: The cidrs of this CreateNetworkInstance.
        :rtype: list[str]
        """
        return self._cidrs

    @cidrs.setter
    def cidrs(self, cidrs):
        """Sets the cidrs of this CreateNetworkInstance.

        VPC或者VGW发布的网段路由列表，ER场景不需要此字段。

        :param cidrs: The cidrs of this CreateNetworkInstance.
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
        if not isinstance(other, CreateNetworkInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
