# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateForwardingConfigRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kafka_config': 'UpdateKafkaConfigRequestDTO',
        'mrs_kafka_config': 'UpdateMrsKafkaConfigRequestDTO'
    }

    attribute_map = {
        'kafka_config': 'kafka_config',
        'mrs_kafka_config': 'mrs_kafka_config'
    }

    def __init__(self, kafka_config=None, mrs_kafka_config=None):
        """UpdateForwardingConfigRequestDTO

        The model defined in huaweicloud sdk

        :param kafka_config: 
        :type kafka_config: :class:`huaweicloudsdkdris.v1.UpdateKafkaConfigRequestDTO`
        :param mrs_kafka_config: 
        :type mrs_kafka_config: :class:`huaweicloudsdkdris.v1.UpdateMrsKafkaConfigRequestDTO`
        """
        
        

        self._kafka_config = None
        self._mrs_kafka_config = None
        self.discriminator = None

        if kafka_config is not None:
            self.kafka_config = kafka_config
        if mrs_kafka_config is not None:
            self.mrs_kafka_config = mrs_kafka_config

    @property
    def kafka_config(self):
        """Gets the kafka_config of this UpdateForwardingConfigRequestDTO.

        :return: The kafka_config of this UpdateForwardingConfigRequestDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateKafkaConfigRequestDTO`
        """
        return self._kafka_config

    @kafka_config.setter
    def kafka_config(self, kafka_config):
        """Sets the kafka_config of this UpdateForwardingConfigRequestDTO.

        :param kafka_config: The kafka_config of this UpdateForwardingConfigRequestDTO.
        :type kafka_config: :class:`huaweicloudsdkdris.v1.UpdateKafkaConfigRequestDTO`
        """
        self._kafka_config = kafka_config

    @property
    def mrs_kafka_config(self):
        """Gets the mrs_kafka_config of this UpdateForwardingConfigRequestDTO.

        :return: The mrs_kafka_config of this UpdateForwardingConfigRequestDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.UpdateMrsKafkaConfigRequestDTO`
        """
        return self._mrs_kafka_config

    @mrs_kafka_config.setter
    def mrs_kafka_config(self, mrs_kafka_config):
        """Sets the mrs_kafka_config of this UpdateForwardingConfigRequestDTO.

        :param mrs_kafka_config: The mrs_kafka_config of this UpdateForwardingConfigRequestDTO.
        :type mrs_kafka_config: :class:`huaweicloudsdkdris.v1.UpdateMrsKafkaConfigRequestDTO`
        """
        self._mrs_kafka_config = mrs_kafka_config

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
        if not isinstance(other, UpdateForwardingConfigRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
