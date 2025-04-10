# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCustomerOrdersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'customer_id': 'str',
        'create_time_begin': 'str',
        'create_time_end': 'str',
        'service_type_code': 'str',
        'status': 'int',
        'order_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'order_by': 'str',
        'payment_time_begin': 'str',
        'payment_time_end': 'str',
        'indirect_partner_id': 'str',
        'method': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'customer_id': 'customer_id',
        'create_time_begin': 'create_time_begin',
        'create_time_end': 'create_time_end',
        'service_type_code': 'service_type_code',
        'status': 'status',
        'order_type': 'order_type',
        'limit': 'limit',
        'offset': 'offset',
        'order_by': 'order_by',
        'payment_time_begin': 'payment_time_begin',
        'payment_time_end': 'payment_time_end',
        'indirect_partner_id': 'indirect_partner_id',
        'method': 'method'
    }

    def __init__(self, order_id=None, customer_id=None, create_time_begin=None, create_time_end=None, service_type_code=None, status=None, order_type=None, limit=None, offset=None, order_by=None, payment_time_begin=None, payment_time_end=None, indirect_partner_id=None, method=None):
        r"""ListCustomerOrdersRequest

        The model defined in huaweicloud sdk

        :param order_id: 订单ID。 说明： 使用特殊字符进行查询的时候，请注意进行URL编码转换，如“%”的转码应为“%25”。
        :type order_id: str
        :param customer_id: 客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/intl/zh-cn/api-bpconsole/mc_00021.html)接口获取customer_id。
        :type customer_id: str
        :param create_time_begin: 订单创建开始时间。UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。
        :type create_time_begin: str
        :param create_time_end: 订单创建结束时间。UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。
        :type create_time_end: str
        :param service_type_code: 云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。
        :type service_type_code: str
        :param status: 订单状态：1：待审核3：处理中4：已取消5：已完成6：待支付9：待确认
        :type status: int
        :param order_type: 订单类型：1：开通2：续订3：变更4：退订11：按需转包年/包月13：试用14：转商用15：费用调整
        :type order_type: str
        :param limit: 每次查询的订单数量，默认值为10。
        :type limit: int
        :param offset: 偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param order_by: 查询的订单列表排序。支持按照创建时间进行排序，带-表示倒序。创建时间：升序为createTime，倒序为-createTime。
        :type order_by: str
        :param payment_time_begin: 订单支付开始时间。UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。
        :type payment_time_begin: str
        :param payment_time_end: 订单支付结束时间。UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。
        :type payment_time_end: str
        :param indirect_partner_id: 云经销商ID。华为云总经销商（一级经销商）查询云经销商的客户订单列表时，需要携带该参数；除此之外，此参数不做处理。否则只能查询自己客户的订单列表。
        :type indirect_partner_id: str
        :param method: |参数名称：查询方式，oneself：客户自己订单sub_customer：客户给企业子代付订单。| |参数的约束及描述：默认为oneself。仅customer_id有值时生效。此参数不携带或携带值为空串或携带值为null时，默认值为“oneself”。|
        :type method: str
        """
        
        

        self._order_id = None
        self._customer_id = None
        self._create_time_begin = None
        self._create_time_end = None
        self._service_type_code = None
        self._status = None
        self._order_type = None
        self._limit = None
        self._offset = None
        self._order_by = None
        self._payment_time_begin = None
        self._payment_time_end = None
        self._indirect_partner_id = None
        self._method = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if customer_id is not None:
            self.customer_id = customer_id
        if create_time_begin is not None:
            self.create_time_begin = create_time_begin
        if create_time_end is not None:
            self.create_time_end = create_time_end
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if status is not None:
            self.status = status
        if order_type is not None:
            self.order_type = order_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order_by is not None:
            self.order_by = order_by
        if payment_time_begin is not None:
            self.payment_time_begin = payment_time_begin
        if payment_time_end is not None:
            self.payment_time_end = payment_time_end
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if method is not None:
            self.method = method

    @property
    def order_id(self):
        r"""Gets the order_id of this ListCustomerOrdersRequest.

        订单ID。 说明： 使用特殊字符进行查询的时候，请注意进行URL编码转换，如“%”的转码应为“%25”。

        :return: The order_id of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ListCustomerOrdersRequest.

        订单ID。 说明： 使用特殊字符进行查询的时候，请注意进行URL编码转换，如“%”的转码应为“%25”。

        :param order_id: The order_id of this ListCustomerOrdersRequest.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def customer_id(self):
        r"""Gets the customer_id of this ListCustomerOrdersRequest.

        客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/intl/zh-cn/api-bpconsole/mc_00021.html)接口获取customer_id。

        :return: The customer_id of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this ListCustomerOrdersRequest.

        客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/intl/zh-cn/api-bpconsole/mc_00021.html)接口获取customer_id。

        :param customer_id: The customer_id of this ListCustomerOrdersRequest.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def create_time_begin(self):
        r"""Gets the create_time_begin of this ListCustomerOrdersRequest.

        订单创建开始时间。UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The create_time_begin of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._create_time_begin

    @create_time_begin.setter
    def create_time_begin(self, create_time_begin):
        r"""Sets the create_time_begin of this ListCustomerOrdersRequest.

        订单创建开始时间。UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :param create_time_begin: The create_time_begin of this ListCustomerOrdersRequest.
        :type create_time_begin: str
        """
        self._create_time_begin = create_time_begin

    @property
    def create_time_end(self):
        r"""Gets the create_time_end of this ListCustomerOrdersRequest.

        订单创建结束时间。UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The create_time_end of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._create_time_end

    @create_time_end.setter
    def create_time_end(self, create_time_end):
        r"""Sets the create_time_end of this ListCustomerOrdersRequest.

        订单创建结束时间。UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :param create_time_end: The create_time_end of this ListCustomerOrdersRequest.
        :type create_time_end: str
        """
        self._create_time_end = create_time_end

    @property
    def service_type_code(self):
        r"""Gets the service_type_code of this ListCustomerOrdersRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :return: The service_type_code of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        r"""Sets the service_type_code of this ListCustomerOrdersRequest.

        云服务类型编码，例如OBS的云服务类型编码为“hws.service.type.obs”。您可以调用查询云服务类型列表接口获取。

        :param service_type_code: The service_type_code of this ListCustomerOrdersRequest.
        :type service_type_code: str
        """
        self._service_type_code = service_type_code

    @property
    def status(self):
        r"""Gets the status of this ListCustomerOrdersRequest.

        订单状态：1：待审核3：处理中4：已取消5：已完成6：待支付9：待确认

        :return: The status of this ListCustomerOrdersRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListCustomerOrdersRequest.

        订单状态：1：待审核3：处理中4：已取消5：已完成6：待支付9：待确认

        :param status: The status of this ListCustomerOrdersRequest.
        :type status: int
        """
        self._status = status

    @property
    def order_type(self):
        r"""Gets the order_type of this ListCustomerOrdersRequest.

        订单类型：1：开通2：续订3：变更4：退订11：按需转包年/包月13：试用14：转商用15：费用调整

        :return: The order_type of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        r"""Sets the order_type of this ListCustomerOrdersRequest.

        订单类型：1：开通2：续订3：变更4：退订11：按需转包年/包月13：试用14：转商用15：费用调整

        :param order_type: The order_type of this ListCustomerOrdersRequest.
        :type order_type: str
        """
        self._order_type = order_type

    @property
    def limit(self):
        r"""Gets the limit of this ListCustomerOrdersRequest.

        每次查询的订单数量，默认值为10。

        :return: The limit of this ListCustomerOrdersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCustomerOrdersRequest.

        每次查询的订单数量，默认值为10。

        :param limit: The limit of this ListCustomerOrdersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCustomerOrdersRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListCustomerOrdersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCustomerOrdersRequest.

        偏移量，从0开始。默认值为0。 说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListCustomerOrdersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def order_by(self):
        r"""Gets the order_by of this ListCustomerOrdersRequest.

        查询的订单列表排序。支持按照创建时间进行排序，带-表示倒序。创建时间：升序为createTime，倒序为-createTime。

        :return: The order_by of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListCustomerOrdersRequest.

        查询的订单列表排序。支持按照创建时间进行排序，带-表示倒序。创建时间：升序为createTime，倒序为-createTime。

        :param order_by: The order_by of this ListCustomerOrdersRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def payment_time_begin(self):
        r"""Gets the payment_time_begin of this ListCustomerOrdersRequest.

        订单支付开始时间。UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The payment_time_begin of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._payment_time_begin

    @payment_time_begin.setter
    def payment_time_begin(self, payment_time_begin):
        r"""Sets the payment_time_begin of this ListCustomerOrdersRequest.

        订单支付开始时间。UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :param payment_time_begin: The payment_time_begin of this ListCustomerOrdersRequest.
        :type payment_time_begin: str
        """
        self._payment_time_begin = payment_time_begin

    @property
    def payment_time_end(self):
        r"""Gets the payment_time_end of this ListCustomerOrdersRequest.

        订单支付结束时间。UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The payment_time_end of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._payment_time_end

    @payment_time_end.setter
    def payment_time_end(self, payment_time_end):
        r"""Sets the payment_time_end of this ListCustomerOrdersRequest.

        订单支付结束时间。UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :param payment_time_end: The payment_time_end of this ListCustomerOrdersRequest.
        :type payment_time_end: str
        """
        self._payment_time_end = payment_time_end

    @property
    def indirect_partner_id(self):
        r"""Gets the indirect_partner_id of this ListCustomerOrdersRequest.

        云经销商ID。华为云总经销商（一级经销商）查询云经销商的客户订单列表时，需要携带该参数；除此之外，此参数不做处理。否则只能查询自己客户的订单列表。

        :return: The indirect_partner_id of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        r"""Sets the indirect_partner_id of this ListCustomerOrdersRequest.

        云经销商ID。华为云总经销商（一级经销商）查询云经销商的客户订单列表时，需要携带该参数；除此之外，此参数不做处理。否则只能查询自己客户的订单列表。

        :param indirect_partner_id: The indirect_partner_id of this ListCustomerOrdersRequest.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def method(self):
        r"""Gets the method of this ListCustomerOrdersRequest.

        |参数名称：查询方式，oneself：客户自己订单sub_customer：客户给企业子代付订单。| |参数的约束及描述：默认为oneself。仅customer_id有值时生效。此参数不携带或携带值为空串或携带值为null时，默认值为“oneself”。|

        :return: The method of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this ListCustomerOrdersRequest.

        |参数名称：查询方式，oneself：客户自己订单sub_customer：客户给企业子代付订单。| |参数的约束及描述：默认为oneself。仅customer_id有值时生效。此参数不携带或携带值为空串或携带值为null时，默认值为“oneself”。|

        :param method: The method of this ListCustomerOrdersRequest.
        :type method: str
        """
        self._method = method

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
        if not isinstance(other, ListCustomerOrdersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
