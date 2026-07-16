# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventCategoriesResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'notification': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'notification': 'notification'
    }

    def __init__(self, id=None, name=None, description=None, notification=None):
        r"""EventCategoriesResp

        The model defined in huaweicloud sdk

        :param id: **参数解释**：事件类型id。 **取值范围**：枚举值如下： - JobStarted：作业开始 - JobCompleted：作业结束 - JobFailed：作业失败 - JobTerminated：作业终止 - JobRestarted：作业重启 - JobHanged：作业疑似卡死 - JobPreempted：作业抢占
        :type id: str
        :param name: **参数解释**：事件类型名称。 **取值范围**：不涉及。
        :type name: str
        :param description: **参数解释**：事件类型描述。 **取值范围**：不涉及。
        :type description: str
        :param notification: **参数解释**：是否通知。 **取值范围**： - true：通知 - false：不通知
        :type notification: bool
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._notification = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if notification is not None:
            self.notification = notification

    @property
    def id(self):
        r"""Gets the id of this EventCategoriesResp.

        **参数解释**：事件类型id。 **取值范围**：枚举值如下： - JobStarted：作业开始 - JobCompleted：作业结束 - JobFailed：作业失败 - JobTerminated：作业终止 - JobRestarted：作业重启 - JobHanged：作业疑似卡死 - JobPreempted：作业抢占

        :return: The id of this EventCategoriesResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EventCategoriesResp.

        **参数解释**：事件类型id。 **取值范围**：枚举值如下： - JobStarted：作业开始 - JobCompleted：作业结束 - JobFailed：作业失败 - JobTerminated：作业终止 - JobRestarted：作业重启 - JobHanged：作业疑似卡死 - JobPreempted：作业抢占

        :param id: The id of this EventCategoriesResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EventCategoriesResp.

        **参数解释**：事件类型名称。 **取值范围**：不涉及。

        :return: The name of this EventCategoriesResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EventCategoriesResp.

        **参数解释**：事件类型名称。 **取值范围**：不涉及。

        :param name: The name of this EventCategoriesResp.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this EventCategoriesResp.

        **参数解释**：事件类型描述。 **取值范围**：不涉及。

        :return: The description of this EventCategoriesResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EventCategoriesResp.

        **参数解释**：事件类型描述。 **取值范围**：不涉及。

        :param description: The description of this EventCategoriesResp.
        :type description: str
        """
        self._description = description

    @property
    def notification(self):
        r"""Gets the notification of this EventCategoriesResp.

        **参数解释**：是否通知。 **取值范围**： - true：通知 - false：不通知

        :return: The notification of this EventCategoriesResp.
        :rtype: bool
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        r"""Sets the notification of this EventCategoriesResp.

        **参数解释**：是否通知。 **取值范围**： - true：通知 - false：不通知

        :param notification: The notification of this EventCategoriesResp.
        :type notification: bool
        """
        self._notification = notification

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
        if not isinstance(other, EventCategoriesResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
