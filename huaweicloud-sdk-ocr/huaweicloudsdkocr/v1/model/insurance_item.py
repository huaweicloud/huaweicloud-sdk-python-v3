# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InsuranceItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'insurance_name': 'InsurancePolicyDetail',
        'insurance_period': 'InsurancePolicyDetail',
        'insurance_amount': 'InsurancePolicyDetail',
        'payment_frequency': 'InsurancePolicyDetail',
        'payment_period': 'InsurancePolicyDetail',
        'payment_amount': 'InsurancePolicyDetail'
    }

    attribute_map = {
        'insurance_name': 'insurance_name',
        'insurance_period': 'insurance_period',
        'insurance_amount': 'insurance_amount',
        'payment_frequency': 'payment_frequency',
        'payment_period': 'payment_period',
        'payment_amount': 'payment_amount'
    }

    def __init__(self, insurance_name=None, insurance_period=None, insurance_amount=None, payment_frequency=None, payment_period=None, payment_amount=None):
        """InsuranceItem

        The model defined in huaweicloud sdk

        :param insurance_name: 
        :type insurance_name: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param insurance_period: 
        :type insurance_period: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param insurance_amount: 
        :type insurance_amount: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param payment_frequency: 
        :type payment_frequency: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param payment_period: 
        :type payment_period: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param payment_amount: 
        :type payment_amount: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        
        

        self._insurance_name = None
        self._insurance_period = None
        self._insurance_amount = None
        self._payment_frequency = None
        self._payment_period = None
        self._payment_amount = None
        self.discriminator = None

        if insurance_name is not None:
            self.insurance_name = insurance_name
        if insurance_period is not None:
            self.insurance_period = insurance_period
        if insurance_amount is not None:
            self.insurance_amount = insurance_amount
        if payment_frequency is not None:
            self.payment_frequency = payment_frequency
        if payment_period is not None:
            self.payment_period = payment_period
        if payment_amount is not None:
            self.payment_amount = payment_amount

    @property
    def insurance_name(self):
        """Gets the insurance_name of this InsuranceItem.

        :return: The insurance_name of this InsuranceItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._insurance_name

    @insurance_name.setter
    def insurance_name(self, insurance_name):
        """Sets the insurance_name of this InsuranceItem.

        :param insurance_name: The insurance_name of this InsuranceItem.
        :type insurance_name: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._insurance_name = insurance_name

    @property
    def insurance_period(self):
        """Gets the insurance_period of this InsuranceItem.

        :return: The insurance_period of this InsuranceItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._insurance_period

    @insurance_period.setter
    def insurance_period(self, insurance_period):
        """Sets the insurance_period of this InsuranceItem.

        :param insurance_period: The insurance_period of this InsuranceItem.
        :type insurance_period: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._insurance_period = insurance_period

    @property
    def insurance_amount(self):
        """Gets the insurance_amount of this InsuranceItem.

        :return: The insurance_amount of this InsuranceItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._insurance_amount

    @insurance_amount.setter
    def insurance_amount(self, insurance_amount):
        """Sets the insurance_amount of this InsuranceItem.

        :param insurance_amount: The insurance_amount of this InsuranceItem.
        :type insurance_amount: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._insurance_amount = insurance_amount

    @property
    def payment_frequency(self):
        """Gets the payment_frequency of this InsuranceItem.

        :return: The payment_frequency of this InsuranceItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._payment_frequency

    @payment_frequency.setter
    def payment_frequency(self, payment_frequency):
        """Sets the payment_frequency of this InsuranceItem.

        :param payment_frequency: The payment_frequency of this InsuranceItem.
        :type payment_frequency: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._payment_frequency = payment_frequency

    @property
    def payment_period(self):
        """Gets the payment_period of this InsuranceItem.

        :return: The payment_period of this InsuranceItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._payment_period

    @payment_period.setter
    def payment_period(self, payment_period):
        """Sets the payment_period of this InsuranceItem.

        :param payment_period: The payment_period of this InsuranceItem.
        :type payment_period: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._payment_period = payment_period

    @property
    def payment_amount(self):
        """Gets the payment_amount of this InsuranceItem.

        :return: The payment_amount of this InsuranceItem.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        """Sets the payment_amount of this InsuranceItem.

        :param payment_amount: The payment_amount of this InsuranceItem.
        :type payment_amount: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._payment_amount = payment_amount

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
        if not isinstance(other, InsuranceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
