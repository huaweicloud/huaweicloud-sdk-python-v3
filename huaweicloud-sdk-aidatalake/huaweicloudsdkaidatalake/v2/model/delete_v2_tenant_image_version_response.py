# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteV2TenantImageVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_id': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'version_id': 'version_id',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, version_id=None, x_request_id=None):
        r"""DeleteV2TenantImageVersionResponse

        The model defined in huaweicloud sdk

        :param version_id: **参数解释**：镜像版本ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 
        :type version_id: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._version_id = None
        self._x_request_id = None
        self.discriminator = None

        if version_id is not None:
            self.version_id = version_id
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def version_id(self):
        r"""Gets the version_id of this DeleteV2TenantImageVersionResponse.

        **参数解释**：镜像版本ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 

        :return: The version_id of this DeleteV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this DeleteV2TenantImageVersionResponse.

        **参数解释**：镜像版本ID。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 

        :param version_id: The version_id of this DeleteV2TenantImageVersionResponse.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this DeleteV2TenantImageVersionResponse.

        :return: The x_request_id of this DeleteV2TenantImageVersionResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this DeleteV2TenantImageVersionResponse.

        :param x_request_id: The x_request_id of this DeleteV2TenantImageVersionResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("DeleteV2TenantImageVersionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteV2TenantImageVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
