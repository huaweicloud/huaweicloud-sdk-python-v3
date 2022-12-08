# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateExecutionPlanRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_id': 'str',
        'template_body': 'str',
        'template_uri': 'str',
        'execution_plan_name': 'str',
        'description': 'str',
        'vars_structure': 'list[VarsStructure]',
        'vars_body': 'str',
        'vars_uri': 'str'
    }

    attribute_map = {
        'stack_id': 'stack_id',
        'template_body': 'template_body',
        'template_uri': 'template_uri',
        'execution_plan_name': 'execution_plan_name',
        'description': 'description',
        'vars_structure': 'vars_structure',
        'vars_body': 'vars_body',
        'vars_uri': 'vars_uri'
    }

    def __init__(self, stack_id=None, template_body=None, template_uri=None, execution_plan_name=None, description=None, vars_structure=None, vars_body=None, vars_uri=None):
        """CreateExecutionPlanRequestBody

        The model defined in huaweicloud sdk

        :param stack_id: 用户希望生成执行计划的栈（stack）的Id。此Id由资源编排服务在生成栈的时候生成，为UUID。
        :type stack_id: str
        :param template_body: HCL模板，描述了资源的目标状态。资源编排服务将比较此模板与当前远程资源的状态之间的区别 template_body 和 template_uri 有且仅有一个存在
        :type template_body: str
        :param template_uri: HCL模板的OBS地址，描述了资源的目标状态。资源编排服务将比较此模板与当前远程资源的状态之间的区别。目前接受纯tf文件或zip压缩包。 纯tf文件需要以“.tf”结尾，并遵守tf模板格式。压缩包目前只支持zip格式，文件需要以\&quot;.zip\&quot;结尾，压缩包解压后应该只包含文件，且文件均以“.tf”结尾，不支持nested结构 template_body 和 template_uri 有且仅有一个存在
        :type template_uri: str
        :param execution_plan_name: 执行计划的名字，在domain_id+region+project_id+stack_id下应唯一。
        :type execution_plan_name: str
        :param description: 执行计划的描述。可用于客户识别自己的执行计划
        :type description: str
        :param vars_structure: terraform支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。var是一系列terraform所需要的参数。 注：资源编排服务支持vars、vars_body和vars_uri，如果vars、vars_body和vars_uri中声名了同一个变量，将报错400。 注：vars中的值只支持简单的字符串类型，如果其他类型，需要用户自己在HCL引用时转换，或者用户可以使用vars_body或vars_uri， vars_body和vars_uri中支持HCL支持的各种类型以及复杂结构。
        :type vars_structure: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        :param vars_body: terraform支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。vars_body用于接收用户直接提交的tfvars文件内容
        :type vars_body: str
        :param vars_uri: 参数文件的OBS地址，如果客户偏向使用文件维护参数，可以将参数上传OBS，并将OBS地址提交。 注：如果用户同时使用了vars_body、vars_uri和vars，且他们的内容中定义了同一个参数，资源编排服务将报错并返回400。 vars_uri和vars_body中的vars按照HCL的语义，可以支持各种类型、复杂结构等
        :type vars_uri: str
        """
        
        

        self._stack_id = None
        self._template_body = None
        self._template_uri = None
        self._execution_plan_name = None
        self._description = None
        self._vars_structure = None
        self._vars_body = None
        self._vars_uri = None
        self.discriminator = None

        if stack_id is not None:
            self.stack_id = stack_id
        if template_body is not None:
            self.template_body = template_body
        if template_uri is not None:
            self.template_uri = template_uri
        self.execution_plan_name = execution_plan_name
        if description is not None:
            self.description = description
        if vars_structure is not None:
            self.vars_structure = vars_structure
        if vars_body is not None:
            self.vars_body = vars_body
        if vars_uri is not None:
            self.vars_uri = vars_uri

    @property
    def stack_id(self):
        """Gets the stack_id of this CreateExecutionPlanRequestBody.

        用户希望生成执行计划的栈（stack）的Id。此Id由资源编排服务在生成栈的时候生成，为UUID。

        :return: The stack_id of this CreateExecutionPlanRequestBody.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this CreateExecutionPlanRequestBody.

        用户希望生成执行计划的栈（stack）的Id。此Id由资源编排服务在生成栈的时候生成，为UUID。

        :param stack_id: The stack_id of this CreateExecutionPlanRequestBody.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def template_body(self):
        """Gets the template_body of this CreateExecutionPlanRequestBody.

        HCL模板，描述了资源的目标状态。资源编排服务将比较此模板与当前远程资源的状态之间的区别 template_body 和 template_uri 有且仅有一个存在

        :return: The template_body of this CreateExecutionPlanRequestBody.
        :rtype: str
        """
        return self._template_body

    @template_body.setter
    def template_body(self, template_body):
        """Sets the template_body of this CreateExecutionPlanRequestBody.

        HCL模板，描述了资源的目标状态。资源编排服务将比较此模板与当前远程资源的状态之间的区别 template_body 和 template_uri 有且仅有一个存在

        :param template_body: The template_body of this CreateExecutionPlanRequestBody.
        :type template_body: str
        """
        self._template_body = template_body

    @property
    def template_uri(self):
        """Gets the template_uri of this CreateExecutionPlanRequestBody.

        HCL模板的OBS地址，描述了资源的目标状态。资源编排服务将比较此模板与当前远程资源的状态之间的区别。目前接受纯tf文件或zip压缩包。 纯tf文件需要以“.tf”结尾，并遵守tf模板格式。压缩包目前只支持zip格式，文件需要以\".zip\"结尾，压缩包解压后应该只包含文件，且文件均以“.tf”结尾，不支持nested结构 template_body 和 template_uri 有且仅有一个存在

        :return: The template_uri of this CreateExecutionPlanRequestBody.
        :rtype: str
        """
        return self._template_uri

    @template_uri.setter
    def template_uri(self, template_uri):
        """Sets the template_uri of this CreateExecutionPlanRequestBody.

        HCL模板的OBS地址，描述了资源的目标状态。资源编排服务将比较此模板与当前远程资源的状态之间的区别。目前接受纯tf文件或zip压缩包。 纯tf文件需要以“.tf”结尾，并遵守tf模板格式。压缩包目前只支持zip格式，文件需要以\".zip\"结尾，压缩包解压后应该只包含文件，且文件均以“.tf”结尾，不支持nested结构 template_body 和 template_uri 有且仅有一个存在

        :param template_uri: The template_uri of this CreateExecutionPlanRequestBody.
        :type template_uri: str
        """
        self._template_uri = template_uri

    @property
    def execution_plan_name(self):
        """Gets the execution_plan_name of this CreateExecutionPlanRequestBody.

        执行计划的名字，在domain_id+region+project_id+stack_id下应唯一。

        :return: The execution_plan_name of this CreateExecutionPlanRequestBody.
        :rtype: str
        """
        return self._execution_plan_name

    @execution_plan_name.setter
    def execution_plan_name(self, execution_plan_name):
        """Sets the execution_plan_name of this CreateExecutionPlanRequestBody.

        执行计划的名字，在domain_id+region+project_id+stack_id下应唯一。

        :param execution_plan_name: The execution_plan_name of this CreateExecutionPlanRequestBody.
        :type execution_plan_name: str
        """
        self._execution_plan_name = execution_plan_name

    @property
    def description(self):
        """Gets the description of this CreateExecutionPlanRequestBody.

        执行计划的描述。可用于客户识别自己的执行计划

        :return: The description of this CreateExecutionPlanRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateExecutionPlanRequestBody.

        执行计划的描述。可用于客户识别自己的执行计划

        :param description: The description of this CreateExecutionPlanRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def vars_structure(self):
        """Gets the vars_structure of this CreateExecutionPlanRequestBody.

        terraform支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。var是一系列terraform所需要的参数。 注：资源编排服务支持vars、vars_body和vars_uri，如果vars、vars_body和vars_uri中声名了同一个变量，将报错400。 注：vars中的值只支持简单的字符串类型，如果其他类型，需要用户自己在HCL引用时转换，或者用户可以使用vars_body或vars_uri， vars_body和vars_uri中支持HCL支持的各种类型以及复杂结构。

        :return: The vars_structure of this CreateExecutionPlanRequestBody.
        :rtype: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        """
        return self._vars_structure

    @vars_structure.setter
    def vars_structure(self, vars_structure):
        """Sets the vars_structure of this CreateExecutionPlanRequestBody.

        terraform支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。var是一系列terraform所需要的参数。 注：资源编排服务支持vars、vars_body和vars_uri，如果vars、vars_body和vars_uri中声名了同一个变量，将报错400。 注：vars中的值只支持简单的字符串类型，如果其他类型，需要用户自己在HCL引用时转换，或者用户可以使用vars_body或vars_uri， vars_body和vars_uri中支持HCL支持的各种类型以及复杂结构。

        :param vars_structure: The vars_structure of this CreateExecutionPlanRequestBody.
        :type vars_structure: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        """
        self._vars_structure = vars_structure

    @property
    def vars_body(self):
        """Gets the vars_body of this CreateExecutionPlanRequestBody.

        terraform支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。vars_body用于接收用户直接提交的tfvars文件内容

        :return: The vars_body of this CreateExecutionPlanRequestBody.
        :rtype: str
        """
        return self._vars_body

    @vars_body.setter
    def vars_body(self, vars_body):
        """Sets the vars_body of this CreateExecutionPlanRequestBody.

        terraform支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。vars_body用于接收用户直接提交的tfvars文件内容

        :param vars_body: The vars_body of this CreateExecutionPlanRequestBody.
        :type vars_body: str
        """
        self._vars_body = vars_body

    @property
    def vars_uri(self):
        """Gets the vars_uri of this CreateExecutionPlanRequestBody.

        参数文件的OBS地址，如果客户偏向使用文件维护参数，可以将参数上传OBS，并将OBS地址提交。 注：如果用户同时使用了vars_body、vars_uri和vars，且他们的内容中定义了同一个参数，资源编排服务将报错并返回400。 vars_uri和vars_body中的vars按照HCL的语义，可以支持各种类型、复杂结构等

        :return: The vars_uri of this CreateExecutionPlanRequestBody.
        :rtype: str
        """
        return self._vars_uri

    @vars_uri.setter
    def vars_uri(self, vars_uri):
        """Sets the vars_uri of this CreateExecutionPlanRequestBody.

        参数文件的OBS地址，如果客户偏向使用文件维护参数，可以将参数上传OBS，并将OBS地址提交。 注：如果用户同时使用了vars_body、vars_uri和vars，且他们的内容中定义了同一个参数，资源编排服务将报错并返回400。 vars_uri和vars_body中的vars按照HCL的语义，可以支持各种类型、复杂结构等

        :param vars_uri: The vars_uri of this CreateExecutionPlanRequestBody.
        :type vars_uri: str
        """
        self._vars_uri = vars_uri

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
        if not isinstance(other, CreateExecutionPlanRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
