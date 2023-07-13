# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventStreamingSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_kafka': 'SourceKafkaMQParameters',
        'name': 'str'
    }

    attribute_map = {
        'source_kafka': 'source_kafka',
        'name': 'name'
    }

    def __init__(self, source_kafka=None, name=None):
        """EventStreamingSource

        The model defined in huaweicloud sdk

        :param source_kafka: 
        :type source_kafka: :class:`huaweicloudsdkeg.v1.SourceKafkaMQParameters`
        :param name: 事件源类型名称
        :type name: str
        """
        
        

        self._source_kafka = None
        self._name = None
        self.discriminator = None

        if source_kafka is not None:
            self.source_kafka = source_kafka
        if name is not None:
            self.name = name

    @property
    def source_kafka(self):
        """Gets the source_kafka of this EventStreamingSource.

        :return: The source_kafka of this EventStreamingSource.
        :rtype: :class:`huaweicloudsdkeg.v1.SourceKafkaMQParameters`
        """
        return self._source_kafka

    @source_kafka.setter
    def source_kafka(self, source_kafka):
        """Sets the source_kafka of this EventStreamingSource.

        :param source_kafka: The source_kafka of this EventStreamingSource.
        :type source_kafka: :class:`huaweicloudsdkeg.v1.SourceKafkaMQParameters`
        """
        self._source_kafka = source_kafka

    @property
    def name(self):
        """Gets the name of this EventStreamingSource.

        事件源类型名称

        :return: The name of this EventStreamingSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EventStreamingSource.

        事件源类型名称

        :param name: The name of this EventStreamingSource.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, EventStreamingSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
