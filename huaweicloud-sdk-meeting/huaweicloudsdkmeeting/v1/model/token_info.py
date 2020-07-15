# coding: utf-8

import pprint
import re

import six





class TokenInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'token': 'str',
        'tmp_ws_token': 'str',
        'ws_url': 'str',
        'expire_time': 'int',
        'user_id': 'str',
        'org_id': 'str',
        'participant_id': 'str',
        'conf_token_expire_time': 'int',
        'vmr_current_conf_id': 'str',
        'support_notify_type': 'list[str]'
    }

    attribute_map = {
        'token': 'token',
        'tmp_ws_token': 'tmpWsToken',
        'ws_url': 'wsURL',
        'expire_time': 'expireTime',
        'user_id': 'userID',
        'org_id': 'orgID',
        'participant_id': 'participantID',
        'conf_token_expire_time': 'confTokenExpireTime',
        'vmr_current_conf_id': 'vmrCurrentConfID',
        'support_notify_type': 'supportNotifyType'
    }

    def __init__(self, token=None, tmp_ws_token=None, ws_url=None, expire_time=None, user_id=None, org_id=None, participant_id=None, conf_token_expire_time=None, vmr_current_conf_id=None, support_notify_type=None):
        """TokenInfo - a model defined in huaweicloud sdk"""
        
        

        self._token = None
        self._tmp_ws_token = None
        self._ws_url = None
        self._expire_time = None
        self._user_id = None
        self._org_id = None
        self._participant_id = None
        self._conf_token_expire_time = None
        self._vmr_current_conf_id = None
        self._support_notify_type = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if tmp_ws_token is not None:
            self.tmp_ws_token = tmp_ws_token
        if ws_url is not None:
            self.ws_url = ws_url
        if expire_time is not None:
            self.expire_time = expire_time
        if user_id is not None:
            self.user_id = user_id
        if org_id is not None:
            self.org_id = org_id
        if participant_id is not None:
            self.participant_id = participant_id
        if conf_token_expire_time is not None:
            self.conf_token_expire_time = conf_token_expire_time
        if vmr_current_conf_id is not None:
            self.vmr_current_conf_id = vmr_current_conf_id
        if support_notify_type is not None:
            self.support_notify_type = support_notify_type

    @property
    def token(self):
        """Gets the token of this TokenInfo.

        会控鉴权Token。

        :return: The token of this TokenInfo.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TokenInfo.

        会控鉴权Token。

        :param token: The token of this TokenInfo.
        :type: str
        """
        self._token = token

    @property
    def tmp_ws_token(self):
        """Gets the tmp_ws_token of this TokenInfo.

        websocket建链鉴权Token，成功时必带。

        :return: The tmp_ws_token of this TokenInfo.
        :rtype: str
        """
        return self._tmp_ws_token

    @tmp_ws_token.setter
    def tmp_ws_token(self, tmp_ws_token):
        """Sets the tmp_ws_token of this TokenInfo.

        websocket建链鉴权Token，成功时必带。

        :param tmp_ws_token: The tmp_ws_token of this TokenInfo.
        :type: str
        """
        self._tmp_ws_token = tmp_ws_token

    @property
    def ws_url(self):
        """Gets the ws_url of this TokenInfo.

        websocket建链URL。

        :return: The ws_url of this TokenInfo.
        :rtype: str
        """
        return self._ws_url

    @ws_url.setter
    def ws_url(self, ws_url):
        """Sets the ws_url of this TokenInfo.

        websocket建链URL。

        :param ws_url: The ws_url of this TokenInfo.
        :type: str
        """
        self._ws_url = ws_url

    @property
    def expire_time(self):
        """Gets the expire_time of this TokenInfo.

        会话过期时间。UTC时间毫秒数。

        :return: The expire_time of this TokenInfo.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this TokenInfo.

        会话过期时间。UTC时间毫秒数。

        :param expire_time: The expire_time of this TokenInfo.
        :type: int
        """
        self._expire_time = expire_time

    @property
    def user_id(self):
        """Gets the user_id of this TokenInfo.

        会议预定人ID。

        :return: The user_id of this TokenInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TokenInfo.

        会议预定人ID。

        :param user_id: The user_id of this TokenInfo.
        :type: str
        """
        self._user_id = user_id

    @property
    def org_id(self):
        """Gets the org_id of this TokenInfo.

        会议所属企业ID。

        :return: The org_id of this TokenInfo.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this TokenInfo.

        会议所属企业ID。

        :param org_id: The org_id of this TokenInfo.
        :type: str
        """
        self._org_id = org_id

    @property
    def participant_id(self):
        """Gets the participant_id of this TokenInfo.

        终端请求时，返回终端入会后会场ID。

        :return: The participant_id of this TokenInfo.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this TokenInfo.

        终端请求时，返回终端入会后会场ID。

        :param participant_id: The participant_id of this TokenInfo.
        :type: str
        """
        self._participant_id = participant_id

    @property
    def conf_token_expire_time(self):
        """Gets the conf_token_expire_time of this TokenInfo.

        会控token失效的时间。（单位秒）

        :return: The conf_token_expire_time of this TokenInfo.
        :rtype: int
        """
        return self._conf_token_expire_time

    @conf_token_expire_time.setter
    def conf_token_expire_time(self, conf_token_expire_time):
        """Sets the conf_token_expire_time of this TokenInfo.

        会控token失效的时间。（单位秒）

        :param conf_token_expire_time: The conf_token_expire_time of this TokenInfo.
        :type: int
        """
        self._conf_token_expire_time = conf_token_expire_time

    @property
    def vmr_current_conf_id(self):
        """Gets the vmr_current_conf_id of this TokenInfo.

        云会议室会议的当前会议ID。

        :return: The vmr_current_conf_id of this TokenInfo.
        :rtype: str
        """
        return self._vmr_current_conf_id

    @vmr_current_conf_id.setter
    def vmr_current_conf_id(self, vmr_current_conf_id):
        """Sets the vmr_current_conf_id of this TokenInfo.

        云会议室会议的当前会议ID。

        :param vmr_current_conf_id: The vmr_current_conf_id of this TokenInfo.
        :type: str
        """
        self._vmr_current_conf_id = vmr_current_conf_id

    @property
    def support_notify_type(self):
        """Gets the support_notify_type of this TokenInfo.

        websocket消息推送支持类型。

        :return: The support_notify_type of this TokenInfo.
        :rtype: list[str]
        """
        return self._support_notify_type

    @support_notify_type.setter
    def support_notify_type(self, support_notify_type):
        """Sets the support_notify_type of this TokenInfo.

        websocket消息推送支持类型。

        :param support_notify_type: The support_notify_type of this TokenInfo.
        :type: list[str]
        """
        self._support_notify_type = support_notify_type

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
        if not isinstance(other, TokenInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
