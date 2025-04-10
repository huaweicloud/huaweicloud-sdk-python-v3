# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuitUnionFromMemberListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inviter_bcsid': 'str',
        'inviter_projectid': 'str',
        'inviter_domainid': 'str',
        'inviter_username': 'str',
        'channel_name': 'str',
        'invitee_bcsid': 'str',
        'invitee_projectid': 'str',
        'invitee_domainid': 'str'
    }

    attribute_map = {
        'inviter_bcsid': 'inviter_bcsid',
        'inviter_projectid': 'inviter_projectid',
        'inviter_domainid': 'inviter_domainid',
        'inviter_username': 'inviter_username',
        'channel_name': 'channel_name',
        'invitee_bcsid': 'invitee_bcsid',
        'invitee_projectid': 'invitee_projectid',
        'invitee_domainid': 'invitee_domainid'
    }

    def __init__(self, inviter_bcsid=None, inviter_projectid=None, inviter_domainid=None, inviter_username=None, channel_name=None, invitee_bcsid=None, invitee_projectid=None, invitee_domainid=None):
        r"""QuitUnionFromMemberListRequestBody

        The model defined in huaweicloud sdk

        :param inviter_bcsid: 邀请方BCS服务实例ID。可调用“查询服务实例列表”接口获取对应的ID
        :type inviter_bcsid: str
        :param inviter_projectid: 邀请方项目ID。控制台-&gt;邀请方帐号-&gt;我的凭证-&gt;API凭证-&gt;项目列表，选择对应的项目ID
        :type inviter_projectid: str
        :param inviter_domainid: 邀请方租户ID。控制台-&gt;邀请方帐号-&gt;我的凭证-&gt;API凭证-&gt;帐号ID
        :type inviter_domainid: str
        :param inviter_username: 邀请方租户名称。控制台-&gt;邀请方帐号-&gt;我的凭证-&gt;API凭证-&gt;帐号名
        :type inviter_username: str
        :param channel_name: 联盟通道名称。BCS管理面-&gt;成员管理-&gt;通道，选择对应的邀请的通道
        :type channel_name: str
        :param invitee_bcsid: 被邀请方BCS服务实例ID。可调用“查询服务实例列表”接口获取对应的id
        :type invitee_bcsid: str
        :param invitee_projectid: 被邀请方项目ID。控制台-&gt;被邀请方帐号-&gt;我的凭证-&gt;API凭证-&gt;项目列表，选择对应的项目ID
        :type invitee_projectid: str
        :param invitee_domainid: 被邀请方租户ID。控制台-&gt;被邀请方帐号-&gt;我的凭证-&gt;API凭证-&gt;帐号ID
        :type invitee_domainid: str
        """
        
        

        self._inviter_bcsid = None
        self._inviter_projectid = None
        self._inviter_domainid = None
        self._inviter_username = None
        self._channel_name = None
        self._invitee_bcsid = None
        self._invitee_projectid = None
        self._invitee_domainid = None
        self.discriminator = None

        self.inviter_bcsid = inviter_bcsid
        self.inviter_projectid = inviter_projectid
        self.inviter_domainid = inviter_domainid
        self.inviter_username = inviter_username
        self.channel_name = channel_name
        self.invitee_bcsid = invitee_bcsid
        self.invitee_projectid = invitee_projectid
        self.invitee_domainid = invitee_domainid

    @property
    def inviter_bcsid(self):
        r"""Gets the inviter_bcsid of this QuitUnionFromMemberListRequestBody.

        邀请方BCS服务实例ID。可调用“查询服务实例列表”接口获取对应的ID

        :return: The inviter_bcsid of this QuitUnionFromMemberListRequestBody.
        :rtype: str
        """
        return self._inviter_bcsid

    @inviter_bcsid.setter
    def inviter_bcsid(self, inviter_bcsid):
        r"""Sets the inviter_bcsid of this QuitUnionFromMemberListRequestBody.

        邀请方BCS服务实例ID。可调用“查询服务实例列表”接口获取对应的ID

        :param inviter_bcsid: The inviter_bcsid of this QuitUnionFromMemberListRequestBody.
        :type inviter_bcsid: str
        """
        self._inviter_bcsid = inviter_bcsid

    @property
    def inviter_projectid(self):
        r"""Gets the inviter_projectid of this QuitUnionFromMemberListRequestBody.

        邀请方项目ID。控制台->邀请方帐号->我的凭证->API凭证->项目列表，选择对应的项目ID

        :return: The inviter_projectid of this QuitUnionFromMemberListRequestBody.
        :rtype: str
        """
        return self._inviter_projectid

    @inviter_projectid.setter
    def inviter_projectid(self, inviter_projectid):
        r"""Sets the inviter_projectid of this QuitUnionFromMemberListRequestBody.

        邀请方项目ID。控制台->邀请方帐号->我的凭证->API凭证->项目列表，选择对应的项目ID

        :param inviter_projectid: The inviter_projectid of this QuitUnionFromMemberListRequestBody.
        :type inviter_projectid: str
        """
        self._inviter_projectid = inviter_projectid

    @property
    def inviter_domainid(self):
        r"""Gets the inviter_domainid of this QuitUnionFromMemberListRequestBody.

        邀请方租户ID。控制台->邀请方帐号->我的凭证->API凭证->帐号ID

        :return: The inviter_domainid of this QuitUnionFromMemberListRequestBody.
        :rtype: str
        """
        return self._inviter_domainid

    @inviter_domainid.setter
    def inviter_domainid(self, inviter_domainid):
        r"""Sets the inviter_domainid of this QuitUnionFromMemberListRequestBody.

        邀请方租户ID。控制台->邀请方帐号->我的凭证->API凭证->帐号ID

        :param inviter_domainid: The inviter_domainid of this QuitUnionFromMemberListRequestBody.
        :type inviter_domainid: str
        """
        self._inviter_domainid = inviter_domainid

    @property
    def inviter_username(self):
        r"""Gets the inviter_username of this QuitUnionFromMemberListRequestBody.

        邀请方租户名称。控制台->邀请方帐号->我的凭证->API凭证->帐号名

        :return: The inviter_username of this QuitUnionFromMemberListRequestBody.
        :rtype: str
        """
        return self._inviter_username

    @inviter_username.setter
    def inviter_username(self, inviter_username):
        r"""Sets the inviter_username of this QuitUnionFromMemberListRequestBody.

        邀请方租户名称。控制台->邀请方帐号->我的凭证->API凭证->帐号名

        :param inviter_username: The inviter_username of this QuitUnionFromMemberListRequestBody.
        :type inviter_username: str
        """
        self._inviter_username = inviter_username

    @property
    def channel_name(self):
        r"""Gets the channel_name of this QuitUnionFromMemberListRequestBody.

        联盟通道名称。BCS管理面->成员管理->通道，选择对应的邀请的通道

        :return: The channel_name of this QuitUnionFromMemberListRequestBody.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        r"""Sets the channel_name of this QuitUnionFromMemberListRequestBody.

        联盟通道名称。BCS管理面->成员管理->通道，选择对应的邀请的通道

        :param channel_name: The channel_name of this QuitUnionFromMemberListRequestBody.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def invitee_bcsid(self):
        r"""Gets the invitee_bcsid of this QuitUnionFromMemberListRequestBody.

        被邀请方BCS服务实例ID。可调用“查询服务实例列表”接口获取对应的id

        :return: The invitee_bcsid of this QuitUnionFromMemberListRequestBody.
        :rtype: str
        """
        return self._invitee_bcsid

    @invitee_bcsid.setter
    def invitee_bcsid(self, invitee_bcsid):
        r"""Sets the invitee_bcsid of this QuitUnionFromMemberListRequestBody.

        被邀请方BCS服务实例ID。可调用“查询服务实例列表”接口获取对应的id

        :param invitee_bcsid: The invitee_bcsid of this QuitUnionFromMemberListRequestBody.
        :type invitee_bcsid: str
        """
        self._invitee_bcsid = invitee_bcsid

    @property
    def invitee_projectid(self):
        r"""Gets the invitee_projectid of this QuitUnionFromMemberListRequestBody.

        被邀请方项目ID。控制台->被邀请方帐号->我的凭证->API凭证->项目列表，选择对应的项目ID

        :return: The invitee_projectid of this QuitUnionFromMemberListRequestBody.
        :rtype: str
        """
        return self._invitee_projectid

    @invitee_projectid.setter
    def invitee_projectid(self, invitee_projectid):
        r"""Sets the invitee_projectid of this QuitUnionFromMemberListRequestBody.

        被邀请方项目ID。控制台->被邀请方帐号->我的凭证->API凭证->项目列表，选择对应的项目ID

        :param invitee_projectid: The invitee_projectid of this QuitUnionFromMemberListRequestBody.
        :type invitee_projectid: str
        """
        self._invitee_projectid = invitee_projectid

    @property
    def invitee_domainid(self):
        r"""Gets the invitee_domainid of this QuitUnionFromMemberListRequestBody.

        被邀请方租户ID。控制台->被邀请方帐号->我的凭证->API凭证->帐号ID

        :return: The invitee_domainid of this QuitUnionFromMemberListRequestBody.
        :rtype: str
        """
        return self._invitee_domainid

    @invitee_domainid.setter
    def invitee_domainid(self, invitee_domainid):
        r"""Sets the invitee_domainid of this QuitUnionFromMemberListRequestBody.

        被邀请方租户ID。控制台->被邀请方帐号->我的凭证->API凭证->帐号ID

        :param invitee_domainid: The invitee_domainid of this QuitUnionFromMemberListRequestBody.
        :type invitee_domainid: str
        """
        self._invitee_domainid = invitee_domainid

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
        if not isinstance(other, QuitUnionFromMemberListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
