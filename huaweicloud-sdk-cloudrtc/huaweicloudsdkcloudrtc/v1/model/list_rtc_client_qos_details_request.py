# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcClientQosDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorization': 'str',
        'x_sdk_date': 'str',
        'x_project_id': 'str',
        'project_id': 'str',
        'domain': 'str',
        'app_id': 'str',
        'room_id': 'str',
        'user_id': 'str',
        'peer_id': 'str',
        'stream_id': 'str',
        'direction': 'str',
        'mid': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'time_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'x_sdk_date': 'X-Sdk-Date',
        'x_project_id': 'X-Project-Id',
        'project_id': 'project_id',
        'domain': 'domain',
        'app_id': 'app_id',
        'room_id': 'room_id',
        'user_id': 'user_id',
        'peer_id': 'peer_id',
        'stream_id': 'stream_id',
        'direction': 'direction',
        'mid': 'mid',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'time_type': 'time_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, authorization=None, x_sdk_date=None, x_project_id=None, project_id=None, domain=None, app_id=None, room_id=None, user_id=None, peer_id=None, stream_id=None, direction=None, mid=None, start_time=None, end_time=None, time_type=None, limit=None, offset=None):
        """ListRtcClientQosDetailsRequest

        The model defined in huaweicloud sdk

        :param authorization: 使用AK/SK方式认证时必选，携带的鉴权信息。 
        :type authorization: str
        :param x_sdk_date: 使用AK/SK方式认证时必选，请求的发生时间。 
        :type x_sdk_date: str
        :param x_project_id: 使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 
        :type x_project_id: str
        :param project_id: 项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 
        :type project_id: str
        :param domain: 域名 
        :type domain: str
        :param app_id: 应用id 
        :type app_id: str
        :param room_id: 房间ID 
        :type room_id: str
        :param user_id: 发送端用户 
        :type user_id: str
        :param peer_id: 需查询接收端用户id 
        :type peer_id: str
        :param stream_id: 流号 
        :type stream_id: str
        :param direction: 判断上下行数据 
        :type direction: str
        :param mid: 需查询的指标，填all则返回所有指标。多个指标使用&#39;,&#39;分割 - appcpu：端侧APP CPU使用率（appCpu） - syscpu：端侧系统 CPU使用率（deviceCpu） - abit：端侧音频码率kpbs（bitrate） - vbit：端侧视频码率kbps（bitRate） - dbit：端侧辅流码率kbps（bitRate） - vfps：端侧视频帧率fps（actFrameRate） - dfps：端侧辅流帧率fps（actFrameRate） - vblock：端侧视频卡顿率（统计大于等于600ms视频卡顿） - dblock：端侧辅流卡顿率（统计大于等于600ms辅流卡顿） - aloss：端侧音频丢包率（pktLoss） - vloss：端侧视频丢包率（pktLoss） - dloss：端侧辅流丢包率（pktLoss） - vwidth：端侧视频分辨率宽（actPicW） - vheight：端侧视频分辨率高（actPicH） - dwidth：端侧辅流分辨率宽（actPicW） - dheight：端侧辅流分辨率高（actPicH） - ajitter：端侧音频抖动率（jitter） - artt：端侧音频时延（rtt） - vjitter：端侧视频抖动率（jitter） - vrtt：端侧视频时延（rtt） - djitter：端侧辅流抖动率（jitter） - drtt：端侧辅流时延（rtt） 
        :type mid: str
        :param start_time: 查询起始时间。UTC时间，格式：yyyy-mm-ddThh:mm:ssZ，如2020-04-23T06:00:00Z 
        :type start_time: str
        :param end_time: 查询结束时间。UTC时间，格式：yyyy-mm-ddThh:mm:ssZ，如2020-04-23T07:00:00Z 
        :type end_time: str
        :param time_type: 查询的时间类型取值：stime 数据库打点时间，不填默认ctime查询
        :type time_type: str
        :param limit: 查询结果限制 
        :type limit: int
        :param offset: 查询偏移量 
        :type offset: int
        """
        
        

        self._authorization = None
        self._x_sdk_date = None
        self._x_project_id = None
        self._project_id = None
        self._domain = None
        self._app_id = None
        self._room_id = None
        self._user_id = None
        self._peer_id = None
        self._stream_id = None
        self._direction = None
        self._mid = None
        self._start_time = None
        self._end_time = None
        self._time_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization
        if x_sdk_date is not None:
            self.x_sdk_date = x_sdk_date
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.project_id = project_id
        if domain is not None:
            self.domain = domain
        self.app_id = app_id
        self.room_id = room_id
        if user_id is not None:
            self.user_id = user_id
        if peer_id is not None:
            self.peer_id = peer_id
        if stream_id is not None:
            self.stream_id = stream_id
        if direction is not None:
            self.direction = direction
        self.mid = mid
        self.start_time = start_time
        self.end_time = end_time
        if time_type is not None:
            self.time_type = time_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def authorization(self):
        """Gets the authorization of this ListRtcClientQosDetailsRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。 

        :return: The authorization of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ListRtcClientQosDetailsRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。 

        :param authorization: The authorization of this ListRtcClientQosDetailsRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this ListRtcClientQosDetailsRequest.

        使用AK/SK方式认证时必选，请求的发生时间。 

        :return: The x_sdk_date of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this ListRtcClientQosDetailsRequest.

        使用AK/SK方式认证时必选，请求的发生时间。 

        :param x_sdk_date: The x_sdk_date of this ListRtcClientQosDetailsRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def x_project_id(self):
        """Gets the x_project_id of this ListRtcClientQosDetailsRequest.

        使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 

        :return: The x_project_id of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this ListRtcClientQosDetailsRequest.

        使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 

        :param x_project_id: The x_project_id of this ListRtcClientQosDetailsRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def project_id(self):
        """Gets the project_id of this ListRtcClientQosDetailsRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 

        :return: The project_id of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListRtcClientQosDetailsRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 

        :param project_id: The project_id of this ListRtcClientQosDetailsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain(self):
        """Gets the domain of this ListRtcClientQosDetailsRequest.

        域名 

        :return: The domain of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ListRtcClientQosDetailsRequest.

        域名 

        :param domain: The domain of this ListRtcClientQosDetailsRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_id(self):
        """Gets the app_id of this ListRtcClientQosDetailsRequest.

        应用id 

        :return: The app_id of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListRtcClientQosDetailsRequest.

        应用id 

        :param app_id: The app_id of this ListRtcClientQosDetailsRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def room_id(self):
        """Gets the room_id of this ListRtcClientQosDetailsRequest.

        房间ID 

        :return: The room_id of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ListRtcClientQosDetailsRequest.

        房间ID 

        :param room_id: The room_id of this ListRtcClientQosDetailsRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def user_id(self):
        """Gets the user_id of this ListRtcClientQosDetailsRequest.

        发送端用户 

        :return: The user_id of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ListRtcClientQosDetailsRequest.

        发送端用户 

        :param user_id: The user_id of this ListRtcClientQosDetailsRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def peer_id(self):
        """Gets the peer_id of this ListRtcClientQosDetailsRequest.

        需查询接收端用户id 

        :return: The peer_id of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._peer_id

    @peer_id.setter
    def peer_id(self, peer_id):
        """Sets the peer_id of this ListRtcClientQosDetailsRequest.

        需查询接收端用户id 

        :param peer_id: The peer_id of this ListRtcClientQosDetailsRequest.
        :type peer_id: str
        """
        self._peer_id = peer_id

    @property
    def stream_id(self):
        """Gets the stream_id of this ListRtcClientQosDetailsRequest.

        流号 

        :return: The stream_id of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this ListRtcClientQosDetailsRequest.

        流号 

        :param stream_id: The stream_id of this ListRtcClientQosDetailsRequest.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def direction(self):
        """Gets the direction of this ListRtcClientQosDetailsRequest.

        判断上下行数据 

        :return: The direction of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ListRtcClientQosDetailsRequest.

        判断上下行数据 

        :param direction: The direction of this ListRtcClientQosDetailsRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def mid(self):
        """Gets the mid of this ListRtcClientQosDetailsRequest.

        需查询的指标，填all则返回所有指标。多个指标使用','分割 - appcpu：端侧APP CPU使用率（appCpu） - syscpu：端侧系统 CPU使用率（deviceCpu） - abit：端侧音频码率kpbs（bitrate） - vbit：端侧视频码率kbps（bitRate） - dbit：端侧辅流码率kbps（bitRate） - vfps：端侧视频帧率fps（actFrameRate） - dfps：端侧辅流帧率fps（actFrameRate） - vblock：端侧视频卡顿率（统计大于等于600ms视频卡顿） - dblock：端侧辅流卡顿率（统计大于等于600ms辅流卡顿） - aloss：端侧音频丢包率（pktLoss） - vloss：端侧视频丢包率（pktLoss） - dloss：端侧辅流丢包率（pktLoss） - vwidth：端侧视频分辨率宽（actPicW） - vheight：端侧视频分辨率高（actPicH） - dwidth：端侧辅流分辨率宽（actPicW） - dheight：端侧辅流分辨率高（actPicH） - ajitter：端侧音频抖动率（jitter） - artt：端侧音频时延（rtt） - vjitter：端侧视频抖动率（jitter） - vrtt：端侧视频时延（rtt） - djitter：端侧辅流抖动率（jitter） - drtt：端侧辅流时延（rtt） 

        :return: The mid of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._mid

    @mid.setter
    def mid(self, mid):
        """Sets the mid of this ListRtcClientQosDetailsRequest.

        需查询的指标，填all则返回所有指标。多个指标使用','分割 - appcpu：端侧APP CPU使用率（appCpu） - syscpu：端侧系统 CPU使用率（deviceCpu） - abit：端侧音频码率kpbs（bitrate） - vbit：端侧视频码率kbps（bitRate） - dbit：端侧辅流码率kbps（bitRate） - vfps：端侧视频帧率fps（actFrameRate） - dfps：端侧辅流帧率fps（actFrameRate） - vblock：端侧视频卡顿率（统计大于等于600ms视频卡顿） - dblock：端侧辅流卡顿率（统计大于等于600ms辅流卡顿） - aloss：端侧音频丢包率（pktLoss） - vloss：端侧视频丢包率（pktLoss） - dloss：端侧辅流丢包率（pktLoss） - vwidth：端侧视频分辨率宽（actPicW） - vheight：端侧视频分辨率高（actPicH） - dwidth：端侧辅流分辨率宽（actPicW） - dheight：端侧辅流分辨率高（actPicH） - ajitter：端侧音频抖动率（jitter） - artt：端侧音频时延（rtt） - vjitter：端侧视频抖动率（jitter） - vrtt：端侧视频时延（rtt） - djitter：端侧辅流抖动率（jitter） - drtt：端侧辅流时延（rtt） 

        :param mid: The mid of this ListRtcClientQosDetailsRequest.
        :type mid: str
        """
        self._mid = mid

    @property
    def start_time(self):
        """Gets the start_time of this ListRtcClientQosDetailsRequest.

        查询起始时间。UTC时间，格式：yyyy-mm-ddThh:mm:ssZ，如2020-04-23T06:00:00Z 

        :return: The start_time of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListRtcClientQosDetailsRequest.

        查询起始时间。UTC时间，格式：yyyy-mm-ddThh:mm:ssZ，如2020-04-23T06:00:00Z 

        :param start_time: The start_time of this ListRtcClientQosDetailsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListRtcClientQosDetailsRequest.

        查询结束时间。UTC时间，格式：yyyy-mm-ddThh:mm:ssZ，如2020-04-23T07:00:00Z 

        :return: The end_time of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListRtcClientQosDetailsRequest.

        查询结束时间。UTC时间，格式：yyyy-mm-ddThh:mm:ssZ，如2020-04-23T07:00:00Z 

        :param end_time: The end_time of this ListRtcClientQosDetailsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def time_type(self):
        """Gets the time_type of this ListRtcClientQosDetailsRequest.

        查询的时间类型取值：stime 数据库打点时间，不填默认ctime查询

        :return: The time_type of this ListRtcClientQosDetailsRequest.
        :rtype: str
        """
        return self._time_type

    @time_type.setter
    def time_type(self, time_type):
        """Sets the time_type of this ListRtcClientQosDetailsRequest.

        查询的时间类型取值：stime 数据库打点时间，不填默认ctime查询

        :param time_type: The time_type of this ListRtcClientQosDetailsRequest.
        :type time_type: str
        """
        self._time_type = time_type

    @property
    def limit(self):
        """Gets the limit of this ListRtcClientQosDetailsRequest.

        查询结果限制 

        :return: The limit of this ListRtcClientQosDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRtcClientQosDetailsRequest.

        查询结果限制 

        :param limit: The limit of this ListRtcClientQosDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListRtcClientQosDetailsRequest.

        查询偏移量 

        :return: The offset of this ListRtcClientQosDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRtcClientQosDetailsRequest.

        查询偏移量 

        :param offset: The offset of this ListRtcClientQosDetailsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListRtcClientQosDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
