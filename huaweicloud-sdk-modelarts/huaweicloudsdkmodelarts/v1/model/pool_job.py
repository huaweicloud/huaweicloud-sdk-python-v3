# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_timestamp': 'int',
        'end_timestamp': 'int',
        'job_id': 'str',
        'job_name': 'str',
        'involved_objects': 'str',
        'inputs': 'str',
        'phase': 'str',
        'suspend': 'bool',
        'type': 'str',
        'conditions': 'str',
        'message': 'str'
    }

    attribute_map = {
        'start_timestamp': 'startTimestamp',
        'end_timestamp': 'endTimestamp',
        'job_id': 'jobId',
        'job_name': 'jobName',
        'involved_objects': 'involvedObjects',
        'inputs': 'inputs',
        'phase': 'phase',
        'suspend': 'suspend',
        'type': 'type',
        'conditions': 'conditions',
        'message': 'message'
    }

    def __init__(self, start_timestamp=None, end_timestamp=None, job_id=None, job_name=None, involved_objects=None, inputs=None, phase=None, suspend=None, type=None, conditions=None, message=None):
        r"""PoolJob

        The model defined in huaweicloud sdk

        :param start_timestamp: **参数解释**： job开始处理时间，单位毫秒。 **取值范围**： 不涉及。
        :type start_timestamp: int
        :param end_timestamp: **参数解释**： Job结束时间，单位毫秒。 **取值范围**： 不涉及。
        :type end_timestamp: int
        :param job_id: **参数解释**： 任务ID。 **取值范围**： 不涉及。
        :type job_id: str
        :param job_name: **参数解释**： 任务名称。 **取值范围**： 不涉及。
        :type job_name: str
        :param involved_objects: **参数解释**： Job关联的资源，比如资源池描述。 **取值范围**： 不涉及。
        :type involved_objects: str
        :param inputs: **参数解释**： Job输入参数。 **取值范围**： 不涉及。
        :type inputs: str
        :param phase: **参数解释**： Job状态。 **取值范围**： 可选值如下： - Running：任务正在运行中。 - Success：任务执行成功。 - Failed：任务执行失败。
        :type phase: str
        :param suspend: **参数解释**： Job是否被挂起。 **取值范围**： 不涉及。
        :type suspend: bool
        :param type: **参数解释**： Job类型。 **取值范围**： 不涉及。
        :type type: str
        :param conditions: **参数解释**： Job的执行过程信息。 **取值范围**： 不涉及。
        :type conditions: str
        :param message: **参数解释**： Job执行失败时返回执行信息。 **取值范围**： 不涉及。
        :type message: str
        """
        
        

        self._start_timestamp = None
        self._end_timestamp = None
        self._job_id = None
        self._job_name = None
        self._involved_objects = None
        self._inputs = None
        self._phase = None
        self._suspend = None
        self._type = None
        self._conditions = None
        self._message = None
        self.discriminator = None

        if start_timestamp is not None:
            self.start_timestamp = start_timestamp
        if end_timestamp is not None:
            self.end_timestamp = end_timestamp
        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if involved_objects is not None:
            self.involved_objects = involved_objects
        if inputs is not None:
            self.inputs = inputs
        if phase is not None:
            self.phase = phase
        if suspend is not None:
            self.suspend = suspend
        if type is not None:
            self.type = type
        if conditions is not None:
            self.conditions = conditions
        if message is not None:
            self.message = message

    @property
    def start_timestamp(self):
        r"""Gets the start_timestamp of this PoolJob.

        **参数解释**： job开始处理时间，单位毫秒。 **取值范围**： 不涉及。

        :return: The start_timestamp of this PoolJob.
        :rtype: int
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        r"""Sets the start_timestamp of this PoolJob.

        **参数解释**： job开始处理时间，单位毫秒。 **取值范围**： 不涉及。

        :param start_timestamp: The start_timestamp of this PoolJob.
        :type start_timestamp: int
        """
        self._start_timestamp = start_timestamp

    @property
    def end_timestamp(self):
        r"""Gets the end_timestamp of this PoolJob.

        **参数解释**： Job结束时间，单位毫秒。 **取值范围**： 不涉及。

        :return: The end_timestamp of this PoolJob.
        :rtype: int
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        r"""Sets the end_timestamp of this PoolJob.

        **参数解释**： Job结束时间，单位毫秒。 **取值范围**： 不涉及。

        :param end_timestamp: The end_timestamp of this PoolJob.
        :type end_timestamp: int
        """
        self._end_timestamp = end_timestamp

    @property
    def job_id(self):
        r"""Gets the job_id of this PoolJob.

        **参数解释**： 任务ID。 **取值范围**： 不涉及。

        :return: The job_id of this PoolJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this PoolJob.

        **参数解释**： 任务ID。 **取值范围**： 不涉及。

        :param job_id: The job_id of this PoolJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this PoolJob.

        **参数解释**： 任务名称。 **取值范围**： 不涉及。

        :return: The job_name of this PoolJob.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this PoolJob.

        **参数解释**： 任务名称。 **取值范围**： 不涉及。

        :param job_name: The job_name of this PoolJob.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def involved_objects(self):
        r"""Gets the involved_objects of this PoolJob.

        **参数解释**： Job关联的资源，比如资源池描述。 **取值范围**： 不涉及。

        :return: The involved_objects of this PoolJob.
        :rtype: str
        """
        return self._involved_objects

    @involved_objects.setter
    def involved_objects(self, involved_objects):
        r"""Sets the involved_objects of this PoolJob.

        **参数解释**： Job关联的资源，比如资源池描述。 **取值范围**： 不涉及。

        :param involved_objects: The involved_objects of this PoolJob.
        :type involved_objects: str
        """
        self._involved_objects = involved_objects

    @property
    def inputs(self):
        r"""Gets the inputs of this PoolJob.

        **参数解释**： Job输入参数。 **取值范围**： 不涉及。

        :return: The inputs of this PoolJob.
        :rtype: str
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this PoolJob.

        **参数解释**： Job输入参数。 **取值范围**： 不涉及。

        :param inputs: The inputs of this PoolJob.
        :type inputs: str
        """
        self._inputs = inputs

    @property
    def phase(self):
        r"""Gets the phase of this PoolJob.

        **参数解释**： Job状态。 **取值范围**： 可选值如下： - Running：任务正在运行中。 - Success：任务执行成功。 - Failed：任务执行失败。

        :return: The phase of this PoolJob.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this PoolJob.

        **参数解释**： Job状态。 **取值范围**： 可选值如下： - Running：任务正在运行中。 - Success：任务执行成功。 - Failed：任务执行失败。

        :param phase: The phase of this PoolJob.
        :type phase: str
        """
        self._phase = phase

    @property
    def suspend(self):
        r"""Gets the suspend of this PoolJob.

        **参数解释**： Job是否被挂起。 **取值范围**： 不涉及。

        :return: The suspend of this PoolJob.
        :rtype: bool
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        r"""Sets the suspend of this PoolJob.

        **参数解释**： Job是否被挂起。 **取值范围**： 不涉及。

        :param suspend: The suspend of this PoolJob.
        :type suspend: bool
        """
        self._suspend = suspend

    @property
    def type(self):
        r"""Gets the type of this PoolJob.

        **参数解释**： Job类型。 **取值范围**： 不涉及。

        :return: The type of this PoolJob.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PoolJob.

        **参数解释**： Job类型。 **取值范围**： 不涉及。

        :param type: The type of this PoolJob.
        :type type: str
        """
        self._type = type

    @property
    def conditions(self):
        r"""Gets the conditions of this PoolJob.

        **参数解释**： Job的执行过程信息。 **取值范围**： 不涉及。

        :return: The conditions of this PoolJob.
        :rtype: str
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this PoolJob.

        **参数解释**： Job的执行过程信息。 **取值范围**： 不涉及。

        :param conditions: The conditions of this PoolJob.
        :type conditions: str
        """
        self._conditions = conditions

    @property
    def message(self):
        r"""Gets the message of this PoolJob.

        **参数解释**： Job执行失败时返回执行信息。 **取值范围**： 不涉及。

        :return: The message of this PoolJob.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this PoolJob.

        **参数解释**： Job执行失败时返回执行信息。 **取值范围**： 不涉及。

        :param message: The message of this PoolJob.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, PoolJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
