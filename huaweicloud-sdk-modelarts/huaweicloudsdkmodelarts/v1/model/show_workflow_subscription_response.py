# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowSubscriptionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'subscription_id': 'str',
        'topic_urns': 'list[str]',
        'entity': 'str',
        'events': 'list[str]'
    }

    attribute_map = {
        'created_at': 'created_at',
        'subscription_id': 'subscription_id',
        'topic_urns': 'topic_urns',
        'entity': 'entity',
        'events': 'events'
    }

    def __init__(self, created_at=None, subscription_id=None, topic_urns=None, entity=None, events=None):
        r"""ShowWorkflowSubscriptionResponse

        The model defined in huaweicloud sdk

        :param created_at: 创建时间。
        :type created_at: str
        :param subscription_id: 订阅ID，唯一性标识。创建订阅时，后台自动生成。
        :type subscription_id: str
        :param topic_urns: 订阅的主题。
        :type topic_urns: list[str]
        :param entity: 订阅的主体。
        :type entity: str
        :param events: 订阅的事件。
        :type events: list[str]
        """
        
        super().__init__()

        self._created_at = None
        self._subscription_id = None
        self._topic_urns = None
        self._entity = None
        self._events = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if topic_urns is not None:
            self.topic_urns = topic_urns
        if entity is not None:
            self.entity = entity
        if events is not None:
            self.events = events

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowWorkflowSubscriptionResponse.

        创建时间。

        :return: The created_at of this ShowWorkflowSubscriptionResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowWorkflowSubscriptionResponse.

        创建时间。

        :param created_at: The created_at of this ShowWorkflowSubscriptionResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this ShowWorkflowSubscriptionResponse.

        订阅ID，唯一性标识。创建订阅时，后台自动生成。

        :return: The subscription_id of this ShowWorkflowSubscriptionResponse.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this ShowWorkflowSubscriptionResponse.

        订阅ID，唯一性标识。创建订阅时，后台自动生成。

        :param subscription_id: The subscription_id of this ShowWorkflowSubscriptionResponse.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

    @property
    def topic_urns(self):
        r"""Gets the topic_urns of this ShowWorkflowSubscriptionResponse.

        订阅的主题。

        :return: The topic_urns of this ShowWorkflowSubscriptionResponse.
        :rtype: list[str]
        """
        return self._topic_urns

    @topic_urns.setter
    def topic_urns(self, topic_urns):
        r"""Sets the topic_urns of this ShowWorkflowSubscriptionResponse.

        订阅的主题。

        :param topic_urns: The topic_urns of this ShowWorkflowSubscriptionResponse.
        :type topic_urns: list[str]
        """
        self._topic_urns = topic_urns

    @property
    def entity(self):
        r"""Gets the entity of this ShowWorkflowSubscriptionResponse.

        订阅的主体。

        :return: The entity of this ShowWorkflowSubscriptionResponse.
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        r"""Sets the entity of this ShowWorkflowSubscriptionResponse.

        订阅的主体。

        :param entity: The entity of this ShowWorkflowSubscriptionResponse.
        :type entity: str
        """
        self._entity = entity

    @property
    def events(self):
        r"""Gets the events of this ShowWorkflowSubscriptionResponse.

        订阅的事件。

        :return: The events of this ShowWorkflowSubscriptionResponse.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this ShowWorkflowSubscriptionResponse.

        订阅的事件。

        :param events: The events of this ShowWorkflowSubscriptionResponse.
        :type events: list[str]
        """
        self._events = events

    def to_dict(self):
        import warnings
        warnings.warn("ShowWorkflowSubscriptionResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowWorkflowSubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
