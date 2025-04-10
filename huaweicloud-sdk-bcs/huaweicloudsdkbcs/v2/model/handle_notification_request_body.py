# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HandleNotificationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_name': 'str',
        'status': 'str',
        'invitor_info': 'HandleNotificationInvitor',
        'invitee_info': 'HandleNotificationInvitee',
        'invited_orgs': 'list[HandleNotificationOrg]'
    }

    attribute_map = {
        'channel_name': 'channel_name',
        'status': 'status',
        'invitor_info': 'invitor_info',
        'invitee_info': 'invitee_info',
        'invited_orgs': 'invited_orgs'
    }

    def __init__(self, channel_name=None, status=None, invitor_info=None, invitee_info=None, invited_orgs=None):
        r"""HandleNotificationRequestBody

        The model defined in huaweicloud sdk

        :param channel_name: 邀请目标通道
        :type channel_name: str
        :param status: 处理邀请
        :type status: str
        :param invitor_info: 
        :type invitor_info: :class:`huaweicloudsdkbcs.v2.HandleNotificationInvitor`
        :param invitee_info: 
        :type invitee_info: :class:`huaweicloudsdkbcs.v2.HandleNotificationInvitee`
        :param invited_orgs: 加入联盟的组织，同意加入时必填
        :type invited_orgs: list[:class:`huaweicloudsdkbcs.v2.HandleNotificationOrg`]
        """
        
        

        self._channel_name = None
        self._status = None
        self._invitor_info = None
        self._invitee_info = None
        self._invited_orgs = None
        self.discriminator = None

        self.channel_name = channel_name
        self.status = status
        self.invitor_info = invitor_info
        if invitee_info is not None:
            self.invitee_info = invitee_info
        if invited_orgs is not None:
            self.invited_orgs = invited_orgs

    @property
    def channel_name(self):
        r"""Gets the channel_name of this HandleNotificationRequestBody.

        邀请目标通道

        :return: The channel_name of this HandleNotificationRequestBody.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        r"""Sets the channel_name of this HandleNotificationRequestBody.

        邀请目标通道

        :param channel_name: The channel_name of this HandleNotificationRequestBody.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def status(self):
        r"""Gets the status of this HandleNotificationRequestBody.

        处理邀请

        :return: The status of this HandleNotificationRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HandleNotificationRequestBody.

        处理邀请

        :param status: The status of this HandleNotificationRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def invitor_info(self):
        r"""Gets the invitor_info of this HandleNotificationRequestBody.

        :return: The invitor_info of this HandleNotificationRequestBody.
        :rtype: :class:`huaweicloudsdkbcs.v2.HandleNotificationInvitor`
        """
        return self._invitor_info

    @invitor_info.setter
    def invitor_info(self, invitor_info):
        r"""Sets the invitor_info of this HandleNotificationRequestBody.

        :param invitor_info: The invitor_info of this HandleNotificationRequestBody.
        :type invitor_info: :class:`huaweicloudsdkbcs.v2.HandleNotificationInvitor`
        """
        self._invitor_info = invitor_info

    @property
    def invitee_info(self):
        r"""Gets the invitee_info of this HandleNotificationRequestBody.

        :return: The invitee_info of this HandleNotificationRequestBody.
        :rtype: :class:`huaweicloudsdkbcs.v2.HandleNotificationInvitee`
        """
        return self._invitee_info

    @invitee_info.setter
    def invitee_info(self, invitee_info):
        r"""Sets the invitee_info of this HandleNotificationRequestBody.

        :param invitee_info: The invitee_info of this HandleNotificationRequestBody.
        :type invitee_info: :class:`huaweicloudsdkbcs.v2.HandleNotificationInvitee`
        """
        self._invitee_info = invitee_info

    @property
    def invited_orgs(self):
        r"""Gets the invited_orgs of this HandleNotificationRequestBody.

        加入联盟的组织，同意加入时必填

        :return: The invited_orgs of this HandleNotificationRequestBody.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.HandleNotificationOrg`]
        """
        return self._invited_orgs

    @invited_orgs.setter
    def invited_orgs(self, invited_orgs):
        r"""Sets the invited_orgs of this HandleNotificationRequestBody.

        加入联盟的组织，同意加入时必填

        :param invited_orgs: The invited_orgs of this HandleNotificationRequestBody.
        :type invited_orgs: list[:class:`huaweicloudsdkbcs.v2.HandleNotificationOrg`]
        """
        self._invited_orgs = invited_orgs

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
        if not isinstance(other, HandleNotificationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
