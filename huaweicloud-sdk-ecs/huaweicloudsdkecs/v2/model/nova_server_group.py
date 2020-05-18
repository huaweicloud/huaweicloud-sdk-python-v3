# coding: utf-8

import pprint
import re

import six


class NovaServerGroup(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'members': 'list[str]',
        'metadata': 'dict(str, str)',
        'policies': 'list[str]',
        'project_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'members': 'members',
        'metadata': 'metadata',
        'policies': 'policies',
        'project_id': 'project_id',
        'user_id': 'user_id'
    }

    def __init__(self, id=None, name=None, members=None, metadata=None, policies=None, project_id=None, user_id=None):  # noqa: E501
        """NovaServerGroup - a model defined in huaweicloud sdk"""

        self._id = None
        self._name = None
        self._members = None
        self._metadata = None
        self._policies = None
        self._project_id = None
        self._user_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.members = members
        self.metadata = metadata
        self.policies = policies
        self.project_id = project_id
        self.user_id = user_id

    @property
    def id(self):
        """Gets the id of this NovaServerGroup.

        云服务器组UUID。

        :return: The id of this NovaServerGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaServerGroup.

        云服务器组UUID。

        :param id: The id of this NovaServerGroup.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NovaServerGroup.

        云服务器组名称。

        :return: The name of this NovaServerGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaServerGroup.

        云服务器组名称。

        :param name: The name of this NovaServerGroup.
        :type: str
        """
        self._name = name

    @property
    def members(self):
        """Gets the members of this NovaServerGroup.

        云服务器组中包含的云服务器列表。

        :return: The members of this NovaServerGroup.
        :rtype: list[str]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this NovaServerGroup.

        云服务器组中包含的云服务器列表。

        :param members: The members of this NovaServerGroup.
        :type: list[str]
        """
        self._members = members

    @property
    def metadata(self):
        """Gets the metadata of this NovaServerGroup.

        云服务器组元数据。

        :return: The metadata of this NovaServerGroup.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NovaServerGroup.

        云服务器组元数据。

        :param metadata: The metadata of this NovaServerGroup.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def policies(self):
        """Gets the policies of this NovaServerGroup.

        与服务器组关联的策略名称列表。当前有效的策略名称为:  anti-affinity -此组中的服务器必须安排到不同的主机；  affinity -此组中的服务器必须安排在同一主机上.  soft-anti-affinity –如果可能, 应将此组中的服务器安排到不同的主机, 但如果无法实现, 则仍应安排它们, 而不是导致生成失败。  soft-affinity -如果可能, 应将此组中的服务器安排在同一主机上, 但如果无法实现, 则仍应安排它们, 而不是导致生成失败。

        :return: The policies of this NovaServerGroup.
        :rtype: list[str]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this NovaServerGroup.

        与服务器组关联的策略名称列表。当前有效的策略名称为:  anti-affinity -此组中的服务器必须安排到不同的主机；  affinity -此组中的服务器必须安排在同一主机上.  soft-anti-affinity –如果可能, 应将此组中的服务器安排到不同的主机, 但如果无法实现, 则仍应安排它们, 而不是导致生成失败。  soft-affinity -如果可能, 应将此组中的服务器安排在同一主机上, 但如果无法实现, 则仍应安排它们, 而不是导致生成失败。

        :param policies: The policies of this NovaServerGroup.
        :type: list[str]
        """
        self._policies = policies

    @property
    def project_id(self):
        """Gets the project_id of this NovaServerGroup.

        弹性云服务器组所属项目ID，UUID格式。   > 说明：  - 微版本2.13新增参数。

        :return: The project_id of this NovaServerGroup.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NovaServerGroup.

        弹性云服务器组所属项目ID，UUID格式。   > 说明：  - 微版本2.13新增参数。

        :param project_id: The project_id of this NovaServerGroup.
        :type: str
        """
        self._project_id = project_id

    @property
    def user_id(self):
        """Gets the user_id of this NovaServerGroup.

        弹性云服务器组所属用户ID，UUID格式。   > 说明：  - 微版本2.13新增参数。

        :return: The user_id of this NovaServerGroup.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NovaServerGroup.

        弹性云服务器组所属用户ID，UUID格式。   > 说明：  - 微版本2.13新增参数。

        :param user_id: The user_id of this NovaServerGroup.
        :type: str
        """
        self._user_id = user_id

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
        if not isinstance(other, NovaServerGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
