# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StackSetOperation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_id': 'str',
        'stack_set_id': 'str',
        'stack_set_name': 'str',
        'action': 'str',
        'status': 'str',
        'status_message': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'operation_id': 'operation_id',
        'stack_set_id': 'stack_set_id',
        'stack_set_name': 'stack_set_name',
        'action': 'action',
        'status': 'status',
        'status_message': 'status_message',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, operation_id=None, stack_set_id=None, stack_set_name=None, action=None, status=None, status_message=None, create_time=None, update_time=None):
        r"""StackSetOperation

        The model defined in huaweicloud sdk

        :param operation_id: 资源栈集操作Id。  此ID由资源编排服务在生成资源栈集操作的时候生成，为UUID。
        :type operation_id: str
        :param stack_set_id: 资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400
        :type stack_set_id: str
        :param stack_set_name: 资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_set_name: str
        :param action: 用户当前的操作   * &#x60;CREATE_STACK_INSTANCES&#x60; - 创建资源栈实例   * &#x60;DELETE_STACK_INSTANCES&#x60; - 删除资源栈实例   * &#x60;DEPLOY_STACK_SET&#x60; - 部署资源栈集   * &#x60;DEPLOY_STACK_INSTANCES&#x60; - 部署资源栈实例   * &#x60;UPDATE_STACK_INSTANCES&#x60; - 更新资源栈实例
        :type action: str
        :param status: 资源栈集操作状态   * &#x60;QUEUE_IN_PROGRESS&#x60; - 正在排队   * &#x60;OPERATION_IN_PROGRESS&#x60; - 正在操作   * &#x60;OPERATION_COMPLETE&#x60; - 操作完成   * &#x60;OPERATION_FAILED&#x60; - 操作失败   * &#x60;STOP_IN_PROGRESS&#x60; - 正在停止   * &#x60;STOP_COMPLETE&#x60; - 停止完成   * &#x60;STOP_FAILED&#x60; - 停止失败
        :type status: str
        :param status_message: 资源栈集操作失败时会展示此次操作失败的原因，例如，资源栈实例部署或删除失败个数超过上限或资源栈集操作超时。  如果需要查看详细失败信息，可通过ListStackInstances API获取查看资源栈实例的status_message。
        :type status_message: str
        :param create_time: 资源栈集操作的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type create_time: str
        :param update_time: 资源栈集操作的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type update_time: str
        """
        
        

        self._operation_id = None
        self._stack_set_id = None
        self._stack_set_name = None
        self._action = None
        self._status = None
        self._status_message = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if operation_id is not None:
            self.operation_id = operation_id
        if stack_set_id is not None:
            self.stack_set_id = stack_set_id
        self.stack_set_name = stack_set_name
        if action is not None:
            self.action = action
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def operation_id(self):
        r"""Gets the operation_id of this StackSetOperation.

        资源栈集操作Id。  此ID由资源编排服务在生成资源栈集操作的时候生成，为UUID。

        :return: The operation_id of this StackSetOperation.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        r"""Sets the operation_id of this StackSetOperation.

        资源栈集操作Id。  此ID由资源编排服务在生成资源栈集操作的时候生成，为UUID。

        :param operation_id: The operation_id of this StackSetOperation.
        :type operation_id: str
        """
        self._operation_id = operation_id

    @property
    def stack_set_id(self):
        r"""Gets the stack_set_id of this StackSetOperation.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :return: The stack_set_id of this StackSetOperation.
        :rtype: str
        """
        return self._stack_set_id

    @stack_set_id.setter
    def stack_set_id(self, stack_set_id):
        r"""Sets the stack_set_id of this StackSetOperation.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :param stack_set_id: The stack_set_id of this StackSetOperation.
        :type stack_set_id: str
        """
        self._stack_set_id = stack_set_id

    @property
    def stack_set_name(self):
        r"""Gets the stack_set_name of this StackSetOperation.

        资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_set_name of this StackSetOperation.
        :rtype: str
        """
        return self._stack_set_name

    @stack_set_name.setter
    def stack_set_name(self, stack_set_name):
        r"""Sets the stack_set_name of this StackSetOperation.

        资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_set_name: The stack_set_name of this StackSetOperation.
        :type stack_set_name: str
        """
        self._stack_set_name = stack_set_name

    @property
    def action(self):
        r"""Gets the action of this StackSetOperation.

        用户当前的操作   * `CREATE_STACK_INSTANCES` - 创建资源栈实例   * `DELETE_STACK_INSTANCES` - 删除资源栈实例   * `DEPLOY_STACK_SET` - 部署资源栈集   * `DEPLOY_STACK_INSTANCES` - 部署资源栈实例   * `UPDATE_STACK_INSTANCES` - 更新资源栈实例

        :return: The action of this StackSetOperation.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this StackSetOperation.

        用户当前的操作   * `CREATE_STACK_INSTANCES` - 创建资源栈实例   * `DELETE_STACK_INSTANCES` - 删除资源栈实例   * `DEPLOY_STACK_SET` - 部署资源栈集   * `DEPLOY_STACK_INSTANCES` - 部署资源栈实例   * `UPDATE_STACK_INSTANCES` - 更新资源栈实例

        :param action: The action of this StackSetOperation.
        :type action: str
        """
        self._action = action

    @property
    def status(self):
        r"""Gets the status of this StackSetOperation.

        资源栈集操作状态   * `QUEUE_IN_PROGRESS` - 正在排队   * `OPERATION_IN_PROGRESS` - 正在操作   * `OPERATION_COMPLETE` - 操作完成   * `OPERATION_FAILED` - 操作失败   * `STOP_IN_PROGRESS` - 正在停止   * `STOP_COMPLETE` - 停止完成   * `STOP_FAILED` - 停止失败

        :return: The status of this StackSetOperation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StackSetOperation.

        资源栈集操作状态   * `QUEUE_IN_PROGRESS` - 正在排队   * `OPERATION_IN_PROGRESS` - 正在操作   * `OPERATION_COMPLETE` - 操作完成   * `OPERATION_FAILED` - 操作失败   * `STOP_IN_PROGRESS` - 正在停止   * `STOP_COMPLETE` - 停止完成   * `STOP_FAILED` - 停止失败

        :param status: The status of this StackSetOperation.
        :type status: str
        """
        self._status = status

    @property
    def status_message(self):
        r"""Gets the status_message of this StackSetOperation.

        资源栈集操作失败时会展示此次操作失败的原因，例如，资源栈实例部署或删除失败个数超过上限或资源栈集操作超时。  如果需要查看详细失败信息，可通过ListStackInstances API获取查看资源栈实例的status_message。

        :return: The status_message of this StackSetOperation.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        r"""Sets the status_message of this StackSetOperation.

        资源栈集操作失败时会展示此次操作失败的原因，例如，资源栈实例部署或删除失败个数超过上限或资源栈集操作超时。  如果需要查看详细失败信息，可通过ListStackInstances API获取查看资源栈实例的status_message。

        :param status_message: The status_message of this StackSetOperation.
        :type status_message: str
        """
        self._status_message = status_message

    @property
    def create_time(self):
        r"""Gets the create_time of this StackSetOperation.

        资源栈集操作的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The create_time of this StackSetOperation.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this StackSetOperation.

        资源栈集操作的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param create_time: The create_time of this StackSetOperation.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this StackSetOperation.

        资源栈集操作的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The update_time of this StackSetOperation.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this StackSetOperation.

        资源栈集操作的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param update_time: The update_time of this StackSetOperation.
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
        if not isinstance(other, StackSetOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
