# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayAuthorizingClaimMatchValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'match_operator': 'str',
        'match_value': 'CoreGatewayMatchValue'
    }

    attribute_map = {
        'match_operator': 'match_operator',
        'match_value': 'match_value'
    }

    def __init__(self, match_operator=None, match_value=None):
        r"""CoreGatewayAuthorizingClaimMatchValue

        The model defined in huaweicloud sdk

        :param match_operator: 匹配操作符。
        :type match_operator: str
        :param match_value: 
        :type match_value: :class:`huaweicloudsdkagentarts.v1.CoreGatewayMatchValue`
        """
        
        

        self._match_operator = None
        self._match_value = None
        self.discriminator = None

        self.match_operator = match_operator
        self.match_value = match_value

    @property
    def match_operator(self):
        r"""Gets the match_operator of this CoreGatewayAuthorizingClaimMatchValue.

        匹配操作符。

        :return: The match_operator of this CoreGatewayAuthorizingClaimMatchValue.
        :rtype: str
        """
        return self._match_operator

    @match_operator.setter
    def match_operator(self, match_operator):
        r"""Sets the match_operator of this CoreGatewayAuthorizingClaimMatchValue.

        匹配操作符。

        :param match_operator: The match_operator of this CoreGatewayAuthorizingClaimMatchValue.
        :type match_operator: str
        """
        self._match_operator = match_operator

    @property
    def match_value(self):
        r"""Gets the match_value of this CoreGatewayAuthorizingClaimMatchValue.

        :return: The match_value of this CoreGatewayAuthorizingClaimMatchValue.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayMatchValue`
        """
        return self._match_value

    @match_value.setter
    def match_value(self, match_value):
        r"""Sets the match_value of this CoreGatewayAuthorizingClaimMatchValue.

        :param match_value: The match_value of this CoreGatewayAuthorizingClaimMatchValue.
        :type match_value: :class:`huaweicloudsdkagentarts.v1.CoreGatewayMatchValue`
        """
        self._match_value = match_value

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
        if not isinstance(other, CoreGatewayAuthorizingClaimMatchValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
