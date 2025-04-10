# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionInfo:

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
        'action_type': 'str',
        'action_id': 'str',
        'sort_order': 'int',
        'playbook_id': 'str',
        'playbook_version_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'action_type': 'action_type',
        'action_id': 'action_id',
        'sort_order': 'sort_order',
        'playbook_id': 'playbook_id',
        'playbook_version_id': 'playbook_version_id',
        'project_id': 'project_id'
    }

    def __init__(self, id=None, name=None, description=None, action_type=None, action_id=None, sort_order=None, playbook_id=None, playbook_version_id=None, project_id=None):
        r"""ActionInfo

        The model defined in huaweicloud sdk

        :param id: Id value
        :type id: str
        :param name: The name, display only
        :type name: str
        :param description: The description, display only
        :type description: str
        :param action_type: Type of action, aopworkflow, Script, Task and so on.
        :type action_type: str
        :param action_id: action id
        :type action_id: str
        :param sort_order: sort_order
        :type sort_order: int
        :param playbook_id: 剧本ID
        :type playbook_id: str
        :param playbook_version_id: 剧本版本ID
        :type playbook_version_id: str
        :param project_id: project_id
        :type project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._action_type = None
        self._action_id = None
        self._sort_order = None
        self._playbook_id = None
        self._playbook_version_id = None
        self._project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if action_type is not None:
            self.action_type = action_type
        if action_id is not None:
            self.action_id = action_id
        if sort_order is not None:
            self.sort_order = sort_order
        if playbook_id is not None:
            self.playbook_id = playbook_id
        if playbook_version_id is not None:
            self.playbook_version_id = playbook_version_id
        if project_id is not None:
            self.project_id = project_id

    @property
    def id(self):
        r"""Gets the id of this ActionInfo.

        Id value

        :return: The id of this ActionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ActionInfo.

        Id value

        :param id: The id of this ActionInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ActionInfo.

        The name, display only

        :return: The name of this ActionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ActionInfo.

        The name, display only

        :param name: The name of this ActionInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ActionInfo.

        The description, display only

        :return: The description of this ActionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ActionInfo.

        The description, display only

        :param description: The description of this ActionInfo.
        :type description: str
        """
        self._description = description

    @property
    def action_type(self):
        r"""Gets the action_type of this ActionInfo.

        Type of action, aopworkflow, Script, Task and so on.

        :return: The action_type of this ActionInfo.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this ActionInfo.

        Type of action, aopworkflow, Script, Task and so on.

        :param action_type: The action_type of this ActionInfo.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def action_id(self):
        r"""Gets the action_id of this ActionInfo.

        action id

        :return: The action_id of this ActionInfo.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this ActionInfo.

        action id

        :param action_id: The action_id of this ActionInfo.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def sort_order(self):
        r"""Gets the sort_order of this ActionInfo.

        sort_order

        :return: The sort_order of this ActionInfo.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        r"""Sets the sort_order of this ActionInfo.

        sort_order

        :param sort_order: The sort_order of this ActionInfo.
        :type sort_order: int
        """
        self._sort_order = sort_order

    @property
    def playbook_id(self):
        r"""Gets the playbook_id of this ActionInfo.

        剧本ID

        :return: The playbook_id of this ActionInfo.
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        r"""Sets the playbook_id of this ActionInfo.

        剧本ID

        :param playbook_id: The playbook_id of this ActionInfo.
        :type playbook_id: str
        """
        self._playbook_id = playbook_id

    @property
    def playbook_version_id(self):
        r"""Gets the playbook_version_id of this ActionInfo.

        剧本版本ID

        :return: The playbook_version_id of this ActionInfo.
        :rtype: str
        """
        return self._playbook_version_id

    @playbook_version_id.setter
    def playbook_version_id(self, playbook_version_id):
        r"""Sets the playbook_version_id of this ActionInfo.

        剧本版本ID

        :param playbook_version_id: The playbook_version_id of this ActionInfo.
        :type playbook_version_id: str
        """
        self._playbook_version_id = playbook_version_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ActionInfo.

        project_id

        :return: The project_id of this ActionInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ActionInfo.

        project_id

        :param project_id: The project_id of this ActionInfo.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ActionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
