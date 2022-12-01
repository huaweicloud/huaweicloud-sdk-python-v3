# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'docker_id': 'str',
        'exception': 'str',
        'generated_snippet': 'str',
        'language': 'str',
        'model_id': 'str',
        'record_time': 'datetime',
        'request_id': 'str',
        'snippet': 'str',
        'start_time': 'datetime',
        'status': 'str',
        'task_id': 'int',
        'time_consuming': 'float'
    }

    attribute_map = {
        'docker_id': 'docker_id',
        'exception': 'exception',
        'generated_snippet': 'generated_snippet',
        'language': 'language',
        'model_id': 'model_id',
        'record_time': 'record_time',
        'request_id': 'request_id',
        'snippet': 'snippet',
        'start_time': 'start_time',
        'status': 'status',
        'task_id': 'task_id',
        'time_consuming': 'time_consuming'
    }

    def __init__(self, docker_id=None, exception=None, generated_snippet=None, language=None, model_id=None, record_time=None, request_id=None, snippet=None, start_time=None, status=None, task_id=None, time_consuming=None):
        """TaskModel

        The model defined in huaweicloud sdk

        :param docker_id: the docker_id
        :type docker_id: str
        :param exception: exception
        :type exception: str
        :param generated_snippet: the generated_snippet
        :type generated_snippet: str
        :param language: code language
        :type language: str
        :param model_id: model_id
        :type model_id: str
        :param record_time: record_time
        :type record_time: datetime
        :param request_id: the unique id of request
        :type request_id: str
        :param snippet: the snippet of code
        :type snippet: str
        :param start_time: start_time
        :type start_time: datetime
        :param status: status
        :type status: str
        :param task_id: task_id
        :type task_id: int
        :param time_consuming: the time_consuming
        :type time_consuming: float
        """
        
        

        self._docker_id = None
        self._exception = None
        self._generated_snippet = None
        self._language = None
        self._model_id = None
        self._record_time = None
        self._request_id = None
        self._snippet = None
        self._start_time = None
        self._status = None
        self._task_id = None
        self._time_consuming = None
        self.discriminator = None

        if docker_id is not None:
            self.docker_id = docker_id
        if exception is not None:
            self.exception = exception
        if generated_snippet is not None:
            self.generated_snippet = generated_snippet
        if language is not None:
            self.language = language
        if model_id is not None:
            self.model_id = model_id
        if record_time is not None:
            self.record_time = record_time
        if request_id is not None:
            self.request_id = request_id
        if snippet is not None:
            self.snippet = snippet
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if task_id is not None:
            self.task_id = task_id
        if time_consuming is not None:
            self.time_consuming = time_consuming

    @property
    def docker_id(self):
        """Gets the docker_id of this TaskModel.

        the docker_id

        :return: The docker_id of this TaskModel.
        :rtype: str
        """
        return self._docker_id

    @docker_id.setter
    def docker_id(self, docker_id):
        """Sets the docker_id of this TaskModel.

        the docker_id

        :param docker_id: The docker_id of this TaskModel.
        :type docker_id: str
        """
        self._docker_id = docker_id

    @property
    def exception(self):
        """Gets the exception of this TaskModel.

        exception

        :return: The exception of this TaskModel.
        :rtype: str
        """
        return self._exception

    @exception.setter
    def exception(self, exception):
        """Sets the exception of this TaskModel.

        exception

        :param exception: The exception of this TaskModel.
        :type exception: str
        """
        self._exception = exception

    @property
    def generated_snippet(self):
        """Gets the generated_snippet of this TaskModel.

        the generated_snippet

        :return: The generated_snippet of this TaskModel.
        :rtype: str
        """
        return self._generated_snippet

    @generated_snippet.setter
    def generated_snippet(self, generated_snippet):
        """Sets the generated_snippet of this TaskModel.

        the generated_snippet

        :param generated_snippet: The generated_snippet of this TaskModel.
        :type generated_snippet: str
        """
        self._generated_snippet = generated_snippet

    @property
    def language(self):
        """Gets the language of this TaskModel.

        code language

        :return: The language of this TaskModel.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TaskModel.

        code language

        :param language: The language of this TaskModel.
        :type language: str
        """
        self._language = language

    @property
    def model_id(self):
        """Gets the model_id of this TaskModel.

        model_id

        :return: The model_id of this TaskModel.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this TaskModel.

        model_id

        :param model_id: The model_id of this TaskModel.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def record_time(self):
        """Gets the record_time of this TaskModel.

        record_time

        :return: The record_time of this TaskModel.
        :rtype: datetime
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        """Sets the record_time of this TaskModel.

        record_time

        :param record_time: The record_time of this TaskModel.
        :type record_time: datetime
        """
        self._record_time = record_time

    @property
    def request_id(self):
        """Gets the request_id of this TaskModel.

        the unique id of request

        :return: The request_id of this TaskModel.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this TaskModel.

        the unique id of request

        :param request_id: The request_id of this TaskModel.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def snippet(self):
        """Gets the snippet of this TaskModel.

        the snippet of code

        :return: The snippet of this TaskModel.
        :rtype: str
        """
        return self._snippet

    @snippet.setter
    def snippet(self, snippet):
        """Sets the snippet of this TaskModel.

        the snippet of code

        :param snippet: The snippet of this TaskModel.
        :type snippet: str
        """
        self._snippet = snippet

    @property
    def start_time(self):
        """Gets the start_time of this TaskModel.

        start_time

        :return: The start_time of this TaskModel.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskModel.

        start_time

        :param start_time: The start_time of this TaskModel.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this TaskModel.

        status

        :return: The status of this TaskModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskModel.

        status

        :param status: The status of this TaskModel.
        :type status: str
        """
        self._status = status

    @property
    def task_id(self):
        """Gets the task_id of this TaskModel.

        task_id

        :return: The task_id of this TaskModel.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskModel.

        task_id

        :param task_id: The task_id of this TaskModel.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def time_consuming(self):
        """Gets the time_consuming of this TaskModel.

        the time_consuming

        :return: The time_consuming of this TaskModel.
        :rtype: float
        """
        return self._time_consuming

    @time_consuming.setter
    def time_consuming(self, time_consuming):
        """Sets the time_consuming of this TaskModel.

        the time_consuming

        :param time_consuming: The time_consuming of this TaskModel.
        :type time_consuming: float
        """
        self._time_consuming = time_consuming

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
        if not isinstance(other, TaskModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
