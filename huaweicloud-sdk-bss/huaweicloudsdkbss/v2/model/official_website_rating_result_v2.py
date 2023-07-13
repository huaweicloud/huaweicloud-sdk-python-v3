# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OfficialWebsiteRatingResultV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'official_website_amount': 'str',
        'installment_official_website_amount': 'str',
        'installment_period_type': 'int'
    }

    attribute_map = {
        'official_website_amount': 'official_website_amount',
        'installment_official_website_amount': 'installment_official_website_amount',
        'installment_period_type': 'installment_period_type'
    }

    def __init__(self, official_website_amount=None, installment_official_website_amount=None, installment_period_type=None):
        """OfficialWebsiteRatingResultV2

        The model defined in huaweicloud sdk

        :param official_website_amount: |参数名称：官网价格。单位为元| |参数约束及描述：官网价格。单位为元|
        :type official_website_amount: str
        :param installment_official_website_amount: |参数名称：分期金额的官网价。单位为元| |参数约束及描述：分期金额的官网价。单位为元|
        :type installment_official_website_amount: str
        :param installment_period_type: |参数名称：分期付款的周期类型。2：月| |参数的约束及描述：分期付款的周期类型。2：月|
        :type installment_period_type: int
        """
        
        

        self._official_website_amount = None
        self._installment_official_website_amount = None
        self._installment_period_type = None
        self.discriminator = None

        if official_website_amount is not None:
            self.official_website_amount = official_website_amount
        if installment_official_website_amount is not None:
            self.installment_official_website_amount = installment_official_website_amount
        if installment_period_type is not None:
            self.installment_period_type = installment_period_type

    @property
    def official_website_amount(self):
        """Gets the official_website_amount of this OfficialWebsiteRatingResultV2.

        |参数名称：官网价格。单位为元| |参数约束及描述：官网价格。单位为元|

        :return: The official_website_amount of this OfficialWebsiteRatingResultV2.
        :rtype: str
        """
        return self._official_website_amount

    @official_website_amount.setter
    def official_website_amount(self, official_website_amount):
        """Sets the official_website_amount of this OfficialWebsiteRatingResultV2.

        |参数名称：官网价格。单位为元| |参数约束及描述：官网价格。单位为元|

        :param official_website_amount: The official_website_amount of this OfficialWebsiteRatingResultV2.
        :type official_website_amount: str
        """
        self._official_website_amount = official_website_amount

    @property
    def installment_official_website_amount(self):
        """Gets the installment_official_website_amount of this OfficialWebsiteRatingResultV2.

        |参数名称：分期金额的官网价。单位为元| |参数约束及描述：分期金额的官网价。单位为元|

        :return: The installment_official_website_amount of this OfficialWebsiteRatingResultV2.
        :rtype: str
        """
        return self._installment_official_website_amount

    @installment_official_website_amount.setter
    def installment_official_website_amount(self, installment_official_website_amount):
        """Sets the installment_official_website_amount of this OfficialWebsiteRatingResultV2.

        |参数名称：分期金额的官网价。单位为元| |参数约束及描述：分期金额的官网价。单位为元|

        :param installment_official_website_amount: The installment_official_website_amount of this OfficialWebsiteRatingResultV2.
        :type installment_official_website_amount: str
        """
        self._installment_official_website_amount = installment_official_website_amount

    @property
    def installment_period_type(self):
        """Gets the installment_period_type of this OfficialWebsiteRatingResultV2.

        |参数名称：分期付款的周期类型。2：月| |参数的约束及描述：分期付款的周期类型。2：月|

        :return: The installment_period_type of this OfficialWebsiteRatingResultV2.
        :rtype: int
        """
        return self._installment_period_type

    @installment_period_type.setter
    def installment_period_type(self, installment_period_type):
        """Sets the installment_period_type of this OfficialWebsiteRatingResultV2.

        |参数名称：分期付款的周期类型。2：月| |参数的约束及描述：分期付款的周期类型。2：月|

        :param installment_period_type: The installment_period_type of this OfficialWebsiteRatingResultV2.
        :type installment_period_type: int
        """
        self._installment_period_type = installment_period_type

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
        if not isinstance(other, OfficialWebsiteRatingResultV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
