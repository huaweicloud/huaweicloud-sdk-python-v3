# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobEntities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'current_task': 'str',
        'image_name': 'str',
        'addition_error_code': 'str',
        'addition_error_msg': 'str',
        'error_code': 'str',
        'error': 'str',
        'alarm_code': 'str',
        'process_percent': 'float',
        'results': 'list[JobEntitiesResult]',
        'sub_jobs_result': 'list[SubJobResult]',
        'sub_jobs_list': 'list[str]'
    }

    attribute_map = {
        'image_id': 'image_id',
        'current_task': 'current_task',
        'image_name': 'image_name',
        'addition_error_code': 'addition_error_code',
        'addition_error_msg': 'addition_error_msg',
        'error_code': 'error_code',
        'error': 'error',
        'alarm_code': 'alarm_code',
        'process_percent': 'process_percent',
        'results': 'results',
        'sub_jobs_result': 'sub_jobs_result',
        'sub_jobs_list': 'sub_jobs_list'
    }

    def __init__(self, image_id=None, current_task=None, image_name=None, addition_error_code=None, addition_error_msg=None, error_code=None, error=None, alarm_code=None, process_percent=None, results=None, sub_jobs_result=None, sub_jobs_list=None):
        r"""JobEntities

        The model defined in huaweicloud sdk

        :param image_id: 镜像ID
        :type image_id: str
        :param current_task: 当前任务名称
        :type current_task: str
        :param image_name: 镜像名称
        :type image_name: str
        :param addition_error_code: 添加错误码
        :type addition_error_code: str
        :param addition_error_msg: 添加错误消息
        :type addition_error_msg: str
        :param error_code: 错误码
        :type error_code: str
        :param error: 错误消息
        :type error: str
        :param alarm_code: 告警代码
        :type alarm_code: str
        :param process_percent: 任务执行进度
        :type process_percent: float
        :param results: 批量任务执行结果
        :type results: list[:class:`huaweicloudsdkims.v2.JobEntitiesResult`]
        :param sub_jobs_result: 子任务结果列表
        :type sub_jobs_result: list[:class:`huaweicloudsdkims.v2.SubJobResult`]
        :param sub_jobs_list: 子任务ID列表
        :type sub_jobs_list: list[str]
        """
        
        

        self._image_id = None
        self._current_task = None
        self._image_name = None
        self._addition_error_code = None
        self._addition_error_msg = None
        self._error_code = None
        self._error = None
        self._alarm_code = None
        self._process_percent = None
        self._results = None
        self._sub_jobs_result = None
        self._sub_jobs_list = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if current_task is not None:
            self.current_task = current_task
        if image_name is not None:
            self.image_name = image_name
        if addition_error_code is not None:
            self.addition_error_code = addition_error_code
        if addition_error_msg is not None:
            self.addition_error_msg = addition_error_msg
        if error_code is not None:
            self.error_code = error_code
        if error is not None:
            self.error = error
        if alarm_code is not None:
            self.alarm_code = alarm_code
        if process_percent is not None:
            self.process_percent = process_percent
        if results is not None:
            self.results = results
        if sub_jobs_result is not None:
            self.sub_jobs_result = sub_jobs_result
        if sub_jobs_list is not None:
            self.sub_jobs_list = sub_jobs_list

    @property
    def image_id(self):
        r"""Gets the image_id of this JobEntities.

        镜像ID

        :return: The image_id of this JobEntities.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this JobEntities.

        镜像ID

        :param image_id: The image_id of this JobEntities.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def current_task(self):
        r"""Gets the current_task of this JobEntities.

        当前任务名称

        :return: The current_task of this JobEntities.
        :rtype: str
        """
        return self._current_task

    @current_task.setter
    def current_task(self, current_task):
        r"""Sets the current_task of this JobEntities.

        当前任务名称

        :param current_task: The current_task of this JobEntities.
        :type current_task: str
        """
        self._current_task = current_task

    @property
    def image_name(self):
        r"""Gets the image_name of this JobEntities.

        镜像名称

        :return: The image_name of this JobEntities.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this JobEntities.

        镜像名称

        :param image_name: The image_name of this JobEntities.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def addition_error_code(self):
        r"""Gets the addition_error_code of this JobEntities.

        添加错误码

        :return: The addition_error_code of this JobEntities.
        :rtype: str
        """
        return self._addition_error_code

    @addition_error_code.setter
    def addition_error_code(self, addition_error_code):
        r"""Sets the addition_error_code of this JobEntities.

        添加错误码

        :param addition_error_code: The addition_error_code of this JobEntities.
        :type addition_error_code: str
        """
        self._addition_error_code = addition_error_code

    @property
    def addition_error_msg(self):
        r"""Gets the addition_error_msg of this JobEntities.

        添加错误消息

        :return: The addition_error_msg of this JobEntities.
        :rtype: str
        """
        return self._addition_error_msg

    @addition_error_msg.setter
    def addition_error_msg(self, addition_error_msg):
        r"""Sets the addition_error_msg of this JobEntities.

        添加错误消息

        :param addition_error_msg: The addition_error_msg of this JobEntities.
        :type addition_error_msg: str
        """
        self._addition_error_msg = addition_error_msg

    @property
    def error_code(self):
        r"""Gets the error_code of this JobEntities.

        错误码

        :return: The error_code of this JobEntities.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this JobEntities.

        错误码

        :param error_code: The error_code of this JobEntities.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error(self):
        r"""Gets the error of this JobEntities.

        错误消息

        :return: The error of this JobEntities.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this JobEntities.

        错误消息

        :param error: The error of this JobEntities.
        :type error: str
        """
        self._error = error

    @property
    def alarm_code(self):
        r"""Gets the alarm_code of this JobEntities.

        告警代码

        :return: The alarm_code of this JobEntities.
        :rtype: str
        """
        return self._alarm_code

    @alarm_code.setter
    def alarm_code(self, alarm_code):
        r"""Sets the alarm_code of this JobEntities.

        告警代码

        :param alarm_code: The alarm_code of this JobEntities.
        :type alarm_code: str
        """
        self._alarm_code = alarm_code

    @property
    def process_percent(self):
        r"""Gets the process_percent of this JobEntities.

        任务执行进度

        :return: The process_percent of this JobEntities.
        :rtype: float
        """
        return self._process_percent

    @process_percent.setter
    def process_percent(self, process_percent):
        r"""Sets the process_percent of this JobEntities.

        任务执行进度

        :param process_percent: The process_percent of this JobEntities.
        :type process_percent: float
        """
        self._process_percent = process_percent

    @property
    def results(self):
        r"""Gets the results of this JobEntities.

        批量任务执行结果

        :return: The results of this JobEntities.
        :rtype: list[:class:`huaweicloudsdkims.v2.JobEntitiesResult`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this JobEntities.

        批量任务执行结果

        :param results: The results of this JobEntities.
        :type results: list[:class:`huaweicloudsdkims.v2.JobEntitiesResult`]
        """
        self._results = results

    @property
    def sub_jobs_result(self):
        r"""Gets the sub_jobs_result of this JobEntities.

        子任务结果列表

        :return: The sub_jobs_result of this JobEntities.
        :rtype: list[:class:`huaweicloudsdkims.v2.SubJobResult`]
        """
        return self._sub_jobs_result

    @sub_jobs_result.setter
    def sub_jobs_result(self, sub_jobs_result):
        r"""Sets the sub_jobs_result of this JobEntities.

        子任务结果列表

        :param sub_jobs_result: The sub_jobs_result of this JobEntities.
        :type sub_jobs_result: list[:class:`huaweicloudsdkims.v2.SubJobResult`]
        """
        self._sub_jobs_result = sub_jobs_result

    @property
    def sub_jobs_list(self):
        r"""Gets the sub_jobs_list of this JobEntities.

        子任务ID列表

        :return: The sub_jobs_list of this JobEntities.
        :rtype: list[str]
        """
        return self._sub_jobs_list

    @sub_jobs_list.setter
    def sub_jobs_list(self, sub_jobs_list):
        r"""Sets the sub_jobs_list of this JobEntities.

        子任务ID列表

        :param sub_jobs_list: The sub_jobs_list of this JobEntities.
        :type sub_jobs_list: list[str]
        """
        self._sub_jobs_list = sub_jobs_list

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
        if not isinstance(other, JobEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
