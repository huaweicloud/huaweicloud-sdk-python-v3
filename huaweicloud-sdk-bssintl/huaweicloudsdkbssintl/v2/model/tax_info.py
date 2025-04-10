# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaxInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tax_class': 'str',
        'tax_rate': 'str',
        'sub_tax_class': 'str',
        'tax_amount': 'decimal.Decimal'
    }

    attribute_map = {
        'tax_class': 'taxClass',
        'tax_rate': 'taxRate',
        'sub_tax_class': 'subTaxClass',
        'tax_amount': 'taxAmount'
    }

    def __init__(self, tax_class=None, tax_rate=None, sub_tax_class=None, tax_amount=None):
        r"""TaxInfo

        The model defined in huaweicloud sdk

        :param tax_class: 税种。 VATISSWHTGST
        :type tax_class: str
        :param tax_rate: 税率。
        :type tax_rate: str
        :param sub_tax_class: 税种子类。 PISCOFINSCGSTSGSTIGSTISSWHTVAT
        :type sub_tax_class: str
        :param tax_amount: 税金金额。 单位：美元
        :type tax_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        
        

        self._tax_class = None
        self._tax_rate = None
        self._sub_tax_class = None
        self._tax_amount = None
        self.discriminator = None

        if tax_class is not None:
            self.tax_class = tax_class
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if sub_tax_class is not None:
            self.sub_tax_class = sub_tax_class
        if tax_amount is not None:
            self.tax_amount = tax_amount

    @property
    def tax_class(self):
        r"""Gets the tax_class of this TaxInfo.

        税种。 VATISSWHTGST

        :return: The tax_class of this TaxInfo.
        :rtype: str
        """
        return self._tax_class

    @tax_class.setter
    def tax_class(self, tax_class):
        r"""Sets the tax_class of this TaxInfo.

        税种。 VATISSWHTGST

        :param tax_class: The tax_class of this TaxInfo.
        :type tax_class: str
        """
        self._tax_class = tax_class

    @property
    def tax_rate(self):
        r"""Gets the tax_rate of this TaxInfo.

        税率。

        :return: The tax_rate of this TaxInfo.
        :rtype: str
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        r"""Sets the tax_rate of this TaxInfo.

        税率。

        :param tax_rate: The tax_rate of this TaxInfo.
        :type tax_rate: str
        """
        self._tax_rate = tax_rate

    @property
    def sub_tax_class(self):
        r"""Gets the sub_tax_class of this TaxInfo.

        税种子类。 PISCOFINSCGSTSGSTIGSTISSWHTVAT

        :return: The sub_tax_class of this TaxInfo.
        :rtype: str
        """
        return self._sub_tax_class

    @sub_tax_class.setter
    def sub_tax_class(self, sub_tax_class):
        r"""Sets the sub_tax_class of this TaxInfo.

        税种子类。 PISCOFINSCGSTSGSTIGSTISSWHTVAT

        :param sub_tax_class: The sub_tax_class of this TaxInfo.
        :type sub_tax_class: str
        """
        self._sub_tax_class = sub_tax_class

    @property
    def tax_amount(self):
        r"""Gets the tax_amount of this TaxInfo.

        税金金额。 单位：美元

        :return: The tax_amount of this TaxInfo.
        :rtype: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        r"""Sets the tax_amount of this TaxInfo.

        税金金额。 单位：美元

        :param tax_amount: The tax_amount of this TaxInfo.
        :type tax_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        self._tax_amount = tax_amount

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
        if not isinstance(other, TaxInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
