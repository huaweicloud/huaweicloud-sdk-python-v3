# coding: utf-8

import pprint
import re

import six





class SecurityGroup:


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
        'project_id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, description=None, project_id=None, created_at=None, updated_at=None, enterprise_project_id=None):
        """SecurityGroup - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._description = None
        self._project_id = None
        self._created_at = None
        self._updated_at = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.project_id = project_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this SecurityGroup.

        功能描述：安全组对应的唯一标识 取值范围：带“-”的标准UUID格式

        :return: The id of this SecurityGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SecurityGroup.

        功能描述：安全组对应的唯一标识 取值范围：带“-”的标准UUID格式

        :param id: The id of this SecurityGroup.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SecurityGroup.

        功能说明：安全组名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this SecurityGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecurityGroup.

        功能说明：安全组名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this SecurityGroup.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this SecurityGroup.

        功能说明：安全组的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this SecurityGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecurityGroup.

        功能说明：安全组的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this SecurityGroup.
        :type: str
        """
        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this SecurityGroup.

        功能说明：安全组所属的项目ID

        :return: The project_id of this SecurityGroup.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SecurityGroup.

        功能说明：安全组所属的项目ID

        :param project_id: The project_id of this SecurityGroup.
        :type: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        """Gets the created_at of this SecurityGroup.

        功能说明：安全组创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :return: The created_at of this SecurityGroup.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SecurityGroup.

        功能说明：安全组创建时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :param created_at: The created_at of this SecurityGroup.
        :type: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SecurityGroup.

        功能说明：安全组更新时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :return: The updated_at of this SecurityGroup.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SecurityGroup.

        功能说明：安全组更新时间 取值范围：UTC时间格式：yyyy-MM-ddTHH:mm:ss

        :param updated_at: The updated_at of this SecurityGroup.
        :type: datetime
        """
        self._updated_at = updated_at

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SecurityGroup.

        功能说明：安全组所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :return: The enterprise_project_id of this SecurityGroup.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SecurityGroup.

        功能说明：安全组所属的企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this SecurityGroup.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, SecurityGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
