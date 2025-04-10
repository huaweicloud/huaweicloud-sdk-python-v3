# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBandwidthInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_bandwidths': 'list[UpdateGroupBandwidthInfoRequest]'
    }

    attribute_map = {
        'group_bandwidths': 'group_bandwidths'
    }

    def __init__(self, group_bandwidths=None):
        r"""UpdateBandwidthInfoRequest

        The model defined in huaweicloud sdk

        :param group_bandwidths: 分片带宽列表。
        :type group_bandwidths: list[:class:`huaweicloudsdkdcs.v2.UpdateGroupBandwidthInfoRequest`]
        """
        
        

        self._group_bandwidths = None
        self.discriminator = None

        if group_bandwidths is not None:
            self.group_bandwidths = group_bandwidths

    @property
    def group_bandwidths(self):
        r"""Gets the group_bandwidths of this UpdateBandwidthInfoRequest.

        分片带宽列表。

        :return: The group_bandwidths of this UpdateBandwidthInfoRequest.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.UpdateGroupBandwidthInfoRequest`]
        """
        return self._group_bandwidths

    @group_bandwidths.setter
    def group_bandwidths(self, group_bandwidths):
        r"""Sets the group_bandwidths of this UpdateBandwidthInfoRequest.

        分片带宽列表。

        :param group_bandwidths: The group_bandwidths of this UpdateBandwidthInfoRequest.
        :type group_bandwidths: list[:class:`huaweicloudsdkdcs.v2.UpdateGroupBandwidthInfoRequest`]
        """
        self._group_bandwidths = group_bandwidths

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
        if not isinstance(other, UpdateBandwidthInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
