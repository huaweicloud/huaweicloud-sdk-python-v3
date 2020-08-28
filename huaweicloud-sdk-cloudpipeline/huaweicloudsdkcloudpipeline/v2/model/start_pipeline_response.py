# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class StartPipelineResponse(SdkResponse):


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
        'pipeline_id': 'str',
        'create_at': 'str',
        'job_id': 'str',
        'job_name': 'str',
        'executor_id': 'str',
        'executor': 'str',
        'pipeline_name': 'str'
    }

    attribute_map = {
        'build_id': 'build_id',
        'pipeline_id': 'pipeline_id',
        'create_at': 'create_at',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'executor_id': 'executor_id',
        'executor': 'executor',
        'pipeline_name': 'pipeline_name'
    }

    def __init__(self, build_id=None, pipeline_id=None, create_at=None, job_id=None, job_name=None, executor_id=None, executor=None, pipeline_name=None):
        """StartPipelineResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._build_id = None
        self._pipeline_id = None
        self._create_at = None
        self._job_id = None
        self._job_name = None
        self._executor_id = None
        self._executor = None
        self._pipeline_name = None
        self.discriminator = None

        if build_id is not None:
            self.build_id = build_id
        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if create_at is not None:
            self.create_at = create_at
        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if executor_id is not None:
            self.executor_id = executor_id
        if executor is not None:
            self.executor = executor
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name

    @property
    def build_id(self):
        """Gets the build_id of this StartPipelineResponse.

        执行ID

        :return: The build_id of this StartPipelineResponse.
        :rtype: str
        """
        return self._build_id

    @build_id.setter
    def build_id(self, build_id):
        """Sets the build_id of this StartPipelineResponse.

        执行ID

        :param build_id: The build_id of this StartPipelineResponse.
        :type: str
        """
        self._build_id = build_id

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this StartPipelineResponse.

        流水线ID

        :return: The pipeline_id of this StartPipelineResponse.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this StartPipelineResponse.

        流水线ID

        :param pipeline_id: The pipeline_id of this StartPipelineResponse.
        :type: str
        """
        self._pipeline_id = pipeline_id

    @property
    def create_at(self):
        """Gets the create_at of this StartPipelineResponse.

        执行时间

        :return: The create_at of this StartPipelineResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this StartPipelineResponse.

        执行时间

        :param create_at: The create_at of this StartPipelineResponse.
        :type: str
        """
        self._create_at = create_at

    @property
    def job_id(self):
        """Gets the job_id of this StartPipelineResponse.

        八爪鱼JobId

        :return: The job_id of this StartPipelineResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this StartPipelineResponse.

        八爪鱼JobId

        :param job_id: The job_id of this StartPipelineResponse.
        :type: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this StartPipelineResponse.

        八爪鱼JobName

        :return: The job_name of this StartPipelineResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this StartPipelineResponse.

        八爪鱼JobName

        :param job_name: The job_name of this StartPipelineResponse.
        :type: str
        """
        self._job_name = job_name

    @property
    def executor_id(self):
        """Gets the executor_id of this StartPipelineResponse.

        执行人ID

        :return: The executor_id of this StartPipelineResponse.
        :rtype: str
        """
        return self._executor_id

    @executor_id.setter
    def executor_id(self, executor_id):
        """Sets the executor_id of this StartPipelineResponse.

        执行人ID

        :param executor_id: The executor_id of this StartPipelineResponse.
        :type: str
        """
        self._executor_id = executor_id

    @property
    def executor(self):
        """Gets the executor of this StartPipelineResponse.

        执行人

        :return: The executor of this StartPipelineResponse.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        """Sets the executor of this StartPipelineResponse.

        执行人

        :param executor: The executor of this StartPipelineResponse.
        :type: str
        """
        self._executor = executor

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this StartPipelineResponse.

        流水线名字

        :return: The pipeline_name of this StartPipelineResponse.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this StartPipelineResponse.

        流水线名字

        :param pipeline_name: The pipeline_name of this StartPipelineResponse.
        :type: str
        """
        self._pipeline_name = pipeline_name

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
        if not isinstance(other, StartPipelineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
