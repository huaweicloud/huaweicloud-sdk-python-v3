# coding: utf-8

import pprint
import re

import six





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


        :return: The coupon_id of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this ListSubCustomerCouponsRequest.


        :param coupon_id: The coupon_id of this ListSubCustomerCouponsRequest.
        :type: str
        """
        self._coupon_id = coupon_id

    @property
    def order_id(self):
        """Gets the order_id of this ListSubCustomerCouponsRequest.


        :return: The order_id of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ListSubCustomerCouponsRequest.


        :param order_id: The order_id of this ListSubCustomerCouponsRequest.
        :type: str
        """
        self._order_id = order_id

    @property
    def promotion_plan_id(self):
        """Gets the promotion_plan_id of this ListSubCustomerCouponsRequest.


        :return: The promotion_plan_id of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, promotion_plan_id):
        """Sets the promotion_plan_id of this ListSubCustomerCouponsRequest.


        :param promotion_plan_id: The promotion_plan_id of this ListSubCustomerCouponsRequest.
        :type: str
        """
        self._promotion_plan_id = promotion_plan_id

    @property
    def coupon_type(self):
        """Gets the coupon_type of this ListSubCustomerCouponsRequest.


        :return: The coupon_type of this ListSubCustomerCouponsRequest.
        :rtype: int
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """Sets the coupon_type of this ListSubCustomerCouponsRequest.


        :param coupon_type: The coupon_type of this ListSubCustomerCouponsRequest.
        :type: int
        """
        self._coupon_type = coupon_type

    @property
    def status(self):
        """Gets the status of this ListSubCustomerCouponsRequest.


        :return: The status of this ListSubCustomerCouponsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListSubCustomerCouponsRequest.


        :param status: The status of this ListSubCustomerCouponsRequest.
        :type: int
        """
        self._status = status

    @property
    def active_start_time(self):
        """Gets the active_start_time of this ListSubCustomerCouponsRequest.


        :return: The active_start_time of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._active_start_time

    @active_start_time.setter
    def active_start_time(self, active_start_time):
        """Sets the active_start_time of this ListSubCustomerCouponsRequest.


        :param active_start_time: The active_start_time of this ListSubCustomerCouponsRequest.
        :type: str
        """
        self._active_start_time = active_start_time

    @property
    def active_end_time(self):
        """Gets the active_end_time of this ListSubCustomerCouponsRequest.


        :return: The active_end_time of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._active_end_time

    @active_end_time.setter
    def active_end_time(self, active_end_time):
        """Sets the active_end_time of this ListSubCustomerCouponsRequest.


        :param active_end_time: The active_end_time of this ListSubCustomerCouponsRequest.
        :type: str
        """
        self._active_end_time = active_end_time

    @property
    def offset(self):
        """Gets the offset of this ListSubCustomerCouponsRequest.


        :return: The offset of this ListSubCustomerCouponsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSubCustomerCouponsRequest.


        :param offset: The offset of this ListSubCustomerCouponsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSubCustomerCouponsRequest.


        :return: The limit of this ListSubCustomerCouponsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubCustomerCouponsRequest.


        :param limit: The limit of this ListSubCustomerCouponsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def source_id(self):
        """Gets the source_id of this ListSubCustomerCouponsRequest.


        :return: The source_id of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ListSubCustomerCouponsRequest.


        :param source_id: The source_id of this ListSubCustomerCouponsRequest.
        :type: str
        """
        self._source_id = source_id

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListSubCustomerCouponsRequest.


        :return: The indirect_partner_id of this ListSubCustomerCouponsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListSubCustomerCouponsRequest.


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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSubCustomerCouponsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
