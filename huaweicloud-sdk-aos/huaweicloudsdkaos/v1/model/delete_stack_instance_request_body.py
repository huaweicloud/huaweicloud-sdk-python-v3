# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteStackInstanceRequestBody:

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
        'deployment_targets': 'DeploymentTargets',
        'operation_preferences': 'OperationPreferences',
        'call_identity': 'str'
    }

    attribute_map = {
        'stack_set_id': 'stack_set_id',
        'deployment_targets': 'deployment_targets',
        'operation_preferences': 'operation_preferences',
        'call_identity': 'call_identity'
    }

    def __init__(self, stack_set_id=None, deployment_targets=None, operation_preferences=None, call_identity=None):
        r"""DeleteStackInstanceRequestBody

        The model defined in huaweicloud sdk

        :param stack_set_id: 资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400
        :type stack_set_id: str
        :param deployment_targets: 
        :type deployment_targets: :class:`huaweicloudsdkaos.v1.DeploymentTargets`
        :param operation_preferences: 
        :type operation_preferences: :class:`huaweicloudsdkaos.v1.OperationPreferences`
        :param call_identity: 仅支持资源栈集权限模式为SERVICE_MANAGED时指定该参数。用于指定用户是以组织管理账号还是成员账号中的服务委托管理员身份调用资源栈集。默认为SELF。 当资源栈集权限模式为SELF_MANAGED时，默认为SELF。 * 无论指定何种用户身份，涉及操作的资源栈集始终在组织管理账号名下。*   * &#x60;SELF&#x60; - 以组织管理账号身份调用。   * &#x60;DELEGATED_ADMIN&#x60; - 以服务委托管理员身份调用。用户的华为云账号必须在组织中已经被注册为”资源编排资源栈集服务“的委托管理员。
        :type call_identity: str
        """
        
        

        self._stack_set_id = None
        self._deployment_targets = None
        self._operation_preferences = None
        self._call_identity = None
        self.discriminator = None

        if stack_set_id is not None:
            self.stack_set_id = stack_set_id
        self.deployment_targets = deployment_targets
        if operation_preferences is not None:
            self.operation_preferences = operation_preferences
        if call_identity is not None:
            self.call_identity = call_identity

    @property
    def stack_set_id(self):
        r"""Gets the stack_set_id of this DeleteStackInstanceRequestBody.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :return: The stack_set_id of this DeleteStackInstanceRequestBody.
        :rtype: str
        """
        return self._stack_set_id

    @stack_set_id.setter
    def stack_set_id(self, stack_set_id):
        r"""Sets the stack_set_id of this DeleteStackInstanceRequestBody.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :param stack_set_id: The stack_set_id of this DeleteStackInstanceRequestBody.
        :type stack_set_id: str
        """
        self._stack_set_id = stack_set_id

    @property
    def deployment_targets(self):
        r"""Gets the deployment_targets of this DeleteStackInstanceRequestBody.

        :return: The deployment_targets of this DeleteStackInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkaos.v1.DeploymentTargets`
        """
        return self._deployment_targets

    @deployment_targets.setter
    def deployment_targets(self, deployment_targets):
        r"""Sets the deployment_targets of this DeleteStackInstanceRequestBody.

        :param deployment_targets: The deployment_targets of this DeleteStackInstanceRequestBody.
        :type deployment_targets: :class:`huaweicloudsdkaos.v1.DeploymentTargets`
        """
        self._deployment_targets = deployment_targets

    @property
    def operation_preferences(self):
        r"""Gets the operation_preferences of this DeleteStackInstanceRequestBody.

        :return: The operation_preferences of this DeleteStackInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkaos.v1.OperationPreferences`
        """
        return self._operation_preferences

    @operation_preferences.setter
    def operation_preferences(self, operation_preferences):
        r"""Sets the operation_preferences of this DeleteStackInstanceRequestBody.

        :param operation_preferences: The operation_preferences of this DeleteStackInstanceRequestBody.
        :type operation_preferences: :class:`huaweicloudsdkaos.v1.OperationPreferences`
        """
        self._operation_preferences = operation_preferences

    @property
    def call_identity(self):
        r"""Gets the call_identity of this DeleteStackInstanceRequestBody.

        仅支持资源栈集权限模式为SERVICE_MANAGED时指定该参数。用于指定用户是以组织管理账号还是成员账号中的服务委托管理员身份调用资源栈集。默认为SELF。 当资源栈集权限模式为SELF_MANAGED时，默认为SELF。 * 无论指定何种用户身份，涉及操作的资源栈集始终在组织管理账号名下。*   * `SELF` - 以组织管理账号身份调用。   * `DELEGATED_ADMIN` - 以服务委托管理员身份调用。用户的华为云账号必须在组织中已经被注册为”资源编排资源栈集服务“的委托管理员。

        :return: The call_identity of this DeleteStackInstanceRequestBody.
        :rtype: str
        """
        return self._call_identity

    @call_identity.setter
    def call_identity(self, call_identity):
        r"""Sets the call_identity of this DeleteStackInstanceRequestBody.

        仅支持资源栈集权限模式为SERVICE_MANAGED时指定该参数。用于指定用户是以组织管理账号还是成员账号中的服务委托管理员身份调用资源栈集。默认为SELF。 当资源栈集权限模式为SELF_MANAGED时，默认为SELF。 * 无论指定何种用户身份，涉及操作的资源栈集始终在组织管理账号名下。*   * `SELF` - 以组织管理账号身份调用。   * `DELEGATED_ADMIN` - 以服务委托管理员身份调用。用户的华为云账号必须在组织中已经被注册为”资源编排资源栈集服务“的委托管理员。

        :param call_identity: The call_identity of this DeleteStackInstanceRequestBody.
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
        if not isinstance(other, DeleteStackInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
