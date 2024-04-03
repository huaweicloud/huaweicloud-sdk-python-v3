# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDesktopRemoteAssistanceInfoResponse(SdkResponse):

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
        'invitation_code': 'str',
        'share_space_name': 'str',
        'share_space_passwd': 'str',
        'private_share_link': 'str',
        'internet_share_link': 'str',
        'create_time': 'str',
        'status': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'share_space_id': 'share_space_id',
        'invitation_code': 'invitation_code',
        'share_space_name': 'share_space_name',
        'share_space_passwd': 'share_space_passwd',
        'private_share_link': 'private_share_link',
        'internet_share_link': 'internet_share_link',
        'create_time': 'create_time',
        'status': 'status',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, share_space_id=None, invitation_code=None, share_space_name=None, share_space_passwd=None, private_share_link=None, internet_share_link=None, create_time=None, status=None, failed_reason=None):
        """ShowDesktopRemoteAssistanceInfoResponse

        The model defined in huaweicloud sdk

        :param share_space_id: 协同空间ID
        :type share_space_id: str
        :param invitation_code: 协同空间邀请码(大写英文+数字,共8位)
        :type invitation_code: str
        :param share_space_name: 协同空间名称
        :type share_space_name: str
        :param share_space_passwd: 协同空间密码
        :type share_space_passwd: str
        :param private_share_link: 专线分享链接
        :type private_share_link: str
        :param internet_share_link: 互联网分享链接
        :type internet_share_link: str
        :param create_time: 创建时间 UTC时间，格式为：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;。
        :type create_time: str
        :param status: 协同空间状态 - OPEN 协同空间已创建 - CLOSE 协同空间已关闭 - WAIT_USER_CONFIRM 等待用户确认进入远程协助 - WAIT_USER_ACCESS 等待用户进入远程协助
        :type status: str
        :param failed_reason: 失败原因
        :type failed_reason: str
        """
        
        super(ShowDesktopRemoteAssistanceInfoResponse, self).__init__()

        self._share_space_id = None
        self._invitation_code = None
        self._share_space_name = None
        self._share_space_passwd = None
        self._private_share_link = None
        self._internet_share_link = None
        self._create_time = None
        self._status = None
        self._failed_reason = None
        self.discriminator = None

        if share_space_id is not None:
            self.share_space_id = share_space_id
        if invitation_code is not None:
            self.invitation_code = invitation_code
        if share_space_name is not None:
            self.share_space_name = share_space_name
        if share_space_passwd is not None:
            self.share_space_passwd = share_space_passwd
        if private_share_link is not None:
            self.private_share_link = private_share_link
        if internet_share_link is not None:
            self.internet_share_link = internet_share_link
        if create_time is not None:
            self.create_time = create_time
        if status is not None:
            self.status = status
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def share_space_id(self):
        """Gets the share_space_id of this ShowDesktopRemoteAssistanceInfoResponse.

        协同空间ID

        :return: The share_space_id of this ShowDesktopRemoteAssistanceInfoResponse.
        :rtype: str
        """
        return self._share_space_id

    @share_space_id.setter
    def share_space_id(self, share_space_id):
        """Sets the share_space_id of this ShowDesktopRemoteAssistanceInfoResponse.

        协同空间ID

        :param share_space_id: The share_space_id of this ShowDesktopRemoteAssistanceInfoResponse.
        :type share_space_id: str
        """
        self._share_space_id = share_space_id

    @property
    def invitation_code(self):
        """Gets the invitation_code of this ShowDesktopRemoteAssistanceInfoResponse.

        协同空间邀请码(大写英文+数字,共8位)

        :return: The invitation_code of this ShowDesktopRemoteAssistanceInfoResponse.
        :rtype: str
        """
        return self._invitation_code

    @invitation_code.setter
    def invitation_code(self, invitation_code):
        """Sets the invitation_code of this ShowDesktopRemoteAssistanceInfoResponse.

        协同空间邀请码(大写英文+数字,共8位)

        :param invitation_code: The invitation_code of this ShowDesktopRemoteAssistanceInfoResponse.
        :type invitation_code: str
        """
        self._invitation_code = invitation_code

    @property
    def share_space_name(self):
        """Gets the share_space_name of this ShowDesktopRemoteAssistanceInfoResponse.

        协同空间名称

        :return: The share_space_name of this ShowDesktopRemoteAssistanceInfoResponse.
        :rtype: str
        """
        return self._share_space_name

    @share_space_name.setter
    def share_space_name(self, share_space_name):
        """Sets the share_space_name of this ShowDesktopRemoteAssistanceInfoResponse.

        协同空间名称

        :param share_space_name: The share_space_name of this ShowDesktopRemoteAssistanceInfoResponse.
        :type share_space_name: str
        """
        self._share_space_name = share_space_name

    @property
    def share_space_passwd(self):
        """Gets the share_space_passwd of this ShowDesktopRemoteAssistanceInfoResponse.

        协同空间密码

        :return: The share_space_passwd of this ShowDesktopRemoteAssistanceInfoResponse.
        :rtype: str
        """
        return self._share_space_passwd

    @share_space_passwd.setter
    def share_space_passwd(self, share_space_passwd):
        """Sets the share_space_passwd of this ShowDesktopRemoteAssistanceInfoResponse.

        协同空间密码

        :param share_space_passwd: The share_space_passwd of this ShowDesktopRemoteAssistanceInfoResponse.
        :type share_space_passwd: str
        """
        self._share_space_passwd = share_space_passwd

    @property
    def private_share_link(self):
        """Gets the private_share_link of this ShowDesktopRemoteAssistanceInfoResponse.

        专线分享链接

        :return: The private_share_link of this ShowDesktopRemoteAssistanceInfoResponse.
        :rtype: str
        """
        return self._private_share_link

    @private_share_link.setter
    def private_share_link(self, private_share_link):
        """Sets the private_share_link of this ShowDesktopRemoteAssistanceInfoResponse.

        专线分享链接

        :param private_share_link: The private_share_link of this ShowDesktopRemoteAssistanceInfoResponse.
        :type private_share_link: str
        """
        self._private_share_link = private_share_link

    @property
    def internet_share_link(self):
        """Gets the internet_share_link of this ShowDesktopRemoteAssistanceInfoResponse.

        互联网分享链接

        :return: The internet_share_link of this ShowDesktopRemoteAssistanceInfoResponse.
        :rtype: str
        """
        return self._internet_share_link

    @internet_share_link.setter
    def internet_share_link(self, internet_share_link):
        """Sets the internet_share_link of this ShowDesktopRemoteAssistanceInfoResponse.

        互联网分享链接

        :param internet_share_link: The internet_share_link of this ShowDesktopRemoteAssistanceInfoResponse.
        :type internet_share_link: str
        """
        self._internet_share_link = internet_share_link

    @property
    def create_time(self):
        """Gets the create_time of this ShowDesktopRemoteAssistanceInfoResponse.

        创建时间 UTC时间，格式为：yyyy-MM-dd'T'HH:mm:ss'Z'。

        :return: The create_time of this ShowDesktopRemoteAssistanceInfoResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowDesktopRemoteAssistanceInfoResponse.

        创建时间 UTC时间，格式为：yyyy-MM-dd'T'HH:mm:ss'Z'。

        :param create_time: The create_time of this ShowDesktopRemoteAssistanceInfoResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def status(self):
        """Gets the status of this ShowDesktopRemoteAssistanceInfoResponse.

        协同空间状态 - OPEN 协同空间已创建 - CLOSE 协同空间已关闭 - WAIT_USER_CONFIRM 等待用户确认进入远程协助 - WAIT_USER_ACCESS 等待用户进入远程协助

        :return: The status of this ShowDesktopRemoteAssistanceInfoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDesktopRemoteAssistanceInfoResponse.

        协同空间状态 - OPEN 协同空间已创建 - CLOSE 协同空间已关闭 - WAIT_USER_CONFIRM 等待用户确认进入远程协助 - WAIT_USER_ACCESS 等待用户进入远程协助

        :param status: The status of this ShowDesktopRemoteAssistanceInfoResponse.
        :type status: str
        """
        self._status = status

    @property
    def failed_reason(self):
        """Gets the failed_reason of this ShowDesktopRemoteAssistanceInfoResponse.

        失败原因

        :return: The failed_reason of this ShowDesktopRemoteAssistanceInfoResponse.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this ShowDesktopRemoteAssistanceInfoResponse.

        失败原因

        :param failed_reason: The failed_reason of this ShowDesktopRemoteAssistanceInfoResponse.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

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
        if not isinstance(other, ShowDesktopRemoteAssistanceInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
