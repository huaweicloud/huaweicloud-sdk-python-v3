# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogicalClusterPlanActions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'next_fire_time': 'str',
        'failed_reason': 'str',
        'id': 'str',
        'type': 'str',
        'strategy': 'str',
        'status': 'str',
        'pre_fire_time': 'date'
    }

    attribute_map = {
        'next_fire_time': 'next_fire_time',
        'failed_reason': 'failed_reason',
        'id': 'id',
        'type': 'type',
        'strategy': 'strategy',
        'status': 'status',
        'pre_fire_time': 'pre_fire_time'
    }

    def __init__(self, next_fire_time=None, failed_reason=None, id=None, type=None, strategy=None, status=None, pre_fire_time=None):
        r"""LogicalClusterPlanActions

        The model defined in huaweicloud sdk

        :param next_fire_time: **参数解释**： 下一次触发时间。 **取值范围**： 不涉及。
        :type next_fire_time: str
        :param failed_reason: **参数解释**： 失败原因。 **取值范围**： 不涉及。
        :type failed_reason: str
        :param id: **参数解释**： 任务ID。 **取值范围**： 不涉及。
        :type id: str
        :param type: **参数解释**： 类型。 **取值范围**： create：创建 delete：删除
        :type type: str
        :param strategy: **参数解释**： 周期信息。Cron表达式：如\&quot;0 0 0 ? * 3\&quot;。 **取值范围**： 不涉及。
        :type strategy: str
        :param status: **参数解释**： 任务状态。 **取值范围**： running|waiting|deleted|finished|disabled|failed。
        :type status: str
        :param pre_fire_time: **参数解释**： 上一次触发时间。 **取值范围**： 不涉及。
        :type pre_fire_time: date
        """
        
        

        self._next_fire_time = None
        self._failed_reason = None
        self._id = None
        self._type = None
        self._strategy = None
        self._status = None
        self._pre_fire_time = None
        self.discriminator = None

        if next_fire_time is not None:
            self.next_fire_time = next_fire_time
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if strategy is not None:
            self.strategy = strategy
        if status is not None:
            self.status = status
        if pre_fire_time is not None:
            self.pre_fire_time = pre_fire_time

    @property
    def next_fire_time(self):
        r"""Gets the next_fire_time of this LogicalClusterPlanActions.

        **参数解释**： 下一次触发时间。 **取值范围**： 不涉及。

        :return: The next_fire_time of this LogicalClusterPlanActions.
        :rtype: str
        """
        return self._next_fire_time

    @next_fire_time.setter
    def next_fire_time(self, next_fire_time):
        r"""Sets the next_fire_time of this LogicalClusterPlanActions.

        **参数解释**： 下一次触发时间。 **取值范围**： 不涉及。

        :param next_fire_time: The next_fire_time of this LogicalClusterPlanActions.
        :type next_fire_time: str
        """
        self._next_fire_time = next_fire_time

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this LogicalClusterPlanActions.

        **参数解释**： 失败原因。 **取值范围**： 不涉及。

        :return: The failed_reason of this LogicalClusterPlanActions.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this LogicalClusterPlanActions.

        **参数解释**： 失败原因。 **取值范围**： 不涉及。

        :param failed_reason: The failed_reason of this LogicalClusterPlanActions.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def id(self):
        r"""Gets the id of this LogicalClusterPlanActions.

        **参数解释**： 任务ID。 **取值范围**： 不涉及。

        :return: The id of this LogicalClusterPlanActions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LogicalClusterPlanActions.

        **参数解释**： 任务ID。 **取值范围**： 不涉及。

        :param id: The id of this LogicalClusterPlanActions.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this LogicalClusterPlanActions.

        **参数解释**： 类型。 **取值范围**： create：创建 delete：删除

        :return: The type of this LogicalClusterPlanActions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this LogicalClusterPlanActions.

        **参数解释**： 类型。 **取值范围**： create：创建 delete：删除

        :param type: The type of this LogicalClusterPlanActions.
        :type type: str
        """
        self._type = type

    @property
    def strategy(self):
        r"""Gets the strategy of this LogicalClusterPlanActions.

        **参数解释**： 周期信息。Cron表达式：如\"0 0 0 ? * 3\"。 **取值范围**： 不涉及。

        :return: The strategy of this LogicalClusterPlanActions.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this LogicalClusterPlanActions.

        **参数解释**： 周期信息。Cron表达式：如\"0 0 0 ? * 3\"。 **取值范围**： 不涉及。

        :param strategy: The strategy of this LogicalClusterPlanActions.
        :type strategy: str
        """
        self._strategy = strategy

    @property
    def status(self):
        r"""Gets the status of this LogicalClusterPlanActions.

        **参数解释**： 任务状态。 **取值范围**： running|waiting|deleted|finished|disabled|failed。

        :return: The status of this LogicalClusterPlanActions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this LogicalClusterPlanActions.

        **参数解释**： 任务状态。 **取值范围**： running|waiting|deleted|finished|disabled|failed。

        :param status: The status of this LogicalClusterPlanActions.
        :type status: str
        """
        self._status = status

    @property
    def pre_fire_time(self):
        r"""Gets the pre_fire_time of this LogicalClusterPlanActions.

        **参数解释**： 上一次触发时间。 **取值范围**： 不涉及。

        :return: The pre_fire_time of this LogicalClusterPlanActions.
        :rtype: date
        """
        return self._pre_fire_time

    @pre_fire_time.setter
    def pre_fire_time(self, pre_fire_time):
        r"""Sets the pre_fire_time of this LogicalClusterPlanActions.

        **参数解释**： 上一次触发时间。 **取值范围**： 不涉及。

        :param pre_fire_time: The pre_fire_time of this LogicalClusterPlanActions.
        :type pre_fire_time: date
        """
        self._pre_fire_time = pre_fire_time

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
        if not isinstance(other, LogicalClusterPlanActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
