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
        """TopicConfiguration

        The model defined in huaweicloud sdk

        :param id: 每项事件通知配置的唯一标识，若是用户未指定ID，系统将自动分配一个ID。 
        :type id: str
        :param filter: 
        :type filter: :class:`huaweicloudsdkobs.v1.TopicConfigurationFilter`
        :param topic: 事件通知主题的URN，当OBS检测到桶中发生特定的事件后，将会发布通知消息至该主题，可以在[消息通知服务主题](https://console.huaweicloud.com/smn/?region&#x3D;cn-north-4#/topics/list)部分找到具体值。 模板：&lt;Topic&gt;urn:smn:region:project_id:smn_topic&lt;/Topic&gt; 
        :type topic: str
        :param event: 需要发布通知消息的事件类型。 说明：在一个TopicConfiguration、FunctionStageConfiguration配置项中可以添加多个事件类型。 合法值： 上传对象操作可以取以下值： ObjectCreated:Put ObjectCreated:Post ObjectCreated:Copy ObjectCreated:CompleteMultipartUpload  或者使用通配符支持所有上传操作 ObjectCreated:*  删除对象操作可以取以下值： ObjectRemoved:Delete ObjectRemoved:DeleteMarkerCreated  或者使用通配符支持所有删除操作 ObjectRemoved:* 
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
        """Gets the id of this TopicConfiguration.

        每项事件通知配置的唯一标识，若是用户未指定ID，系统将自动分配一个ID。 

        :return: The id of this TopicConfiguration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TopicConfiguration.

        每项事件通知配置的唯一标识，若是用户未指定ID，系统将自动分配一个ID。 

        :param id: The id of this TopicConfiguration.
        :type id: str
        """
        self._id = id

    @property
    def filter(self):
        """Gets the filter of this TopicConfiguration.

        :return: The filter of this TopicConfiguration.
        :rtype: :class:`huaweicloudsdkobs.v1.TopicConfigurationFilter`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this TopicConfiguration.

        :param filter: The filter of this TopicConfiguration.
        :type filter: :class:`huaweicloudsdkobs.v1.TopicConfigurationFilter`
        """
        self._filter = filter

    @property
    def topic(self):
        """Gets the topic of this TopicConfiguration.

        事件通知主题的URN，当OBS检测到桶中发生特定的事件后，将会发布通知消息至该主题，可以在[消息通知服务主题](https://console.huaweicloud.com/smn/?region=cn-north-4#/topics/list)部分找到具体值。 模板：<Topic>urn:smn:region:project_id:smn_topic</Topic> 

        :return: The topic of this TopicConfiguration.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this TopicConfiguration.

        事件通知主题的URN，当OBS检测到桶中发生特定的事件后，将会发布通知消息至该主题，可以在[消息通知服务主题](https://console.huaweicloud.com/smn/?region=cn-north-4#/topics/list)部分找到具体值。 模板：<Topic>urn:smn:region:project_id:smn_topic</Topic> 

        :param topic: The topic of this TopicConfiguration.
        :type topic: str
        """
        self._topic = topic

    @property
    def event(self):
        """Gets the event of this TopicConfiguration.

        需要发布通知消息的事件类型。 说明：在一个TopicConfiguration、FunctionStageConfiguration配置项中可以添加多个事件类型。 合法值： 上传对象操作可以取以下值： ObjectCreated:Put ObjectCreated:Post ObjectCreated:Copy ObjectCreated:CompleteMultipartUpload  或者使用通配符支持所有上传操作 ObjectCreated:*  删除对象操作可以取以下值： ObjectRemoved:Delete ObjectRemoved:DeleteMarkerCreated  或者使用通配符支持所有删除操作 ObjectRemoved:* 

        :return: The event of this TopicConfiguration.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this TopicConfiguration.

        需要发布通知消息的事件类型。 说明：在一个TopicConfiguration、FunctionStageConfiguration配置项中可以添加多个事件类型。 合法值： 上传对象操作可以取以下值： ObjectCreated:Put ObjectCreated:Post ObjectCreated:Copy ObjectCreated:CompleteMultipartUpload  或者使用通配符支持所有上传操作 ObjectCreated:*  删除对象操作可以取以下值： ObjectRemoved:Delete ObjectRemoved:DeleteMarkerCreated  或者使用通配符支持所有删除操作 ObjectRemoved:* 

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
