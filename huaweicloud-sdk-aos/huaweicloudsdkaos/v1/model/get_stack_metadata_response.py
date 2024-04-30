# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetStackMetadataResponse(SdkResponse):

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
        'stack_name': 'str',
        'description': 'str',
        'vars_structure': 'list[VarsStructure]',
        'vars_body': 'str',
        'enable_deletion_protection': 'bool',
        'enable_auto_rollback': 'bool',
        'status': 'str',
        'agencies': 'list[Agency]',
        'status_message': 'str',
        'vars_uri_content': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'stack_id': 'stack_id',
        'stack_name': 'stack_name',
        'description': 'description',
        'vars_structure': 'vars_structure',
        'vars_body': 'vars_body',
        'enable_deletion_protection': 'enable_deletion_protection',
        'enable_auto_rollback': 'enable_auto_rollback',
        'status': 'status',
        'agencies': 'agencies',
        'status_message': 'status_message',
        'vars_uri_content': 'vars_uri_content',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, stack_id=None, stack_name=None, description=None, vars_structure=None, vars_body=None, enable_deletion_protection=None, enable_auto_rollback=None, status=None, agencies=None, status_message=None, vars_uri_content=None, create_time=None, update_time=None):
        """GetStackMetadataResponse

        The model defined in huaweicloud sdk

        :param stack_id: 资源栈（stack）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给予的stack_id和当前资源栈的ID不一致，则返回400
        :type stack_id: str
        :param stack_name: 资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_name: str
        :param description: 资源栈的描述。可用于客户识别自己的资源栈。
        :type description: str
        :param vars_structure: HCL参数结构。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * var_structure可以允许客户提交最简单的字符串类型的参数  * 资源编排服务支持vars_structure，vars_body和vars_uri，如果以上三种方式中声名了同一个变量，将报错400  * vars_structure中的值只支持简单的字符串类型，如果需要使用其他类型，需要用户自己在HCL引用时转换， 或者用户可以使用vars_uri、vars_body，vars_uri和vars_body中支持HCL支持的各种类型以及复杂结构  * 如果vars_structure过大，可以使用vars_uri  * 注意：vars_structure中默认不应该含有任何敏感信息，资源编排服务会直接明文使用、log、展示、存储对应的vars。如为敏感信息，建议设置encryption字段开启加密
        :type vars_structure: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        :param vars_body: HCL参数文件的内容。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中  * 资源编排服务支持vars_body和vars_uri，如果以上两种方式中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储对应的vars_body。
        :type vars_body: str
        :param enable_deletion_protection: 删除保护的标识位，如果不传默认为false，即默认不开启资源栈删除保护（删除保护开启后资源栈不允许被删除）  *在UpdateStack API中，如果该参数未在RequestBody中给予，则不会对资源栈的删除保护属性进行更新*
        :type enable_deletion_protection: bool
        :param enable_auto_rollback: 自动回滚的标识位，如果不传默认为false，即默认不开启资源栈自动回滚（自动回滚开启后，如果部署失败，则会自动回滚，并返回上一个稳定状态）  *在UpdateStack API中，如果该参数未在RequestBody中给予，则不会对资源栈的自动回滚属性进行更新* *该属性与使用模板导入资源功能互斥，如果堆栈的自动回滚设置为true，则不允许部署包含导入资源的模板*
        :type enable_auto_rollback: bool
        :param status: 资源栈的状态    * &#x60;CREATION_COMPLETE&#x60; - 生成空资源栈完成，并没有任何部署    * &#x60;DEPLOYMENT_IN_PROGRESS&#x60; - 正在部署，请等待    * &#x60;DEPLOYMENT_FAILED&#x60; - 部署失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情    * &#x60;DEPLOYMENT_COMPLETE&#x60; - 部署完成    * &#x60;ROLLBACK_IN_PROGRESS&#x60; - 部署失败，正在回滚，请等待    * &#x60;ROLLBACK_FAILED&#x60; - 回滚失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情    * &#x60;ROLLBACK_COMPLETE&#x60; - 回滚完成    * &#x60;DELETION_IN_PROGRESS&#x60; - 正在删除，请等待    * &#x60;DELETION_FAILED&#x60; - 删除失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情
        :type status: str
        :param agencies: 委托授权的信息。  RFS仅在创建资源栈（触发部署）、创建执行计划、部署资源栈、删除资源栈等涉及资源操作的请求中使用委托，且该委托仅作用于与之绑定的Provider对资源的操作中。如果委托中提供的权限不足，有可能导致相关资源操作失败。  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)
        :type agencies: list[:class:`huaweicloudsdkaos.v1.Agency`]
        :param status_message: 当资源栈的状态为任意失败状态（即以 &#x60;FAILED&#x60; 结尾时），将会展示简要的错误信息总结以供debug
        :type status_message: str
        :param vars_uri_content: vars_uri对应的文件内容
        :type vars_uri_content: str
        :param create_time: 资源栈的生成时间 格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type create_time: str
        :param update_time: 资源栈的更新时间（更新场景包括元数据更新场景和部署场景） 格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type update_time: str
        """
        
        super(GetStackMetadataResponse, self).__init__()

        self._stack_id = None
        self._stack_name = None
        self._description = None
        self._vars_structure = None
        self._vars_body = None
        self._enable_deletion_protection = None
        self._enable_auto_rollback = None
        self._status = None
        self._agencies = None
        self._status_message = None
        self._vars_uri_content = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if stack_id is not None:
            self.stack_id = stack_id
        self.stack_name = stack_name
        if description is not None:
            self.description = description
        if vars_structure is not None:
            self.vars_structure = vars_structure
        if vars_body is not None:
            self.vars_body = vars_body
        if enable_deletion_protection is not None:
            self.enable_deletion_protection = enable_deletion_protection
        if enable_auto_rollback is not None:
            self.enable_auto_rollback = enable_auto_rollback
        if status is not None:
            self.status = status
        if agencies is not None:
            self.agencies = agencies
        if status_message is not None:
            self.status_message = status_message
        if vars_uri_content is not None:
            self.vars_uri_content = vars_uri_content
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def stack_id(self):
        """Gets the stack_id of this GetStackMetadataResponse.

        资源栈（stack）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给予的stack_id和当前资源栈的ID不一致，则返回400

        :return: The stack_id of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this GetStackMetadataResponse.

        资源栈（stack）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给予的stack_id和当前资源栈的ID不一致，则返回400

        :param stack_id: The stack_id of this GetStackMetadataResponse.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def stack_name(self):
        """Gets the stack_name of this GetStackMetadataResponse.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_name of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this GetStackMetadataResponse.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_name: The stack_name of this GetStackMetadataResponse.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def description(self):
        """Gets the description of this GetStackMetadataResponse.

        资源栈的描述。可用于客户识别自己的资源栈。

        :return: The description of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetStackMetadataResponse.

        资源栈的描述。可用于客户识别自己的资源栈。

        :param description: The description of this GetStackMetadataResponse.
        :type description: str
        """
        self._description = description

    @property
    def vars_structure(self):
        """Gets the vars_structure of this GetStackMetadataResponse.

        HCL参数结构。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * var_structure可以允许客户提交最简单的字符串类型的参数  * 资源编排服务支持vars_structure，vars_body和vars_uri，如果以上三种方式中声名了同一个变量，将报错400  * vars_structure中的值只支持简单的字符串类型，如果需要使用其他类型，需要用户自己在HCL引用时转换， 或者用户可以使用vars_uri、vars_body，vars_uri和vars_body中支持HCL支持的各种类型以及复杂结构  * 如果vars_structure过大，可以使用vars_uri  * 注意：vars_structure中默认不应该含有任何敏感信息，资源编排服务会直接明文使用、log、展示、存储对应的vars。如为敏感信息，建议设置encryption字段开启加密

        :return: The vars_structure of this GetStackMetadataResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        """
        return self._vars_structure

    @vars_structure.setter
    def vars_structure(self, vars_structure):
        """Sets the vars_structure of this GetStackMetadataResponse.

        HCL参数结构。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * var_structure可以允许客户提交最简单的字符串类型的参数  * 资源编排服务支持vars_structure，vars_body和vars_uri，如果以上三种方式中声名了同一个变量，将报错400  * vars_structure中的值只支持简单的字符串类型，如果需要使用其他类型，需要用户自己在HCL引用时转换， 或者用户可以使用vars_uri、vars_body，vars_uri和vars_body中支持HCL支持的各种类型以及复杂结构  * 如果vars_structure过大，可以使用vars_uri  * 注意：vars_structure中默认不应该含有任何敏感信息，资源编排服务会直接明文使用、log、展示、存储对应的vars。如为敏感信息，建议设置encryption字段开启加密

        :param vars_structure: The vars_structure of this GetStackMetadataResponse.
        :type vars_structure: list[:class:`huaweicloudsdkaos.v1.VarsStructure`]
        """
        self._vars_structure = vars_structure

    @property
    def vars_body(self):
        """Gets the vars_body of this GetStackMetadataResponse.

        HCL参数文件的内容。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中  * 资源编排服务支持vars_body和vars_uri，如果以上两种方式中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储对应的vars_body。

        :return: The vars_body of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._vars_body

    @vars_body.setter
    def vars_body(self, vars_body):
        """Sets the vars_body of this GetStackMetadataResponse.

        HCL参数文件的内容。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中  * 资源编排服务支持vars_body和vars_uri，如果以上两种方式中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储对应的vars_body。

        :param vars_body: The vars_body of this GetStackMetadataResponse.
        :type vars_body: str
        """
        self._vars_body = vars_body

    @property
    def enable_deletion_protection(self):
        """Gets the enable_deletion_protection of this GetStackMetadataResponse.

        删除保护的标识位，如果不传默认为false，即默认不开启资源栈删除保护（删除保护开启后资源栈不允许被删除）  *在UpdateStack API中，如果该参数未在RequestBody中给予，则不会对资源栈的删除保护属性进行更新*

        :return: The enable_deletion_protection of this GetStackMetadataResponse.
        :rtype: bool
        """
        return self._enable_deletion_protection

    @enable_deletion_protection.setter
    def enable_deletion_protection(self, enable_deletion_protection):
        """Sets the enable_deletion_protection of this GetStackMetadataResponse.

        删除保护的标识位，如果不传默认为false，即默认不开启资源栈删除保护（删除保护开启后资源栈不允许被删除）  *在UpdateStack API中，如果该参数未在RequestBody中给予，则不会对资源栈的删除保护属性进行更新*

        :param enable_deletion_protection: The enable_deletion_protection of this GetStackMetadataResponse.
        :type enable_deletion_protection: bool
        """
        self._enable_deletion_protection = enable_deletion_protection

    @property
    def enable_auto_rollback(self):
        """Gets the enable_auto_rollback of this GetStackMetadataResponse.

        自动回滚的标识位，如果不传默认为false，即默认不开启资源栈自动回滚（自动回滚开启后，如果部署失败，则会自动回滚，并返回上一个稳定状态）  *在UpdateStack API中，如果该参数未在RequestBody中给予，则不会对资源栈的自动回滚属性进行更新* *该属性与使用模板导入资源功能互斥，如果堆栈的自动回滚设置为true，则不允许部署包含导入资源的模板*

        :return: The enable_auto_rollback of this GetStackMetadataResponse.
        :rtype: bool
        """
        return self._enable_auto_rollback

    @enable_auto_rollback.setter
    def enable_auto_rollback(self, enable_auto_rollback):
        """Sets the enable_auto_rollback of this GetStackMetadataResponse.

        自动回滚的标识位，如果不传默认为false，即默认不开启资源栈自动回滚（自动回滚开启后，如果部署失败，则会自动回滚，并返回上一个稳定状态）  *在UpdateStack API中，如果该参数未在RequestBody中给予，则不会对资源栈的自动回滚属性进行更新* *该属性与使用模板导入资源功能互斥，如果堆栈的自动回滚设置为true，则不允许部署包含导入资源的模板*

        :param enable_auto_rollback: The enable_auto_rollback of this GetStackMetadataResponse.
        :type enable_auto_rollback: bool
        """
        self._enable_auto_rollback = enable_auto_rollback

    @property
    def status(self):
        """Gets the status of this GetStackMetadataResponse.

        资源栈的状态    * `CREATION_COMPLETE` - 生成空资源栈完成，并没有任何部署    * `DEPLOYMENT_IN_PROGRESS` - 正在部署，请等待    * `DEPLOYMENT_FAILED` - 部署失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情    * `DEPLOYMENT_COMPLETE` - 部署完成    * `ROLLBACK_IN_PROGRESS` - 部署失败，正在回滚，请等待    * `ROLLBACK_FAILED` - 回滚失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情    * `ROLLBACK_COMPLETE` - 回滚完成    * `DELETION_IN_PROGRESS` - 正在删除，请等待    * `DELETION_FAILED` - 删除失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情

        :return: The status of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetStackMetadataResponse.

        资源栈的状态    * `CREATION_COMPLETE` - 生成空资源栈完成，并没有任何部署    * `DEPLOYMENT_IN_PROGRESS` - 正在部署，请等待    * `DEPLOYMENT_FAILED` - 部署失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情    * `DEPLOYMENT_COMPLETE` - 部署完成    * `ROLLBACK_IN_PROGRESS` - 部署失败，正在回滚，请等待    * `ROLLBACK_FAILED` - 回滚失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情    * `ROLLBACK_COMPLETE` - 回滚完成    * `DELETION_IN_PROGRESS` - 正在删除，请等待    * `DELETION_FAILED` - 删除失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情

        :param status: The status of this GetStackMetadataResponse.
        :type status: str
        """
        self._status = status

    @property
    def agencies(self):
        """Gets the agencies of this GetStackMetadataResponse.

        委托授权的信息。  RFS仅在创建资源栈（触发部署）、创建执行计划、部署资源栈、删除资源栈等涉及资源操作的请求中使用委托，且该委托仅作用于与之绑定的Provider对资源的操作中。如果委托中提供的权限不足，有可能导致相关资源操作失败。  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)

        :return: The agencies of this GetStackMetadataResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.Agency`]
        """
        return self._agencies

    @agencies.setter
    def agencies(self, agencies):
        """Sets the agencies of this GetStackMetadataResponse.

        委托授权的信息。  RFS仅在创建资源栈（触发部署）、创建执行计划、部署资源栈、删除资源栈等涉及资源操作的请求中使用委托，且该委托仅作用于与之绑定的Provider对资源的操作中。如果委托中提供的权限不足，有可能导致相关资源操作失败。  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)

        :param agencies: The agencies of this GetStackMetadataResponse.
        :type agencies: list[:class:`huaweicloudsdkaos.v1.Agency`]
        """
        self._agencies = agencies

    @property
    def status_message(self):
        """Gets the status_message of this GetStackMetadataResponse.

        当资源栈的状态为任意失败状态（即以 `FAILED` 结尾时），将会展示简要的错误信息总结以供debug

        :return: The status_message of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this GetStackMetadataResponse.

        当资源栈的状态为任意失败状态（即以 `FAILED` 结尾时），将会展示简要的错误信息总结以供debug

        :param status_message: The status_message of this GetStackMetadataResponse.
        :type status_message: str
        """
        self._status_message = status_message

    @property
    def vars_uri_content(self):
        """Gets the vars_uri_content of this GetStackMetadataResponse.

        vars_uri对应的文件内容

        :return: The vars_uri_content of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._vars_uri_content

    @vars_uri_content.setter
    def vars_uri_content(self, vars_uri_content):
        """Sets the vars_uri_content of this GetStackMetadataResponse.

        vars_uri对应的文件内容

        :param vars_uri_content: The vars_uri_content of this GetStackMetadataResponse.
        :type vars_uri_content: str
        """
        self._vars_uri_content = vars_uri_content

    @property
    def create_time(self):
        """Gets the create_time of this GetStackMetadataResponse.

        资源栈的生成时间 格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The create_time of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this GetStackMetadataResponse.

        资源栈的生成时间 格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param create_time: The create_time of this GetStackMetadataResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this GetStackMetadataResponse.

        资源栈的更新时间（更新场景包括元数据更新场景和部署场景） 格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The update_time of this GetStackMetadataResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this GetStackMetadataResponse.

        资源栈的更新时间（更新场景包括元数据更新场景和部署场景） 格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param update_time: The update_time of this GetStackMetadataResponse.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, GetStackMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
