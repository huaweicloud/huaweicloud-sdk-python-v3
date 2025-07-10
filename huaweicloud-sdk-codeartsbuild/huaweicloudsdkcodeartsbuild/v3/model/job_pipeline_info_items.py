# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobPipelineInfoItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scms': 'list[CreateBuildJobScm]',
        'parameters': 'list[JobPipelineInfoParameters]',
        'job_name': 'str',
        'job_name_massage': 'str',
        'job_name_regex': 'str',
        'source_code': 'str'
    }

    attribute_map = {
        'scms': 'scms',
        'parameters': 'parameters',
        'job_name': 'job_name',
        'job_name_massage': 'job_name_massage',
        'job_name_regex': 'job_name_regex',
        'source_code': 'source_code'
    }

    def __init__(self, scms=None, parameters=None, job_name=None, job_name_massage=None, job_name_regex=None, source_code=None):
        r"""JobPipelineInfoItems

        The model defined in huaweicloud sdk

        :param scms: 构建执行SCM
        :type scms: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobScm`]
        :param parameters: 参数
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobPipelineInfoParameters`]
        :param job_name: 任务名称
        :type job_name: str
        :param job_name_massage: 任务名称信息
        :type job_name_massage: str
        :param job_name_regex: 任务名称正则
        :type job_name_regex: str
        :param source_code: 任务名称正则
        :type source_code: str
        """
        
        

        self._scms = None
        self._parameters = None
        self._job_name = None
        self._job_name_massage = None
        self._job_name_regex = None
        self._source_code = None
        self.discriminator = None

        if scms is not None:
            self.scms = scms
        if parameters is not None:
            self.parameters = parameters
        if job_name is not None:
            self.job_name = job_name
        if job_name_massage is not None:
            self.job_name_massage = job_name_massage
        if job_name_regex is not None:
            self.job_name_regex = job_name_regex
        if source_code is not None:
            self.source_code = source_code

    @property
    def scms(self):
        r"""Gets the scms of this JobPipelineInfoItems.

        构建执行SCM

        :return: The scms of this JobPipelineInfoItems.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobScm`]
        """
        return self._scms

    @scms.setter
    def scms(self, scms):
        r"""Sets the scms of this JobPipelineInfoItems.

        构建执行SCM

        :param scms: The scms of this JobPipelineInfoItems.
        :type scms: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobScm`]
        """
        self._scms = scms

    @property
    def parameters(self):
        r"""Gets the parameters of this JobPipelineInfoItems.

        参数

        :return: The parameters of this JobPipelineInfoItems.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobPipelineInfoParameters`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this JobPipelineInfoItems.

        参数

        :param parameters: The parameters of this JobPipelineInfoItems.
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.JobPipelineInfoParameters`]
        """
        self._parameters = parameters

    @property
    def job_name(self):
        r"""Gets the job_name of this JobPipelineInfoItems.

        任务名称

        :return: The job_name of this JobPipelineInfoItems.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this JobPipelineInfoItems.

        任务名称

        :param job_name: The job_name of this JobPipelineInfoItems.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_name_massage(self):
        r"""Gets the job_name_massage of this JobPipelineInfoItems.

        任务名称信息

        :return: The job_name_massage of this JobPipelineInfoItems.
        :rtype: str
        """
        return self._job_name_massage

    @job_name_massage.setter
    def job_name_massage(self, job_name_massage):
        r"""Sets the job_name_massage of this JobPipelineInfoItems.

        任务名称信息

        :param job_name_massage: The job_name_massage of this JobPipelineInfoItems.
        :type job_name_massage: str
        """
        self._job_name_massage = job_name_massage

    @property
    def job_name_regex(self):
        r"""Gets the job_name_regex of this JobPipelineInfoItems.

        任务名称正则

        :return: The job_name_regex of this JobPipelineInfoItems.
        :rtype: str
        """
        return self._job_name_regex

    @job_name_regex.setter
    def job_name_regex(self, job_name_regex):
        r"""Sets the job_name_regex of this JobPipelineInfoItems.

        任务名称正则

        :param job_name_regex: The job_name_regex of this JobPipelineInfoItems.
        :type job_name_regex: str
        """
        self._job_name_regex = job_name_regex

    @property
    def source_code(self):
        r"""Gets the source_code of this JobPipelineInfoItems.

        任务名称正则

        :return: The source_code of this JobPipelineInfoItems.
        :rtype: str
        """
        return self._source_code

    @source_code.setter
    def source_code(self, source_code):
        r"""Sets the source_code of this JobPipelineInfoItems.

        任务名称正则

        :param source_code: The source_code of this JobPipelineInfoItems.
        :type source_code: str
        """
        self._source_code = source_code

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
        if not isinstance(other, JobPipelineInfoItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
