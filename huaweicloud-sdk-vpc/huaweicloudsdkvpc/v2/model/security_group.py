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
        'name': 'str',
        'description': 'str',
        'id': 'str',
        'vpc_id': 'str',
        'enterprise_project_id': 'str',
        'security_group_rules': 'list[SecurityGroupRule]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'id': 'id',
        'vpc_id': 'vpc_id',
        'enterprise_project_id': 'enterprise_project_id',
        'security_group_rules': 'security_group_rules'
    }

    def __init__(self, name=None, description=None, id=None, vpc_id=None, enterprise_project_id=None, security_group_rules=None):
        """SecurityGroup - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._id = None
        self._vpc_id = None
        self._enterprise_project_id = None
        self._security_group_rules = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.id = id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.security_group_rules = security_group_rules

    @property
    def name(self):
        """Gets the name of this SecurityGroup.

        安全组名称

        :return: The name of this SecurityGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecurityGroup.

        安全组名称

        :param name: The name of this SecurityGroup.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this SecurityGroup.

        安全组描述

        :return: The description of this SecurityGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecurityGroup.

        安全组描述

        :param description: The description of this SecurityGroup.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this SecurityGroup.

        安全组唯一标识

        :return: The id of this SecurityGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SecurityGroup.

        安全组唯一标识

        :param id: The id of this SecurityGroup.
        :type: str
        """
        self._id = id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this SecurityGroup.

        安全组所在的vpc的资源标识

        :return: The vpc_id of this SecurityGroup.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this SecurityGroup.

        安全组所在的vpc的资源标识

        :param vpc_id: The vpc_id of this SecurityGroup.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SecurityGroup.

        功能说明：企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :return: The enterprise_project_id of this SecurityGroup.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SecurityGroup.

        功能说明：企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this SecurityGroup.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def security_group_rules(self):
        """Gets the security_group_rules of this SecurityGroup.

        安全组规则

        :return: The security_group_rules of this SecurityGroup.
        :rtype: list[SecurityGroupRule]
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        """Sets the security_group_rules of this SecurityGroup.

        安全组规则

        :param security_group_rules: The security_group_rules of this SecurityGroup.
        :type: list[SecurityGroupRule]
        """
        self._security_group_rules = security_group_rules

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
