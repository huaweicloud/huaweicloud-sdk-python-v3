# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGrowthRateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'growth_rate': 'float'
    }

    attribute_map = {
        'growth_rate': 'growth_rate'
    }

    def __init__(self, growth_rate=None):
        r"""ShowGrowthRateResponse

        The model defined in huaweicloud sdk

        :param growth_rate: 环比值。
        :type growth_rate: float
        """
        
        super(ShowGrowthRateResponse, self).__init__()

        self._growth_rate = None
        self.discriminator = None

        if growth_rate is not None:
            self.growth_rate = growth_rate

    @property
    def growth_rate(self):
        r"""Gets the growth_rate of this ShowGrowthRateResponse.

        环比值。

        :return: The growth_rate of this ShowGrowthRateResponse.
        :rtype: float
        """
        return self._growth_rate

    @growth_rate.setter
    def growth_rate(self, growth_rate):
        r"""Sets the growth_rate of this ShowGrowthRateResponse.

        环比值。

        :param growth_rate: The growth_rate of this ShowGrowthRateResponse.
        :type growth_rate: float
        """
        self._growth_rate = growth_rate

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
        if not isinstance(other, ShowGrowthRateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
