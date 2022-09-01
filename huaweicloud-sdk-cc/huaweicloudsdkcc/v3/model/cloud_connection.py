# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudConnection:

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
        'enterprise_project_id': 'str',
        'status': 'str',
        'admin_state_up': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'used_scene': 'str',
        'network_instance_number': 'int',
        'bandwidth_package_number': 'int',
        'inter_region_bandwidth_number': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'domain_id': 'domain_id',
        'enterprise_project_id': 'enterprise_project_id',
        'status': 'status',
        'admin_state_up': 'admin_state_up',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'used_scene': 'used_scene',
        'network_instance_number': 'network_instance_number',
        'bandwidth_package_number': 'bandwidth_package_number',
        'inter_region_bandwidth_number': 'inter_region_bandwidth_number'
    }

    def __init__(self, id=None, name=None, description=None, domain_id=None, enterprise_project_id=None, status=None, admin_state_up=None, created_at=None, updated_at=None, used_scene=None, network_instance_number=None, bandwidth_package_number=None, inter_region_bandwidth_number=None):
        """CloudConnection

        The model defined in huaweicloud sdk

        :param id: 云连接实例的ID。
        :type id: str
        :param name: 云连接实例的名字。
        :type name: str
        :param description: 云连接实例的描述。
        :type description: str
        :param domain_id: 帐号ID。
        :type domain_id: str
        :param enterprise_project_id: 云连接实例的企业项目ID。
        :type enterprise_project_id: str
        :param status: 云连接实例的状态。ACTIVE：表示状态可用。
        :type status: str
        :param admin_state_up: 云连接实例的管理状态。
        :type admin_state_up: bool
        :param created_at: 云连接实例的创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss
        :type created_at: datetime
        :param updated_at: 云连接实例的更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss
        :type updated_at: datetime
        :param used_scene: 云连接使用场景。 - VPC：虚拟私有云。
        :type used_scene: str
        :param network_instance_number: 云连接实例关联网络实例的个数。
        :type network_instance_number: int
        :param bandwidth_package_number: 云连接实例关联带宽包的个数。
        :type bandwidth_package_number: int
        :param inter_region_bandwidth_number: 云连接实例关联域间带宽的个数。
        :type inter_region_bandwidth_number: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._domain_id = None
        self._enterprise_project_id = None
        self._status = None
        self._admin_state_up = None
        self._created_at = None
        self._updated_at = None
        self._used_scene = None
        self._network_instance_number = None
        self._bandwidth_package_number = None
        self._inter_region_bandwidth_number = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if domain_id is not None:
            self.domain_id = domain_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if status is not None:
            self.status = status
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if used_scene is not None:
            self.used_scene = used_scene
        if network_instance_number is not None:
            self.network_instance_number = network_instance_number
        if bandwidth_package_number is not None:
            self.bandwidth_package_number = bandwidth_package_number
        if inter_region_bandwidth_number is not None:
            self.inter_region_bandwidth_number = inter_region_bandwidth_number

    @property
    def id(self):
        """Gets the id of this CloudConnection.

        云连接实例的ID。

        :return: The id of this CloudConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudConnection.

        云连接实例的ID。

        :param id: The id of this CloudConnection.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CloudConnection.

        云连接实例的名字。

        :return: The name of this CloudConnection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudConnection.

        云连接实例的名字。

        :param name: The name of this CloudConnection.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CloudConnection.

        云连接实例的描述。

        :return: The description of this CloudConnection.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CloudConnection.

        云连接实例的描述。

        :param description: The description of this CloudConnection.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        """Gets the domain_id of this CloudConnection.

        帐号ID。

        :return: The domain_id of this CloudConnection.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CloudConnection.

        帐号ID。

        :param domain_id: The domain_id of this CloudConnection.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CloudConnection.

        云连接实例的企业项目ID。

        :return: The enterprise_project_id of this CloudConnection.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CloudConnection.

        云连接实例的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CloudConnection.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def status(self):
        """Gets the status of this CloudConnection.

        云连接实例的状态。ACTIVE：表示状态可用。

        :return: The status of this CloudConnection.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CloudConnection.

        云连接实例的状态。ACTIVE：表示状态可用。

        :param status: The status of this CloudConnection.
        :type status: str
        """
        self._status = status

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CloudConnection.

        云连接实例的管理状态。

        :return: The admin_state_up of this CloudConnection.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CloudConnection.

        云连接实例的管理状态。

        :param admin_state_up: The admin_state_up of this CloudConnection.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def created_at(self):
        """Gets the created_at of this CloudConnection.

        云连接实例的创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this CloudConnection.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CloudConnection.

        云连接实例的创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this CloudConnection.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CloudConnection.

        云连接实例的更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this CloudConnection.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CloudConnection.

        云连接实例的更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this CloudConnection.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def used_scene(self):
        """Gets the used_scene of this CloudConnection.

        云连接使用场景。 - VPC：虚拟私有云。

        :return: The used_scene of this CloudConnection.
        :rtype: str
        """
        return self._used_scene

    @used_scene.setter
    def used_scene(self, used_scene):
        """Sets the used_scene of this CloudConnection.

        云连接使用场景。 - VPC：虚拟私有云。

        :param used_scene: The used_scene of this CloudConnection.
        :type used_scene: str
        """
        self._used_scene = used_scene

    @property
    def network_instance_number(self):
        """Gets the network_instance_number of this CloudConnection.

        云连接实例关联网络实例的个数。

        :return: The network_instance_number of this CloudConnection.
        :rtype: int
        """
        return self._network_instance_number

    @network_instance_number.setter
    def network_instance_number(self, network_instance_number):
        """Sets the network_instance_number of this CloudConnection.

        云连接实例关联网络实例的个数。

        :param network_instance_number: The network_instance_number of this CloudConnection.
        :type network_instance_number: int
        """
        self._network_instance_number = network_instance_number

    @property
    def bandwidth_package_number(self):
        """Gets the bandwidth_package_number of this CloudConnection.

        云连接实例关联带宽包的个数。

        :return: The bandwidth_package_number of this CloudConnection.
        :rtype: int
        """
        return self._bandwidth_package_number

    @bandwidth_package_number.setter
    def bandwidth_package_number(self, bandwidth_package_number):
        """Sets the bandwidth_package_number of this CloudConnection.

        云连接实例关联带宽包的个数。

        :param bandwidth_package_number: The bandwidth_package_number of this CloudConnection.
        :type bandwidth_package_number: int
        """
        self._bandwidth_package_number = bandwidth_package_number

    @property
    def inter_region_bandwidth_number(self):
        """Gets the inter_region_bandwidth_number of this CloudConnection.

        云连接实例关联域间带宽的个数。

        :return: The inter_region_bandwidth_number of this CloudConnection.
        :rtype: int
        """
        return self._inter_region_bandwidth_number

    @inter_region_bandwidth_number.setter
    def inter_region_bandwidth_number(self, inter_region_bandwidth_number):
        """Sets the inter_region_bandwidth_number of this CloudConnection.

        云连接实例关联域间带宽的个数。

        :param inter_region_bandwidth_number: The inter_region_bandwidth_number of this CloudConnection.
        :type inter_region_bandwidth_number: int
        """
        self._inter_region_bandwidth_number = inter_region_bandwidth_number

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
        if not isinstance(other, CloudConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
