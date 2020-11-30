# coding: utf-8

import pprint
import re

import six





class Member:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tcs_need': 'bool',
        'channel_name': 'str',
        'invited_orgs': 'list[OrganizationV2]',
        'invitor_info': 'MemberInvitor',
        'invitee_info': 'MemberInvitee'
    }

    attribute_map = {
        'tcs_need': 'tcs_need',
        'channel_name': 'channel_name',
        'invited_orgs': 'invited_orgs',
        'invitor_info': 'invitor_info',
        'invitee_info': 'invitee_info'
    }

    def __init__(self, tcs_need=None, channel_name=None, invited_orgs=None, invitor_info=None, invitee_info=None):
        """Member - a model defined in huaweicloud sdk"""
        
        

        self._tcs_need = None
        self._channel_name = None
        self._invited_orgs = None
        self._invitor_info = None
        self._invitee_info = None
        self.discriminator = None

        if tcs_need is not None:
            self.tcs_need = tcs_need
        if channel_name is not None:
            self.channel_name = channel_name
        if invited_orgs is not None:
            self.invited_orgs = invited_orgs
        if invitor_info is not None:
            self.invitor_info = invitor_info
        if invitee_info is not None:
            self.invitee_info = invitee_info

    @property
    def tcs_need(self):
        """Gets the tcs_need of this Member.

        是否支持可信

        :return: The tcs_need of this Member.
        :rtype: bool
        """
        return self._tcs_need

    @tcs_need.setter
    def tcs_need(self, tcs_need):
        """Sets the tcs_need of this Member.

        是否支持可信

        :param tcs_need: The tcs_need of this Member.
        :type: bool
        """
        self._tcs_need = tcs_need

    @property
    def channel_name(self):
        """Gets the channel_name of this Member.

        通道名称

        :return: The channel_name of this Member.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this Member.

        通道名称

        :param channel_name: The channel_name of this Member.
        :type: str
        """
        self._channel_name = channel_name

    @property
    def invited_orgs(self):
        """Gets the invited_orgs of this Member.

        被邀请的组织

        :return: The invited_orgs of this Member.
        :rtype: list[OrganizationV2]
        """
        return self._invited_orgs

    @invited_orgs.setter
    def invited_orgs(self, invited_orgs):
        """Sets the invited_orgs of this Member.

        被邀请的组织

        :param invited_orgs: The invited_orgs of this Member.
        :type: list[OrganizationV2]
        """
        self._invited_orgs = invited_orgs

    @property
    def invitor_info(self):
        """Gets the invitor_info of this Member.


        :return: The invitor_info of this Member.
        :rtype: MemberInvitor
        """
        return self._invitor_info

    @invitor_info.setter
    def invitor_info(self, invitor_info):
        """Sets the invitor_info of this Member.


        :param invitor_info: The invitor_info of this Member.
        :type: MemberInvitor
        """
        self._invitor_info = invitor_info

    @property
    def invitee_info(self):
        """Gets the invitee_info of this Member.


        :return: The invitee_info of this Member.
        :rtype: MemberInvitee
        """
        return self._invitee_info

    @invitee_info.setter
    def invitee_info(self, invitee_info):
        """Sets the invitee_info of this Member.


        :param invitee_info: The invitee_info of this Member.
        :type: MemberInvitee
        """
        self._invitee_info = invitee_info

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
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
