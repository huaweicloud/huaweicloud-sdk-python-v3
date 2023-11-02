# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Stack:

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
        'description': 'str',
        'stack_id': 'str',
        'status': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'status_message': 'str'
    }

    attribute_map = {
        'stack_name': 'stack_name',
        'description': 'description',
        'stack_id': 'stack_id',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'status_message': 'status_message'
    }

    def __init__(self, stack_name=None, description=None, stack_id=None, status=None, create_time=None, update_time=None, status_message=None):
        """Stack

        The model defined in huaweicloud sdk

        :param stack_name: 资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_name: str
        :param description: 资源栈的描述。可用于客户识别自己的资源栈。
        :type description: str
        :param stack_id: 资源栈（stack）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400
        :type stack_id: str
        :param status: 资源栈的状态    * &#x60;CREATION_COMPLETE&#x60; - 生成空资源栈完成，并没有任何部署    * &#x60;DEPLOYMENT_IN_PROGRESS&#x60; - 正在部署，请等待    * &#x60;DEPLOYMENT_FAILED&#x60; - 部署失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情    * &#x60;DEPLOYMENT_COMPLETE&#x60; - 部署完成    * &#x60;ROLLBACK_IN_PROGRESS&#x60; - 部署失败，正在回滚，请等待    * &#x60;ROLLBACK_FAILED&#x60; - 回滚失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情    * &#x60;ROLLBACK_COMPLETE&#x60; - 回滚完成    * &#x60;DELETION_IN_PROGRESS&#x60; - 正在删除，请等待    * &#x60;DELETION_FAILED&#x60; - 删除失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情
        :type status: str
        :param create_time: 资源栈的生成时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type create_time: str
        :param update_time: 资源栈的更新时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type update_time: str
        :param status_message: 在失败的时候（资源栈状态以FAILED结尾）会显示简要的错误信息总结以供debug
        :type status_message: str
        """
        
        

        self._stack_name = None
        self._description = None
        self._stack_id = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._status_message = None
        self.discriminator = None

        self.stack_name = stack_name
        if description is not None:
            self.description = description
        if stack_id is not None:
            self.stack_id = stack_id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if status_message is not None:
            self.status_message = status_message

    @property
    def stack_name(self):
        """Gets the stack_name of this Stack.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_name of this Stack.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this Stack.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_name: The stack_name of this Stack.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def description(self):
        """Gets the description of this Stack.

        资源栈的描述。可用于客户识别自己的资源栈。

        :return: The description of this Stack.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Stack.

        资源栈的描述。可用于客户识别自己的资源栈。

        :param description: The description of this Stack.
        :type description: str
        """
        self._description = description

    @property
    def stack_id(self):
        """Gets the stack_id of this Stack.

        资源栈（stack）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400

        :return: The stack_id of this Stack.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this Stack.

        资源栈（stack）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400

        :param stack_id: The stack_id of this Stack.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def status(self):
        """Gets the status of this Stack.

        资源栈的状态    * `CREATION_COMPLETE` - 生成空资源栈完成，并没有任何部署    * `DEPLOYMENT_IN_PROGRESS` - 正在部署，请等待    * `DEPLOYMENT_FAILED` - 部署失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情    * `DEPLOYMENT_COMPLETE` - 部署完成    * `ROLLBACK_IN_PROGRESS` - 部署失败，正在回滚，请等待    * `ROLLBACK_FAILED` - 回滚失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情    * `ROLLBACK_COMPLETE` - 回滚完成    * `DELETION_IN_PROGRESS` - 正在删除，请等待    * `DELETION_FAILED` - 删除失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情

        :return: The status of this Stack.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Stack.

        资源栈的状态    * `CREATION_COMPLETE` - 生成空资源栈完成，并没有任何部署    * `DEPLOYMENT_IN_PROGRESS` - 正在部署，请等待    * `DEPLOYMENT_FAILED` - 部署失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情    * `DEPLOYMENT_COMPLETE` - 部署完成    * `ROLLBACK_IN_PROGRESS` - 部署失败，正在回滚，请等待    * `ROLLBACK_FAILED` - 回滚失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情    * `ROLLBACK_COMPLETE` - 回滚完成    * `DELETION_IN_PROGRESS` - 正在删除，请等待    * `DELETION_FAILED` - 删除失败。请从status_message获取错误信息汇总，或者调用ListStackEvents获得事件详情

        :param status: The status of this Stack.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this Stack.

        资源栈的生成时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The create_time of this Stack.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Stack.

        资源栈的生成时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param create_time: The create_time of this Stack.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Stack.

        资源栈的更新时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The update_time of this Stack.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Stack.

        资源栈的更新时间，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param update_time: The update_time of this Stack.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def status_message(self):
        """Gets the status_message of this Stack.

        在失败的时候（资源栈状态以FAILED结尾）会显示简要的错误信息总结以供debug

        :return: The status_message of this Stack.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this Stack.

        在失败的时候（资源栈状态以FAILED结尾）会显示简要的错误信息总结以供debug

        :param status_message: The status_message of this Stack.
        :type status_message: str
        """
        self._status_message = status_message

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
        if not isinstance(other, Stack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
