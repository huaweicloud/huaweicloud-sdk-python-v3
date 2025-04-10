# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InvoiceVerificationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'number': 'str',
        'issue_date': 'str',
        'check_code': 'str',
        'subtotal_amount': 'str'
    }

    attribute_map = {
        'code': 'code',
        'number': 'number',
        'issue_date': 'issue_date',
        'check_code': 'check_code',
        'subtotal_amount': 'subtotal_amount'
    }

    def __init__(self, code=None, number=None, issue_date=None, check_code=None, subtotal_amount=None):
        r"""InvoiceVerificationRequestBody

        The model defined in huaweicloud sdk

        :param code: 发票代码。发票种类为全电发票时，该参数须为空字符串。
        :type code: str
        :param number: 发票号码
        :type number: str
        :param issue_date: 发票日期格式YYYY-MM-DD
        :type issue_date: str
        :param check_code: 校验码后六位。 - 以下种类发票，参数不可为空    增值税普通发票、增值税电子普通发票、增值税普通发票（卷式）、增值税电子普通发票（通行费）、区块链电子发票。  - 区块链电子发票需要填写5位校验码。 
        :type check_code: str
        :param subtotal_amount: 合计金额。和票据上的金额的有效数字保持一致，例如票据上的金额为88.00，则需要输入字符串为“88.00”，才能验真成功。如果输入“88”或“88.0”可能会产生\&quot;result_code\&quot;: \&quot;1010\&quot;, \&quot; Parameter error.\&quot;报错。  - 以下种类发票，参数不可为空    增值税专用发票、增值税电子专用发票、机动车销售统一发票、二手车销售统一发票、区块链电子发票、全电发票。  - 填写发票合计金额（不含税）    增值税专用发票、增值税电子专用发票、机动车销售统一发票、区块链电子发票。  - 填写发票车价合计    二手车发票。  - 填写发票合计金额    全电发票。  - 填写票价或者退票费    全电发票（铁路电子客票） 
        :type subtotal_amount: str
        """
        
        

        self._code = None
        self._number = None
        self._issue_date = None
        self._check_code = None
        self._subtotal_amount = None
        self.discriminator = None

        self.code = code
        self.number = number
        self.issue_date = issue_date
        if check_code is not None:
            self.check_code = check_code
        if subtotal_amount is not None:
            self.subtotal_amount = subtotal_amount

    @property
    def code(self):
        r"""Gets the code of this InvoiceVerificationRequestBody.

        发票代码。发票种类为全电发票时，该参数须为空字符串。

        :return: The code of this InvoiceVerificationRequestBody.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this InvoiceVerificationRequestBody.

        发票代码。发票种类为全电发票时，该参数须为空字符串。

        :param code: The code of this InvoiceVerificationRequestBody.
        :type code: str
        """
        self._code = code

    @property
    def number(self):
        r"""Gets the number of this InvoiceVerificationRequestBody.

        发票号码

        :return: The number of this InvoiceVerificationRequestBody.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this InvoiceVerificationRequestBody.

        发票号码

        :param number: The number of this InvoiceVerificationRequestBody.
        :type number: str
        """
        self._number = number

    @property
    def issue_date(self):
        r"""Gets the issue_date of this InvoiceVerificationRequestBody.

        发票日期格式YYYY-MM-DD

        :return: The issue_date of this InvoiceVerificationRequestBody.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        r"""Sets the issue_date of this InvoiceVerificationRequestBody.

        发票日期格式YYYY-MM-DD

        :param issue_date: The issue_date of this InvoiceVerificationRequestBody.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def check_code(self):
        r"""Gets the check_code of this InvoiceVerificationRequestBody.

        校验码后六位。 - 以下种类发票，参数不可为空    增值税普通发票、增值税电子普通发票、增值税普通发票（卷式）、增值税电子普通发票（通行费）、区块链电子发票。  - 区块链电子发票需要填写5位校验码。 

        :return: The check_code of this InvoiceVerificationRequestBody.
        :rtype: str
        """
        return self._check_code

    @check_code.setter
    def check_code(self, check_code):
        r"""Sets the check_code of this InvoiceVerificationRequestBody.

        校验码后六位。 - 以下种类发票，参数不可为空    增值税普通发票、增值税电子普通发票、增值税普通发票（卷式）、增值税电子普通发票（通行费）、区块链电子发票。  - 区块链电子发票需要填写5位校验码。 

        :param check_code: The check_code of this InvoiceVerificationRequestBody.
        :type check_code: str
        """
        self._check_code = check_code

    @property
    def subtotal_amount(self):
        r"""Gets the subtotal_amount of this InvoiceVerificationRequestBody.

        合计金额。和票据上的金额的有效数字保持一致，例如票据上的金额为88.00，则需要输入字符串为“88.00”，才能验真成功。如果输入“88”或“88.0”可能会产生\"result_code\": \"1010\", \" Parameter error.\"报错。  - 以下种类发票，参数不可为空    增值税专用发票、增值税电子专用发票、机动车销售统一发票、二手车销售统一发票、区块链电子发票、全电发票。  - 填写发票合计金额（不含税）    增值税专用发票、增值税电子专用发票、机动车销售统一发票、区块链电子发票。  - 填写发票车价合计    二手车发票。  - 填写发票合计金额    全电发票。  - 填写票价或者退票费    全电发票（铁路电子客票） 

        :return: The subtotal_amount of this InvoiceVerificationRequestBody.
        :rtype: str
        """
        return self._subtotal_amount

    @subtotal_amount.setter
    def subtotal_amount(self, subtotal_amount):
        r"""Sets the subtotal_amount of this InvoiceVerificationRequestBody.

        合计金额。和票据上的金额的有效数字保持一致，例如票据上的金额为88.00，则需要输入字符串为“88.00”，才能验真成功。如果输入“88”或“88.0”可能会产生\"result_code\": \"1010\", \" Parameter error.\"报错。  - 以下种类发票，参数不可为空    增值税专用发票、增值税电子专用发票、机动车销售统一发票、二手车销售统一发票、区块链电子发票、全电发票。  - 填写发票合计金额（不含税）    增值税专用发票、增值税电子专用发票、机动车销售统一发票、区块链电子发票。  - 填写发票车价合计    二手车发票。  - 填写发票合计金额    全电发票。  - 填写票价或者退票费    全电发票（铁路电子客票） 

        :param subtotal_amount: The subtotal_amount of this InvoiceVerificationRequestBody.
        :type subtotal_amount: str
        """
        self._subtotal_amount = subtotal_amount

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
        if not isinstance(other, InvoiceVerificationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
