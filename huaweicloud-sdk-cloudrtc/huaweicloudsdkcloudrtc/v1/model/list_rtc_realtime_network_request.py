# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcRealtimeNetworkRequest:

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
        'app': 'str',
        'room_id': 'str',
        'metric': 'str',
        'sdk_type': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'x_sdk_date': 'X-Sdk-Date',
        'x_project_id': 'X-Project-Id',
        'project_id': 'project_id',
        'app': 'app',
        'room_id': 'room_id',
        'metric': 'metric',
        'sdk_type': 'sdk_type',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, authorization=None, x_sdk_date=None, x_project_id=None, project_id=None, app=None, room_id=None, metric=None, sdk_type=None, start_time=None, end_time=None):
        """ListRtcRealtimeNetworkRequest

        The model defined in huaweicloud sdk

        :param authorization: 使用AK/SK方式认证时必选，携带的鉴权信息。 
        :type authorization: str
        :param x_sdk_date: 使用AK/SK方式认证时必选，请求的发生时间。 
        :type x_sdk_date: str
        :param x_project_id: 使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 
        :type x_project_id: str
        :param project_id: 项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 
        :type project_id: str
        :param app: 应用标识 
        :type app: str
        :param room_id: 房间ID 
        :type room_id: str
        :param metric: 查询的数据类型 VideoUpstreamExcellentTransRate：客户端视频上行优质传输率; AudioUpstreamExcellentTransRate：客户端音频上行优质传输率; VideoExcellentTransRate：端到端视频优质传输率; AudioExcellentTransRate：端到端音频优质传输率; 
        :type metric: str
        :param sdk_type: sdk类型 - native: 非web版sdk; - webrtc: web版sdk; 
        :type sdk_type: str
        :param start_time: 查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认读取过去1小时数据。 
        :type start_time: str
        :param end_time: 查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认为当前时间。 
        :type end_time: str
        """
        
        

        self._authorization = None
        self._x_sdk_date = None
        self._x_project_id = None
        self._project_id = None
        self._app = None
        self._room_id = None
        self._metric = None
        self._sdk_type = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if authorization is not None:
            self.authorization = authorization
        if x_sdk_date is not None:
            self.x_sdk_date = x_sdk_date
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.project_id = project_id
        self.app = app
        if room_id is not None:
            self.room_id = room_id
        self.metric = metric
        self.sdk_type = sdk_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def authorization(self):
        """Gets the authorization of this ListRtcRealtimeNetworkRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。 

        :return: The authorization of this ListRtcRealtimeNetworkRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ListRtcRealtimeNetworkRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。 

        :param authorization: The authorization of this ListRtcRealtimeNetworkRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this ListRtcRealtimeNetworkRequest.

        使用AK/SK方式认证时必选，请求的发生时间。 

        :return: The x_sdk_date of this ListRtcRealtimeNetworkRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this ListRtcRealtimeNetworkRequest.

        使用AK/SK方式认证时必选，请求的发生时间。 

        :param x_sdk_date: The x_sdk_date of this ListRtcRealtimeNetworkRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def x_project_id(self):
        """Gets the x_project_id of this ListRtcRealtimeNetworkRequest.

        使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 

        :return: The x_project_id of this ListRtcRealtimeNetworkRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this ListRtcRealtimeNetworkRequest.

        使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 

        :param x_project_id: The x_project_id of this ListRtcRealtimeNetworkRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def project_id(self):
        """Gets the project_id of this ListRtcRealtimeNetworkRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 

        :return: The project_id of this ListRtcRealtimeNetworkRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListRtcRealtimeNetworkRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 

        :param project_id: The project_id of this ListRtcRealtimeNetworkRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def app(self):
        """Gets the app of this ListRtcRealtimeNetworkRequest.

        应用标识 

        :return: The app of this ListRtcRealtimeNetworkRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListRtcRealtimeNetworkRequest.

        应用标识 

        :param app: The app of this ListRtcRealtimeNetworkRequest.
        :type app: str
        """
        self._app = app

    @property
    def room_id(self):
        """Gets the room_id of this ListRtcRealtimeNetworkRequest.

        房间ID 

        :return: The room_id of this ListRtcRealtimeNetworkRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ListRtcRealtimeNetworkRequest.

        房间ID 

        :param room_id: The room_id of this ListRtcRealtimeNetworkRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def metric(self):
        """Gets the metric of this ListRtcRealtimeNetworkRequest.

        查询的数据类型 VideoUpstreamExcellentTransRate：客户端视频上行优质传输率; AudioUpstreamExcellentTransRate：客户端音频上行优质传输率; VideoExcellentTransRate：端到端视频优质传输率; AudioExcellentTransRate：端到端音频优质传输率; 

        :return: The metric of this ListRtcRealtimeNetworkRequest.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this ListRtcRealtimeNetworkRequest.

        查询的数据类型 VideoUpstreamExcellentTransRate：客户端视频上行优质传输率; AudioUpstreamExcellentTransRate：客户端音频上行优质传输率; VideoExcellentTransRate：端到端视频优质传输率; AudioExcellentTransRate：端到端音频优质传输率; 

        :param metric: The metric of this ListRtcRealtimeNetworkRequest.
        :type metric: str
        """
        self._metric = metric

    @property
    def sdk_type(self):
        """Gets the sdk_type of this ListRtcRealtimeNetworkRequest.

        sdk类型 - native: 非web版sdk; - webrtc: web版sdk; 

        :return: The sdk_type of this ListRtcRealtimeNetworkRequest.
        :rtype: str
        """
        return self._sdk_type

    @sdk_type.setter
    def sdk_type(self, sdk_type):
        """Sets the sdk_type of this ListRtcRealtimeNetworkRequest.

        sdk类型 - native: 非web版sdk; - webrtc: web版sdk; 

        :param sdk_type: The sdk_type of this ListRtcRealtimeNetworkRequest.
        :type sdk_type: str
        """
        self._sdk_type = sdk_type

    @property
    def start_time(self):
        """Gets the start_time of this ListRtcRealtimeNetworkRequest.

        查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认读取过去1小时数据。 

        :return: The start_time of this ListRtcRealtimeNetworkRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListRtcRealtimeNetworkRequest.

        查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认读取过去1小时数据。 

        :param start_time: The start_time of this ListRtcRealtimeNetworkRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListRtcRealtimeNetworkRequest.

        查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认为当前时间。 

        :return: The end_time of this ListRtcRealtimeNetworkRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListRtcRealtimeNetworkRequest.

        查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认为当前时间。 

        :param end_time: The end_time of this ListRtcRealtimeNetworkRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListRtcRealtimeNetworkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
