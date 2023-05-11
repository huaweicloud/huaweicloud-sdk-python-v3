# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InvoiceRequestInfoIntl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'cancel_reason': 'str',
        'title_type': 'int',
        'channel_type': 'int',
        'invoice_type': 'int',
        'invoice_title': 'str',
        'invoice_amount': 'float',
        'invoice_method': 'int',
        'invoice_class': 'int',
        'invoice_state': 'int',
        'apply_opera': 'str',
        'address_info': 'PostAddressInfoIntl',
        'apply_time': 'str',
        'invoice_mode': 'str',
        'email': 'str',
        'request_mode': 'str',
        'src_request_id': 'str',
        'sales_id': 'str',
        'invoice_no': 'str',
        'trade_type': 'int',
        'bill_cycle': 'str',
        'tax_list': 'list[TaxInfo]'
    }

    attribute_map = {
        'request_id': 'requestId',
        'cancel_reason': 'cancelReason',
        'title_type': 'titleType',
        'channel_type': 'channelType',
        'invoice_type': 'invoiceType',
        'invoice_title': 'invoiceTitle',
        'invoice_amount': 'invoiceAmount',
        'invoice_method': 'invoiceMethod',
        'invoice_class': 'invoiceClass',
        'invoice_state': 'invoiceState',
        'apply_opera': 'applyOpera',
        'address_info': 'addressInfo',
        'apply_time': 'applyTime',
        'invoice_mode': 'invoiceMode',
        'email': 'email',
        'request_mode': 'requestMode',
        'src_request_id': 'srcRequestId',
        'sales_id': 'salesId',
        'invoice_no': 'invoiceNo',
        'trade_type': 'tradeType',
        'bill_cycle': 'billCycle',
        'tax_list': 'taxList'
    }

    def __init__(self, request_id=None, cancel_reason=None, title_type=None, channel_type=None, invoice_type=None, invoice_title=None, invoice_amount=None, invoice_method=None, invoice_class=None, invoice_state=None, apply_opera=None, address_info=None, apply_time=None, invoice_mode=None, email=None, request_mode=None, src_request_id=None, sales_id=None, invoice_no=None, trade_type=None, bill_cycle=None, tax_list=None):
        """InvoiceRequestInfoIntl

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。
        :type request_id: str
        :param cancel_reason: 驳回原因。
        :type cancel_reason: str
        :param title_type: 开票类型。 0：个人1：企业
        :type title_type: int
        :param channel_type: 渠道类型。 0：华为云
        :type channel_type: int
        :param invoice_type: 发票种类。 0：增值税专用发票1：增值税普通发票
        :type invoice_type: int
        :param invoice_title: 发票抬头。
        :type invoice_title: str
        :param invoice_amount: 已开票金额（美元） 。
        :type invoice_amount: float
        :param invoice_method: 开票方式。 0：账期1：到账2：订单
        :type invoice_method: int
        :param invoice_class: 发票类别。 0：税票1：商票
        :type invoice_class: int
        :param invoice_state: 开票状态。 0：草稿1：待审核4：等待导出发票文件5：等待发票文件回填6：等待邮寄确认7：等待回执确认8：完成9：已退票11：等待驳回审核13：退票待审核14：待退票状态回填15：退票失败
        :type invoice_state: int
        :param apply_opera: 发票申请人员。
        :type apply_opera: str
        :param address_info: 
        :type address_info: :class:`huaweicloudsdkbssintl.v2.PostAddressInfoIntl`
        :param apply_time: 申请时间（UTC时间）。
        :type apply_time: str
        :param invoice_mode: 发票类型。 0：纸质票
        :type invoice_mode: str
        :param email: 电子发票寄送地。
        :type email: str
        :param request_mode: 申请类型。 0：开票申请1：退票申请2：正向开票已退票
        :type request_mode: str
        :param src_request_id: 退票时的原申请ID。
        :type src_request_id: str
        :param sales_id: 签约主体ID。
        :type sales_id: str
        :param invoice_no: 发票号码。
        :type invoice_no: str
        :param trade_type: 交易类型。 3：结算信用卡扣减4：结算未结清开票5：先开票后到款6：BP月结开票7：充值开票8：包年/包月在线支付开票10：普通提现开票
        :type trade_type: int
        :param bill_cycle: 发票账期。
        :type bill_cycle: str
        :param tax_list: 税务信息列表，参见表4。
        :type tax_list: list[:class:`huaweicloudsdkbssintl.v2.TaxInfo`]
        """
        
        

        self._request_id = None
        self._cancel_reason = None
        self._title_type = None
        self._channel_type = None
        self._invoice_type = None
        self._invoice_title = None
        self._invoice_amount = None
        self._invoice_method = None
        self._invoice_class = None
        self._invoice_state = None
        self._apply_opera = None
        self._address_info = None
        self._apply_time = None
        self._invoice_mode = None
        self._email = None
        self._request_mode = None
        self._src_request_id = None
        self._sales_id = None
        self._invoice_no = None
        self._trade_type = None
        self._bill_cycle = None
        self._tax_list = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if cancel_reason is not None:
            self.cancel_reason = cancel_reason
        if title_type is not None:
            self.title_type = title_type
        if channel_type is not None:
            self.channel_type = channel_type
        if invoice_type is not None:
            self.invoice_type = invoice_type
        if invoice_title is not None:
            self.invoice_title = invoice_title
        if invoice_amount is not None:
            self.invoice_amount = invoice_amount
        if invoice_method is not None:
            self.invoice_method = invoice_method
        if invoice_class is not None:
            self.invoice_class = invoice_class
        if invoice_state is not None:
            self.invoice_state = invoice_state
        if apply_opera is not None:
            self.apply_opera = apply_opera
        if address_info is not None:
            self.address_info = address_info
        if apply_time is not None:
            self.apply_time = apply_time
        if invoice_mode is not None:
            self.invoice_mode = invoice_mode
        if email is not None:
            self.email = email
        if request_mode is not None:
            self.request_mode = request_mode
        if src_request_id is not None:
            self.src_request_id = src_request_id
        if sales_id is not None:
            self.sales_id = sales_id
        if invoice_no is not None:
            self.invoice_no = invoice_no
        if trade_type is not None:
            self.trade_type = trade_type
        if bill_cycle is not None:
            self.bill_cycle = bill_cycle
        if tax_list is not None:
            self.tax_list = tax_list

    @property
    def request_id(self):
        """Gets the request_id of this InvoiceRequestInfoIntl.

        请求ID。

        :return: The request_id of this InvoiceRequestInfoIntl.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this InvoiceRequestInfoIntl.

        请求ID。

        :param request_id: The request_id of this InvoiceRequestInfoIntl.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def cancel_reason(self):
        """Gets the cancel_reason of this InvoiceRequestInfoIntl.

        驳回原因。

        :return: The cancel_reason of this InvoiceRequestInfoIntl.
        :rtype: str
        """
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, cancel_reason):
        """Sets the cancel_reason of this InvoiceRequestInfoIntl.

        驳回原因。

        :param cancel_reason: The cancel_reason of this InvoiceRequestInfoIntl.
        :type cancel_reason: str
        """
        self._cancel_reason = cancel_reason

    @property
    def title_type(self):
        """Gets the title_type of this InvoiceRequestInfoIntl.

        开票类型。 0：个人1：企业

        :return: The title_type of this InvoiceRequestInfoIntl.
        :rtype: int
        """
        return self._title_type

    @title_type.setter
    def title_type(self, title_type):
        """Sets the title_type of this InvoiceRequestInfoIntl.

        开票类型。 0：个人1：企业

        :param title_type: The title_type of this InvoiceRequestInfoIntl.
        :type title_type: int
        """
        self._title_type = title_type

    @property
    def channel_type(self):
        """Gets the channel_type of this InvoiceRequestInfoIntl.

        渠道类型。 0：华为云

        :return: The channel_type of this InvoiceRequestInfoIntl.
        :rtype: int
        """
        return self._channel_type

    @channel_type.setter
    def channel_type(self, channel_type):
        """Sets the channel_type of this InvoiceRequestInfoIntl.

        渠道类型。 0：华为云

        :param channel_type: The channel_type of this InvoiceRequestInfoIntl.
        :type channel_type: int
        """
        self._channel_type = channel_type

    @property
    def invoice_type(self):
        """Gets the invoice_type of this InvoiceRequestInfoIntl.

        发票种类。 0：增值税专用发票1：增值税普通发票

        :return: The invoice_type of this InvoiceRequestInfoIntl.
        :rtype: int
        """
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, invoice_type):
        """Sets the invoice_type of this InvoiceRequestInfoIntl.

        发票种类。 0：增值税专用发票1：增值税普通发票

        :param invoice_type: The invoice_type of this InvoiceRequestInfoIntl.
        :type invoice_type: int
        """
        self._invoice_type = invoice_type

    @property
    def invoice_title(self):
        """Gets the invoice_title of this InvoiceRequestInfoIntl.

        发票抬头。

        :return: The invoice_title of this InvoiceRequestInfoIntl.
        :rtype: str
        """
        return self._invoice_title

    @invoice_title.setter
    def invoice_title(self, invoice_title):
        """Sets the invoice_title of this InvoiceRequestInfoIntl.

        发票抬头。

        :param invoice_title: The invoice_title of this InvoiceRequestInfoIntl.
        :type invoice_title: str
        """
        self._invoice_title = invoice_title

    @property
    def invoice_amount(self):
        """Gets the invoice_amount of this InvoiceRequestInfoIntl.

        已开票金额（美元） 。

        :return: The invoice_amount of this InvoiceRequestInfoIntl.
        :rtype: float
        """
        return self._invoice_amount

    @invoice_amount.setter
    def invoice_amount(self, invoice_amount):
        """Sets the invoice_amount of this InvoiceRequestInfoIntl.

        已开票金额（美元） 。

        :param invoice_amount: The invoice_amount of this InvoiceRequestInfoIntl.
        :type invoice_amount: float
        """
        self._invoice_amount = invoice_amount

    @property
    def invoice_method(self):
        """Gets the invoice_method of this InvoiceRequestInfoIntl.

        开票方式。 0：账期1：到账2：订单

        :return: The invoice_method of this InvoiceRequestInfoIntl.
        :rtype: int
        """
        return self._invoice_method

    @invoice_method.setter
    def invoice_method(self, invoice_method):
        """Sets the invoice_method of this InvoiceRequestInfoIntl.

        开票方式。 0：账期1：到账2：订单

        :param invoice_method: The invoice_method of this InvoiceRequestInfoIntl.
        :type invoice_method: int
        """
        self._invoice_method = invoice_method

    @property
    def invoice_class(self):
        """Gets the invoice_class of this InvoiceRequestInfoIntl.

        发票类别。 0：税票1：商票

        :return: The invoice_class of this InvoiceRequestInfoIntl.
        :rtype: int
        """
        return self._invoice_class

    @invoice_class.setter
    def invoice_class(self, invoice_class):
        """Sets the invoice_class of this InvoiceRequestInfoIntl.

        发票类别。 0：税票1：商票

        :param invoice_class: The invoice_class of this InvoiceRequestInfoIntl.
        :type invoice_class: int
        """
        self._invoice_class = invoice_class

    @property
    def invoice_state(self):
        """Gets the invoice_state of this InvoiceRequestInfoIntl.

        开票状态。 0：草稿1：待审核4：等待导出发票文件5：等待发票文件回填6：等待邮寄确认7：等待回执确认8：完成9：已退票11：等待驳回审核13：退票待审核14：待退票状态回填15：退票失败

        :return: The invoice_state of this InvoiceRequestInfoIntl.
        :rtype: int
        """
        return self._invoice_state

    @invoice_state.setter
    def invoice_state(self, invoice_state):
        """Sets the invoice_state of this InvoiceRequestInfoIntl.

        开票状态。 0：草稿1：待审核4：等待导出发票文件5：等待发票文件回填6：等待邮寄确认7：等待回执确认8：完成9：已退票11：等待驳回审核13：退票待审核14：待退票状态回填15：退票失败

        :param invoice_state: The invoice_state of this InvoiceRequestInfoIntl.
        :type invoice_state: int
        """
        self._invoice_state = invoice_state

    @property
    def apply_opera(self):
        """Gets the apply_opera of this InvoiceRequestInfoIntl.

        发票申请人员。

        :return: The apply_opera of this InvoiceRequestInfoIntl.
        :rtype: str
        """
        return self._apply_opera

    @apply_opera.setter
    def apply_opera(self, apply_opera):
        """Sets the apply_opera of this InvoiceRequestInfoIntl.

        发票申请人员。

        :param apply_opera: The apply_opera of this InvoiceRequestInfoIntl.
        :type apply_opera: str
        """
        self._apply_opera = apply_opera

    @property
    def address_info(self):
        """Gets the address_info of this InvoiceRequestInfoIntl.

        :return: The address_info of this InvoiceRequestInfoIntl.
        :rtype: :class:`huaweicloudsdkbssintl.v2.PostAddressInfoIntl`
        """
        return self._address_info

    @address_info.setter
    def address_info(self, address_info):
        """Sets the address_info of this InvoiceRequestInfoIntl.

        :param address_info: The address_info of this InvoiceRequestInfoIntl.
        :type address_info: :class:`huaweicloudsdkbssintl.v2.PostAddressInfoIntl`
        """
        self._address_info = address_info

    @property
    def apply_time(self):
        """Gets the apply_time of this InvoiceRequestInfoIntl.

        申请时间（UTC时间）。

        :return: The apply_time of this InvoiceRequestInfoIntl.
        :rtype: str
        """
        return self._apply_time

    @apply_time.setter
    def apply_time(self, apply_time):
        """Sets the apply_time of this InvoiceRequestInfoIntl.

        申请时间（UTC时间）。

        :param apply_time: The apply_time of this InvoiceRequestInfoIntl.
        :type apply_time: str
        """
        self._apply_time = apply_time

    @property
    def invoice_mode(self):
        """Gets the invoice_mode of this InvoiceRequestInfoIntl.

        发票类型。 0：纸质票

        :return: The invoice_mode of this InvoiceRequestInfoIntl.
        :rtype: str
        """
        return self._invoice_mode

    @invoice_mode.setter
    def invoice_mode(self, invoice_mode):
        """Sets the invoice_mode of this InvoiceRequestInfoIntl.

        发票类型。 0：纸质票

        :param invoice_mode: The invoice_mode of this InvoiceRequestInfoIntl.
        :type invoice_mode: str
        """
        self._invoice_mode = invoice_mode

    @property
    def email(self):
        """Gets the email of this InvoiceRequestInfoIntl.

        电子发票寄送地。

        :return: The email of this InvoiceRequestInfoIntl.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InvoiceRequestInfoIntl.

        电子发票寄送地。

        :param email: The email of this InvoiceRequestInfoIntl.
        :type email: str
        """
        self._email = email

    @property
    def request_mode(self):
        """Gets the request_mode of this InvoiceRequestInfoIntl.

        申请类型。 0：开票申请1：退票申请2：正向开票已退票

        :return: The request_mode of this InvoiceRequestInfoIntl.
        :rtype: str
        """
        return self._request_mode

    @request_mode.setter
    def request_mode(self, request_mode):
        """Sets the request_mode of this InvoiceRequestInfoIntl.

        申请类型。 0：开票申请1：退票申请2：正向开票已退票

        :param request_mode: The request_mode of this InvoiceRequestInfoIntl.
        :type request_mode: str
        """
        self._request_mode = request_mode

    @property
    def src_request_id(self):
        """Gets the src_request_id of this InvoiceRequestInfoIntl.

        退票时的原申请ID。

        :return: The src_request_id of this InvoiceRequestInfoIntl.
        :rtype: str
        """
        return self._src_request_id

    @src_request_id.setter
    def src_request_id(self, src_request_id):
        """Sets the src_request_id of this InvoiceRequestInfoIntl.

        退票时的原申请ID。

        :param src_request_id: The src_request_id of this InvoiceRequestInfoIntl.
        :type src_request_id: str
        """
        self._src_request_id = src_request_id

    @property
    def sales_id(self):
        """Gets the sales_id of this InvoiceRequestInfoIntl.

        签约主体ID。

        :return: The sales_id of this InvoiceRequestInfoIntl.
        :rtype: str
        """
        return self._sales_id

    @sales_id.setter
    def sales_id(self, sales_id):
        """Sets the sales_id of this InvoiceRequestInfoIntl.

        签约主体ID。

        :param sales_id: The sales_id of this InvoiceRequestInfoIntl.
        :type sales_id: str
        """
        self._sales_id = sales_id

    @property
    def invoice_no(self):
        """Gets the invoice_no of this InvoiceRequestInfoIntl.

        发票号码。

        :return: The invoice_no of this InvoiceRequestInfoIntl.
        :rtype: str
        """
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, invoice_no):
        """Sets the invoice_no of this InvoiceRequestInfoIntl.

        发票号码。

        :param invoice_no: The invoice_no of this InvoiceRequestInfoIntl.
        :type invoice_no: str
        """
        self._invoice_no = invoice_no

    @property
    def trade_type(self):
        """Gets the trade_type of this InvoiceRequestInfoIntl.

        交易类型。 3：结算信用卡扣减4：结算未结清开票5：先开票后到款6：BP月结开票7：充值开票8：包年/包月在线支付开票10：普通提现开票

        :return: The trade_type of this InvoiceRequestInfoIntl.
        :rtype: int
        """
        return self._trade_type

    @trade_type.setter
    def trade_type(self, trade_type):
        """Sets the trade_type of this InvoiceRequestInfoIntl.

        交易类型。 3：结算信用卡扣减4：结算未结清开票5：先开票后到款6：BP月结开票7：充值开票8：包年/包月在线支付开票10：普通提现开票

        :param trade_type: The trade_type of this InvoiceRequestInfoIntl.
        :type trade_type: int
        """
        self._trade_type = trade_type

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this InvoiceRequestInfoIntl.

        发票账期。

        :return: The bill_cycle of this InvoiceRequestInfoIntl.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this InvoiceRequestInfoIntl.

        发票账期。

        :param bill_cycle: The bill_cycle of this InvoiceRequestInfoIntl.
        :type bill_cycle: str
        """
        self._bill_cycle = bill_cycle

    @property
    def tax_list(self):
        """Gets the tax_list of this InvoiceRequestInfoIntl.

        税务信息列表，参见表4。

        :return: The tax_list of this InvoiceRequestInfoIntl.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.TaxInfo`]
        """
        return self._tax_list

    @tax_list.setter
    def tax_list(self, tax_list):
        """Sets the tax_list of this InvoiceRequestInfoIntl.

        税务信息列表，参见表4。

        :param tax_list: The tax_list of this InvoiceRequestInfoIntl.
        :type tax_list: list[:class:`huaweicloudsdkbssintl.v2.TaxInfo`]
        """
        self._tax_list = tax_list

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
        if not isinstance(other, InvoiceRequestInfoIntl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
