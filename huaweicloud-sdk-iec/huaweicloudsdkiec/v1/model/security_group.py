# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'security_group_rules': 'list[SecurityGroupRule]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'security_group_rules': 'security_group_rules'
    }

    def __init__(self, id=None, name=None, description=None, security_group_rules=None):
        """SecurityGroup

        The model defined in huaweicloud sdk

        :param id: 安全组的ID。UUID
        :type id: str
        :param name: 安全组的名称。
        :type name: str
        :param description: 安全组的描述。
        :type description: str
        :param security_group_rules: 安全组规则列表。
        :type security_group_rules: list[:class:`huaweicloudsdkiec.v1.SecurityGroupRule`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._security_group_rules = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if security_group_rules is not None:
            self.security_group_rules = security_group_rules

    @property
    def id(self):
        """Gets the id of this SecurityGroup.

        安全组的ID。UUID

        :return: The id of this SecurityGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SecurityGroup.

        安全组的ID。UUID

        :param id: The id of this SecurityGroup.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SecurityGroup.

        安全组的名称。

        :return: The name of this SecurityGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SecurityGroup.

        安全组的名称。

        :param name: The name of this SecurityGroup.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this SecurityGroup.

        安全组的描述。

        :return: The description of this SecurityGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SecurityGroup.

        安全组的描述。

        :param description: The description of this SecurityGroup.
        :type description: str
        """
        self._description = description

    @property
    def security_group_rules(self):
        """Gets the security_group_rules of this SecurityGroup.

        安全组规则列表。

        :return: The security_group_rules of this SecurityGroup.
        :rtype: list[:class:`huaweicloudsdkiec.v1.SecurityGroupRule`]
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        """Sets the security_group_rules of this SecurityGroup.

        安全组规则列表。

        :param security_group_rules: The security_group_rules of this SecurityGroup.
        :type security_group_rules: list[:class:`huaweicloudsdkiec.v1.SecurityGroupRule`]
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
        if not isinstance(other, SecurityGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
