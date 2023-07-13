# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTracedEventsRespResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_name': 'str',
        'source_name': 'str',
        'source_provider': 'str',
        'event_type': 'str',
        'event_id': 'str',
        'event_received_time': 'int'
    }

    attribute_map = {
        'subscription_name': 'subscription_name',
        'source_name': 'source_name',
        'source_provider': 'source_provider',
        'event_type': 'event_type',
        'event_id': 'event_id',
        'event_received_time': 'event_received_time'
    }

    def __init__(self, subscription_name=None, source_name=None, source_provider=None, event_type=None, event_id=None, event_received_time=None):
        """ListTracedEventsRespResult

        The model defined in huaweicloud sdk

        :param subscription_name: 
        :type subscription_name: str
        :param source_name: 
        :type source_name: str
        :param source_provider: 
        :type source_provider: str
        :param event_type: 
        :type event_type: str
        :param event_id: 
        :type event_id: str
        :param event_received_time: 
        :type event_received_time: int
        """
        
        

        self._subscription_name = None
        self._source_name = None
        self._source_provider = None
        self._event_type = None
        self._event_id = None
        self._event_received_time = None
        self.discriminator = None

        if subscription_name is not None:
            self.subscription_name = subscription_name
        if source_name is not None:
            self.source_name = source_name
        if source_provider is not None:
            self.source_provider = source_provider
        if event_type is not None:
            self.event_type = event_type
        if event_id is not None:
            self.event_id = event_id
        if event_received_time is not None:
            self.event_received_time = event_received_time

    @property
    def subscription_name(self):
        """Gets the subscription_name of this ListTracedEventsRespResult.

        :return: The subscription_name of this ListTracedEventsRespResult.
        :rtype: str
        """
        return self._subscription_name

    @subscription_name.setter
    def subscription_name(self, subscription_name):
        """Sets the subscription_name of this ListTracedEventsRespResult.

        :param subscription_name: The subscription_name of this ListTracedEventsRespResult.
        :type subscription_name: str
        """
        self._subscription_name = subscription_name

    @property
    def source_name(self):
        """Gets the source_name of this ListTracedEventsRespResult.

        :return: The source_name of this ListTracedEventsRespResult.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this ListTracedEventsRespResult.

        :param source_name: The source_name of this ListTracedEventsRespResult.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def source_provider(self):
        """Gets the source_provider of this ListTracedEventsRespResult.

        :return: The source_provider of this ListTracedEventsRespResult.
        :rtype: str
        """
        return self._source_provider

    @source_provider.setter
    def source_provider(self, source_provider):
        """Sets the source_provider of this ListTracedEventsRespResult.

        :param source_provider: The source_provider of this ListTracedEventsRespResult.
        :type source_provider: str
        """
        self._source_provider = source_provider

    @property
    def event_type(self):
        """Gets the event_type of this ListTracedEventsRespResult.

        :return: The event_type of this ListTracedEventsRespResult.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ListTracedEventsRespResult.

        :param event_type: The event_type of this ListTracedEventsRespResult.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_id(self):
        """Gets the event_id of this ListTracedEventsRespResult.

        :return: The event_id of this ListTracedEventsRespResult.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this ListTracedEventsRespResult.

        :param event_id: The event_id of this ListTracedEventsRespResult.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_received_time(self):
        """Gets the event_received_time of this ListTracedEventsRespResult.

        :return: The event_received_time of this ListTracedEventsRespResult.
        :rtype: int
        """
        return self._event_received_time

    @event_received_time.setter
    def event_received_time(self, event_received_time):
        """Sets the event_received_time of this ListTracedEventsRespResult.

        :param event_received_time: The event_received_time of this ListTracedEventsRespResult.
        :type event_received_time: int
        """
        self._event_received_time = event_received_time

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
        if not isinstance(other, ListTracedEventsRespResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
