# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Permission:

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
        'instance_id': 'str',
        'project_id': 'str',
        'region_id': 'str',
        'created_at': 'datetime',
        'domain_id': 'str',
        'cloud_connection_id': 'str',
        'status': 'str',
        'instance_type': 'str',
        'instance_domain_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'instance_id': 'instance_id',
        'project_id': 'project_id',
        'region_id': 'region_id',
        'created_at': 'created_at',
        'domain_id': 'domain_id',
        'cloud_connection_id': 'cloud_connection_id',
        'status': 'status',
        'instance_type': 'instance_type',
        'instance_domain_id': 'instance_domain_id'
    }

    def __init__(self, id=None, name=None, description=None, instance_id=None, project_id=None, region_id=None, created_at=None, domain_id=None, cloud_connection_id=None, status=None, instance_type=None, instance_domain_id=None):
        """Permission

        The model defined in huaweicloud sdk

        :param id: 资源ID标识符。
        :type id: str
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
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param domain_id: 实例所属帐号ID。
        :type domain_id: str
        :param cloud_connection_id: 资源ID标识符。
        :type cloud_connection_id: str
        :param status: 授权的状态。
        :type status: str
        :param instance_type: 授权实例的类型。
        :type instance_type: str
        :param instance_domain_id: 被授权网络实例所属的账户ID。
        :type instance_domain_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._instance_id = None
        self._project_id = None
        self._region_id = None
        self._created_at = None
        self._domain_id = None
        self._cloud_connection_id = None
        self._status = None
        self._instance_type = None
        self._instance_domain_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.instance_id = instance_id
        self.project_id = project_id
        self.region_id = region_id
        self.created_at = created_at
        self.domain_id = domain_id
        self.cloud_connection_id = cloud_connection_id
        if status is not None:
            self.status = status
        if instance_type is not None:
            self.instance_type = instance_type
        if instance_domain_id is not None:
            self.instance_domain_id = instance_domain_id

    @property
    def id(self):
        """Gets the id of this Permission.

        资源ID标识符。

        :return: The id of this Permission.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Permission.

        资源ID标识符。

        :param id: The id of this Permission.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Permission.

        实例名字。

        :return: The name of this Permission.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Permission.

        实例名字。

        :param name: The name of this Permission.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Permission.

        实例描述。不支持 <>。

        :return: The description of this Permission.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Permission.

        实例描述。不支持 <>。

        :param description: The description of this Permission.
        :type description: str
        """
        self._description = description

    @property
    def instance_id(self):
        """Gets the instance_id of this Permission.

        资源ID标识符。

        :return: The instance_id of this Permission.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Permission.

        资源ID标识符。

        :param instance_id: The instance_id of this Permission.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def project_id(self):
        """Gets the project_id of this Permission.

        实例所属项目ID。

        :return: The project_id of this Permission.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Permission.

        实例所属项目ID。

        :param project_id: The project_id of this Permission.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        """Gets the region_id of this Permission.

        RegionID。

        :return: The region_id of this Permission.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this Permission.

        RegionID。

        :param region_id: The region_id of this Permission.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def created_at(self):
        """Gets the created_at of this Permission.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this Permission.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Permission.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this Permission.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def domain_id(self):
        """Gets the domain_id of this Permission.

        实例所属帐号ID。

        :return: The domain_id of this Permission.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Permission.

        实例所属帐号ID。

        :param domain_id: The domain_id of this Permission.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def cloud_connection_id(self):
        """Gets the cloud_connection_id of this Permission.

        资源ID标识符。

        :return: The cloud_connection_id of this Permission.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        """Sets the cloud_connection_id of this Permission.

        资源ID标识符。

        :param cloud_connection_id: The cloud_connection_id of this Permission.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def status(self):
        """Gets the status of this Permission.

        授权的状态。

        :return: The status of this Permission.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Permission.

        授权的状态。

        :param status: The status of this Permission.
        :type status: str
        """
        self._status = status

    @property
    def instance_type(self):
        """Gets the instance_type of this Permission.

        授权实例的类型。

        :return: The instance_type of this Permission.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this Permission.

        授权实例的类型。

        :param instance_type: The instance_type of this Permission.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_domain_id(self):
        """Gets the instance_domain_id of this Permission.

        被授权网络实例所属的账户ID。

        :return: The instance_domain_id of this Permission.
        :rtype: str
        """
        return self._instance_domain_id

    @instance_domain_id.setter
    def instance_domain_id(self, instance_domain_id):
        """Sets the instance_domain_id of this Permission.

        被授权网络实例所属的账户ID。

        :param instance_domain_id: The instance_domain_id of this Permission.
        :type instance_domain_id: str
        """
        self._instance_domain_id = instance_domain_id

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
        if not isinstance(other, Permission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
