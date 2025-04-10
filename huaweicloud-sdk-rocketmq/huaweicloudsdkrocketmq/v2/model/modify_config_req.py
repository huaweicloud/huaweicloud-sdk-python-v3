# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyConfigReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rocketmq_configs': 'list[RocketMQConfigReq]'
    }

    attribute_map = {
        'rocketmq_configs': 'rocketmq_configs'
    }

    def __init__(self, rocketmq_configs=None):
        r"""ModifyConfigReq

        The model defined in huaweicloud sdk

        :param rocketmq_configs: RocketMQ配置。
        :type rocketmq_configs: list[:class:`huaweicloudsdkrocketmq.v2.RocketMQConfigReq`]
        """
        
        

        self._rocketmq_configs = None
        self.discriminator = None

        if rocketmq_configs is not None:
            self.rocketmq_configs = rocketmq_configs

    @property
    def rocketmq_configs(self):
        r"""Gets the rocketmq_configs of this ModifyConfigReq.

        RocketMQ配置。

        :return: The rocketmq_configs of this ModifyConfigReq.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.RocketMQConfigReq`]
        """
        return self._rocketmq_configs

    @rocketmq_configs.setter
    def rocketmq_configs(self, rocketmq_configs):
        r"""Sets the rocketmq_configs of this ModifyConfigReq.

        RocketMQ配置。

        :param rocketmq_configs: The rocketmq_configs of this ModifyConfigReq.
        :type rocketmq_configs: list[:class:`huaweicloudsdkrocketmq.v2.RocketMQConfigReq`]
        """
        self._rocketmq_configs = rocketmq_configs

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
        if not isinstance(other, ModifyConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
