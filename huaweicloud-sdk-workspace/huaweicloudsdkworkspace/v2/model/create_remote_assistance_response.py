# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRemoteAssistanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_space_id': 'str',
        'status': 'str',
        'desktop_id': 'str',
        'initiator_type': 'str'
    }

    attribute_map = {
        'share_space_id': 'share_space_id',
        'status': 'status',
        'desktop_id': 'desktop_id',
        'initiator_type': 'initiator_type'
    }

    def __init__(self, share_space_id=None, status=None, desktop_id=None, initiator_type=None):
        """CreateRemoteAssistanceResponse

        The model defined in huaweicloud sdk

        :param share_space_id: 协同空间ID
        :type share_space_id: str
        :param status: 协同空间状态 - OPEN 协同空间已创建 - CLOSE 协同空间已关闭 - WAIT_USER_CONFIRM 等待用户确认进入远程协助 - WAIT_USER_ACCESS 等待用户进入远程协助
        :type status: str
        :param desktop_id: 桌面的desktopId
        :type desktop_id: str
        :param initiator_type: 发起方类型 - ADMIN_INITIATE 管理员发起 - ENDUSER_INITIATE 终端用户发起
        :type initiator_type: str
        """
        
        super(CreateRemoteAssistanceResponse, self).__init__()

        self._share_space_id = None
        self._status = None
        self._desktop_id = None
        self._initiator_type = None
        self.discriminator = None

        if share_space_id is not None:
            self.share_space_id = share_space_id
        if status is not None:
            self.status = status
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if initiator_type is not None:
            self.initiator_type = initiator_type

    @property
    def share_space_id(self):
        """Gets the share_space_id of this CreateRemoteAssistanceResponse.

        协同空间ID

        :return: The share_space_id of this CreateRemoteAssistanceResponse.
        :rtype: str
        """
        return self._share_space_id

    @share_space_id.setter
    def share_space_id(self, share_space_id):
        """Sets the share_space_id of this CreateRemoteAssistanceResponse.

        协同空间ID

        :param share_space_id: The share_space_id of this CreateRemoteAssistanceResponse.
        :type share_space_id: str
        """
        self._share_space_id = share_space_id

    @property
    def status(self):
        """Gets the status of this CreateRemoteAssistanceResponse.

        协同空间状态 - OPEN 协同空间已创建 - CLOSE 协同空间已关闭 - WAIT_USER_CONFIRM 等待用户确认进入远程协助 - WAIT_USER_ACCESS 等待用户进入远程协助

        :return: The status of this CreateRemoteAssistanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateRemoteAssistanceResponse.

        协同空间状态 - OPEN 协同空间已创建 - CLOSE 协同空间已关闭 - WAIT_USER_CONFIRM 等待用户确认进入远程协助 - WAIT_USER_ACCESS 等待用户进入远程协助

        :param status: The status of this CreateRemoteAssistanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def desktop_id(self):
        """Gets the desktop_id of this CreateRemoteAssistanceResponse.

        桌面的desktopId

        :return: The desktop_id of this CreateRemoteAssistanceResponse.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this CreateRemoteAssistanceResponse.

        桌面的desktopId

        :param desktop_id: The desktop_id of this CreateRemoteAssistanceResponse.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def initiator_type(self):
        """Gets the initiator_type of this CreateRemoteAssistanceResponse.

        发起方类型 - ADMIN_INITIATE 管理员发起 - ENDUSER_INITIATE 终端用户发起

        :return: The initiator_type of this CreateRemoteAssistanceResponse.
        :rtype: str
        """
        return self._initiator_type

    @initiator_type.setter
    def initiator_type(self, initiator_type):
        """Sets the initiator_type of this CreateRemoteAssistanceResponse.

        发起方类型 - ADMIN_INITIATE 管理员发起 - ENDUSER_INITIATE 终端用户发起

        :param initiator_type: The initiator_type of this CreateRemoteAssistanceResponse.
        :type initiator_type: str
        """
        self._initiator_type = initiator_type

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
        if not isinstance(other, CreateRemoteAssistanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
