# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcRealtimeScaleDimensionRequest:

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
        'dimension': 'str',
        'time': 'str'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'x_sdk_date': 'X-Sdk-Date',
        'x_project_id': 'X-Project-Id',
        'project_id': 'project_id',
        'app': 'app',
        'room_id': 'room_id',
        'metric': 'metric',
        'dimension': 'dimension',
        'time': 'time'
    }

    def __init__(self, authorization=None, x_sdk_date=None, x_project_id=None, project_id=None, app=None, room_id=None, metric=None, dimension=None, time=None):
        """ListRtcRealtimeScaleDimensionRequest

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
        :param metric: 查询的数据类型  OnlineUsers:在线用户数 
        :type metric: str
        :param dimension: 维度类型: region:省份 access_net:网络类型 platform:系统平台 sdk:SDK版本 
        :type dimension: str
        :param time: 查询时刻。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ 
        :type time: str
        """
        
        

        self._authorization = None
        self._x_sdk_date = None
        self._x_project_id = None
        self._project_id = None
        self._app = None
        self._room_id = None
        self._metric = None
        self._dimension = None
        self._time = None
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
        self.dimension = dimension
        self.time = time

    @property
    def authorization(self):
        """Gets the authorization of this ListRtcRealtimeScaleDimensionRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。 

        :return: The authorization of this ListRtcRealtimeScaleDimensionRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ListRtcRealtimeScaleDimensionRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。 

        :param authorization: The authorization of this ListRtcRealtimeScaleDimensionRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this ListRtcRealtimeScaleDimensionRequest.

        使用AK/SK方式认证时必选，请求的发生时间。 

        :return: The x_sdk_date of this ListRtcRealtimeScaleDimensionRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this ListRtcRealtimeScaleDimensionRequest.

        使用AK/SK方式认证时必选，请求的发生时间。 

        :param x_sdk_date: The x_sdk_date of this ListRtcRealtimeScaleDimensionRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def x_project_id(self):
        """Gets the x_project_id of this ListRtcRealtimeScaleDimensionRequest.

        使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 

        :return: The x_project_id of this ListRtcRealtimeScaleDimensionRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this ListRtcRealtimeScaleDimensionRequest.

        使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 

        :param x_project_id: The x_project_id of this ListRtcRealtimeScaleDimensionRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def project_id(self):
        """Gets the project_id of this ListRtcRealtimeScaleDimensionRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 

        :return: The project_id of this ListRtcRealtimeScaleDimensionRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListRtcRealtimeScaleDimensionRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 

        :param project_id: The project_id of this ListRtcRealtimeScaleDimensionRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def app(self):
        """Gets the app of this ListRtcRealtimeScaleDimensionRequest.

        应用标识 

        :return: The app of this ListRtcRealtimeScaleDimensionRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListRtcRealtimeScaleDimensionRequest.

        应用标识 

        :param app: The app of this ListRtcRealtimeScaleDimensionRequest.
        :type app: str
        """
        self._app = app

    @property
    def room_id(self):
        """Gets the room_id of this ListRtcRealtimeScaleDimensionRequest.

        房间ID 

        :return: The room_id of this ListRtcRealtimeScaleDimensionRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ListRtcRealtimeScaleDimensionRequest.

        房间ID 

        :param room_id: The room_id of this ListRtcRealtimeScaleDimensionRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def metric(self):
        """Gets the metric of this ListRtcRealtimeScaleDimensionRequest.

        查询的数据类型  OnlineUsers:在线用户数 

        :return: The metric of this ListRtcRealtimeScaleDimensionRequest.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this ListRtcRealtimeScaleDimensionRequest.

        查询的数据类型  OnlineUsers:在线用户数 

        :param metric: The metric of this ListRtcRealtimeScaleDimensionRequest.
        :type metric: str
        """
        self._metric = metric

    @property
    def dimension(self):
        """Gets the dimension of this ListRtcRealtimeScaleDimensionRequest.

        维度类型: region:省份 access_net:网络类型 platform:系统平台 sdk:SDK版本 

        :return: The dimension of this ListRtcRealtimeScaleDimensionRequest.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this ListRtcRealtimeScaleDimensionRequest.

        维度类型: region:省份 access_net:网络类型 platform:系统平台 sdk:SDK版本 

        :param dimension: The dimension of this ListRtcRealtimeScaleDimensionRequest.
        :type dimension: str
        """
        self._dimension = dimension

    @property
    def time(self):
        """Gets the time of this ListRtcRealtimeScaleDimensionRequest.

        查询时刻。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ 

        :return: The time of this ListRtcRealtimeScaleDimensionRequest.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ListRtcRealtimeScaleDimensionRequest.

        查询时刻。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ 

        :param time: The time of this ListRtcRealtimeScaleDimensionRequest.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, ListRtcRealtimeScaleDimensionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
