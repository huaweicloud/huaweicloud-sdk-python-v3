# coding: utf-8

import pprint
import re

import six





class BatchInviteMembersToChannelRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bcs_id': 'str',
        'channel_name': 'str',
        'invitor_username': 'str',
        'invited_userinfo': 'list[InvitedDomain]'
    }

    attribute_map = {
        'bcs_id': 'bcs_id',
        'channel_name': 'channel_name',
        'invitor_username': 'invitor_username',
        'invited_userinfo': 'invited_userinfo'
    }

    def __init__(self, bcs_id=None, channel_name=None, invitor_username=None, invited_userinfo=None):
        """BatchInviteMembersToChannelRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._bcs_id = None
        self._channel_name = None
        self._invitor_username = None
        self._invited_userinfo = None
        self.discriminator = None

        self.bcs_id = bcs_id
        self.channel_name = channel_name
        if invitor_username is not None:
            self.invitor_username = invitor_username
        self.invited_userinfo = invited_userinfo

    @property
    def bcs_id(self):
        """Gets the bcs_id of this BatchInviteMembersToChannelRequestBody.

        邀请实例id

        :return: The bcs_id of this BatchInviteMembersToChannelRequestBody.
        :rtype: str
        """
        return self._bcs_id

    @bcs_id.setter
    def bcs_id(self, bcs_id):
        """Sets the bcs_id of this BatchInviteMembersToChannelRequestBody.

        邀请实例id

        :param bcs_id: The bcs_id of this BatchInviteMembersToChannelRequestBody.
        :type: str
        """
        self._bcs_id = bcs_id

    @property
    def channel_name(self):
        """Gets the channel_name of this BatchInviteMembersToChannelRequestBody.

        邀请加入的通道名

        :return: The channel_name of this BatchInviteMembersToChannelRequestBody.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this BatchInviteMembersToChannelRequestBody.

        邀请加入的通道名

        :param channel_name: The channel_name of this BatchInviteMembersToChannelRequestBody.
        :type: str
        """
        self._channel_name = channel_name

    @property
    def invitor_username(self):
        """Gets the invitor_username of this BatchInviteMembersToChannelRequestBody.

        发出邀请的租户名

        :return: The invitor_username of this BatchInviteMembersToChannelRequestBody.
        :rtype: str
        """
        return self._invitor_username

    @invitor_username.setter
    def invitor_username(self, invitor_username):
        """Sets the invitor_username of this BatchInviteMembersToChannelRequestBody.

        发出邀请的租户名

        :param invitor_username: The invitor_username of this BatchInviteMembersToChannelRequestBody.
        :type: str
        """
        self._invitor_username = invitor_username

    @property
    def invited_userinfo(self):
        """Gets the invited_userinfo of this BatchInviteMembersToChannelRequestBody.

        被邀请的用户列表

        :return: The invited_userinfo of this BatchInviteMembersToChannelRequestBody.
        :rtype: list[InvitedDomain]
        """
        return self._invited_userinfo

    @invited_userinfo.setter
    def invited_userinfo(self, invited_userinfo):
        """Sets the invited_userinfo of this BatchInviteMembersToChannelRequestBody.

        被邀请的用户列表

        :param invited_userinfo: The invited_userinfo of this BatchInviteMembersToChannelRequestBody.
        :type: list[InvitedDomain]
        """
        self._invited_userinfo = invited_userinfo

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
        if not isinstance(other, BatchInviteMembersToChannelRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
