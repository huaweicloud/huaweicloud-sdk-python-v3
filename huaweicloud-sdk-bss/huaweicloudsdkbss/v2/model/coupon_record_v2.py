# coding: utf-8

import pprint
import re

import six





class CouponRecordV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'operation_type': 'str',
        'quota_id': 'str',
        'quota_type': 'int',
        'coupon_id': 'str',
        'customer_id': 'str',
        'operation_amount': 'float',
        'operation_time': 'str',
        'result': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'id': 'id',
        'operation_type': 'operation_type',
        'quota_id': 'quota_id',
        'quota_type': 'quota_type',
        'coupon_id': 'coupon_id',
        'customer_id': 'customer_id',
        'operation_amount': 'operation_amount',
        'operation_time': 'operation_time',
        'result': 'result',
        'remark': 'remark'
    }

    def __init__(self, id=None, operation_type=None, quota_id=None, quota_type=None, coupon_id=None, customer_id=None, operation_amount=None, operation_time=None, result=None, remark=None):
        """CouponRecordV2 - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._operation_type = None
        self._quota_id = None
        self._quota_type = None
        self._coupon_id = None
        self._customer_id = None
        self._operation_amount = None
        self._operation_time = None
        self._result = None
        self._remark = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if operation_type is not None:
            self.operation_type = operation_type
        if quota_id is not None:
            self.quota_id = quota_id
        if quota_type is not None:
            self.quota_type = quota_type
        if coupon_id is not None:
            self.coupon_id = coupon_id
        if customer_id is not None:
            self.customer_id = customer_id
        if operation_amount is not None:
            self.operation_amount = operation_amount
        if operation_time is not None:
            self.operation_time = operation_time
        if result is not None:
            self.result = result
        if remark is not None:
            self.remark = remark

    @property
    def id(self):
        """Gets the id of this CouponRecordV2.

        |参数名称：唯一ID。| |参数约束及描述：唯一ID。|

        :return: The id of this CouponRecordV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CouponRecordV2.

        |参数名称：唯一ID。| |参数约束及描述：唯一ID。|

        :param id: The id of this CouponRecordV2.
        :type: str
        """
        self._id = id

    @property
    def operation_type(self):
        """Gets the operation_type of this CouponRecordV2.

        |参数名称：操作类型：1：发放；2：手动回收；3：解绑自动回收| |参数约束及描述：操作类型：1：发放；2：手动回收；3：解绑自动回收|

        :return: The operation_type of this CouponRecordV2.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this CouponRecordV2.

        |参数名称：操作类型：1：发放；2：手动回收；3：解绑自动回收| |参数约束及描述：操作类型：1：发放；2：手动回收；3：解绑自动回收|

        :param operation_type: The operation_type of this CouponRecordV2.
        :type: str
        """
        self._operation_type = operation_type

    @property
    def quota_id(self):
        """Gets the quota_id of this CouponRecordV2.

        |参数名称：额度ID。| |参数约束及描述：额度ID。|

        :return: The quota_id of this CouponRecordV2.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this CouponRecordV2.

        |参数名称：额度ID。| |参数约束及描述：额度ID。|

        :param quota_id: The quota_id of this CouponRecordV2.
        :type: str
        """
        self._quota_id = quota_id

    @property
    def quota_type(self):
        """Gets the quota_type of this CouponRecordV2.

        |参数名称：操作类型：1：发放；2：手动回收；3：解绑自动回收。| |参数的约束及描述：操作类型：1：发放；2：手动回收；3：解绑自动回收。|

        :return: The quota_type of this CouponRecordV2.
        :rtype: int
        """
        return self._quota_type

    @quota_type.setter
    def quota_type(self, quota_type):
        """Sets the quota_type of this CouponRecordV2.

        |参数名称：操作类型：1：发放；2：手动回收；3：解绑自动回收。| |参数的约束及描述：操作类型：1：发放；2：手动回收；3：解绑自动回收。|

        :param quota_type: The quota_type of this CouponRecordV2.
        :type: int
        """
        self._quota_type = quota_type

    @property
    def coupon_id(self):
        """Gets the coupon_id of this CouponRecordV2.

        |参数名称：代金券ID。| |参数约束及描述：代金券ID。|

        :return: The coupon_id of this CouponRecordV2.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this CouponRecordV2.

        |参数名称：代金券ID。| |参数约束及描述：代金券ID。|

        :param coupon_id: The coupon_id of this CouponRecordV2.
        :type: str
        """
        self._coupon_id = coupon_id

    @property
    def customer_id(self):
        """Gets the customer_id of this CouponRecordV2.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :return: The customer_id of this CouponRecordV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CouponRecordV2.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :param customer_id: The customer_id of this CouponRecordV2.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def operation_amount(self):
        """Gets the operation_amount of this CouponRecordV2.

        |参数名称：操作的面额值。发放时，等于面额值；回收时，指每次回收的具体值。| |参数的约束及描述：操作的面额值。发放时，等于面额值；回收时，指每次回收的具体值。|

        :return: The operation_amount of this CouponRecordV2.
        :rtype: float
        """
        return self._operation_amount

    @operation_amount.setter
    def operation_amount(self, operation_amount):
        """Sets the operation_amount of this CouponRecordV2.

        |参数名称：操作的面额值。发放时，等于面额值；回收时，指每次回收的具体值。| |参数的约束及描述：操作的面额值。发放时，等于面额值；回收时，指每次回收的具体值。|

        :param operation_amount: The operation_amount of this CouponRecordV2.
        :type: float
        """
        self._operation_amount = operation_amount

    @property
    def operation_time(self):
        """Gets the operation_time of this CouponRecordV2.

        |参数名称：操作时间。| |参数约束及描述：操作时间。|

        :return: The operation_time of this CouponRecordV2.
        :rtype: str
        """
        return self._operation_time

    @operation_time.setter
    def operation_time(self, operation_time):
        """Sets the operation_time of this CouponRecordV2.

        |参数名称：操作时间。| |参数约束及描述：操作时间。|

        :param operation_time: The operation_time of this CouponRecordV2.
        :type: str
        """
        self._operation_time = operation_time

    @property
    def result(self):
        """Gets the result of this CouponRecordV2.

        |参数名称：操作结果：0：成功；其他：失败（直接记录错误码）。|参数约束及描述：操作结果：0：成功；其他：失败（直接记录错误码）。|

        :return: The result of this CouponRecordV2.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CouponRecordV2.

        |参数名称：操作结果：0：成功；其他：失败（直接记录错误码）。|参数约束及描述：操作结果：0：成功；其他：失败（直接记录错误码）。|

        :param result: The result of this CouponRecordV2.
        :type: str
        """
        self._result = result

    @property
    def remark(self):
        """Gets the remark of this CouponRecordV2.

        |参数名称：操作记录中的备注| |参数约束及描述：操作记录中的备注|

        :return: The remark of this CouponRecordV2.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this CouponRecordV2.

        |参数名称：操作记录中的备注| |参数约束及描述：操作记录中的备注|

        :param remark: The remark of this CouponRecordV2.
        :type: str
        """
        self._remark = remark

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
        if not isinstance(other, CouponRecordV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
