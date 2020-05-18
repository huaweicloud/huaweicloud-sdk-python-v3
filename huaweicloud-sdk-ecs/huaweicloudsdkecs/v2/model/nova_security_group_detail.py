# coding: utf-8

import pprint
import re

import six


class NovaSecurityGroupDetail(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'project_id': 'str',
        'rules': 'list[NovaSecurityGroupCommonRule]'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'rules': 'rules'
    }

    def __init__(self, description=None, id=None, name=None, project_id=None, rules=None):  # noqa: E501
        """NovaSecurityGroupDetail - a model defined in huaweicloud sdk"""

        self._description = None
        self._id = None
        self._name = None
        self._project_id = None
        self._rules = None
        self.discriminator = None

        self.description = description
        self.id = id
        self.name = name
        self.project_id = project_id
        self.rules = rules

    @property
    def description(self):
        """Gets the description of this NovaSecurityGroupDetail.

        安全组信息，长度0-255

        :return: The description of this NovaSecurityGroupDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NovaSecurityGroupDetail.

        安全组信息，长度0-255

        :param description: The description of this NovaSecurityGroupDetail.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this NovaSecurityGroupDetail.

        安全组ID，UUID格式

        :return: The id of this NovaSecurityGroupDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaSecurityGroupDetail.

        安全组ID，UUID格式

        :param id: The id of this NovaSecurityGroupDetail.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NovaSecurityGroupDetail.

        安全组名字，长度0-255

        :return: The name of this NovaSecurityGroupDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaSecurityGroupDetail.

        安全组名字，长度0-255

        :param name: The name of this NovaSecurityGroupDetail.
        :type: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this NovaSecurityGroupDetail.

        项目ID

        :return: The project_id of this NovaSecurityGroupDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NovaSecurityGroupDetail.

        项目ID

        :param project_id: The project_id of this NovaSecurityGroupDetail.
        :type: str
        """
        self._project_id = project_id

    @property
    def rules(self):
        """Gets the rules of this NovaSecurityGroupDetail.

        安全组规则列表

        :return: The rules of this NovaSecurityGroupDetail.
        :rtype: list[NovaSecurityGroupCommonRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this NovaSecurityGroupDetail.

        安全组规则列表

        :param rules: The rules of this NovaSecurityGroupDetail.
        :type: list[NovaSecurityGroupCommonRule]
        """
        self._rules = rules

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
        if not isinstance(other, NovaSecurityGroupDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
