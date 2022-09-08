# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestAssigneeListItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'float',
        'name': 'str',
        'state': 'str',
        'username': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'username': 'username'
    }

    def __init__(self, id=None, name=None, state=None, username=None):
        """MergeRequestAssigneeListItem

        The model defined in huaweicloud sdk

        :param id: 用户id
        :type id: float
        :param name: 用户名
        :type name: str
        :param state: 用户状态
        :type state: str
        :param username: 用户iamId
        :type username: str
        """
        
        

        self._id = None
        self._name = None
        self._state = None
        self._username = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if username is not None:
            self.username = username

    @property
    def id(self):
        """Gets the id of this MergeRequestAssigneeListItem.

        用户id

        :return: The id of this MergeRequestAssigneeListItem.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MergeRequestAssigneeListItem.

        用户id

        :param id: The id of this MergeRequestAssigneeListItem.
        :type id: float
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this MergeRequestAssigneeListItem.

        用户名

        :return: The name of this MergeRequestAssigneeListItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MergeRequestAssigneeListItem.

        用户名

        :param name: The name of this MergeRequestAssigneeListItem.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        """Gets the state of this MergeRequestAssigneeListItem.

        用户状态

        :return: The state of this MergeRequestAssigneeListItem.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MergeRequestAssigneeListItem.

        用户状态

        :param state: The state of this MergeRequestAssigneeListItem.
        :type state: str
        """
        self._state = state

    @property
    def username(self):
        """Gets the username of this MergeRequestAssigneeListItem.

        用户iamId

        :return: The username of this MergeRequestAssigneeListItem.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this MergeRequestAssigneeListItem.

        用户iamId

        :param username: The username of this MergeRequestAssigneeListItem.
        :type username: str
        """
        self._username = username

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
        if not isinstance(other, MergeRequestAssigneeListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
