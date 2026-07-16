# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDevServerPublicIPResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_ips': 'list[ServerPublicIp]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'public_ips': 'public_ips',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, public_ips=None, x_request_id=None):
        r"""ListDevServerPublicIPResponse

        The model defined in huaweicloud sdk

        :param public_ips: **参数解释**：EIP相关信息的数组。
        :type public_ips: list[:class:`huaweicloudsdkmodelarts.v1.ServerPublicIp`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._public_ips = None
        self._x_request_id = None
        self.discriminator = None

        if public_ips is not None:
            self.public_ips = public_ips
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def public_ips(self):
        r"""Gets the public_ips of this ListDevServerPublicIPResponse.

        **参数解释**：EIP相关信息的数组。

        :return: The public_ips of this ListDevServerPublicIPResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ServerPublicIp`]
        """
        return self._public_ips

    @public_ips.setter
    def public_ips(self, public_ips):
        r"""Sets the public_ips of this ListDevServerPublicIPResponse.

        **参数解释**：EIP相关信息的数组。

        :param public_ips: The public_ips of this ListDevServerPublicIPResponse.
        :type public_ips: list[:class:`huaweicloudsdkmodelarts.v1.ServerPublicIp`]
        """
        self._public_ips = public_ips

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListDevServerPublicIPResponse.

        :return: The x_request_id of this ListDevServerPublicIPResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListDevServerPublicIPResponse.

        :param x_request_id: The x_request_id of this ListDevServerPublicIPResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListDevServerPublicIPResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListDevServerPublicIPResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
