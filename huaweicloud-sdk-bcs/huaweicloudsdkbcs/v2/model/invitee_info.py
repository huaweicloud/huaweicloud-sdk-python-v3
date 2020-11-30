# coding: utf-8

import pprint
import re

import six





class InviteeInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'invitee_id': 'str',
        'invitee_name': 'int',
        'invitee_bcs_name': 'str',
        'invitee_bcs_id': 'str',
        'invitee_project_id': 'str'
    }

    attribute_map = {
        'invitee_id': 'invitee_id',
        'invitee_name': 'invitee_name',
        'invitee_bcs_name': 'invitee_bcs_name',
        'invitee_bcs_id': 'invitee_bcs_id',
        'invitee_project_id': 'invitee_project_id'
    }

    def __init__(self, invitee_id=None, invitee_name=None, invitee_bcs_name=None, invitee_bcs_id=None, invitee_project_id=None):
        """InviteeInfo - a model defined in huaweicloud sdk"""
        
        

        self._invitee_id = None
        self._invitee_name = None
        self._invitee_bcs_name = None
        self._invitee_bcs_id = None
        self._invitee_project_id = None
        self.discriminator = None

        if invitee_id is not None:
            self.invitee_id = invitee_id
        if invitee_name is not None:
            self.invitee_name = invitee_name
        if invitee_bcs_name is not None:
            self.invitee_bcs_name = invitee_bcs_name
        if invitee_bcs_id is not None:
            self.invitee_bcs_id = invitee_bcs_id
        if invitee_project_id is not None:
            self.invitee_project_id = invitee_project_id

    @property
    def invitee_id(self):
        """Gets the invitee_id of this InviteeInfo.

        被邀请用户id

        :return: The invitee_id of this InviteeInfo.
        :rtype: str
        """
        return self._invitee_id

    @invitee_id.setter
    def invitee_id(self, invitee_id):
        """Sets the invitee_id of this InviteeInfo.

        被邀请用户id

        :param invitee_id: The invitee_id of this InviteeInfo.
        :type: str
        """
        self._invitee_id = invitee_id

    @property
    def invitee_name(self):
        """Gets the invitee_name of this InviteeInfo.

        被邀请租户名称

        :return: The invitee_name of this InviteeInfo.
        :rtype: int
        """
        return self._invitee_name

    @invitee_name.setter
    def invitee_name(self, invitee_name):
        """Sets the invitee_name of this InviteeInfo.

        被邀请租户名称

        :param invitee_name: The invitee_name of this InviteeInfo.
        :type: int
        """
        self._invitee_name = invitee_name

    @property
    def invitee_bcs_name(self):
        """Gets the invitee_bcs_name of this InviteeInfo.

        被邀请的服务名称

        :return: The invitee_bcs_name of this InviteeInfo.
        :rtype: str
        """
        return self._invitee_bcs_name

    @invitee_bcs_name.setter
    def invitee_bcs_name(self, invitee_bcs_name):
        """Sets the invitee_bcs_name of this InviteeInfo.

        被邀请的服务名称

        :param invitee_bcs_name: The invitee_bcs_name of this InviteeInfo.
        :type: str
        """
        self._invitee_bcs_name = invitee_bcs_name

    @property
    def invitee_bcs_id(self):
        """Gets the invitee_bcs_id of this InviteeInfo.

        被邀请的服务id

        :return: The invitee_bcs_id of this InviteeInfo.
        :rtype: str
        """
        return self._invitee_bcs_id

    @invitee_bcs_id.setter
    def invitee_bcs_id(self, invitee_bcs_id):
        """Sets the invitee_bcs_id of this InviteeInfo.

        被邀请的服务id

        :param invitee_bcs_id: The invitee_bcs_id of this InviteeInfo.
        :type: str
        """
        self._invitee_bcs_id = invitee_bcs_id

    @property
    def invitee_project_id(self):
        """Gets the invitee_project_id of this InviteeInfo.

        被邀请的项目id

        :return: The invitee_project_id of this InviteeInfo.
        :rtype: str
        """
        return self._invitee_project_id

    @invitee_project_id.setter
    def invitee_project_id(self, invitee_project_id):
        """Sets the invitee_project_id of this InviteeInfo.

        被邀请的项目id

        :param invitee_project_id: The invitee_project_id of this InviteeInfo.
        :type: str
        """
        self._invitee_project_id = invitee_project_id

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
        if not isinstance(other, InviteeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
