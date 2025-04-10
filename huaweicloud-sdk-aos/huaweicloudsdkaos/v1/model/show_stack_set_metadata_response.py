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
        'administration_agency_urn': 'str',
        'managed_operation': 'ManagedOperation',
        'organizational_unit_ids': 'list[str]'
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
        'administration_agency_urn': 'administration_agency_urn',
        'managed_operation': 'managed_operation',
        'organizational_unit_ids': 'organizational_unit_ids'
    }

    def __init__(self, stack_set_id=None, stack_set_name=None, stack_set_description=None, initial_stack_description=None, permission_model=None, administration_agency_name=None, managed_agency_name=None, status=None, vars_uri_content=None, vars_body=None, create_time=None, update_time=None, administration_agency_urn=None, managed_operation=None, organizational_unit_ids=None):
        r"""ShowStackSetMetadataResponse

        The model defined in huaweicloud sdk

        :param stack_set_id: 资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400
        :type stack_set_id: str
        :param stack_set_name: 资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_set_name: str
        :param stack_set_description: 资源栈集的描述。可用于客户识别自己的资源栈集。
        :type stack_set_description: str
        :param initial_stack_description: 初始化资源栈描述。可用于客户识别被资源栈集所管理的资源栈。  资源栈集下的资源栈仅在创建时统一使用该描述。客户想要更新初始化资源栈描述，可以通过UpdateStackSet API。  后续更新资源栈集描述将不会同步更新已管理的资源栈描述。
        :type initial_stack_description: str
        :param permission_model: 权限模型，定义了RFS操作资源栈集时所需委托的创建方式，枚举值，默认为SELF_MANAGED。用户可以使用创建资源栈集（CreateStackSet）API 指定该参数。该参数暂不支持更新。用户如果想要更新权限模型，可以通过先删除再创建同名资源栈集实现。   * &#x60;SELF_MANAGED&#x60; - 自我管理，基于部署需求，用户需要提前手动创建委托，既包含管理账号授权给RFS的委托，也包含成员账号授权给管理账号的委托。如果委托不存在或权限不足，创建资源栈集不会失败，创建资源栈实例时才会报错。   * &#x60;SERVICE_MANAGED&#x60; - 服务管理，基于Organization服务，RFS会自动创建部署Organization 成员账号时所需的全部 IAM 委托。用户需要提前在Organization可信服务列表中将”资源编排资源栈集服务“启用，且只有Organization的管理账号或”资源编排资源栈集服务“的委托管理员，才允许指定SERVICE_MANAGED创建资源栈集，否则会报错。
        :type permission_model: str
        :param administration_agency_name: 管理委托名称  资源编排服务使用该委托获取成员账号委托给管理账号的权限。该委托中必须含有iam:tokens:assume权限，用以后续获取被管理委托凭证。如果不包含，则会在新增或者部署实例时报错。  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用信任委托时给予administration_agency_urn，administration_agency_name只支持接收委托名称，如果给予了信任委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)
        :type administration_agency_name: str
        :param managed_agency_name: 被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)
        :type managed_agency_name: str
        :param status: 资源栈集的状态     * &#x60;IDLE&#x60; - 资源栈集空闲 * &#x60;OPERATION_IN_PROGRESS&#x60; - 资源栈集操作中 * &#x60;DEACTIVATED&#x60; - 资源栈集禁用
        :type status: str
        :param vars_uri_content: vars_uri对应的文件内容
        :type vars_uri_content: str
        :param vars_body: HCL参数文件的内容。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中  * 资源编排服务支持vars_body和vars_uri，如果以上两种方式中声明了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储对应的vars_body。
        :type vars_body: str
        :param create_time: 资源栈集的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type create_time: str
        :param update_time: 资源栈集的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type update_time: str
        :param administration_agency_urn: 管理委托URN  资源编排服务使用该委托获取成员账号委托给管理账号的权限。该委托中必须含有sts:tokens:assume权限，用以后续获取被管理委托凭证。如果不包含，则会在新增或者部署实例时报错。  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用信任委托时给予administration_agency_urn，administration_agency_name只支持接收委托名称，如果给予了信任委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。
        :type administration_agency_urn: str
        :param managed_operation: 
        :type managed_operation: :class:`huaweicloudsdkaos.v1.ManagedOperation`
        :param organizational_unit_ids: 组织单元（Organizational Unit，缩写OU）ID列表，仅在资源栈集权限模型是SERVICE_MANAGED时，才允许指定该参数。  用户指定的Organization组织部署的ID列表，可以是根组织（Root）ID，也可以是某些组织单元的ID。  创建资源栈实例 （CreateStackInstances）API 必须指定该参数，该API 会异步校验OU IDs 的合法性，校验有效的OU IDs 及其所有非空子OU ID 都会被资源栈集记录管理。该API允许指定没有或者已经被资源栈集管理的OU IDs。   * 若资源栈集不自动部署，空子OU不会被资源栈集记录管理（特指子OU下无成员账号或部署排除其下所有成员账号）。*   * 【暂不支持】若资源栈集开启自动部署，空子OU也会被资源栈集记录管理（特指子OU下无成员账号或部署排除其下所有成员账号），自动部署仅针对成员账号变动，不针对其他组织结构变化，例如新增OU等，新增OU不会自动被资源栈集管理。*  部署或删除资源栈实例（DeployStackSet、UpdateStackInstances、DeleteStackInstances） API，只允许指定已经被资源栈集管理的OU IDs。若指定了没有被资源栈集记录管理的OU IDs，则会报错。  删除资源栈实例 （DeleteStackInstances）API 必须指定该参数。  用户可以通过获取资源栈集元数据（ShowStackSetMetadata）API ，获取通过创建资源栈实例（CreateStackInstances）API 请求指定过的OU IDs。  资源栈集不仅会部署到目标 OU 中的用户，同时还会部署所有子 OU 下的用户。指定该参数后，资源栈集会根据用户输入的 OU 列表下所有的用户信息（包含子 OU 下的用户）和region列表，以笛卡尔积的形式，选择资源栈实例进行创建或部署。  *资源栈集不会选择组织管理员作为部署目标，进行资源栈实例的创建或部署，即使组织管理员位于给与的组织或组织的 OU 中。*
        :type organizational_unit_ids: list[str]
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
        self._managed_operation = None
        self._organizational_unit_ids = None
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
        if managed_operation is not None:
            self.managed_operation = managed_operation
        if organizational_unit_ids is not None:
            self.organizational_unit_ids = organizational_unit_ids

    @property
    def stack_set_id(self):
        r"""Gets the stack_set_id of this ShowStackSetMetadataResponse.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :return: The stack_set_id of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._stack_set_id

    @stack_set_id.setter
    def stack_set_id(self, stack_set_id):
        r"""Sets the stack_set_id of this ShowStackSetMetadataResponse.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :param stack_set_id: The stack_set_id of this ShowStackSetMetadataResponse.
        :type stack_set_id: str
        """
        self._stack_set_id = stack_set_id

    @property
    def stack_set_name(self):
        r"""Gets the stack_set_name of this ShowStackSetMetadataResponse.

        资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_set_name of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._stack_set_name

    @stack_set_name.setter
    def stack_set_name(self, stack_set_name):
        r"""Sets the stack_set_name of this ShowStackSetMetadataResponse.

        资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_set_name: The stack_set_name of this ShowStackSetMetadataResponse.
        :type stack_set_name: str
        """
        self._stack_set_name = stack_set_name

    @property
    def stack_set_description(self):
        r"""Gets the stack_set_description of this ShowStackSetMetadataResponse.

        资源栈集的描述。可用于客户识别自己的资源栈集。

        :return: The stack_set_description of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._stack_set_description

    @stack_set_description.setter
    def stack_set_description(self, stack_set_description):
        r"""Sets the stack_set_description of this ShowStackSetMetadataResponse.

        资源栈集的描述。可用于客户识别自己的资源栈集。

        :param stack_set_description: The stack_set_description of this ShowStackSetMetadataResponse.
        :type stack_set_description: str
        """
        self._stack_set_description = stack_set_description

    @property
    def initial_stack_description(self):
        r"""Gets the initial_stack_description of this ShowStackSetMetadataResponse.

        初始化资源栈描述。可用于客户识别被资源栈集所管理的资源栈。  资源栈集下的资源栈仅在创建时统一使用该描述。客户想要更新初始化资源栈描述，可以通过UpdateStackSet API。  后续更新资源栈集描述将不会同步更新已管理的资源栈描述。

        :return: The initial_stack_description of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._initial_stack_description

    @initial_stack_description.setter
    def initial_stack_description(self, initial_stack_description):
        r"""Sets the initial_stack_description of this ShowStackSetMetadataResponse.

        初始化资源栈描述。可用于客户识别被资源栈集所管理的资源栈。  资源栈集下的资源栈仅在创建时统一使用该描述。客户想要更新初始化资源栈描述，可以通过UpdateStackSet API。  后续更新资源栈集描述将不会同步更新已管理的资源栈描述。

        :param initial_stack_description: The initial_stack_description of this ShowStackSetMetadataResponse.
        :type initial_stack_description: str
        """
        self._initial_stack_description = initial_stack_description

    @property
    def permission_model(self):
        r"""Gets the permission_model of this ShowStackSetMetadataResponse.

        权限模型，定义了RFS操作资源栈集时所需委托的创建方式，枚举值，默认为SELF_MANAGED。用户可以使用创建资源栈集（CreateStackSet）API 指定该参数。该参数暂不支持更新。用户如果想要更新权限模型，可以通过先删除再创建同名资源栈集实现。   * `SELF_MANAGED` - 自我管理，基于部署需求，用户需要提前手动创建委托，既包含管理账号授权给RFS的委托，也包含成员账号授权给管理账号的委托。如果委托不存在或权限不足，创建资源栈集不会失败，创建资源栈实例时才会报错。   * `SERVICE_MANAGED` - 服务管理，基于Organization服务，RFS会自动创建部署Organization 成员账号时所需的全部 IAM 委托。用户需要提前在Organization可信服务列表中将”资源编排资源栈集服务“启用，且只有Organization的管理账号或”资源编排资源栈集服务“的委托管理员，才允许指定SERVICE_MANAGED创建资源栈集，否则会报错。

        :return: The permission_model of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._permission_model

    @permission_model.setter
    def permission_model(self, permission_model):
        r"""Sets the permission_model of this ShowStackSetMetadataResponse.

        权限模型，定义了RFS操作资源栈集时所需委托的创建方式，枚举值，默认为SELF_MANAGED。用户可以使用创建资源栈集（CreateStackSet）API 指定该参数。该参数暂不支持更新。用户如果想要更新权限模型，可以通过先删除再创建同名资源栈集实现。   * `SELF_MANAGED` - 自我管理，基于部署需求，用户需要提前手动创建委托，既包含管理账号授权给RFS的委托，也包含成员账号授权给管理账号的委托。如果委托不存在或权限不足，创建资源栈集不会失败，创建资源栈实例时才会报错。   * `SERVICE_MANAGED` - 服务管理，基于Organization服务，RFS会自动创建部署Organization 成员账号时所需的全部 IAM 委托。用户需要提前在Organization可信服务列表中将”资源编排资源栈集服务“启用，且只有Organization的管理账号或”资源编排资源栈集服务“的委托管理员，才允许指定SERVICE_MANAGED创建资源栈集，否则会报错。

        :param permission_model: The permission_model of this ShowStackSetMetadataResponse.
        :type permission_model: str
        """
        self._permission_model = permission_model

    @property
    def administration_agency_name(self):
        r"""Gets the administration_agency_name of this ShowStackSetMetadataResponse.

        管理委托名称  资源编排服务使用该委托获取成员账号委托给管理账号的权限。该委托中必须含有iam:tokens:assume权限，用以后续获取被管理委托凭证。如果不包含，则会在新增或者部署实例时报错。  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用信任委托时给予administration_agency_urn，administration_agency_name只支持接收委托名称，如果给予了信任委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)

        :return: The administration_agency_name of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._administration_agency_name

    @administration_agency_name.setter
    def administration_agency_name(self, administration_agency_name):
        r"""Sets the administration_agency_name of this ShowStackSetMetadataResponse.

        管理委托名称  资源编排服务使用该委托获取成员账号委托给管理账号的权限。该委托中必须含有iam:tokens:assume权限，用以后续获取被管理委托凭证。如果不包含，则会在新增或者部署实例时报错。  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用信任委托时给予administration_agency_urn，administration_agency_name只支持接收委托名称，如果给予了信任委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)

        :param administration_agency_name: The administration_agency_name of this ShowStackSetMetadataResponse.
        :type administration_agency_name: str
        """
        self._administration_agency_name = administration_agency_name

    @property
    def managed_agency_name(self):
        r"""Gets the managed_agency_name of this ShowStackSetMetadataResponse.

        被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)

        :return: The managed_agency_name of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._managed_agency_name

    @managed_agency_name.setter
    def managed_agency_name(self, managed_agency_name):
        r"""Sets the managed_agency_name of this ShowStackSetMetadataResponse.

        被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)

        :param managed_agency_name: The managed_agency_name of this ShowStackSetMetadataResponse.
        :type managed_agency_name: str
        """
        self._managed_agency_name = managed_agency_name

    @property
    def status(self):
        r"""Gets the status of this ShowStackSetMetadataResponse.

        资源栈集的状态     * `IDLE` - 资源栈集空闲 * `OPERATION_IN_PROGRESS` - 资源栈集操作中 * `DEACTIVATED` - 资源栈集禁用

        :return: The status of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowStackSetMetadataResponse.

        资源栈集的状态     * `IDLE` - 资源栈集空闲 * `OPERATION_IN_PROGRESS` - 资源栈集操作中 * `DEACTIVATED` - 资源栈集禁用

        :param status: The status of this ShowStackSetMetadataResponse.
        :type status: str
        """
        self._status = status

    @property
    def vars_uri_content(self):
        r"""Gets the vars_uri_content of this ShowStackSetMetadataResponse.

        vars_uri对应的文件内容

        :return: The vars_uri_content of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._vars_uri_content

    @vars_uri_content.setter
    def vars_uri_content(self, vars_uri_content):
        r"""Sets the vars_uri_content of this ShowStackSetMetadataResponse.

        vars_uri对应的文件内容

        :param vars_uri_content: The vars_uri_content of this ShowStackSetMetadataResponse.
        :type vars_uri_content: str
        """
        self._vars_uri_content = vars_uri_content

    @property
    def vars_body(self):
        r"""Gets the vars_body of this ShowStackSetMetadataResponse.

        HCL参数文件的内容。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中  * 资源编排服务支持vars_body和vars_uri，如果以上两种方式中声明了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储对应的vars_body。

        :return: The vars_body of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._vars_body

    @vars_body.setter
    def vars_body(self, vars_body):
        r"""Sets the vars_body of this ShowStackSetMetadataResponse.

        HCL参数文件的内容。HCL模板支持参数传入，即，同一个模板可以给予不同的参数而达到不同的效果。  * vars_body使用HCL的tfvars格式，用户可以将“.tfvars”中的内容提交到vars_body中  * 资源编排服务支持vars_body和vars_uri，如果以上两种方式中声明了同一个变量，将报错400  * 如果vars_body过大，可以使用vars_uri  * 资源栈集不支持敏感数据加密，资源编排服务会直接明文使用、log、展示、存储对应的vars_body。

        :param vars_body: The vars_body of this ShowStackSetMetadataResponse.
        :type vars_body: str
        """
        self._vars_body = vars_body

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowStackSetMetadataResponse.

        资源栈集的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The create_time of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowStackSetMetadataResponse.

        资源栈集的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param create_time: The create_time of this ShowStackSetMetadataResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowStackSetMetadataResponse.

        资源栈集的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The update_time of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowStackSetMetadataResponse.

        资源栈集的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param update_time: The update_time of this ShowStackSetMetadataResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def administration_agency_urn(self):
        r"""Gets the administration_agency_urn of this ShowStackSetMetadataResponse.

        管理委托URN  资源编排服务使用该委托获取成员账号委托给管理账号的权限。该委托中必须含有sts:tokens:assume权限，用以后续获取被管理委托凭证。如果不包含，则会在新增或者部署实例时报错。  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用信任委托时给予administration_agency_urn，administration_agency_name只支持接收委托名称，如果给予了信任委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。

        :return: The administration_agency_urn of this ShowStackSetMetadataResponse.
        :rtype: str
        """
        return self._administration_agency_urn

    @administration_agency_urn.setter
    def administration_agency_urn(self, administration_agency_urn):
        r"""Sets the administration_agency_urn of this ShowStackSetMetadataResponse.

        管理委托URN  资源编排服务使用该委托获取成员账号委托给管理账号的权限。该委托中必须含有sts:tokens:assume权限，用以后续获取被管理委托凭证。如果不包含，则会在新增或者部署实例时报错。  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用信任委托时给予administration_agency_urn，administration_agency_name只支持接收委托名称，如果给予了信任委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。

        :param administration_agency_urn: The administration_agency_urn of this ShowStackSetMetadataResponse.
        :type administration_agency_urn: str
        """
        self._administration_agency_urn = administration_agency_urn

    @property
    def managed_operation(self):
        r"""Gets the managed_operation of this ShowStackSetMetadataResponse.

        :return: The managed_operation of this ShowStackSetMetadataResponse.
        :rtype: :class:`huaweicloudsdkaos.v1.ManagedOperation`
        """
        return self._managed_operation

    @managed_operation.setter
    def managed_operation(self, managed_operation):
        r"""Sets the managed_operation of this ShowStackSetMetadataResponse.

        :param managed_operation: The managed_operation of this ShowStackSetMetadataResponse.
        :type managed_operation: :class:`huaweicloudsdkaos.v1.ManagedOperation`
        """
        self._managed_operation = managed_operation

    @property
    def organizational_unit_ids(self):
        r"""Gets the organizational_unit_ids of this ShowStackSetMetadataResponse.

        组织单元（Organizational Unit，缩写OU）ID列表，仅在资源栈集权限模型是SERVICE_MANAGED时，才允许指定该参数。  用户指定的Organization组织部署的ID列表，可以是根组织（Root）ID，也可以是某些组织单元的ID。  创建资源栈实例 （CreateStackInstances）API 必须指定该参数，该API 会异步校验OU IDs 的合法性，校验有效的OU IDs 及其所有非空子OU ID 都会被资源栈集记录管理。该API允许指定没有或者已经被资源栈集管理的OU IDs。   * 若资源栈集不自动部署，空子OU不会被资源栈集记录管理（特指子OU下无成员账号或部署排除其下所有成员账号）。*   * 【暂不支持】若资源栈集开启自动部署，空子OU也会被资源栈集记录管理（特指子OU下无成员账号或部署排除其下所有成员账号），自动部署仅针对成员账号变动，不针对其他组织结构变化，例如新增OU等，新增OU不会自动被资源栈集管理。*  部署或删除资源栈实例（DeployStackSet、UpdateStackInstances、DeleteStackInstances） API，只允许指定已经被资源栈集管理的OU IDs。若指定了没有被资源栈集记录管理的OU IDs，则会报错。  删除资源栈实例 （DeleteStackInstances）API 必须指定该参数。  用户可以通过获取资源栈集元数据（ShowStackSetMetadata）API ，获取通过创建资源栈实例（CreateStackInstances）API 请求指定过的OU IDs。  资源栈集不仅会部署到目标 OU 中的用户，同时还会部署所有子 OU 下的用户。指定该参数后，资源栈集会根据用户输入的 OU 列表下所有的用户信息（包含子 OU 下的用户）和region列表，以笛卡尔积的形式，选择资源栈实例进行创建或部署。  *资源栈集不会选择组织管理员作为部署目标，进行资源栈实例的创建或部署，即使组织管理员位于给与的组织或组织的 OU 中。*

        :return: The organizational_unit_ids of this ShowStackSetMetadataResponse.
        :rtype: list[str]
        """
        return self._organizational_unit_ids

    @organizational_unit_ids.setter
    def organizational_unit_ids(self, organizational_unit_ids):
        r"""Sets the organizational_unit_ids of this ShowStackSetMetadataResponse.

        组织单元（Organizational Unit，缩写OU）ID列表，仅在资源栈集权限模型是SERVICE_MANAGED时，才允许指定该参数。  用户指定的Organization组织部署的ID列表，可以是根组织（Root）ID，也可以是某些组织单元的ID。  创建资源栈实例 （CreateStackInstances）API 必须指定该参数，该API 会异步校验OU IDs 的合法性，校验有效的OU IDs 及其所有非空子OU ID 都会被资源栈集记录管理。该API允许指定没有或者已经被资源栈集管理的OU IDs。   * 若资源栈集不自动部署，空子OU不会被资源栈集记录管理（特指子OU下无成员账号或部署排除其下所有成员账号）。*   * 【暂不支持】若资源栈集开启自动部署，空子OU也会被资源栈集记录管理（特指子OU下无成员账号或部署排除其下所有成员账号），自动部署仅针对成员账号变动，不针对其他组织结构变化，例如新增OU等，新增OU不会自动被资源栈集管理。*  部署或删除资源栈实例（DeployStackSet、UpdateStackInstances、DeleteStackInstances） API，只允许指定已经被资源栈集管理的OU IDs。若指定了没有被资源栈集记录管理的OU IDs，则会报错。  删除资源栈实例 （DeleteStackInstances）API 必须指定该参数。  用户可以通过获取资源栈集元数据（ShowStackSetMetadata）API ，获取通过创建资源栈实例（CreateStackInstances）API 请求指定过的OU IDs。  资源栈集不仅会部署到目标 OU 中的用户，同时还会部署所有子 OU 下的用户。指定该参数后，资源栈集会根据用户输入的 OU 列表下所有的用户信息（包含子 OU 下的用户）和region列表，以笛卡尔积的形式，选择资源栈实例进行创建或部署。  *资源栈集不会选择组织管理员作为部署目标，进行资源栈实例的创建或部署，即使组织管理员位于给与的组织或组织的 OU 中。*

        :param organizational_unit_ids: The organizational_unit_ids of this ShowStackSetMetadataResponse.
        :type organizational_unit_ids: list[str]
        """
        self._organizational_unit_ids = organizational_unit_ids

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
