# coding: utf-8

import pprint
import re

import six





class HandleNotificationInvitee:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'invitee_bcs_id': 'str',
        'invitee_bcs_name': 'str',
        'invitee_project_id': 'str',
        'invitee_user_id': 'str'
    }

    attribute_map = {
        'invitee_bcs_id': 'invitee_bcs_id',
        'invitee_bcs_name': 'invitee_bcs_name',
        'invitee_project_id': 'invitee_project_id',
        'invitee_user_id': 'invitee_user_id'
    }

    def __init__(self, invitee_bcs_id=None, invitee_bcs_name=None, invitee_project_id=None, invitee_user_id=None):
        """HandleNotificationInvitee - a model defined in huaweicloud sdk"""
        
        

        self._invitee_bcs_id = None
        self._invitee_bcs_name = None
        self._invitee_project_id = None
        self._invitee_user_id = None
        self.discriminator = None

        self.invitee_bcs_id = invitee_bcs_id
        self.invitee_bcs_name = invitee_bcs_name
        self.invitee_project_id = invitee_project_id
        self.invitee_user_id = invitee_user_id

    @property
    def invitee_bcs_id(self):
        """Gets the invitee_bcs_id of this HandleNotificationInvitee.

        被邀请方服务实例id

        :return: The invitee_bcs_id of this HandleNotificationInvitee.
        :rtype: str
        """
        return self._invitee_bcs_id

    @invitee_bcs_id.setter
    def invitee_bcs_id(self, invitee_bcs_id):
        """Sets the invitee_bcs_id of this HandleNotificationInvitee.

        被邀请方服务实例id

        :param invitee_bcs_id: The invitee_bcs_id of this HandleNotificationInvitee.
        :type: str
        """
        self._invitee_bcs_id = invitee_bcs_id

    @property
    def invitee_bcs_name(self):
        """Gets the invitee_bcs_name of this HandleNotificationInvitee.

        被邀请方服务实例名称，同意联盟邀请时比填

        :return: The invitee_bcs_name of this HandleNotificationInvitee.
        :rtype: str
        """
        return self._invitee_bcs_name

    @invitee_bcs_name.setter
    def invitee_bcs_name(self, invitee_bcs_name):
        """Sets the invitee_bcs_name of this HandleNotificationInvitee.

        被邀请方服务实例名称，同意联盟邀请时比填

        :param invitee_bcs_name: The invitee_bcs_name of this HandleNotificationInvitee.
        :type: str
        """
        self._invitee_bcs_name = invitee_bcs_name

    @property
    def invitee_project_id(self):
        """Gets the invitee_project_id of this HandleNotificationInvitee.

        被邀请方project id

        :return: The invitee_project_id of this HandleNotificationInvitee.
        :rtype: str
        """
        return self._invitee_project_id

    @invitee_project_id.setter
    def invitee_project_id(self, invitee_project_id):
        """Sets the invitee_project_id of this HandleNotificationInvitee.

        被邀请方project id

        :param invitee_project_id: The invitee_project_id of this HandleNotificationInvitee.
        :type: str
        """
        self._invitee_project_id = invitee_project_id

    @property
    def invitee_user_id(self):
        """Gets the invitee_user_id of this HandleNotificationInvitee.

        被邀请方租户id

        :return: The invitee_user_id of this HandleNotificationInvitee.
        :rtype: str
        """
        return self._invitee_user_id

    @invitee_user_id.setter
    def invitee_user_id(self, invitee_user_id):
        """Sets the invitee_user_id of this HandleNotificationInvitee.

        被邀请方租户id

        :param invitee_user_id: The invitee_user_id of this HandleNotificationInvitee.
        :type: str
        """
        self._invitee_user_id = invitee_user_id

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
        if not isinstance(other, HandleNotificationInvitee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
