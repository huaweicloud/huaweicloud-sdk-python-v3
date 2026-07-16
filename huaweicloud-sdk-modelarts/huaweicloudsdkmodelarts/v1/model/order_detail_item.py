# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderDetailItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_name': 'str',
        'action': 'str',
        'status': 'str',
        'begin_timestamp': 'str',
        'update_timestamp': 'str',
        'message': 'str'
    }

    attribute_map = {
        'resource_name': 'resourceName',
        'action': 'action',
        'status': 'status',
        'begin_timestamp': 'beginTimestamp',
        'update_timestamp': 'updateTimestamp',
        'message': 'message'
    }

    def __init__(self, resource_name=None, action=None, status=None, begin_timestamp=None, update_timestamp=None, message=None):
        r"""OrderDetailItem

        The model defined in huaweicloud sdk

        :param resource_name: **参数解释**：资源的ID，取值自资源详情的metadata.name字段。 **取值范围**：不涉及。
        :type resource_name: str
        :param action: **参数解释**：订单关联的资源变更动作类型。 **取值范围**：可选值如下： - createPool：创建资源池。 - deletePool：删除资源池。 - createNode：创建节点。 - deleteNode：删除节点，主要是包周期节点退订场景。 - renew：续费。 - toPeriodic：转包周期。
        :type action: str
        :param status: **参数解释**：订单关联资源的变更状态。 **取值范围**：可选值如下： - processing：处理中，资源正在处理中。 - succeed：成功，资源处理成功。 - failed：失败，资源处理失败。
        :type status: str
        :param begin_timestamp: **参数解释**：资源开始变更时间戳，形如1744285793000，单位毫秒。 **取值范围**：不涉及。
        :type begin_timestamp: str
        :param update_timestamp: **参数解释**：资源变更最后更新时间戳，形如1744285793000，单位毫秒。 **取值范围**：不涉及。
        :type update_timestamp: str
        :param message: **参数解释**：资源变更的执行信息，如失败原因。 **取值范围**：不涉及。
        :type message: str
        """
        
        

        self._resource_name = None
        self._action = None
        self._status = None
        self._begin_timestamp = None
        self._update_timestamp = None
        self._message = None
        self.discriminator = None

        if resource_name is not None:
            self.resource_name = resource_name
        self.action = action
        self.status = status
        if begin_timestamp is not None:
            self.begin_timestamp = begin_timestamp
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp
        if message is not None:
            self.message = message

    @property
    def resource_name(self):
        r"""Gets the resource_name of this OrderDetailItem.

        **参数解释**：资源的ID，取值自资源详情的metadata.name字段。 **取值范围**：不涉及。

        :return: The resource_name of this OrderDetailItem.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this OrderDetailItem.

        **参数解释**：资源的ID，取值自资源详情的metadata.name字段。 **取值范围**：不涉及。

        :param resource_name: The resource_name of this OrderDetailItem.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def action(self):
        r"""Gets the action of this OrderDetailItem.

        **参数解释**：订单关联的资源变更动作类型。 **取值范围**：可选值如下： - createPool：创建资源池。 - deletePool：删除资源池。 - createNode：创建节点。 - deleteNode：删除节点，主要是包周期节点退订场景。 - renew：续费。 - toPeriodic：转包周期。

        :return: The action of this OrderDetailItem.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this OrderDetailItem.

        **参数解释**：订单关联的资源变更动作类型。 **取值范围**：可选值如下： - createPool：创建资源池。 - deletePool：删除资源池。 - createNode：创建节点。 - deleteNode：删除节点，主要是包周期节点退订场景。 - renew：续费。 - toPeriodic：转包周期。

        :param action: The action of this OrderDetailItem.
        :type action: str
        """
        self._action = action

    @property
    def status(self):
        r"""Gets the status of this OrderDetailItem.

        **参数解释**：订单关联资源的变更状态。 **取值范围**：可选值如下： - processing：处理中，资源正在处理中。 - succeed：成功，资源处理成功。 - failed：失败，资源处理失败。

        :return: The status of this OrderDetailItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OrderDetailItem.

        **参数解释**：订单关联资源的变更状态。 **取值范围**：可选值如下： - processing：处理中，资源正在处理中。 - succeed：成功，资源处理成功。 - failed：失败，资源处理失败。

        :param status: The status of this OrderDetailItem.
        :type status: str
        """
        self._status = status

    @property
    def begin_timestamp(self):
        r"""Gets the begin_timestamp of this OrderDetailItem.

        **参数解释**：资源开始变更时间戳，形如1744285793000，单位毫秒。 **取值范围**：不涉及。

        :return: The begin_timestamp of this OrderDetailItem.
        :rtype: str
        """
        return self._begin_timestamp

    @begin_timestamp.setter
    def begin_timestamp(self, begin_timestamp):
        r"""Sets the begin_timestamp of this OrderDetailItem.

        **参数解释**：资源开始变更时间戳，形如1744285793000，单位毫秒。 **取值范围**：不涉及。

        :param begin_timestamp: The begin_timestamp of this OrderDetailItem.
        :type begin_timestamp: str
        """
        self._begin_timestamp = begin_timestamp

    @property
    def update_timestamp(self):
        r"""Gets the update_timestamp of this OrderDetailItem.

        **参数解释**：资源变更最后更新时间戳，形如1744285793000，单位毫秒。 **取值范围**：不涉及。

        :return: The update_timestamp of this OrderDetailItem.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        r"""Sets the update_timestamp of this OrderDetailItem.

        **参数解释**：资源变更最后更新时间戳，形如1744285793000，单位毫秒。 **取值范围**：不涉及。

        :param update_timestamp: The update_timestamp of this OrderDetailItem.
        :type update_timestamp: str
        """
        self._update_timestamp = update_timestamp

    @property
    def message(self):
        r"""Gets the message of this OrderDetailItem.

        **参数解释**：资源变更的执行信息，如失败原因。 **取值范围**：不涉及。

        :return: The message of this OrderDetailItem.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this OrderDetailItem.

        **参数解释**：资源变更的执行信息，如失败原因。 **取值范围**：不涉及。

        :param message: The message of this OrderDetailItem.
        :type message: str
        """
        self._message = message

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrderDetailItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
