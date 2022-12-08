# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Authorisation:

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
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'domain_id': 'str',
        'instance_id': 'str',
        'instance_type': 'str',
        'region_id': 'str',
        'project_id': 'str',
        'cloud_connection_domain_id': 'str',
        'cloud_connection_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'domain_id': 'domain_id',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type',
        'region_id': 'region_id',
        'project_id': 'project_id',
        'cloud_connection_domain_id': 'cloud_connection_domain_id',
        'cloud_connection_id': 'cloud_connection_id'
    }

    def __init__(self, id=None, name=None, description=None, status=None, created_at=None, updated_at=None, domain_id=None, instance_id=None, instance_type=None, region_id=None, project_id=None, cloud_connection_domain_id=None, cloud_connection_id=None):
        """Authorisation

        The model defined in huaweicloud sdk

        :param id: 授权的ID。
        :type id: str
        :param name: 授权的名称。
        :type name: str
        :param description: 授权的描述信息。
        :type description: str
        :param status: 授权的状态。
        :type status: str
        :param created_at: 创建授权的时间。
        :type created_at: datetime
        :param updated_at: 更新授权的时间。
        :type updated_at: datetime
        :param domain_id: 授权者的账户ID。
        :type domain_id: str
        :param instance_id: 授权实例的ID。
        :type instance_id: str
        :param instance_type: 授权实例的类型。
        :type instance_type: str
        :param region_id: 授权实例所属Region。
        :type region_id: str
        :param project_id: 授权实例所属项目ID。
        :type project_id: str
        :param cloud_connection_domain_id: 被授权云连接实例所属的账户ID。
        :type cloud_connection_domain_id: str
        :param cloud_connection_id: 被授权云连接实例ID。
        :type cloud_connection_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._domain_id = None
        self._instance_id = None
        self._instance_type = None
        self._region_id = None
        self._project_id = None
        self._cloud_connection_domain_id = None
        self._cloud_connection_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if domain_id is not None:
            self.domain_id = domain_id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type
        if region_id is not None:
            self.region_id = region_id
        if project_id is not None:
            self.project_id = project_id
        if cloud_connection_domain_id is not None:
            self.cloud_connection_domain_id = cloud_connection_domain_id
        if cloud_connection_id is not None:
            self.cloud_connection_id = cloud_connection_id

    @property
    def id(self):
        """Gets the id of this Authorisation.

        授权的ID。

        :return: The id of this Authorisation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Authorisation.

        授权的ID。

        :param id: The id of this Authorisation.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Authorisation.

        授权的名称。

        :return: The name of this Authorisation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Authorisation.

        授权的名称。

        :param name: The name of this Authorisation.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Authorisation.

        授权的描述信息。

        :return: The description of this Authorisation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Authorisation.

        授权的描述信息。

        :param description: The description of this Authorisation.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this Authorisation.

        授权的状态。

        :return: The status of this Authorisation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Authorisation.

        授权的状态。

        :param status: The status of this Authorisation.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this Authorisation.

        创建授权的时间。

        :return: The created_at of this Authorisation.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Authorisation.

        创建授权的时间。

        :param created_at: The created_at of this Authorisation.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Authorisation.

        更新授权的时间。

        :return: The updated_at of this Authorisation.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Authorisation.

        更新授权的时间。

        :param updated_at: The updated_at of this Authorisation.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def domain_id(self):
        """Gets the domain_id of this Authorisation.

        授权者的账户ID。

        :return: The domain_id of this Authorisation.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Authorisation.

        授权者的账户ID。

        :param domain_id: The domain_id of this Authorisation.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def instance_id(self):
        """Gets the instance_id of this Authorisation.

        授权实例的ID。

        :return: The instance_id of this Authorisation.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Authorisation.

        授权实例的ID。

        :param instance_id: The instance_id of this Authorisation.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this Authorisation.

        授权实例的类型。

        :return: The instance_type of this Authorisation.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this Authorisation.

        授权实例的类型。

        :param instance_type: The instance_type of this Authorisation.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def region_id(self):
        """Gets the region_id of this Authorisation.

        授权实例所属Region。

        :return: The region_id of this Authorisation.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this Authorisation.

        授权实例所属Region。

        :param region_id: The region_id of this Authorisation.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        """Gets the project_id of this Authorisation.

        授权实例所属项目ID。

        :return: The project_id of this Authorisation.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Authorisation.

        授权实例所属项目ID。

        :param project_id: The project_id of this Authorisation.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def cloud_connection_domain_id(self):
        """Gets the cloud_connection_domain_id of this Authorisation.

        被授权云连接实例所属的账户ID。

        :return: The cloud_connection_domain_id of this Authorisation.
        :rtype: str
        """
        return self._cloud_connection_domain_id

    @cloud_connection_domain_id.setter
    def cloud_connection_domain_id(self, cloud_connection_domain_id):
        """Sets the cloud_connection_domain_id of this Authorisation.

        被授权云连接实例所属的账户ID。

        :param cloud_connection_domain_id: The cloud_connection_domain_id of this Authorisation.
        :type cloud_connection_domain_id: str
        """
        self._cloud_connection_domain_id = cloud_connection_domain_id

    @property
    def cloud_connection_id(self):
        """Gets the cloud_connection_id of this Authorisation.

        被授权云连接实例ID。

        :return: The cloud_connection_id of this Authorisation.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        """Sets the cloud_connection_id of this Authorisation.

        被授权云连接实例ID。

        :param cloud_connection_id: The cloud_connection_id of this Authorisation.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

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
        if not isinstance(other, Authorisation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
