# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBuildJobRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'arch': 'str',
        'project_id': 'str',
        'job_name': 'str',
        'auto_update_sub_module': 'str',
        'flavor': 'str',
        'parameters': 'list[CreateBuildJobParameter]',
        'scms': 'list[CreateBuildJobScm]',
        'steps': 'list[CreateBuildJobSteps]',
        'host_type': 'str',
        'build_config_type': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'project_id': 'project_id',
        'job_name': 'job_name',
        'auto_update_sub_module': 'auto_update_sub_module',
        'flavor': 'flavor',
        'parameters': 'parameters',
        'scms': 'scms',
        'steps': 'steps',
        'host_type': 'host_type',
        'build_config_type': 'build_config_type'
    }

    def __init__(self, arch=None, project_id=None, job_name=None, auto_update_sub_module=None, flavor=None, parameters=None, scms=None, steps=None, host_type=None, build_config_type=None):
        """CreateBuildJobRequestBody

        The model defined in huaweicloud sdk

        :param arch: 使用机器的架构
        :type arch: str
        :param project_id: 构建任务所在项目的ID
        :type project_id: str
        :param job_name: 任务名称
        :type job_name: str
        :param auto_update_sub_module: 是否自动更新子模块
        :type auto_update_sub_module: str
        :param flavor: 执行机规格
        :type flavor: str
        :param parameters: 构建执行参数列表
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        :param scms: 构建执行SCM
        :type scms: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobScm`]
        :param steps: 构建执行的步骤
        :type steps: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobSteps`]
        :param host_type: host类型
        :type host_type: str
        :param build_config_type: 构建的配置类型
        :type build_config_type: str
        """
        
        

        self._arch = None
        self._project_id = None
        self._job_name = None
        self._auto_update_sub_module = None
        self._flavor = None
        self._parameters = None
        self._scms = None
        self._steps = None
        self._host_type = None
        self._build_config_type = None
        self.discriminator = None

        self.arch = arch
        self.project_id = project_id
        self.job_name = job_name
        if auto_update_sub_module is not None:
            self.auto_update_sub_module = auto_update_sub_module
        if flavor is not None:
            self.flavor = flavor
        if parameters is not None:
            self.parameters = parameters
        if scms is not None:
            self.scms = scms
        self.steps = steps
        if host_type is not None:
            self.host_type = host_type
        if build_config_type is not None:
            self.build_config_type = build_config_type

    @property
    def arch(self):
        """Gets the arch of this CreateBuildJobRequestBody.

        使用机器的架构

        :return: The arch of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this CreateBuildJobRequestBody.

        使用机器的架构

        :param arch: The arch of this CreateBuildJobRequestBody.
        :type arch: str
        """
        self._arch = arch

    @property
    def project_id(self):
        """Gets the project_id of this CreateBuildJobRequestBody.

        构建任务所在项目的ID

        :return: The project_id of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateBuildJobRequestBody.

        构建任务所在项目的ID

        :param project_id: The project_id of this CreateBuildJobRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def job_name(self):
        """Gets the job_name of this CreateBuildJobRequestBody.

        任务名称

        :return: The job_name of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this CreateBuildJobRequestBody.

        任务名称

        :param job_name: The job_name of this CreateBuildJobRequestBody.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def auto_update_sub_module(self):
        """Gets the auto_update_sub_module of this CreateBuildJobRequestBody.

        是否自动更新子模块

        :return: The auto_update_sub_module of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._auto_update_sub_module

    @auto_update_sub_module.setter
    def auto_update_sub_module(self, auto_update_sub_module):
        """Sets the auto_update_sub_module of this CreateBuildJobRequestBody.

        是否自动更新子模块

        :param auto_update_sub_module: The auto_update_sub_module of this CreateBuildJobRequestBody.
        :type auto_update_sub_module: str
        """
        self._auto_update_sub_module = auto_update_sub_module

    @property
    def flavor(self):
        """Gets the flavor of this CreateBuildJobRequestBody.

        执行机规格

        :return: The flavor of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this CreateBuildJobRequestBody.

        执行机规格

        :param flavor: The flavor of this CreateBuildJobRequestBody.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def parameters(self):
        """Gets the parameters of this CreateBuildJobRequestBody.

        构建执行参数列表

        :return: The parameters of this CreateBuildJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this CreateBuildJobRequestBody.

        构建执行参数列表

        :param parameters: The parameters of this CreateBuildJobRequestBody.
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        """
        self._parameters = parameters

    @property
    def scms(self):
        """Gets the scms of this CreateBuildJobRequestBody.

        构建执行SCM

        :return: The scms of this CreateBuildJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobScm`]
        """
        return self._scms

    @scms.setter
    def scms(self, scms):
        """Sets the scms of this CreateBuildJobRequestBody.

        构建执行SCM

        :param scms: The scms of this CreateBuildJobRequestBody.
        :type scms: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobScm`]
        """
        self._scms = scms

    @property
    def steps(self):
        """Gets the steps of this CreateBuildJobRequestBody.

        构建执行的步骤

        :return: The steps of this CreateBuildJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobSteps`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this CreateBuildJobRequestBody.

        构建执行的步骤

        :param steps: The steps of this CreateBuildJobRequestBody.
        :type steps: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobSteps`]
        """
        self._steps = steps

    @property
    def host_type(self):
        """Gets the host_type of this CreateBuildJobRequestBody.

        host类型

        :return: The host_type of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """Sets the host_type of this CreateBuildJobRequestBody.

        host类型

        :param host_type: The host_type of this CreateBuildJobRequestBody.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def build_config_type(self):
        """Gets the build_config_type of this CreateBuildJobRequestBody.

        构建的配置类型

        :return: The build_config_type of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._build_config_type

    @build_config_type.setter
    def build_config_type(self, build_config_type):
        """Sets the build_config_type of this CreateBuildJobRequestBody.

        构建的配置类型

        :param build_config_type: The build_config_type of this CreateBuildJobRequestBody.
        :type build_config_type: str
        """
        self._build_config_type = build_config_type

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
        if not isinstance(other, CreateBuildJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
