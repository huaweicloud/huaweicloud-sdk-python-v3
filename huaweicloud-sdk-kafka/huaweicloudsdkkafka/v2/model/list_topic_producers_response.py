# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopicProducersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'producers': 'list[KafkaTopicProducerResponseProducers]'
    }

    attribute_map = {
        'total': 'total',
        'producers': 'producers'
    }

    def __init__(self, total=None, producers=None):
        """ListTopicProducersResponse

        The model defined in huaweicloud sdk

        :param total: 总条数
        :type total: int
        :param producers: 生产者列表
        :type producers: list[:class:`huaweicloudsdkkafka.v2.KafkaTopicProducerResponseProducers`]
        """
        
        super(ListTopicProducersResponse, self).__init__()

        self._total = None
        self._producers = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if producers is not None:
            self.producers = producers

    @property
    def total(self):
        """Gets the total of this ListTopicProducersResponse.

        总条数

        :return: The total of this ListTopicProducersResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListTopicProducersResponse.

        总条数

        :param total: The total of this ListTopicProducersResponse.
        :type total: int
        """
        self._total = total

    @property
    def producers(self):
        """Gets the producers of this ListTopicProducersResponse.

        生产者列表

        :return: The producers of this ListTopicProducersResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.KafkaTopicProducerResponseProducers`]
        """
        return self._producers

    @producers.setter
    def producers(self, producers):
        """Sets the producers of this ListTopicProducersResponse.

        生产者列表

        :param producers: The producers of this ListTopicProducersResponse.
        :type producers: list[:class:`huaweicloudsdkkafka.v2.KafkaTopicProducerResponseProducers`]
        """
        self._producers = producers

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
        if not isinstance(other, ListTopicProducersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
