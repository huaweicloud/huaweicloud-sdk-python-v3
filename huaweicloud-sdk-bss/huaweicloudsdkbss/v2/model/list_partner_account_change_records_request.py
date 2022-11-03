# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPartnerAccountChangeRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'balance_type': 'str',
        'trade_type': 'str',
        'trade_time_begin': 'str',
        'trade_time_end': 'str',
        'offset': 'int',
        'limit': 'int',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'balance_type': 'balance_type',
        'trade_type': 'trade_type',
        'trade_time_begin': 'trade_time_begin',
        'trade_time_end': 'trade_time_end',
        'offset': 'offset',
        'limit': 'limit',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, balance_type=None, trade_type=None, trade_time_begin=None, trade_time_end=None, offset=None, limit=None, indirect_partner_id=None):
        """ListPartnerAccountChangeRecordsRequest

        The model defined in huaweicloud sdk

        :param balance_type: 账户类型。BALANCE_TYPE_DEBIT：现金账户,BALANCE_TYPE_CREDIT：信用账户
        :type balance_type: str
        :param trade_type: 交易类型。RECHARGE：充值,DEDEUCT：消费,REFUND：退款,RFROZEN：冻结,TRANS：转账，余额和保证金互换（老商务模式，当前已无保证金账户）,ADJUST：调账（华为核销等）,BEADJUST：经销商拨款,BERETRIEVE：经销商回收,BEUNBIND：解绑/关联模式切换导致的回收,BONUSCONVERT：奖励金转换（老商务模式，当前已无奖励金账户）,TRADE_MODE_TRANSFER：交易模式变更, 此参数不携带或携带值为空时，不作为筛选条件。
        :type trade_type: str
        :param trade_time_begin: 查询收支明细的开始日期。 说明： 东八区时间，格式为YYYY-MM-DD，如“2017-10-21”。默认值为一年前的当天日期。
        :type trade_time_begin: str
        :param trade_time_end: 查询收支明细的结束日期。 说明： 东八区时间，格式为YYYY-MM-DD，如“2017-12-21”。默认值为当前日期。
        :type trade_time_end: str
        :param offset: 偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询的数量，默认值为10。
        :type limit: int
        :param indirect_partner_id: 云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。  说明： 华为云总经销商（一级经销商）查询云经销商（二级经销商）的收支明细时，需携带此参数；除此之外，此参数不作处理。否则只能查询自身的收支明细。
        :type indirect_partner_id: str
        """
        
        

        self._balance_type = None
        self._trade_type = None
        self._trade_time_begin = None
        self._trade_time_end = None
        self._offset = None
        self._limit = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.balance_type = balance_type
        if trade_type is not None:
            self.trade_type = trade_type
        if trade_time_begin is not None:
            self.trade_time_begin = trade_time_begin
        if trade_time_end is not None:
            self.trade_time_end = trade_time_end
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def balance_type(self):
        """Gets the balance_type of this ListPartnerAccountChangeRecordsRequest.

        账户类型。BALANCE_TYPE_DEBIT：现金账户,BALANCE_TYPE_CREDIT：信用账户

        :return: The balance_type of this ListPartnerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._balance_type

    @balance_type.setter
    def balance_type(self, balance_type):
        """Sets the balance_type of this ListPartnerAccountChangeRecordsRequest.

        账户类型。BALANCE_TYPE_DEBIT：现金账户,BALANCE_TYPE_CREDIT：信用账户

        :param balance_type: The balance_type of this ListPartnerAccountChangeRecordsRequest.
        :type balance_type: str
        """
        self._balance_type = balance_type

    @property
    def trade_type(self):
        """Gets the trade_type of this ListPartnerAccountChangeRecordsRequest.

        交易类型。RECHARGE：充值,DEDEUCT：消费,REFUND：退款,RFROZEN：冻结,TRANS：转账，余额和保证金互换（老商务模式，当前已无保证金账户）,ADJUST：调账（华为核销等）,BEADJUST：经销商拨款,BERETRIEVE：经销商回收,BEUNBIND：解绑/关联模式切换导致的回收,BONUSCONVERT：奖励金转换（老商务模式，当前已无奖励金账户）,TRADE_MODE_TRANSFER：交易模式变更, 此参数不携带或携带值为空时，不作为筛选条件。

        :return: The trade_type of this ListPartnerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._trade_type

    @trade_type.setter
    def trade_type(self, trade_type):
        """Sets the trade_type of this ListPartnerAccountChangeRecordsRequest.

        交易类型。RECHARGE：充值,DEDEUCT：消费,REFUND：退款,RFROZEN：冻结,TRANS：转账，余额和保证金互换（老商务模式，当前已无保证金账户）,ADJUST：调账（华为核销等）,BEADJUST：经销商拨款,BERETRIEVE：经销商回收,BEUNBIND：解绑/关联模式切换导致的回收,BONUSCONVERT：奖励金转换（老商务模式，当前已无奖励金账户）,TRADE_MODE_TRANSFER：交易模式变更, 此参数不携带或携带值为空时，不作为筛选条件。

        :param trade_type: The trade_type of this ListPartnerAccountChangeRecordsRequest.
        :type trade_type: str
        """
        self._trade_type = trade_type

    @property
    def trade_time_begin(self):
        """Gets the trade_time_begin of this ListPartnerAccountChangeRecordsRequest.

        查询收支明细的开始日期。 说明： 东八区时间，格式为YYYY-MM-DD，如“2017-10-21”。默认值为一年前的当天日期。

        :return: The trade_time_begin of this ListPartnerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._trade_time_begin

    @trade_time_begin.setter
    def trade_time_begin(self, trade_time_begin):
        """Sets the trade_time_begin of this ListPartnerAccountChangeRecordsRequest.

        查询收支明细的开始日期。 说明： 东八区时间，格式为YYYY-MM-DD，如“2017-10-21”。默认值为一年前的当天日期。

        :param trade_time_begin: The trade_time_begin of this ListPartnerAccountChangeRecordsRequest.
        :type trade_time_begin: str
        """
        self._trade_time_begin = trade_time_begin

    @property
    def trade_time_end(self):
        """Gets the trade_time_end of this ListPartnerAccountChangeRecordsRequest.

        查询收支明细的结束日期。 说明： 东八区时间，格式为YYYY-MM-DD，如“2017-12-21”。默认值为当前日期。

        :return: The trade_time_end of this ListPartnerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._trade_time_end

    @trade_time_end.setter
    def trade_time_end(self, trade_time_end):
        """Sets the trade_time_end of this ListPartnerAccountChangeRecordsRequest.

        查询收支明细的结束日期。 说明： 东八区时间，格式为YYYY-MM-DD，如“2017-12-21”。默认值为当前日期。

        :param trade_time_end: The trade_time_end of this ListPartnerAccountChangeRecordsRequest.
        :type trade_time_end: str
        """
        self._trade_time_end = trade_time_end

    @property
    def offset(self):
        """Gets the offset of this ListPartnerAccountChangeRecordsRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListPartnerAccountChangeRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPartnerAccountChangeRecordsRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListPartnerAccountChangeRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPartnerAccountChangeRecordsRequest.

        每次查询的数量，默认值为10。

        :return: The limit of this ListPartnerAccountChangeRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPartnerAccountChangeRecordsRequest.

        每次查询的数量，默认值为10。

        :param limit: The limit of this ListPartnerAccountChangeRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListPartnerAccountChangeRecordsRequest.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。  说明： 华为云总经销商（一级经销商）查询云经销商（二级经销商）的收支明细时，需携带此参数；除此之外，此参数不作处理。否则只能查询自身的收支明细。

        :return: The indirect_partner_id of this ListPartnerAccountChangeRecordsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListPartnerAccountChangeRecordsRequest.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。  说明： 华为云总经销商（一级经销商）查询云经销商（二级经销商）的收支明细时，需携带此参数；除此之外，此参数不作处理。否则只能查询自身的收支明细。

        :param indirect_partner_id: The indirect_partner_id of this ListPartnerAccountChangeRecordsRequest.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        if not isinstance(other, ListPartnerAccountChangeRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
