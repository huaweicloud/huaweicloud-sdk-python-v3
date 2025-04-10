# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'role': 'int',
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
        'role': 'role',
        'expire_time': 'expireTime',
        'user_id': 'userID',
        'org_id': 'orgID',
        'participant_id': 'participantID',
        'conf_token_expire_time': 'confTokenExpireTime',
        'vmr_current_conf_id': 'vmrCurrentConfID',
        'support_notify_type': 'supportNotifyType'
    }

    def __init__(self, token=None, tmp_ws_token=None, ws_url=None, role=None, expire_time=None, user_id=None, org_id=None, participant_id=None, conf_token_expire_time=None, vmr_current_conf_id=None, support_notify_type=None):
        r"""TokenInfo

        The model defined in huaweicloud sdk

        :param token: 会控Token。有效期半个小时。
        :type token: str
        :param tmp_ws_token: 会控WebSocket建链鉴权Token。
        :type tmp_ws_token: str
        :param ws_url: 会控WebSocket建链URL。
        :type ws_url: str
        :param role: 会议中的角色。 * 0 ：普通与会者 * 1 ：会议主持人 
        :type role: int
        :param expire_time: 会控Token过期时间戳（单位：毫秒）。
        :type expire_time: int
        :param user_id: 会议预定者的用户UUID。
        :type user_id: str
        :param org_id: 会议所属企业ID。
        :type org_id: str
        :param participant_id: 终端请求时，返回终端入会后会场ID。 &gt; 该参数将废弃，请勿使用。 
        :type participant_id: str
        :param conf_token_expire_time: 会控Token有效时长（单位秒）。
        :type conf_token_expire_time: int
        :param vmr_current_conf_id: 云会议室会议的当前会议ID。
        :type vmr_current_conf_id: str
        :param support_notify_type: 会控WebSocket消息推送支持类型。
        :type support_notify_type: list[str]
        """
        
        

        self._token = None
        self._tmp_ws_token = None
        self._ws_url = None
        self._role = None
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
        if role is not None:
            self.role = role
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
        r"""Gets the token of this TokenInfo.

        会控Token。有效期半个小时。

        :return: The token of this TokenInfo.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this TokenInfo.

        会控Token。有效期半个小时。

        :param token: The token of this TokenInfo.
        :type token: str
        """
        self._token = token

    @property
    def tmp_ws_token(self):
        r"""Gets the tmp_ws_token of this TokenInfo.

        会控WebSocket建链鉴权Token。

        :return: The tmp_ws_token of this TokenInfo.
        :rtype: str
        """
        return self._tmp_ws_token

    @tmp_ws_token.setter
    def tmp_ws_token(self, tmp_ws_token):
        r"""Sets the tmp_ws_token of this TokenInfo.

        会控WebSocket建链鉴权Token。

        :param tmp_ws_token: The tmp_ws_token of this TokenInfo.
        :type tmp_ws_token: str
        """
        self._tmp_ws_token = tmp_ws_token

    @property
    def ws_url(self):
        r"""Gets the ws_url of this TokenInfo.

        会控WebSocket建链URL。

        :return: The ws_url of this TokenInfo.
        :rtype: str
        """
        return self._ws_url

    @ws_url.setter
    def ws_url(self, ws_url):
        r"""Sets the ws_url of this TokenInfo.

        会控WebSocket建链URL。

        :param ws_url: The ws_url of this TokenInfo.
        :type ws_url: str
        """
        self._ws_url = ws_url

    @property
    def role(self):
        r"""Gets the role of this TokenInfo.

        会议中的角色。 * 0 ：普通与会者 * 1 ：会议主持人 

        :return: The role of this TokenInfo.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this TokenInfo.

        会议中的角色。 * 0 ：普通与会者 * 1 ：会议主持人 

        :param role: The role of this TokenInfo.
        :type role: int
        """
        self._role = role

    @property
    def expire_time(self):
        r"""Gets the expire_time of this TokenInfo.

        会控Token过期时间戳（单位：毫秒）。

        :return: The expire_time of this TokenInfo.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this TokenInfo.

        会控Token过期时间戳（单位：毫秒）。

        :param expire_time: The expire_time of this TokenInfo.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def user_id(self):
        r"""Gets the user_id of this TokenInfo.

        会议预定者的用户UUID。

        :return: The user_id of this TokenInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this TokenInfo.

        会议预定者的用户UUID。

        :param user_id: The user_id of this TokenInfo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def org_id(self):
        r"""Gets the org_id of this TokenInfo.

        会议所属企业ID。

        :return: The org_id of this TokenInfo.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        r"""Sets the org_id of this TokenInfo.

        会议所属企业ID。

        :param org_id: The org_id of this TokenInfo.
        :type org_id: str
        """
        self._org_id = org_id

    @property
    def participant_id(self):
        r"""Gets the participant_id of this TokenInfo.

        终端请求时，返回终端入会后会场ID。 > 该参数将废弃，请勿使用。 

        :return: The participant_id of this TokenInfo.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        r"""Sets the participant_id of this TokenInfo.

        终端请求时，返回终端入会后会场ID。 > 该参数将废弃，请勿使用。 

        :param participant_id: The participant_id of this TokenInfo.
        :type participant_id: str
        """
        self._participant_id = participant_id

    @property
    def conf_token_expire_time(self):
        r"""Gets the conf_token_expire_time of this TokenInfo.

        会控Token有效时长（单位秒）。

        :return: The conf_token_expire_time of this TokenInfo.
        :rtype: int
        """
        return self._conf_token_expire_time

    @conf_token_expire_time.setter
    def conf_token_expire_time(self, conf_token_expire_time):
        r"""Sets the conf_token_expire_time of this TokenInfo.

        会控Token有效时长（单位秒）。

        :param conf_token_expire_time: The conf_token_expire_time of this TokenInfo.
        :type conf_token_expire_time: int
        """
        self._conf_token_expire_time = conf_token_expire_time

    @property
    def vmr_current_conf_id(self):
        r"""Gets the vmr_current_conf_id of this TokenInfo.

        云会议室会议的当前会议ID。

        :return: The vmr_current_conf_id of this TokenInfo.
        :rtype: str
        """
        return self._vmr_current_conf_id

    @vmr_current_conf_id.setter
    def vmr_current_conf_id(self, vmr_current_conf_id):
        r"""Sets the vmr_current_conf_id of this TokenInfo.

        云会议室会议的当前会议ID。

        :param vmr_current_conf_id: The vmr_current_conf_id of this TokenInfo.
        :type vmr_current_conf_id: str
        """
        self._vmr_current_conf_id = vmr_current_conf_id

    @property
    def support_notify_type(self):
        r"""Gets the support_notify_type of this TokenInfo.

        会控WebSocket消息推送支持类型。

        :return: The support_notify_type of this TokenInfo.
        :rtype: list[str]
        """
        return self._support_notify_type

    @support_notify_type.setter
    def support_notify_type(self, support_notify_type):
        r"""Sets the support_notify_type of this TokenInfo.

        会控WebSocket消息推送支持类型。

        :param support_notify_type: The support_notify_type of this TokenInfo.
        :type support_notify_type: list[str]
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
        if not isinstance(other, TokenInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
