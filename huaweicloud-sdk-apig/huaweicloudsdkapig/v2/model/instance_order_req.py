# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceOrderReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'charging_mode': 'int',
        'payment_mode': 'str',
        'period_type': 'int',
        'period_num': 'int',
        'is_auto_renew': 'int',
        'promotion_id': 'str',
        'promotion_plan_id': 'str',
        'promotion_info': 'str',
        'composite_product_id': 'str',
        'instance_info': 'InstanceCreateReqV2'
    }

    attribute_map = {
        'product_id': 'product_id',
        'charging_mode': 'charging_mode',
        'payment_mode': 'payment_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'promotion_id': 'promotion_id',
        'promotion_plan_id': 'promotion_plan_id',
        'promotion_info': 'promotion_info',
        'composite_product_id': 'composite_product_id',
        'instance_info': 'instance_info'
    }

    def __init__(self, product_id=None, charging_mode=None, payment_mode=None, period_type=None, period_num=None, is_auto_renew=None, promotion_id=None, promotion_plan_id=None, promotion_info=None, composite_product_id=None, instance_info=None):
        r"""InstanceOrderReq

        The model defined in huaweicloud sdk

        :param product_id: 产品编号
        :type product_id: str
        :param charging_mode: 计费模式： - 0：按需 - 1：包周期 
        :type charging_mode: int
        :param payment_mode: 支付模式： - ALL_UPFRONT：全预付 
        :type payment_mode: str
        :param period_type: 订购周期类型： - 2：月 - 3：年 
        :type period_type: int
        :param period_num: 订购周期数：1-9 
        :type period_num: int
        :param is_auto_renew: 是否支持自动续费： - 0：不自动续费 - 1：自动续费 
        :type is_auto_renew: int
        :param promotion_id: 促销产品编号
        :type promotion_id: str
        :param promotion_plan_id: 促销计划编号
        :type promotion_plan_id: str
        :param promotion_info: 促销信息
        :type promotion_info: str
        :param composite_product_id: 组合产品编号
        :type composite_product_id: str
        :param instance_info: 
        :type instance_info: :class:`huaweicloudsdkapig.v2.InstanceCreateReqV2`
        """
        
        

        self._product_id = None
        self._charging_mode = None
        self._payment_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._promotion_id = None
        self._promotion_plan_id = None
        self._promotion_info = None
        self._composite_product_id = None
        self._instance_info = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if payment_mode is not None:
            self.payment_mode = payment_mode
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if promotion_id is not None:
            self.promotion_id = promotion_id
        if promotion_plan_id is not None:
            self.promotion_plan_id = promotion_plan_id
        if promotion_info is not None:
            self.promotion_info = promotion_info
        if composite_product_id is not None:
            self.composite_product_id = composite_product_id
        if instance_info is not None:
            self.instance_info = instance_info

    @property
    def product_id(self):
        r"""Gets the product_id of this InstanceOrderReq.

        产品编号

        :return: The product_id of this InstanceOrderReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this InstanceOrderReq.

        产品编号

        :param product_id: The product_id of this InstanceOrderReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this InstanceOrderReq.

        计费模式： - 0：按需 - 1：包周期 

        :return: The charging_mode of this InstanceOrderReq.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this InstanceOrderReq.

        计费模式： - 0：按需 - 1：包周期 

        :param charging_mode: The charging_mode of this InstanceOrderReq.
        :type charging_mode: int
        """
        self._charging_mode = charging_mode

    @property
    def payment_mode(self):
        r"""Gets the payment_mode of this InstanceOrderReq.

        支付模式： - ALL_UPFRONT：全预付 

        :return: The payment_mode of this InstanceOrderReq.
        :rtype: str
        """
        return self._payment_mode

    @payment_mode.setter
    def payment_mode(self, payment_mode):
        r"""Sets the payment_mode of this InstanceOrderReq.

        支付模式： - ALL_UPFRONT：全预付 

        :param payment_mode: The payment_mode of this InstanceOrderReq.
        :type payment_mode: str
        """
        self._payment_mode = payment_mode

    @property
    def period_type(self):
        r"""Gets the period_type of this InstanceOrderReq.

        订购周期类型： - 2：月 - 3：年 

        :return: The period_type of this InstanceOrderReq.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this InstanceOrderReq.

        订购周期类型： - 2：月 - 3：年 

        :param period_type: The period_type of this InstanceOrderReq.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this InstanceOrderReq.

        订购周期数：1-9 

        :return: The period_num of this InstanceOrderReq.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this InstanceOrderReq.

        订购周期数：1-9 

        :param period_num: The period_num of this InstanceOrderReq.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this InstanceOrderReq.

        是否支持自动续费： - 0：不自动续费 - 1：自动续费 

        :return: The is_auto_renew of this InstanceOrderReq.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this InstanceOrderReq.

        是否支持自动续费： - 0：不自动续费 - 1：自动续费 

        :param is_auto_renew: The is_auto_renew of this InstanceOrderReq.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    @property
    def promotion_id(self):
        r"""Gets the promotion_id of this InstanceOrderReq.

        促销产品编号

        :return: The promotion_id of this InstanceOrderReq.
        :rtype: str
        """
        return self._promotion_id

    @promotion_id.setter
    def promotion_id(self, promotion_id):
        r"""Sets the promotion_id of this InstanceOrderReq.

        促销产品编号

        :param promotion_id: The promotion_id of this InstanceOrderReq.
        :type promotion_id: str
        """
        self._promotion_id = promotion_id

    @property
    def promotion_plan_id(self):
        r"""Gets the promotion_plan_id of this InstanceOrderReq.

        促销计划编号

        :return: The promotion_plan_id of this InstanceOrderReq.
        :rtype: str
        """
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, promotion_plan_id):
        r"""Sets the promotion_plan_id of this InstanceOrderReq.

        促销计划编号

        :param promotion_plan_id: The promotion_plan_id of this InstanceOrderReq.
        :type promotion_plan_id: str
        """
        self._promotion_plan_id = promotion_plan_id

    @property
    def promotion_info(self):
        r"""Gets the promotion_info of this InstanceOrderReq.

        促销信息

        :return: The promotion_info of this InstanceOrderReq.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        r"""Sets the promotion_info of this InstanceOrderReq.

        促销信息

        :param promotion_info: The promotion_info of this InstanceOrderReq.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

    @property
    def composite_product_id(self):
        r"""Gets the composite_product_id of this InstanceOrderReq.

        组合产品编号

        :return: The composite_product_id of this InstanceOrderReq.
        :rtype: str
        """
        return self._composite_product_id

    @composite_product_id.setter
    def composite_product_id(self, composite_product_id):
        r"""Sets the composite_product_id of this InstanceOrderReq.

        组合产品编号

        :param composite_product_id: The composite_product_id of this InstanceOrderReq.
        :type composite_product_id: str
        """
        self._composite_product_id = composite_product_id

    @property
    def instance_info(self):
        r"""Gets the instance_info of this InstanceOrderReq.

        :return: The instance_info of this InstanceOrderReq.
        :rtype: :class:`huaweicloudsdkapig.v2.InstanceCreateReqV2`
        """
        return self._instance_info

    @instance_info.setter
    def instance_info(self, instance_info):
        r"""Sets the instance_info of this InstanceOrderReq.

        :param instance_info: The instance_info of this InstanceOrderReq.
        :type instance_info: :class:`huaweicloudsdkapig.v2.InstanceCreateReqV2`
        """
        self._instance_info = instance_info

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
        if not isinstance(other, InstanceOrderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
