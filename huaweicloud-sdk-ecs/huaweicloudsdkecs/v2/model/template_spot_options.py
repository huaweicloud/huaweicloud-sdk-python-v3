# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateSpotOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spot_price': 'float',
        'block_duration_minutes': 'int',
        'instance_interruption_behavior': 'str'
    }

    attribute_map = {
        'spot_price': 'spot_price',
        'block_duration_minutes': 'block_duration_minutes',
        'instance_interruption_behavior': 'instance_interruption_behavior'
    }

    def __init__(self, spot_price=None, block_duration_minutes=None, instance_interruption_behavior=None):
        r"""TemplateSpotOptions

        The model defined in huaweicloud sdk

        :param spot_price: 用户愿意为竞价实例每小时支付的最高价格
        :type spot_price: float
        :param block_duration_minutes: 购买的竞价实例时长
        :type block_duration_minutes: int
        :param instance_interruption_behavior: 竞价实例中断策略，当前支持immediate
        :type instance_interruption_behavior: str
        """
        
        

        self._spot_price = None
        self._block_duration_minutes = None
        self._instance_interruption_behavior = None
        self.discriminator = None

        if spot_price is not None:
            self.spot_price = spot_price
        if block_duration_minutes is not None:
            self.block_duration_minutes = block_duration_minutes
        if instance_interruption_behavior is not None:
            self.instance_interruption_behavior = instance_interruption_behavior

    @property
    def spot_price(self):
        r"""Gets the spot_price of this TemplateSpotOptions.

        用户愿意为竞价实例每小时支付的最高价格

        :return: The spot_price of this TemplateSpotOptions.
        :rtype: float
        """
        return self._spot_price

    @spot_price.setter
    def spot_price(self, spot_price):
        r"""Sets the spot_price of this TemplateSpotOptions.

        用户愿意为竞价实例每小时支付的最高价格

        :param spot_price: The spot_price of this TemplateSpotOptions.
        :type spot_price: float
        """
        self._spot_price = spot_price

    @property
    def block_duration_minutes(self):
        r"""Gets the block_duration_minutes of this TemplateSpotOptions.

        购买的竞价实例时长

        :return: The block_duration_minutes of this TemplateSpotOptions.
        :rtype: int
        """
        return self._block_duration_minutes

    @block_duration_minutes.setter
    def block_duration_minutes(self, block_duration_minutes):
        r"""Sets the block_duration_minutes of this TemplateSpotOptions.

        购买的竞价实例时长

        :param block_duration_minutes: The block_duration_minutes of this TemplateSpotOptions.
        :type block_duration_minutes: int
        """
        self._block_duration_minutes = block_duration_minutes

    @property
    def instance_interruption_behavior(self):
        r"""Gets the instance_interruption_behavior of this TemplateSpotOptions.

        竞价实例中断策略，当前支持immediate

        :return: The instance_interruption_behavior of this TemplateSpotOptions.
        :rtype: str
        """
        return self._instance_interruption_behavior

    @instance_interruption_behavior.setter
    def instance_interruption_behavior(self, instance_interruption_behavior):
        r"""Sets the instance_interruption_behavior of this TemplateSpotOptions.

        竞价实例中断策略，当前支持immediate

        :param instance_interruption_behavior: The instance_interruption_behavior of this TemplateSpotOptions.
        :type instance_interruption_behavior: str
        """
        self._instance_interruption_behavior = instance_interruption_behavior

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
        if not isinstance(other, TemplateSpotOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
