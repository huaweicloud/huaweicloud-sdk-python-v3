# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRocketMqConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'float',
        'next_offset': 'int',
        'previous_offset': 'int',
        'rocketmq_configs': 'list[RocketMQConfigResp]'
    }

    attribute_map = {
        'total': 'total',
        'next_offset': 'next_offset',
        'previous_offset': 'previous_offset',
        'rocketmq_configs': 'rocketmq_configs'
    }

    def __init__(self, total=None, next_offset=None, previous_offset=None, rocketmq_configs=None):
        r"""ShowRocketMqConfigsResponse

        The model defined in huaweicloud sdk

        :param total: 总数。
        :type total: float
        :param next_offset: 下个分页的offset。
        :type next_offset: int
        :param previous_offset: 上个分页的offset。
        :type previous_offset: int
        :param rocketmq_configs: RocketMQ配置。
        :type rocketmq_configs: list[:class:`huaweicloudsdkrocketmq.v2.RocketMQConfigResp`]
        """
        
        super(ShowRocketMqConfigsResponse, self).__init__()

        self._total = None
        self._next_offset = None
        self._previous_offset = None
        self._rocketmq_configs = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if next_offset is not None:
            self.next_offset = next_offset
        if previous_offset is not None:
            self.previous_offset = previous_offset
        if rocketmq_configs is not None:
            self.rocketmq_configs = rocketmq_configs

    @property
    def total(self):
        r"""Gets the total of this ShowRocketMqConfigsResponse.

        总数。

        :return: The total of this ShowRocketMqConfigsResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowRocketMqConfigsResponse.

        总数。

        :param total: The total of this ShowRocketMqConfigsResponse.
        :type total: float
        """
        self._total = total

    @property
    def next_offset(self):
        r"""Gets the next_offset of this ShowRocketMqConfigsResponse.

        下个分页的offset。

        :return: The next_offset of this ShowRocketMqConfigsResponse.
        :rtype: int
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        r"""Sets the next_offset of this ShowRocketMqConfigsResponse.

        下个分页的offset。

        :param next_offset: The next_offset of this ShowRocketMqConfigsResponse.
        :type next_offset: int
        """
        self._next_offset = next_offset

    @property
    def previous_offset(self):
        r"""Gets the previous_offset of this ShowRocketMqConfigsResponse.

        上个分页的offset。

        :return: The previous_offset of this ShowRocketMqConfigsResponse.
        :rtype: int
        """
        return self._previous_offset

    @previous_offset.setter
    def previous_offset(self, previous_offset):
        r"""Sets the previous_offset of this ShowRocketMqConfigsResponse.

        上个分页的offset。

        :param previous_offset: The previous_offset of this ShowRocketMqConfigsResponse.
        :type previous_offset: int
        """
        self._previous_offset = previous_offset

    @property
    def rocketmq_configs(self):
        r"""Gets the rocketmq_configs of this ShowRocketMqConfigsResponse.

        RocketMQ配置。

        :return: The rocketmq_configs of this ShowRocketMqConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.RocketMQConfigResp`]
        """
        return self._rocketmq_configs

    @rocketmq_configs.setter
    def rocketmq_configs(self, rocketmq_configs):
        r"""Sets the rocketmq_configs of this ShowRocketMqConfigsResponse.

        RocketMQ配置。

        :param rocketmq_configs: The rocketmq_configs of this ShowRocketMqConfigsResponse.
        :type rocketmq_configs: list[:class:`huaweicloudsdkrocketmq.v2.RocketMQConfigResp`]
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
        if not isinstance(other, ShowRocketMqConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
