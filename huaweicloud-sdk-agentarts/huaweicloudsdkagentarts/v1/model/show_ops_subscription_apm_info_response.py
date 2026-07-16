# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsSubscriptionApmInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec': 'str',
        'business_id': 'str',
        'business_name': 'str'
    }

    attribute_map = {
        'spec': 'spec',
        'business_id': 'business_id',
        'business_name': 'business_name'
    }

    def __init__(self, spec=None, business_id=None, business_name=None):
        r"""ShowOpsSubscriptionApmInfoResponse

        The model defined in huaweicloud sdk

        :param spec: 规格
        :type spec: str
        :param business_id: 应用id
        :type business_id: str
        :param business_name: 名称
        :type business_name: str
        """
        
        super().__init__()

        self._spec = None
        self._business_id = None
        self._business_name = None
        self.discriminator = None

        if spec is not None:
            self.spec = spec
        if business_id is not None:
            self.business_id = business_id
        if business_name is not None:
            self.business_name = business_name

    @property
    def spec(self):
        r"""Gets the spec of this ShowOpsSubscriptionApmInfoResponse.

        规格

        :return: The spec of this ShowOpsSubscriptionApmInfoResponse.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ShowOpsSubscriptionApmInfoResponse.

        规格

        :param spec: The spec of this ShowOpsSubscriptionApmInfoResponse.
        :type spec: str
        """
        self._spec = spec

    @property
    def business_id(self):
        r"""Gets the business_id of this ShowOpsSubscriptionApmInfoResponse.

        应用id

        :return: The business_id of this ShowOpsSubscriptionApmInfoResponse.
        :rtype: str
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        r"""Sets the business_id of this ShowOpsSubscriptionApmInfoResponse.

        应用id

        :param business_id: The business_id of this ShowOpsSubscriptionApmInfoResponse.
        :type business_id: str
        """
        self._business_id = business_id

    @property
    def business_name(self):
        r"""Gets the business_name of this ShowOpsSubscriptionApmInfoResponse.

        名称

        :return: The business_name of this ShowOpsSubscriptionApmInfoResponse.
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        r"""Sets the business_name of this ShowOpsSubscriptionApmInfoResponse.

        名称

        :param business_name: The business_name of this ShowOpsSubscriptionApmInfoResponse.
        :type business_name: str
        """
        self._business_name = business_name

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsSubscriptionApmInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsSubscriptionApmInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
