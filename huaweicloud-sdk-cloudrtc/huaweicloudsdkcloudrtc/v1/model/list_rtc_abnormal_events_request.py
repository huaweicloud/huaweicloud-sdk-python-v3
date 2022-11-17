# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcAbnormalEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app': 'str',
        'room_id': 'str',
        'uid': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'app': 'app',
        'room_id': 'room_id',
        'uid': 'uid',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, app=None, room_id=None, uid=None, start_time=None, end_time=None, limit=None, offset=None):
        """ListRtcAbnormalEventsRequest

        The model defined in huaweicloud sdk

        :param app: 应用ID 
        :type app: str
        :param room_id: 房间ID 
        :type room_id: str
        :param uid: 用户ID 
        :type uid: str
        :param start_time: 查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不填写则默认读取过去1小时数据数据。 
        :type start_time: str
        :param end_time: 查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z，不填写则默认为当前时间。 
        :type end_time: str
        :param limit: 查询结果条数 
        :type limit: int
        :param offset: 查询偏移量 
        :type offset: int
        """
        
        

        self._app = None
        self._room_id = None
        self._uid = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.app = app
        if room_id is not None:
            self.room_id = room_id
        if uid is not None:
            self.uid = uid
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def app(self):
        """Gets the app of this ListRtcAbnormalEventsRequest.

        应用ID 

        :return: The app of this ListRtcAbnormalEventsRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListRtcAbnormalEventsRequest.

        应用ID 

        :param app: The app of this ListRtcAbnormalEventsRequest.
        :type app: str
        """
        self._app = app

    @property
    def room_id(self):
        """Gets the room_id of this ListRtcAbnormalEventsRequest.

        房间ID 

        :return: The room_id of this ListRtcAbnormalEventsRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ListRtcAbnormalEventsRequest.

        房间ID 

        :param room_id: The room_id of this ListRtcAbnormalEventsRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def uid(self):
        """Gets the uid of this ListRtcAbnormalEventsRequest.

        用户ID 

        :return: The uid of this ListRtcAbnormalEventsRequest.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ListRtcAbnormalEventsRequest.

        用户ID 

        :param uid: The uid of this ListRtcAbnormalEventsRequest.
        :type uid: str
        """
        self._uid = uid

    @property
    def start_time(self):
        """Gets the start_time of this ListRtcAbnormalEventsRequest.

        查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不填写则默认读取过去1小时数据数据。 

        :return: The start_time of this ListRtcAbnormalEventsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListRtcAbnormalEventsRequest.

        查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不填写则默认读取过去1小时数据数据。 

        :param start_time: The start_time of this ListRtcAbnormalEventsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListRtcAbnormalEventsRequest.

        查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z，不填写则默认为当前时间。 

        :return: The end_time of this ListRtcAbnormalEventsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListRtcAbnormalEventsRequest.

        查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z，不填写则默认为当前时间。 

        :param end_time: The end_time of this ListRtcAbnormalEventsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ListRtcAbnormalEventsRequest.

        查询结果条数 

        :return: The limit of this ListRtcAbnormalEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRtcAbnormalEventsRequest.

        查询结果条数 

        :param limit: The limit of this ListRtcAbnormalEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListRtcAbnormalEventsRequest.

        查询偏移量 

        :return: The offset of this ListRtcAbnormalEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRtcAbnormalEventsRequest.

        查询偏移量 

        :param offset: The offset of this ListRtcAbnormalEventsRequest.
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
        if not isinstance(other, ListRtcAbnormalEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
