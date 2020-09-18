# coding: utf-8

import pprint
import re

import six





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
        """TransferEnterpriseMultiAccountReq - a model defined in huaweicloud sdk"""
        
        

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
        """Gets the customer_id of this TransferEnterpriseMultiAccountReq.

        |参数名称：企业子账号的客户ID。| |参数约束及描述：企业子账号的客户ID。|

        :return: The customer_id of this TransferEnterpriseMultiAccountReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this TransferEnterpriseMultiAccountReq.

        |参数名称：企业子账号的客户ID。| |参数约束及描述：企业子账号的客户ID。|

        :param customer_id: The customer_id of this TransferEnterpriseMultiAccountReq.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def amount(self):
        """Gets the amount of this TransferEnterpriseMultiAccountReq.

        |参数名称：现金账户总划拨金额。金额单位为货币标准单位，如人民币则单位为元。| |参数约束及描述：现金账户总划拨金额。金额单位为货币标准单位，如人民币则单位为元。|

        :return: The amount of this TransferEnterpriseMultiAccountReq.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransferEnterpriseMultiAccountReq.

        |参数名称：现金账户总划拨金额。金额单位为货币标准单位，如人民币则单位为元。| |参数约束及描述：现金账户总划拨金额。金额单位为货币标准单位，如人民币则单位为元。|

        :param amount: The amount of this TransferEnterpriseMultiAccountReq.
        :type: str
        """
        self._amount = amount

    @property
    def trans_id(self):
        """Gets the trans_id of this TransferEnterpriseMultiAccountReq.

        |参数名称：交易序列号，用于防止重复提交。如果接口调用方不传此参数的值，则系统自动生成。如果接口调用方传入此参数的值，请采用UUID保证全局唯一。| |参数约束及描述：交易序列号，用于防止重复提交。如果接口调用方不传此参数的值，则系统自动生成。如果接口调用方传入此参数的值，请采用UUID保证全局唯一。|

        :return: The trans_id of this TransferEnterpriseMultiAccountReq.
        :rtype: str
        """
        return self._trans_id

    @trans_id.setter
    def trans_id(self, trans_id):
        """Sets the trans_id of this TransferEnterpriseMultiAccountReq.

        |参数名称：交易序列号，用于防止重复提交。如果接口调用方不传此参数的值，则系统自动生成。如果接口调用方传入此参数的值，请采用UUID保证全局唯一。| |参数约束及描述：交易序列号，用于防止重复提交。如果接口调用方不传此参数的值，则系统自动生成。如果接口调用方传入此参数的值，请采用UUID保证全局唯一。|

        :param trans_id: The trans_id of this TransferEnterpriseMultiAccountReq.
        :type: str
        """
        self._trans_id = trans_id

    @property
    def balance_type(self):
        """Gets the balance_type of this TransferEnterpriseMultiAccountReq.

        |参数名称：账户类型：BALANCE_TYPE_DEBIT：余额账户（默认）；BALANCE_TYPE_CREDIT：信用账户。| |参数约束及描述：账户类型：BALANCE_TYPE_DEBIT：余额账户（默认）；BALANCE_TYPE_CREDIT：信用账户。|

        :return: The balance_type of this TransferEnterpriseMultiAccountReq.
        :rtype: str
        """
        return self._balance_type

    @balance_type.setter
    def balance_type(self, balance_type):
        """Sets the balance_type of this TransferEnterpriseMultiAccountReq.

        |参数名称：账户类型：BALANCE_TYPE_DEBIT：余额账户（默认）；BALANCE_TYPE_CREDIT：信用账户。| |参数约束及描述：账户类型：BALANCE_TYPE_DEBIT：余额账户（默认）；BALANCE_TYPE_CREDIT：信用账户。|

        :param balance_type: The balance_type of this TransferEnterpriseMultiAccountReq.
        :type: str
        """
        self._balance_type = balance_type

    @property
    def expire_time(self):
        """Gets the expire_time of this TransferEnterpriseMultiAccountReq.

        |参数名称：账户到期时间，UTC时间，格式为：2016-03-28T14:45:38Z。暂只对信用账户有效，用于限制针对有效期到期时间等于该时间的信用账户余额进行拨款，精确到秒。如果查询信用账户可拨款余额的查询结果没有失效时间，表示永久有效，对于这种账本拨款的时候不用填写。| |参数约束及描述：账户到期时间，UTC时间，格式为：2016-03-28T14:45:38Z。暂只对信用账户有效，用于限制针对有效期到期时间等于该时间的信用账户余额进行拨款，精确到秒。如果查询信用账户可拨款余额的查询结果没有失效时间，表示永久有效，对于这种账本拨款的时候不用填写。|

        :return: The expire_time of this TransferEnterpriseMultiAccountReq.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this TransferEnterpriseMultiAccountReq.

        |参数名称：账户到期时间，UTC时间，格式为：2016-03-28T14:45:38Z。暂只对信用账户有效，用于限制针对有效期到期时间等于该时间的信用账户余额进行拨款，精确到秒。如果查询信用账户可拨款余额的查询结果没有失效时间，表示永久有效，对于这种账本拨款的时候不用填写。| |参数约束及描述：账户到期时间，UTC时间，格式为：2016-03-28T14:45:38Z。暂只对信用账户有效，用于限制针对有效期到期时间等于该时间的信用账户余额进行拨款，精确到秒。如果查询信用账户可拨款余额的查询结果没有失效时间，表示永久有效，对于这种账本拨款的时候不用填写。|

        :param expire_time: The expire_time of this TransferEnterpriseMultiAccountReq.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TransferEnterpriseMultiAccountReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
