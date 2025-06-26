# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlanStage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'month': 'str',
        'day': 'str',
        'plan_id': 'str',
        'stage_id': 'str',
        'stage_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'next_valid_time': 'str',
        'queue_list': 'list[QueueResourceItem]'
    }

    attribute_map = {
        'month': 'month',
        'day': 'day',
        'plan_id': 'plan_id',
        'stage_id': 'stage_id',
        'stage_name': 'stage_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'next_valid_time': 'next_valid_time',
        'queue_list': 'queue_list'
    }

    def __init__(self, month=None, day=None, plan_id=None, stage_id=None, stage_name=None, start_time=None, end_time=None, next_valid_time=None, queue_list=None):
        r"""PlanStage

        The model defined in huaweicloud sdk

        :param month: **参数解释**： 计划月份。 **取值范围**： 不涉及。
        :type month: str
        :param day: **参数解释**： 计划日期。 **取值范围**： 不涉及。
        :type day: str
        :param plan_id: **参数解释**： 计划ID。 **取值范围**： 不涉及。
        :type plan_id: str
        :param stage_id: **参数解释**： 计划阶段ID。 **取值范围**： 不涉及。
        :type stage_id: str
        :param stage_name: **参数解释**： 计划阶段名称。 **取值范围**： 不涉及。
        :type stage_name: str
        :param start_time: **参数解释**： 计划开始时间。 **取值范围**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 计划结束时间。 **取值范围**： 不涉及。
        :type end_time: str
        :param next_valid_time: **参数解释**： 下次校验时间。 **取值范围**： 不涉及。
        :type next_valid_time: str
        :param queue_list: **参数解释**： 资源队列列表。 **取值范围**： 不涉及。
        :type queue_list: list[:class:`huaweicloudsdkdws.v2.QueueResourceItem`]
        """
        
        

        self._month = None
        self._day = None
        self._plan_id = None
        self._stage_id = None
        self._stage_name = None
        self._start_time = None
        self._end_time = None
        self._next_valid_time = None
        self._queue_list = None
        self.discriminator = None

        self.month = month
        self.day = day
        self.plan_id = plan_id
        self.stage_id = stage_id
        self.stage_name = stage_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if next_valid_time is not None:
            self.next_valid_time = next_valid_time
        if queue_list is not None:
            self.queue_list = queue_list

    @property
    def month(self):
        r"""Gets the month of this PlanStage.

        **参数解释**： 计划月份。 **取值范围**： 不涉及。

        :return: The month of this PlanStage.
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        r"""Sets the month of this PlanStage.

        **参数解释**： 计划月份。 **取值范围**： 不涉及。

        :param month: The month of this PlanStage.
        :type month: str
        """
        self._month = month

    @property
    def day(self):
        r"""Gets the day of this PlanStage.

        **参数解释**： 计划日期。 **取值范围**： 不涉及。

        :return: The day of this PlanStage.
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        r"""Sets the day of this PlanStage.

        **参数解释**： 计划日期。 **取值范围**： 不涉及。

        :param day: The day of this PlanStage.
        :type day: str
        """
        self._day = day

    @property
    def plan_id(self):
        r"""Gets the plan_id of this PlanStage.

        **参数解释**： 计划ID。 **取值范围**： 不涉及。

        :return: The plan_id of this PlanStage.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this PlanStage.

        **参数解释**： 计划ID。 **取值范围**： 不涉及。

        :param plan_id: The plan_id of this PlanStage.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def stage_id(self):
        r"""Gets the stage_id of this PlanStage.

        **参数解释**： 计划阶段ID。 **取值范围**： 不涉及。

        :return: The stage_id of this PlanStage.
        :rtype: str
        """
        return self._stage_id

    @stage_id.setter
    def stage_id(self, stage_id):
        r"""Sets the stage_id of this PlanStage.

        **参数解释**： 计划阶段ID。 **取值范围**： 不涉及。

        :param stage_id: The stage_id of this PlanStage.
        :type stage_id: str
        """
        self._stage_id = stage_id

    @property
    def stage_name(self):
        r"""Gets the stage_name of this PlanStage.

        **参数解释**： 计划阶段名称。 **取值范围**： 不涉及。

        :return: The stage_name of this PlanStage.
        :rtype: str
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name):
        r"""Sets the stage_name of this PlanStage.

        **参数解释**： 计划阶段名称。 **取值范围**： 不涉及。

        :param stage_name: The stage_name of this PlanStage.
        :type stage_name: str
        """
        self._stage_name = stage_name

    @property
    def start_time(self):
        r"""Gets the start_time of this PlanStage.

        **参数解释**： 计划开始时间。 **取值范围**： 不涉及。

        :return: The start_time of this PlanStage.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this PlanStage.

        **参数解释**： 计划开始时间。 **取值范围**： 不涉及。

        :param start_time: The start_time of this PlanStage.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this PlanStage.

        **参数解释**： 计划结束时间。 **取值范围**： 不涉及。

        :return: The end_time of this PlanStage.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this PlanStage.

        **参数解释**： 计划结束时间。 **取值范围**： 不涉及。

        :param end_time: The end_time of this PlanStage.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def next_valid_time(self):
        r"""Gets the next_valid_time of this PlanStage.

        **参数解释**： 下次校验时间。 **取值范围**： 不涉及。

        :return: The next_valid_time of this PlanStage.
        :rtype: str
        """
        return self._next_valid_time

    @next_valid_time.setter
    def next_valid_time(self, next_valid_time):
        r"""Sets the next_valid_time of this PlanStage.

        **参数解释**： 下次校验时间。 **取值范围**： 不涉及。

        :param next_valid_time: The next_valid_time of this PlanStage.
        :type next_valid_time: str
        """
        self._next_valid_time = next_valid_time

    @property
    def queue_list(self):
        r"""Gets the queue_list of this PlanStage.

        **参数解释**： 资源队列列表。 **取值范围**： 不涉及。

        :return: The queue_list of this PlanStage.
        :rtype: list[:class:`huaweicloudsdkdws.v2.QueueResourceItem`]
        """
        return self._queue_list

    @queue_list.setter
    def queue_list(self, queue_list):
        r"""Sets the queue_list of this PlanStage.

        **参数解释**： 资源队列列表。 **取值范围**： 不涉及。

        :param queue_list: The queue_list of this PlanStage.
        :type queue_list: list[:class:`huaweicloudsdkdws.v2.QueueResourceItem`]
        """
        self._queue_list = queue_list

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
        if not isinstance(other, PlanStage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
