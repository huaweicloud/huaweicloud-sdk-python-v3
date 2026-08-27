# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTenantUpgradeStrategyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'strategy_ids': 'list[str]'
    }

    attribute_map = {
        'strategy_ids': 'strategy_ids'
    }

    def __init__(self, strategy_ids=None):
        r"""DeleteTenantUpgradeStrategyRequestBody

        The model defined in huaweicloud sdk

        :param strategy_ids: 策略ID列表
        :type strategy_ids: list[str]
        """
        
        

        self._strategy_ids = None
        self.discriminator = None

        if strategy_ids is not None:
            self.strategy_ids = strategy_ids

    @property
    def strategy_ids(self):
        r"""Gets the strategy_ids of this DeleteTenantUpgradeStrategyRequestBody.

        策略ID列表

        :return: The strategy_ids of this DeleteTenantUpgradeStrategyRequestBody.
        :rtype: list[str]
        """
        return self._strategy_ids

    @strategy_ids.setter
    def strategy_ids(self, strategy_ids):
        r"""Sets the strategy_ids of this DeleteTenantUpgradeStrategyRequestBody.

        策略ID列表

        :param strategy_ids: The strategy_ids of this DeleteTenantUpgradeStrategyRequestBody.
        :type strategy_ids: list[str]
        """
        self._strategy_ids = strategy_ids

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteTenantUpgradeStrategyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
