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
        'quota': 'VpcQuotas',
        'request_id': 'str'
    }

    attribute_map = {
        'quota': 'quota',
        'request_id': 'request_id'
    }

    def __init__(self, quota=None, request_id=None):
        r"""ShowQuotaResponse

        The model defined in huaweicloud sdk

        :param quota: 
        :type quota: :class:`huaweicloudsdkvpc.v3.VpcQuotas`
        :param request_id: **参数解释**： 请求ID。 **取值范围**： 不涉及。
        :type request_id: str
        """
        
        super().__init__()

        self._quota = None
        self._request_id = None
        self.discriminator = None

        if quota is not None:
            self.quota = quota
        if request_id is not None:
            self.request_id = request_id

    @property
    def quota(self):
        r"""Gets the quota of this ShowQuotaResponse.

        :return: The quota of this ShowQuotaResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.VpcQuotas`
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ShowQuotaResponse.

        :param quota: The quota of this ShowQuotaResponse.
        :type quota: :class:`huaweicloudsdkvpc.v3.VpcQuotas`
        """
        self._quota = quota

    @property
    def request_id(self):
        r"""Gets the request_id of this ShowQuotaResponse.

        **参数解释**： 请求ID。 **取值范围**： 不涉及。

        :return: The request_id of this ShowQuotaResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ShowQuotaResponse.

        **参数解释**： 请求ID。 **取值范围**： 不涉及。

        :param request_id: The request_id of this ShowQuotaResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
