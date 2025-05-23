# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDetachInternetBandwidthsGlobalEipRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'global_eips': 'list[object]'
    }

    attribute_map = {
        'global_eips': 'global_eips'
    }

    def __init__(self, global_eips=None):
        r"""BatchDetachInternetBandwidthsGlobalEipRequestBody

        The model defined in huaweicloud sdk

        :param global_eips: 批量解绑全域公网带宽请求体对象
        :type global_eips: list[object]
        """
        
        

        self._global_eips = None
        self.discriminator = None

        self.global_eips = global_eips

    @property
    def global_eips(self):
        r"""Gets the global_eips of this BatchDetachInternetBandwidthsGlobalEipRequestBody.

        批量解绑全域公网带宽请求体对象

        :return: The global_eips of this BatchDetachInternetBandwidthsGlobalEipRequestBody.
        :rtype: list[object]
        """
        return self._global_eips

    @global_eips.setter
    def global_eips(self, global_eips):
        r"""Sets the global_eips of this BatchDetachInternetBandwidthsGlobalEipRequestBody.

        批量解绑全域公网带宽请求体对象

        :param global_eips: The global_eips of this BatchDetachInternetBandwidthsGlobalEipRequestBody.
        :type global_eips: list[object]
        """
        self._global_eips = global_eips

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
        if not isinstance(other, BatchDetachInternetBandwidthsGlobalEipRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
