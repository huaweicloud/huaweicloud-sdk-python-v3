# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRealNameAuthStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'verified_status': 'int',
        'verified_type': 'int'
    }

    attribute_map = {
        'verified_status': 'verified_status',
        'verified_type': 'verified_type'
    }

    def __init__(self, verified_status=None, verified_type=None):
        r"""ShowRealNameAuthStatusResponse

        The model defined in huaweicloud sdk

        :param verified_status: 实名认证状态。enum:-1,0,1,2。 -1未实名认证、0实名认证审核中、1实名认证不通过、2已实名认证
        :type verified_status: int
        :param verified_type: 实名认证类型。实名认证状态为-1未实名认证返回null。enum:0,1。 0个人实名认证、1企业实名认证
        :type verified_type: int
        """
        
        super().__init__()

        self._verified_status = None
        self._verified_type = None
        self.discriminator = None

        if verified_status is not None:
            self.verified_status = verified_status
        if verified_type is not None:
            self.verified_type = verified_type

    @property
    def verified_status(self):
        r"""Gets the verified_status of this ShowRealNameAuthStatusResponse.

        实名认证状态。enum:-1,0,1,2。 -1未实名认证、0实名认证审核中、1实名认证不通过、2已实名认证

        :return: The verified_status of this ShowRealNameAuthStatusResponse.
        :rtype: int
        """
        return self._verified_status

    @verified_status.setter
    def verified_status(self, verified_status):
        r"""Sets the verified_status of this ShowRealNameAuthStatusResponse.

        实名认证状态。enum:-1,0,1,2。 -1未实名认证、0实名认证审核中、1实名认证不通过、2已实名认证

        :param verified_status: The verified_status of this ShowRealNameAuthStatusResponse.
        :type verified_status: int
        """
        self._verified_status = verified_status

    @property
    def verified_type(self):
        r"""Gets the verified_type of this ShowRealNameAuthStatusResponse.

        实名认证类型。实名认证状态为-1未实名认证返回null。enum:0,1。 0个人实名认证、1企业实名认证

        :return: The verified_type of this ShowRealNameAuthStatusResponse.
        :rtype: int
        """
        return self._verified_type

    @verified_type.setter
    def verified_type(self, verified_type):
        r"""Sets the verified_type of this ShowRealNameAuthStatusResponse.

        实名认证类型。实名认证状态为-1未实名认证返回null。enum:0,1。 0个人实名认证、1企业实名认证

        :param verified_type: The verified_type of this ShowRealNameAuthStatusResponse.
        :type verified_type: int
        """
        self._verified_type = verified_type

    def to_dict(self):
        import warnings
        warnings.warn("ShowRealNameAuthStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowRealNameAuthStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
