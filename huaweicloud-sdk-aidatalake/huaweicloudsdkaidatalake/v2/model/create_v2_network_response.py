# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateV2NetworkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'vpc_cidr': 'str'
    }

    attribute_map = {
        'id': 'id',
        'vpc_cidr': 'vpc_cidr'
    }

    def __init__(self, id=None, vpc_cidr=None):
        r"""CreateV2NetworkResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**：网络连接的ID。 **取值范围**：长度为1~64的英文、数字、中划线组合。 
        :type id: str
        :param vpc_cidr: **参数解释**：路由网段范围，标准的IPv4格式。 **取值范围**：允许网段为10.0.0.0~10.255.0.0/8~22,172.16.0.0~172.31.0.0/12~22,192.168.0.0~192.168.0.0/16~22。 
        :type vpc_cidr: str
        """
        
        super().__init__()

        self._id = None
        self._vpc_cidr = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vpc_cidr is not None:
            self.vpc_cidr = vpc_cidr

    @property
    def id(self):
        r"""Gets the id of this CreateV2NetworkResponse.

        **参数解释**：网络连接的ID。 **取值范围**：长度为1~64的英文、数字、中划线组合。 

        :return: The id of this CreateV2NetworkResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateV2NetworkResponse.

        **参数解释**：网络连接的ID。 **取值范围**：长度为1~64的英文、数字、中划线组合。 

        :param id: The id of this CreateV2NetworkResponse.
        :type id: str
        """
        self._id = id

    @property
    def vpc_cidr(self):
        r"""Gets the vpc_cidr of this CreateV2NetworkResponse.

        **参数解释**：路由网段范围，标准的IPv4格式。 **取值范围**：允许网段为10.0.0.0~10.255.0.0/8~22,172.16.0.0~172.31.0.0/12~22,192.168.0.0~192.168.0.0/16~22。 

        :return: The vpc_cidr of this CreateV2NetworkResponse.
        :rtype: str
        """
        return self._vpc_cidr

    @vpc_cidr.setter
    def vpc_cidr(self, vpc_cidr):
        r"""Sets the vpc_cidr of this CreateV2NetworkResponse.

        **参数解释**：路由网段范围，标准的IPv4格式。 **取值范围**：允许网段为10.0.0.0~10.255.0.0/8~22,172.16.0.0~172.31.0.0/12~22,192.168.0.0~192.168.0.0/16~22。 

        :param vpc_cidr: The vpc_cidr of this CreateV2NetworkResponse.
        :type vpc_cidr: str
        """
        self._vpc_cidr = vpc_cidr

    def to_dict(self):
        import warnings
        warnings.warn("CreateV2NetworkResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateV2NetworkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
