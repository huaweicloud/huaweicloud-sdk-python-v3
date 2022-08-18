# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPartnerAdjustRecordsRequest:

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
        'operation_type': 'str',
        'operation_time_begin': 'str',
        'operation_time_end': 'str',
        'trans_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'operation_type': 'operation_type',
        'operation_time_begin': 'operation_time_begin',
        'operation_time_end': 'operation_time_end',
        'trans_id': 'trans_id',
        'offset': 'offset',
        'limit': 'limit',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, customer_id=None, operation_type=None, operation_time_begin=None, operation_time_end=None, trans_id=None, offset=None, limit=None, indirect_partner_id=None):
        """ListPartnerAdjustRecordsRequest

        The model defined in huaweicloud sdk

        :param customer_id: 客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)获取customer_id。为空表示查询所有的调账记录。不为空表示仅查询与该客户相关的调账记录。此参数不携带或携带值为空时，默认查询所有客户的调账记录。 说明： 此处的客户包含伙伴的子客户，以及华为云总经销商关联的云经销商（二级经销商）。
        :type customer_id: str
        :param operation_type: 操作类型。SOURCE_OPERATION_BEADJUST：拨款,SOURCE_OPERATION_BERETRIEVE：回收,SOURCE_OPERATION_BEUNBIND：解绑回收,此参数不携带或携带值为空时，默认查询所有类型。
        :type operation_type: str
        :param operation_time_begin: 调账起始时间。UTC时间，格式为：2016-03-28T14:45:38Z。此参数不携带或携带值为空时，不作为筛选条件。
        :type operation_time_begin: str
        :param operation_time_end: 调账截止时间。UTC时间，格式为：2016-03-28T14:45:38Z。此参数不携带或携带值为空时，不作为筛选条件。
        :type operation_time_end: str
        :param trans_id: 事务ID。此参数不携带或携带值为空时，不作为筛选条件。
        :type trans_id: str
        :param offset: 偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每页的显示条数。默认值为10。
        :type limit: int
        :param indirect_partner_id: 云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。华为云总经销商（一级经销商）查询云经销商（二级经销商）的子客户调账记录时，需携带此参数；除此之外，此参数不做处理。否则只能查询自己的子客户调账记录。
        :type indirect_partner_id: str
        """
        
        

        self._customer_id = None
        self._operation_type = None
        self._operation_time_begin = None
        self._operation_time_end = None
        self._trans_id = None
        self._offset = None
        self._limit = None
        self._indirect_partner_id = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if operation_type is not None:
            self.operation_type = operation_type
        if operation_time_begin is not None:
            self.operation_time_begin = operation_time_begin
        if operation_time_end is not None:
            self.operation_time_end = operation_time_end
        if trans_id is not None:
            self.trans_id = trans_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def customer_id(self):
        """Gets the customer_id of this ListPartnerAdjustRecordsRequest.

        客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)获取customer_id。为空表示查询所有的调账记录。不为空表示仅查询与该客户相关的调账记录。此参数不携带或携带值为空时，默认查询所有客户的调账记录。 说明： 此处的客户包含伙伴的子客户，以及华为云总经销商关联的云经销商（二级经销商）。

        :return: The customer_id of this ListPartnerAdjustRecordsRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ListPartnerAdjustRecordsRequest.

        客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)获取customer_id。为空表示查询所有的调账记录。不为空表示仅查询与该客户相关的调账记录。此参数不携带或携带值为空时，默认查询所有客户的调账记录。 说明： 此处的客户包含伙伴的子客户，以及华为云总经销商关联的云经销商（二级经销商）。

        :param customer_id: The customer_id of this ListPartnerAdjustRecordsRequest.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def operation_type(self):
        """Gets the operation_type of this ListPartnerAdjustRecordsRequest.

        操作类型。SOURCE_OPERATION_BEADJUST：拨款,SOURCE_OPERATION_BERETRIEVE：回收,SOURCE_OPERATION_BEUNBIND：解绑回收,此参数不携带或携带值为空时，默认查询所有类型。

        :return: The operation_type of this ListPartnerAdjustRecordsRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this ListPartnerAdjustRecordsRequest.

        操作类型。SOURCE_OPERATION_BEADJUST：拨款,SOURCE_OPERATION_BERETRIEVE：回收,SOURCE_OPERATION_BEUNBIND：解绑回收,此参数不携带或携带值为空时，默认查询所有类型。

        :param operation_type: The operation_type of this ListPartnerAdjustRecordsRequest.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def operation_time_begin(self):
        """Gets the operation_time_begin of this ListPartnerAdjustRecordsRequest.

        调账起始时间。UTC时间，格式为：2016-03-28T14:45:38Z。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The operation_time_begin of this ListPartnerAdjustRecordsRequest.
        :rtype: str
        """
        return self._operation_time_begin

    @operation_time_begin.setter
    def operation_time_begin(self, operation_time_begin):
        """Sets the operation_time_begin of this ListPartnerAdjustRecordsRequest.

        调账起始时间。UTC时间，格式为：2016-03-28T14:45:38Z。此参数不携带或携带值为空时，不作为筛选条件。

        :param operation_time_begin: The operation_time_begin of this ListPartnerAdjustRecordsRequest.
        :type operation_time_begin: str
        """
        self._operation_time_begin = operation_time_begin

    @property
    def operation_time_end(self):
        """Gets the operation_time_end of this ListPartnerAdjustRecordsRequest.

        调账截止时间。UTC时间，格式为：2016-03-28T14:45:38Z。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The operation_time_end of this ListPartnerAdjustRecordsRequest.
        :rtype: str
        """
        return self._operation_time_end

    @operation_time_end.setter
    def operation_time_end(self, operation_time_end):
        """Sets the operation_time_end of this ListPartnerAdjustRecordsRequest.

        调账截止时间。UTC时间，格式为：2016-03-28T14:45:38Z。此参数不携带或携带值为空时，不作为筛选条件。

        :param operation_time_end: The operation_time_end of this ListPartnerAdjustRecordsRequest.
        :type operation_time_end: str
        """
        self._operation_time_end = operation_time_end

    @property
    def trans_id(self):
        """Gets the trans_id of this ListPartnerAdjustRecordsRequest.

        事务ID。此参数不携带或携带值为空时，不作为筛选条件。

        :return: The trans_id of this ListPartnerAdjustRecordsRequest.
        :rtype: str
        """
        return self._trans_id

    @trans_id.setter
    def trans_id(self, trans_id):
        """Sets the trans_id of this ListPartnerAdjustRecordsRequest.

        事务ID。此参数不携带或携带值为空时，不作为筛选条件。

        :param trans_id: The trans_id of this ListPartnerAdjustRecordsRequest.
        :type trans_id: str
        """
        self._trans_id = trans_id

    @property
    def offset(self):
        """Gets the offset of this ListPartnerAdjustRecordsRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListPartnerAdjustRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPartnerAdjustRecordsRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListPartnerAdjustRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPartnerAdjustRecordsRequest.

        每页的显示条数。默认值为10。

        :return: The limit of this ListPartnerAdjustRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPartnerAdjustRecordsRequest.

        每页的显示条数。默认值为10。

        :param limit: The limit of this ListPartnerAdjustRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListPartnerAdjustRecordsRequest.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。华为云总经销商（一级经销商）查询云经销商（二级经销商）的子客户调账记录时，需携带此参数；除此之外，此参数不做处理。否则只能查询自己的子客户调账记录。

        :return: The indirect_partner_id of this ListPartnerAdjustRecordsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListPartnerAdjustRecordsRequest.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。华为云总经销商（一级经销商）查询云经销商（二级经销商）的子客户调账记录时，需携带此参数；除此之外，此参数不做处理。否则只能查询自己的子客户调账记录。

        :param indirect_partner_id: The indirect_partner_id of this ListPartnerAdjustRecordsRequest.
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
        if not isinstance(other, ListPartnerAdjustRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
