# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNatGatewaySpecsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'specs': 'list[str]'
    }

    attribute_map = {
        'specs': 'specs'
    }

    def __init__(self, specs=None):
        r"""ListNatGatewaySpecsResponse

        The model defined in huaweicloud sdk

        :param specs: 可创建的NAT网关实例列表  取值范围：  “1”：小型，SNAT最大连接数10000  “2”：中型，SNAT最大连接数50000  “3”：大型，SNAT最大连接数200000  “4”：超大型，SNAT最大连接数1000000  “5”：企业型，SNAT最大连接数10000000 
        :type specs: list[str]
        """
        
        super().__init__()

        self._specs = None
        self.discriminator = None

        if specs is not None:
            self.specs = specs

    @property
    def specs(self):
        r"""Gets the specs of this ListNatGatewaySpecsResponse.

        可创建的NAT网关实例列表  取值范围：  “1”：小型，SNAT最大连接数10000  “2”：中型，SNAT最大连接数50000  “3”：大型，SNAT最大连接数200000  “4”：超大型，SNAT最大连接数1000000  “5”：企业型，SNAT最大连接数10000000 

        :return: The specs of this ListNatGatewaySpecsResponse.
        :rtype: list[str]
        """
        return self._specs

    @specs.setter
    def specs(self, specs):
        r"""Sets the specs of this ListNatGatewaySpecsResponse.

        可创建的NAT网关实例列表  取值范围：  “1”：小型，SNAT最大连接数10000  “2”：中型，SNAT最大连接数50000  “3”：大型，SNAT最大连接数200000  “4”：超大型，SNAT最大连接数1000000  “5”：企业型，SNAT最大连接数10000000 

        :param specs: The specs of this ListNatGatewaySpecsResponse.
        :type specs: list[str]
        """
        self._specs = specs

    def to_dict(self):
        import warnings
        warnings.warn("ListNatGatewaySpecsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListNatGatewaySpecsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
