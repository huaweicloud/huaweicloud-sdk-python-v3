# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateV2NetworkRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cidr_in_vpc': 'str'
    }

    attribute_map = {
        'cidr_in_vpc': 'cidr_in_vpc'
    }

    def __init__(self, cidr_in_vpc=None):
        r"""CreateV2NetworkRequestBody

        The model defined in huaweicloud sdk

        :param cidr_in_vpc: **参数解释**：路由网段范围，标准的IPv4格式。 **取值范围**：允许网段为10.0.0.0~10.255.0.0/8~22,172.16.0.0~172.31.0.0/12~22,192.168.0.0~192.168.0.0/16~22。 
        :type cidr_in_vpc: str
        """
        
        

        self._cidr_in_vpc = None
        self.discriminator = None

        if cidr_in_vpc is not None:
            self.cidr_in_vpc = cidr_in_vpc

    @property
    def cidr_in_vpc(self):
        r"""Gets the cidr_in_vpc of this CreateV2NetworkRequestBody.

        **参数解释**：路由网段范围，标准的IPv4格式。 **取值范围**：允许网段为10.0.0.0~10.255.0.0/8~22,172.16.0.0~172.31.0.0/12~22,192.168.0.0~192.168.0.0/16~22。 

        :return: The cidr_in_vpc of this CreateV2NetworkRequestBody.
        :rtype: str
        """
        return self._cidr_in_vpc

    @cidr_in_vpc.setter
    def cidr_in_vpc(self, cidr_in_vpc):
        r"""Sets the cidr_in_vpc of this CreateV2NetworkRequestBody.

        **参数解释**：路由网段范围，标准的IPv4格式。 **取值范围**：允许网段为10.0.0.0~10.255.0.0/8~22,172.16.0.0~172.31.0.0/12~22,192.168.0.0~192.168.0.0/16~22。 

        :param cidr_in_vpc: The cidr_in_vpc of this CreateV2NetworkRequestBody.
        :type cidr_in_vpc: str
        """
        self._cidr_in_vpc = cidr_in_vpc

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
        if not isinstance(other, CreateV2NetworkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
