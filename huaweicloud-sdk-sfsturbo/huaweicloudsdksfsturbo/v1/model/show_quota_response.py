# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quotas': 'ShowQuotaResource',
        'x_request_id': 'str'
    }

    attribute_map = {
        'quotas': 'quotas',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, quotas=None, x_request_id=None):
        r"""ShowQuotaResponse

        The model defined in huaweicloud sdk

        :param quotas: 
        :type quotas: :class:`huaweicloudsdksfsturbo.v1.ShowQuotaResource`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._quotas = None
        self._x_request_id = None
        self.discriminator = None

        if quotas is not None:
            self.quotas = quotas
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def quotas(self):
        r"""Gets the quotas of this ShowQuotaResponse.

        :return: The quotas of this ShowQuotaResponse.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ShowQuotaResource`
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas):
        r"""Sets the quotas of this ShowQuotaResponse.

        :param quotas: The quotas of this ShowQuotaResponse.
        :type quotas: :class:`huaweicloudsdksfsturbo.v1.ShowQuotaResource`
        """
        self._quotas = quotas

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowQuotaResponse.

        :return: The x_request_id of this ShowQuotaResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowQuotaResponse.

        :param x_request_id: The x_request_id of this ShowQuotaResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowQuotaResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowQuotaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
