# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrackerConfigBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel': 'ChannelConfigBody',
        'selector': 'SelectorConfigBody',
        'agency_name': 'str'
    }

    attribute_map = {
        'channel': 'channel',
        'selector': 'selector',
        'agency_name': 'agency_name'
    }

    def __init__(self, channel=None, selector=None, agency_name=None):
        """TrackerConfigBody

        The model defined in huaweicloud sdk

        :param channel: 
        :type channel: :class:`huaweicloudsdkrms.v1.ChannelConfigBody`
        :param selector: 
        :type selector: :class:`huaweicloudsdkrms.v1.SelectorConfigBody`
        :param agency_name: IAM委托名称
        :type agency_name: str
        """
        
        

        self._channel = None
        self._selector = None
        self._agency_name = None
        self.discriminator = None

        self.channel = channel
        self.selector = selector
        self.agency_name = agency_name

    @property
    def channel(self):
        """Gets the channel of this TrackerConfigBody.

        :return: The channel of this TrackerConfigBody.
        :rtype: :class:`huaweicloudsdkrms.v1.ChannelConfigBody`
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this TrackerConfigBody.

        :param channel: The channel of this TrackerConfigBody.
        :type channel: :class:`huaweicloudsdkrms.v1.ChannelConfigBody`
        """
        self._channel = channel

    @property
    def selector(self):
        """Gets the selector of this TrackerConfigBody.

        :return: The selector of this TrackerConfigBody.
        :rtype: :class:`huaweicloudsdkrms.v1.SelectorConfigBody`
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this TrackerConfigBody.

        :param selector: The selector of this TrackerConfigBody.
        :type selector: :class:`huaweicloudsdkrms.v1.SelectorConfigBody`
        """
        self._selector = selector

    @property
    def agency_name(self):
        """Gets the agency_name of this TrackerConfigBody.

        IAM委托名称

        :return: The agency_name of this TrackerConfigBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this TrackerConfigBody.

        IAM委托名称

        :param agency_name: The agency_name of this TrackerConfigBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

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
        if not isinstance(other, TrackerConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
