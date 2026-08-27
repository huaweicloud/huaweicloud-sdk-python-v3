# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTenantUpgradeStrategyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'strategy_id': 'str',
        'body': 'UpdateTenantUpgradeStrategyRequestBody'
    }

    attribute_map = {
        'strategy_id': 'strategy_id',
        'body': 'body'
    }

    def __init__(self, strategy_id=None, body=None):
        r"""UpdateTenantUpgradeStrategyRequest

        The model defined in huaweicloud sdk

        :param strategy_id: 策略ID
        :type strategy_id: str
        :param body: Body of the UpdateTenantUpgradeStrategyRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.UpdateTenantUpgradeStrategyRequestBody`
        """
        
        

        self._strategy_id = None
        self._body = None
        self.discriminator = None

        self.strategy_id = strategy_id
        if body is not None:
            self.body = body

    @property
    def strategy_id(self):
        r"""Gets the strategy_id of this UpdateTenantUpgradeStrategyRequest.

        策略ID

        :return: The strategy_id of this UpdateTenantUpgradeStrategyRequest.
        :rtype: str
        """
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, strategy_id):
        r"""Sets the strategy_id of this UpdateTenantUpgradeStrategyRequest.

        策略ID

        :param strategy_id: The strategy_id of this UpdateTenantUpgradeStrategyRequest.
        :type strategy_id: str
        """
        self._strategy_id = strategy_id

    @property
    def body(self):
        r"""Gets the body of this UpdateTenantUpgradeStrategyRequest.

        :return: The body of this UpdateTenantUpgradeStrategyRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateTenantUpgradeStrategyRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateTenantUpgradeStrategyRequest.

        :param body: The body of this UpdateTenantUpgradeStrategyRequest.
        :type body: :class:`huaweicloudsdkworkspace.v2.UpdateTenantUpgradeStrategyRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateTenantUpgradeStrategyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
