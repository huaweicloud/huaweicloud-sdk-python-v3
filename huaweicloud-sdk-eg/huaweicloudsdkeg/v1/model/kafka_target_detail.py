# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaTargetDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic': 'str',
        'key_transform': 'KafkaTargetDetailKeyTransform'
    }

    attribute_map = {
        'topic': 'topic',
        'key_transform': 'keyTransform'
    }

    def __init__(self, topic=None, key_transform=None):
        r"""KafkaTargetDetail

        The model defined in huaweicloud sdk

        :param topic: 主题
        :type topic: str
        :param key_transform: 
        :type key_transform: :class:`huaweicloudsdkeg.v1.KafkaTargetDetailKeyTransform`
        """
        
        

        self._topic = None
        self._key_transform = None
        self.discriminator = None

        self.topic = topic
        if key_transform is not None:
            self.key_transform = key_transform

    @property
    def topic(self):
        r"""Gets the topic of this KafkaTargetDetail.

        主题

        :return: The topic of this KafkaTargetDetail.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this KafkaTargetDetail.

        主题

        :param topic: The topic of this KafkaTargetDetail.
        :type topic: str
        """
        self._topic = topic

    @property
    def key_transform(self):
        r"""Gets the key_transform of this KafkaTargetDetail.

        :return: The key_transform of this KafkaTargetDetail.
        :rtype: :class:`huaweicloudsdkeg.v1.KafkaTargetDetailKeyTransform`
        """
        return self._key_transform

    @key_transform.setter
    def key_transform(self, key_transform):
        r"""Sets the key_transform of this KafkaTargetDetail.

        :param key_transform: The key_transform of this KafkaTargetDetail.
        :type key_transform: :class:`huaweicloudsdkeg.v1.KafkaTargetDetailKeyTransform`
        """
        self._key_transform = key_transform

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
        if not isinstance(other, KafkaTargetDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
