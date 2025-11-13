# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUsageDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'x_app_user_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'user_id': 'str',
        'resource_type': 'str',
        'business_type': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'x_app_user_id': 'X-App-UserId',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'user_id': 'user_id',
        'resource_type': 'resource_type',
        'business_type': 'business_type',
        'unit': 'unit'
    }

    def __init__(self, limit=None, offset=None, x_app_user_id=None, start_time=None, end_time=None, user_id=None, resource_type=None, business_type=None, unit=None):
        r"""ShowUsageDataRequest

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param start_time: 查询时间段开始时间,格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;
        :type start_time: str
        :param end_time: 查询时间段结束时间,格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;
        :type end_time: str
        :param user_id: 用户id(仅开启了子账号隔离功能的主账号携带才生效)
        :type user_id: str
        :param resource_type: 资源类型 * video_time_2d_model：分身数字人视频制作 * video_time_flexus_2d_model：分身数字人视频制作flexus版
        :type resource_type: str
        :param business_type: 业务类型 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作
        :type business_type: str
        :param unit: 使用量的单位。 * MIN：分钟 * HOUR：小时
        :type unit: str
        """
        
        

        self._limit = None
        self._offset = None
        self._x_app_user_id = None
        self._start_time = None
        self._end_time = None
        self._user_id = None
        self._resource_type = None
        self._business_type = None
        self._unit = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        self.start_time = start_time
        self.end_time = end_time
        if user_id is not None:
            self.user_id = user_id
        if resource_type is not None:
            self.resource_type = resource_type
        if business_type is not None:
            self.business_type = business_type
        if unit is not None:
            self.unit = unit

    @property
    def limit(self):
        r"""Gets the limit of this ShowUsageDataRequest.

        每页显示的条目数量。

        :return: The limit of this ShowUsageDataRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowUsageDataRequest.

        每页显示的条目数量。

        :param limit: The limit of this ShowUsageDataRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowUsageDataRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ShowUsageDataRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowUsageDataRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ShowUsageDataRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ShowUsageDataRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ShowUsageDataRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ShowUsageDataRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ShowUsageDataRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowUsageDataRequest.

        查询时间段开始时间,格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :return: The start_time of this ShowUsageDataRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowUsageDataRequest.

        查询时间段开始时间,格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :param start_time: The start_time of this ShowUsageDataRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowUsageDataRequest.

        查询时间段结束时间,格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :return: The end_time of this ShowUsageDataRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowUsageDataRequest.

        查询时间段结束时间,格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :param end_time: The end_time of this ShowUsageDataRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def user_id(self):
        r"""Gets the user_id of this ShowUsageDataRequest.

        用户id(仅开启了子账号隔离功能的主账号携带才生效)

        :return: The user_id of this ShowUsageDataRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ShowUsageDataRequest.

        用户id(仅开启了子账号隔离功能的主账号携带才生效)

        :param user_id: The user_id of this ShowUsageDataRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowUsageDataRequest.

        资源类型 * video_time_2d_model：分身数字人视频制作 * video_time_flexus_2d_model：分身数字人视频制作flexus版

        :return: The resource_type of this ShowUsageDataRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowUsageDataRequest.

        资源类型 * video_time_2d_model：分身数字人视频制作 * video_time_flexus_2d_model：分身数字人视频制作flexus版

        :param resource_type: The resource_type of this ShowUsageDataRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def business_type(self):
        r"""Gets the business_type of this ShowUsageDataRequest.

        业务类型 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作

        :return: The business_type of this ShowUsageDataRequest.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this ShowUsageDataRequest.

        业务类型 * LIVE_2D：分身数字人视频直播 * VIDEO_2D：分身数字人视频制作

        :param business_type: The business_type of this ShowUsageDataRequest.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def unit(self):
        r"""Gets the unit of this ShowUsageDataRequest.

        使用量的单位。 * MIN：分钟 * HOUR：小时

        :return: The unit of this ShowUsageDataRequest.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ShowUsageDataRequest.

        使用量的单位。 * MIN：分钟 * HOUR：小时

        :param unit: The unit of this ShowUsageDataRequest.
        :type unit: str
        """
        self._unit = unit

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowUsageDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
