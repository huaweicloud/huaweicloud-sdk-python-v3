# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateBandwidthRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth': 'BatchCreateBandwidthOption'
    }

    attribute_map = {
        'bandwidth': 'bandwidth'
    }

    def __init__(self, bandwidth=None):
        r"""BatchCreateBandwidthRequestBody

        The model defined in huaweicloud sdk

        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkeip.v2.BatchCreateBandwidthOption`
        """
        
        

        self._bandwidth = None
        self.discriminator = None

        self.bandwidth = bandwidth

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this BatchCreateBandwidthRequestBody.

        :return: The bandwidth of this BatchCreateBandwidthRequestBody.
        :rtype: :class:`huaweicloudsdkeip.v2.BatchCreateBandwidthOption`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this BatchCreateBandwidthRequestBody.

        :param bandwidth: The bandwidth of this BatchCreateBandwidthRequestBody.
        :type bandwidth: :class:`huaweicloudsdkeip.v2.BatchCreateBandwidthOption`
        """
        self._bandwidth = bandwidth

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
        if not isinstance(other, BatchCreateBandwidthRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
