# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BudgetRecordInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'budget_amount': 'decimal.Decimal',
        'operation_type': 'str',
        'operation_time': 'str',
        'operator': 'str',
        'budget_type': 'str',
        'partner_corp_name': 'str',
        'partner_account_name': 'str'
    }

    attribute_map = {
        'budget_amount': 'budget_amount',
        'operation_type': 'operation_type',
        'operation_time': 'operation_time',
        'operator': 'operator',
        'budget_type': 'budget_type',
        'partner_corp_name': 'partner_corp_name',
        'partner_account_name': 'partner_account_name'
    }

    def __init__(self, budget_amount=None, operation_type=None, operation_time=None, operator=None, budget_type=None, partner_corp_name=None, partner_account_name=None):
        r"""BudgetRecordInfo

        The model defined in huaweicloud sdk

        :param budget_amount: |参数名称：预算金额||参数的约束及描述：单位：元，精确至小数点后2位。范围限制:0-2147483647|
        :type budget_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        :param operation_type: |参数名称：操作类别| |参数的约束及描述：范围限制：0-10。SETTING：设置 DELETE：解除关联关系。|
        :type operation_type: str
        :param operation_time: |参数名称：操作时间| |参数的约束及描述：UTC时间，格式为：yyyy-MM-ddTHH:mm:ssZ。|
        :type operation_time: str
        :param operator: |参数名称：操作员或系统system| |参数的约束及描述：范围限制：0-64|
        :type operator: str
        :param budget_type: |参数名称：预算模式| |参数的约束及描述：范围限制：0-10。MONTHLY：月度预算 PACKAGE：一次性预算|
        :type budget_type: str
        :param partner_corp_name: |参数名称：伙伴名称| |参数的约束及描述：范围限制：0-256|
        :type partner_corp_name: str
        :param partner_account_name: |参数名称：伙伴账号名| |参数的约束及描述：范围限制：0-128|
        :type partner_account_name: str
        """
        
        

        self._budget_amount = None
        self._operation_type = None
        self._operation_time = None
        self._operator = None
        self._budget_type = None
        self._partner_corp_name = None
        self._partner_account_name = None
        self.discriminator = None

        if budget_amount is not None:
            self.budget_amount = budget_amount
        if operation_type is not None:
            self.operation_type = operation_type
        if operation_time is not None:
            self.operation_time = operation_time
        if operator is not None:
            self.operator = operator
        if budget_type is not None:
            self.budget_type = budget_type
        if partner_corp_name is not None:
            self.partner_corp_name = partner_corp_name
        if partner_account_name is not None:
            self.partner_account_name = partner_account_name

    @property
    def budget_amount(self):
        r"""Gets the budget_amount of this BudgetRecordInfo.

        |参数名称：预算金额||参数的约束及描述：单位：元，精确至小数点后2位。范围限制:0-2147483647|

        :return: The budget_amount of this BudgetRecordInfo.
        :rtype: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, budget_amount):
        r"""Sets the budget_amount of this BudgetRecordInfo.

        |参数名称：预算金额||参数的约束及描述：单位：元，精确至小数点后2位。范围限制:0-2147483647|

        :param budget_amount: The budget_amount of this BudgetRecordInfo.
        :type budget_amount: :class:`huaweicloudsdkbssintl.v2.decimal.Decimal`
        """
        self._budget_amount = budget_amount

    @property
    def operation_type(self):
        r"""Gets the operation_type of this BudgetRecordInfo.

        |参数名称：操作类别| |参数的约束及描述：范围限制：0-10。SETTING：设置 DELETE：解除关联关系。|

        :return: The operation_type of this BudgetRecordInfo.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this BudgetRecordInfo.

        |参数名称：操作类别| |参数的约束及描述：范围限制：0-10。SETTING：设置 DELETE：解除关联关系。|

        :param operation_type: The operation_type of this BudgetRecordInfo.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def operation_time(self):
        r"""Gets the operation_time of this BudgetRecordInfo.

        |参数名称：操作时间| |参数的约束及描述：UTC时间，格式为：yyyy-MM-ddTHH:mm:ssZ。|

        :return: The operation_time of this BudgetRecordInfo.
        :rtype: str
        """
        return self._operation_time

    @operation_time.setter
    def operation_time(self, operation_time):
        r"""Sets the operation_time of this BudgetRecordInfo.

        |参数名称：操作时间| |参数的约束及描述：UTC时间，格式为：yyyy-MM-ddTHH:mm:ssZ。|

        :param operation_time: The operation_time of this BudgetRecordInfo.
        :type operation_time: str
        """
        self._operation_time = operation_time

    @property
    def operator(self):
        r"""Gets the operator of this BudgetRecordInfo.

        |参数名称：操作员或系统system| |参数的约束及描述：范围限制：0-64|

        :return: The operator of this BudgetRecordInfo.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this BudgetRecordInfo.

        |参数名称：操作员或系统system| |参数的约束及描述：范围限制：0-64|

        :param operator: The operator of this BudgetRecordInfo.
        :type operator: str
        """
        self._operator = operator

    @property
    def budget_type(self):
        r"""Gets the budget_type of this BudgetRecordInfo.

        |参数名称：预算模式| |参数的约束及描述：范围限制：0-10。MONTHLY：月度预算 PACKAGE：一次性预算|

        :return: The budget_type of this BudgetRecordInfo.
        :rtype: str
        """
        return self._budget_type

    @budget_type.setter
    def budget_type(self, budget_type):
        r"""Sets the budget_type of this BudgetRecordInfo.

        |参数名称：预算模式| |参数的约束及描述：范围限制：0-10。MONTHLY：月度预算 PACKAGE：一次性预算|

        :param budget_type: The budget_type of this BudgetRecordInfo.
        :type budget_type: str
        """
        self._budget_type = budget_type

    @property
    def partner_corp_name(self):
        r"""Gets the partner_corp_name of this BudgetRecordInfo.

        |参数名称：伙伴名称| |参数的约束及描述：范围限制：0-256|

        :return: The partner_corp_name of this BudgetRecordInfo.
        :rtype: str
        """
        return self._partner_corp_name

    @partner_corp_name.setter
    def partner_corp_name(self, partner_corp_name):
        r"""Sets the partner_corp_name of this BudgetRecordInfo.

        |参数名称：伙伴名称| |参数的约束及描述：范围限制：0-256|

        :param partner_corp_name: The partner_corp_name of this BudgetRecordInfo.
        :type partner_corp_name: str
        """
        self._partner_corp_name = partner_corp_name

    @property
    def partner_account_name(self):
        r"""Gets the partner_account_name of this BudgetRecordInfo.

        |参数名称：伙伴账号名| |参数的约束及描述：范围限制：0-128|

        :return: The partner_account_name of this BudgetRecordInfo.
        :rtype: str
        """
        return self._partner_account_name

    @partner_account_name.setter
    def partner_account_name(self, partner_account_name):
        r"""Sets the partner_account_name of this BudgetRecordInfo.

        |参数名称：伙伴账号名| |参数的约束及描述：范围限制：0-128|

        :param partner_account_name: The partner_account_name of this BudgetRecordInfo.
        :type partner_account_name: str
        """
        self._partner_account_name = partner_account_name

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
        if not isinstance(other, BudgetRecordInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
