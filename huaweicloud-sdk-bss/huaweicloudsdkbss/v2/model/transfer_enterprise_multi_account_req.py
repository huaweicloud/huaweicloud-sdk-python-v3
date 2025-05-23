# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferEnterpriseMultiAccountReq:

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
        'amount': 'str',
        'trans_id': 'str',
        'balance_type': 'str',
        'expire_time': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'amount': 'amount',
        'trans_id': 'trans_id',
        'balance_type': 'balance_type',
        'expire_time': 'expire_time'
    }

    def __init__(self, customer_id=None, amount=None, trans_id=None, balance_type=None, expire_time=None):
        r"""TransferEnterpriseMultiAccountReq

        The model defined in huaweicloud sdk

        :param customer_id: 企业子账号的客户ID。您可以调用查询企业子账号列表接口，获取响应参数“id”的返回值。
        :type customer_id: str
        :param amount: 现金账户总划拨金额。 单位：元。取值大于0且精确到小数点后2位。
        :type amount: str
        :param trans_id: 交易序列号，用于防止重复提交。 如果接口调用方不传此参数的值，则系统自动生成。如果接口调用方传入此参数的值，请采用UUID保证全局唯一。
        :type trans_id: str
        :param balance_type: 账户类型： BALANCE_TYPE_DEBIT：余额账户（默认）BALANCE_TYPE_CREDIT：信用账户
        :type balance_type: str
        :param expire_time: 账户到期时间，UTC时间，格式为：2016-03-28T14:45:38Z。 只对信用账户有效，用于限制针对有效期到期时间等于该时间的信用账户余额进行拨款，精确到秒。如果查询信用账户可拨款余额的查询结果没有失效时间，表示永久有效，对于这种账本拨款的情况无需填写。
        :type expire_time: str
        """
        
        

        self._customer_id = None
        self._amount = None
        self._trans_id = None
        self._balance_type = None
        self._expire_time = None
        self.discriminator = None

        self.customer_id = customer_id
        self.amount = amount
        if trans_id is not None:
            self.trans_id = trans_id
        if balance_type is not None:
            self.balance_type = balance_type
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def customer_id(self):
        r"""Gets the customer_id of this TransferEnterpriseMultiAccountReq.

        企业子账号的客户ID。您可以调用查询企业子账号列表接口，获取响应参数“id”的返回值。

        :return: The customer_id of this TransferEnterpriseMultiAccountReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this TransferEnterpriseMultiAccountReq.

        企业子账号的客户ID。您可以调用查询企业子账号列表接口，获取响应参数“id”的返回值。

        :param customer_id: The customer_id of this TransferEnterpriseMultiAccountReq.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def amount(self):
        r"""Gets the amount of this TransferEnterpriseMultiAccountReq.

        现金账户总划拨金额。 单位：元。取值大于0且精确到小数点后2位。

        :return: The amount of this TransferEnterpriseMultiAccountReq.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this TransferEnterpriseMultiAccountReq.

        现金账户总划拨金额。 单位：元。取值大于0且精确到小数点后2位。

        :param amount: The amount of this TransferEnterpriseMultiAccountReq.
        :type amount: str
        """
        self._amount = amount

    @property
    def trans_id(self):
        r"""Gets the trans_id of this TransferEnterpriseMultiAccountReq.

        交易序列号，用于防止重复提交。 如果接口调用方不传此参数的值，则系统自动生成。如果接口调用方传入此参数的值，请采用UUID保证全局唯一。

        :return: The trans_id of this TransferEnterpriseMultiAccountReq.
        :rtype: str
        """
        return self._trans_id

    @trans_id.setter
    def trans_id(self, trans_id):
        r"""Sets the trans_id of this TransferEnterpriseMultiAccountReq.

        交易序列号，用于防止重复提交。 如果接口调用方不传此参数的值，则系统自动生成。如果接口调用方传入此参数的值，请采用UUID保证全局唯一。

        :param trans_id: The trans_id of this TransferEnterpriseMultiAccountReq.
        :type trans_id: str
        """
        self._trans_id = trans_id

    @property
    def balance_type(self):
        r"""Gets the balance_type of this TransferEnterpriseMultiAccountReq.

        账户类型： BALANCE_TYPE_DEBIT：余额账户（默认）BALANCE_TYPE_CREDIT：信用账户

        :return: The balance_type of this TransferEnterpriseMultiAccountReq.
        :rtype: str
        """
        return self._balance_type

    @balance_type.setter
    def balance_type(self, balance_type):
        r"""Sets the balance_type of this TransferEnterpriseMultiAccountReq.

        账户类型： BALANCE_TYPE_DEBIT：余额账户（默认）BALANCE_TYPE_CREDIT：信用账户

        :param balance_type: The balance_type of this TransferEnterpriseMultiAccountReq.
        :type balance_type: str
        """
        self._balance_type = balance_type

    @property
    def expire_time(self):
        r"""Gets the expire_time of this TransferEnterpriseMultiAccountReq.

        账户到期时间，UTC时间，格式为：2016-03-28T14:45:38Z。 只对信用账户有效，用于限制针对有效期到期时间等于该时间的信用账户余额进行拨款，精确到秒。如果查询信用账户可拨款余额的查询结果没有失效时间，表示永久有效，对于这种账本拨款的情况无需填写。

        :return: The expire_time of this TransferEnterpriseMultiAccountReq.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this TransferEnterpriseMultiAccountReq.

        账户到期时间，UTC时间，格式为：2016-03-28T14:45:38Z。 只对信用账户有效，用于限制针对有效期到期时间等于该时间的信用账户余额进行拨款，精确到秒。如果查询信用账户可拨款余额的查询结果没有失效时间，表示永久有效，对于这种账本拨款的情况无需填写。

        :param expire_time: The expire_time of this TransferEnterpriseMultiAccountReq.
        :type expire_time: str
        """
        self._expire_time = expire_time

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
        if not isinstance(other, TransferEnterpriseMultiAccountReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
