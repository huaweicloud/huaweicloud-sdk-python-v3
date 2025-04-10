# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""Member

        The model defined in huaweicloud sdk

        :param tcs_need: 是否支持可信
        :type tcs_need: bool
        :param channel_name: 通道名称
        :type channel_name: str
        :param invited_orgs: 被邀请的组织
        :type invited_orgs: list[:class:`huaweicloudsdkbcs.v2.OrganizationV2`]
        :param invitor_info: 
        :type invitor_info: :class:`huaweicloudsdkbcs.v2.MemberInvitor`
        :param invitee_info: 
        :type invitee_info: :class:`huaweicloudsdkbcs.v2.MemberInvitee`
        """
        
        

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
        r"""Gets the tcs_need of this Member.

        是否支持可信

        :return: The tcs_need of this Member.
        :rtype: bool
        """
        return self._tcs_need

    @tcs_need.setter
    def tcs_need(self, tcs_need):
        r"""Sets the tcs_need of this Member.

        是否支持可信

        :param tcs_need: The tcs_need of this Member.
        :type tcs_need: bool
        """
        self._tcs_need = tcs_need

    @property
    def channel_name(self):
        r"""Gets the channel_name of this Member.

        通道名称

        :return: The channel_name of this Member.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        r"""Sets the channel_name of this Member.

        通道名称

        :param channel_name: The channel_name of this Member.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def invited_orgs(self):
        r"""Gets the invited_orgs of this Member.

        被邀请的组织

        :return: The invited_orgs of this Member.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.OrganizationV2`]
        """
        return self._invited_orgs

    @invited_orgs.setter
    def invited_orgs(self, invited_orgs):
        r"""Sets the invited_orgs of this Member.

        被邀请的组织

        :param invited_orgs: The invited_orgs of this Member.
        :type invited_orgs: list[:class:`huaweicloudsdkbcs.v2.OrganizationV2`]
        """
        self._invited_orgs = invited_orgs

    @property
    def invitor_info(self):
        r"""Gets the invitor_info of this Member.

        :return: The invitor_info of this Member.
        :rtype: :class:`huaweicloudsdkbcs.v2.MemberInvitor`
        """
        return self._invitor_info

    @invitor_info.setter
    def invitor_info(self, invitor_info):
        r"""Sets the invitor_info of this Member.

        :param invitor_info: The invitor_info of this Member.
        :type invitor_info: :class:`huaweicloudsdkbcs.v2.MemberInvitor`
        """
        self._invitor_info = invitor_info

    @property
    def invitee_info(self):
        r"""Gets the invitee_info of this Member.

        :return: The invitee_info of this Member.
        :rtype: :class:`huaweicloudsdkbcs.v2.MemberInvitee`
        """
        return self._invitee_info

    @invitee_info.setter
    def invitee_info(self, invitee_info):
        r"""Sets the invitee_info of this Member.

        :param invitee_info: The invitee_info of this Member.
        :type invitee_info: :class:`huaweicloudsdkbcs.v2.MemberInvitee`
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
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
