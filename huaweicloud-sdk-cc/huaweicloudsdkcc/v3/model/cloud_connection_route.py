# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudConnectionRoute:

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
        'cloud_connection_id': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'instance_id': 'str',
        'type': 'str',
        'region_id': 'str',
        'destination': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cloud_connection_id': 'cloud_connection_id',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'instance_id': 'instance_id',
        'type': 'type',
        'region_id': 'region_id',
        'destination': 'destination'
    }

    def __init__(self, id=None, cloud_connection_id=None, domain_id=None, project_id=None, instance_id=None, type=None, region_id=None, destination=None):
        """CloudConnectionRoute

        The model defined in huaweicloud sdk

        :param id: 云连接实例路由的ID。
        :type id: str
        :param cloud_connection_id: 云连接实例的ID。
        :type cloud_connection_id: str
        :param domain_id: 帐号ID。
        :type domain_id: str
        :param project_id: 网络实例的项目ID。
        :type project_id: str
        :param instance_id: 路由条目下一跳指向的网络实例的ID。
        :type instance_id: str
        :param type: 路由条目下一跳指向的网络实例的类型。 - VPC：虚拟私有云。 - VGW：虚拟网关。
        :type type: str
        :param region_id: Region的ID。
        :type region_id: str
        :param destination: 目的地址。
        :type destination: str
        """
        
        

        self._id = None
        self._cloud_connection_id = None
        self._domain_id = None
        self._project_id = None
        self._instance_id = None
        self._type = None
        self._region_id = None
        self._destination = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if instance_id is not None:
            self.instance_id = instance_id
        if type is not None:
            self.type = type
        if region_id is not None:
            self.region_id = region_id
        if destination is not None:
            self.destination = destination

    @property
    def id(self):
        """Gets the id of this CloudConnectionRoute.

        云连接实例路由的ID。

        :return: The id of this CloudConnectionRoute.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudConnectionRoute.

        云连接实例路由的ID。

        :param id: The id of this CloudConnectionRoute.
        :type id: str
        """
        self._id = id

    @property
    def cloud_connection_id(self):
        """Gets the cloud_connection_id of this CloudConnectionRoute.

        云连接实例的ID。

        :return: The cloud_connection_id of this CloudConnectionRoute.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        """Sets the cloud_connection_id of this CloudConnectionRoute.

        云连接实例的ID。

        :param cloud_connection_id: The cloud_connection_id of this CloudConnectionRoute.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def domain_id(self):
        """Gets the domain_id of this CloudConnectionRoute.

        帐号ID。

        :return: The domain_id of this CloudConnectionRoute.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CloudConnectionRoute.

        帐号ID。

        :param domain_id: The domain_id of this CloudConnectionRoute.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        """Gets the project_id of this CloudConnectionRoute.

        网络实例的项目ID。

        :return: The project_id of this CloudConnectionRoute.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CloudConnectionRoute.

        网络实例的项目ID。

        :param project_id: The project_id of this CloudConnectionRoute.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_id(self):
        """Gets the instance_id of this CloudConnectionRoute.

        路由条目下一跳指向的网络实例的ID。

        :return: The instance_id of this CloudConnectionRoute.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CloudConnectionRoute.

        路由条目下一跳指向的网络实例的ID。

        :param instance_id: The instance_id of this CloudConnectionRoute.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        """Gets the type of this CloudConnectionRoute.

        路由条目下一跳指向的网络实例的类型。 - VPC：虚拟私有云。 - VGW：虚拟网关。

        :return: The type of this CloudConnectionRoute.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudConnectionRoute.

        路由条目下一跳指向的网络实例的类型。 - VPC：虚拟私有云。 - VGW：虚拟网关。

        :param type: The type of this CloudConnectionRoute.
        :type type: str
        """
        self._type = type

    @property
    def region_id(self):
        """Gets the region_id of this CloudConnectionRoute.

        Region的ID。

        :return: The region_id of this CloudConnectionRoute.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CloudConnectionRoute.

        Region的ID。

        :param region_id: The region_id of this CloudConnectionRoute.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def destination(self):
        """Gets the destination of this CloudConnectionRoute.

        目的地址。

        :return: The destination of this CloudConnectionRoute.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this CloudConnectionRoute.

        目的地址。

        :param destination: The destination of this CloudConnectionRoute.
        :type destination: str
        """
        self._destination = destination

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
        if not isinstance(other, CloudConnectionRoute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
