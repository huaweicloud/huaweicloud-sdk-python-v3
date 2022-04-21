# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCloudConnection:

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
        'enterprise_project_id': 'str',
        'used_scene': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'used_scene': 'used_scene'
    }

    def __init__(self, name=None, description=None, enterprise_project_id=None, used_scene=None):
        """CreateCloudConnection

        The model defined in huaweicloud sdk

        :param name: 云连接实例的名字。
        :type name: str
        :param description: 云连接实例的描述。
        :type description: str
        :param enterprise_project_id: 云连接实例所属的企业项目ID。
        :type enterprise_project_id: str
        :param used_scene: 云连接使用场景。|- VPC：虚拟私有云。 ER：虚拟路由器。
        :type used_scene: str
        """
        
        

        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self._used_scene = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if used_scene is not None:
            self.used_scene = used_scene

    @property
    def name(self):
        """Gets the name of this CreateCloudConnection.

        云连接实例的名字。

        :return: The name of this CreateCloudConnection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCloudConnection.

        云连接实例的名字。

        :param name: The name of this CreateCloudConnection.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateCloudConnection.

        云连接实例的描述。

        :return: The description of this CreateCloudConnection.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCloudConnection.

        云连接实例的描述。

        :param description: The description of this CreateCloudConnection.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateCloudConnection.

        云连接实例所属的企业项目ID。

        :return: The enterprise_project_id of this CreateCloudConnection.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateCloudConnection.

        云连接实例所属的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateCloudConnection.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def used_scene(self):
        """Gets the used_scene of this CreateCloudConnection.

        云连接使用场景。|- VPC：虚拟私有云。 ER：虚拟路由器。

        :return: The used_scene of this CreateCloudConnection.
        :rtype: str
        """
        return self._used_scene

    @used_scene.setter
    def used_scene(self, used_scene):
        """Sets the used_scene of this CreateCloudConnection.

        云连接使用场景。|- VPC：虚拟私有云。 ER：虚拟路由器。

        :param used_scene: The used_scene of this CreateCloudConnection.
        :type used_scene: str
        """
        self._used_scene = used_scene

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
        if not isinstance(other, CreateCloudConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
