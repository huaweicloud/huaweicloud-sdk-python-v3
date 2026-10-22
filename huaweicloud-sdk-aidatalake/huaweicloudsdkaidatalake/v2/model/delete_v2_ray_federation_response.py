# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteV2RayFederationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ray_federation_id': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'ray_federation_id': 'ray_federation_id',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, ray_federation_id=None, x_request_id=None):
        r"""DeleteV2RayFederationResponse

        The model defined in huaweicloud sdk

        :param ray_federation_id: **参数解释**：Ray联邦端点ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。
        :type ray_federation_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._ray_federation_id = None
        self._x_request_id = None
        self.discriminator = None

        if ray_federation_id is not None:
            self.ray_federation_id = ray_federation_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def ray_federation_id(self):
        r"""Gets the ray_federation_id of this DeleteV2RayFederationResponse.

        **参数解释**：Ray联邦端点ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。

        :return: The ray_federation_id of this DeleteV2RayFederationResponse.
        :rtype: str
        """
        return self._ray_federation_id

    @ray_federation_id.setter
    def ray_federation_id(self, ray_federation_id):
        r"""Sets the ray_federation_id of this DeleteV2RayFederationResponse.

        **参数解释**：Ray联邦端点ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。

        :param ray_federation_id: The ray_federation_id of this DeleteV2RayFederationResponse.
        :type ray_federation_id: str
        """
        self._ray_federation_id = ray_federation_id

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this DeleteV2RayFederationResponse.

        :return: The x_request_id of this DeleteV2RayFederationResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this DeleteV2RayFederationResponse.

        :param x_request_id: The x_request_id of this DeleteV2RayFederationResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("DeleteV2RayFederationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteV2RayFederationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
