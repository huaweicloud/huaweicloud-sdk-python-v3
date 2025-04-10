# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthCompareJob:

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
        'type': 'str',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'compute_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'compute_type': 'compute_type'
    }

    def __init__(self, id=None, type=None, status=None, start_time=None, end_time=None, compute_type=None):
        r"""HealthCompareJob

        The model defined in huaweicloud sdk

        :param id: 对比任务ID。
        :type id: str
        :param type: 对比类型： - object_comparison：对象对比。 - lines：行对比。 - account：用户对比。
        :type type: str
        :param status: 状态。 - WAITING_FOR_RUNNING：等待启动中 - RUNNING：运行中 - SUCCESSFUL：完成 - FAILED：失败 - CANCELLED：已取消 - TIMEOUT_INTERRUPT：超时中断 - FULL_DOING：全量校验中 - INCRE_DOING：增量校验中
        :type status: str
        :param start_time: 对比开始时间，UTC时间。
        :type start_time: str
        :param end_time: 对比结束时间，UTC时间。
        :type end_time: str
        :param compute_type: 对比计算资源。
        :type compute_type: str
        """
        
        

        self._id = None
        self._type = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._compute_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if compute_type is not None:
            self.compute_type = compute_type

    @property
    def id(self):
        r"""Gets the id of this HealthCompareJob.

        对比任务ID。

        :return: The id of this HealthCompareJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HealthCompareJob.

        对比任务ID。

        :param id: The id of this HealthCompareJob.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this HealthCompareJob.

        对比类型： - object_comparison：对象对比。 - lines：行对比。 - account：用户对比。

        :return: The type of this HealthCompareJob.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HealthCompareJob.

        对比类型： - object_comparison：对象对比。 - lines：行对比。 - account：用户对比。

        :param type: The type of this HealthCompareJob.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this HealthCompareJob.

        状态。 - WAITING_FOR_RUNNING：等待启动中 - RUNNING：运行中 - SUCCESSFUL：完成 - FAILED：失败 - CANCELLED：已取消 - TIMEOUT_INTERRUPT：超时中断 - FULL_DOING：全量校验中 - INCRE_DOING：增量校验中

        :return: The status of this HealthCompareJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HealthCompareJob.

        状态。 - WAITING_FOR_RUNNING：等待启动中 - RUNNING：运行中 - SUCCESSFUL：完成 - FAILED：失败 - CANCELLED：已取消 - TIMEOUT_INTERRUPT：超时中断 - FULL_DOING：全量校验中 - INCRE_DOING：增量校验中

        :param status: The status of this HealthCompareJob.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this HealthCompareJob.

        对比开始时间，UTC时间。

        :return: The start_time of this HealthCompareJob.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this HealthCompareJob.

        对比开始时间，UTC时间。

        :param start_time: The start_time of this HealthCompareJob.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this HealthCompareJob.

        对比结束时间，UTC时间。

        :return: The end_time of this HealthCompareJob.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this HealthCompareJob.

        对比结束时间，UTC时间。

        :param end_time: The end_time of this HealthCompareJob.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def compute_type(self):
        r"""Gets the compute_type of this HealthCompareJob.

        对比计算资源。

        :return: The compute_type of this HealthCompareJob.
        :rtype: str
        """
        return self._compute_type

    @compute_type.setter
    def compute_type(self, compute_type):
        r"""Sets the compute_type of this HealthCompareJob.

        对比计算资源。

        :param compute_type: The compute_type of this HealthCompareJob.
        :type compute_type: str
        """
        self._compute_type = compute_type

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
        if not isinstance(other, HealthCompareJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
