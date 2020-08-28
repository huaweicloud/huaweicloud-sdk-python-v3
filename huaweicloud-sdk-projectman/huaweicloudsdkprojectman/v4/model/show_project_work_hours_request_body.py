# coding: utf-8

import pprint
import re

import six





class ShowProjectWorkHoursRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_ids': 'list[str]',
        'work_hours_types': 'str',
        'work_hours_dates': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'user_ids': 'user_ids',
        'work_hours_types': 'work_hours_types',
        'work_hours_dates': 'work_hours_dates',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, user_ids=None, work_hours_types=None, work_hours_dates=None, begin_time=None, end_time=None, offset='0', limit='10'):
        """ShowProjectWorkHoursRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._user_ids = None
        self._work_hours_types = None
        self._work_hours_dates = None
        self._begin_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if user_ids is not None:
            self.user_ids = user_ids
        if work_hours_types is not None:
            self.work_hours_types = work_hours_types
        if work_hours_dates is not None:
            self.work_hours_dates = work_hours_dates
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        self.offset = offset
        self.limit = limit

    @property
    def user_ids(self):
        """Gets the user_ids of this ShowProjectWorkHoursRequestBody.

        查询的用户id列表

        :return: The user_ids of this ShowProjectWorkHoursRequestBody.
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this ShowProjectWorkHoursRequestBody.

        查询的用户id列表

        :param user_ids: The user_ids of this ShowProjectWorkHoursRequestBody.
        :type: list[str]
        """
        self._user_ids = user_ids

    @property
    def work_hours_types(self):
        """Gets the work_hours_types of this ShowProjectWorkHoursRequestBody.

        工时类型，以逗号分隔,21:研发设计,22:后端开发,23:前端开发(Web),24:前端开发(小程序),25:前端开发(App),26:测试验证,27:缺陷修复,28:UI设计,29:会议,30:公共事务,31:培训,32:研究,33:其它,34:调休请假

        :return: The work_hours_types of this ShowProjectWorkHoursRequestBody.
        :rtype: str
        """
        return self._work_hours_types

    @work_hours_types.setter
    def work_hours_types(self, work_hours_types):
        """Sets the work_hours_types of this ShowProjectWorkHoursRequestBody.

        工时类型，以逗号分隔,21:研发设计,22:后端开发,23:前端开发(Web),24:前端开发(小程序),25:前端开发(App),26:测试验证,27:缺陷修复,28:UI设计,29:会议,30:公共事务,31:培训,32:研究,33:其它,34:调休请假

        :param work_hours_types: The work_hours_types of this ShowProjectWorkHoursRequestBody.
        :type: str
        """
        self._work_hours_types = work_hours_types

    @property
    def work_hours_dates(self):
        """Gets the work_hours_dates of this ShowProjectWorkHoursRequestBody.

        工时日期，以逗号分隔，年-月-日

        :return: The work_hours_dates of this ShowProjectWorkHoursRequestBody.
        :rtype: str
        """
        return self._work_hours_dates

    @work_hours_dates.setter
    def work_hours_dates(self, work_hours_dates):
        """Sets the work_hours_dates of this ShowProjectWorkHoursRequestBody.

        工时日期，以逗号分隔，年-月-日

        :param work_hours_dates: The work_hours_dates of this ShowProjectWorkHoursRequestBody.
        :type: str
        """
        self._work_hours_dates = work_hours_dates

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowProjectWorkHoursRequestBody.

        工时开始日期，年-月-日

        :return: The begin_time of this ShowProjectWorkHoursRequestBody.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowProjectWorkHoursRequestBody.

        工时开始日期，年-月-日

        :param begin_time: The begin_time of this ShowProjectWorkHoursRequestBody.
        :type: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowProjectWorkHoursRequestBody.

        工时结束日期，年-月-日

        :return: The end_time of this ShowProjectWorkHoursRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowProjectWorkHoursRequestBody.

        工时结束日期，年-月-日

        :param end_time: The end_time of this ShowProjectWorkHoursRequestBody.
        :type: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        """Gets the offset of this ShowProjectWorkHoursRequestBody.

        偏移量

        :return: The offset of this ShowProjectWorkHoursRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowProjectWorkHoursRequestBody.

        偏移量

        :param offset: The offset of this ShowProjectWorkHoursRequestBody.
        :type: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowProjectWorkHoursRequestBody.

        每页显示数量，每页最多显示100条

        :return: The limit of this ShowProjectWorkHoursRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowProjectWorkHoursRequestBody.

        每页显示数量，每页最多显示100条

        :param limit: The limit of this ShowProjectWorkHoursRequestBody.
        :type: str
        """
        self._limit = limit

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowProjectWorkHoursRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
