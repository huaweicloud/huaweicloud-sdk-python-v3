# coding: utf-8

import pprint
import re

import six





class TemplateState:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'name': 'str',
        'module_or_template_id': 'str',
        'module_or_template_name': 'str',
        'display_name': 'str',
        'dsl_method': 'str',
        'parameters': 'object',
        'is_manual_execution': 'bool',
        'job_parameter_validate': 'bool',
        'is_show_codehub_url': 'bool',
        'is_execute': 'bool',
        'job_id': 'str',
        'job_name': 'str',
        'project_id': 'str',
        'execution_mode': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'module_or_template_id': 'module_or_template_id',
        'module_or_template_name': 'module_or_template_name',
        'display_name': 'display_name',
        'dsl_method': 'dsl_method',
        'parameters': 'parameters',
        'is_manual_execution': 'is_manual_execution',
        'job_parameter_validate': 'job_parameter_validate',
        'is_show_codehub_url': 'is_show_codehub_url',
        'is_execute': 'is_execute',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'project_id': 'project_id',
        'execution_mode': 'execution_mode'
    }

    def __init__(self, type=None, name=None, module_or_template_id=None, module_or_template_name=None, display_name=None, dsl_method=None, parameters=None, is_manual_execution=None, job_parameter_validate=None, is_show_codehub_url=None, is_execute=None, job_id=None, job_name=None, project_id=None, execution_mode=None):
        """TemplateState - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._name = None
        self._module_or_template_id = None
        self._module_or_template_name = None
        self._display_name = None
        self._dsl_method = None
        self._parameters = None
        self._is_manual_execution = None
        self._job_parameter_validate = None
        self._is_show_codehub_url = None
        self._is_execute = None
        self._job_id = None
        self._job_name = None
        self._project_id = None
        self._execution_mode = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.module_or_template_id = module_or_template_id
        self.module_or_template_name = module_or_template_name
        self.display_name = display_name
        self.dsl_method = dsl_method
        self.parameters = parameters
        self.is_manual_execution = is_manual_execution
        self.job_parameter_validate = job_parameter_validate
        self.is_show_codehub_url = is_show_codehub_url
        self.is_execute = is_execute
        self.job_id = job_id
        self.job_name = job_name
        self.project_id = project_id
        self.execution_mode = execution_mode

    @property
    def type(self):
        """Gets the type of this TemplateState.

        任务类型

        :return: The type of this TemplateState.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TemplateState.

        任务类型

        :param type: The type of this TemplateState.
        :type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this TemplateState.

        任务名字

        :return: The name of this TemplateState.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateState.

        任务名字

        :param name: The name of this TemplateState.
        :type: str
        """
        self._name = name

    @property
    def module_or_template_id(self):
        """Gets the module_or_template_id of this TemplateState.

        模板任务ID

        :return: The module_or_template_id of this TemplateState.
        :rtype: str
        """
        return self._module_or_template_id

    @module_or_template_id.setter
    def module_or_template_id(self, module_or_template_id):
        """Sets the module_or_template_id of this TemplateState.

        模板任务ID

        :param module_or_template_id: The module_or_template_id of this TemplateState.
        :type: str
        """
        self._module_or_template_id = module_or_template_id

    @property
    def module_or_template_name(self):
        """Gets the module_or_template_name of this TemplateState.

        模板任务名字

        :return: The module_or_template_name of this TemplateState.
        :rtype: str
        """
        return self._module_or_template_name

    @module_or_template_name.setter
    def module_or_template_name(self, module_or_template_name):
        """Sets the module_or_template_name of this TemplateState.

        模板任务名字

        :param module_or_template_name: The module_or_template_name of this TemplateState.
        :type: str
        """
        self._module_or_template_name = module_or_template_name

    @property
    def display_name(self):
        """Gets the display_name of this TemplateState.

        任务在流水线页面展示名字

        :return: The display_name of this TemplateState.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this TemplateState.

        任务在流水线页面展示名字

        :param display_name: The display_name of this TemplateState.
        :type: str
        """
        self._display_name = display_name

    @property
    def dsl_method(self):
        """Gets the dsl_method of this TemplateState.

        流水线可挂载任务类型

        :return: The dsl_method of this TemplateState.
        :rtype: str
        """
        return self._dsl_method

    @dsl_method.setter
    def dsl_method(self, dsl_method):
        """Sets the dsl_method of this TemplateState.

        流水线可挂载任务类型

        :param dsl_method: The dsl_method of this TemplateState.
        :type: str
        """
        self._dsl_method = dsl_method

    @property
    def parameters(self):
        """Gets the parameters of this TemplateState.

        任务参数,map类型数据

        :return: The parameters of this TemplateState.
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this TemplateState.

        任务参数,map类型数据

        :param parameters: The parameters of this TemplateState.
        :type: object
        """
        self._parameters = parameters

    @property
    def is_manual_execution(self):
        """Gets the is_manual_execution of this TemplateState.

        是否手动执行

        :return: The is_manual_execution of this TemplateState.
        :rtype: bool
        """
        return self._is_manual_execution

    @is_manual_execution.setter
    def is_manual_execution(self, is_manual_execution):
        """Sets the is_manual_execution of this TemplateState.

        是否手动执行

        :param is_manual_execution: The is_manual_execution of this TemplateState.
        :type: bool
        """
        self._is_manual_execution = is_manual_execution

    @property
    def job_parameter_validate(self):
        """Gets the job_parameter_validate of this TemplateState.

        任务参数是否校验

        :return: The job_parameter_validate of this TemplateState.
        :rtype: bool
        """
        return self._job_parameter_validate

    @job_parameter_validate.setter
    def job_parameter_validate(self, job_parameter_validate):
        """Sets the job_parameter_validate of this TemplateState.

        任务参数是否校验

        :param job_parameter_validate: The job_parameter_validate of this TemplateState.
        :type: bool
        """
        self._job_parameter_validate = job_parameter_validate

    @property
    def is_show_codehub_url(self):
        """Gets the is_show_codehub_url of this TemplateState.

        是否显示代码仓URL

        :return: The is_show_codehub_url of this TemplateState.
        :rtype: bool
        """
        return self._is_show_codehub_url

    @is_show_codehub_url.setter
    def is_show_codehub_url(self, is_show_codehub_url):
        """Sets the is_show_codehub_url of this TemplateState.

        是否显示代码仓URL

        :param is_show_codehub_url: The is_show_codehub_url of this TemplateState.
        :type: bool
        """
        self._is_show_codehub_url = is_show_codehub_url

    @property
    def is_execute(self):
        """Gets the is_execute of this TemplateState.

        是否执行

        :return: The is_execute of this TemplateState.
        :rtype: bool
        """
        return self._is_execute

    @is_execute.setter
    def is_execute(self, is_execute):
        """Sets the is_execute of this TemplateState.

        是否执行

        :param is_execute: The is_execute of this TemplateState.
        :type: bool
        """
        self._is_execute = is_execute

    @property
    def job_id(self):
        """Gets the job_id of this TemplateState.

        执行任务ID

        :return: The job_id of this TemplateState.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this TemplateState.

        执行任务ID

        :param job_id: The job_id of this TemplateState.
        :type: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this TemplateState.

        执行任务名字

        :return: The job_name of this TemplateState.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this TemplateState.

        执行任务名字

        :param job_name: The job_name of this TemplateState.
        :type: str
        """
        self._job_name = job_name

    @property
    def project_id(self):
        """Gets the project_id of this TemplateState.

        任务所属项目ID

        :return: The project_id of this TemplateState.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TemplateState.

        任务所属项目ID

        :param project_id: The project_id of this TemplateState.
        :type: str
        """
        self._project_id = project_id

    @property
    def execution_mode(self):
        """Gets the execution_mode of this TemplateState.

        执行方式

        :return: The execution_mode of this TemplateState.
        :rtype: str
        """
        return self._execution_mode

    @execution_mode.setter
    def execution_mode(self, execution_mode):
        """Sets the execution_mode of this TemplateState.

        执行方式

        :param execution_mode: The execution_mode of this TemplateState.
        :type: str
        """
        self._execution_mode = execution_mode

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
        if not isinstance(other, TemplateState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
