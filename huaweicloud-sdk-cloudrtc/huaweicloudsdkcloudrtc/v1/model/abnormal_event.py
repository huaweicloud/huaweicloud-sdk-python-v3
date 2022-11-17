# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AbnormalEvent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'uid': 'str',
        'room_id': 'str',
        'stage': 'str',
        'location': 'str',
        'peer_uid': 'str',
        'abnormal_type': 'int',
        'abnormal_type_desc': 'str',
        'abnormal_factor': 'int',
        'abnormal_factor_desc': 'str'
    }

    attribute_map = {
        'time': 'time',
        'uid': 'uid',
        'room_id': 'room_id',
        'stage': 'stage',
        'location': 'location',
        'peer_uid': 'peer_uid',
        'abnormal_type': 'abnormal_type',
        'abnormal_type_desc': 'abnormal_type_desc',
        'abnormal_factor': 'abnormal_factor',
        'abnormal_factor_desc': 'abnormal_factor_desc'
    }

    def __init__(self, time=None, uid=None, room_id=None, stage=None, location=None, peer_uid=None, abnormal_type=None, abnormal_type_desc=None, abnormal_factor=None, abnormal_factor_desc=None):
        """AbnormalEvent

        The model defined in huaweicloud sdk

        :param time: 采样时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为YYYY-MM-DDThh:mm:ssZ
        :type time: str
        :param uid: 出现异常的用户ID
        :type uid: str
        :param room_id: 出现异常的房间ID
        :type room_id: str
        :param stage: 出现异常的环节 - join_room：加入房间 - communication：通话中 
        :type stage: str
        :param location: 事件发生位置 - local：事件发生在客户端本地 - remote：事件发生在远端 
        :type location: str
        :param peer_uid: 如果根因来自远端用户，则peerid为远端用户的用户ID。如果根因来自自身，则peerid为空字符串
        :type peer_uid: str
        :param abnormal_type: 异常类型： - 1：进房慢(5s加入房间失败) - 2：视频卡顿 - 3：音频卡顿 
        :type abnormal_type: int
        :param abnormal_type_desc: 异常类型描述与异常类型对应，支持国际化，取值范围为： - 进房慢(5s加入房间失败) - 视频卡顿 - 音频卡顿 
        :type abnormal_type_desc: str
        :param abnormal_factor: 异常因素 当异常类型为1时，异常因素取值范围为： - 1：建链失败 - 2：房间非空闲 - 3：服务器异常 - 4：服务器反馈503 - 5：鉴权失败 - 6：鉴权重试 - 7：时钟同步失败 - 8：url错误 - 9：终端内部异常 - 90000004：SDK发出的加入房间信令响应超时 - 90100009：web侧没有收到MSP下发的配置信息 - 90100008：websocket链路建链失败 - 10000001：服务侧返回的异常信息 - 31000003：服务侧返回的异常信息 - 32000030：服务侧返回的异常信息 - 15：浏览器设置sdp异常 当异常类型为2或者3时，异常因素取值范围为： - 1：系统CPU占用高 - 2：App CPU占用高 - 3：音频上行网络延时 - 4：音频上行网络抖动 - 5：视频上行网络延时 - 6：视频上行网络抖动 - 7：音频下行网络延时 - 8：音频下行网络抖动 - 9：视频下行网络延时 - 10：视频下行网络抖动 - 11：上行音频丢包 - 12：上行视频丢包 - 13：下行音频丢包 - 14：下行视频丢包 - 15：下行音频无声音 - 16：其他 - 17：对端用户离线 - 18：对端用户无码流 - 19：对端用户无帧率 - 20：本端服务器下行无码流 - 21：本端服务器下行无帧率 
        :type abnormal_factor: int
        :param abnormal_factor_desc: 异常因素描述，支持国际化 当异常类型为1时，异常因素描述与异常因素对应，取值范围为： - 建链失败 - 房间非空闲 - 服务器异常 - 服务器反馈503 - 鉴权失败 - 鉴权重试 - 时钟同步失败 - url错误 - 终端内部异常 - SDK发出的加入房间信令响应超时 - web侧没有收到MSP下发的配置信息 - websocket链路建链失败 - 服务侧返回的异常信息 - 服务侧返回的异常信息 - 服务侧返回的异常信息 - 浏览器设置sdp异常 当异常类型为2或者3时，异常因素描述与异常因素对应，取值范围为： - 系统CPU占用高 - App CPU占用高 - 音频上行网络延时 - 音频上行网络抖动 - 视频上行网络延时 - 视频上行网络抖动 - 音频下行网络延时 - 音频下行网络抖动 - 视频下行网络延时 - 视频下行网络抖动 - 上行音频丢包 - 上行视频丢包 - 下行音频丢包 - 下行视频丢包 - 下行音频无声音 - 其他 - 对端用户离线 - 对端用户无码流 - 对端用户无帧率 - 本端服务器下行无码流 - 本端服务器下行无帧率 其他情况，异常因素描述为：其他 
        :type abnormal_factor_desc: str
        """
        
        

        self._time = None
        self._uid = None
        self._room_id = None
        self._stage = None
        self._location = None
        self._peer_uid = None
        self._abnormal_type = None
        self._abnormal_type_desc = None
        self._abnormal_factor = None
        self._abnormal_factor_desc = None
        self.discriminator = None

        self.time = time
        self.uid = uid
        self.room_id = room_id
        self.stage = stage
        self.location = location
        self.peer_uid = peer_uid
        self.abnormal_type = abnormal_type
        self.abnormal_type_desc = abnormal_type_desc
        self.abnormal_factor = abnormal_factor
        self.abnormal_factor_desc = abnormal_factor_desc

    @property
    def time(self):
        """Gets the time of this AbnormalEvent.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为YYYY-MM-DDThh:mm:ssZ

        :return: The time of this AbnormalEvent.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this AbnormalEvent.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为YYYY-MM-DDThh:mm:ssZ

        :param time: The time of this AbnormalEvent.
        :type time: str
        """
        self._time = time

    @property
    def uid(self):
        """Gets the uid of this AbnormalEvent.

        出现异常的用户ID

        :return: The uid of this AbnormalEvent.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AbnormalEvent.

        出现异常的用户ID

        :param uid: The uid of this AbnormalEvent.
        :type uid: str
        """
        self._uid = uid

    @property
    def room_id(self):
        """Gets the room_id of this AbnormalEvent.

        出现异常的房间ID

        :return: The room_id of this AbnormalEvent.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this AbnormalEvent.

        出现异常的房间ID

        :param room_id: The room_id of this AbnormalEvent.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def stage(self):
        """Gets the stage of this AbnormalEvent.

        出现异常的环节 - join_room：加入房间 - communication：通话中 

        :return: The stage of this AbnormalEvent.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this AbnormalEvent.

        出现异常的环节 - join_room：加入房间 - communication：通话中 

        :param stage: The stage of this AbnormalEvent.
        :type stage: str
        """
        self._stage = stage

    @property
    def location(self):
        """Gets the location of this AbnormalEvent.

        事件发生位置 - local：事件发生在客户端本地 - remote：事件发生在远端 

        :return: The location of this AbnormalEvent.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AbnormalEvent.

        事件发生位置 - local：事件发生在客户端本地 - remote：事件发生在远端 

        :param location: The location of this AbnormalEvent.
        :type location: str
        """
        self._location = location

    @property
    def peer_uid(self):
        """Gets the peer_uid of this AbnormalEvent.

        如果根因来自远端用户，则peerid为远端用户的用户ID。如果根因来自自身，则peerid为空字符串

        :return: The peer_uid of this AbnormalEvent.
        :rtype: str
        """
        return self._peer_uid

    @peer_uid.setter
    def peer_uid(self, peer_uid):
        """Sets the peer_uid of this AbnormalEvent.

        如果根因来自远端用户，则peerid为远端用户的用户ID。如果根因来自自身，则peerid为空字符串

        :param peer_uid: The peer_uid of this AbnormalEvent.
        :type peer_uid: str
        """
        self._peer_uid = peer_uid

    @property
    def abnormal_type(self):
        """Gets the abnormal_type of this AbnormalEvent.

        异常类型： - 1：进房慢(5s加入房间失败) - 2：视频卡顿 - 3：音频卡顿 

        :return: The abnormal_type of this AbnormalEvent.
        :rtype: int
        """
        return self._abnormal_type

    @abnormal_type.setter
    def abnormal_type(self, abnormal_type):
        """Sets the abnormal_type of this AbnormalEvent.

        异常类型： - 1：进房慢(5s加入房间失败) - 2：视频卡顿 - 3：音频卡顿 

        :param abnormal_type: The abnormal_type of this AbnormalEvent.
        :type abnormal_type: int
        """
        self._abnormal_type = abnormal_type

    @property
    def abnormal_type_desc(self):
        """Gets the abnormal_type_desc of this AbnormalEvent.

        异常类型描述与异常类型对应，支持国际化，取值范围为： - 进房慢(5s加入房间失败) - 视频卡顿 - 音频卡顿 

        :return: The abnormal_type_desc of this AbnormalEvent.
        :rtype: str
        """
        return self._abnormal_type_desc

    @abnormal_type_desc.setter
    def abnormal_type_desc(self, abnormal_type_desc):
        """Sets the abnormal_type_desc of this AbnormalEvent.

        异常类型描述与异常类型对应，支持国际化，取值范围为： - 进房慢(5s加入房间失败) - 视频卡顿 - 音频卡顿 

        :param abnormal_type_desc: The abnormal_type_desc of this AbnormalEvent.
        :type abnormal_type_desc: str
        """
        self._abnormal_type_desc = abnormal_type_desc

    @property
    def abnormal_factor(self):
        """Gets the abnormal_factor of this AbnormalEvent.

        异常因素 当异常类型为1时，异常因素取值范围为： - 1：建链失败 - 2：房间非空闲 - 3：服务器异常 - 4：服务器反馈503 - 5：鉴权失败 - 6：鉴权重试 - 7：时钟同步失败 - 8：url错误 - 9：终端内部异常 - 90000004：SDK发出的加入房间信令响应超时 - 90100009：web侧没有收到MSP下发的配置信息 - 90100008：websocket链路建链失败 - 10000001：服务侧返回的异常信息 - 31000003：服务侧返回的异常信息 - 32000030：服务侧返回的异常信息 - 15：浏览器设置sdp异常 当异常类型为2或者3时，异常因素取值范围为： - 1：系统CPU占用高 - 2：App CPU占用高 - 3：音频上行网络延时 - 4：音频上行网络抖动 - 5：视频上行网络延时 - 6：视频上行网络抖动 - 7：音频下行网络延时 - 8：音频下行网络抖动 - 9：视频下行网络延时 - 10：视频下行网络抖动 - 11：上行音频丢包 - 12：上行视频丢包 - 13：下行音频丢包 - 14：下行视频丢包 - 15：下行音频无声音 - 16：其他 - 17：对端用户离线 - 18：对端用户无码流 - 19：对端用户无帧率 - 20：本端服务器下行无码流 - 21：本端服务器下行无帧率 

        :return: The abnormal_factor of this AbnormalEvent.
        :rtype: int
        """
        return self._abnormal_factor

    @abnormal_factor.setter
    def abnormal_factor(self, abnormal_factor):
        """Sets the abnormal_factor of this AbnormalEvent.

        异常因素 当异常类型为1时，异常因素取值范围为： - 1：建链失败 - 2：房间非空闲 - 3：服务器异常 - 4：服务器反馈503 - 5：鉴权失败 - 6：鉴权重试 - 7：时钟同步失败 - 8：url错误 - 9：终端内部异常 - 90000004：SDK发出的加入房间信令响应超时 - 90100009：web侧没有收到MSP下发的配置信息 - 90100008：websocket链路建链失败 - 10000001：服务侧返回的异常信息 - 31000003：服务侧返回的异常信息 - 32000030：服务侧返回的异常信息 - 15：浏览器设置sdp异常 当异常类型为2或者3时，异常因素取值范围为： - 1：系统CPU占用高 - 2：App CPU占用高 - 3：音频上行网络延时 - 4：音频上行网络抖动 - 5：视频上行网络延时 - 6：视频上行网络抖动 - 7：音频下行网络延时 - 8：音频下行网络抖动 - 9：视频下行网络延时 - 10：视频下行网络抖动 - 11：上行音频丢包 - 12：上行视频丢包 - 13：下行音频丢包 - 14：下行视频丢包 - 15：下行音频无声音 - 16：其他 - 17：对端用户离线 - 18：对端用户无码流 - 19：对端用户无帧率 - 20：本端服务器下行无码流 - 21：本端服务器下行无帧率 

        :param abnormal_factor: The abnormal_factor of this AbnormalEvent.
        :type abnormal_factor: int
        """
        self._abnormal_factor = abnormal_factor

    @property
    def abnormal_factor_desc(self):
        """Gets the abnormal_factor_desc of this AbnormalEvent.

        异常因素描述，支持国际化 当异常类型为1时，异常因素描述与异常因素对应，取值范围为： - 建链失败 - 房间非空闲 - 服务器异常 - 服务器反馈503 - 鉴权失败 - 鉴权重试 - 时钟同步失败 - url错误 - 终端内部异常 - SDK发出的加入房间信令响应超时 - web侧没有收到MSP下发的配置信息 - websocket链路建链失败 - 服务侧返回的异常信息 - 服务侧返回的异常信息 - 服务侧返回的异常信息 - 浏览器设置sdp异常 当异常类型为2或者3时，异常因素描述与异常因素对应，取值范围为： - 系统CPU占用高 - App CPU占用高 - 音频上行网络延时 - 音频上行网络抖动 - 视频上行网络延时 - 视频上行网络抖动 - 音频下行网络延时 - 音频下行网络抖动 - 视频下行网络延时 - 视频下行网络抖动 - 上行音频丢包 - 上行视频丢包 - 下行音频丢包 - 下行视频丢包 - 下行音频无声音 - 其他 - 对端用户离线 - 对端用户无码流 - 对端用户无帧率 - 本端服务器下行无码流 - 本端服务器下行无帧率 其他情况，异常因素描述为：其他 

        :return: The abnormal_factor_desc of this AbnormalEvent.
        :rtype: str
        """
        return self._abnormal_factor_desc

    @abnormal_factor_desc.setter
    def abnormal_factor_desc(self, abnormal_factor_desc):
        """Sets the abnormal_factor_desc of this AbnormalEvent.

        异常因素描述，支持国际化 当异常类型为1时，异常因素描述与异常因素对应，取值范围为： - 建链失败 - 房间非空闲 - 服务器异常 - 服务器反馈503 - 鉴权失败 - 鉴权重试 - 时钟同步失败 - url错误 - 终端内部异常 - SDK发出的加入房间信令响应超时 - web侧没有收到MSP下发的配置信息 - websocket链路建链失败 - 服务侧返回的异常信息 - 服务侧返回的异常信息 - 服务侧返回的异常信息 - 浏览器设置sdp异常 当异常类型为2或者3时，异常因素描述与异常因素对应，取值范围为： - 系统CPU占用高 - App CPU占用高 - 音频上行网络延时 - 音频上行网络抖动 - 视频上行网络延时 - 视频上行网络抖动 - 音频下行网络延时 - 音频下行网络抖动 - 视频下行网络延时 - 视频下行网络抖动 - 上行音频丢包 - 上行视频丢包 - 下行音频丢包 - 下行视频丢包 - 下行音频无声音 - 其他 - 对端用户离线 - 对端用户无码流 - 对端用户无帧率 - 本端服务器下行无码流 - 本端服务器下行无帧率 其他情况，异常因素描述为：其他 

        :param abnormal_factor_desc: The abnormal_factor_desc of this AbnormalEvent.
        :type abnormal_factor_desc: str
        """
        self._abnormal_factor_desc = abnormal_factor_desc

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
        if not isinstance(other, AbnormalEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
