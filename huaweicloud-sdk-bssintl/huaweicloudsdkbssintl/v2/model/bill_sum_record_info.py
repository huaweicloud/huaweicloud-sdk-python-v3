# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BillSumRecordInfo:

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
        'resource_type_code': 'str',
        'region_code': 'str',
        'cloud_service_type_code': 'str',
        'consume_time': 'str',
        'pay_method': 'str',
        'consume_amount': 'float',
        'debt': 'float',
        'discount': 'float',
        'measure_id': 'int',
        'bill_type': 'int',
        'account_details': 'list[BalanceTypePay]',
        'discount_detail_infos': 'list[DiscountDetailInfo]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'resource_type_code': 'resource_type_code',
        'region_code': 'region_code',
        'cloud_service_type_code': 'cloud_service_type_code',
        'consume_time': 'consume_time',
        'pay_method': 'pay_method',
        'consume_amount': 'consume_amount',
        'debt': 'debt',
        'discount': 'discount',
        'measure_id': 'measure_id',
        'bill_type': 'bill_type',
        'account_details': 'account_details',
        'discount_detail_infos': 'discount_detail_infos',
        'enterprise_project_id': 'enterpriseProjectId'
    }

    def __init__(self, customer_id=None, resource_type_code=None, region_code=None, cloud_service_type_code=None, consume_time=None, pay_method=None, consume_amount=None, debt=None, discount=None, measure_id=None, bill_type=None, account_details=None, discount_detail_infos=None, enterprise_project_id=None):
        """BillSumRecordInfo

        The model defined in huaweicloud sdk

        :param customer_id: 客户账号ID。
        :type customer_id: str
        :param resource_type_code: 资源类型编码，例如ECS的VM为“hws.resource.type.vm”。  说明： 当请求消息中不传递“cloud_service_type_code”参数时，此值返回“null”。
        :type resource_type_code: str
        :param region_code: 云服务区，该字段预留，先不使用。
        :type region_code: str
        :param cloud_service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。
        :type cloud_service_type_code: str
        :param consume_time: 消费统计的时期。 格式为YYYY-MM。 示例：2018-05
        :type consume_time: str
        :param pay_method: 消费类型。 当请求消息中不传递“cloud_service_type_code”参数时，如果此值返回“0”表示此服务类型下所有的资源类型都是包年/包月计费模式，如果此值返回空字符串表示此服务类型下有资源类型为按需计费模式。当请求消息中传递“cloud_service_type_code”参数时，如果此值返回“0”表示此资源类型是包年/包月计费模式，如果此值返回“1”表示此资源类型为按需计费模式。
        :type pay_method: str
        :param consume_amount: 消费的金额，即从客户账户实际扣除的金额。包含代金券支付的金额。
        :type consume_amount: float
        :param debt: 欠费金额，即从客户账户扣费的时候，客户账户金额不足，欠费的金额。
        :type debt: float
        :param discount: 折扣金额。
        :type discount: float
        :param measure_id: 金额单位。 1：元3：分 默认值为3。
        :type measure_id: int
        :param bill_type: 账单类型。 0：消费1：退订
        :type bill_type: int
        :param account_details: 按不同账户消费类型和付费方式区分的支付总金额。 具体请参见表4。
        :type account_details: list[:class:`huaweicloudsdkbssintl.v2.BalanceTypePay`]
        :param discount_detail_infos: 折扣金额详情。 具体请参见表5。 当bill_type为1时，不返回此参数。
        :type discount_detail_infos: list[:class:`huaweicloudsdkbssintl.v2.DiscountDetailInfo`]
        :param enterprise_project_id: 企业项目ID。 当请求参数中传递了“enterpriseProjectId”，响应参数“bill_sums”返回以企业项目ID为维度的账单记录。
        :type enterprise_project_id: str
        """
        
        

        self._customer_id = None
        self._resource_type_code = None
        self._region_code = None
        self._cloud_service_type_code = None
        self._consume_time = None
        self._pay_method = None
        self._consume_amount = None
        self._debt = None
        self._discount = None
        self._measure_id = None
        self._bill_type = None
        self._account_details = None
        self._discount_detail_infos = None
        self._enterprise_project_id = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if region_code is not None:
            self.region_code = region_code
        if cloud_service_type_code is not None:
            self.cloud_service_type_code = cloud_service_type_code
        if consume_time is not None:
            self.consume_time = consume_time
        if pay_method is not None:
            self.pay_method = pay_method
        if consume_amount is not None:
            self.consume_amount = consume_amount
        if debt is not None:
            self.debt = debt
        if discount is not None:
            self.discount = discount
        if measure_id is not None:
            self.measure_id = measure_id
        if bill_type is not None:
            self.bill_type = bill_type
        if account_details is not None:
            self.account_details = account_details
        if discount_detail_infos is not None:
            self.discount_detail_infos = discount_detail_infos
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def customer_id(self):
        """Gets the customer_id of this BillSumRecordInfo.

        客户账号ID。

        :return: The customer_id of this BillSumRecordInfo.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this BillSumRecordInfo.

        客户账号ID。

        :param customer_id: The customer_id of this BillSumRecordInfo.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this BillSumRecordInfo.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。  说明： 当请求消息中不传递“cloud_service_type_code”参数时，此值返回“null”。

        :return: The resource_type_code of this BillSumRecordInfo.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this BillSumRecordInfo.

        资源类型编码，例如ECS的VM为“hws.resource.type.vm”。  说明： 当请求消息中不传递“cloud_service_type_code”参数时，此值返回“null”。

        :param resource_type_code: The resource_type_code of this BillSumRecordInfo.
        :type resource_type_code: str
        """
        self._resource_type_code = resource_type_code

    @property
    def region_code(self):
        """Gets the region_code of this BillSumRecordInfo.

        云服务区，该字段预留，先不使用。

        :return: The region_code of this BillSumRecordInfo.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this BillSumRecordInfo.

        云服务区，该字段预留，先不使用。

        :param region_code: The region_code of this BillSumRecordInfo.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def cloud_service_type_code(self):
        """Gets the cloud_service_type_code of this BillSumRecordInfo.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。

        :return: The cloud_service_type_code of this BillSumRecordInfo.
        :rtype: str
        """
        return self._cloud_service_type_code

    @cloud_service_type_code.setter
    def cloud_service_type_code(self, cloud_service_type_code):
        """Sets the cloud_service_type_code of this BillSumRecordInfo.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。

        :param cloud_service_type_code: The cloud_service_type_code of this BillSumRecordInfo.
        :type cloud_service_type_code: str
        """
        self._cloud_service_type_code = cloud_service_type_code

    @property
    def consume_time(self):
        """Gets the consume_time of this BillSumRecordInfo.

        消费统计的时期。 格式为YYYY-MM。 示例：2018-05

        :return: The consume_time of this BillSumRecordInfo.
        :rtype: str
        """
        return self._consume_time

    @consume_time.setter
    def consume_time(self, consume_time):
        """Sets the consume_time of this BillSumRecordInfo.

        消费统计的时期。 格式为YYYY-MM。 示例：2018-05

        :param consume_time: The consume_time of this BillSumRecordInfo.
        :type consume_time: str
        """
        self._consume_time = consume_time

    @property
    def pay_method(self):
        """Gets the pay_method of this BillSumRecordInfo.

        消费类型。 当请求消息中不传递“cloud_service_type_code”参数时，如果此值返回“0”表示此服务类型下所有的资源类型都是包年/包月计费模式，如果此值返回空字符串表示此服务类型下有资源类型为按需计费模式。当请求消息中传递“cloud_service_type_code”参数时，如果此值返回“0”表示此资源类型是包年/包月计费模式，如果此值返回“1”表示此资源类型为按需计费模式。

        :return: The pay_method of this BillSumRecordInfo.
        :rtype: str
        """
        return self._pay_method

    @pay_method.setter
    def pay_method(self, pay_method):
        """Sets the pay_method of this BillSumRecordInfo.

        消费类型。 当请求消息中不传递“cloud_service_type_code”参数时，如果此值返回“0”表示此服务类型下所有的资源类型都是包年/包月计费模式，如果此值返回空字符串表示此服务类型下有资源类型为按需计费模式。当请求消息中传递“cloud_service_type_code”参数时，如果此值返回“0”表示此资源类型是包年/包月计费模式，如果此值返回“1”表示此资源类型为按需计费模式。

        :param pay_method: The pay_method of this BillSumRecordInfo.
        :type pay_method: str
        """
        self._pay_method = pay_method

    @property
    def consume_amount(self):
        """Gets the consume_amount of this BillSumRecordInfo.

        消费的金额，即从客户账户实际扣除的金额。包含代金券支付的金额。

        :return: The consume_amount of this BillSumRecordInfo.
        :rtype: float
        """
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, consume_amount):
        """Sets the consume_amount of this BillSumRecordInfo.

        消费的金额，即从客户账户实际扣除的金额。包含代金券支付的金额。

        :param consume_amount: The consume_amount of this BillSumRecordInfo.
        :type consume_amount: float
        """
        self._consume_amount = consume_amount

    @property
    def debt(self):
        """Gets the debt of this BillSumRecordInfo.

        欠费金额，即从客户账户扣费的时候，客户账户金额不足，欠费的金额。

        :return: The debt of this BillSumRecordInfo.
        :rtype: float
        """
        return self._debt

    @debt.setter
    def debt(self, debt):
        """Sets the debt of this BillSumRecordInfo.

        欠费金额，即从客户账户扣费的时候，客户账户金额不足，欠费的金额。

        :param debt: The debt of this BillSumRecordInfo.
        :type debt: float
        """
        self._debt = debt

    @property
    def discount(self):
        """Gets the discount of this BillSumRecordInfo.

        折扣金额。

        :return: The discount of this BillSumRecordInfo.
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this BillSumRecordInfo.

        折扣金额。

        :param discount: The discount of this BillSumRecordInfo.
        :type discount: float
        """
        self._discount = discount

    @property
    def measure_id(self):
        """Gets the measure_id of this BillSumRecordInfo.

        金额单位。 1：元3：分 默认值为3。

        :return: The measure_id of this BillSumRecordInfo.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this BillSumRecordInfo.

        金额单位。 1：元3：分 默认值为3。

        :param measure_id: The measure_id of this BillSumRecordInfo.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def bill_type(self):
        """Gets the bill_type of this BillSumRecordInfo.

        账单类型。 0：消费1：退订

        :return: The bill_type of this BillSumRecordInfo.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this BillSumRecordInfo.

        账单类型。 0：消费1：退订

        :param bill_type: The bill_type of this BillSumRecordInfo.
        :type bill_type: int
        """
        self._bill_type = bill_type

    @property
    def account_details(self):
        """Gets the account_details of this BillSumRecordInfo.

        按不同账户消费类型和付费方式区分的支付总金额。 具体请参见表4。

        :return: The account_details of this BillSumRecordInfo.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.BalanceTypePay`]
        """
        return self._account_details

    @account_details.setter
    def account_details(self, account_details):
        """Sets the account_details of this BillSumRecordInfo.

        按不同账户消费类型和付费方式区分的支付总金额。 具体请参见表4。

        :param account_details: The account_details of this BillSumRecordInfo.
        :type account_details: list[:class:`huaweicloudsdkbssintl.v2.BalanceTypePay`]
        """
        self._account_details = account_details

    @property
    def discount_detail_infos(self):
        """Gets the discount_detail_infos of this BillSumRecordInfo.

        折扣金额详情。 具体请参见表5。 当bill_type为1时，不返回此参数。

        :return: The discount_detail_infos of this BillSumRecordInfo.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.DiscountDetailInfo`]
        """
        return self._discount_detail_infos

    @discount_detail_infos.setter
    def discount_detail_infos(self, discount_detail_infos):
        """Sets the discount_detail_infos of this BillSumRecordInfo.

        折扣金额详情。 具体请参见表5。 当bill_type为1时，不返回此参数。

        :param discount_detail_infos: The discount_detail_infos of this BillSumRecordInfo.
        :type discount_detail_infos: list[:class:`huaweicloudsdkbssintl.v2.DiscountDetailInfo`]
        """
        self._discount_detail_infos = discount_detail_infos

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this BillSumRecordInfo.

        企业项目ID。 当请求参数中传递了“enterpriseProjectId”，响应参数“bill_sums”返回以企业项目ID为维度的账单记录。

        :return: The enterprise_project_id of this BillSumRecordInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this BillSumRecordInfo.

        企业项目ID。 当请求参数中传递了“enterpriseProjectId”，响应参数“bill_sums”返回以企业项目ID为维度的账单记录。

        :param enterprise_project_id: The enterprise_project_id of this BillSumRecordInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, BillSumRecordInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
