# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePlaybookInfo:

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
        'workspace_id': 'str',
        'approve_role': 'str',
        'user_role': 'str',
        'edit_role': 'str',
        'owner_id': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'workspace_id': 'workspace_id',
        'approve_role': 'approve_role',
        'user_role': 'user_role',
        'edit_role': 'edit_role',
        'owner_id': 'owner_id',
        'enabled': 'enabled'
    }

    def __init__(self, name=None, description=None, workspace_id=None, approve_role=None, user_role=None, edit_role=None, owner_id=None, enabled=None):
        """CreatePlaybookInfo

        The model defined in huaweicloud sdk

        :param name: The name, display only
        :type name: str
        :param description: The description, display only
        :type description: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param approve_role: Role required for approve
        :type approve_role: str
        :param user_role: Role required for use
        :type user_role: str
        :param edit_role: Role required for edit
        :type edit_role: str
        :param owner_id: Owner id
        :type owner_id: str
        :param enabled: If is enabled, false for disenabled, true for enabled
        :type enabled: bool
        """
        
        

        self._name = None
        self._description = None
        self._workspace_id = None
        self._approve_role = None
        self._user_role = None
        self._edit_role = None
        self._owner_id = None
        self._enabled = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if approve_role is not None:
            self.approve_role = approve_role
        if user_role is not None:
            self.user_role = user_role
        if edit_role is not None:
            self.edit_role = edit_role
        if owner_id is not None:
            self.owner_id = owner_id
        if enabled is not None:
            self.enabled = enabled

    @property
    def name(self):
        """Gets the name of this CreatePlaybookInfo.

        The name, display only

        :return: The name of this CreatePlaybookInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePlaybookInfo.

        The name, display only

        :param name: The name of this CreatePlaybookInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreatePlaybookInfo.

        The description, display only

        :return: The description of this CreatePlaybookInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePlaybookInfo.

        The description, display only

        :param description: The description of this CreatePlaybookInfo.
        :type description: str
        """
        self._description = description

    @property
    def workspace_id(self):
        """Gets the workspace_id of this CreatePlaybookInfo.

        工作空间id

        :return: The workspace_id of this CreatePlaybookInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this CreatePlaybookInfo.

        工作空间id

        :param workspace_id: The workspace_id of this CreatePlaybookInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def approve_role(self):
        """Gets the approve_role of this CreatePlaybookInfo.

        Role required for approve

        :return: The approve_role of this CreatePlaybookInfo.
        :rtype: str
        """
        return self._approve_role

    @approve_role.setter
    def approve_role(self, approve_role):
        """Sets the approve_role of this CreatePlaybookInfo.

        Role required for approve

        :param approve_role: The approve_role of this CreatePlaybookInfo.
        :type approve_role: str
        """
        self._approve_role = approve_role

    @property
    def user_role(self):
        """Gets the user_role of this CreatePlaybookInfo.

        Role required for use

        :return: The user_role of this CreatePlaybookInfo.
        :rtype: str
        """
        return self._user_role

    @user_role.setter
    def user_role(self, user_role):
        """Sets the user_role of this CreatePlaybookInfo.

        Role required for use

        :param user_role: The user_role of this CreatePlaybookInfo.
        :type user_role: str
        """
        self._user_role = user_role

    @property
    def edit_role(self):
        """Gets the edit_role of this CreatePlaybookInfo.

        Role required for edit

        :return: The edit_role of this CreatePlaybookInfo.
        :rtype: str
        """
        return self._edit_role

    @edit_role.setter
    def edit_role(self, edit_role):
        """Sets the edit_role of this CreatePlaybookInfo.

        Role required for edit

        :param edit_role: The edit_role of this CreatePlaybookInfo.
        :type edit_role: str
        """
        self._edit_role = edit_role

    @property
    def owner_id(self):
        """Gets the owner_id of this CreatePlaybookInfo.

        Owner id

        :return: The owner_id of this CreatePlaybookInfo.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this CreatePlaybookInfo.

        Owner id

        :param owner_id: The owner_id of this CreatePlaybookInfo.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def enabled(self):
        """Gets the enabled of this CreatePlaybookInfo.

        If is enabled, false for disenabled, true for enabled

        :return: The enabled of this CreatePlaybookInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreatePlaybookInfo.

        If is enabled, false for disenabled, true for enabled

        :param enabled: The enabled of this CreatePlaybookInfo.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, CreatePlaybookInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
