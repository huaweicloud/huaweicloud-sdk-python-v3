# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStackSetMetadataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_set_id': 'str',
        'stack_set_name': 'str',
        'stack_set_description': 'str',
        'initial_stack_description': 'str',
        'permission_model': 'str',
        'administration_agency_name': 'str',
        'managed_agency_name': 'str',
        'status': 'str',
        'vars_uri_content': 'str',
        'vars_body': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'administration_agency_urn': 'str'
    }

    attribute_map = {
        'stack_set_id': 'stack_set_id',
        'stack_set_name': 'stack_set_name',
        'stack_set_description': 'stack_set_description',
        'initial_stack_description': 'initial_stack_description',
        'permission_model': 'permission_model',
        'administration_agency_name': 'administration_agency_name',
        'managed_agency_name': 'managed_agency_name',
        'status': 'status',
        'vars_uri_content': 'vars_uri_content',
        'vars_body': 'vars_body',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'administration_agency_urn': 'administration_agency_urn'
    }

    def __init__(self, stack_set_id=None, stack_set_name=None, stack_set_description=None, initial_stack_description=None, permission_model=None, administration_agency_name=None, managed_agency_name=None, status=None, vars_uri_content=None, vars_body=None, create_time=None, update_time=None, administration_agency_urn=None):
        """ShowStackSetMetadataResponse

        The model defined in huaweicloud sdk

        :param stack_set_id: 资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，在重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是又其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给与的stack_set_id和当前资源栈集的ID不一致，则返回400
        :type stack_set_id: str
        :param stack_set_name: 资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_set_name: str
        :param stack_set_description: 资源栈集的描述。可用于客户识别自己的资源栈集。
        :type stack_set_description: str
        :param initial_stack_description: 初始化资源栈描述。可用于客户识别被资源栈集所管理的资源栈。  资源栈集下的资源栈仅在创建时统一使用该描述。客户想要更新初始化资源栈描述，可以通过UpdateStackSet API。  后续更新资源栈集描述将不会同步更新已管理的资源栈描述。
        :type initial_stack_description: str
        :param permission_model: 权限模型，定义了RFS操作资源栈集时所需委托的创建方式，枚举值    * &#x60;SELF_MANAGED&#x60; - 基于部署需求，用户需要提前手动创建委托，既包含管理账号给RFS的委托，也包含成员账号创建给管理账号的委托。如果委托不存在或错误，创建资源栈集不会失败，部署资源栈集或部署资源栈实例的时候才会报错。
        :type permission_model: str
        :param administration_agency_name: 管理委托名称  资源编排服务使用该委托获取成员账号委托给管理账号的权限  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用v5委托时给与administration_agency_urn，administration_agency_name只支持接收v3委托名称，若给与了v5委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)
        :type administration_agency_name: str
        :param managed_agency_name: 被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)
        :type managed_agency_name: str
        :param status: 资源栈集的状态     * &#x60;IDLE&#x60; - 资源栈集空闲 * &#x60;OPERATION_IN_PROGRESS&#x60; - 资源栈集操作中 * &#x60;DEACTIVATED&#x60; - 资源栈集禁用
        :type status: str
        :param vars_uri_content: vars_uri对应的文件内容
        :type vars_uri_content: str
        :param vars_body: HCL参数文件的内容。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中  * 资源编排服务支持vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储对应的vars_body。
        :type vars_body: str
        :param create_time: 资源栈集的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type create_time: str
        :param update_time: 资源栈集的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type update_time: str
        :param administration_agency_urn: 管理委托URN  资源编排服务使用该委托获取成员账号委托给管理账号的权限  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用v5委托时给与administration_agency_urn，administration_agency_name只支持接收普通委托名称，若给与了v5委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。
        :type administration_agency_urn: str
        """
        
        super(ShowStackSetMetadataResponse, self).__init__()

        self._stack_set_id = None
        self._stack_set_name = None
        self._stack_set_description = None
        self._initial_stack_description = None
        self._permission_model = None
        self._administration_agency_name = None
        self._managed_agency_name = None
        self._status = None
        self._vars_uri_content = None
        self._vars_body = None
        self._create_time = None
        self._update_time = None
        self._administration_agency_urn = None
        self.discriminator = None

        if stack_set_id is not None:
            self.stack_set_id = stack_set_id
        self.stack_set_name = stack_set_name
        if stack_set_description is not None:
            self.stack_set_description = stack_set_description
        if initial_stack_description is not None:
            self.initial_stack_description = initial_stack_description
        if permission_model is not None:
            self.permission_model = permission_model
        if administration_agency_name is not None:
            self.administration_agency_name = administration_agency_name
        if managed_agency_name is not None:
            self.managed_agency_name = managed_agency_name
        if status is not None:
            self.status = status
        if vars_uri_content is not None:
            self.vars_uri_content = vars_uri_content
        if vars_body is not None:
            self.vars_body = vars_body
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if administration_agency_urn is not None:
            self.administration_agency_urn = administration_agency_urn

    @property
    def stack_set_id(self):
        """Gets the stack_set_id of this ShowStackSetMetadataResponse.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，在重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是又其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给与的stack_set_id和当前资源栈集的ID不一致，则返回400

        :return: The stack_set_id of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._stack_set_id

    @stack_set_id.setter
    def stack_set_id(self, stack_set_id):
        """Sets the stack_set_id of this ShowStackSetMetadataResponse.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，在重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是又其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给与的stack_set_id和当前资源栈集的ID不一致，则返回400

        :param stack_set_id: The stack_set_id of this ShowStackSetMetadataResponse.
        :type stack_set_id: str
        """
        self._stack_set_id = stack_set_id

    @property
    def stack_set_name(self):
        """Gets the stack_set_name of this ShowStackSetMetadataResponse.

        资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_set_name of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._stack_set_name

    @stack_set_name.setter
    def stack_set_name(self, stack_set_name):
        """Sets the stack_set_name of this ShowStackSetMetadataResponse.

        资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_set_name: The stack_set_name of this ShowStackSetMetadataResponse.
        :type stack_set_name: str
        """
        self._stack_set_name = stack_set_name

    @property
    def stack_set_description(self):
        """Gets the stack_set_description of this ShowStackSetMetadataResponse.

        资源栈集的描述。可用于客户识别自己的资源栈集。

        :return: The stack_set_description of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._stack_set_description

    @stack_set_description.setter
    def stack_set_description(self, stack_set_description):
        """Sets the stack_set_description of this ShowStackSetMetadataResponse.

        资源栈集的描述。可用于客户识别自己的资源栈集。

        :param stack_set_description: The stack_set_description of this ShowStackSetMetadataResponse.
        :type stack_set_description: str
        """
        self._stack_set_description = stack_set_description

    @property
    def initial_stack_description(self):
        """Gets the initial_stack_description of this ShowStackSetMetadataResponse.

        初始化资源栈描述。可用于客户识别被资源栈集所管理的资源栈。  资源栈集下的资源栈仅在创建时统一使用该描述。客户想要更新初始化资源栈描述，可以通过UpdateStackSet API。  后续更新资源栈集描述将不会同步更新已管理的资源栈描述。

        :return: The initial_stack_description of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._initial_stack_description

    @initial_stack_description.setter
    def initial_stack_description(self, initial_stack_description):
        """Sets the initial_stack_description of this ShowStackSetMetadataResponse.

        初始化资源栈描述。可用于客户识别被资源栈集所管理的资源栈。  资源栈集下的资源栈仅在创建时统一使用该描述。客户想要更新初始化资源栈描述，可以通过UpdateStackSet API。  后续更新资源栈集描述将不会同步更新已管理的资源栈描述。

        :param initial_stack_description: The initial_stack_description of this ShowStackSetMetadataResponse.
        :type initial_stack_description: str
        """
        self._initial_stack_description = initial_stack_description

    @property
    def permission_model(self):
        """Gets the permission_model of this ShowStackSetMetadataResponse.

        权限模型，定义了RFS操作资源栈集时所需委托的创建方式，枚举值    * `SELF_MANAGED` - 基于部署需求，用户需要提前手动创建委托，既包含管理账号给RFS的委托，也包含成员账号创建给管理账号的委托。如果委托不存在或错误，创建资源栈集不会失败，部署资源栈集或部署资源栈实例的时候才会报错。

        :return: The permission_model of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._permission_model

    @permission_model.setter
    def permission_model(self, permission_model):
        """Sets the permission_model of this ShowStackSetMetadataResponse.

        权限模型，定义了RFS操作资源栈集时所需委托的创建方式，枚举值    * `SELF_MANAGED` - 基于部署需求，用户需要提前手动创建委托，既包含管理账号给RFS的委托，也包含成员账号创建给管理账号的委托。如果委托不存在或错误，创建资源栈集不会失败，部署资源栈集或部署资源栈实例的时候才会报错。

        :param permission_model: The permission_model of this ShowStackSetMetadataResponse.
        :type permission_model: str
        """
        self._permission_model = permission_model

    @property
    def administration_agency_name(self):
        """Gets the administration_agency_name of this ShowStackSetMetadataResponse.

        管理委托名称  资源编排服务使用该委托获取成员账号委托给管理账号的权限  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用v5委托时给与administration_agency_urn，administration_agency_name只支持接收v3委托名称，若给与了v5委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)

        :return: The administration_agency_name of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._administration_agency_name

    @administration_agency_name.setter
    def administration_agency_name(self, administration_agency_name):
        """Sets the administration_agency_name of this ShowStackSetMetadataResponse.

        管理委托名称  资源编排服务使用该委托获取成员账号委托给管理账号的权限  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用v5委托时给与administration_agency_urn，administration_agency_name只支持接收v3委托名称，若给与了v5委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)

        :param administration_agency_name: The administration_agency_name of this ShowStackSetMetadataResponse.
        :type administration_agency_name: str
        """
        self._administration_agency_name = administration_agency_name

    @property
    def managed_agency_name(self):
        """Gets the managed_agency_name of this ShowStackSetMetadataResponse.

        被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)

        :return: The managed_agency_name of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._managed_agency_name

    @managed_agency_name.setter
    def managed_agency_name(self, managed_agency_name):
        """Sets the managed_agency_name of this ShowStackSetMetadataResponse.

        被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)

        :param managed_agency_name: The managed_agency_name of this ShowStackSetMetadataResponse.
        :type managed_agency_name: str
        """
        self._managed_agency_name = managed_agency_name

    @property
    def status(self):
        """Gets the status of this ShowStackSetMetadataResponse.

        资源栈集的状态     * `IDLE` - 资源栈集空闲 * `OPERATION_IN_PROGRESS` - 资源栈集操作中 * `DEACTIVATED` - 资源栈集禁用

        :return: The status of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowStackSetMetadataResponse.

        资源栈集的状态     * `IDLE` - 资源栈集空闲 * `OPERATION_IN_PROGRESS` - 资源栈集操作中 * `DEACTIVATED` - 资源栈集禁用

        :param status: The status of this ShowStackSetMetadataResponse.
        :type status: str
        """
        self._status = status

    @property
    def vars_uri_content(self):
        """Gets the vars_uri_content of this ShowStackSetMetadataResponse.

        vars_uri对应的文件内容

        :return: The vars_uri_content of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._vars_uri_content

    @vars_uri_content.setter
    def vars_uri_content(self, vars_uri_content):
        """Sets the vars_uri_content of this ShowStackSetMetadataResponse.

        vars_uri对应的文件内容

        :param vars_uri_content: The vars_uri_content of this ShowStackSetMetadataResponse.
        :type vars_uri_content: str
        """
        self._vars_uri_content = vars_uri_content

    @property
    def vars_body(self):
        """Gets the vars_body of this ShowStackSetMetadataResponse.

        HCL参数文件的内容。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中  * 资源编排服务支持vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储对应的vars_body。

        :return: The vars_body of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._vars_body

    @vars_body.setter
    def vars_body(self, vars_body):
        """Sets the vars_body of this ShowStackSetMetadataResponse.

        HCL参数文件的内容。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中  * 资源编排服务支持vars_body和vars_uri，如果他们中声名了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储对应的vars_body。

        :param vars_body: The vars_body of this ShowStackSetMetadataResponse.
        :type vars_body: str
        """
        self._vars_body = vars_body

    @property
    def create_time(self):
        """Gets the create_time of this ShowStackSetMetadataResponse.

        资源栈集的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The create_time of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowStackSetMetadataResponse.

        资源栈集的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param create_time: The create_time of this ShowStackSetMetadataResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowStackSetMetadataResponse.

        资源栈集的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The update_time of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowStackSetMetadataResponse.

        资源栈集的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param update_time: The update_time of this ShowStackSetMetadataResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def administration_agency_urn(self):
        """Gets the administration_agency_urn of this ShowStackSetMetadataResponse.

        管理委托URN  资源编排服务使用该委托获取成员账号委托给管理账号的权限  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用v5委托时给与administration_agency_urn，administration_agency_name只支持接收普通委托名称，若给与了v5委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。

        :return: The administration_agency_urn of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._administration_agency_urn

    @administration_agency_urn.setter
    def administration_agency_urn(self, administration_agency_urn):
        """Sets the administration_agency_urn of this ShowStackSetMetadataResponse.

        管理委托URN  资源编排服务使用该委托获取成员账号委托给管理账号的权限  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用v5委托时给与administration_agency_urn，administration_agency_name只支持接收普通委托名称，若给与了v5委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。

        :param administration_agency_urn: The administration_agency_urn of this ShowStackSetMetadataResponse.
        :type administration_agency_urn: str
        """
        self._administration_agency_urn = administration_agency_urn

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
        if not isinstance(other, ShowStackSetMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
