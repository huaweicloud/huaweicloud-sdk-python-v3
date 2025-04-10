# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOttChannelInfoResponse(SdkResponse):

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
        'channels': 'list[CreateOttChannelInfoReq]'
    }

    attribute_map = {
        'total': 'total',
        'channels': 'channels'
    }

    def __init__(self, total=None, channels=None):
        r"""ListOttChannelInfoResponse

        The model defined in huaweicloud sdk

        :param total: 总频道数
        :type total: int
        :param channels: 频道信息
        :type channels: list[:class:`huaweicloudsdklive.v1.CreateOttChannelInfoReq`]
        """
        
        super(ListOttChannelInfoResponse, self).__init__()

        self._total = None
        self._channels = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if channels is not None:
            self.channels = channels

    @property
    def total(self):
        r"""Gets the total of this ListOttChannelInfoResponse.

        总频道数

        :return: The total of this ListOttChannelInfoResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOttChannelInfoResponse.

        总频道数

        :param total: The total of this ListOttChannelInfoResponse.
        :type total: int
        """
        self._total = total

    @property
    def channels(self):
        r"""Gets the channels of this ListOttChannelInfoResponse.

        频道信息

        :return: The channels of this ListOttChannelInfoResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.CreateOttChannelInfoReq`]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        r"""Sets the channels of this ListOttChannelInfoResponse.

        频道信息

        :param channels: The channels of this ListOttChannelInfoResponse.
        :type channels: list[:class:`huaweicloudsdklive.v1.CreateOttChannelInfoReq`]
        """
        self._channels = channels

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
        if not isinstance(other, ListOttChannelInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
