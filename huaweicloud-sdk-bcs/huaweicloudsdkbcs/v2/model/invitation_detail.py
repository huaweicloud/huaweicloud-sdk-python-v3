# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InvitationDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'invited_user': 'str',
        'status': 'str',
        'invited_bcs_id': 'str'
    }

    attribute_map = {
        'invited_user': 'invited_user',
        'status': 'status',
        'invited_bcs_id': 'invited_bcs_id'
    }

    def __init__(self, invited_user=None, status=None, invited_bcs_id=None):
        r"""InvitationDetail

        The model defined in huaweicloud sdk

        :param invited_user: 被邀请方租户名，IAM用户名
        :type invited_user: str
        :param status: 邀请状态，可选：已退出（quit），等待中（waiting），已拒绝（reject），已解散（released），其他状态不允许删除
        :type status: str
        :param invited_bcs_id: 被邀请方服务实例ID
        :type invited_bcs_id: str
        """
        
        

        self._invited_user = None
        self._status = None
        self._invited_bcs_id = None
        self.discriminator = None

        self.invited_user = invited_user
        if status is not None:
            self.status = status
        if invited_bcs_id is not None:
            self.invited_bcs_id = invited_bcs_id

    @property
    def invited_user(self):
        r"""Gets the invited_user of this InvitationDetail.

        被邀请方租户名，IAM用户名

        :return: The invited_user of this InvitationDetail.
        :rtype: str
        """
        return self._invited_user

    @invited_user.setter
    def invited_user(self, invited_user):
        r"""Sets the invited_user of this InvitationDetail.

        被邀请方租户名，IAM用户名

        :param invited_user: The invited_user of this InvitationDetail.
        :type invited_user: str
        """
        self._invited_user = invited_user

    @property
    def status(self):
        r"""Gets the status of this InvitationDetail.

        邀请状态，可选：已退出（quit），等待中（waiting），已拒绝（reject），已解散（released），其他状态不允许删除

        :return: The status of this InvitationDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InvitationDetail.

        邀请状态，可选：已退出（quit），等待中（waiting），已拒绝（reject），已解散（released），其他状态不允许删除

        :param status: The status of this InvitationDetail.
        :type status: str
        """
        self._status = status

    @property
    def invited_bcs_id(self):
        r"""Gets the invited_bcs_id of this InvitationDetail.

        被邀请方服务实例ID

        :return: The invited_bcs_id of this InvitationDetail.
        :rtype: str
        """
        return self._invited_bcs_id

    @invited_bcs_id.setter
    def invited_bcs_id(self, invited_bcs_id):
        r"""Sets the invited_bcs_id of this InvitationDetail.

        被邀请方服务实例ID

        :param invited_bcs_id: The invited_bcs_id of this InvitationDetail.
        :type invited_bcs_id: str
        """
        self._invited_bcs_id = invited_bcs_id

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
        if not isinstance(other, InvitationDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
