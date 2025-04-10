# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInterRegionBandwidthRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inter_region_bandwidth': 'CreateInterRegionBandwidth'
    }

    attribute_map = {
        'inter_region_bandwidth': 'inter_region_bandwidth'
    }

    def __init__(self, inter_region_bandwidth=None):
        r"""CreateInterRegionBandwidthRequestBody

        The model defined in huaweicloud sdk

        :param inter_region_bandwidth: 
        :type inter_region_bandwidth: :class:`huaweicloudsdkcc.v3.CreateInterRegionBandwidth`
        """
        
        

        self._inter_region_bandwidth = None
        self.discriminator = None

        self.inter_region_bandwidth = inter_region_bandwidth

    @property
    def inter_region_bandwidth(self):
        r"""Gets the inter_region_bandwidth of this CreateInterRegionBandwidthRequestBody.

        :return: The inter_region_bandwidth of this CreateInterRegionBandwidthRequestBody.
        :rtype: :class:`huaweicloudsdkcc.v3.CreateInterRegionBandwidth`
        """
        return self._inter_region_bandwidth

    @inter_region_bandwidth.setter
    def inter_region_bandwidth(self, inter_region_bandwidth):
        r"""Sets the inter_region_bandwidth of this CreateInterRegionBandwidthRequestBody.

        :param inter_region_bandwidth: The inter_region_bandwidth of this CreateInterRegionBandwidthRequestBody.
        :type inter_region_bandwidth: :class:`huaweicloudsdkcc.v3.CreateInterRegionBandwidth`
        """
        self._inter_region_bandwidth = inter_region_bandwidth

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
        if not isinstance(other, CreateInterRegionBandwidthRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
