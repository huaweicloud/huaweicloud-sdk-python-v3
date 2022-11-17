# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineBuildResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_id': 'str',
        'elapse_time': 'str',
        'end_time': 'str',
        'outcome': 'str',
        'pipeline_id': 'str',
        'pipeline_name': 'str',
        'start_time': 'str',
        'status': 'str'
    }

    attribute_map = {
        'build_id': 'build_id',
        'elapse_time': 'elapse_time',
        'end_time': 'end_time',
        'outcome': 'outcome',
        'pipeline_id': 'pipeline_id',
        'pipeline_name': 'pipeline_name',
        'start_time': 'start_time',
        'status': 'status'
    }

    def __init__(self, build_id=None, elapse_time=None, end_time=None, outcome=None, pipeline_id=None, pipeline_name=None, start_time=None, status=None):
        """PipelineBuildResult

        The model defined in huaweicloud sdk

        :param build_id: 执行ID
        :type build_id: str
        :param elapse_time: 运行耗时
        :type elapse_time: str
        :param end_time: 执行结束时间
        :type end_time: str
        :param outcome: 运行结果
        :type outcome: str
        :param pipeline_id: 流水线id
        :type pipeline_id: str
        :param pipeline_name: 流水线名称
        :type pipeline_name: str
        :param start_time: 执行开始时间
        :type start_time: str
        :param status: 运行状态
        :type status: str
        """
        
        

        self._build_id = None
        self._elapse_time = None
        self._end_time = None
        self._outcome = None
        self._pipeline_id = None
        self._pipeline_name = None
        self._start_time = None
        self._status = None
        self.discriminator = None

        self.build_id = build_id
        if elapse_time is not None:
            self.elapse_time = elapse_time
        self.end_time = end_time
        self.outcome = outcome
        self.pipeline_id = pipeline_id
        self.pipeline_name = pipeline_name
        self.start_time = start_time
        self.status = status

    @property
    def build_id(self):
        """Gets the build_id of this PipelineBuildResult.

        执行ID

        :return: The build_id of this PipelineBuildResult.
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        """Sets the build_id of this PipelineBuildResult.

        执行ID

        :param build_id: The build_id of this PipelineBuildResult.
        :type build_id: str
        """
        self._build_id = build_id

    @property
    def elapse_time(self):
        """Gets the elapse_time of this PipelineBuildResult.

        运行耗时

        :return: The elapse_time of this PipelineBuildResult.
        :rtype: str
        """
        return self._elapse_time

    @elapse_time.setter
    def elapse_time(self, elapse_time):
        """Sets the elapse_time of this PipelineBuildResult.

        运行耗时

        :param elapse_time: The elapse_time of this PipelineBuildResult.
        :type elapse_time: str
        """
        self._elapse_time = elapse_time

    @property
    def end_time(self):
        """Gets the end_time of this PipelineBuildResult.

        执行结束时间

        :return: The end_time of this PipelineBuildResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this PipelineBuildResult.

        执行结束时间

        :param end_time: The end_time of this PipelineBuildResult.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def outcome(self):
        """Gets the outcome of this PipelineBuildResult.

        运行结果

        :return: The outcome of this PipelineBuildResult.
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this PipelineBuildResult.

        运行结果

        :param outcome: The outcome of this PipelineBuildResult.
        :type outcome: str
        """
        self._outcome = outcome

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this PipelineBuildResult.

        流水线id

        :return: The pipeline_id of this PipelineBuildResult.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this PipelineBuildResult.

        流水线id

        :param pipeline_id: The pipeline_id of this PipelineBuildResult.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this PipelineBuildResult.

        流水线名称

        :return: The pipeline_name of this PipelineBuildResult.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this PipelineBuildResult.

        流水线名称

        :param pipeline_name: The pipeline_name of this PipelineBuildResult.
        :type pipeline_name: str
        """
        self._pipeline_name = pipeline_name

    @property
    def start_time(self):
        """Gets the start_time of this PipelineBuildResult.

        执行开始时间

        :return: The start_time of this PipelineBuildResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PipelineBuildResult.

        执行开始时间

        :param start_time: The start_time of this PipelineBuildResult.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this PipelineBuildResult.

        运行状态

        :return: The status of this PipelineBuildResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PipelineBuildResult.

        运行状态

        :param status: The status of this PipelineBuildResult.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, PipelineBuildResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
