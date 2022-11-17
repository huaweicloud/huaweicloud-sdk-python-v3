# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJudgementDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_status': 'str',
        'status': 'str',
        'judgement_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'result': 'JudgementResult'
    }

    attribute_map = {
        'task_status': 'task_status',
        'status': 'status',
        'judgement_id': 'judgement_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'result': 'result'
    }

    def __init__(self, task_status=None, status=None, judgement_id=None, start_time=None, end_time=None, result=None):
        """ShowJudgementDetailResponse

        The model defined in huaweicloud sdk

        :param task_status: 任务回调状态:callback_success(回调成功)、callback_error(回调出错)
        :type task_status: str
        :param status: 任务运行状态:success(成功)、compile_error(编译错误)、internal_error(系统内部错误)、run_timeout(运行超时)、judging(代码运行中)、runtime_error(运行出错)、output_match_error(不符合输出规范)
        :type status: str
        :param judgement_id: 判题任务ID
        :type judgement_id: str
        :param start_time: 任务开始时间
        :type start_time: str
        :param end_time: 任务结束时间
        :type end_time: str
        :param result: 
        :type result: :class:`huaweicloudsdkclassroom.v3.JudgementResult`
        """
        
        super(ShowJudgementDetailResponse, self).__init__()

        self._task_status = None
        self._status = None
        self._judgement_id = None
        self._start_time = None
        self._end_time = None
        self._result = None
        self.discriminator = None

        if task_status is not None:
            self.task_status = task_status
        if status is not None:
            self.status = status
        if judgement_id is not None:
            self.judgement_id = judgement_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if result is not None:
            self.result = result

    @property
    def task_status(self):
        """Gets the task_status of this ShowJudgementDetailResponse.

        任务回调状态:callback_success(回调成功)、callback_error(回调出错)

        :return: The task_status of this ShowJudgementDetailResponse.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ShowJudgementDetailResponse.

        任务回调状态:callback_success(回调成功)、callback_error(回调出错)

        :param task_status: The task_status of this ShowJudgementDetailResponse.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def status(self):
        """Gets the status of this ShowJudgementDetailResponse.

        任务运行状态:success(成功)、compile_error(编译错误)、internal_error(系统内部错误)、run_timeout(运行超时)、judging(代码运行中)、runtime_error(运行出错)、output_match_error(不符合输出规范)

        :return: The status of this ShowJudgementDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowJudgementDetailResponse.

        任务运行状态:success(成功)、compile_error(编译错误)、internal_error(系统内部错误)、run_timeout(运行超时)、judging(代码运行中)、runtime_error(运行出错)、output_match_error(不符合输出规范)

        :param status: The status of this ShowJudgementDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def judgement_id(self):
        """Gets the judgement_id of this ShowJudgementDetailResponse.

        判题任务ID

        :return: The judgement_id of this ShowJudgementDetailResponse.
        :rtype: str
        """
        return self._judgement_id

    @judgement_id.setter
    def judgement_id(self, judgement_id):
        """Sets the judgement_id of this ShowJudgementDetailResponse.

        判题任务ID

        :param judgement_id: The judgement_id of this ShowJudgementDetailResponse.
        :type judgement_id: str
        """
        self._judgement_id = judgement_id

    @property
    def start_time(self):
        """Gets the start_time of this ShowJudgementDetailResponse.

        任务开始时间

        :return: The start_time of this ShowJudgementDetailResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowJudgementDetailResponse.

        任务开始时间

        :param start_time: The start_time of this ShowJudgementDetailResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowJudgementDetailResponse.

        任务结束时间

        :return: The end_time of this ShowJudgementDetailResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowJudgementDetailResponse.

        任务结束时间

        :param end_time: The end_time of this ShowJudgementDetailResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def result(self):
        """Gets the result of this ShowJudgementDetailResponse.

        :return: The result of this ShowJudgementDetailResponse.
        :rtype: :class:`huaweicloudsdkclassroom.v3.JudgementResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ShowJudgementDetailResponse.

        :param result: The result of this ShowJudgementDetailResponse.
        :type result: :class:`huaweicloudsdkclassroom.v3.JudgementResult`
        """
        self._result = result

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
        if not isinstance(other, ShowJudgementDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
