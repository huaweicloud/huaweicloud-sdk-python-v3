# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcAbnormalEventDimensionRequest:

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
        'dimension': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'app': 'app',
        'room_id': 'room_id',
        'dimension': 'dimension',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, app=None, room_id=None, dimension=None, start_time=None, end_time=None):
        """ListRtcAbnormalEventDimensionRequest

        The model defined in huaweicloud sdk

        :param app: 应用ID 
        :type app: str
        :param room_id: 房间ID 
        :type room_id: str
        :param dimension: 分组类型，支持同时指定两种类型 - abnormal_type：异常类型 - abnormal_factor：异常因素 
        :type dimension: str
        :param start_time: 查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不填写则默认读取过去1小时数据数据。 
        :type start_time: str
        :param end_time: 查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z，不填写则默认为当前时间。 
        :type end_time: str
        """
        
        

        self._app = None
        self._room_id = None
        self._dimension = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.app = app
        if room_id is not None:
            self.room_id = room_id
        if dimension is not None:
            self.dimension = dimension
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def app(self):
        """Gets the app of this ListRtcAbnormalEventDimensionRequest.

        应用ID 

        :return: The app of this ListRtcAbnormalEventDimensionRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListRtcAbnormalEventDimensionRequest.

        应用ID 

        :param app: The app of this ListRtcAbnormalEventDimensionRequest.
        :type app: str
        """
        self._app = app

    @property
    def room_id(self):
        """Gets the room_id of this ListRtcAbnormalEventDimensionRequest.

        房间ID 

        :return: The room_id of this ListRtcAbnormalEventDimensionRequest.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ListRtcAbnormalEventDimensionRequest.

        房间ID 

        :param room_id: The room_id of this ListRtcAbnormalEventDimensionRequest.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def dimension(self):
        """Gets the dimension of this ListRtcAbnormalEventDimensionRequest.

        分组类型，支持同时指定两种类型 - abnormal_type：异常类型 - abnormal_factor：异常因素 

        :return: The dimension of this ListRtcAbnormalEventDimensionRequest.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this ListRtcAbnormalEventDimensionRequest.

        分组类型，支持同时指定两种类型 - abnormal_type：异常类型 - abnormal_factor：异常因素 

        :param dimension: The dimension of this ListRtcAbnormalEventDimensionRequest.
        :type dimension: str
        """
        self._dimension = dimension

    @property
    def start_time(self):
        """Gets the start_time of this ListRtcAbnormalEventDimensionRequest.

        查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不填写则默认读取过去1小时数据数据。 

        :return: The start_time of this ListRtcAbnormalEventDimensionRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListRtcAbnormalEventDimensionRequest.

        查询起始时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T06:00:00Z，不填写则默认读取过去1小时数据数据。 

        :param start_time: The start_time of this ListRtcAbnormalEventDimensionRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListRtcAbnormalEventDimensionRequest.

        查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z，不填写则默认为当前时间。 

        :return: The end_time of this ListRtcAbnormalEventDimensionRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListRtcAbnormalEventDimensionRequest.

        查询结束时间。UTC时间，格式：YYYY-MM-DDThh:mm:ssZ，如2020-04-23T07:00:00Z，不填写则默认为当前时间。 

        :param end_time: The end_time of this ListRtcAbnormalEventDimensionRequest.
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
        if not isinstance(other, ListRtcAbnormalEventDimensionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
