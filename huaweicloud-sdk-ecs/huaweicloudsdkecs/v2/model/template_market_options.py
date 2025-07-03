# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateMarketOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'market_type': 'str',
        'spot_options': 'TemplateSpotOptions'
    }

    attribute_map = {
        'market_type': 'market_type',
        'spot_options': 'spot_options'
    }

    def __init__(self, market_type=None, spot_options=None):
        r"""TemplateMarketOptions

        The model defined in huaweicloud sdk

        :param market_type: 计费类型
        :type market_type: str
        :param spot_options: 
        :type spot_options: :class:`huaweicloudsdkecs.v2.TemplateSpotOptions`
        """
        
        

        self._market_type = None
        self._spot_options = None
        self.discriminator = None

        if market_type is not None:
            self.market_type = market_type
        if spot_options is not None:
            self.spot_options = spot_options

    @property
    def market_type(self):
        r"""Gets the market_type of this TemplateMarketOptions.

        计费类型

        :return: The market_type of this TemplateMarketOptions.
        :rtype: str
        """
        return self._market_type

    @market_type.setter
    def market_type(self, market_type):
        r"""Sets the market_type of this TemplateMarketOptions.

        计费类型

        :param market_type: The market_type of this TemplateMarketOptions.
        :type market_type: str
        """
        self._market_type = market_type

    @property
    def spot_options(self):
        r"""Gets the spot_options of this TemplateMarketOptions.

        :return: The spot_options of this TemplateMarketOptions.
        :rtype: :class:`huaweicloudsdkecs.v2.TemplateSpotOptions`
        """
        return self._spot_options

    @spot_options.setter
    def spot_options(self, spot_options):
        r"""Sets the spot_options of this TemplateMarketOptions.

        :param spot_options: The spot_options of this TemplateMarketOptions.
        :type spot_options: :class:`huaweicloudsdkecs.v2.TemplateSpotOptions`
        """
        self._spot_options = spot_options

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
        if not isinstance(other, TemplateMarketOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
