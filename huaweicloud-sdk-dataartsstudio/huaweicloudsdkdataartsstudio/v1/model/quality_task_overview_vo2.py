# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QualityTaskOverviewVO2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'category_id': 'int',
        'schedule_status': 'str',
        'schedule_period': 'str',
        'schedule_interval': 'str',
        'create_time': 'int',
        'last_run_time': 'int',
        'creator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'category_id': 'category_id',
        'schedule_status': 'schedule_status',
        'schedule_period': 'schedule_period',
        'schedule_interval': 'schedule_interval',
        'create_time': 'create_time',
        'last_run_time': 'last_run_time',
        'creator': 'creator'
    }

    def __init__(self, id=None, name=None, category_id=None, schedule_status=None, schedule_period=None, schedule_interval=None, create_time=None, last_run_time=None, creator=None):
        r"""QualityTaskOverviewVO2

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param name: name
        :type name: str
        :param category_id: 目录ID
        :type category_id: int
        :param schedule_status: 调度状态 UNKNOWN:未知,NOT_START:未启动,SCHEDULING:调度中,FINISH_SUCCESS:正常结束,KILL:手动停止,RUNNING_EXCEPTION:运行失败
        :type schedule_status: str
        :param schedule_period: 调度周期 MINUTE:按分钟调度,HOUR:按小时调度,DAY:按天调度,WEEK:按周调度
        :type schedule_period: str
        :param schedule_interval: 调度间隔 当调度周期为分钟、小时、天时，返回数值字符串，当调度周期为周时，返回具体的调度星期信息如（MONDAY,THURSDAY）
        :type schedule_interval: str
        :param create_time: 创建时间,13位时间戳(精确到毫秒)
        :type create_time: int
        :param last_run_time: 最新运行时间,13位时间戳(精确到毫秒)
        :type last_run_time: int
        :param creator: 创建者
        :type creator: str
        """
        
        

        self._id = None
        self._name = None
        self._category_id = None
        self._schedule_status = None
        self._schedule_period = None
        self._schedule_interval = None
        self._create_time = None
        self._last_run_time = None
        self._creator = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if category_id is not None:
            self.category_id = category_id
        if schedule_status is not None:
            self.schedule_status = schedule_status
        if schedule_period is not None:
            self.schedule_period = schedule_period
        if schedule_interval is not None:
            self.schedule_interval = schedule_interval
        if create_time is not None:
            self.create_time = create_time
        if last_run_time is not None:
            self.last_run_time = last_run_time
        if creator is not None:
            self.creator = creator

    @property
    def id(self):
        r"""Gets the id of this QualityTaskOverviewVO2.

        id

        :return: The id of this QualityTaskOverviewVO2.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QualityTaskOverviewVO2.

        id

        :param id: The id of this QualityTaskOverviewVO2.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this QualityTaskOverviewVO2.

        name

        :return: The name of this QualityTaskOverviewVO2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QualityTaskOverviewVO2.

        name

        :param name: The name of this QualityTaskOverviewVO2.
        :type name: str
        """
        self._name = name

    @property
    def category_id(self):
        r"""Gets the category_id of this QualityTaskOverviewVO2.

        目录ID

        :return: The category_id of this QualityTaskOverviewVO2.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this QualityTaskOverviewVO2.

        目录ID

        :param category_id: The category_id of this QualityTaskOverviewVO2.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def schedule_status(self):
        r"""Gets the schedule_status of this QualityTaskOverviewVO2.

        调度状态 UNKNOWN:未知,NOT_START:未启动,SCHEDULING:调度中,FINISH_SUCCESS:正常结束,KILL:手动停止,RUNNING_EXCEPTION:运行失败

        :return: The schedule_status of this QualityTaskOverviewVO2.
        :rtype: str
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        r"""Sets the schedule_status of this QualityTaskOverviewVO2.

        调度状态 UNKNOWN:未知,NOT_START:未启动,SCHEDULING:调度中,FINISH_SUCCESS:正常结束,KILL:手动停止,RUNNING_EXCEPTION:运行失败

        :param schedule_status: The schedule_status of this QualityTaskOverviewVO2.
        :type schedule_status: str
        """
        self._schedule_status = schedule_status

    @property
    def schedule_period(self):
        r"""Gets the schedule_period of this QualityTaskOverviewVO2.

        调度周期 MINUTE:按分钟调度,HOUR:按小时调度,DAY:按天调度,WEEK:按周调度

        :return: The schedule_period of this QualityTaskOverviewVO2.
        :rtype: str
        """
        return self._schedule_period

    @schedule_period.setter
    def schedule_period(self, schedule_period):
        r"""Sets the schedule_period of this QualityTaskOverviewVO2.

        调度周期 MINUTE:按分钟调度,HOUR:按小时调度,DAY:按天调度,WEEK:按周调度

        :param schedule_period: The schedule_period of this QualityTaskOverviewVO2.
        :type schedule_period: str
        """
        self._schedule_period = schedule_period

    @property
    def schedule_interval(self):
        r"""Gets the schedule_interval of this QualityTaskOverviewVO2.

        调度间隔 当调度周期为分钟、小时、天时，返回数值字符串，当调度周期为周时，返回具体的调度星期信息如（MONDAY,THURSDAY）

        :return: The schedule_interval of this QualityTaskOverviewVO2.
        :rtype: str
        """
        return self._schedule_interval

    @schedule_interval.setter
    def schedule_interval(self, schedule_interval):
        r"""Sets the schedule_interval of this QualityTaskOverviewVO2.

        调度间隔 当调度周期为分钟、小时、天时，返回数值字符串，当调度周期为周时，返回具体的调度星期信息如（MONDAY,THURSDAY）

        :param schedule_interval: The schedule_interval of this QualityTaskOverviewVO2.
        :type schedule_interval: str
        """
        self._schedule_interval = schedule_interval

    @property
    def create_time(self):
        r"""Gets the create_time of this QualityTaskOverviewVO2.

        创建时间,13位时间戳(精确到毫秒)

        :return: The create_time of this QualityTaskOverviewVO2.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this QualityTaskOverviewVO2.

        创建时间,13位时间戳(精确到毫秒)

        :param create_time: The create_time of this QualityTaskOverviewVO2.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_run_time(self):
        r"""Gets the last_run_time of this QualityTaskOverviewVO2.

        最新运行时间,13位时间戳(精确到毫秒)

        :return: The last_run_time of this QualityTaskOverviewVO2.
        :rtype: int
        """
        return self._last_run_time

    @last_run_time.setter
    def last_run_time(self, last_run_time):
        r"""Sets the last_run_time of this QualityTaskOverviewVO2.

        最新运行时间,13位时间戳(精确到毫秒)

        :param last_run_time: The last_run_time of this QualityTaskOverviewVO2.
        :type last_run_time: int
        """
        self._last_run_time = last_run_time

    @property
    def creator(self):
        r"""Gets the creator of this QualityTaskOverviewVO2.

        创建者

        :return: The creator of this QualityTaskOverviewVO2.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this QualityTaskOverviewVO2.

        创建者

        :param creator: The creator of this QualityTaskOverviewVO2.
        :type creator: str
        """
        self._creator = creator

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
        if not isinstance(other, QualityTaskOverviewVO2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
