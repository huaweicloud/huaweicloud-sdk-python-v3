# coding: utf-8

import pprint
import re

import six





class PipelineStateStatus:


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
        'name': 'str',
        'type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'elapsed_time': 'str',
        'status': 'str',
        'outcome': 'str',
        'error_code': 'str',
        'error_msg': 'str',
        'children': 'list[PipelineStateStatus]',
        'detail_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'elapsed_time': 'elapsed_time',
        'status': 'status',
        'outcome': 'outcome',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'children': 'children',
        'detail_url': 'detail_url'
    }

    def __init__(self, id=None, name=None, type=None, start_time=None, end_time=None, elapsed_time=None, status=None, outcome=None, error_code=None, error_msg=None, children=None, detail_url=None):
        """PipelineStateStatus - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._type = None
        self._start_time = None
        self._end_time = None
        self._elapsed_time = None
        self._status = None
        self._outcome = None
        self._error_code = None
        self._error_msg = None
        self._children = None
        self._detail_url = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.type = type
        self.start_time = start_time
        self.end_time = end_time
        self.elapsed_time = elapsed_time
        self.status = status
        self.outcome = outcome
        self.error_code = error_code
        self.error_msg = error_msg
        self.children = children
        self.detail_url = detail_url

    @property
    def id(self):
        """Gets the id of this PipelineStateStatus.

        阶段或任务标识

        :return: The id of this PipelineStateStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelineStateStatus.

        阶段或任务标识

        :param id: The id of this PipelineStateStatus.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PipelineStateStatus.

        阶段或任务名称

        :return: The name of this PipelineStateStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineStateStatus.

        阶段或任务名称

        :param name: The name of this PipelineStateStatus.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this PipelineStateStatus.

        类别(阶段/任务)

        :return: The type of this PipelineStateStatus.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PipelineStateStatus.

        类别(阶段/任务)

        :param type: The type of this PipelineStateStatus.
        :type: str
        """
        self._type = type

    @property
    def start_time(self):
        """Gets the start_time of this PipelineStateStatus.

        执行开始时间

        :return: The start_time of this PipelineStateStatus.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PipelineStateStatus.

        执行开始时间

        :param start_time: The start_time of this PipelineStateStatus.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this PipelineStateStatus.

        执行结束时间

        :return: The end_time of this PipelineStateStatus.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this PipelineStateStatus.

        执行结束时间

        :param end_time: The end_time of this PipelineStateStatus.
        :type: str
        """
        self._end_time = end_time

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this PipelineStateStatus.

        运行耗时

        :return: The elapsed_time of this PipelineStateStatus.
        :rtype: str
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this PipelineStateStatus.

        运行耗时

        :param elapsed_time: The elapsed_time of this PipelineStateStatus.
        :type: str
        """
        self._elapsed_time = elapsed_time

    @property
    def status(self):
        """Gets the status of this PipelineStateStatus.

        运行状态

        :return: The status of this PipelineStateStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PipelineStateStatus.

        运行状态

        :param status: The status of this PipelineStateStatus.
        :type: str
        """
        self._status = status

    @property
    def outcome(self):
        """Gets the outcome of this PipelineStateStatus.

        运行结果

        :return: The outcome of this PipelineStateStatus.
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this PipelineStateStatus.

        运行结果

        :param outcome: The outcome of this PipelineStateStatus.
        :type: str
        """
        self._outcome = outcome

    @property
    def error_code(self):
        """Gets the error_code of this PipelineStateStatus.

        错误码

        :return: The error_code of this PipelineStateStatus.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this PipelineStateStatus.

        错误码

        :param error_code: The error_code of this PipelineStateStatus.
        :type: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this PipelineStateStatus.

        错误信息

        :return: The error_msg of this PipelineStateStatus.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this PipelineStateStatus.

        错误信息

        :param error_msg: The error_msg of this PipelineStateStatus.
        :type: str
        """
        self._error_msg = error_msg

    @property
    def children(self):
        """Gets the children of this PipelineStateStatus.

        子任务运行信息(对任务来说是空的)

        :return: The children of this PipelineStateStatus.
        :rtype: list[PipelineStateStatus]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this PipelineStateStatus.

        子任务运行信息(对任务来说是空的)

        :param children: The children of this PipelineStateStatus.
        :type: list[PipelineStateStatus]
        """
        self._children = children

    @property
    def detail_url(self):
        """Gets the detail_url of this PipelineStateStatus.

        任务运行记录跳转链接

        :return: The detail_url of this PipelineStateStatus.
        :rtype: str
        """
        return self._detail_url

    @detail_url.setter
    def detail_url(self, detail_url):
        """Sets the detail_url of this PipelineStateStatus.

        任务运行记录跳转链接

        :param detail_url: The detail_url of this PipelineStateStatus.
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
        if not isinstance(other, PipelineStateStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
