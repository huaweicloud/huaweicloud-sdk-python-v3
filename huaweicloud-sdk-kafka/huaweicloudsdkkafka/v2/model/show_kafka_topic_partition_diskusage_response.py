# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKafkaTopicPartitionDiskusageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'broker_list': 'list[DiskusageEntity]'
    }

    attribute_map = {
        'broker_list': 'broker_list'
    }

    def __init__(self, broker_list=None):
        """ShowKafkaTopicPartitionDiskusageResponse

        The model defined in huaweicloud sdk

        :param broker_list: Broker列表。
        :type broker_list: list[:class:`huaweicloudsdkkafka.v2.DiskusageEntity`]
        """
        
        super(ShowKafkaTopicPartitionDiskusageResponse, self).__init__()

        self._broker_list = None
        self.discriminator = None

        if broker_list is not None:
            self.broker_list = broker_list

    @property
    def broker_list(self):
        """Gets the broker_list of this ShowKafkaTopicPartitionDiskusageResponse.

        Broker列表。

        :return: The broker_list of this ShowKafkaTopicPartitionDiskusageResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.DiskusageEntity`]
        """
        return self._broker_list

    @broker_list.setter
    def broker_list(self, broker_list):
        """Sets the broker_list of this ShowKafkaTopicPartitionDiskusageResponse.

        Broker列表。

        :param broker_list: The broker_list of this ShowKafkaTopicPartitionDiskusageResponse.
        :type broker_list: list[:class:`huaweicloudsdkkafka.v2.DiskusageEntity`]
        """
        self._broker_list = broker_list

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
        if not isinstance(other, ShowKafkaTopicPartitionDiskusageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
