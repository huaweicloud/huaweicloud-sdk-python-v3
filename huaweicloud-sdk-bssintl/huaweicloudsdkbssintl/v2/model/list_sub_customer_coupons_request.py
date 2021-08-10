# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubCustomerCouponsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'coupon_id': 'str',
        'order_id': 'str',
        'promotion_plan_id': 'str',
        'coupon_type': 'int',
        'status': 'int',
        'active_start_time': 'str',
        'active_end_time': 'str',
        'offset': 'int',
        'limit': 'int',
        'source_id': 'str',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'coupon_id': 'coupon_id',
        'order_id': 'order_id',
        'promotion_plan_id': 'promotion_plan_id',
        'coupon_type': 'coupon_type',
        'status': 'status',
        'active_start_time': 'active_start_time',
        'active_end_time': 'active_end_time',
        'offset': 'offset',
        'limit': 'limit',
        'source_id': 'source_id',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, coupon_id=None, order_id=None, promotion_plan_id=None, coupon_type=None, status=None, active_start_time=None, active_end_time=None, offset=None, limit=None, source_id=None, indirect_partner_id=None):
        """ListSubCustomerCouponsRequest - a model defined in huaweicloud sdk"""
        
        

        self._coupon_id = None
        self._order_id = None
        self._promotion_plan_id = None
        self._coupon_type = None
        self._status = None
        self._active_start_time = None
        self._active_end_time = None
        self._offset = None
        self._limit = None
        self._source_id = None
        self._indirect_partner_id = None
        self.discriminator = None

        if coupon_id is not None:
            self.coupon_id = coupon_id
        if order_id is not None:
            self.order_id = order_id
        if promotion_plan_id is not None:
            self.promotion_plan_id = promotion_plan_id
        if coupon_type is not None:
            self.coupon_type = coupon_type
        if status is not None:
            self.status = status
        if active_start_time is not None:
            self.active_start_time = active_start_time
        if active_end_time is not None:
            self.active_end_time = active_end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if source_id is not None:
            self.source_id = source_id
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def coupon_id(self):
        """Gets the coupon_id of this ListSubCustomerCouponsRequest.

        |参数名称：优惠券ID。| |参数的约束及描述：优惠券ID。|

        :return: The coupon_id of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this ListSubCustomerCouponsRequest.

        |参数名称：优惠券ID。| |参数的约束及描述：优惠券ID。|

        :param coupon_id: The coupon_id of this ListSubCustomerCouponsRequest.
        :type: str
        """
        self._coupon_id = coupon_id

    @property
    def order_id(self):
        """Gets the order_id of this ListSubCustomerCouponsRequest.

        |参数名称：订单ID。| |参数的约束及描述：订单ID。|

        :return: The order_id of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ListSubCustomerCouponsRequest.

        |参数名称：订单ID。| |参数的约束及描述：订单ID。|

        :param order_id: The order_id of this ListSubCustomerCouponsRequest.
        :type: str
        """
        self._order_id = order_id

    @property
    def promotion_plan_id(self):
        """Gets the promotion_plan_id of this ListSubCustomerCouponsRequest.

        |参数名称：促销计划ID。| |参数的约束及描述：促销计划ID。|

        :return: The promotion_plan_id of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, promotion_plan_id):
        """Sets the promotion_plan_id of this ListSubCustomerCouponsRequest.

        |参数名称：促销计划ID。| |参数的约束及描述：促销计划ID。|

        :param promotion_plan_id: The promotion_plan_id of this ListSubCustomerCouponsRequest.
        :type: str
        """
        self._promotion_plan_id = promotion_plan_id

    @property
    def coupon_type(self):
        """Gets the coupon_type of this ListSubCustomerCouponsRequest.

        |参数名称：优惠券类型：1：代金券；2：折扣券；3：产品券；4：现金券。| |参数的约束及描述：优惠券类型：1：代金券；2：折扣券；3：产品券；4：现金券。|

        :return: The coupon_type of this ListSubCustomerCouponsRequest.
        :rtype: int
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """Sets the coupon_type of this ListSubCustomerCouponsRequest.

        |参数名称：优惠券类型：1：代金券；2：折扣券；3：产品券；4：现金券。| |参数的约束及描述：优惠券类型：1：代金券；2：折扣券；3：产品券；4：现金券。|

        :param coupon_type: The coupon_type of this ListSubCustomerCouponsRequest.
        :type: int
        """
        self._coupon_type = coupon_type

    @property
    def status(self):
        """Gets the status of this ListSubCustomerCouponsRequest.

        |参数名称：客户优惠券实例状态：1：未激活；2：待使用；3：已使用；4：已过期。| |参数的约束及描述：客户优惠券实例状态：1：未激活；2：待使用；3：已使用；4：已过期。|

        :return: The status of this ListSubCustomerCouponsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListSubCustomerCouponsRequest.

        |参数名称：客户优惠券实例状态：1：未激活；2：待使用；3：已使用；4：已过期。| |参数的约束及描述：客户优惠券实例状态：1：未激活；2：待使用；3：已使用；4：已过期。|

        :param status: The status of this ListSubCustomerCouponsRequest.
        :type: int
        """
        self._status = status

    @property
    def active_start_time(self):
        """Gets the active_start_time of this ListSubCustomerCouponsRequest.

        |参数名称：激活时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数的约束及描述：激活时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The active_start_time of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._active_start_time

    @active_start_time.setter
    def active_start_time(self, active_start_time):
        """Sets the active_start_time of this ListSubCustomerCouponsRequest.

        |参数名称：激活时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数的约束及描述：激活时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param active_start_time: The active_start_time of this ListSubCustomerCouponsRequest.
        :type: str
        """
        self._active_start_time = active_start_time

    @property
    def active_end_time(self):
        """Gets the active_end_time of this ListSubCustomerCouponsRequest.

        |参数名称：结束时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数的约束及描述：结束时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The active_end_time of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._active_end_time

    @active_end_time.setter
    def active_end_time(self, active_end_time):
        """Sets the active_end_time of this ListSubCustomerCouponsRequest.

        |参数名称：结束时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数的约束及描述：结束时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param active_end_time: The active_end_time of this ListSubCustomerCouponsRequest.
        :type: str
        """
        self._active_end_time = active_end_time

    @property
    def offset(self):
        """Gets the offset of this ListSubCustomerCouponsRequest.

        |参数名称：偏移量，默认为0| |参数的约束及描述：偏移量，默认为0|

        :return: The offset of this ListSubCustomerCouponsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSubCustomerCouponsRequest.

        |参数名称：偏移量，默认为0| |参数的约束及描述：偏移量，默认为0|

        :param offset: The offset of this ListSubCustomerCouponsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSubCustomerCouponsRequest.

        |参数名称：每页数量，默认10。| |参数的约束及描述：每页数量，默认10。|

        :return: The limit of this ListSubCustomerCouponsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubCustomerCouponsRequest.

        |参数名称：每页数量，默认10。| |参数的约束及描述：每页数量，默认10。|

        :param limit: The limit of this ListSubCustomerCouponsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def source_id(self):
        """Gets the source_id of this ListSubCustomerCouponsRequest.

        |参数名称：发券来源| |参数的约束及描述：如果是合作伙伴发送的券，这个地方是伙伴ID。 如果想查询某个伙伴发放的券，可以在这里输入伙伴ID|

        :return: The source_id of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ListSubCustomerCouponsRequest.

        |参数名称：发券来源| |参数的约束及描述：如果是合作伙伴发送的券，这个地方是伙伴ID。 如果想查询某个伙伴发放的券，可以在这里输入伙伴ID|

        :param source_id: The source_id of this ListSubCustomerCouponsRequest.
        :type: str
        """
        self._source_id = source_id

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListSubCustomerCouponsRequest.

        |参数名称：经营服务商（二级经销商）ID，如果要查询二级经销商名下的券，要传递该字段，否则查询的就是一级经销商自己的券列表。| |参数的约束及描述：经营服务商（二级经销商）ID，如果要查询二级经销商名下的券，要传递该字段，否则查询的就是一级经销商自己的券列表。|

        :return: The indirect_partner_id of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListSubCustomerCouponsRequest.

        |参数名称：经营服务商（二级经销商）ID，如果要查询二级经销商名下的券，要传递该字段，否则查询的就是一级经销商自己的券列表。| |参数的约束及描述：经营服务商（二级经销商）ID，如果要查询二级经销商名下的券，要传递该字段，否则查询的就是一级经销商自己的券列表。|

        :param indirect_partner_id: The indirect_partner_id of this ListSubCustomerCouponsRequest.
        :type: str
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
        if not isinstance(other, ListSubCustomerCouponsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
