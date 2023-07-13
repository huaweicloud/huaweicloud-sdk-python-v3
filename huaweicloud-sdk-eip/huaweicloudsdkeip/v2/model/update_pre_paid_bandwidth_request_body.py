# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePrePaidBandwidthRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth': 'UpdatePrePaidBandwidthOption',
        'extend_param': 'UpdatePrePaidBandwidthExtendParamOption'
    }

    attribute_map = {
        'bandwidth': 'bandwidth',
        'extend_param': 'extendParam'
    }

    def __init__(self, bandwidth=None, extend_param=None):
        """UpdatePrePaidBandwidthRequestBody

        The model defined in huaweicloud sdk

        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthOption`
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthExtendParamOption`
        """
        
        

        self._bandwidth = None
        self._extend_param = None
        self.discriminator = None

        self.bandwidth = bandwidth
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def bandwidth(self):
        """Gets the bandwidth of this UpdatePrePaidBandwidthRequestBody.

        :return: The bandwidth of this UpdatePrePaidBandwidthRequestBody.
        :rtype: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthOption`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this UpdatePrePaidBandwidthRequestBody.

        :param bandwidth: The bandwidth of this UpdatePrePaidBandwidthRequestBody.
        :type bandwidth: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthOption`
        """
        self._bandwidth = bandwidth

    @property
    def extend_param(self):
        """Gets the extend_param of this UpdatePrePaidBandwidthRequestBody.

        :return: The extend_param of this UpdatePrePaidBandwidthRequestBody.
        :rtype: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthExtendParamOption`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this UpdatePrePaidBandwidthRequestBody.

        :param extend_param: The extend_param of this UpdatePrePaidBandwidthRequestBody.
        :type extend_param: :class:`huaweicloudsdkeip.v2.UpdatePrePaidBandwidthExtendParamOption`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, UpdatePrePaidBandwidthRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
