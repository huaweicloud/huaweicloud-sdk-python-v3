# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStackSetRequestBody:

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
        'stack_set_description': 'str',
        'initial_stack_description': 'str',
        'administration_agency_name': 'str',
        'managed_agency_name': 'str',
        'administration_agency_urn': 'str',
        'managed_operation': 'ManagedOperation',
        'call_identity': 'str'
    }

    attribute_map = {
        'stack_set_id': 'stack_set_id',
        'stack_set_description': 'stack_set_description',
        'initial_stack_description': 'initial_stack_description',
        'administration_agency_name': 'administration_agency_name',
        'managed_agency_name': 'managed_agency_name',
        'administration_agency_urn': 'administration_agency_urn',
        'managed_operation': 'managed_operation',
        'call_identity': 'call_identity'
    }

    def __init__(self, stack_set_id=None, stack_set_description=None, initial_stack_description=None, administration_agency_name=None, managed_agency_name=None, administration_agency_urn=None, managed_operation=None, call_identity=None):
        r"""UpdateStackSetRequestBody

        The model defined in huaweicloud sdk

        :param stack_set_id: 资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400
        :type stack_set_id: str
        :param stack_set_description: 资源栈集的描述。可用于客户识别自己的资源栈集。
        :type stack_set_description: str
        :param initial_stack_description: 初始化资源栈描述。可用于客户识别被资源栈集所管理的资源栈。  资源栈集下的资源栈仅在创建时统一使用该描述。客户想要更新初始化资源栈描述，可以通过UpdateStackSet API。  后续更新资源栈集描述将不会同步更新已管理的资源栈描述。
        :type initial_stack_description: str
        :param administration_agency_name: 管理委托名称  资源编排服务使用该委托获取成员账号委托给管理账号的权限。该委托中必须含有iam:tokens:assume权限，用以后续获取被管理委托凭证。如果不包含，则会在新增或者部署实例时报错。  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用信任委托时给予administration_agency_urn，administration_agency_name只支持接收委托名称，如果给予了信任委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)
        :type administration_agency_name: str
        :param managed_agency_name: 被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)
        :type managed_agency_name: str
        :param administration_agency_urn: 管理委托URN  资源编排服务使用该委托获取成员账号委托给管理账号的权限。该委托中必须含有sts:tokens:assume权限，用以后续获取被管理委托凭证。如果不包含，则会在新增或者部署实例时报错。  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用信任委托时给予administration_agency_urn，administration_agency_name只支持接收委托名称，如果给予了信任委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。
        :type administration_agency_urn: str
        :param managed_operation: 
        :type managed_operation: :class:`huaweicloudsdkaos.v1.ManagedOperation`
        :param call_identity: 仅支持资源栈集权限模式为SERVICE_MANAGED时指定该参数。用于指定用户是以组织管理账号还是成员账号中的服务委托管理员身份调用资源栈集。默认为SELF。 当资源栈集权限模式为SELF_MANAGED时，默认为SELF。 * 无论指定何种用户身份，涉及操作的资源栈集始终在组织管理账号名下。*   * &#x60;SELF&#x60; - 以组织管理账号身份调用。   * &#x60;DELEGATED_ADMIN&#x60; - 以服务委托管理员身份调用。用户的华为云账号必须在组织中已经被注册为”资源编排资源栈集服务“的委托管理员。
        :type call_identity: str
        """
        
        

        self._stack_set_id = None
        self._stack_set_description = None
        self._initial_stack_description = None
        self._administration_agency_name = None
        self._managed_agency_name = None
        self._administration_agency_urn = None
        self._managed_operation = None
        self._call_identity = None
        self.discriminator = None

        if stack_set_id is not None:
            self.stack_set_id = stack_set_id
        if stack_set_description is not None:
            self.stack_set_description = stack_set_description
        if initial_stack_description is not None:
            self.initial_stack_description = initial_stack_description
        if administration_agency_name is not None:
            self.administration_agency_name = administration_agency_name
        if managed_agency_name is not None:
            self.managed_agency_name = managed_agency_name
        if administration_agency_urn is not None:
            self.administration_agency_urn = administration_agency_urn
        if managed_operation is not None:
            self.managed_operation = managed_operation
        if call_identity is not None:
            self.call_identity = call_identity

    @property
    def stack_set_id(self):
        r"""Gets the stack_set_id of this UpdateStackSetRequestBody.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :return: The stack_set_id of this UpdateStackSetRequestBody.
        :rtype: str
        """
        return self._stack_set_id

    @stack_set_id.setter
    def stack_set_id(self, stack_set_id):
        r"""Sets the stack_set_id of this UpdateStackSetRequestBody.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :param stack_set_id: The stack_set_id of this UpdateStackSetRequestBody.
        :type stack_set_id: str
        """
        self._stack_set_id = stack_set_id

    @property
    def stack_set_description(self):
        r"""Gets the stack_set_description of this UpdateStackSetRequestBody.

        资源栈集的描述。可用于客户识别自己的资源栈集。

        :return: The stack_set_description of this UpdateStackSetRequestBody.
        :rtype: str
        """
        return self._stack_set_description

    @stack_set_description.setter
    def stack_set_description(self, stack_set_description):
        r"""Sets the stack_set_description of this UpdateStackSetRequestBody.

        资源栈集的描述。可用于客户识别自己的资源栈集。

        :param stack_set_description: The stack_set_description of this UpdateStackSetRequestBody.
        :type stack_set_description: str
        """
        self._stack_set_description = stack_set_description

    @property
    def initial_stack_description(self):
        r"""Gets the initial_stack_description of this UpdateStackSetRequestBody.

        初始化资源栈描述。可用于客户识别被资源栈集所管理的资源栈。  资源栈集下的资源栈仅在创建时统一使用该描述。客户想要更新初始化资源栈描述，可以通过UpdateStackSet API。  后续更新资源栈集描述将不会同步更新已管理的资源栈描述。

        :return: The initial_stack_description of this UpdateStackSetRequestBody.
        :rtype: str
        """
        return self._initial_stack_description

    @initial_stack_description.setter
    def initial_stack_description(self, initial_stack_description):
        r"""Sets the initial_stack_description of this UpdateStackSetRequestBody.

        初始化资源栈描述。可用于客户识别被资源栈集所管理的资源栈。  资源栈集下的资源栈仅在创建时统一使用该描述。客户想要更新初始化资源栈描述，可以通过UpdateStackSet API。  后续更新资源栈集描述将不会同步更新已管理的资源栈描述。

        :param initial_stack_description: The initial_stack_description of this UpdateStackSetRequestBody.
        :type initial_stack_description: str
        """
        self._initial_stack_description = initial_stack_description

    @property
    def administration_agency_name(self):
        r"""Gets the administration_agency_name of this UpdateStackSetRequestBody.

        管理委托名称  资源编排服务使用该委托获取成员账号委托给管理账号的权限。该委托中必须含有iam:tokens:assume权限，用以后续获取被管理委托凭证。如果不包含，则会在新增或者部署实例时报错。  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用信任委托时给予administration_agency_urn，administration_agency_name只支持接收委托名称，如果给予了信任委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)

        :return: The administration_agency_name of this UpdateStackSetRequestBody.
        :rtype: str
        """
        return self._administration_agency_name

    @administration_agency_name.setter
    def administration_agency_name(self, administration_agency_name):
        r"""Sets the administration_agency_name of this UpdateStackSetRequestBody.

        管理委托名称  资源编排服务使用该委托获取成员账号委托给管理账号的权限。该委托中必须含有iam:tokens:assume权限，用以后续获取被管理委托凭证。如果不包含，则会在新增或者部署实例时报错。  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用信任委托时给予administration_agency_urn，administration_agency_name只支持接收委托名称，如果给予了信任委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)

        :param administration_agency_name: The administration_agency_name of this UpdateStackSetRequestBody.
        :type administration_agency_name: str
        """
        self._administration_agency_name = administration_agency_name

    @property
    def managed_agency_name(self):
        r"""Gets the managed_agency_name of this UpdateStackSetRequestBody.

        被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)

        :return: The managed_agency_name of this UpdateStackSetRequestBody.
        :rtype: str
        """
        return self._managed_agency_name

    @managed_agency_name.setter
    def managed_agency_name(self, managed_agency_name):
        r"""Sets the managed_agency_name of this UpdateStackSetRequestBody.

        被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [[创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)](tag:hws) [[创建委托及授权方式](https://support.huaweicloud.com/intl/zh-cn/usermanual-iam/iam_06_0002.html)](tag:hws_hk) [[创建委托及授权方式](https://support.huaweicloud.com/eu/usermanual-iam/iam_06_0002.html)](tag:hws_eu)

        :param managed_agency_name: The managed_agency_name of this UpdateStackSetRequestBody.
        :type managed_agency_name: str
        """
        self._managed_agency_name = managed_agency_name

    @property
    def administration_agency_urn(self):
        r"""Gets the administration_agency_urn of this UpdateStackSetRequestBody.

        管理委托URN  资源编排服务使用该委托获取成员账号委托给管理账号的权限。该委托中必须含有sts:tokens:assume权限，用以后续获取被管理委托凭证。如果不包含，则会在新增或者部署实例时报错。  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用信任委托时给予administration_agency_urn，administration_agency_name只支持接收委托名称，如果给予了信任委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。

        :return: The administration_agency_urn of this UpdateStackSetRequestBody.
        :rtype: str
        """
        return self._administration_agency_urn

    @administration_agency_urn.setter
    def administration_agency_urn(self, administration_agency_urn):
        r"""Sets the administration_agency_urn of this UpdateStackSetRequestBody.

        管理委托URN  资源编排服务使用该委托获取成员账号委托给管理账号的权限。该委托中必须含有sts:tokens:assume权限，用以后续获取被管理委托凭证。如果不包含，则会在新增或者部署实例时报错。  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用信任委托时给予administration_agency_urn，administration_agency_name只支持接收委托名称，如果给予了信任委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。

        :param administration_agency_urn: The administration_agency_urn of this UpdateStackSetRequestBody.
        :type administration_agency_urn: str
        """
        self._administration_agency_urn = administration_agency_urn

    @property
    def managed_operation(self):
        r"""Gets the managed_operation of this UpdateStackSetRequestBody.

        :return: The managed_operation of this UpdateStackSetRequestBody.
        :rtype: :class:`huaweicloudsdkaos.v1.ManagedOperation`
        """
        return self._managed_operation

    @managed_operation.setter
    def managed_operation(self, managed_operation):
        r"""Sets the managed_operation of this UpdateStackSetRequestBody.

        :param managed_operation: The managed_operation of this UpdateStackSetRequestBody.
        :type managed_operation: :class:`huaweicloudsdkaos.v1.ManagedOperation`
        """
        self._managed_operation = managed_operation

    @property
    def call_identity(self):
        r"""Gets the call_identity of this UpdateStackSetRequestBody.

        仅支持资源栈集权限模式为SERVICE_MANAGED时指定该参数。用于指定用户是以组织管理账号还是成员账号中的服务委托管理员身份调用资源栈集。默认为SELF。 当资源栈集权限模式为SELF_MANAGED时，默认为SELF。 * 无论指定何种用户身份，涉及操作的资源栈集始终在组织管理账号名下。*   * `SELF` - 以组织管理账号身份调用。   * `DELEGATED_ADMIN` - 以服务委托管理员身份调用。用户的华为云账号必须在组织中已经被注册为”资源编排资源栈集服务“的委托管理员。

        :return: The call_identity of this UpdateStackSetRequestBody.
        :rtype: str
        """
        return self._call_identity

    @call_identity.setter
    def call_identity(self, call_identity):
        r"""Sets the call_identity of this UpdateStackSetRequestBody.

        仅支持资源栈集权限模式为SERVICE_MANAGED时指定该参数。用于指定用户是以组织管理账号还是成员账号中的服务委托管理员身份调用资源栈集。默认为SELF。 当资源栈集权限模式为SELF_MANAGED时，默认为SELF。 * 无论指定何种用户身份，涉及操作的资源栈集始终在组织管理账号名下。*   * `SELF` - 以组织管理账号身份调用。   * `DELEGATED_ADMIN` - 以服务委托管理员身份调用。用户的华为云账号必须在组织中已经被注册为”资源编排资源栈集服务“的委托管理员。

        :param call_identity: The call_identity of this UpdateStackSetRequestBody.
        :type call_identity: str
        """
        self._call_identity = call_identity

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
        if not isinstance(other, UpdateStackSetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
