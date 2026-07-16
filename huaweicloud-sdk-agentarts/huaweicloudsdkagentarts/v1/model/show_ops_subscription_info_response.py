# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsSubscriptionInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscribe_apm_response': 'SubscribeApmRes',
        'subscribe_aom_response': 'SubscribeAomRes',
        'subscribe_lts_response': 'SubscribeLtsRes'
    }

    attribute_map = {
        'subscribe_apm_response': 'subscribe_apm_response',
        'subscribe_aom_response': 'subscribe_aom_response',
        'subscribe_lts_response': 'subscribe_lts_response'
    }

    def __init__(self, subscribe_apm_response=None, subscribe_aom_response=None, subscribe_lts_response=None):
        r"""ShowOpsSubscriptionInfoResponse

        The model defined in huaweicloud sdk

        :param subscribe_apm_response: 
        :type subscribe_apm_response: :class:`huaweicloudsdkagentarts.v1.SubscribeApmRes`
        :param subscribe_aom_response: 
        :type subscribe_aom_response: :class:`huaweicloudsdkagentarts.v1.SubscribeAomRes`
        :param subscribe_lts_response: 
        :type subscribe_lts_response: :class:`huaweicloudsdkagentarts.v1.SubscribeLtsRes`
        """
        
        super().__init__()

        self._subscribe_apm_response = None
        self._subscribe_aom_response = None
        self._subscribe_lts_response = None
        self.discriminator = None

        if subscribe_apm_response is not None:
            self.subscribe_apm_response = subscribe_apm_response
        if subscribe_aom_response is not None:
            self.subscribe_aom_response = subscribe_aom_response
        if subscribe_lts_response is not None:
            self.subscribe_lts_response = subscribe_lts_response

    @property
    def subscribe_apm_response(self):
        r"""Gets the subscribe_apm_response of this ShowOpsSubscriptionInfoResponse.

        :return: The subscribe_apm_response of this ShowOpsSubscriptionInfoResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.SubscribeApmRes`
        """
        return self._subscribe_apm_response

    @subscribe_apm_response.setter
    def subscribe_apm_response(self, subscribe_apm_response):
        r"""Sets the subscribe_apm_response of this ShowOpsSubscriptionInfoResponse.

        :param subscribe_apm_response: The subscribe_apm_response of this ShowOpsSubscriptionInfoResponse.
        :type subscribe_apm_response: :class:`huaweicloudsdkagentarts.v1.SubscribeApmRes`
        """
        self._subscribe_apm_response = subscribe_apm_response

    @property
    def subscribe_aom_response(self):
        r"""Gets the subscribe_aom_response of this ShowOpsSubscriptionInfoResponse.

        :return: The subscribe_aom_response of this ShowOpsSubscriptionInfoResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.SubscribeAomRes`
        """
        return self._subscribe_aom_response

    @subscribe_aom_response.setter
    def subscribe_aom_response(self, subscribe_aom_response):
        r"""Sets the subscribe_aom_response of this ShowOpsSubscriptionInfoResponse.

        :param subscribe_aom_response: The subscribe_aom_response of this ShowOpsSubscriptionInfoResponse.
        :type subscribe_aom_response: :class:`huaweicloudsdkagentarts.v1.SubscribeAomRes`
        """
        self._subscribe_aom_response = subscribe_aom_response

    @property
    def subscribe_lts_response(self):
        r"""Gets the subscribe_lts_response of this ShowOpsSubscriptionInfoResponse.

        :return: The subscribe_lts_response of this ShowOpsSubscriptionInfoResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.SubscribeLtsRes`
        """
        return self._subscribe_lts_response

    @subscribe_lts_response.setter
    def subscribe_lts_response(self, subscribe_lts_response):
        r"""Sets the subscribe_lts_response of this ShowOpsSubscriptionInfoResponse.

        :param subscribe_lts_response: The subscribe_lts_response of this ShowOpsSubscriptionInfoResponse.
        :type subscribe_lts_response: :class:`huaweicloudsdkagentarts.v1.SubscribeLtsRes`
        """
        self._subscribe_lts_response = subscribe_lts_response

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsSubscriptionInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsSubscriptionInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
