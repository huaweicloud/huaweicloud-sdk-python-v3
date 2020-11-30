# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowPipleineStatusResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pipeline_id': 'str',
        'pipeline_name': 'str',
        'executor': 'str',
        'build_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'parameters': 'list[PipelineParameter]',
        'states': 'list[PipelineStateStatus]',
        'elapsed_time': 'str',
        'status': 'str',
        'outcome': 'str',
        'detail_url': 'str'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'pipeline_name': 'pipeline_name',
        'executor': 'executor',
        'build_id': 'build_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'parameters': 'parameters',
        'states': 'states',
        'elapsed_time': 'elapsed_time',
        'status': 'status',
        'outcome': 'outcome',
        'detail_url': 'detail_url'
    }

    def __init__(self, pipeline_id=None, pipeline_name=None, executor=None, build_id=None, start_time=None, end_time=None, parameters=None, states=None, elapsed_time=None, status=None, outcome=None, detail_url=None):
        """ShowPipleineStatusResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._pipeline_id = None
        self._pipeline_name = None
        self._executor = None
        self._build_id = None
        self._start_time = None
        self._end_time = None
        self._parameters = None
        self._states = None
        self._elapsed_time = None
        self._status = None
        self._outcome = None
        self._detail_url = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name
        if executor is not None:
            self.executor = executor
        if build_id is not None:
            self.build_id = build_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if parameters is not None:
            self.parameters = parameters
        if states is not None:
            self.states = states
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if status is not None:
            self.status = status
        if outcome is not None:
            self.outcome = outcome
        if detail_url is not None:
            self.detail_url = detail_url

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this ShowPipleineStatusResponse.

        流水线ID

        :return: The pipeline_id of this ShowPipleineStatusResponse.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this ShowPipleineStatusResponse.

        流水线ID

        :param pipeline_id: The pipeline_id of this ShowPipleineStatusResponse.
        :type: str
        """
        self._pipeline_id = pipeline_id

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this ShowPipleineStatusResponse.

        流水线名称

        :return: The pipeline_name of this ShowPipleineStatusResponse.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this ShowPipleineStatusResponse.

        流水线名称

        :param pipeline_name: The pipeline_name of this ShowPipleineStatusResponse.
        :type: str
        """
        self._pipeline_name = pipeline_name

    @property
    def executor(self):
        """Gets the executor of this ShowPipleineStatusResponse.

        执行人

        :return: The executor of this ShowPipleineStatusResponse.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this ShowPipleineStatusResponse.

        执行人

        :param executor: The executor of this ShowPipleineStatusResponse.
        :type: str
        """
        self._executor = executor

    @property
    def build_id(self):
        """Gets the build_id of this ShowPipleineStatusResponse.

        流水线执行ID

        :return: The build_id of this ShowPipleineStatusResponse.
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        """Sets the build_id of this ShowPipleineStatusResponse.

        流水线执行ID

        :param build_id: The build_id of this ShowPipleineStatusResponse.
        :type: str
        """
        self._build_id = build_id

    @property
    def start_time(self):
        """Gets the start_time of this ShowPipleineStatusResponse.

        开始执行时间

        :return: The start_time of this ShowPipleineStatusResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowPipleineStatusResponse.

        开始执行时间

        :param start_time: The start_time of this ShowPipleineStatusResponse.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowPipleineStatusResponse.

        结束执行时间

        :return: The end_time of this ShowPipleineStatusResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowPipleineStatusResponse.

        结束执行时间

        :param end_time: The end_time of this ShowPipleineStatusResponse.
        :type: str
        """
        self._end_time = end_time

    @property
    def parameters(self):
        """Gets the parameters of this ShowPipleineStatusResponse.

        流水线参数

        :return: The parameters of this ShowPipleineStatusResponse.
        :rtype: list[PipelineParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ShowPipleineStatusResponse.

        流水线参数

        :param parameters: The parameters of this ShowPipleineStatusResponse.
        :type: list[PipelineParameter]
        """
        self._parameters = parameters

    @property
    def states(self):
        """Gets the states of this ShowPipleineStatusResponse.

        流水线执行情况

        :return: The states of this ShowPipleineStatusResponse.
        :rtype: list[PipelineStateStatus]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this ShowPipleineStatusResponse.

        流水线执行情况

        :param states: The states of this ShowPipleineStatusResponse.
        :type: list[PipelineStateStatus]
        """
        self._states = states

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this ShowPipleineStatusResponse.

        执行耗时

        :return: The elapsed_time of this ShowPipleineStatusResponse.
        :rtype: str
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this ShowPipleineStatusResponse.

        执行耗时

        :param elapsed_time: The elapsed_time of this ShowPipleineStatusResponse.
        :type: str
        """
        self._elapsed_time = elapsed_time

    @property
    def status(self):
        """Gets the status of this ShowPipleineStatusResponse.

        流水线运行状态

        :return: The status of this ShowPipleineStatusResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowPipleineStatusResponse.

        流水线运行状态

        :param status: The status of this ShowPipleineStatusResponse.
        :type: str
        """
        self._status = status

    @property
    def outcome(self):
        """Gets the outcome of this ShowPipleineStatusResponse.

        流水线执行结果

        :return: The outcome of this ShowPipleineStatusResponse.
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this ShowPipleineStatusResponse.

        流水线执行结果

        :param outcome: The outcome of this ShowPipleineStatusResponse.
        :type: str
        """
        self._outcome = outcome

    @property
    def detail_url(self):
        """Gets the detail_url of this ShowPipleineStatusResponse.

        流水线详情页地址

        :return: The detail_url of this ShowPipleineStatusResponse.
        :rtype: str
        """
        return self._detail_url

    @detail_url.setter
    def detail_url(self, detail_url):
        """Sets the detail_url of this ShowPipleineStatusResponse.

        流水线详情页地址

        :param detail_url: The detail_url of this ShowPipleineStatusResponse.
        :type: str
        """
        self._detail_url = detail_url

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
        if not isinstance(other, ShowPipleineStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
