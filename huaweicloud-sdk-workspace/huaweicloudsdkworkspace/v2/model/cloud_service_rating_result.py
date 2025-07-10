# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudServiceRatingResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_request_id': 'str',
        'official_website_rating_result': 'OfficialWebsiteRatingResult',
        'optional_discount_rating_results': 'list[OptionalDiscountRatingResult]'
    }

    attribute_map = {
        'order_request_id': 'order_request_id',
        'official_website_rating_result': 'official_website_rating_result',
        'optional_discount_rating_results': 'optional_discount_rating_results'
    }

    def __init__(self, order_request_id=None, official_website_rating_result=None, optional_discount_rating_results=None):
        r"""CloudServiceRatingResult

        The model defined in huaweicloud sdk

        :param order_request_id: 下单请求体中的orderRequestId。
        :type order_request_id: str
        :param official_website_rating_result: 
        :type official_website_rating_result: :class:`huaweicloudsdkworkspace.v2.OfficialWebsiteRatingResult`
        :param optional_discount_rating_results: 优惠询价结果。
        :type optional_discount_rating_results: list[:class:`huaweicloudsdkworkspace.v2.OptionalDiscountRatingResult`]
        """
        
        

        self._order_request_id = None
        self._official_website_rating_result = None
        self._optional_discount_rating_results = None
        self.discriminator = None

        if order_request_id is not None:
            self.order_request_id = order_request_id
        if official_website_rating_result is not None:
            self.official_website_rating_result = official_website_rating_result
        if optional_discount_rating_results is not None:
            self.optional_discount_rating_results = optional_discount_rating_results

    @property
    def order_request_id(self):
        r"""Gets the order_request_id of this CloudServiceRatingResult.

        下单请求体中的orderRequestId。

        :return: The order_request_id of this CloudServiceRatingResult.
        :rtype: str
        """
        return self._order_request_id

    @order_request_id.setter
    def order_request_id(self, order_request_id):
        r"""Sets the order_request_id of this CloudServiceRatingResult.

        下单请求体中的orderRequestId。

        :param order_request_id: The order_request_id of this CloudServiceRatingResult.
        :type order_request_id: str
        """
        self._order_request_id = order_request_id

    @property
    def official_website_rating_result(self):
        r"""Gets the official_website_rating_result of this CloudServiceRatingResult.

        :return: The official_website_rating_result of this CloudServiceRatingResult.
        :rtype: :class:`huaweicloudsdkworkspace.v2.OfficialWebsiteRatingResult`
        """
        return self._official_website_rating_result

    @official_website_rating_result.setter
    def official_website_rating_result(self, official_website_rating_result):
        r"""Sets the official_website_rating_result of this CloudServiceRatingResult.

        :param official_website_rating_result: The official_website_rating_result of this CloudServiceRatingResult.
        :type official_website_rating_result: :class:`huaweicloudsdkworkspace.v2.OfficialWebsiteRatingResult`
        """
        self._official_website_rating_result = official_website_rating_result

    @property
    def optional_discount_rating_results(self):
        r"""Gets the optional_discount_rating_results of this CloudServiceRatingResult.

        优惠询价结果。

        :return: The optional_discount_rating_results of this CloudServiceRatingResult.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.OptionalDiscountRatingResult`]
        """
        return self._optional_discount_rating_results

    @optional_discount_rating_results.setter
    def optional_discount_rating_results(self, optional_discount_rating_results):
        r"""Sets the optional_discount_rating_results of this CloudServiceRatingResult.

        优惠询价结果。

        :param optional_discount_rating_results: The optional_discount_rating_results of this CloudServiceRatingResult.
        :type optional_discount_rating_results: list[:class:`huaweicloudsdkworkspace.v2.OptionalDiscountRatingResult`]
        """
        self._optional_discount_rating_results = optional_discount_rating_results

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
        if not isinstance(other, CloudServiceRatingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
