# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EstimateDesktopPoolChangeImageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'currency': 'str',
        'cloud_service_rating_results': 'list[CloudServiceRatingResult]'
    }

    attribute_map = {
        'currency': 'currency',
        'cloud_service_rating_results': 'cloud_service_rating_results'
    }

    def __init__(self, currency=None, cloud_service_rating_results=None):
        r"""EstimateDesktopPoolChangeImageResponse

        The model defined in huaweicloud sdk

        :param currency: 币种，比如CNY。
        :type currency: str
        :param cloud_service_rating_results: 询价结果。
        :type cloud_service_rating_results: list[:class:`huaweicloudsdkworkspace.v2.CloudServiceRatingResult`]
        """
        
        super(EstimateDesktopPoolChangeImageResponse, self).__init__()

        self._currency = None
        self._cloud_service_rating_results = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if cloud_service_rating_results is not None:
            self.cloud_service_rating_results = cloud_service_rating_results

    @property
    def currency(self):
        r"""Gets the currency of this EstimateDesktopPoolChangeImageResponse.

        币种，比如CNY。

        :return: The currency of this EstimateDesktopPoolChangeImageResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this EstimateDesktopPoolChangeImageResponse.

        币种，比如CNY。

        :param currency: The currency of this EstimateDesktopPoolChangeImageResponse.
        :type currency: str
        """
        self._currency = currency

    @property
    def cloud_service_rating_results(self):
        r"""Gets the cloud_service_rating_results of this EstimateDesktopPoolChangeImageResponse.

        询价结果。

        :return: The cloud_service_rating_results of this EstimateDesktopPoolChangeImageResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.CloudServiceRatingResult`]
        """
        return self._cloud_service_rating_results

    @cloud_service_rating_results.setter
    def cloud_service_rating_results(self, cloud_service_rating_results):
        r"""Sets the cloud_service_rating_results of this EstimateDesktopPoolChangeImageResponse.

        询价结果。

        :param cloud_service_rating_results: The cloud_service_rating_results of this EstimateDesktopPoolChangeImageResponse.
        :type cloud_service_rating_results: list[:class:`huaweicloudsdkworkspace.v2.CloudServiceRatingResult`]
        """
        self._cloud_service_rating_results = cloud_service_rating_results

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EstimateDesktopPoolChangeImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
