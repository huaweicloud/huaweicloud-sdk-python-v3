# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModSubCustomerBudgetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'budget_amount': 'float',
        'cancel_partner_frozen': 'str',
        'indirect_partner_id': 'str',
        'budget_type': 'str',
        'frozen_operate_type': 'int'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'budget_amount': 'budget_amount',
        'cancel_partner_frozen': 'cancel_partner_frozen',
        'indirect_partner_id': 'indirect_partner_id',
        'budget_type': 'budget_type',
        'frozen_operate_type': 'frozen_operate_type'
    }

    def __init__(self, customer_id=None, budget_amount=None, cancel_partner_frozen=None, indirect_partner_id=None, budget_type=None, frozen_operate_type=None):
        r"""ModSubCustomerBudgetReq

        The model defined in huaweicloud sdk

        :param customer_id: 客户账号ID。您可以调用查询客户列表接口获取customer_id。
        :type customer_id: str
        :param budget_amount: 调整的目标金额。 单位：元。精确至小数点后2位。
        :type budget_amount: float
        :param cancel_partner_frozen: 是否在设置客户预算的同时解除账号冻结： 0：否1：是 默认值为0。
        :type cancel_partner_frozen: str
        :param indirect_partner_id: 云经销商ID。获取方法请参见查询云经销商列表。如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。
        :type indirect_partner_id: str
        :param budget_type: |参数名称：预算模式| |参数的约束及描述：MONTHLY 月度预算 PACKAGE 一次性预算 ，此参数不携带或携带值为null时，默认值为MONTHLY。|
        :type budget_type: str
        :param frozen_operate_type: |参数名称：设置超预算时是否自动冻结| |参数的约束及描述：0：手工冻结 1：自动冻结，此参数不携带或携带值为null或携带值为空时，字段不生效。|
        :type frozen_operate_type: int
        """
        
        

        self._customer_id = None
        self._budget_amount = None
        self._cancel_partner_frozen = None
        self._indirect_partner_id = None
        self._budget_type = None
        self._frozen_operate_type = None
        self.discriminator = None

        self.customer_id = customer_id
        self.budget_amount = budget_amount
        if cancel_partner_frozen is not None:
            self.cancel_partner_frozen = cancel_partner_frozen
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if budget_type is not None:
            self.budget_type = budget_type
        if frozen_operate_type is not None:
            self.frozen_operate_type = frozen_operate_type

    @property
    def customer_id(self):
        r"""Gets the customer_id of this ModSubCustomerBudgetReq.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :return: The customer_id of this ModSubCustomerBudgetReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this ModSubCustomerBudgetReq.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :param customer_id: The customer_id of this ModSubCustomerBudgetReq.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def budget_amount(self):
        r"""Gets the budget_amount of this ModSubCustomerBudgetReq.

        调整的目标金额。 单位：元。精确至小数点后2位。

        :return: The budget_amount of this ModSubCustomerBudgetReq.
        :rtype: float
        """
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, budget_amount):
        r"""Sets the budget_amount of this ModSubCustomerBudgetReq.

        调整的目标金额。 单位：元。精确至小数点后2位。

        :param budget_amount: The budget_amount of this ModSubCustomerBudgetReq.
        :type budget_amount: float
        """
        self._budget_amount = budget_amount

    @property
    def cancel_partner_frozen(self):
        r"""Gets the cancel_partner_frozen of this ModSubCustomerBudgetReq.

        是否在设置客户预算的同时解除账号冻结： 0：否1：是 默认值为0。

        :return: The cancel_partner_frozen of this ModSubCustomerBudgetReq.
        :rtype: str
        """
        return self._cancel_partner_frozen

    @cancel_partner_frozen.setter
    def cancel_partner_frozen(self, cancel_partner_frozen):
        r"""Sets the cancel_partner_frozen of this ModSubCustomerBudgetReq.

        是否在设置客户预算的同时解除账号冻结： 0：否1：是 默认值为0。

        :param cancel_partner_frozen: The cancel_partner_frozen of this ModSubCustomerBudgetReq.
        :type cancel_partner_frozen: str
        """
        self._cancel_partner_frozen = cancel_partner_frozen

    @property
    def indirect_partner_id(self):
        r"""Gets the indirect_partner_id of this ModSubCustomerBudgetReq.

        云经销商ID。获取方法请参见查询云经销商列表。如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。

        :return: The indirect_partner_id of this ModSubCustomerBudgetReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        r"""Sets the indirect_partner_id of this ModSubCustomerBudgetReq.

        云经销商ID。获取方法请参见查询云经销商列表。如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。

        :param indirect_partner_id: The indirect_partner_id of this ModSubCustomerBudgetReq.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def budget_type(self):
        r"""Gets the budget_type of this ModSubCustomerBudgetReq.

        |参数名称：预算模式| |参数的约束及描述：MONTHLY 月度预算 PACKAGE 一次性预算 ，此参数不携带或携带值为null时，默认值为MONTHLY。|

        :return: The budget_type of this ModSubCustomerBudgetReq.
        :rtype: str
        """
        return self._budget_type

    @budget_type.setter
    def budget_type(self, budget_type):
        r"""Sets the budget_type of this ModSubCustomerBudgetReq.

        |参数名称：预算模式| |参数的约束及描述：MONTHLY 月度预算 PACKAGE 一次性预算 ，此参数不携带或携带值为null时，默认值为MONTHLY。|

        :param budget_type: The budget_type of this ModSubCustomerBudgetReq.
        :type budget_type: str
        """
        self._budget_type = budget_type

    @property
    def frozen_operate_type(self):
        r"""Gets the frozen_operate_type of this ModSubCustomerBudgetReq.

        |参数名称：设置超预算时是否自动冻结| |参数的约束及描述：0：手工冻结 1：自动冻结，此参数不携带或携带值为null或携带值为空时，字段不生效。|

        :return: The frozen_operate_type of this ModSubCustomerBudgetReq.
        :rtype: int
        """
        return self._frozen_operate_type

    @frozen_operate_type.setter
    def frozen_operate_type(self, frozen_operate_type):
        r"""Sets the frozen_operate_type of this ModSubCustomerBudgetReq.

        |参数名称：设置超预算时是否自动冻结| |参数的约束及描述：0：手工冻结 1：自动冻结，此参数不携带或携带值为null或携带值为空时，字段不生效。|

        :param frozen_operate_type: The frozen_operate_type of this ModSubCustomerBudgetReq.
        :type frozen_operate_type: int
        """
        self._frozen_operate_type = frozen_operate_type

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
        if not isinstance(other, ModSubCustomerBudgetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
