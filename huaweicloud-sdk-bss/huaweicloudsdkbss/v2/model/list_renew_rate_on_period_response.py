# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRenewRateOnPeriodResponse(SdkResponse):

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
        'renew_inquiry_results': 'list[RenewInquiryResultInfo]',
        'official_website_rating_result': 'OfficialWebsiteRatingResultV2',
        'optional_discount_rating_results': 'list[OptionalDiscountRatingResultV2]',
        'fail_resource_infos': 'list[FailResourceInfo]'
    }

    attribute_map = {
        'currency': 'currency',
        'renew_inquiry_results': 'renew_inquiry_results',
        'official_website_rating_result': 'official_website_rating_result',
        'optional_discount_rating_results': 'optional_discount_rating_results',
        'fail_resource_infos': 'fail_resource_infos'
    }

    def __init__(self, currency=None, renew_inquiry_results=None, official_website_rating_result=None, optional_discount_rating_results=None, fail_resource_infos=None):
        r"""ListRenewRateOnPeriodResponse

        The model defined in huaweicloud sdk

        :param currency: |参数名称：币种。CNY：人民币。USD：美元。| |参数约束及描述：币种。CNY：人民币。USD：美元。|
        :type currency: str
        :param renew_inquiry_results: |参数名称：主资源（包含从资源）询价结果| |参数约束以及描述：主资源（包含从资源）询价结果|
        :type renew_inquiry_results: list[:class:`huaweicloudsdkbss.v2.RenewInquiryResultInfo`]
        :param official_website_rating_result: 
        :type official_website_rating_result: :class:`huaweicloudsdkbss.v2.OfficialWebsiteRatingResultV2`
        :param optional_discount_rating_results: |参数名称：存在可选折扣优惠时返回折扣优惠维度询价结果，每个折扣优惠一组询价结果| |参数约束以及描述：存在可选折扣优惠时返回折扣优惠维度询价结果，每个折扣优惠一组询价结果|
        :type optional_discount_rating_results: list[:class:`huaweicloudsdkbss.v2.OptionalDiscountRatingResultV2`]
        :param fail_resource_infos: |参数名称：失败的资源信息列表| |参数约束以及描述：失败的资源信息列表|
        :type fail_resource_infos: list[:class:`huaweicloudsdkbss.v2.FailResourceInfo`]
        """
        
        super(ListRenewRateOnPeriodResponse, self).__init__()

        self._currency = None
        self._renew_inquiry_results = None
        self._official_website_rating_result = None
        self._optional_discount_rating_results = None
        self._fail_resource_infos = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if renew_inquiry_results is not None:
            self.renew_inquiry_results = renew_inquiry_results
        if official_website_rating_result is not None:
            self.official_website_rating_result = official_website_rating_result
        if optional_discount_rating_results is not None:
            self.optional_discount_rating_results = optional_discount_rating_results
        if fail_resource_infos is not None:
            self.fail_resource_infos = fail_resource_infos

    @property
    def currency(self):
        r"""Gets the currency of this ListRenewRateOnPeriodResponse.

        |参数名称：币种。CNY：人民币。USD：美元。| |参数约束及描述：币种。CNY：人民币。USD：美元。|

        :return: The currency of this ListRenewRateOnPeriodResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this ListRenewRateOnPeriodResponse.

        |参数名称：币种。CNY：人民币。USD：美元。| |参数约束及描述：币种。CNY：人民币。USD：美元。|

        :param currency: The currency of this ListRenewRateOnPeriodResponse.
        :type currency: str
        """
        self._currency = currency

    @property
    def renew_inquiry_results(self):
        r"""Gets the renew_inquiry_results of this ListRenewRateOnPeriodResponse.

        |参数名称：主资源（包含从资源）询价结果| |参数约束以及描述：主资源（包含从资源）询价结果|

        :return: The renew_inquiry_results of this ListRenewRateOnPeriodResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.RenewInquiryResultInfo`]
        """
        return self._renew_inquiry_results

    @renew_inquiry_results.setter
    def renew_inquiry_results(self, renew_inquiry_results):
        r"""Sets the renew_inquiry_results of this ListRenewRateOnPeriodResponse.

        |参数名称：主资源（包含从资源）询价结果| |参数约束以及描述：主资源（包含从资源）询价结果|

        :param renew_inquiry_results: The renew_inquiry_results of this ListRenewRateOnPeriodResponse.
        :type renew_inquiry_results: list[:class:`huaweicloudsdkbss.v2.RenewInquiryResultInfo`]
        """
        self._renew_inquiry_results = renew_inquiry_results

    @property
    def official_website_rating_result(self):
        r"""Gets the official_website_rating_result of this ListRenewRateOnPeriodResponse.

        :return: The official_website_rating_result of this ListRenewRateOnPeriodResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.OfficialWebsiteRatingResultV2`
        """
        return self._official_website_rating_result

    @official_website_rating_result.setter
    def official_website_rating_result(self, official_website_rating_result):
        r"""Sets the official_website_rating_result of this ListRenewRateOnPeriodResponse.

        :param official_website_rating_result: The official_website_rating_result of this ListRenewRateOnPeriodResponse.
        :type official_website_rating_result: :class:`huaweicloudsdkbss.v2.OfficialWebsiteRatingResultV2`
        """
        self._official_website_rating_result = official_website_rating_result

    @property
    def optional_discount_rating_results(self):
        r"""Gets the optional_discount_rating_results of this ListRenewRateOnPeriodResponse.

        |参数名称：存在可选折扣优惠时返回折扣优惠维度询价结果，每个折扣优惠一组询价结果| |参数约束以及描述：存在可选折扣优惠时返回折扣优惠维度询价结果，每个折扣优惠一组询价结果|

        :return: The optional_discount_rating_results of this ListRenewRateOnPeriodResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.OptionalDiscountRatingResultV2`]
        """
        return self._optional_discount_rating_results

    @optional_discount_rating_results.setter
    def optional_discount_rating_results(self, optional_discount_rating_results):
        r"""Sets the optional_discount_rating_results of this ListRenewRateOnPeriodResponse.

        |参数名称：存在可选折扣优惠时返回折扣优惠维度询价结果，每个折扣优惠一组询价结果| |参数约束以及描述：存在可选折扣优惠时返回折扣优惠维度询价结果，每个折扣优惠一组询价结果|

        :param optional_discount_rating_results: The optional_discount_rating_results of this ListRenewRateOnPeriodResponse.
        :type optional_discount_rating_results: list[:class:`huaweicloudsdkbss.v2.OptionalDiscountRatingResultV2`]
        """
        self._optional_discount_rating_results = optional_discount_rating_results

    @property
    def fail_resource_infos(self):
        r"""Gets the fail_resource_infos of this ListRenewRateOnPeriodResponse.

        |参数名称：失败的资源信息列表| |参数约束以及描述：失败的资源信息列表|

        :return: The fail_resource_infos of this ListRenewRateOnPeriodResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.FailResourceInfo`]
        """
        return self._fail_resource_infos

    @fail_resource_infos.setter
    def fail_resource_infos(self, fail_resource_infos):
        r"""Sets the fail_resource_infos of this ListRenewRateOnPeriodResponse.

        |参数名称：失败的资源信息列表| |参数约束以及描述：失败的资源信息列表|

        :param fail_resource_infos: The fail_resource_infos of this ListRenewRateOnPeriodResponse.
        :type fail_resource_infos: list[:class:`huaweicloudsdkbss.v2.FailResourceInfo`]
        """
        self._fail_resource_infos = fail_resource_infos

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
        if not isinstance(other, ListRenewRateOnPeriodResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
