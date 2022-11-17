# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateQueueResponse(SdkResponse):

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
        'kafka_topic': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'kafka_topic': 'kafka_topic'
    }

    def __init__(self, id=None, name=None, kafka_topic=None):
        """CreateQueueResponse

        The model defined in huaweicloud sdk

        :param id: 队列ID。
        :type id: str
        :param name: 队列的名称。
        :type name: str
        :param kafka_topic: 仅Kafka队列才有该响应参数。  使用Kafka SDK时的Kafka topic的ID。
        :type kafka_topic: str
        """
        
        super(CreateQueueResponse, self).__init__()

        self._id = None
        self._name = None
        self._kafka_topic = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if kafka_topic is not None:
            self.kafka_topic = kafka_topic

    @property
    def id(self):
        """Gets the id of this CreateQueueResponse.

        队列ID。

        :return: The id of this CreateQueueResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateQueueResponse.

        队列ID。

        :param id: The id of this CreateQueueResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateQueueResponse.

        队列的名称。

        :return: The name of this CreateQueueResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateQueueResponse.

        队列的名称。

        :param name: The name of this CreateQueueResponse.
        :type name: str
        """
        self._name = name

    @property
    def kafka_topic(self):
        """Gets the kafka_topic of this CreateQueueResponse.

        仅Kafka队列才有该响应参数。  使用Kafka SDK时的Kafka topic的ID。

        :return: The kafka_topic of this CreateQueueResponse.
        :rtype: str
        """
        return self._kafka_topic

    @kafka_topic.setter
    def kafka_topic(self, kafka_topic):
        """Sets the kafka_topic of this CreateQueueResponse.

        仅Kafka队列才有该响应参数。  使用Kafka SDK时的Kafka topic的ID。

        :param kafka_topic: The kafka_topic of this CreateQueueResponse.
        :type kafka_topic: str
        """
        self._kafka_topic = kafka_topic

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
        if not isinstance(other, CreateQueueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
