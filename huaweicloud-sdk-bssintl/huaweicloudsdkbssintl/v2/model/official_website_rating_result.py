# coding: utf-8

import pprint
import re

import six





class OfficialWebsiteRatingResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'official_website_amount': 'float',
        'measure_id': 'int',
        'product_rating_results': 'list[PeriodProductOfficialRatingResult]'
    }

    attribute_map = {
        'official_website_amount': 'official_website_amount',
        'measure_id': 'measure_id',
        'product_rating_results': 'product_rating_results'
    }

    def __init__(self, official_website_amount=None, measure_id=None, product_rating_results=None):
        """OfficialWebsiteRatingResult - a model defined in huaweicloud sdk"""
        
        

        self._official_website_amount = None
        self._measure_id = None
        self._product_rating_results = None
        self.discriminator = None

        if official_website_amount is not None:
            self.official_website_amount = official_website_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if product_rating_results is not None:
            self.product_rating_results = product_rating_results

    @property
    def official_website_amount(self):
        """Gets the official_website_amount of this OfficialWebsiteRatingResult.

        |参数名称：官网价| |参数约束及描述：官网价|

        :return: The official_website_amount of this OfficialWebsiteRatingResult.
        :rtype: float
        """
        return self._official_website_amount

    @official_website_amount.setter
    def official_website_amount(self, official_website_amount):
        """Sets the official_website_amount of this OfficialWebsiteRatingResult.

        |参数名称：官网价| |参数约束及描述：官网价|

        :param official_website_amount: The official_website_amount of this OfficialWebsiteRatingResult.
        :type: float
        """
        self._official_website_amount = official_website_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this OfficialWebsiteRatingResult.

        |参数名称：度量单位标识1：元|

        :return: The measure_id of this OfficialWebsiteRatingResult.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this OfficialWebsiteRatingResult.

        |参数名称：度量单位标识1：元|

        :param measure_id: The measure_id of this OfficialWebsiteRatingResult.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def product_rating_results(self):
        """Gets the product_rating_results of this OfficialWebsiteRatingResult.

        |参数名称：产品询价结果| |参数的约束及描述：产品询价结果|

        :return: The product_rating_results of this OfficialWebsiteRatingResult.
        :rtype: list[PeriodProductOfficialRatingResult]
        """
        return self._product_rating_results

    @product_rating_results.setter
    def product_rating_results(self, product_rating_results):
        """Sets the product_rating_results of this OfficialWebsiteRatingResult.

        |参数名称：产品询价结果| |参数的约束及描述：产品询价结果|

        :param product_rating_results: The product_rating_results of this OfficialWebsiteRatingResult.
        :type: list[PeriodProductOfficialRatingResult]
        """
        self._product_rating_results = product_rating_results

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OfficialWebsiteRatingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
