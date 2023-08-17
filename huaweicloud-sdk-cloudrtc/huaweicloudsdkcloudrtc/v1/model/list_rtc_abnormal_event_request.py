# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcAbnormalEventRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'app_id': 'str',
        'room_id': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'app_id': 'app_id',
        'room_id': 'room_id',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, project_id=None, app_id=None, room_id=None, start_time=None, end_time=None):
        """ListRtcAbnormalEventRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。
        :type project_id: str
        :param app_id: 应用id
        :type app_id: str
        :param room_id: 房间id
        :type room_id: str
        :param start_time: 起始时间。UTC时间，格式：yyyy-mm-ddThh:mm:ssZ，如2020-04-23T06:00:00Z。查询起止时间不超过1个小时，每次查询单个用户时，支持跨天查询，最长1天。 
        :type start_time: str
        :param end_time: 结束时间。UTC时间，格式：yyyy-mm-ddThh:mm:ssZ，如2020-04-23T06:00:00Z。查询起止时间不超过1个小时，每次查询单个用户时，支持跨天查询，最长1天。 
        :type end_time: str
        """
        
        

        self._project_id = None
        self._app_id = None
        self._room_id = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.project_id = project_id
        self.app_id = app_id
        if room_id is not None:
            self.room_id = room_id
        self.start_time = start_time
        self.end_time = end_time

    @property
    def project_id(self):
        """Gets the project_id of this ListRtcAbnormalEventRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。

        :return: The project_id of this ListRtcAbnormalEventRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListRtcAbnormalEventRequest.

        项目ID，获取方法请参考[获取项目ID](rtc_07_0015.xml)。

        :param project_id: The project_id of this ListRtcAbnormalEventRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def app_id(self):
        """Gets the app_id of this ListRtcAbnormalEventRequest.

        应用id

        :return: The app_id of this ListRtcAbnormalEventRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListRtcAbnormalEventRequest.

        应用id

        :param app_id: The app_id of this ListRtcAbnormalEventRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def room_id(self):
        """Gets the room_id of this ListRtcAbnormalEventRequest.

        房间id

        :return: The room_id of this ListRtcAbnormalEventRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ListRtcAbnormalEventRequest.

        房间id

        :param room_id: The room_id of this ListRtcAbnormalEventRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def start_time(self):
        """Gets the start_time of this ListRtcAbnormalEventRequest.

        起始时间。UTC时间，格式：yyyy-mm-ddThh:mm:ssZ，如2020-04-23T06:00:00Z。查询起止时间不超过1个小时，每次查询单个用户时，支持跨天查询，最长1天。 

        :return: The start_time of this ListRtcAbnormalEventRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListRtcAbnormalEventRequest.

        起始时间。UTC时间，格式：yyyy-mm-ddThh:mm:ssZ，如2020-04-23T06:00:00Z。查询起止时间不超过1个小时，每次查询单个用户时，支持跨天查询，最长1天。 

        :param start_time: The start_time of this ListRtcAbnormalEventRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListRtcAbnormalEventRequest.

        结束时间。UTC时间，格式：yyyy-mm-ddThh:mm:ssZ，如2020-04-23T06:00:00Z。查询起止时间不超过1个小时，每次查询单个用户时，支持跨天查询，最长1天。 

        :return: The end_time of this ListRtcAbnormalEventRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListRtcAbnormalEventRequest.

        结束时间。UTC时间，格式：yyyy-mm-ddThh:mm:ssZ，如2020-04-23T06:00:00Z。查询起止时间不超过1个小时，每次查询单个用户时，支持跨天查询，最长1天。 

        :param end_time: The end_time of this ListRtcAbnormalEventRequest.
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
        if not isinstance(other, ListRtcAbnormalEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
