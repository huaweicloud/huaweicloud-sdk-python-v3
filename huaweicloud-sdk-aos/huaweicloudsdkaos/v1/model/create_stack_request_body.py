# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStackRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_name': 'str',
        'agencies': 'list[Agency]',
        'description': 'str',
        'enable_deletion_protection': 'bool',
        'enable_auto_rollback': 'bool',
        'template_body': 'str',
        'template_uri': 'str',
        'vars_body': 'str',
        'vars_structure': 'list[VarsStructure]',
        'vars_uri': 'str'
    }

    attribute_map = {
        'stack_name': 'stack_name',
        'agencies': 'agencies',
        'description': 'description',
        'enable_deletion_protection': 'enable_deletion_protection',
        'enable_auto_rollback': 'enable_auto_rollback',
        'template_body': 'template_body',
        'template_uri': 'template_uri',
        'vars_body': 'vars_body',
        'vars_structure': 'vars_structure',
        'vars_uri': 'vars_uri'
    }

    def __init__(self, stack_name=None, agencies=None, description=None, enable_deletion_protection=None, enable_auto_rollback=None, template_body=None, template_uri=None, vars_body=None, vars_structure=None, vars_uri=None):
        """CreateStackRequestBody

        The model defined in huaweicloud sdk

        :param stack_name: 用户希望生成的资源栈的名字。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_name: str
        :param agencies: 委托授权的信息。
        :type agencies: list[:class:`huaweicloudsdkaos.v1.Agency`]
        :param description: 资源栈的描述。可用于客户识别自己的资源栈。
        :type description: str
        :param enable_deletion_protection: 删除保护的标识位，如果不传默认为false，即默认不开启资源栈删除保护（删除保护开启后资源栈不允许被删除）
        :type enable_deletion_protection: bool
        :param enable_auto_rollback: 自动回滚的标识位，如果不传默认为false，即默认不开启资源栈自动回滚（自动回滚开启后，如果部署失败，则会自动回滚，并返回上一个稳定状态）
        :type enable_auto_rollback: bool
        :param template_body: HCL模板，描述了资源的目标状态。资源编排服务将比较此模板与当前远程资源的状态之间的区别。  template_body和template_uri 必须有且只有一个存在 
        :type template_body: str
        :param template_uri: HCL模板的OBS地址，该模板描述了资源的目标状态  OBS地址必须为同region的OBS地址，暂不支持跨region访问  对应的文件应该是纯tf文件或zip压缩包  纯tf文件需要以&#x60;.tf&#x60;或者&#x60;.tfjson&#x60;结尾，并遵守hcl语法  压缩包目前只支持zip格式，文件需要以\&quot;.zip\&quot;结尾。解压后的文件不得包含\&quot;.tfvars\&quot;文件  template_body和template_uri 必须有且只有一个存在 
        :type template_uri: str
        :param vars_body: HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中。具体tfvars格式见：https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files  * 资源编排服务支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 如果vars中都是简单的字符串格式，可以使用var_structure  * 注意：vars_body中不应该含有任何敏感信息，资源编排服务会直接明文使用、log、展示、存储对应的vars。如为敏感信息，建议通过vars_structure并设置encryption字段传递 
        :type vars_body: str
        :param vars_structure: HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。  * var_structure可以允许客户提交最简单的字符串类型的参数  * 资源编排服务支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * vars_structure中的值只支持简单的字符串类型，如果需要使用其他类型，需要用户自己在HCL引用时转换， 或者用户可以使用vars_uri、vars_body，vars_uri和vars_body中支持HCL支持的各种类型以及复杂结构  * 如果vars_structure过大，可以使用vars_uri  * 注意：vars_structure中默认不应该含有任何敏感信息，资源编排服务会直接明文使用、log、展示、存储对应的vars。如为敏感信息，建议设置encryption字段开启加密 
        :type vars_structure: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        :param vars_uri: HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果  * vars_uri需要指向一个OBS的pre-signed URL地址，其他地址暂不支持  * 资源编排服务支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * vars_uri中的内容使用HCL的tfvars格式，用户可以将”.tfvars”中的内容保存到文件并上传到OBS中，并将OBS pre-signed URL传递给vars_uri。具体tfvars格式见：https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files  * 注意：vars_uri的内容不应该含有任何敏感信息，资源编排服务会直接明文使用、log、展示、存储对应的vars。如为敏感信息，建议通过vars_structure并设置encryption字段传递 
        :type vars_uri: str
        """
        
        

        self._stack_name = None
        self._agencies = None
        self._description = None
        self._enable_deletion_protection = None
        self._enable_auto_rollback = None
        self._template_body = None
        self._template_uri = None
        self._vars_body = None
        self._vars_structure = None
        self._vars_uri = None
        self.discriminator = None

        self.stack_name = stack_name
        if agencies is not None:
            self.agencies = agencies
        if description is not None:
            self.description = description
        if enable_deletion_protection is not None:
            self.enable_deletion_protection = enable_deletion_protection
        if enable_auto_rollback is not None:
            self.enable_auto_rollback = enable_auto_rollback
        if template_body is not None:
            self.template_body = template_body
        if template_uri is not None:
            self.template_uri = template_uri
        if vars_body is not None:
            self.vars_body = vars_body
        if vars_structure is not None:
            self.vars_structure = vars_structure
        if vars_uri is not None:
            self.vars_uri = vars_uri

    @property
    def stack_name(self):
        """Gets the stack_name of this CreateStackRequestBody.

        用户希望生成的资源栈的名字。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_name of this CreateStackRequestBody.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this CreateStackRequestBody.

        用户希望生成的资源栈的名字。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_name: The stack_name of this CreateStackRequestBody.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def agencies(self):
        """Gets the agencies of this CreateStackRequestBody.

        委托授权的信息。

        :return: The agencies of this CreateStackRequestBody.
        :rtype: list[:class:`huaweicloudsdkaos.v1.Agency`]
        """
        return self._agencies

    @agencies.setter
    def agencies(self, agencies):
        """Sets the agencies of this CreateStackRequestBody.

        委托授权的信息。

        :param agencies: The agencies of this CreateStackRequestBody.
        :type agencies: list[:class:`huaweicloudsdkaos.v1.Agency`]
        """
        self._agencies = agencies

    @property
    def description(self):
        """Gets the description of this CreateStackRequestBody.

        资源栈的描述。可用于客户识别自己的资源栈。

        :return: The description of this CreateStackRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateStackRequestBody.

        资源栈的描述。可用于客户识别自己的资源栈。

        :param description: The description of this CreateStackRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def enable_deletion_protection(self):
        """Gets the enable_deletion_protection of this CreateStackRequestBody.

        删除保护的标识位，如果不传默认为false，即默认不开启资源栈删除保护（删除保护开启后资源栈不允许被删除）

        :return: The enable_deletion_protection of this CreateStackRequestBody.
        :rtype: bool
        """
        return self._enable_deletion_protection

    @enable_deletion_protection.setter
    def enable_deletion_protection(self, enable_deletion_protection):
        """Sets the enable_deletion_protection of this CreateStackRequestBody.

        删除保护的标识位，如果不传默认为false，即默认不开启资源栈删除保护（删除保护开启后资源栈不允许被删除）

        :param enable_deletion_protection: The enable_deletion_protection of this CreateStackRequestBody.
        :type enable_deletion_protection: bool
        """
        self._enable_deletion_protection = enable_deletion_protection

    @property
    def enable_auto_rollback(self):
        """Gets the enable_auto_rollback of this CreateStackRequestBody.

        自动回滚的标识位，如果不传默认为false，即默认不开启资源栈自动回滚（自动回滚开启后，如果部署失败，则会自动回滚，并返回上一个稳定状态）

        :return: The enable_auto_rollback of this CreateStackRequestBody.
        :rtype: bool
        """
        return self._enable_auto_rollback

    @enable_auto_rollback.setter
    def enable_auto_rollback(self, enable_auto_rollback):
        """Sets the enable_auto_rollback of this CreateStackRequestBody.

        自动回滚的标识位，如果不传默认为false，即默认不开启资源栈自动回滚（自动回滚开启后，如果部署失败，则会自动回滚，并返回上一个稳定状态）

        :param enable_auto_rollback: The enable_auto_rollback of this CreateStackRequestBody.
        :type enable_auto_rollback: bool
        """
        self._enable_auto_rollback = enable_auto_rollback

    @property
    def template_body(self):
        """Gets the template_body of this CreateStackRequestBody.

        HCL模板，描述了资源的目标状态。资源编排服务将比较此模板与当前远程资源的状态之间的区别。  template_body和template_uri 必须有且只有一个存在 

        :return: The template_body of this CreateStackRequestBody.
        :rtype: str
        """
        return self._template_body

    @template_body.setter
    def template_body(self, template_body):
        """Sets the template_body of this CreateStackRequestBody.

        HCL模板，描述了资源的目标状态。资源编排服务将比较此模板与当前远程资源的状态之间的区别。  template_body和template_uri 必须有且只有一个存在 

        :param template_body: The template_body of this CreateStackRequestBody.
        :type template_body: str
        """
        self._template_body = template_body

    @property
    def template_uri(self):
        """Gets the template_uri of this CreateStackRequestBody.

        HCL模板的OBS地址，该模板描述了资源的目标状态  OBS地址必须为同region的OBS地址，暂不支持跨region访问  对应的文件应该是纯tf文件或zip压缩包  纯tf文件需要以`.tf`或者`.tfjson`结尾，并遵守hcl语法  压缩包目前只支持zip格式，文件需要以\".zip\"结尾。解压后的文件不得包含\".tfvars\"文件  template_body和template_uri 必须有且只有一个存在 

        :return: The template_uri of this CreateStackRequestBody.
        :rtype: str
        """
        return self._template_uri

    @template_uri.setter
    def template_uri(self, template_uri):
        """Sets the template_uri of this CreateStackRequestBody.

        HCL模板的OBS地址，该模板描述了资源的目标状态  OBS地址必须为同region的OBS地址，暂不支持跨region访问  对应的文件应该是纯tf文件或zip压缩包  纯tf文件需要以`.tf`或者`.tfjson`结尾，并遵守hcl语法  压缩包目前只支持zip格式，文件需要以\".zip\"结尾。解压后的文件不得包含\".tfvars\"文件  template_body和template_uri 必须有且只有一个存在 

        :param template_uri: The template_uri of this CreateStackRequestBody.
        :type template_uri: str
        """
        self._template_uri = template_uri

    @property
    def vars_body(self):
        """Gets the vars_body of this CreateStackRequestBody.

        HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中。具体tfvars格式见：https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files  * 资源编排服务支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 如果vars中都是简单的字符串格式，可以使用var_structure  * 注意：vars_body中不应该含有任何敏感信息，资源编排服务会直接明文使用、log、展示、存储对应的vars。如为敏感信息，建议通过vars_structure并设置encryption字段传递 

        :return: The vars_body of this CreateStackRequestBody.
        :rtype: str
        """
        return self._vars_body

    @vars_body.setter
    def vars_body(self, vars_body):
        """Sets the vars_body of this CreateStackRequestBody.

        HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中。具体tfvars格式见：https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files  * 资源编排服务支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 如果vars中都是简单的字符串格式，可以使用var_structure  * 注意：vars_body中不应该含有任何敏感信息，资源编排服务会直接明文使用、log、展示、存储对应的vars。如为敏感信息，建议通过vars_structure并设置encryption字段传递 

        :param vars_body: The vars_body of this CreateStackRequestBody.
        :type vars_body: str
        """
        self._vars_body = vars_body

    @property
    def vars_structure(self):
        """Gets the vars_structure of this CreateStackRequestBody.

        HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。  * var_structure可以允许客户提交最简单的字符串类型的参数  * 资源编排服务支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * vars_structure中的值只支持简单的字符串类型，如果需要使用其他类型，需要用户自己在HCL引用时转换， 或者用户可以使用vars_uri、vars_body，vars_uri和vars_body中支持HCL支持的各种类型以及复杂结构  * 如果vars_structure过大，可以使用vars_uri  * 注意：vars_structure中默认不应该含有任何敏感信息，资源编排服务会直接明文使用、log、展示、存储对应的vars。如为敏感信息，建议设置encryption字段开启加密 

        :return: The vars_structure of this CreateStackRequestBody.
        :rtype: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        """
        return self._vars_structure

    @vars_structure.setter
    def vars_structure(self, vars_structure):
        """Sets the vars_structure of this CreateStackRequestBody.

        HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果。  * var_structure可以允许客户提交最简单的字符串类型的参数  * 资源编排服务支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * vars_structure中的值只支持简单的字符串类型，如果需要使用其他类型，需要用户自己在HCL引用时转换， 或者用户可以使用vars_uri、vars_body，vars_uri和vars_body中支持HCL支持的各种类型以及复杂结构  * 如果vars_structure过大，可以使用vars_uri  * 注意：vars_structure中默认不应该含有任何敏感信息，资源编排服务会直接明文使用、log、展示、存储对应的vars。如为敏感信息，建议设置encryption字段开启加密 

        :param vars_structure: The vars_structure of this CreateStackRequestBody.
        :type vars_structure: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        """
        self._vars_structure = vars_structure

    @property
    def vars_uri(self):
        """Gets the vars_uri of this CreateStackRequestBody.

        HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果  * vars_uri需要指向一个OBS的pre-signed URL地址，其他地址暂不支持  * 资源编排服务支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * vars_uri中的内容使用HCL的tfvars格式，用户可以将”.tfvars”中的内容保存到文件并上传到OBS中，并将OBS pre-signed URL传递给vars_uri。具体tfvars格式见：https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files  * 注意：vars_uri的内容不应该含有任何敏感信息，资源编排服务会直接明文使用、log、展示、存储对应的vars。如为敏感信息，建议通过vars_structure并设置encryption字段传递 

        :return: The vars_uri of this CreateStackRequestBody.
        :rtype: str
        """
        return self._vars_uri

    @vars_uri.setter
    def vars_uri(self, vars_uri):
        """Sets the vars_uri of this CreateStackRequestBody.

        HCL支持参数，即，同一个模板可以给予不同的参数而达到不同的效果  * vars_uri需要指向一个OBS的pre-signed URL地址，其他地址暂不支持  * 资源编排服务支持vars_structure，vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * vars_uri中的内容使用HCL的tfvars格式，用户可以将”.tfvars”中的内容保存到文件并上传到OBS中，并将OBS pre-signed URL传递给vars_uri。具体tfvars格式见：https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files  * 注意：vars_uri的内容不应该含有任何敏感信息，资源编排服务会直接明文使用、log、展示、存储对应的vars。如为敏感信息，建议通过vars_structure并设置encryption字段传递 

        :param vars_uri: The vars_uri of this CreateStackRequestBody.
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
        if not isinstance(other, CreateStackRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
