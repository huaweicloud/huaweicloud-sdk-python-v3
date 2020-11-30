# coding: utf-8

import pprint
import re

import six





class PipelineExecuteStates:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'status': 'str',
        'stages': 'list[Stages]',
        'executor': 'str',
        'pipeline_name': 'str',
        'pipeline_id': 'str',
        'detail_url': 'str',
        'modify_url': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'result': 'result',
        'status': 'status',
        'stages': 'stages',
        'executor': 'executor',
        'pipeline_name': 'pipeline_name',
        'pipeline_id': 'pipeline_id',
        'detail_url': 'detail_url',
        'modify_url': 'modify_url',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, result=None, status=None, stages=None, executor=None, pipeline_name=None, pipeline_id=None, detail_url=None, modify_url=None, start_time=None, end_time=None):
        """PipelineExecuteStates - a model defined in huaweicloud sdk"""
        
        

        self._result = None
        self._status = None
        self._stages = None
        self._executor = None
        self._pipeline_name = None
        self._pipeline_id = None
        self._detail_url = None
        self._modify_url = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.result = result
        self.status = status
        self.stages = stages
        self.executor = executor
        self.pipeline_name = pipeline_name
        self.pipeline_id = pipeline_id
        self.detail_url = detail_url
        self.modify_url = modify_url
        self.start_time = start_time
        self.end_time = end_time

    @property
    def result(self):
        """Gets the result of this PipelineExecuteStates.

        流水线执行结果

        :return: The result of this PipelineExecuteStates.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PipelineExecuteStates.

        流水线执行结果

        :param result: The result of this PipelineExecuteStates.
        :type: str
        """
        self._result = result

    @property
    def status(self):
        """Gets the status of this PipelineExecuteStates.

        流水线执行状态

        :return: The status of this PipelineExecuteStates.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PipelineExecuteStates.

        流水线执行状态

        :param status: The status of this PipelineExecuteStates.
        :type: str
        """
        self._status = status

    @property
    def stages(self):
        """Gets the stages of this PipelineExecuteStates.

        阶段执行情况

        :return: The stages of this PipelineExecuteStates.
        :rtype: list[Stages]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this PipelineExecuteStates.

        阶段执行情况

        :param stages: The stages of this PipelineExecuteStates.
        :type: list[Stages]
        """
        self._stages = stages

    @property
    def executor(self):
        """Gets the executor of this PipelineExecuteStates.

        执行人

        :return: The executor of this PipelineExecuteStates.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this PipelineExecuteStates.

        执行人

        :param executor: The executor of this PipelineExecuteStates.
        :type: str
        """
        self._executor = executor

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this PipelineExecuteStates.

        流水线名字

        :return: The pipeline_name of this PipelineExecuteStates.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this PipelineExecuteStates.

        流水线名字

        :param pipeline_name: The pipeline_name of this PipelineExecuteStates.
        :type: str
        """
        self._pipeline_name = pipeline_name

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this PipelineExecuteStates.

        流水线ID

        :return: The pipeline_id of this PipelineExecuteStates.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this PipelineExecuteStates.

        流水线ID

        :param pipeline_id: The pipeline_id of this PipelineExecuteStates.
        :type: str
        """
        self._pipeline_id = pipeline_id

    @property
    def detail_url(self):
        """Gets the detail_url of this PipelineExecuteStates.

        流水线详情页URL

        :return: The detail_url of this PipelineExecuteStates.
        :rtype: str
        """
        return self._detail_url

    @detail_url.setter
    def detail_url(self, detail_url):
        """Sets the detail_url of this PipelineExecuteStates.

        流水线详情页URL

        :param detail_url: The detail_url of this PipelineExecuteStates.
        :type: str
        """
        self._detail_url = detail_url

    @property
    def modify_url(self):
        """Gets the modify_url of this PipelineExecuteStates.

        流水线编辑页URL

        :return: The modify_url of this PipelineExecuteStates.
        :rtype: str
        """
        return self._modify_url

    @modify_url.setter
    def modify_url(self, modify_url):
        """Sets the modify_url of this PipelineExecuteStates.

        流水线编辑页URL

        :param modify_url: The modify_url of this PipelineExecuteStates.
        :type: str
        """
        self._modify_url = modify_url

    @property
    def start_time(self):
        """Gets the start_time of this PipelineExecuteStates.

        开始执行时间

        :return: The start_time of this PipelineExecuteStates.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PipelineExecuteStates.

        开始执行时间

        :param start_time: The start_time of this PipelineExecuteStates.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this PipelineExecuteStates.

        结束执行时间

        :return: The end_time of this PipelineExecuteStates.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this PipelineExecuteStates.

        结束执行时间

        :param end_time: The end_time of this PipelineExecuteStates.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PipelineExecuteStates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
