# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopicConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "TopicConfiguration"

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'filter': 'TopicConfigurationFilter',
        'topic': 'str',
        'event': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'filter': 'Filter',
        'topic': 'Topic',
        'event': 'Event'
    }

    def __init__(self, id=None, filter=None, topic=None, event=None):
        r"""TopicConfiguration

        The model defined in huaweicloud sdk

        :param id: Unique ID of each event notification. If you do not specify an ID, the system assigns one.
        :type id: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkobs.v1.TopicConfigurationFilter`
        :param topic: URN of the event notification topic. When OBS detects a specific event in a bucket, it publishes a notification message to this topic. You can find the topic&#39;s URN on the [Topics](https://console-intl.huaweicloud.com/smn/?agencyId&#x3D;7b00025342f14bcabb245478269c6593&amp;region&#x3D;cn-east-3&amp;locale&#x3D;en-us#/topics/list) page of the SMN console. Template: &lt;Topic&gt;urn:smn:region:project_id:smn_topic&lt;/Topic&gt;
        :type topic: str
        :param event: Event types for which OBS sends notifications. Multiple event types can be added in one **TopicConfiguration** or **FunctionGraphConfiguration** item. Value options: Choose from the following for object upload operations: ObjectCreated:Put ObjectCreated:Post ObjectCreated:Copy ObjectCreated:CompleteMultipartUpload  Or use a wildcard character to support all upload operations: ObjectCreated:*  Choose from the following for object delete operations: ObjectRemoved:Delete ObjectRemoved:DeleteMarkerCreated  Or use a wildcard character to support all delete operations: ObjectRemoved:*
        :type event: str
        """
        
        

        self._id = None
        self._filter = None
        self._topic = None
        self._event = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if filter is not None:
            self.filter = filter
        if topic is not None:
            self.topic = topic
        if event is not None:
            self.event = event

    @property
    def id(self):
        r"""Gets the id of this TopicConfiguration.

        Unique ID of each event notification. If you do not specify an ID, the system assigns one.

        :return: The id of this TopicConfiguration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TopicConfiguration.

        Unique ID of each event notification. If you do not specify an ID, the system assigns one.

        :param id: The id of this TopicConfiguration.
        :type id: str
        """
        self._id = id

    @property
    def filter(self):
        r"""Gets the filter of this TopicConfiguration.

        :return: The filter of this TopicConfiguration.
        :rtype: :class:`huaweicloudsdkobs.v1.TopicConfigurationFilter`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this TopicConfiguration.

        :param filter: The filter of this TopicConfiguration.
        :type filter: :class:`huaweicloudsdkobs.v1.TopicConfigurationFilter`
        """
        self._filter = filter

    @property
    def topic(self):
        r"""Gets the topic of this TopicConfiguration.

        URN of the event notification topic. When OBS detects a specific event in a bucket, it publishes a notification message to this topic. You can find the topic's URN on the [Topics](https://console-intl.huaweicloud.com/smn/?agencyId=7b00025342f14bcabb245478269c6593&region=cn-east-3&locale=en-us#/topics/list) page of the SMN console. Template: <Topic>urn:smn:region:project_id:smn_topic</Topic>

        :return: The topic of this TopicConfiguration.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this TopicConfiguration.

        URN of the event notification topic. When OBS detects a specific event in a bucket, it publishes a notification message to this topic. You can find the topic's URN on the [Topics](https://console-intl.huaweicloud.com/smn/?agencyId=7b00025342f14bcabb245478269c6593&region=cn-east-3&locale=en-us#/topics/list) page of the SMN console. Template: <Topic>urn:smn:region:project_id:smn_topic</Topic>

        :param topic: The topic of this TopicConfiguration.
        :type topic: str
        """
        self._topic = topic

    @property
    def event(self):
        r"""Gets the event of this TopicConfiguration.

        Event types for which OBS sends notifications. Multiple event types can be added in one **TopicConfiguration** or **FunctionGraphConfiguration** item. Value options: Choose from the following for object upload operations: ObjectCreated:Put ObjectCreated:Post ObjectCreated:Copy ObjectCreated:CompleteMultipartUpload  Or use a wildcard character to support all upload operations: ObjectCreated:*  Choose from the following for object delete operations: ObjectRemoved:Delete ObjectRemoved:DeleteMarkerCreated  Or use a wildcard character to support all delete operations: ObjectRemoved:*

        :return: The event of this TopicConfiguration.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        r"""Sets the event of this TopicConfiguration.

        Event types for which OBS sends notifications. Multiple event types can be added in one **TopicConfiguration** or **FunctionGraphConfiguration** item. Value options: Choose from the following for object upload operations: ObjectCreated:Put ObjectCreated:Post ObjectCreated:Copy ObjectCreated:CompleteMultipartUpload  Or use a wildcard character to support all upload operations: ObjectCreated:*  Choose from the following for object delete operations: ObjectRemoved:Delete ObjectRemoved:DeleteMarkerCreated  Or use a wildcard character to support all delete operations: ObjectRemoved:*

        :param event: The event of this TopicConfiguration.
        :type event: str
        """
        self._event = event

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
        if not isinstance(other, TopicConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
