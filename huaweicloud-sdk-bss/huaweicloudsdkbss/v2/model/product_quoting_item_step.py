# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductQuotingItemStep:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'step_id': 'str',
        'step_no': 'str',
        'step_start': 'decimal.Decimal',
        'start_measure_id': 'int',
        'step_end': 'decimal.Decimal',
        'end_measure_id': 'int',
        'preferential_type': 'int',
        'sales_price': 'decimal.Decimal',
        'discount_ratio': 'decimal.Decimal',
        'pricing_basis': 'str'
    }

    attribute_map = {
        'step_id': 'step_id',
        'step_no': 'step_no',
        'step_start': 'step_start',
        'start_measure_id': 'start_measure_id',
        'step_end': 'step_end',
        'end_measure_id': 'end_measure_id',
        'preferential_type': 'preferential_type',
        'sales_price': 'sales_price',
        'discount_ratio': 'discount_ratio',
        'pricing_basis': 'pricing_basis'
    }

    def __init__(self, step_id=None, step_no=None, step_start=None, start_measure_id=None, step_end=None, end_measure_id=None, preferential_type=None, sales_price=None, discount_ratio=None, pricing_basis=None):
        r"""ProductQuotingItemStep

        The model defined in huaweicloud sdk

        :param step_id: 阶梯ID
        :type step_id: str
        :param step_no: 阶梯编号
        :type step_no: str
        :param step_start: 阶梯起始值
        :type step_start: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param start_measure_id: 起始值度量单位
        :type start_measure_id: int
        :param step_end: 阶梯结束值
        :type step_end: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param end_measure_id: 结束值度量单位（1：元/美元）
        :type end_measure_id: int
        :param preferential_type: 优惠方式：0：产品折扣，1：固定单价
        :type preferential_type: int
        :param sales_price: 固定单价（preferential_type&#x3D;1固定单价时有值）
        :type sales_price: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param discount_ratio: 折扣率（preferential_type&#x3D;0产品折扣时有值）
        :type discount_ratio: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param pricing_basis: 计费单位
        :type pricing_basis: str
        """
        
        

        self._step_id = None
        self._step_no = None
        self._step_start = None
        self._start_measure_id = None
        self._step_end = None
        self._end_measure_id = None
        self._preferential_type = None
        self._sales_price = None
        self._discount_ratio = None
        self._pricing_basis = None
        self.discriminator = None

        if step_id is not None:
            self.step_id = step_id
        if step_no is not None:
            self.step_no = step_no
        if step_start is not None:
            self.step_start = step_start
        if start_measure_id is not None:
            self.start_measure_id = start_measure_id
        if step_end is not None:
            self.step_end = step_end
        if end_measure_id is not None:
            self.end_measure_id = end_measure_id
        if preferential_type is not None:
            self.preferential_type = preferential_type
        if sales_price is not None:
            self.sales_price = sales_price
        if discount_ratio is not None:
            self.discount_ratio = discount_ratio
        if pricing_basis is not None:
            self.pricing_basis = pricing_basis

    @property
    def step_id(self):
        r"""Gets the step_id of this ProductQuotingItemStep.

        阶梯ID

        :return: The step_id of this ProductQuotingItemStep.
        :rtype: str
        """
        return self._step_id

    @step_id.setter
    def step_id(self, step_id):
        r"""Sets the step_id of this ProductQuotingItemStep.

        阶梯ID

        :param step_id: The step_id of this ProductQuotingItemStep.
        :type step_id: str
        """
        self._step_id = step_id

    @property
    def step_no(self):
        r"""Gets the step_no of this ProductQuotingItemStep.

        阶梯编号

        :return: The step_no of this ProductQuotingItemStep.
        :rtype: str
        """
        return self._step_no

    @step_no.setter
    def step_no(self, step_no):
        r"""Sets the step_no of this ProductQuotingItemStep.

        阶梯编号

        :param step_no: The step_no of this ProductQuotingItemStep.
        :type step_no: str
        """
        self._step_no = step_no

    @property
    def step_start(self):
        r"""Gets the step_start of this ProductQuotingItemStep.

        阶梯起始值

        :return: The step_start of this ProductQuotingItemStep.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._step_start

    @step_start.setter
    def step_start(self, step_start):
        r"""Sets the step_start of this ProductQuotingItemStep.

        阶梯起始值

        :param step_start: The step_start of this ProductQuotingItemStep.
        :type step_start: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._step_start = step_start

    @property
    def start_measure_id(self):
        r"""Gets the start_measure_id of this ProductQuotingItemStep.

        起始值度量单位

        :return: The start_measure_id of this ProductQuotingItemStep.
        :rtype: int
        """
        return self._start_measure_id

    @start_measure_id.setter
    def start_measure_id(self, start_measure_id):
        r"""Sets the start_measure_id of this ProductQuotingItemStep.

        起始值度量单位

        :param start_measure_id: The start_measure_id of this ProductQuotingItemStep.
        :type start_measure_id: int
        """
        self._start_measure_id = start_measure_id

    @property
    def step_end(self):
        r"""Gets the step_end of this ProductQuotingItemStep.

        阶梯结束值

        :return: The step_end of this ProductQuotingItemStep.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._step_end

    @step_end.setter
    def step_end(self, step_end):
        r"""Sets the step_end of this ProductQuotingItemStep.

        阶梯结束值

        :param step_end: The step_end of this ProductQuotingItemStep.
        :type step_end: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._step_end = step_end

    @property
    def end_measure_id(self):
        r"""Gets the end_measure_id of this ProductQuotingItemStep.

        结束值度量单位（1：元/美元）

        :return: The end_measure_id of this ProductQuotingItemStep.
        :rtype: int
        """
        return self._end_measure_id

    @end_measure_id.setter
    def end_measure_id(self, end_measure_id):
        r"""Sets the end_measure_id of this ProductQuotingItemStep.

        结束值度量单位（1：元/美元）

        :param end_measure_id: The end_measure_id of this ProductQuotingItemStep.
        :type end_measure_id: int
        """
        self._end_measure_id = end_measure_id

    @property
    def preferential_type(self):
        r"""Gets the preferential_type of this ProductQuotingItemStep.

        优惠方式：0：产品折扣，1：固定单价

        :return: The preferential_type of this ProductQuotingItemStep.
        :rtype: int
        """
        return self._preferential_type

    @preferential_type.setter
    def preferential_type(self, preferential_type):
        r"""Sets the preferential_type of this ProductQuotingItemStep.

        优惠方式：0：产品折扣，1：固定单价

        :param preferential_type: The preferential_type of this ProductQuotingItemStep.
        :type preferential_type: int
        """
        self._preferential_type = preferential_type

    @property
    def sales_price(self):
        r"""Gets the sales_price of this ProductQuotingItemStep.

        固定单价（preferential_type=1固定单价时有值）

        :return: The sales_price of this ProductQuotingItemStep.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._sales_price

    @sales_price.setter
    def sales_price(self, sales_price):
        r"""Sets the sales_price of this ProductQuotingItemStep.

        固定单价（preferential_type=1固定单价时有值）

        :param sales_price: The sales_price of this ProductQuotingItemStep.
        :type sales_price: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._sales_price = sales_price

    @property
    def discount_ratio(self):
        r"""Gets the discount_ratio of this ProductQuotingItemStep.

        折扣率（preferential_type=0产品折扣时有值）

        :return: The discount_ratio of this ProductQuotingItemStep.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._discount_ratio

    @discount_ratio.setter
    def discount_ratio(self, discount_ratio):
        r"""Sets the discount_ratio of this ProductQuotingItemStep.

        折扣率（preferential_type=0产品折扣时有值）

        :param discount_ratio: The discount_ratio of this ProductQuotingItemStep.
        :type discount_ratio: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._discount_ratio = discount_ratio

    @property
    def pricing_basis(self):
        r"""Gets the pricing_basis of this ProductQuotingItemStep.

        计费单位

        :return: The pricing_basis of this ProductQuotingItemStep.
        :rtype: str
        """
        return self._pricing_basis

    @pricing_basis.setter
    def pricing_basis(self, pricing_basis):
        r"""Sets the pricing_basis of this ProductQuotingItemStep.

        计费单位

        :param pricing_basis: The pricing_basis of this ProductQuotingItemStep.
        :type pricing_basis: str
        """
        self._pricing_basis = pricing_basis

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProductQuotingItemStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
