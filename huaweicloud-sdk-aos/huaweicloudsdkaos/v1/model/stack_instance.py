# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StackInstance:

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
        'status': 'str',
        'status_message': 'str',
        'stack_id': 'str',
        'stack_name': 'str',
        'stack_domain_id': 'str',
        'latest_stack_set_operation_id': 'str',
        'region': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'stack_set_id': 'stack_set_id',
        'stack_set_name': 'stack_set_name',
        'status': 'status',
        'status_message': 'status_message',
        'stack_id': 'stack_id',
        'stack_name': 'stack_name',
        'stack_domain_id': 'stack_domain_id',
        'latest_stack_set_operation_id': 'latest_stack_set_operation_id',
        'region': 'region',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, stack_set_id=None, stack_set_name=None, status=None, status_message=None, stack_id=None, stack_name=None, stack_domain_id=None, latest_stack_set_operation_id=None, region=None, create_time=None, update_time=None):
        """StackInstance

        The model defined in huaweicloud sdk

        :param stack_set_id: 资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，在重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是又其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400
        :type stack_set_id: str
        :param stack_set_name: 资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_set_name: str
        :param status: 资源栈实例的状态  * &#x60;WAIT_IN_PROGRESS&#x60; - 资源栈实例等待操作中 * &#x60;CANCEL_COMPLETE&#x60; - 资源栈实例操作取消完成 * &#x60;OPERATION_IN_PROGRESS&#x60; - 资源栈实例操作中 * &#x60;OPERATION_FAILED&#x60; - 资源栈实例操作失败 * &#x60;INOPERABLE&#x60; - 资源栈实例不可操作 * &#x60;OPERATION_COMPLETE&#x60; - 资源栈实例操作完成
        :type status: str
        :param status_message: 在资源栈实例状态为&#x60;INOPERABLE&#x60;或&#x60;OPERATION_FAILED&#x60;时，会显示简要的错误信息总结以供debug
        :type status_message: str
        :param stack_id: 资源栈（stack）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给予的stack_id和当前资源栈的ID不一致，则返回400
        :type stack_id: str
        :param stack_name: 资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_name: str
        :param stack_domain_id: 资源栈实例所关联的资源栈所在的租户ID
        :type stack_domain_id: str
        :param latest_stack_set_operation_id: 最新一次部署该资源栈实例的资源栈集操作ID。  此ID由资源编排服务在生成资源栈集操作的时候生成，为UUID。
        :type latest_stack_set_operation_id: str
        :param region: 资源栈实例所关联的资源栈所在的区域
        :type region: str
        :param create_time: 资源栈实例的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type create_time: str
        :param update_time: 资源栈实例的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type update_time: str
        """
        
        

        self._stack_set_id = None
        self._stack_set_name = None
        self._status = None
        self._status_message = None
        self._stack_id = None
        self._stack_name = None
        self._stack_domain_id = None
        self._latest_stack_set_operation_id = None
        self._region = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if stack_set_id is not None:
            self.stack_set_id = stack_set_id
        self.stack_set_name = stack_set_name
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if stack_id is not None:
            self.stack_id = stack_id
        if stack_name is not None:
            self.stack_name = stack_name
        if stack_domain_id is not None:
            self.stack_domain_id = stack_domain_id
        if latest_stack_set_operation_id is not None:
            self.latest_stack_set_operation_id = latest_stack_set_operation_id
        if region is not None:
            self.region = region
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def stack_set_id(self):
        """Gets the stack_set_id of this StackInstance.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，在重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是又其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :return: The stack_set_id of this StackInstance.
        :rtype: str
        """
        return self._stack_set_id

    @stack_set_id.setter
    def stack_set_id(self, stack_set_id):
        """Sets the stack_set_id of this StackInstance.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，在重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是又其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :param stack_set_id: The stack_set_id of this StackInstance.
        :type stack_set_id: str
        """
        self._stack_set_id = stack_set_id

    @property
    def stack_set_name(self):
        """Gets the stack_set_name of this StackInstance.

        资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_set_name of this StackInstance.
        :rtype: str
        """
        return self._stack_set_name

    @stack_set_name.setter
    def stack_set_name(self, stack_set_name):
        """Sets the stack_set_name of this StackInstance.

        资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_set_name: The stack_set_name of this StackInstance.
        :type stack_set_name: str
        """
        self._stack_set_name = stack_set_name

    @property
    def status(self):
        """Gets the status of this StackInstance.

        资源栈实例的状态  * `WAIT_IN_PROGRESS` - 资源栈实例等待操作中 * `CANCEL_COMPLETE` - 资源栈实例操作取消完成 * `OPERATION_IN_PROGRESS` - 资源栈实例操作中 * `OPERATION_FAILED` - 资源栈实例操作失败 * `INOPERABLE` - 资源栈实例不可操作 * `OPERATION_COMPLETE` - 资源栈实例操作完成

        :return: The status of this StackInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StackInstance.

        资源栈实例的状态  * `WAIT_IN_PROGRESS` - 资源栈实例等待操作中 * `CANCEL_COMPLETE` - 资源栈实例操作取消完成 * `OPERATION_IN_PROGRESS` - 资源栈实例操作中 * `OPERATION_FAILED` - 资源栈实例操作失败 * `INOPERABLE` - 资源栈实例不可操作 * `OPERATION_COMPLETE` - 资源栈实例操作完成

        :param status: The status of this StackInstance.
        :type status: str
        """
        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this StackInstance.

        在资源栈实例状态为`INOPERABLE`或`OPERATION_FAILED`时，会显示简要的错误信息总结以供debug

        :return: The status_message of this StackInstance.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this StackInstance.

        在资源栈实例状态为`INOPERABLE`或`OPERATION_FAILED`时，会显示简要的错误信息总结以供debug

        :param status_message: The status_message of this StackInstance.
        :type status_message: str
        """
        self._status_message = status_message

    @property
    def stack_id(self):
        """Gets the stack_id of this StackInstance.

        资源栈（stack）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给予的stack_id和当前资源栈的ID不一致，则返回400

        :return: The stack_id of this StackInstance.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this StackInstance.

        资源栈（stack）的唯一ID。  此ID由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给予的stack_id和当前资源栈的ID不一致，则返回400

        :param stack_id: The stack_id of this StackInstance.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def stack_name(self):
        """Gets the stack_name of this StackInstance.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_name of this StackInstance.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this StackInstance.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_name: The stack_name of this StackInstance.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def stack_domain_id(self):
        """Gets the stack_domain_id of this StackInstance.

        资源栈实例所关联的资源栈所在的租户ID

        :return: The stack_domain_id of this StackInstance.
        :rtype: str
        """
        return self._stack_domain_id

    @stack_domain_id.setter
    def stack_domain_id(self, stack_domain_id):
        """Sets the stack_domain_id of this StackInstance.

        资源栈实例所关联的资源栈所在的租户ID

        :param stack_domain_id: The stack_domain_id of this StackInstance.
        :type stack_domain_id: str
        """
        self._stack_domain_id = stack_domain_id

    @property
    def latest_stack_set_operation_id(self):
        """Gets the latest_stack_set_operation_id of this StackInstance.

        最新一次部署该资源栈实例的资源栈集操作ID。  此ID由资源编排服务在生成资源栈集操作的时候生成，为UUID。

        :return: The latest_stack_set_operation_id of this StackInstance.
        :rtype: str
        """
        return self._latest_stack_set_operation_id

    @latest_stack_set_operation_id.setter
    def latest_stack_set_operation_id(self, latest_stack_set_operation_id):
        """Sets the latest_stack_set_operation_id of this StackInstance.

        最新一次部署该资源栈实例的资源栈集操作ID。  此ID由资源编排服务在生成资源栈集操作的时候生成，为UUID。

        :param latest_stack_set_operation_id: The latest_stack_set_operation_id of this StackInstance.
        :type latest_stack_set_operation_id: str
        """
        self._latest_stack_set_operation_id = latest_stack_set_operation_id

    @property
    def region(self):
        """Gets the region of this StackInstance.

        资源栈实例所关联的资源栈所在的区域

        :return: The region of this StackInstance.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this StackInstance.

        资源栈实例所关联的资源栈所在的区域

        :param region: The region of this StackInstance.
        :type region: str
        """
        self._region = region

    @property
    def create_time(self):
        """Gets the create_time of this StackInstance.

        资源栈实例的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The create_time of this StackInstance.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this StackInstance.

        资源栈实例的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param create_time: The create_time of this StackInstance.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this StackInstance.

        资源栈实例的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The update_time of this StackInstance.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this StackInstance.

        资源栈实例的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param update_time: The update_time of this StackInstance.
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
        if not isinstance(other, StackInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
