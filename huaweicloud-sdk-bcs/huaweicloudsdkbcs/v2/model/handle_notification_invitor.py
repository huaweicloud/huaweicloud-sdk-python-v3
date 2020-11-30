# coding: utf-8

import pprint
import re

import six





class HandleNotificationInvitor:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'invitor_bcs_id': 'str',
        'invitor_project_id': 'str',
        'invitor_username': 'str'
    }

    attribute_map = {
        'invitor_bcs_id': 'invitor_bcs_id',
        'invitor_project_id': 'invitor_project_id',
        'invitor_username': 'invitor_username'
    }

    def __init__(self, invitor_bcs_id=None, invitor_project_id=None, invitor_username=None):
        """HandleNotificationInvitor - a model defined in huaweicloud sdk"""
        
        

        self._invitor_bcs_id = None
        self._invitor_project_id = None
        self._invitor_username = None
        self.discriminator = None

        if invitor_bcs_id is not None:
            self.invitor_bcs_id = invitor_bcs_id
        if invitor_project_id is not None:
            self.invitor_project_id = invitor_project_id
        if invitor_username is not None:
            self.invitor_username = invitor_username

    @property
    def invitor_bcs_id(self):
        """Gets the invitor_bcs_id of this HandleNotificationInvitor.

        邀请方实例id

        :return: The invitor_bcs_id of this HandleNotificationInvitor.
        :rtype: str
        """
        return self._invitor_bcs_id

    @invitor_bcs_id.setter
    def invitor_bcs_id(self, invitor_bcs_id):
        """Sets the invitor_bcs_id of this HandleNotificationInvitor.

        邀请方实例id

        :param invitor_bcs_id: The invitor_bcs_id of this HandleNotificationInvitor.
        :type: str
        """
        self._invitor_bcs_id = invitor_bcs_id

    @property
    def invitor_project_id(self):
        """Gets the invitor_project_id of this HandleNotificationInvitor.

        邀请方project id

        :return: The invitor_project_id of this HandleNotificationInvitor.
        :rtype: str
        """
        return self._invitor_project_id

    @invitor_project_id.setter
    def invitor_project_id(self, invitor_project_id):
        """Sets the invitor_project_id of this HandleNotificationInvitor.

        邀请方project id

        :param invitor_project_id: The invitor_project_id of this HandleNotificationInvitor.
        :type: str
        """
        self._invitor_project_id = invitor_project_id

    @property
    def invitor_username(self):
        """Gets the invitor_username of this HandleNotificationInvitor.

        邀请方租户名

        :return: The invitor_username of this HandleNotificationInvitor.
        :rtype: str
        """
        return self._invitor_username

    @invitor_username.setter
    def invitor_username(self, invitor_username):
        """Sets the invitor_username of this HandleNotificationInvitor.

        邀请方租户名

        :param invitor_username: The invitor_username of this HandleNotificationInvitor.
        :type: str
        """
        self._invitor_username = invitor_username

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
        if not isinstance(other, HandleNotificationInvitor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
