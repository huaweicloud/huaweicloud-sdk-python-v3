# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CopyBuildJobRequestBody:

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
        'copy_job_id': 'str',
        'auto_update_sub_module': 'str',
        'flavor': 'str',
        'parameters': 'list[CreateBuildJobParameter]',
        'scms': 'list[CreateBuildJobScm]',
        'steps': 'list[CreateBuildJobSteps]',
        'host_type': 'str',
        'build_config_type': 'str',
        'triggers': 'list[Trigger]'
    }

    attribute_map = {
        'arch': 'arch',
        'project_id': 'project_id',
        'job_name': 'job_name',
        'copy_job_id': 'copy_job_id',
        'auto_update_sub_module': 'auto_update_sub_module',
        'flavor': 'flavor',
        'parameters': 'parameters',
        'scms': 'scms',
        'steps': 'steps',
        'host_type': 'host_type',
        'build_config_type': 'build_config_type',
        'triggers': 'triggers'
    }

    def __init__(self, arch=None, project_id=None, job_name=None, copy_job_id=None, auto_update_sub_module=None, flavor=None, parameters=None, scms=None, steps=None, host_type=None, build_config_type=None, triggers=None):
        r"""CopyBuildJobRequestBody

        The model defined in huaweicloud sdk

        :param arch: 使用机器的架构
        :type arch: str
        :param project_id: 构建任务所在项目的ID
        :type project_id: str
        :param job_name: 任务名称
        :type job_name: str
        :param copy_job_id: 构建任务ID
        :type copy_job_id: str
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
        :param triggers: 定时任务触发器集合
        :type triggers: list[:class:`huaweicloudsdkcodeartsbuild.v3.Trigger`]
        """
        
        

        self._arch = None
        self._project_id = None
        self._job_name = None
        self._copy_job_id = None
        self._auto_update_sub_module = None
        self._flavor = None
        self._parameters = None
        self._scms = None
        self._steps = None
        self._host_type = None
        self._build_config_type = None
        self._triggers = None
        self.discriminator = None

        self.arch = arch
        self.project_id = project_id
        self.job_name = job_name
        self.copy_job_id = copy_job_id
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
        if triggers is not None:
            self.triggers = triggers

    @property
    def arch(self):
        r"""Gets the arch of this CopyBuildJobRequestBody.

        使用机器的架构

        :return: The arch of this CopyBuildJobRequestBody.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this CopyBuildJobRequestBody.

        使用机器的架构

        :param arch: The arch of this CopyBuildJobRequestBody.
        :type arch: str
        """
        self._arch = arch

    @property
    def project_id(self):
        r"""Gets the project_id of this CopyBuildJobRequestBody.

        构建任务所在项目的ID

        :return: The project_id of this CopyBuildJobRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CopyBuildJobRequestBody.

        构建任务所在项目的ID

        :param project_id: The project_id of this CopyBuildJobRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def job_name(self):
        r"""Gets the job_name of this CopyBuildJobRequestBody.

        任务名称

        :return: The job_name of this CopyBuildJobRequestBody.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this CopyBuildJobRequestBody.

        任务名称

        :param job_name: The job_name of this CopyBuildJobRequestBody.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def copy_job_id(self):
        r"""Gets the copy_job_id of this CopyBuildJobRequestBody.

        构建任务ID

        :return: The copy_job_id of this CopyBuildJobRequestBody.
        :rtype: str
        """
        return self._copy_job_id

    @copy_job_id.setter
    def copy_job_id(self, copy_job_id):
        r"""Sets the copy_job_id of this CopyBuildJobRequestBody.

        构建任务ID

        :param copy_job_id: The copy_job_id of this CopyBuildJobRequestBody.
        :type copy_job_id: str
        """
        self._copy_job_id = copy_job_id

    @property
    def auto_update_sub_module(self):
        r"""Gets the auto_update_sub_module of this CopyBuildJobRequestBody.

        是否自动更新子模块

        :return: The auto_update_sub_module of this CopyBuildJobRequestBody.
        :rtype: str
        """
        return self._auto_update_sub_module

    @auto_update_sub_module.setter
    def auto_update_sub_module(self, auto_update_sub_module):
        r"""Sets the auto_update_sub_module of this CopyBuildJobRequestBody.

        是否自动更新子模块

        :param auto_update_sub_module: The auto_update_sub_module of this CopyBuildJobRequestBody.
        :type auto_update_sub_module: str
        """
        self._auto_update_sub_module = auto_update_sub_module

    @property
    def flavor(self):
        r"""Gets the flavor of this CopyBuildJobRequestBody.

        执行机规格

        :return: The flavor of this CopyBuildJobRequestBody.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CopyBuildJobRequestBody.

        执行机规格

        :param flavor: The flavor of this CopyBuildJobRequestBody.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def parameters(self):
        r"""Gets the parameters of this CopyBuildJobRequestBody.

        构建执行参数列表

        :return: The parameters of this CopyBuildJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this CopyBuildJobRequestBody.

        构建执行参数列表

        :param parameters: The parameters of this CopyBuildJobRequestBody.
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        """
        self._parameters = parameters

    @property
    def scms(self):
        r"""Gets the scms of this CopyBuildJobRequestBody.

        构建执行SCM

        :return: The scms of this CopyBuildJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobScm`]
        """
        return self._scms

    @scms.setter
    def scms(self, scms):
        r"""Sets the scms of this CopyBuildJobRequestBody.

        构建执行SCM

        :param scms: The scms of this CopyBuildJobRequestBody.
        :type scms: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobScm`]
        """
        self._scms = scms

    @property
    def steps(self):
        r"""Gets the steps of this CopyBuildJobRequestBody.

        构建执行的步骤

        :return: The steps of this CopyBuildJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobSteps`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this CopyBuildJobRequestBody.

        构建执行的步骤

        :param steps: The steps of this CopyBuildJobRequestBody.
        :type steps: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobSteps`]
        """
        self._steps = steps

    @property
    def host_type(self):
        r"""Gets the host_type of this CopyBuildJobRequestBody.

        host类型

        :return: The host_type of this CopyBuildJobRequestBody.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        r"""Sets the host_type of this CopyBuildJobRequestBody.

        host类型

        :param host_type: The host_type of this CopyBuildJobRequestBody.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def build_config_type(self):
        r"""Gets the build_config_type of this CopyBuildJobRequestBody.

        构建的配置类型

        :return: The build_config_type of this CopyBuildJobRequestBody.
        :rtype: str
        """
        return self._build_config_type

    @build_config_type.setter
    def build_config_type(self, build_config_type):
        r"""Sets the build_config_type of this CopyBuildJobRequestBody.

        构建的配置类型

        :param build_config_type: The build_config_type of this CopyBuildJobRequestBody.
        :type build_config_type: str
        """
        self._build_config_type = build_config_type

    @property
    def triggers(self):
        r"""Gets the triggers of this CopyBuildJobRequestBody.

        定时任务触发器集合

        :return: The triggers of this CopyBuildJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.Trigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this CopyBuildJobRequestBody.

        定时任务触发器集合

        :param triggers: The triggers of this CopyBuildJobRequestBody.
        :type triggers: list[:class:`huaweicloudsdkcodeartsbuild.v3.Trigger`]
        """
        self._triggers = triggers

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
        if not isinstance(other, CopyBuildJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
