# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RTCUserInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_type': 'str',
        'user_id': 'str',
        'signature': 'str',
        'ctime': 'int'
    }

    attribute_map = {
        'user_type': 'user_type',
        'user_id': 'user_id',
        'signature': 'signature',
        'ctime': 'ctime'
    }

    def __init__(self, user_type=None, user_id=None, signature=None, ctime=None):
        r"""RTCUserInfo

        The model defined in huaweicloud sdk

        :param user_type: 用户类型。 * CAPTURE: 直播助手，将摄像头获取视频流推送到RTC房间 * ANIMATION: VDS服务，从RTC房间拉视频流生成动作数据 * RENDER: 渲染服务，将动作数据渲染成数字人动画 * PLAYER: 普通观看方，可选择原始视频流或者数字人动画视频流观看 * INFERENCE_USER: 数字人推理端用户。从RTC房间接收音频流，并推送视频流到RTC房间 * END_USER: 端侧用户。从推送音频流到RTC房间，并从RTC房间接收视频流
        :type user_type: str
        :param user_id: RTC用户ID。
        :type user_id: str
        :param signature: RTC鉴权token。
        :type signature: str
        :param ctime: 有效期。时间戳，单位：秒。
        :type ctime: int
        """
        
        

        self._user_type = None
        self._user_id = None
        self._signature = None
        self._ctime = None
        self.discriminator = None

        if user_type is not None:
            self.user_type = user_type
        if user_id is not None:
            self.user_id = user_id
        if signature is not None:
            self.signature = signature
        if ctime is not None:
            self.ctime = ctime

    @property
    def user_type(self):
        r"""Gets the user_type of this RTCUserInfo.

        用户类型。 * CAPTURE: 直播助手，将摄像头获取视频流推送到RTC房间 * ANIMATION: VDS服务，从RTC房间拉视频流生成动作数据 * RENDER: 渲染服务，将动作数据渲染成数字人动画 * PLAYER: 普通观看方，可选择原始视频流或者数字人动画视频流观看 * INFERENCE_USER: 数字人推理端用户。从RTC房间接收音频流，并推送视频流到RTC房间 * END_USER: 端侧用户。从推送音频流到RTC房间，并从RTC房间接收视频流

        :return: The user_type of this RTCUserInfo.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        r"""Sets the user_type of this RTCUserInfo.

        用户类型。 * CAPTURE: 直播助手，将摄像头获取视频流推送到RTC房间 * ANIMATION: VDS服务，从RTC房间拉视频流生成动作数据 * RENDER: 渲染服务，将动作数据渲染成数字人动画 * PLAYER: 普通观看方，可选择原始视频流或者数字人动画视频流观看 * INFERENCE_USER: 数字人推理端用户。从RTC房间接收音频流，并推送视频流到RTC房间 * END_USER: 端侧用户。从推送音频流到RTC房间，并从RTC房间接收视频流

        :param user_type: The user_type of this RTCUserInfo.
        :type user_type: str
        """
        self._user_type = user_type

    @property
    def user_id(self):
        r"""Gets the user_id of this RTCUserInfo.

        RTC用户ID。

        :return: The user_id of this RTCUserInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this RTCUserInfo.

        RTC用户ID。

        :param user_id: The user_id of this RTCUserInfo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def signature(self):
        r"""Gets the signature of this RTCUserInfo.

        RTC鉴权token。

        :return: The signature of this RTCUserInfo.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        r"""Sets the signature of this RTCUserInfo.

        RTC鉴权token。

        :param signature: The signature of this RTCUserInfo.
        :type signature: str
        """
        self._signature = signature

    @property
    def ctime(self):
        r"""Gets the ctime of this RTCUserInfo.

        有效期。时间戳，单位：秒。

        :return: The ctime of this RTCUserInfo.
        :rtype: int
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        r"""Sets the ctime of this RTCUserInfo.

        有效期。时间戳，单位：秒。

        :param ctime: The ctime of this RTCUserInfo.
        :type ctime: int
        """
        self._ctime = ctime

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
        if not isinstance(other, RTCUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
