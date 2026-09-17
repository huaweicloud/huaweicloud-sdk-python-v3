# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRiskInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risks': 'list[ShowRiskInfoEngineRiskDesc]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'risks': 'risks',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, risks=None, x_request_id=None):
        r"""ShowRiskInfoResponse

        The model defined in huaweicloud sdk

        :param risks: 风险版本信息
        :type risks: list[:class:`huaweicloudsdkrds.v3.ShowRiskInfoEngineRiskDesc`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._risks = None
        self._x_request_id = None
        self.discriminator = None

        if risks is not None:
            self.risks = risks
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def risks(self):
        r"""Gets the risks of this ShowRiskInfoResponse.

        风险版本信息

        :return: The risks of this ShowRiskInfoResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ShowRiskInfoEngineRiskDesc`]
        """
        return self._risks

    @risks.setter
    def risks(self, risks):
        r"""Sets the risks of this ShowRiskInfoResponse.

        风险版本信息

        :param risks: The risks of this ShowRiskInfoResponse.
        :type risks: list[:class:`huaweicloudsdkrds.v3.ShowRiskInfoEngineRiskDesc`]
        """
        self._risks = risks

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowRiskInfoResponse.

        :return: The x_request_id of this ShowRiskInfoResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowRiskInfoResponse.

        :param x_request_id: The x_request_id of this ShowRiskInfoResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowRiskInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowRiskInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
