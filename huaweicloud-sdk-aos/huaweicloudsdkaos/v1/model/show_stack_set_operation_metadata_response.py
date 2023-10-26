# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStackSetOperationMetadataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_set_operation_id': 'str',
        'stack_set_id': 'str',
        'stack_set_name': 'str',
        'status': 'str',
        'status_message': 'str',
        'action': 'str',
        'administration_agency_name': 'str',
        'administration_agency_urn': 'str',
        'managed_agency_name': 'str',
        'deployment_targets': 'DeploymentTargets',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'stack_set_operation_id': 'stack_set_operation_id',
        'stack_set_id': 'stack_set_id',
        'stack_set_name': 'stack_set_name',
        'status': 'status',
        'status_message': 'status_message',
        'action': 'action',
        'administration_agency_name': 'administration_agency_name',
        'administration_agency_urn': 'administration_agency_urn',
        'managed_agency_name': 'managed_agency_name',
        'deployment_targets': 'deployment_targets',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, stack_set_operation_id=None, stack_set_id=None, stack_set_name=None, status=None, status_message=None, action=None, administration_agency_name=None, administration_agency_urn=None, managed_agency_name=None, deployment_targets=None, create_time=None, update_time=None):
        """ShowStackSetOperationMetadataResponse

        The model defined in huaweicloud sdk

        :param stack_set_operation_id: 资源栈集操作（operation）的唯一Id。  此Id由资源编排服务在生成资源栈集操作的时候生成，为UUID。
        :type stack_set_operation_id: str
        :param stack_set_id: 资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，在重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是又其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给与的stack_set_id和当前资源栈集的ID不一致，则返回400
        :type stack_set_id: str
        :param stack_set_name: 资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_set_name: str
        :param status: 资源栈集操作状态   * &#x60;QUEUE_IN_PROGRESS&#x60; - 正在排队   * &#x60;OPERATION_IN_PROGRESS&#x60; - 正在操作   * &#x60;OPERATION_COMPLETE&#x60; - 操作完成   * &#x60;OPERATION_FAILED&#x60; - 操作失败   * &#x60;STOP_IN_PROGRESS&#x60; - 正在停止   * &#x60;STOP_COMPLETE&#x60; - 停止完成   * &#x60;STOP_FAILED&#x60; - 停止失败
        :type status: str
        :param status_message: 资源栈集操作失败时会展示此次操作失败的原因，例如，资源栈实例部署或删除失败个数超过上限或资源栈集操作超时。  如果需要查看详细失败信息，可通过ListStackInstances API获取查看资源栈实例的status_message。
        :type status_message: str
        :param action: 用户当前的操作   * &#x60;CREATE_STACK_INSTANCES&#x60; - 创建资源栈实例   * &#x60;DELETE_STACK_INSTANCES&#x60; - 删除资源栈实例   * &#x60;DEPLOY_STACK_SET&#x60; - 部署资源栈集   * &#x60;DEPLOY_STACK_INSTANCES&#x60; - 部署资源栈实例
        :type action: str
        :param administration_agency_name: 管理委托名称  资源编排服务使用该委托获取成员账号委托给管理账号的权限  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用v5委托时给与administration_agency_urn，administration_agency_name只支持接收v3委托名称，若给与了v5委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)
        :type administration_agency_name: str
        :param administration_agency_urn: 管理委托URN  资源编排服务使用该委托获取成员账号委托给管理账号的权限  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用v5委托时给与administration_agency_urn，administration_agency_name只支持接收普通委托名称，若给与了v5委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。
        :type administration_agency_urn: str
        :param managed_agency_name: 被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)
        :type managed_agency_name: str
        :param deployment_targets: 
        :type deployment_targets: :class:`huaweicloudsdkaos.v1.DeploymentTargets`
        :param create_time: 资源栈集操作的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type create_time: str
        :param update_time: 资源栈集操作的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type update_time: str
        """
        
        super(ShowStackSetOperationMetadataResponse, self).__init__()

        self._stack_set_operation_id = None
        self._stack_set_id = None
        self._stack_set_name = None
        self._status = None
        self._status_message = None
        self._action = None
        self._administration_agency_name = None
        self._administration_agency_urn = None
        self._managed_agency_name = None
        self._deployment_targets = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if stack_set_operation_id is not None:
            self.stack_set_operation_id = stack_set_operation_id
        if stack_set_id is not None:
            self.stack_set_id = stack_set_id
        self.stack_set_name = stack_set_name
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if action is not None:
            self.action = action
        if administration_agency_name is not None:
            self.administration_agency_name = administration_agency_name
        if administration_agency_urn is not None:
            self.administration_agency_urn = administration_agency_urn
        if managed_agency_name is not None:
            self.managed_agency_name = managed_agency_name
        self.deployment_targets = deployment_targets
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def stack_set_operation_id(self):
        """Gets the stack_set_operation_id of this ShowStackSetOperationMetadataResponse.

        资源栈集操作（operation）的唯一Id。  此Id由资源编排服务在生成资源栈集操作的时候生成，为UUID。

        :return: The stack_set_operation_id of this ShowStackSetOperationMetadataResponse.
        :rtype: str
        """
        return self._stack_set_operation_id

    @stack_set_operation_id.setter
    def stack_set_operation_id(self, stack_set_operation_id):
        """Sets the stack_set_operation_id of this ShowStackSetOperationMetadataResponse.

        资源栈集操作（operation）的唯一Id。  此Id由资源编排服务在生成资源栈集操作的时候生成，为UUID。

        :param stack_set_operation_id: The stack_set_operation_id of this ShowStackSetOperationMetadataResponse.
        :type stack_set_operation_id: str
        """
        self._stack_set_operation_id = stack_set_operation_id

    @property
    def stack_set_id(self):
        """Gets the stack_set_id of this ShowStackSetOperationMetadataResponse.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，在重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是又其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给与的stack_set_id和当前资源栈集的ID不一致，则返回400

        :return: The stack_set_id of this ShowStackSetOperationMetadataResponse.
        :rtype: str
        """
        return self._stack_set_id

    @stack_set_id.setter
    def stack_set_id(self, stack_set_id):
        """Sets the stack_set_id of this ShowStackSetOperationMetadataResponse.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，在重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是又其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给与的stack_set_id和当前资源栈集的ID不一致，则返回400

        :param stack_set_id: The stack_set_id of this ShowStackSetOperationMetadataResponse.
        :type stack_set_id: str
        """
        self._stack_set_id = stack_set_id

    @property
    def stack_set_name(self):
        """Gets the stack_set_name of this ShowStackSetOperationMetadataResponse.

        资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_set_name of this ShowStackSetOperationMetadataResponse.
        :rtype: str
        """
        return self._stack_set_name

    @stack_set_name.setter
    def stack_set_name(self, stack_set_name):
        """Sets the stack_set_name of this ShowStackSetOperationMetadataResponse.

        资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_set_name: The stack_set_name of this ShowStackSetOperationMetadataResponse.
        :type stack_set_name: str
        """
        self._stack_set_name = stack_set_name

    @property
    def status(self):
        """Gets the status of this ShowStackSetOperationMetadataResponse.

        资源栈集操作状态   * `QUEUE_IN_PROGRESS` - 正在排队   * `OPERATION_IN_PROGRESS` - 正在操作   * `OPERATION_COMPLETE` - 操作完成   * `OPERATION_FAILED` - 操作失败   * `STOP_IN_PROGRESS` - 正在停止   * `STOP_COMPLETE` - 停止完成   * `STOP_FAILED` - 停止失败

        :return: The status of this ShowStackSetOperationMetadataResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowStackSetOperationMetadataResponse.

        资源栈集操作状态   * `QUEUE_IN_PROGRESS` - 正在排队   * `OPERATION_IN_PROGRESS` - 正在操作   * `OPERATION_COMPLETE` - 操作完成   * `OPERATION_FAILED` - 操作失败   * `STOP_IN_PROGRESS` - 正在停止   * `STOP_COMPLETE` - 停止完成   * `STOP_FAILED` - 停止失败

        :param status: The status of this ShowStackSetOperationMetadataResponse.
        :type status: str
        """
        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this ShowStackSetOperationMetadataResponse.

        资源栈集操作失败时会展示此次操作失败的原因，例如，资源栈实例部署或删除失败个数超过上限或资源栈集操作超时。  如果需要查看详细失败信息，可通过ListStackInstances API获取查看资源栈实例的status_message。

        :return: The status_message of this ShowStackSetOperationMetadataResponse.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this ShowStackSetOperationMetadataResponse.

        资源栈集操作失败时会展示此次操作失败的原因，例如，资源栈实例部署或删除失败个数超过上限或资源栈集操作超时。  如果需要查看详细失败信息，可通过ListStackInstances API获取查看资源栈实例的status_message。

        :param status_message: The status_message of this ShowStackSetOperationMetadataResponse.
        :type status_message: str
        """
        self._status_message = status_message

    @property
    def action(self):
        """Gets the action of this ShowStackSetOperationMetadataResponse.

        用户当前的操作   * `CREATE_STACK_INSTANCES` - 创建资源栈实例   * `DELETE_STACK_INSTANCES` - 删除资源栈实例   * `DEPLOY_STACK_SET` - 部署资源栈集   * `DEPLOY_STACK_INSTANCES` - 部署资源栈实例

        :return: The action of this ShowStackSetOperationMetadataResponse.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ShowStackSetOperationMetadataResponse.

        用户当前的操作   * `CREATE_STACK_INSTANCES` - 创建资源栈实例   * `DELETE_STACK_INSTANCES` - 删除资源栈实例   * `DEPLOY_STACK_SET` - 部署资源栈集   * `DEPLOY_STACK_INSTANCES` - 部署资源栈实例

        :param action: The action of this ShowStackSetOperationMetadataResponse.
        :type action: str
        """
        self._action = action

    @property
    def administration_agency_name(self):
        """Gets the administration_agency_name of this ShowStackSetOperationMetadataResponse.

        管理委托名称  资源编排服务使用该委托获取成员账号委托给管理账号的权限  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用v5委托时给与administration_agency_urn，administration_agency_name只支持接收v3委托名称，若给与了v5委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)

        :return: The administration_agency_name of this ShowStackSetOperationMetadataResponse.
        :rtype: str
        """
        return self._administration_agency_name

    @administration_agency_name.setter
    def administration_agency_name(self, administration_agency_name):
        """Sets the administration_agency_name of this ShowStackSetOperationMetadataResponse.

        管理委托名称  资源编排服务使用该委托获取成员账号委托给管理账号的权限  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用v5委托时给与administration_agency_urn，administration_agency_name只支持接收v3委托名称，若给与了v5委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)

        :param administration_agency_name: The administration_agency_name of this ShowStackSetOperationMetadataResponse.
        :type administration_agency_name: str
        """
        self._administration_agency_name = administration_agency_name

    @property
    def administration_agency_urn(self):
        """Gets the administration_agency_urn of this ShowStackSetOperationMetadataResponse.

        管理委托URN  资源编排服务使用该委托获取成员账号委托给管理账号的权限  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用v5委托时给与administration_agency_urn，administration_agency_name只支持接收普通委托名称，若给与了v5委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。

        :return: The administration_agency_urn of this ShowStackSetOperationMetadataResponse.
        :rtype: str
        """
        return self._administration_agency_urn

    @administration_agency_urn.setter
    def administration_agency_urn(self, administration_agency_urn):
        """Sets the administration_agency_urn of this ShowStackSetOperationMetadataResponse.

        管理委托URN  资源编排服务使用该委托获取成员账号委托给管理账号的权限  当用户定义SELF_MANAGED权限类型时，administration_agency_name和administration_agency_urn 必须有且只有一个存在。  推荐用户在使用v5委托时给与administration_agency_urn，administration_agency_name只支持接收普通委托名称，若给与了v5委托名称，则会在部署模板时失败。  当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400。

        :param administration_agency_urn: The administration_agency_urn of this ShowStackSetOperationMetadataResponse.
        :type administration_agency_urn: str
        """
        self._administration_agency_urn = administration_agency_urn

    @property
    def managed_agency_name(self):
        """Gets the managed_agency_name of this ShowStackSetOperationMetadataResponse.

        被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)

        :return: The managed_agency_name of this ShowStackSetOperationMetadataResponse.
        :rtype: str
        """
        return self._managed_agency_name

    @managed_agency_name.setter
    def managed_agency_name(self, managed_agency_name):
        """Sets the managed_agency_name of this ShowStackSetOperationMetadataResponse.

        被管理的委托名称。  资源编排服务会使用该委托获取实际部署资源所需要的权限  不同成员账号委托给管理账号的委托名称需要保持一致。暂不支持根据不同provider定义不同委托权限  当用户定义SELF_MANAGED权限类型时，必须指定该参数。当用户使用SERVICE_MANAGED权限类型时，指定该参数将报错400  [创建委托及授权方式](https://support.huaweicloud.com/usermanual-iam/iam_06_0002.html)

        :param managed_agency_name: The managed_agency_name of this ShowStackSetOperationMetadataResponse.
        :type managed_agency_name: str
        """
        self._managed_agency_name = managed_agency_name

    @property
    def deployment_targets(self):
        """Gets the deployment_targets of this ShowStackSetOperationMetadataResponse.

        :return: The deployment_targets of this ShowStackSetOperationMetadataResponse.
        :rtype: :class:`huaweicloudsdkaos.v1.DeploymentTargets`
        """
        return self._deployment_targets

    @deployment_targets.setter
    def deployment_targets(self, deployment_targets):
        """Sets the deployment_targets of this ShowStackSetOperationMetadataResponse.

        :param deployment_targets: The deployment_targets of this ShowStackSetOperationMetadataResponse.
        :type deployment_targets: :class:`huaweicloudsdkaos.v1.DeploymentTargets`
        """
        self._deployment_targets = deployment_targets

    @property
    def create_time(self):
        """Gets the create_time of this ShowStackSetOperationMetadataResponse.

        资源栈集操作的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The create_time of this ShowStackSetOperationMetadataResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowStackSetOperationMetadataResponse.

        资源栈集操作的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param create_time: The create_time of this ShowStackSetOperationMetadataResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowStackSetOperationMetadataResponse.

        资源栈集操作的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The update_time of this ShowStackSetOperationMetadataResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowStackSetOperationMetadataResponse.

        资源栈集操作的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param update_time: The update_time of this ShowStackSetOperationMetadataResponse.
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
        if not isinstance(other, ShowStackSetOperationMetadataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
