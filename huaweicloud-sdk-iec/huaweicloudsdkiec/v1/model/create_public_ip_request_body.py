# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePublicIpRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip': 'CreatePublicIpOption',
        'bandwidth': 'CreatePublicIpBandwidthOption'
    }

    attribute_map = {
        'publicip': 'publicip',
        'bandwidth': 'bandwidth'
    }

    def __init__(self, publicip=None, bandwidth=None):
        r"""CreatePublicIpRequestBody

        The model defined in huaweicloud sdk

        :param publicip: 
        :type publicip: :class:`huaweicloudsdkiec.v1.CreatePublicIpOption`
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkiec.v1.CreatePublicIpBandwidthOption`
        """
        
        

        self._publicip = None
        self._bandwidth = None
        self.discriminator = None

        self.publicip = publicip
        if bandwidth is not None:
            self.bandwidth = bandwidth

    @property
    def publicip(self):
        r"""Gets the publicip of this CreatePublicIpRequestBody.

        :return: The publicip of this CreatePublicIpRequestBody.
        :rtype: :class:`huaweicloudsdkiec.v1.CreatePublicIpOption`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        r"""Sets the publicip of this CreatePublicIpRequestBody.

        :param publicip: The publicip of this CreatePublicIpRequestBody.
        :type publicip: :class:`huaweicloudsdkiec.v1.CreatePublicIpOption`
        """
        self._publicip = publicip

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this CreatePublicIpRequestBody.

        :return: The bandwidth of this CreatePublicIpRequestBody.
        :rtype: :class:`huaweicloudsdkiec.v1.CreatePublicIpBandwidthOption`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this CreatePublicIpRequestBody.

        :param bandwidth: The bandwidth of this CreatePublicIpRequestBody.
        :type bandwidth: :class:`huaweicloudsdkiec.v1.CreatePublicIpBandwidthOption`
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
        if not isinstance(other, CreatePublicIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
