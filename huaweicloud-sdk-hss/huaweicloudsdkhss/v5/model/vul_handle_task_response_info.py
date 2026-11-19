# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulHandleTaskResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'handle_type': 'str',
        'status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'vul_types': 'list[str]',
        'ready_num': 'int',
        'running_num': 'int',
        'success_num': 'int',
        'failed_num': 'int',
        'estimated_time': 'float'
    }

    attribute_map = {
        'id': 'id',
        'handle_type': 'handle_type',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'vul_types': 'vul_types',
        'ready_num': 'ready_num',
        'running_num': 'running_num',
        'success_num': 'success_num',
        'failed_num': 'failed_num',
        'estimated_time': 'estimated_time'
    }

    def __init__(self, id=None, handle_type=None, status=None, start_time=None, end_time=None, vul_types=None, ready_num=None, running_num=None, success_num=None, failed_num=None, estimated_time=None):
        r"""VulHandleTaskResponseInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 任务ID **取值范围**: 字符长度1-64位 
        :type id: str
        :param handle_type: **参数解释**: 处置任务类型 **取值范围**: - immediate_repair：立即修复。 - verify：验证。 
        :type handle_type: str
        :param status: **参数解释**: 任务状态 **取值范围**: - running：执行中。 - finished：已完成。 
        :type status: str
        :param start_time: **参数解释**: 任务开始时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type start_time: int
        :param end_time: **参数解释**: 任务结束时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type end_time: int
        :param vul_types: **参数解释**: 任务涉及的漏洞类型列表 **取值范围**: 最小值0，最大值100 
        :type vul_types: list[str]
        :param ready_num: **参数解释**: 等待执行的数量 **取值范围**: 最小值0，最大值2147483647 
        :type ready_num: int
        :param running_num: **参数解释**: 执行中的数量 **取值范围**: 最小值0，最大值2147483647 
        :type running_num: int
        :param success_num: **参数解释**: 执行成功的数量 **取值范围**: 最小值0，最大值2147483647 
        :type success_num: int
        :param failed_num: **参数解释**: 执行失败的数量 **取值范围**: 最小值0，最大值2147483647 
        :type failed_num: int
        :param estimated_time: **参数解释**: 预计还需要多长时间 **取值范围**: 最小值0，最大值604800 
        :type estimated_time: float
        """
        
        

        self._id = None
        self._handle_type = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._vul_types = None
        self._ready_num = None
        self._running_num = None
        self._success_num = None
        self._failed_num = None
        self._estimated_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if handle_type is not None:
            self.handle_type = handle_type
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if vul_types is not None:
            self.vul_types = vul_types
        if ready_num is not None:
            self.ready_num = ready_num
        if running_num is not None:
            self.running_num = running_num
        if success_num is not None:
            self.success_num = success_num
        if failed_num is not None:
            self.failed_num = failed_num
        if estimated_time is not None:
            self.estimated_time = estimated_time

    @property
    def id(self):
        r"""Gets the id of this VulHandleTaskResponseInfo.

        **参数解释**: 任务ID **取值范围**: 字符长度1-64位 

        :return: The id of this VulHandleTaskResponseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VulHandleTaskResponseInfo.

        **参数解释**: 任务ID **取值范围**: 字符长度1-64位 

        :param id: The id of this VulHandleTaskResponseInfo.
        :type id: str
        """
        self._id = id

    @property
    def handle_type(self):
        r"""Gets the handle_type of this VulHandleTaskResponseInfo.

        **参数解释**: 处置任务类型 **取值范围**: - immediate_repair：立即修复。 - verify：验证。 

        :return: The handle_type of this VulHandleTaskResponseInfo.
        :rtype: str
        """
        return self._handle_type

    @handle_type.setter
    def handle_type(self, handle_type):
        r"""Sets the handle_type of this VulHandleTaskResponseInfo.

        **参数解释**: 处置任务类型 **取值范围**: - immediate_repair：立即修复。 - verify：验证。 

        :param handle_type: The handle_type of this VulHandleTaskResponseInfo.
        :type handle_type: str
        """
        self._handle_type = handle_type

    @property
    def status(self):
        r"""Gets the status of this VulHandleTaskResponseInfo.

        **参数解释**: 任务状态 **取值范围**: - running：执行中。 - finished：已完成。 

        :return: The status of this VulHandleTaskResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulHandleTaskResponseInfo.

        **参数解释**: 任务状态 **取值范围**: - running：执行中。 - finished：已完成。 

        :param status: The status of this VulHandleTaskResponseInfo.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this VulHandleTaskResponseInfo.

        **参数解释**: 任务开始时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The start_time of this VulHandleTaskResponseInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this VulHandleTaskResponseInfo.

        **参数解释**: 任务开始时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param start_time: The start_time of this VulHandleTaskResponseInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this VulHandleTaskResponseInfo.

        **参数解释**: 任务结束时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The end_time of this VulHandleTaskResponseInfo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this VulHandleTaskResponseInfo.

        **参数解释**: 任务结束时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param end_time: The end_time of this VulHandleTaskResponseInfo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def vul_types(self):
        r"""Gets the vul_types of this VulHandleTaskResponseInfo.

        **参数解释**: 任务涉及的漏洞类型列表 **取值范围**: 最小值0，最大值100 

        :return: The vul_types of this VulHandleTaskResponseInfo.
        :rtype: list[str]
        """
        return self._vul_types

    @vul_types.setter
    def vul_types(self, vul_types):
        r"""Sets the vul_types of this VulHandleTaskResponseInfo.

        **参数解释**: 任务涉及的漏洞类型列表 **取值范围**: 最小值0，最大值100 

        :param vul_types: The vul_types of this VulHandleTaskResponseInfo.
        :type vul_types: list[str]
        """
        self._vul_types = vul_types

    @property
    def ready_num(self):
        r"""Gets the ready_num of this VulHandleTaskResponseInfo.

        **参数解释**: 等待执行的数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The ready_num of this VulHandleTaskResponseInfo.
        :rtype: int
        """
        return self._ready_num

    @ready_num.setter
    def ready_num(self, ready_num):
        r"""Sets the ready_num of this VulHandleTaskResponseInfo.

        **参数解释**: 等待执行的数量 **取值范围**: 最小值0，最大值2147483647 

        :param ready_num: The ready_num of this VulHandleTaskResponseInfo.
        :type ready_num: int
        """
        self._ready_num = ready_num

    @property
    def running_num(self):
        r"""Gets the running_num of this VulHandleTaskResponseInfo.

        **参数解释**: 执行中的数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The running_num of this VulHandleTaskResponseInfo.
        :rtype: int
        """
        return self._running_num

    @running_num.setter
    def running_num(self, running_num):
        r"""Sets the running_num of this VulHandleTaskResponseInfo.

        **参数解释**: 执行中的数量 **取值范围**: 最小值0，最大值2147483647 

        :param running_num: The running_num of this VulHandleTaskResponseInfo.
        :type running_num: int
        """
        self._running_num = running_num

    @property
    def success_num(self):
        r"""Gets the success_num of this VulHandleTaskResponseInfo.

        **参数解释**: 执行成功的数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The success_num of this VulHandleTaskResponseInfo.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        r"""Sets the success_num of this VulHandleTaskResponseInfo.

        **参数解释**: 执行成功的数量 **取值范围**: 最小值0，最大值2147483647 

        :param success_num: The success_num of this VulHandleTaskResponseInfo.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def failed_num(self):
        r"""Gets the failed_num of this VulHandleTaskResponseInfo.

        **参数解释**: 执行失败的数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The failed_num of this VulHandleTaskResponseInfo.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        r"""Sets the failed_num of this VulHandleTaskResponseInfo.

        **参数解释**: 执行失败的数量 **取值范围**: 最小值0，最大值2147483647 

        :param failed_num: The failed_num of this VulHandleTaskResponseInfo.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def estimated_time(self):
        r"""Gets the estimated_time of this VulHandleTaskResponseInfo.

        **参数解释**: 预计还需要多长时间 **取值范围**: 最小值0，最大值604800 

        :return: The estimated_time of this VulHandleTaskResponseInfo.
        :rtype: float
        """
        return self._estimated_time

    @estimated_time.setter
    def estimated_time(self, estimated_time):
        r"""Sets the estimated_time of this VulHandleTaskResponseInfo.

        **参数解释**: 预计还需要多长时间 **取值范围**: 最小值0，最大值604800 

        :param estimated_time: The estimated_time of this VulHandleTaskResponseInfo.
        :type estimated_time: float
        """
        self._estimated_time = estimated_time

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
        if not isinstance(other, VulHandleTaskResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
