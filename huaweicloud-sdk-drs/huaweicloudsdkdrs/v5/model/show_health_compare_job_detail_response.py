# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHealthCompareJobDetailResponse(SdkResponse):

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
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'job_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'job_name': 'job_name'
    }

    def __init__(self, id=None, type=None, start_time=None, end_time=None, status=None, job_name=None):
        """ShowHealthCompareJobDetailResponse

        The model defined in huaweicloud sdk

        :param id: 对比任务ID。
        :type id: str
        :param type: 对比类型： object_comparison：对象对比。 lines：行对比。 account：用户对比。
        :type type: str
        :param start_time: 开始时间，UTC时间，例如：2024-04-03T08:00:01Z。
        :type start_time: str
        :param end_time: 结束时间，UTC时间，例如：2024-04-03T08:00:01Z。
        :type end_time: str
        :param status: 对比任务的状态。取值： - RUNNING：运行中。 - WAITING_FOR_RUNNING：等待启动中。 - SUCCESSFUL：完成。 - FAILED：失败。 - CANCELLED：已取消。 - TIMEOUT_INTERRUPT：超时中断。 - FULL_DOING：全量校验中。 - INCRE_DOING：增量校验中。
        :type status: str
        :param job_name: 任务名称。
        :type job_name: str
        """
        
        super(ShowHealthCompareJobDetailResponse, self).__init__()

        self._id = None
        self._type = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._job_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if job_name is not None:
            self.job_name = job_name

    @property
    def id(self):
        """Gets the id of this ShowHealthCompareJobDetailResponse.

        对比任务ID。

        :return: The id of this ShowHealthCompareJobDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowHealthCompareJobDetailResponse.

        对比任务ID。

        :param id: The id of this ShowHealthCompareJobDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this ShowHealthCompareJobDetailResponse.

        对比类型： object_comparison：对象对比。 lines：行对比。 account：用户对比。

        :return: The type of this ShowHealthCompareJobDetailResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowHealthCompareJobDetailResponse.

        对比类型： object_comparison：对象对比。 lines：行对比。 account：用户对比。

        :param type: The type of this ShowHealthCompareJobDetailResponse.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        """Gets the start_time of this ShowHealthCompareJobDetailResponse.

        开始时间，UTC时间，例如：2024-04-03T08:00:01Z。

        :return: The start_time of this ShowHealthCompareJobDetailResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowHealthCompareJobDetailResponse.

        开始时间，UTC时间，例如：2024-04-03T08:00:01Z。

        :param start_time: The start_time of this ShowHealthCompareJobDetailResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowHealthCompareJobDetailResponse.

        结束时间，UTC时间，例如：2024-04-03T08:00:01Z。

        :return: The end_time of this ShowHealthCompareJobDetailResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowHealthCompareJobDetailResponse.

        结束时间，UTC时间，例如：2024-04-03T08:00:01Z。

        :param end_time: The end_time of this ShowHealthCompareJobDetailResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ShowHealthCompareJobDetailResponse.

        对比任务的状态。取值： - RUNNING：运行中。 - WAITING_FOR_RUNNING：等待启动中。 - SUCCESSFUL：完成。 - FAILED：失败。 - CANCELLED：已取消。 - TIMEOUT_INTERRUPT：超时中断。 - FULL_DOING：全量校验中。 - INCRE_DOING：增量校验中。

        :return: The status of this ShowHealthCompareJobDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowHealthCompareJobDetailResponse.

        对比任务的状态。取值： - RUNNING：运行中。 - WAITING_FOR_RUNNING：等待启动中。 - SUCCESSFUL：完成。 - FAILED：失败。 - CANCELLED：已取消。 - TIMEOUT_INTERRUPT：超时中断。 - FULL_DOING：全量校验中。 - INCRE_DOING：增量校验中。

        :param status: The status of this ShowHealthCompareJobDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def job_name(self):
        """Gets the job_name of this ShowHealthCompareJobDetailResponse.

        任务名称。

        :return: The job_name of this ShowHealthCompareJobDetailResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ShowHealthCompareJobDetailResponse.

        任务名称。

        :param job_name: The job_name of this ShowHealthCompareJobDetailResponse.
        :type job_name: str
        """
        self._job_name = job_name

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
        if not isinstance(other, ShowHealthCompareJobDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
