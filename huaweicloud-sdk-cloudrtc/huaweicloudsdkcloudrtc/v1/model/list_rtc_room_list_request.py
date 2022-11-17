# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcRoomListRequest:

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
        'state': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'x_sdk_date': 'X-Sdk-Date',
        'x_project_id': 'X-Project-Id',
        'project_id': 'project_id',
        'app': 'app',
        'room_id': 'room_id',
        'state': 'state',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, authorization=None, x_sdk_date=None, x_project_id=None, project_id=None, app=None, room_id=None, state=None, start_time=None, end_time=None, limit=None, offset=None):
        """ListRtcRoomListRequest

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
        :param room_id: 房间id 
        :type room_id: str
        :param state: 房间状态，取值如下： - RUNNING：开启中 - CLOSED：已关闭 
        :type state: str
        :param start_time: 查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认读取过去1小时数据数据。 
        :type start_time: str
        :param end_time: 查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z，不写默认为当前时间。 
        :type end_time: str
        :param limit: 查询结果条数 
        :type limit: int
        :param offset: 查询偏移量 
        :type offset: int
        """
        
        

        self._authorization = None
        self._x_sdk_date = None
        self._x_project_id = None
        self._project_id = None
        self._app = None
        self._room_id = None
        self._state = None
        self._start_time = None
        self._end_time = None
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
        self.app = app
        if room_id is not None:
            self.room_id = room_id
        if state is not None:
            self.state = state
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def authorization(self):
        """Gets the authorization of this ListRtcRoomListRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。 

        :return: The authorization of this ListRtcRoomListRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ListRtcRoomListRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。 

        :param authorization: The authorization of this ListRtcRoomListRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this ListRtcRoomListRequest.

        使用AK/SK方式认证时必选，请求的发生时间。 

        :return: The x_sdk_date of this ListRtcRoomListRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this ListRtcRoomListRequest.

        使用AK/SK方式认证时必选，请求的发生时间。 

        :param x_sdk_date: The x_sdk_date of this ListRtcRoomListRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def x_project_id(self):
        """Gets the x_project_id of this ListRtcRoomListRequest.

        使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 

        :return: The x_project_id of this ListRtcRoomListRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this ListRtcRoomListRequest.

        使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 

        :param x_project_id: The x_project_id of this ListRtcRoomListRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def project_id(self):
        """Gets the project_id of this ListRtcRoomListRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 

        :return: The project_id of this ListRtcRoomListRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListRtcRoomListRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 

        :param project_id: The project_id of this ListRtcRoomListRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def app(self):
        """Gets the app of this ListRtcRoomListRequest.

        应用标识 

        :return: The app of this ListRtcRoomListRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListRtcRoomListRequest.

        应用标识 

        :param app: The app of this ListRtcRoomListRequest.
        :type app: str
        """
        self._app = app

    @property
    def room_id(self):
        """Gets the room_id of this ListRtcRoomListRequest.

        房间id 

        :return: The room_id of this ListRtcRoomListRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ListRtcRoomListRequest.

        房间id 

        :param room_id: The room_id of this ListRtcRoomListRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def state(self):
        """Gets the state of this ListRtcRoomListRequest.

        房间状态，取值如下： - RUNNING：开启中 - CLOSED：已关闭 

        :return: The state of this ListRtcRoomListRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListRtcRoomListRequest.

        房间状态，取值如下： - RUNNING：开启中 - CLOSED：已关闭 

        :param state: The state of this ListRtcRoomListRequest.
        :type state: str
        """
        self._state = state

    @property
    def start_time(self):
        """Gets the start_time of this ListRtcRoomListRequest.

        查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认读取过去1小时数据数据。 

        :return: The start_time of this ListRtcRoomListRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListRtcRoomListRequest.

        查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认读取过去1小时数据数据。 

        :param start_time: The start_time of this ListRtcRoomListRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListRtcRoomListRequest.

        查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z，不写默认为当前时间。 

        :return: The end_time of this ListRtcRoomListRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListRtcRoomListRequest.

        查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z，不写默认为当前时间。 

        :param end_time: The end_time of this ListRtcRoomListRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ListRtcRoomListRequest.

        查询结果条数 

        :return: The limit of this ListRtcRoomListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRtcRoomListRequest.

        查询结果条数 

        :param limit: The limit of this ListRtcRoomListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListRtcRoomListRequest.

        查询偏移量 

        :return: The offset of this ListRtcRoomListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRtcRoomListRequest.

        查询偏移量 

        :param offset: The offset of this ListRtcRoomListRequest.
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
        if not isinstance(other, ListRtcRoomListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
