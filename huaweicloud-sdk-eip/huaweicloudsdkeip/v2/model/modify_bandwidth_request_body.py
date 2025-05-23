# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyBandwidthRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidths': 'list[ModifyBandwidthOption]'
    }

    attribute_map = {
        'bandwidths': 'bandwidths'
    }

    def __init__(self, bandwidths=None):
        r"""ModifyBandwidthRequestBody

        The model defined in huaweicloud sdk

        :param bandwidths: 更新带宽列表
        :type bandwidths: list[:class:`huaweicloudsdkeip.v2.ModifyBandwidthOption`]
        """
        
        

        self._bandwidths = None
        self.discriminator = None

        self.bandwidths = bandwidths

    @property
    def bandwidths(self):
        r"""Gets the bandwidths of this ModifyBandwidthRequestBody.

        更新带宽列表

        :return: The bandwidths of this ModifyBandwidthRequestBody.
        :rtype: list[:class:`huaweicloudsdkeip.v2.ModifyBandwidthOption`]
        """
        return self._bandwidths

    @bandwidths.setter
    def bandwidths(self, bandwidths):
        r"""Sets the bandwidths of this ModifyBandwidthRequestBody.

        更新带宽列表

        :param bandwidths: The bandwidths of this ModifyBandwidthRequestBody.
        :type bandwidths: list[:class:`huaweicloudsdkeip.v2.ModifyBandwidthOption`]
        """
        self._bandwidths = bandwidths

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
        if not isinstance(other, ModifyBandwidthRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
