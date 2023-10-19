# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAuthorisation:

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
        'instance_id': 'str',
        'project_id': 'str',
        'region_id': 'str',
        'cloud_connection_id': 'str',
        'instance_type': 'str',
        'cloud_connection_domain_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'instance_id': 'instance_id',
        'project_id': 'project_id',
        'region_id': 'region_id',
        'cloud_connection_id': 'cloud_connection_id',
        'instance_type': 'instance_type',
        'cloud_connection_domain_id': 'cloud_connection_domain_id'
    }

    def __init__(self, name=None, description=None, instance_id=None, project_id=None, region_id=None, cloud_connection_id=None, instance_type=None, cloud_connection_domain_id=None):
        """CreateAuthorisation

        The model defined in huaweicloud sdk

        :param name: 实例名字。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param instance_id: 资源ID标识符。
        :type instance_id: str
        :param project_id: 实例所属项目ID。
        :type project_id: str
        :param region_id: RegionID。
        :type region_id: str
        :param cloud_connection_id: 资源ID标识符。
        :type cloud_connection_id: str
        :param instance_type: 授权网络实例的类型: - vpc：虚拟私有云
        :type instance_type: str
        :param cloud_connection_domain_id: 被授权云连接实例所属的账户ID。
        :type cloud_connection_domain_id: str
        """
        
        

        self._name = None
        self._description = None
        self._instance_id = None
        self._project_id = None
        self._region_id = None
        self._cloud_connection_id = None
        self._instance_type = None
        self._cloud_connection_domain_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.instance_id = instance_id
        self.project_id = project_id
        self.region_id = region_id
        self.cloud_connection_id = cloud_connection_id
        self.instance_type = instance_type
        self.cloud_connection_domain_id = cloud_connection_domain_id

    @property
    def name(self):
        """Gets the name of this CreateAuthorisation.

        实例名字。

        :return: The name of this CreateAuthorisation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAuthorisation.

        实例名字。

        :param name: The name of this CreateAuthorisation.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateAuthorisation.

        实例描述。不支持 <>。

        :return: The description of this CreateAuthorisation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAuthorisation.

        实例描述。不支持 <>。

        :param description: The description of this CreateAuthorisation.
        :type description: str
        """
        self._description = description

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateAuthorisation.

        资源ID标识符。

        :return: The instance_id of this CreateAuthorisation.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateAuthorisation.

        资源ID标识符。

        :param instance_id: The instance_id of this CreateAuthorisation.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def project_id(self):
        """Gets the project_id of this CreateAuthorisation.

        实例所属项目ID。

        :return: The project_id of this CreateAuthorisation.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateAuthorisation.

        实例所属项目ID。

        :param project_id: The project_id of this CreateAuthorisation.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        """Gets the region_id of this CreateAuthorisation.

        RegionID。

        :return: The region_id of this CreateAuthorisation.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CreateAuthorisation.

        RegionID。

        :param region_id: The region_id of this CreateAuthorisation.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def cloud_connection_id(self):
        """Gets the cloud_connection_id of this CreateAuthorisation.

        资源ID标识符。

        :return: The cloud_connection_id of this CreateAuthorisation.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        """Sets the cloud_connection_id of this CreateAuthorisation.

        资源ID标识符。

        :param cloud_connection_id: The cloud_connection_id of this CreateAuthorisation.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def instance_type(self):
        """Gets the instance_type of this CreateAuthorisation.

        授权网络实例的类型: - vpc：虚拟私有云

        :return: The instance_type of this CreateAuthorisation.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this CreateAuthorisation.

        授权网络实例的类型: - vpc：虚拟私有云

        :param instance_type: The instance_type of this CreateAuthorisation.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def cloud_connection_domain_id(self):
        """Gets the cloud_connection_domain_id of this CreateAuthorisation.

        被授权云连接实例所属的账户ID。

        :return: The cloud_connection_domain_id of this CreateAuthorisation.
        :rtype: str
        """
        return self._cloud_connection_domain_id

    @cloud_connection_domain_id.setter
    def cloud_connection_domain_id(self, cloud_connection_domain_id):
        """Sets the cloud_connection_domain_id of this CreateAuthorisation.

        被授权云连接实例所属的账户ID。

        :param cloud_connection_domain_id: The cloud_connection_domain_id of this CreateAuthorisation.
        :type cloud_connection_domain_id: str
        """
        self._cloud_connection_domain_id = cloud_connection_domain_id

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
        if not isinstance(other, CreateAuthorisation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
