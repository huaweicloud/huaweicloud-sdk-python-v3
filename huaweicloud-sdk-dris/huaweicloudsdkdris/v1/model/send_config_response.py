# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendConfigResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel': 'Channel',
        'target_list': 'TargetList'
    }

    attribute_map = {
        'channel': 'channel',
        'target_list': 'target_list'
    }

    def __init__(self, channel=None, target_list=None):
        """SendConfigResponse

        The model defined in huaweicloud sdk

        :param channel: 
        :type channel: :class:`huaweicloudsdkdris.v1.Channel`
        :param target_list: 
        :type target_list: :class:`huaweicloudsdkdris.v1.TargetList`
        """
        
        

        self._channel = None
        self._target_list = None
        self.discriminator = None

        if channel is not None:
            self.channel = channel
        if target_list is not None:
            self.target_list = target_list

    @property
    def channel(self):
        """Gets the channel of this SendConfigResponse.

        :return: The channel of this SendConfigResponse.
        :rtype: :class:`huaweicloudsdkdris.v1.Channel`
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this SendConfigResponse.

        :param channel: The channel of this SendConfigResponse.
        :type channel: :class:`huaweicloudsdkdris.v1.Channel`
        """
        self._channel = channel

    @property
    def target_list(self):
        """Gets the target_list of this SendConfigResponse.

        :return: The target_list of this SendConfigResponse.
        :rtype: :class:`huaweicloudsdkdris.v1.TargetList`
        """
        return self._target_list

    @target_list.setter
    def target_list(self, target_list):
        """Sets the target_list of this SendConfigResponse.

        :param target_list: The target_list of this SendConfigResponse.
        :type target_list: :class:`huaweicloudsdkdris.v1.TargetList`
        """
        self._target_list = target_list

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
        if not isinstance(other, SendConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
