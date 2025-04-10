# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteMemberInviteRequestBody:

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
        'invited_userinfo': 'list[InvitationDetail]'
    }

    attribute_map = {
        'bcs_id': 'bcs_id',
        'channel_name': 'channel_name',
        'invited_userinfo': 'invited_userinfo'
    }

    def __init__(self, bcs_id=None, channel_name=None, invited_userinfo=None):
        r"""DeleteMemberInviteRequestBody

        The model defined in huaweicloud sdk

        :param bcs_id: 邀请实例id
        :type bcs_id: str
        :param channel_name: 邀请加入的通道名
        :type channel_name: str
        :param invited_userinfo: 被邀请的用户列表，对应信息可通过获取联盟成员列表（ListMembers）接口查询，或被邀请方已加入联盟，或邀请状态为released时，需填写准确的被邀请方bcs实例id和邀请状态
        :type invited_userinfo: list[:class:`huaweicloudsdkbcs.v2.InvitationDetail`]
        """
        
        

        self._bcs_id = None
        self._channel_name = None
        self._invited_userinfo = None
        self.discriminator = None

        self.bcs_id = bcs_id
        self.channel_name = channel_name
        self.invited_userinfo = invited_userinfo

    @property
    def bcs_id(self):
        r"""Gets the bcs_id of this DeleteMemberInviteRequestBody.

        邀请实例id

        :return: The bcs_id of this DeleteMemberInviteRequestBody.
        :rtype: str
        """
        return self._bcs_id

    @bcs_id.setter
    def bcs_id(self, bcs_id):
        r"""Sets the bcs_id of this DeleteMemberInviteRequestBody.

        邀请实例id

        :param bcs_id: The bcs_id of this DeleteMemberInviteRequestBody.
        :type bcs_id: str
        """
        self._bcs_id = bcs_id

    @property
    def channel_name(self):
        r"""Gets the channel_name of this DeleteMemberInviteRequestBody.

        邀请加入的通道名

        :return: The channel_name of this DeleteMemberInviteRequestBody.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        r"""Sets the channel_name of this DeleteMemberInviteRequestBody.

        邀请加入的通道名

        :param channel_name: The channel_name of this DeleteMemberInviteRequestBody.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def invited_userinfo(self):
        r"""Gets the invited_userinfo of this DeleteMemberInviteRequestBody.

        被邀请的用户列表，对应信息可通过获取联盟成员列表（ListMembers）接口查询，或被邀请方已加入联盟，或邀请状态为released时，需填写准确的被邀请方bcs实例id和邀请状态

        :return: The invited_userinfo of this DeleteMemberInviteRequestBody.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.InvitationDetail`]
        """
        return self._invited_userinfo

    @invited_userinfo.setter
    def invited_userinfo(self, invited_userinfo):
        r"""Sets the invited_userinfo of this DeleteMemberInviteRequestBody.

        被邀请的用户列表，对应信息可通过获取联盟成员列表（ListMembers）接口查询，或被邀请方已加入联盟，或邀请状态为released时，需填写准确的被邀请方bcs实例id和邀请状态

        :param invited_userinfo: The invited_userinfo of this DeleteMemberInviteRequestBody.
        :type invited_userinfo: list[:class:`huaweicloudsdkbcs.v2.InvitationDetail`]
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
        if not isinstance(other, DeleteMemberInviteRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
