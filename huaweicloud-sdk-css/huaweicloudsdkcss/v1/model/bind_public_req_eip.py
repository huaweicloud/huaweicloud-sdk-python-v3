# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindPublicReqEip:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'band_width': 'BindPublicReqEipBandWidth'
    }

    attribute_map = {
        'band_width': 'bandWidth'
    }

    def __init__(self, band_width=None):
        r"""BindPublicReqEip

        The model defined in huaweicloud sdk

        :param band_width: 
        :type band_width: :class:`huaweicloudsdkcss.v1.BindPublicReqEipBandWidth`
        """
        
        

        self._band_width = None
        self.discriminator = None

        self.band_width = band_width

    @property
    def band_width(self):
        r"""Gets the band_width of this BindPublicReqEip.

        :return: The band_width of this BindPublicReqEip.
        :rtype: :class:`huaweicloudsdkcss.v1.BindPublicReqEipBandWidth`
        """
        return self._band_width

    @band_width.setter
    def band_width(self, band_width):
        r"""Sets the band_width of this BindPublicReqEip.

        :param band_width: The band_width of this BindPublicReqEip.
        :type band_width: :class:`huaweicloudsdkcss.v1.BindPublicReqEipBandWidth`
        """
        self._band_width = band_width

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
        if not isinstance(other, BindPublicReqEip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
