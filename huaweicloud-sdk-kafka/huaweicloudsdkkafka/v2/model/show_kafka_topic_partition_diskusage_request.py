# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKafkaTopicPartitionDiskusageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'min_size': 'str',
        'top': 'str',
        'percentage': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'min_size': 'minSize',
        'top': 'top',
        'percentage': 'percentage'
    }

    def __init__(self, instance_id=None, min_size=None, top=None, percentage=None):
        r"""ShowKafkaTopicPartitionDiskusageRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param min_size: 占用磁盘大小，默认值1G (1K，1M，1G)。
        :type min_size: str
        :param top: **参数解释**： 占用磁盘大小，查询top N。 **约束限制**： 不涉及。 **取值范围**： 1~1000。 **默认取值**： 不涉及。
        :type top: str
        :param percentage: 占用磁盘大小，查询大于占比的分区。
        :type percentage: str
        """
        
        

        self._instance_id = None
        self._min_size = None
        self._top = None
        self._percentage = None
        self.discriminator = None

        self.instance_id = instance_id
        if min_size is not None:
            self.min_size = min_size
        if top is not None:
            self.top = top
        if percentage is not None:
            self.percentage = percentage

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowKafkaTopicPartitionDiskusageRequest.

        实例ID。

        :return: The instance_id of this ShowKafkaTopicPartitionDiskusageRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowKafkaTopicPartitionDiskusageRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowKafkaTopicPartitionDiskusageRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def min_size(self):
        r"""Gets the min_size of this ShowKafkaTopicPartitionDiskusageRequest.

        占用磁盘大小，默认值1G (1K，1M，1G)。

        :return: The min_size of this ShowKafkaTopicPartitionDiskusageRequest.
        :rtype: str
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        r"""Sets the min_size of this ShowKafkaTopicPartitionDiskusageRequest.

        占用磁盘大小，默认值1G (1K，1M，1G)。

        :param min_size: The min_size of this ShowKafkaTopicPartitionDiskusageRequest.
        :type min_size: str
        """
        self._min_size = min_size

    @property
    def top(self):
        r"""Gets the top of this ShowKafkaTopicPartitionDiskusageRequest.

        **参数解释**： 占用磁盘大小，查询top N。 **约束限制**： 不涉及。 **取值范围**： 1~1000。 **默认取值**： 不涉及。

        :return: The top of this ShowKafkaTopicPartitionDiskusageRequest.
        :rtype: str
        """
        return self._top

    @top.setter
    def top(self, top):
        r"""Sets the top of this ShowKafkaTopicPartitionDiskusageRequest.

        **参数解释**： 占用磁盘大小，查询top N。 **约束限制**： 不涉及。 **取值范围**： 1~1000。 **默认取值**： 不涉及。

        :param top: The top of this ShowKafkaTopicPartitionDiskusageRequest.
        :type top: str
        """
        self._top = top

    @property
    def percentage(self):
        r"""Gets the percentage of this ShowKafkaTopicPartitionDiskusageRequest.

        占用磁盘大小，查询大于占比的分区。

        :return: The percentage of this ShowKafkaTopicPartitionDiskusageRequest.
        :rtype: str
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        r"""Sets the percentage of this ShowKafkaTopicPartitionDiskusageRequest.

        占用磁盘大小，查询大于占比的分区。

        :param percentage: The percentage of this ShowKafkaTopicPartitionDiskusageRequest.
        :type percentage: str
        """
        self._percentage = percentage

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
        if not isinstance(other, ShowKafkaTopicPartitionDiskusageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
