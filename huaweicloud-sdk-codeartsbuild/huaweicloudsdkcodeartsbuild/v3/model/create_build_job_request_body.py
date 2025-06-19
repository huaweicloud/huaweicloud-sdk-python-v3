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
        'group_id': 'str',
        'timeout': 'CreateBuildTimeout',
        'scms': 'list[CreateBuildJobScm]',
        'steps': 'list[CreateBuildJobSteps]',
        'host_type': 'str',
        'build_config_type': 'str',
        'build_if_code_updated': 'bool',
        'triggers': 'list[Trigger]'
    }

    attribute_map = {
        'arch': 'arch',
        'project_id': 'project_id',
        'job_name': 'job_name',
        'auto_update_sub_module': 'auto_update_sub_module',
        'flavor': 'flavor',
        'parameters': 'parameters',
        'group_id': 'group_id',
        'timeout': 'timeout',
        'scms': 'scms',
        'steps': 'steps',
        'host_type': 'host_type',
        'build_config_type': 'build_config_type',
        'build_if_code_updated': 'build_if_code_updated',
        'triggers': 'triggers'
    }

    def __init__(self, arch=None, project_id=None, job_name=None, auto_update_sub_module=None, flavor=None, parameters=None, group_id=None, timeout=None, scms=None, steps=None, host_type=None, build_config_type=None, build_if_code_updated=None, triggers=None):
        r"""CreateBuildJobRequestBody

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
        :param group_id: 任务分组id
        :type group_id: str
        :param timeout: 
        :type timeout: :class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildTimeout`
        :param scms: 构建执行SCM
        :type scms: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobScm`]
        :param steps: 构建执行的步骤
        :type steps: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobSteps`]
        :param host_type: host类型
        :type host_type: str
        :param build_config_type: 构建的配置类型
        :type build_config_type: str
        :param build_if_code_updated: 提交代码触发构建开关
        :type build_if_code_updated: bool
        :param triggers: 定时任务触发器集合
        :type triggers: list[:class:`huaweicloudsdkcodeartsbuild.v3.Trigger`]
        """
        
        

        self._arch = None
        self._project_id = None
        self._job_name = None
        self._auto_update_sub_module = None
        self._flavor = None
        self._parameters = None
        self._group_id = None
        self._timeout = None
        self._scms = None
        self._steps = None
        self._host_type = None
        self._build_config_type = None
        self._build_if_code_updated = None
        self._triggers = None
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
        if group_id is not None:
            self.group_id = group_id
        if timeout is not None:
            self.timeout = timeout
        if scms is not None:
            self.scms = scms
        self.steps = steps
        if host_type is not None:
            self.host_type = host_type
        if build_config_type is not None:
            self.build_config_type = build_config_type
        if build_if_code_updated is not None:
            self.build_if_code_updated = build_if_code_updated
        if triggers is not None:
            self.triggers = triggers

    @property
    def arch(self):
        r"""Gets the arch of this CreateBuildJobRequestBody.

        使用机器的架构

        :return: The arch of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this CreateBuildJobRequestBody.

        使用机器的架构

        :param arch: The arch of this CreateBuildJobRequestBody.
        :type arch: str
        """
        self._arch = arch

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateBuildJobRequestBody.

        构建任务所在项目的ID

        :return: The project_id of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateBuildJobRequestBody.

        构建任务所在项目的ID

        :param project_id: The project_id of this CreateBuildJobRequestBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def job_name(self):
        r"""Gets the job_name of this CreateBuildJobRequestBody.

        任务名称

        :return: The job_name of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this CreateBuildJobRequestBody.

        任务名称

        :param job_name: The job_name of this CreateBuildJobRequestBody.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def auto_update_sub_module(self):
        r"""Gets the auto_update_sub_module of this CreateBuildJobRequestBody.

        是否自动更新子模块

        :return: The auto_update_sub_module of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._auto_update_sub_module

    @auto_update_sub_module.setter
    def auto_update_sub_module(self, auto_update_sub_module):
        r"""Sets the auto_update_sub_module of this CreateBuildJobRequestBody.

        是否自动更新子模块

        :param auto_update_sub_module: The auto_update_sub_module of this CreateBuildJobRequestBody.
        :type auto_update_sub_module: str
        """
        self._auto_update_sub_module = auto_update_sub_module

    @property
    def flavor(self):
        r"""Gets the flavor of this CreateBuildJobRequestBody.

        执行机规格

        :return: The flavor of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CreateBuildJobRequestBody.

        执行机规格

        :param flavor: The flavor of this CreateBuildJobRequestBody.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def parameters(self):
        r"""Gets the parameters of this CreateBuildJobRequestBody.

        构建执行参数列表

        :return: The parameters of this CreateBuildJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this CreateBuildJobRequestBody.

        构建执行参数列表

        :param parameters: The parameters of this CreateBuildJobRequestBody.
        :type parameters: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobParameter`]
        """
        self._parameters = parameters

    @property
    def group_id(self):
        r"""Gets the group_id of this CreateBuildJobRequestBody.

        任务分组id

        :return: The group_id of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this CreateBuildJobRequestBody.

        任务分组id

        :param group_id: The group_id of this CreateBuildJobRequestBody.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def timeout(self):
        r"""Gets the timeout of this CreateBuildJobRequestBody.

        :return: The timeout of this CreateBuildJobRequestBody.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildTimeout`
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this CreateBuildJobRequestBody.

        :param timeout: The timeout of this CreateBuildJobRequestBody.
        :type timeout: :class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildTimeout`
        """
        self._timeout = timeout

    @property
    def scms(self):
        r"""Gets the scms of this CreateBuildJobRequestBody.

        构建执行SCM

        :return: The scms of this CreateBuildJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobScm`]
        """
        return self._scms

    @scms.setter
    def scms(self, scms):
        r"""Sets the scms of this CreateBuildJobRequestBody.

        构建执行SCM

        :param scms: The scms of this CreateBuildJobRequestBody.
        :type scms: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobScm`]
        """
        self._scms = scms

    @property
    def steps(self):
        r"""Gets the steps of this CreateBuildJobRequestBody.

        构建执行的步骤

        :return: The steps of this CreateBuildJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobSteps`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this CreateBuildJobRequestBody.

        构建执行的步骤

        :param steps: The steps of this CreateBuildJobRequestBody.
        :type steps: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobSteps`]
        """
        self._steps = steps

    @property
    def host_type(self):
        r"""Gets the host_type of this CreateBuildJobRequestBody.

        host类型

        :return: The host_type of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        r"""Sets the host_type of this CreateBuildJobRequestBody.

        host类型

        :param host_type: The host_type of this CreateBuildJobRequestBody.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def build_config_type(self):
        r"""Gets the build_config_type of this CreateBuildJobRequestBody.

        构建的配置类型

        :return: The build_config_type of this CreateBuildJobRequestBody.
        :rtype: str
        """
        return self._build_config_type

    @build_config_type.setter
    def build_config_type(self, build_config_type):
        r"""Sets the build_config_type of this CreateBuildJobRequestBody.

        构建的配置类型

        :param build_config_type: The build_config_type of this CreateBuildJobRequestBody.
        :type build_config_type: str
        """
        self._build_config_type = build_config_type

    @property
    def build_if_code_updated(self):
        r"""Gets the build_if_code_updated of this CreateBuildJobRequestBody.

        提交代码触发构建开关

        :return: The build_if_code_updated of this CreateBuildJobRequestBody.
        :rtype: bool
        """
        return self._build_if_code_updated

    @build_if_code_updated.setter
    def build_if_code_updated(self, build_if_code_updated):
        r"""Sets the build_if_code_updated of this CreateBuildJobRequestBody.

        提交代码触发构建开关

        :param build_if_code_updated: The build_if_code_updated of this CreateBuildJobRequestBody.
        :type build_if_code_updated: bool
        """
        self._build_if_code_updated = build_if_code_updated

    @property
    def triggers(self):
        r"""Gets the triggers of this CreateBuildJobRequestBody.

        定时任务触发器集合

        :return: The triggers of this CreateBuildJobRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.Trigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this CreateBuildJobRequestBody.

        定时任务触发器集合

        :param triggers: The triggers of this CreateBuildJobRequestBody.
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
        if not isinstance(other, CreateBuildJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
