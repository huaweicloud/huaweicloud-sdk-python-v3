# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberInvitee:

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
        'invitee_user_id': 'str',
        'invitee_username': 'str'
    }

    attribute_map = {
        'invitee_bcs_id': 'invitee_bcs_id',
        'invitee_user_id': 'invitee_user_id',
        'invitee_username': 'invitee_username'
    }

    def __init__(self, invitee_bcs_id=None, invitee_user_id=None, invitee_username=None):
        """MemberInvitee

        The model defined in huaweicloud sdk

        :param invitee_bcs_id: 被邀请方BCS服务实例ID
        :type invitee_bcs_id: str
        :param invitee_user_id: 被邀请方租户id
        :type invitee_user_id: str
        :param invitee_username: 被邀请方租户名
        :type invitee_username: str
        """
        
        

        self._invitee_bcs_id = None
        self._invitee_user_id = None
        self._invitee_username = None
        self.discriminator = None

        if invitee_bcs_id is not None:
            self.invitee_bcs_id = invitee_bcs_id
        if invitee_user_id is not None:
            self.invitee_user_id = invitee_user_id
        if invitee_username is not None:
            self.invitee_username = invitee_username

    @property
    def invitee_bcs_id(self):
        """Gets the invitee_bcs_id of this MemberInvitee.

        被邀请方BCS服务实例ID

        :return: The invitee_bcs_id of this MemberInvitee.
        :rtype: str
        """
        return self._invitee_bcs_id

    @invitee_bcs_id.setter
    def invitee_bcs_id(self, invitee_bcs_id):
        """Sets the invitee_bcs_id of this MemberInvitee.

        被邀请方BCS服务实例ID

        :param invitee_bcs_id: The invitee_bcs_id of this MemberInvitee.
        :type invitee_bcs_id: str
        """
        self._invitee_bcs_id = invitee_bcs_id

    @property
    def invitee_user_id(self):
        """Gets the invitee_user_id of this MemberInvitee.

        被邀请方租户id

        :return: The invitee_user_id of this MemberInvitee.
        :rtype: str
        """
        return self._invitee_user_id

    @invitee_user_id.setter
    def invitee_user_id(self, invitee_user_id):
        """Sets the invitee_user_id of this MemberInvitee.

        被邀请方租户id

        :param invitee_user_id: The invitee_user_id of this MemberInvitee.
        :type invitee_user_id: str
        """
        self._invitee_user_id = invitee_user_id

    @property
    def invitee_username(self):
        """Gets the invitee_username of this MemberInvitee.

        被邀请方租户名

        :return: The invitee_username of this MemberInvitee.
        :rtype: str
        """
        return self._invitee_username

    @invitee_username.setter
    def invitee_username(self, invitee_username):
        """Sets the invitee_username of this MemberInvitee.

        被邀请方租户名

        :param invitee_username: The invitee_username of this MemberInvitee.
        :type invitee_username: str
        """
        self._invitee_username = invitee_username

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
        if not isinstance(other, MemberInvitee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
