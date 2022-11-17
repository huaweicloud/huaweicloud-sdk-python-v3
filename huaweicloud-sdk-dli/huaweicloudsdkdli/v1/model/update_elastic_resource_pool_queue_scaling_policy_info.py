# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateElasticResourcePoolQueueScalingPolicyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_scaling_policies': 'list[QueueScalingPolicyInfo]'
    }

    attribute_map = {
        'queue_scaling_policies': 'queue_scaling_policies'
    }

    def __init__(self, queue_scaling_policies=None):
        """UpdateElasticResourcePoolQueueScalingPolicyInfo

        The model defined in huaweicloud sdk

        :param queue_scaling_policies: 该队列在该弹性资源池下的扩缩容策略信息。单条策略信息包含时间段、优先级和CU范围。每个队列至少要配置一条时间段为[00:00, 24:00]的默认扩缩容策略。
        :type queue_scaling_policies: list[:class:`huaweicloudsdkdli.v1.QueueScalingPolicyInfo`]
        """
        
        

        self._queue_scaling_policies = None
        self.discriminator = None

        self.queue_scaling_policies = queue_scaling_policies

    @property
    def queue_scaling_policies(self):
        """Gets the queue_scaling_policies of this UpdateElasticResourcePoolQueueScalingPolicyInfo.

        该队列在该弹性资源池下的扩缩容策略信息。单条策略信息包含时间段、优先级和CU范围。每个队列至少要配置一条时间段为[00:00, 24:00]的默认扩缩容策略。

        :return: The queue_scaling_policies of this UpdateElasticResourcePoolQueueScalingPolicyInfo.
        :rtype: list[:class:`huaweicloudsdkdli.v1.QueueScalingPolicyInfo`]
        """
        return self._queue_scaling_policies

    @queue_scaling_policies.setter
    def queue_scaling_policies(self, queue_scaling_policies):
        """Sets the queue_scaling_policies of this UpdateElasticResourcePoolQueueScalingPolicyInfo.

        该队列在该弹性资源池下的扩缩容策略信息。单条策略信息包含时间段、优先级和CU范围。每个队列至少要配置一条时间段为[00:00, 24:00]的默认扩缩容策略。

        :param queue_scaling_policies: The queue_scaling_policies of this UpdateElasticResourcePoolQueueScalingPolicyInfo.
        :type queue_scaling_policies: list[:class:`huaweicloudsdkdli.v1.QueueScalingPolicyInfo`]
        """
        self._queue_scaling_policies = queue_scaling_policies

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
        if not isinstance(other, UpdateElasticResourcePoolQueueScalingPolicyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
