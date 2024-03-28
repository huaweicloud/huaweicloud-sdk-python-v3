# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotificationsResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_name': 'str',
        'operation_type': 'str',
        'agency_name': 'str',
        'operations': 'list[Operations]',
        'notify_user_list': 'list[NotificationUsers]',
        'status': 'str',
        'topic_id': 'str',
        'notification_id': 'str',
        'notification_type': 'str',
        'project_id': 'str',
        'create_time': 'int',
        'filter': 'Filter'
    }

    attribute_map = {
        'notification_name': 'notification_name',
        'operation_type': 'operation_type',
        'agency_name': 'agency_name',
        'operations': 'operations',
        'notify_user_list': 'notify_user_list',
        'status': 'status',
        'topic_id': 'topic_id',
        'notification_id': 'notification_id',
        'notification_type': 'notification_type',
        'project_id': 'project_id',
        'create_time': 'create_time',
        'filter': 'filter'
    }

    def __init__(self, notification_name=None, operation_type=None, agency_name=None, operations=None, notify_user_list=None, status=None, topic_id=None, notification_id=None, notification_type=None, project_id=None, create_time=None, filter=None):
        """NotificationsResponseBody

        The model defined in huaweicloud sdk

        :param notification_name: 标识关键操作名称。
        :type notification_name: str
        :param operation_type: 标识操作类型。 目前支持的操作类型有完整类型(complete)和自定义类型(customized)。 完整类型下，CTS发送通知的对象为已对接服务的所有事件。 自定义类型下，CTS发送通知的对象是在operations列表中指定的事件。
        :type operation_type: str
        :param agency_name: 云服务委托名称。
        :type agency_name: str
        :param operations: 操作事件列表。
        :type operations: list[:class:`huaweicloudsdkcts.v3.Operations`]
        :param notify_user_list: 通知用户列表，目前最多支持对10个用户组和50个用户发起的操作进行配置。
        :type notify_user_list: list[:class:`huaweicloudsdkcts.v3.NotificationUsers`]
        :param status: 标识关键操作通知状态，包括正常(enabled)，停止(disabled)两种状态。
        :type status: str
        :param topic_id: 消息通知服务的topic_urn或者函数工作流的func_urn。 - 消息通知服务的topic_urn可以通过消息通知服务的查询主题列表API获取，示例：urn:smn:regionId:f96188c7ccaf4ffba0c9aa149ab2bd57:test_topic_v2。 - 函数工作流的func_urn可以通过函数工作流的获取函数列表API获取，示例：urn:fss:xxxxxxxxx:7aad83af3e8d42e99ac194e8419e2c9b:function:default:test。
        :type topic_id: str
        :param notification_id: 关键操作通知的唯一标识。
        :type notification_id: str
        :param notification_type: 关键操作通知类型，根据topic_id区分为消息通知服务(smn)和函数工作流(fun)。
        :type notification_type: str
        :param project_id: 项目ID。
        :type project_id: str
        :param create_time: 关键操作通知创建时间戳。
        :type create_time: int
        :param filter: 
        :type filter: :class:`huaweicloudsdkcts.v3.Filter`
        """
        
        

        self._notification_name = None
        self._operation_type = None
        self._agency_name = None
        self._operations = None
        self._notify_user_list = None
        self._status = None
        self._topic_id = None
        self._notification_id = None
        self._notification_type = None
        self._project_id = None
        self._create_time = None
        self._filter = None
        self.discriminator = None

        if notification_name is not None:
            self.notification_name = notification_name
        if operation_type is not None:
            self.operation_type = operation_type
        if agency_name is not None:
            self.agency_name = agency_name
        if operations is not None:
            self.operations = operations
        if notify_user_list is not None:
            self.notify_user_list = notify_user_list
        if status is not None:
            self.status = status
        if topic_id is not None:
            self.topic_id = topic_id
        if notification_id is not None:
            self.notification_id = notification_id
        if notification_type is not None:
            self.notification_type = notification_type
        if project_id is not None:
            self.project_id = project_id
        if create_time is not None:
            self.create_time = create_time
        if filter is not None:
            self.filter = filter

    @property
    def notification_name(self):
        """Gets the notification_name of this NotificationsResponseBody.

        标识关键操作名称。

        :return: The notification_name of this NotificationsResponseBody.
        :rtype: str
        """
        return self._notification_name

    @notification_name.setter
    def notification_name(self, notification_name):
        """Sets the notification_name of this NotificationsResponseBody.

        标识关键操作名称。

        :param notification_name: The notification_name of this NotificationsResponseBody.
        :type notification_name: str
        """
        self._notification_name = notification_name

    @property
    def operation_type(self):
        """Gets the operation_type of this NotificationsResponseBody.

        标识操作类型。 目前支持的操作类型有完整类型(complete)和自定义类型(customized)。 完整类型下，CTS发送通知的对象为已对接服务的所有事件。 自定义类型下，CTS发送通知的对象是在operations列表中指定的事件。

        :return: The operation_type of this NotificationsResponseBody.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this NotificationsResponseBody.

        标识操作类型。 目前支持的操作类型有完整类型(complete)和自定义类型(customized)。 完整类型下，CTS发送通知的对象为已对接服务的所有事件。 自定义类型下，CTS发送通知的对象是在operations列表中指定的事件。

        :param operation_type: The operation_type of this NotificationsResponseBody.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def agency_name(self):
        """Gets the agency_name of this NotificationsResponseBody.

        云服务委托名称。

        :return: The agency_name of this NotificationsResponseBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this NotificationsResponseBody.

        云服务委托名称。

        :param agency_name: The agency_name of this NotificationsResponseBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def operations(self):
        """Gets the operations of this NotificationsResponseBody.

        操作事件列表。

        :return: The operations of this NotificationsResponseBody.
        :rtype: list[:class:`huaweicloudsdkcts.v3.Operations`]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this NotificationsResponseBody.

        操作事件列表。

        :param operations: The operations of this NotificationsResponseBody.
        :type operations: list[:class:`huaweicloudsdkcts.v3.Operations`]
        """
        self._operations = operations

    @property
    def notify_user_list(self):
        """Gets the notify_user_list of this NotificationsResponseBody.

        通知用户列表，目前最多支持对10个用户组和50个用户发起的操作进行配置。

        :return: The notify_user_list of this NotificationsResponseBody.
        :rtype: list[:class:`huaweicloudsdkcts.v3.NotificationUsers`]
        """
        return self._notify_user_list

    @notify_user_list.setter
    def notify_user_list(self, notify_user_list):
        """Sets the notify_user_list of this NotificationsResponseBody.

        通知用户列表，目前最多支持对10个用户组和50个用户发起的操作进行配置。

        :param notify_user_list: The notify_user_list of this NotificationsResponseBody.
        :type notify_user_list: list[:class:`huaweicloudsdkcts.v3.NotificationUsers`]
        """
        self._notify_user_list = notify_user_list

    @property
    def status(self):
        """Gets the status of this NotificationsResponseBody.

        标识关键操作通知状态，包括正常(enabled)，停止(disabled)两种状态。

        :return: The status of this NotificationsResponseBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NotificationsResponseBody.

        标识关键操作通知状态，包括正常(enabled)，停止(disabled)两种状态。

        :param status: The status of this NotificationsResponseBody.
        :type status: str
        """
        self._status = status

    @property
    def topic_id(self):
        """Gets the topic_id of this NotificationsResponseBody.

        消息通知服务的topic_urn或者函数工作流的func_urn。 - 消息通知服务的topic_urn可以通过消息通知服务的查询主题列表API获取，示例：urn:smn:regionId:f96188c7ccaf4ffba0c9aa149ab2bd57:test_topic_v2。 - 函数工作流的func_urn可以通过函数工作流的获取函数列表API获取，示例：urn:fss:xxxxxxxxx:7aad83af3e8d42e99ac194e8419e2c9b:function:default:test。

        :return: The topic_id of this NotificationsResponseBody.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        """Sets the topic_id of this NotificationsResponseBody.

        消息通知服务的topic_urn或者函数工作流的func_urn。 - 消息通知服务的topic_urn可以通过消息通知服务的查询主题列表API获取，示例：urn:smn:regionId:f96188c7ccaf4ffba0c9aa149ab2bd57:test_topic_v2。 - 函数工作流的func_urn可以通过函数工作流的获取函数列表API获取，示例：urn:fss:xxxxxxxxx:7aad83af3e8d42e99ac194e8419e2c9b:function:default:test。

        :param topic_id: The topic_id of this NotificationsResponseBody.
        :type topic_id: str
        """
        self._topic_id = topic_id

    @property
    def notification_id(self):
        """Gets the notification_id of this NotificationsResponseBody.

        关键操作通知的唯一标识。

        :return: The notification_id of this NotificationsResponseBody.
        :rtype: str
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this NotificationsResponseBody.

        关键操作通知的唯一标识。

        :param notification_id: The notification_id of this NotificationsResponseBody.
        :type notification_id: str
        """
        self._notification_id = notification_id

    @property
    def notification_type(self):
        """Gets the notification_type of this NotificationsResponseBody.

        关键操作通知类型，根据topic_id区分为消息通知服务(smn)和函数工作流(fun)。

        :return: The notification_type of this NotificationsResponseBody.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this NotificationsResponseBody.

        关键操作通知类型，根据topic_id区分为消息通知服务(smn)和函数工作流(fun)。

        :param notification_type: The notification_type of this NotificationsResponseBody.
        :type notification_type: str
        """
        self._notification_type = notification_type

    @property
    def project_id(self):
        """Gets the project_id of this NotificationsResponseBody.

        项目ID。

        :return: The project_id of this NotificationsResponseBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this NotificationsResponseBody.

        项目ID。

        :param project_id: The project_id of this NotificationsResponseBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def create_time(self):
        """Gets the create_time of this NotificationsResponseBody.

        关键操作通知创建时间戳。

        :return: The create_time of this NotificationsResponseBody.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this NotificationsResponseBody.

        关键操作通知创建时间戳。

        :param create_time: The create_time of this NotificationsResponseBody.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def filter(self):
        """Gets the filter of this NotificationsResponseBody.

        :return: The filter of this NotificationsResponseBody.
        :rtype: :class:`huaweicloudsdkcts.v3.Filter`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this NotificationsResponseBody.

        :param filter: The filter of this NotificationsResponseBody.
        :type filter: :class:`huaweicloudsdkcts.v3.Filter`
        """
        self._filter = filter

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
        if not isinstance(other, NotificationsResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
