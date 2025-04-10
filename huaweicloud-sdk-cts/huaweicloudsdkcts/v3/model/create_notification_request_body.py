# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNotificationRequestBody:

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
        'topic_id': 'str',
        'filter': 'Filter'
    }

    attribute_map = {
        'notification_name': 'notification_name',
        'operation_type': 'operation_type',
        'agency_name': 'agency_name',
        'operations': 'operations',
        'notify_user_list': 'notify_user_list',
        'topic_id': 'topic_id',
        'filter': 'filter'
    }

    def __init__(self, notification_name=None, operation_type=None, agency_name=None, operations=None, notify_user_list=None, topic_id=None, filter=None):
        r"""CreateNotificationRequestBody

        The model defined in huaweicloud sdk

        :param notification_name: 标识关键操作名称。
        :type notification_name: str
        :param operation_type: 标识操作类型。 目前支持的操作类型有完整类型(complete)和自定义类型(customized)。 完整类型下，CTS发送通知的对象为已对接服务的所有事件，此时不用指定operations和notify_user_list字段。 自定义类型下，CTS发送通知的对象是在operations列表中指定的事件。
        :type operation_type: str
        :param agency_name: 云服务委托名称。 参数值为\&quot;cts_admin_trust\&quot;时，创建关键操作通知时会自动创建一个云服务委托：cts_admin_trust。
        :type agency_name: str
        :param operations: 操作事件列表。
        :type operations: list[:class:`huaweicloudsdkcts.v3.Operations`]
        :param notify_user_list: 通知用户列表，目前最多支持对10个用户组和50个用户发起的操作进行配置。
        :type notify_user_list: list[:class:`huaweicloudsdkcts.v3.NotificationUsers`]
        :param topic_id: 消息通知服务的topic_urn或者函数工作流的func_urn。 - 消息通知服务的topic_urn可以通过消息通知服务的查询主题列表API获取，示例：urn:smn:regionId:f96188c7ccaf4ffba0c9aa149ab2bd57:test_topic_v2。 - 函数工作流的func_urn可以通过函数工作流的获取函数列表API获取，示例：urn:fss:xxxxxxxxx:7aad83af3e8d42e99ac194e8419e2c9b:function:default:test。
        :type topic_id: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkcts.v3.Filter`
        """
        
        

        self._notification_name = None
        self._operation_type = None
        self._agency_name = None
        self._operations = None
        self._notify_user_list = None
        self._topic_id = None
        self._filter = None
        self.discriminator = None

        self.notification_name = notification_name
        self.operation_type = operation_type
        if agency_name is not None:
            self.agency_name = agency_name
        if operations is not None:
            self.operations = operations
        if notify_user_list is not None:
            self.notify_user_list = notify_user_list
        if topic_id is not None:
            self.topic_id = topic_id
        if filter is not None:
            self.filter = filter

    @property
    def notification_name(self):
        r"""Gets the notification_name of this CreateNotificationRequestBody.

        标识关键操作名称。

        :return: The notification_name of this CreateNotificationRequestBody.
        :rtype: str
        """
        return self._notification_name

    @notification_name.setter
    def notification_name(self, notification_name):
        r"""Sets the notification_name of this CreateNotificationRequestBody.

        标识关键操作名称。

        :param notification_name: The notification_name of this CreateNotificationRequestBody.
        :type notification_name: str
        """
        self._notification_name = notification_name

    @property
    def operation_type(self):
        r"""Gets the operation_type of this CreateNotificationRequestBody.

        标识操作类型。 目前支持的操作类型有完整类型(complete)和自定义类型(customized)。 完整类型下，CTS发送通知的对象为已对接服务的所有事件，此时不用指定operations和notify_user_list字段。 自定义类型下，CTS发送通知的对象是在operations列表中指定的事件。

        :return: The operation_type of this CreateNotificationRequestBody.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this CreateNotificationRequestBody.

        标识操作类型。 目前支持的操作类型有完整类型(complete)和自定义类型(customized)。 完整类型下，CTS发送通知的对象为已对接服务的所有事件，此时不用指定operations和notify_user_list字段。 自定义类型下，CTS发送通知的对象是在operations列表中指定的事件。

        :param operation_type: The operation_type of this CreateNotificationRequestBody.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CreateNotificationRequestBody.

        云服务委托名称。 参数值为\"cts_admin_trust\"时，创建关键操作通知时会自动创建一个云服务委托：cts_admin_trust。

        :return: The agency_name of this CreateNotificationRequestBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CreateNotificationRequestBody.

        云服务委托名称。 参数值为\"cts_admin_trust\"时，创建关键操作通知时会自动创建一个云服务委托：cts_admin_trust。

        :param agency_name: The agency_name of this CreateNotificationRequestBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def operations(self):
        r"""Gets the operations of this CreateNotificationRequestBody.

        操作事件列表。

        :return: The operations of this CreateNotificationRequestBody.
        :rtype: list[:class:`huaweicloudsdkcts.v3.Operations`]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        r"""Sets the operations of this CreateNotificationRequestBody.

        操作事件列表。

        :param operations: The operations of this CreateNotificationRequestBody.
        :type operations: list[:class:`huaweicloudsdkcts.v3.Operations`]
        """
        self._operations = operations

    @property
    def notify_user_list(self):
        r"""Gets the notify_user_list of this CreateNotificationRequestBody.

        通知用户列表，目前最多支持对10个用户组和50个用户发起的操作进行配置。

        :return: The notify_user_list of this CreateNotificationRequestBody.
        :rtype: list[:class:`huaweicloudsdkcts.v3.NotificationUsers`]
        """
        return self._notify_user_list

    @notify_user_list.setter
    def notify_user_list(self, notify_user_list):
        r"""Sets the notify_user_list of this CreateNotificationRequestBody.

        通知用户列表，目前最多支持对10个用户组和50个用户发起的操作进行配置。

        :param notify_user_list: The notify_user_list of this CreateNotificationRequestBody.
        :type notify_user_list: list[:class:`huaweicloudsdkcts.v3.NotificationUsers`]
        """
        self._notify_user_list = notify_user_list

    @property
    def topic_id(self):
        r"""Gets the topic_id of this CreateNotificationRequestBody.

        消息通知服务的topic_urn或者函数工作流的func_urn。 - 消息通知服务的topic_urn可以通过消息通知服务的查询主题列表API获取，示例：urn:smn:regionId:f96188c7ccaf4ffba0c9aa149ab2bd57:test_topic_v2。 - 函数工作流的func_urn可以通过函数工作流的获取函数列表API获取，示例：urn:fss:xxxxxxxxx:7aad83af3e8d42e99ac194e8419e2c9b:function:default:test。

        :return: The topic_id of this CreateNotificationRequestBody.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        r"""Sets the topic_id of this CreateNotificationRequestBody.

        消息通知服务的topic_urn或者函数工作流的func_urn。 - 消息通知服务的topic_urn可以通过消息通知服务的查询主题列表API获取，示例：urn:smn:regionId:f96188c7ccaf4ffba0c9aa149ab2bd57:test_topic_v2。 - 函数工作流的func_urn可以通过函数工作流的获取函数列表API获取，示例：urn:fss:xxxxxxxxx:7aad83af3e8d42e99ac194e8419e2c9b:function:default:test。

        :param topic_id: The topic_id of this CreateNotificationRequestBody.
        :type topic_id: str
        """
        self._topic_id = topic_id

    @property
    def filter(self):
        r"""Gets the filter of this CreateNotificationRequestBody.

        :return: The filter of this CreateNotificationRequestBody.
        :rtype: :class:`huaweicloudsdkcts.v3.Filter`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this CreateNotificationRequestBody.

        :param filter: The filter of this CreateNotificationRequestBody.
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
        if not isinstance(other, CreateNotificationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
