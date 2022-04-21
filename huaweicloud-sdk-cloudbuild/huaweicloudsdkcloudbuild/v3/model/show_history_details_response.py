# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHistoryDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'build_number': 'int',
        'project_id': 'str',
        'project_name': 'str',
        'parameters': 'dict(str, str)',
        'build_steps': 'list[BuildStep]'
    }

    attribute_map = {
        'job_name': 'job_name',
        'build_number': 'build_number',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'parameters': 'parameters',
        'build_steps': 'build_steps'
    }

    def __init__(self, job_name=None, build_number=None, project_id=None, project_name=None, parameters=None, build_steps=None):
        """ShowHistoryDetailsResponse

        The model defined in huaweicloud sdk

        :param job_name: 构建任务名称
        :type job_name: str
        :param build_number: 构建编号
        :type build_number: int
        :param project_id: 构建任务所在项目的ID
        :type project_id: str
        :param project_name: 构建任务所在项目的名称
        :type project_name: str
        :param parameters: 本次构建的参数，Map类型，敏感参数值返回*号
        :type parameters: dict(str, str)
        :param build_steps: 本次任务的构建步骤详情，返回的步骤为页面可见步骤
        :type build_steps: list[:class:`huaweicloudsdkcloudbuild.v3.BuildStep`]
        """
        
        super(ShowHistoryDetailsResponse, self).__init__()

        self._job_name = None
        self._build_number = None
        self._project_id = None
        self._project_name = None
        self._parameters = None
        self._build_steps = None
        self.discriminator = None

        if job_name is not None:
            self.job_name = job_name
        if build_number is not None:
            self.build_number = build_number
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if parameters is not None:
            self.parameters = parameters
        if build_steps is not None:
            self.build_steps = build_steps

    @property
    def job_name(self):
        """Gets the job_name of this ShowHistoryDetailsResponse.

        构建任务名称

        :return: The job_name of this ShowHistoryDetailsResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ShowHistoryDetailsResponse.

        构建任务名称

        :param job_name: The job_name of this ShowHistoryDetailsResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def build_number(self):
        """Gets the build_number of this ShowHistoryDetailsResponse.

        构建编号

        :return: The build_number of this ShowHistoryDetailsResponse.
        :rtype: int
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this ShowHistoryDetailsResponse.

        构建编号

        :param build_number: The build_number of this ShowHistoryDetailsResponse.
        :type build_number: int
        """
        self._build_number = build_number

    @property
    def project_id(self):
        """Gets the project_id of this ShowHistoryDetailsResponse.

        构建任务所在项目的ID

        :return: The project_id of this ShowHistoryDetailsResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowHistoryDetailsResponse.

        构建任务所在项目的ID

        :param project_id: The project_id of this ShowHistoryDetailsResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ShowHistoryDetailsResponse.

        构建任务所在项目的名称

        :return: The project_name of this ShowHistoryDetailsResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ShowHistoryDetailsResponse.

        构建任务所在项目的名称

        :param project_name: The project_name of this ShowHistoryDetailsResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def parameters(self):
        """Gets the parameters of this ShowHistoryDetailsResponse.

        本次构建的参数，Map类型，敏感参数值返回*号

        :return: The parameters of this ShowHistoryDetailsResponse.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ShowHistoryDetailsResponse.

        本次构建的参数，Map类型，敏感参数值返回*号

        :param parameters: The parameters of this ShowHistoryDetailsResponse.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def build_steps(self):
        """Gets the build_steps of this ShowHistoryDetailsResponse.

        本次任务的构建步骤详情，返回的步骤为页面可见步骤

        :return: The build_steps of this ShowHistoryDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkcloudbuild.v3.BuildStep`]
        """
        return self._build_steps

    @build_steps.setter
    def build_steps(self, build_steps):
        """Sets the build_steps of this ShowHistoryDetailsResponse.

        本次任务的构建步骤详情，返回的步骤为页面可见步骤

        :param build_steps: The build_steps of this ShowHistoryDetailsResponse.
        :type build_steps: list[:class:`huaweicloudsdkcloudbuild.v3.BuildStep`]
        """
        self._build_steps = build_steps

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
        if not isinstance(other, ShowHistoryDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
