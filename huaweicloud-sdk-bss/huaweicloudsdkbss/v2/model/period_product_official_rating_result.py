# coding: utf-8

import pprint
import re

import six





class PeriodProductOfficialRatingResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'product_id': 'str',
        'official_website_amount': 'float',
        'measure_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'product_id': 'product_id',
        'official_website_amount': 'official_website_amount',
        'measure_id': 'measure_id'
    }

    def __init__(self, id=None, product_id=None, official_website_amount=None, measure_id=None):
        """PeriodProductOfficialRatingResult - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._product_id = None
        self._official_website_amount = None
        self._measure_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if product_id is not None:
            self.product_id = product_id
        if official_website_amount is not None:
            self.official_website_amount = official_website_amount
        if measure_id is not None:
            self.measure_id = measure_id

    @property
    def id(self):
        """Gets the id of this PeriodProductOfficialRatingResult.

        |参数名称：ID标识，来源于请求中的ID| |参数约束及描述：ID标识，来源于请求中的ID|

        :return: The id of this PeriodProductOfficialRatingResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PeriodProductOfficialRatingResult.

        |参数名称：ID标识，来源于请求中的ID| |参数约束及描述：ID标识，来源于请求中的ID|

        :param id: The id of this PeriodProductOfficialRatingResult.
        :type: str
        """
        self._id = id

    @property
    def product_id(self):
        """Gets the product_id of this PeriodProductOfficialRatingResult.

        |参数名称：产品ID| |参数约束及描述：产品ID|

        :return: The product_id of this PeriodProductOfficialRatingResult.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this PeriodProductOfficialRatingResult.

        |参数名称：产品ID| |参数约束及描述：产品ID|

        :param product_id: The product_id of this PeriodProductOfficialRatingResult.
        :type: str
        """
        self._product_id = product_id

    @property
    def official_website_amount(self):
        """Gets the official_website_amount of this PeriodProductOfficialRatingResult.

        |参数名称：官网价| |参数约束及描述：官网价|

        :return: The official_website_amount of this PeriodProductOfficialRatingResult.
        :rtype: float
        """
        return self._official_website_amount

    @official_website_amount.setter
    def official_website_amount(self, official_website_amount):
        """Sets the official_website_amount of this PeriodProductOfficialRatingResult.

        |参数名称：官网价| |参数约束及描述：官网价|

        :param official_website_amount: The official_website_amount of this PeriodProductOfficialRatingResult.
        :type: float
        """
        self._official_website_amount = official_website_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this PeriodProductOfficialRatingResult.

        |参数名称：度量单位标识1：元|

        :return: The measure_id of this PeriodProductOfficialRatingResult.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this PeriodProductOfficialRatingResult.

        |参数名称：度量单位标识1：元|

        :param measure_id: The measure_id of this PeriodProductOfficialRatingResult.
        :type: int
        """
        self._measure_id = measure_id

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
        if not isinstance(other, PeriodProductOfficialRatingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
