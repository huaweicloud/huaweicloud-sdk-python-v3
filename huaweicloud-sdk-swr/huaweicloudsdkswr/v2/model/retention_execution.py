# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetentionExecution:

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
        'policy_id': 'int',
        'dry_run': 'bool',
        'status': 'str',
        'trigger': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'policy_id': 'policy_id',
        'dry_run': 'dry_run',
        'status': 'status',
        'trigger': 'trigger',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, policy_id=None, dry_run=None, status=None, trigger=None, start_time=None, end_time=None):
        r"""RetentionExecution

        The model defined in huaweicloud sdk

        :param id: 老化策略执行记录ID
        :type id: int
        :param policy_id: 老化策略ID
        :type policy_id: int
        :param dry_run: 是否模拟运行
        :type dry_run: bool
        :param status: 执行状态，InProgress Succeed Failed Stopped
        :type status: str
        :param trigger: 触发类型，scheduled manual
        :type trigger: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        """
        
        

        self._id = None
        self._policy_id = None
        self._dry_run = None
        self._status = None
        self._trigger = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.id = id
        self.policy_id = policy_id
        self.dry_run = dry_run
        self.status = status
        self.trigger = trigger
        self.start_time = start_time
        self.end_time = end_time

    @property
    def id(self):
        r"""Gets the id of this RetentionExecution.

        老化策略执行记录ID

        :return: The id of this RetentionExecution.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RetentionExecution.

        老化策略执行记录ID

        :param id: The id of this RetentionExecution.
        :type id: int
        """
        self._id = id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this RetentionExecution.

        老化策略ID

        :return: The policy_id of this RetentionExecution.
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this RetentionExecution.

        老化策略ID

        :param policy_id: The policy_id of this RetentionExecution.
        :type policy_id: int
        """
        self._policy_id = policy_id

    @property
    def dry_run(self):
        r"""Gets the dry_run of this RetentionExecution.

        是否模拟运行

        :return: The dry_run of this RetentionExecution.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        r"""Sets the dry_run of this RetentionExecution.

        是否模拟运行

        :param dry_run: The dry_run of this RetentionExecution.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def status(self):
        r"""Gets the status of this RetentionExecution.

        执行状态，InProgress Succeed Failed Stopped

        :return: The status of this RetentionExecution.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RetentionExecution.

        执行状态，InProgress Succeed Failed Stopped

        :param status: The status of this RetentionExecution.
        :type status: str
        """
        self._status = status

    @property
    def trigger(self):
        r"""Gets the trigger of this RetentionExecution.

        触发类型，scheduled manual

        :return: The trigger of this RetentionExecution.
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this RetentionExecution.

        触发类型，scheduled manual

        :param trigger: The trigger of this RetentionExecution.
        :type trigger: str
        """
        self._trigger = trigger

    @property
    def start_time(self):
        r"""Gets the start_time of this RetentionExecution.

        开始时间

        :return: The start_time of this RetentionExecution.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this RetentionExecution.

        开始时间

        :param start_time: The start_time of this RetentionExecution.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this RetentionExecution.

        结束时间

        :return: The end_time of this RetentionExecution.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this RetentionExecution.

        结束时间

        :param end_time: The end_time of this RetentionExecution.
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
        if not isinstance(other, RetentionExecution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
