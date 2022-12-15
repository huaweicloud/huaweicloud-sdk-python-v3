# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteChannelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blockchain_id': 'str',
        'channel_id': 'str'
    }

    attribute_map = {
        'blockchain_id': 'blockchain_id',
        'channel_id': 'channel_id'
    }

    def __init__(self, blockchain_id=None, channel_id=None):
        """DeleteChannelRequest

        The model defined in huaweicloud sdk

        :param blockchain_id: 区块链服务id。可调用“查询服务实例列表”接口获取ID
        :type blockchain_id: str
        :param channel_id: 区块链通道名称。可调用“查询实例信息”接口获取，接口返回的“channels”中的name字段值
        :type channel_id: str
        """
        
        

        self._blockchain_id = None
        self._channel_id = None
        self.discriminator = None

        self.blockchain_id = blockchain_id
        self.channel_id = channel_id

    @property
    def blockchain_id(self):
        """Gets the blockchain_id of this DeleteChannelRequest.

        区块链服务id。可调用“查询服务实例列表”接口获取ID

        :return: The blockchain_id of this DeleteChannelRequest.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        """Sets the blockchain_id of this DeleteChannelRequest.

        区块链服务id。可调用“查询服务实例列表”接口获取ID

        :param blockchain_id: The blockchain_id of this DeleteChannelRequest.
        :type blockchain_id: str
        """
        self._blockchain_id = blockchain_id

    @property
    def channel_id(self):
        """Gets the channel_id of this DeleteChannelRequest.

        区块链通道名称。可调用“查询实例信息”接口获取，接口返回的“channels”中的name字段值

        :return: The channel_id of this DeleteChannelRequest.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this DeleteChannelRequest.

        区块链通道名称。可调用“查询实例信息”接口获取，接口返回的“channels”中的name字段值

        :param channel_id: The channel_id of this DeleteChannelRequest.
        :type channel_id: str
        """
        self._channel_id = channel_id

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
        if not isinstance(other, DeleteChannelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
