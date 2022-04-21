# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcUserListRequest:

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
        'uid': 'str',
        'nickname': 'str',
        'region': 'list[str]',
        'isp': 'list[str]',
        'state': 'list[str]',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int',
        'type': 'str'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'x_sdk_date': 'X-Sdk-Date',
        'x_project_id': 'X-Project-Id',
        'project_id': 'project_id',
        'app': 'app',
        'room_id': 'room_id',
        'uid': 'uid',
        'nickname': 'nickname',
        'region': 'region',
        'isp': 'isp',
        'state': 'state',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'type': 'type'
    }

    def __init__(self, authorization=None, x_sdk_date=None, x_project_id=None, project_id=None, app=None, room_id=None, uid=None, nickname=None, region=None, isp=None, state=None, start_time=None, end_time=None, limit=None, offset=None, type=None):
        """ListRtcUserListRequest

        The model defined in huaweicloud sdk

        :param authorization: 使用AK/SK方式认证时必选，携带的鉴权信息。 
        :type authorization: str
        :param x_sdk_date: 使用AK/SK方式认证时必选，请求的发生时间。 
        :type x_sdk_date: str
        :param x_project_id: 使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 
        :type x_project_id: str
        :param project_id: 项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 
        :type project_id: str
        :param app: 应用id 
        :type app: str
        :param room_id: 房间id 
        :type room_id: str
        :param uid: 用户id 
        :type uid: str
        :param nickname: 用户昵称 
        :type nickname: str
        :param region: 用户省份，支持省份名或缩写，如广东或者GD 
        :type region: list[str]
        :param isp: 用户接入运营商 
        :type isp: list[str]
        :param state: 用户状态，取值如下： - FAIL：加入失败 - ONLINE：在线 - OFFLINE：离开 
        :type state: list[str]
        :param start_time: 查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认读取过去1小时数据数据。 
        :type start_time: str
        :param end_time: 查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认为当前时间。 
        :type end_time: str
        :param limit: 查询结果限制 
        :type limit: int
        :param offset: 查询偏移量 
        :type offset: int
        :param type: 查询模式，取值如下： - detail：会话级 - summary：用户级（默认） 
        :type type: str
        """
        
        

        self._authorization = None
        self._x_sdk_date = None
        self._x_project_id = None
        self._project_id = None
        self._app = None
        self._room_id = None
        self._uid = None
        self._nickname = None
        self._region = None
        self._isp = None
        self._state = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._type = None
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
        if uid is not None:
            self.uid = uid
        if nickname is not None:
            self.nickname = nickname
        if region is not None:
            self.region = region
        if isp is not None:
            self.isp = isp
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
        if type is not None:
            self.type = type

    @property
    def authorization(self):
        """Gets the authorization of this ListRtcUserListRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。 

        :return: The authorization of this ListRtcUserListRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this ListRtcUserListRequest.

        使用AK/SK方式认证时必选，携带的鉴权信息。 

        :param authorization: The authorization of this ListRtcUserListRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def x_sdk_date(self):
        """Gets the x_sdk_date of this ListRtcUserListRequest.

        使用AK/SK方式认证时必选，请求的发生时间。 

        :return: The x_sdk_date of this ListRtcUserListRequest.
        :rtype: str
        """
        return self._x_sdk_date

    @x_sdk_date.setter
    def x_sdk_date(self, x_sdk_date):
        """Sets the x_sdk_date of this ListRtcUserListRequest.

        使用AK/SK方式认证时必选，请求的发生时间。 

        :param x_sdk_date: The x_sdk_date of this ListRtcUserListRequest.
        :type x_sdk_date: str
        """
        self._x_sdk_date = x_sdk_date

    @property
    def x_project_id(self):
        """Gets the x_project_id of this ListRtcUserListRequest.

        使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 

        :return: The x_project_id of this ListRtcUserListRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this ListRtcUserListRequest.

        使用AK/SK方式认证时必选，携带项目ID信息，与路径参数中的项目ID相同。 

        :param x_project_id: The x_project_id of this ListRtcUserListRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def project_id(self):
        """Gets the project_id of this ListRtcUserListRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 

        :return: The project_id of this ListRtcUserListRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListRtcUserListRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。 

        :param project_id: The project_id of this ListRtcUserListRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def app(self):
        """Gets the app of this ListRtcUserListRequest.

        应用id 

        :return: The app of this ListRtcUserListRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListRtcUserListRequest.

        应用id 

        :param app: The app of this ListRtcUserListRequest.
        :type app: str
        """
        self._app = app

    @property
    def room_id(self):
        """Gets the room_id of this ListRtcUserListRequest.

        房间id 

        :return: The room_id of this ListRtcUserListRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ListRtcUserListRequest.

        房间id 

        :param room_id: The room_id of this ListRtcUserListRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def uid(self):
        """Gets the uid of this ListRtcUserListRequest.

        用户id 

        :return: The uid of this ListRtcUserListRequest.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ListRtcUserListRequest.

        用户id 

        :param uid: The uid of this ListRtcUserListRequest.
        :type uid: str
        """
        self._uid = uid

    @property
    def nickname(self):
        """Gets the nickname of this ListRtcUserListRequest.

        用户昵称 

        :return: The nickname of this ListRtcUserListRequest.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this ListRtcUserListRequest.

        用户昵称 

        :param nickname: The nickname of this ListRtcUserListRequest.
        :type nickname: str
        """
        self._nickname = nickname

    @property
    def region(self):
        """Gets the region of this ListRtcUserListRequest.

        用户省份，支持省份名或缩写，如广东或者GD 

        :return: The region of this ListRtcUserListRequest.
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListRtcUserListRequest.

        用户省份，支持省份名或缩写，如广东或者GD 

        :param region: The region of this ListRtcUserListRequest.
        :type region: list[str]
        """
        self._region = region

    @property
    def isp(self):
        """Gets the isp of this ListRtcUserListRequest.

        用户接入运营商 

        :return: The isp of this ListRtcUserListRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ListRtcUserListRequest.

        用户接入运营商 

        :param isp: The isp of this ListRtcUserListRequest.
        :type isp: list[str]
        """
        self._isp = isp

    @property
    def state(self):
        """Gets the state of this ListRtcUserListRequest.

        用户状态，取值如下： - FAIL：加入失败 - ONLINE：在线 - OFFLINE：离开 

        :return: The state of this ListRtcUserListRequest.
        :rtype: list[str]
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListRtcUserListRequest.

        用户状态，取值如下： - FAIL：加入失败 - ONLINE：在线 - OFFLINE：离开 

        :param state: The state of this ListRtcUserListRequest.
        :type state: list[str]
        """
        self._state = state

    @property
    def start_time(self):
        """Gets the start_time of this ListRtcUserListRequest.

        查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认读取过去1小时数据数据。 

        :return: The start_time of this ListRtcUserListRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListRtcUserListRequest.

        查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认读取过去1小时数据数据。 

        :param start_time: The start_time of this ListRtcUserListRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListRtcUserListRequest.

        查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认为当前时间。 

        :return: The end_time of this ListRtcUserListRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListRtcUserListRequest.

        查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不写默认为当前时间。 

        :param end_time: The end_time of this ListRtcUserListRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ListRtcUserListRequest.

        查询结果限制 

        :return: The limit of this ListRtcUserListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRtcUserListRequest.

        查询结果限制 

        :param limit: The limit of this ListRtcUserListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListRtcUserListRequest.

        查询偏移量 

        :return: The offset of this ListRtcUserListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRtcUserListRequest.

        查询偏移量 

        :param offset: The offset of this ListRtcUserListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def type(self):
        """Gets the type of this ListRtcUserListRequest.

        查询模式，取值如下： - detail：会话级 - summary：用户级（默认） 

        :return: The type of this ListRtcUserListRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListRtcUserListRequest.

        查询模式，取值如下： - detail：会话级 - summary：用户级（默认） 

        :param type: The type of this ListRtcUserListRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListRtcUserListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
