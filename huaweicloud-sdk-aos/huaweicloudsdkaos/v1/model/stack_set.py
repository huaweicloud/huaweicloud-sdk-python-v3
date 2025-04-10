# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StackSet:

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
        'permission_model': 'str',
        'status': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'stack_set_id': 'stack_set_id',
        'stack_set_name': 'stack_set_name',
        'stack_set_description': 'stack_set_description',
        'permission_model': 'permission_model',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, stack_set_id=None, stack_set_name=None, stack_set_description=None, permission_model=None, status=None, create_time=None, update_time=None):
        r"""StackSet

        The model defined in huaweicloud sdk

        :param stack_set_id: 资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400
        :type stack_set_id: str
        :param stack_set_name: 资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_set_name: str
        :param stack_set_description: 资源栈集的描述。可用于客户识别自己的资源栈集。
        :type stack_set_description: str
        :param permission_model: 权限模型，定义了RFS操作资源栈集时所需委托的创建方式，枚举值，默认为SELF_MANAGED。用户可以使用创建资源栈集（CreateStackSet）API 指定该参数。该参数暂不支持更新。用户如果想要更新权限模型，可以通过先删除再创建同名资源栈集实现。   * &#x60;SELF_MANAGED&#x60; - 自我管理，基于部署需求，用户需要提前手动创建委托，既包含管理账号授权给RFS的委托，也包含成员账号授权给管理账号的委托。如果委托不存在或权限不足，创建资源栈集不会失败，创建资源栈实例时才会报错。   * &#x60;SERVICE_MANAGED&#x60; - 服务管理，基于Organization服务，RFS会自动创建部署Organization 成员账号时所需的全部 IAM 委托。用户需要提前在Organization可信服务列表中将”资源编排资源栈集服务“启用，且只有Organization的管理账号或”资源编排资源栈集服务“的委托管理员，才允许指定SERVICE_MANAGED创建资源栈集，否则会报错。
        :type permission_model: str
        :param status: 资源栈集的状态     * &#x60;IDLE&#x60; - 资源栈集空闲 * &#x60;OPERATION_IN_PROGRESS&#x60; - 资源栈集操作中 * &#x60;DEACTIVATED&#x60; - 资源栈集禁用
        :type status: str
        :param create_time: 资源栈集的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type create_time: str
        :param update_time: 资源栈集的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。
        :type update_time: str
        """
        
        

        self._stack_set_id = None
        self._stack_set_name = None
        self._stack_set_description = None
        self._permission_model = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if stack_set_id is not None:
            self.stack_set_id = stack_set_id
        self.stack_set_name = stack_set_name
        if stack_set_description is not None:
            self.stack_set_description = stack_set_description
        if permission_model is not None:
            self.permission_model = permission_model
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def stack_set_id(self):
        r"""Gets the stack_set_id of this StackSet.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :return: The stack_set_id of this StackSet.
        :rtype: str
        """
        return self._stack_set_id

    @stack_set_id.setter
    def stack_set_id(self, stack_set_id):
        r"""Sets the stack_set_id of this StackSet.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我以为的那个，而不是被其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :param stack_set_id: The stack_set_id of this StackSet.
        :type stack_set_id: str
        """
        self._stack_set_id = stack_set_id

    @property
    def stack_set_name(self):
        r"""Gets the stack_set_name of this StackSet.

        资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_set_name of this StackSet.
        :rtype: str
        """
        return self._stack_set_name

    @stack_set_name.setter
    def stack_set_name(self, stack_set_name):
        r"""Sets the stack_set_name of this StackSet.

        资源栈集（stack_set）的名字。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_set_name: The stack_set_name of this StackSet.
        :type stack_set_name: str
        """
        self._stack_set_name = stack_set_name

    @property
    def stack_set_description(self):
        r"""Gets the stack_set_description of this StackSet.

        资源栈集的描述。可用于客户识别自己的资源栈集。

        :return: The stack_set_description of this StackSet.
        :rtype: str
        """
        return self._stack_set_description

    @stack_set_description.setter
    def stack_set_description(self, stack_set_description):
        r"""Sets the stack_set_description of this StackSet.

        资源栈集的描述。可用于客户识别自己的资源栈集。

        :param stack_set_description: The stack_set_description of this StackSet.
        :type stack_set_description: str
        """
        self._stack_set_description = stack_set_description

    @property
    def permission_model(self):
        r"""Gets the permission_model of this StackSet.

        权限模型，定义了RFS操作资源栈集时所需委托的创建方式，枚举值，默认为SELF_MANAGED。用户可以使用创建资源栈集（CreateStackSet）API 指定该参数。该参数暂不支持更新。用户如果想要更新权限模型，可以通过先删除再创建同名资源栈集实现。   * `SELF_MANAGED` - 自我管理，基于部署需求，用户需要提前手动创建委托，既包含管理账号授权给RFS的委托，也包含成员账号授权给管理账号的委托。如果委托不存在或权限不足，创建资源栈集不会失败，创建资源栈实例时才会报错。   * `SERVICE_MANAGED` - 服务管理，基于Organization服务，RFS会自动创建部署Organization 成员账号时所需的全部 IAM 委托。用户需要提前在Organization可信服务列表中将”资源编排资源栈集服务“启用，且只有Organization的管理账号或”资源编排资源栈集服务“的委托管理员，才允许指定SERVICE_MANAGED创建资源栈集，否则会报错。

        :return: The permission_model of this StackSet.
        :rtype: str
        """
        return self._permission_model

    @permission_model.setter
    def permission_model(self, permission_model):
        r"""Sets the permission_model of this StackSet.

        权限模型，定义了RFS操作资源栈集时所需委托的创建方式，枚举值，默认为SELF_MANAGED。用户可以使用创建资源栈集（CreateStackSet）API 指定该参数。该参数暂不支持更新。用户如果想要更新权限模型，可以通过先删除再创建同名资源栈集实现。   * `SELF_MANAGED` - 自我管理，基于部署需求，用户需要提前手动创建委托，既包含管理账号授权给RFS的委托，也包含成员账号授权给管理账号的委托。如果委托不存在或权限不足，创建资源栈集不会失败，创建资源栈实例时才会报错。   * `SERVICE_MANAGED` - 服务管理，基于Organization服务，RFS会自动创建部署Organization 成员账号时所需的全部 IAM 委托。用户需要提前在Organization可信服务列表中将”资源编排资源栈集服务“启用，且只有Organization的管理账号或”资源编排资源栈集服务“的委托管理员，才允许指定SERVICE_MANAGED创建资源栈集，否则会报错。

        :param permission_model: The permission_model of this StackSet.
        :type permission_model: str
        """
        self._permission_model = permission_model

    @property
    def status(self):
        r"""Gets the status of this StackSet.

        资源栈集的状态     * `IDLE` - 资源栈集空闲 * `OPERATION_IN_PROGRESS` - 资源栈集操作中 * `DEACTIVATED` - 资源栈集禁用

        :return: The status of this StackSet.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StackSet.

        资源栈集的状态     * `IDLE` - 资源栈集空闲 * `OPERATION_IN_PROGRESS` - 资源栈集操作中 * `DEACTIVATED` - 资源栈集禁用

        :param status: The status of this StackSet.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this StackSet.

        资源栈集的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The create_time of this StackSet.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this StackSet.

        资源栈集的创建时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param create_time: The create_time of this StackSet.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this StackSet.

        资源栈集的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :return: The update_time of this StackSet.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this StackSet.

        资源栈集的更新时间，格式为YYYY-MM-DDTHH:mm:ss.SSSZ，精确到毫秒，UTC时区，即，如1970-01-01T00:00:00.000Z。

        :param update_time: The update_time of this StackSet.
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
        if not isinstance(other, StackSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
