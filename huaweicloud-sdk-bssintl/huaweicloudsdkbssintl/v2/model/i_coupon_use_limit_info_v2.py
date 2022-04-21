# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ICouponUseLimitInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'use_limiti_info_id': 'str',
        'limit_key': 'str',
        'value1': 'str',
        'value2': 'str',
        'value_unit': 'str',
        'limit_type': 'str',
        'promotion_plan_id': 'str'
    }

    attribute_map = {
        'use_limiti_info_id': 'use_limiti_info_id',
        'limit_key': 'limit_key',
        'value1': 'value1',
        'value2': 'value2',
        'value_unit': 'value_unit',
        'limit_type': 'limit_type',
        'promotion_plan_id': 'promotion_plan_id'
    }

    def __init__(self, use_limiti_info_id=None, limit_key=None, value1=None, value2=None, value_unit=None, limit_type=None, promotion_plan_id=None):
        """ICouponUseLimitInfoV2

        The model defined in huaweicloud sdk

        :param use_limiti_info_id: 使用限制ID，主键。
        :type use_limiti_info_id: str
        :param limit_key: 折扣限制，key的取值请参考表4。
        :type limit_key: str
        :param value1: value1。
        :type value1: str
        :param value2: value2。
        :type value2: str
        :param value_unit: value单位。
        :type value_unit: str
        :param limit_type: 限制类型。
        :type limit_type: str
        :param promotion_plan_id: 促销计划ID。
        :type promotion_plan_id: str
        """
        
        

        self._use_limiti_info_id = None
        self._limit_key = None
        self._value1 = None
        self._value2 = None
        self._value_unit = None
        self._limit_type = None
        self._promotion_plan_id = None
        self.discriminator = None

        if use_limiti_info_id is not None:
            self.use_limiti_info_id = use_limiti_info_id
        if limit_key is not None:
            self.limit_key = limit_key
        if value1 is not None:
            self.value1 = value1
        if value2 is not None:
            self.value2 = value2
        if value_unit is not None:
            self.value_unit = value_unit
        if limit_type is not None:
            self.limit_type = limit_type
        if promotion_plan_id is not None:
            self.promotion_plan_id = promotion_plan_id

    @property
    def use_limiti_info_id(self):
        """Gets the use_limiti_info_id of this ICouponUseLimitInfoV2.

        使用限制ID，主键。

        :return: The use_limiti_info_id of this ICouponUseLimitInfoV2.
        :rtype: str
        """
        return self._use_limiti_info_id

    @use_limiti_info_id.setter
    def use_limiti_info_id(self, use_limiti_info_id):
        """Sets the use_limiti_info_id of this ICouponUseLimitInfoV2.

        使用限制ID，主键。

        :param use_limiti_info_id: The use_limiti_info_id of this ICouponUseLimitInfoV2.
        :type use_limiti_info_id: str
        """
        self._use_limiti_info_id = use_limiti_info_id

    @property
    def limit_key(self):
        """Gets the limit_key of this ICouponUseLimitInfoV2.

        折扣限制，key的取值请参考表4。

        :return: The limit_key of this ICouponUseLimitInfoV2.
        :rtype: str
        """
        return self._limit_key

    @limit_key.setter
    def limit_key(self, limit_key):
        """Sets the limit_key of this ICouponUseLimitInfoV2.

        折扣限制，key的取值请参考表4。

        :param limit_key: The limit_key of this ICouponUseLimitInfoV2.
        :type limit_key: str
        """
        self._limit_key = limit_key

    @property
    def value1(self):
        """Gets the value1 of this ICouponUseLimitInfoV2.

        value1。

        :return: The value1 of this ICouponUseLimitInfoV2.
        :rtype: str
        """
        return self._value1

    @value1.setter
    def value1(self, value1):
        """Sets the value1 of this ICouponUseLimitInfoV2.

        value1。

        :param value1: The value1 of this ICouponUseLimitInfoV2.
        :type value1: str
        """
        self._value1 = value1

    @property
    def value2(self):
        """Gets the value2 of this ICouponUseLimitInfoV2.

        value2。

        :return: The value2 of this ICouponUseLimitInfoV2.
        :rtype: str
        """
        return self._value2

    @value2.setter
    def value2(self, value2):
        """Sets the value2 of this ICouponUseLimitInfoV2.

        value2。

        :param value2: The value2 of this ICouponUseLimitInfoV2.
        :type value2: str
        """
        self._value2 = value2

    @property
    def value_unit(self):
        """Gets the value_unit of this ICouponUseLimitInfoV2.

        value单位。

        :return: The value_unit of this ICouponUseLimitInfoV2.
        :rtype: str
        """
        return self._value_unit

    @value_unit.setter
    def value_unit(self, value_unit):
        """Sets the value_unit of this ICouponUseLimitInfoV2.

        value单位。

        :param value_unit: The value_unit of this ICouponUseLimitInfoV2.
        :type value_unit: str
        """
        self._value_unit = value_unit

    @property
    def limit_type(self):
        """Gets the limit_type of this ICouponUseLimitInfoV2.

        限制类型。

        :return: The limit_type of this ICouponUseLimitInfoV2.
        :rtype: str
        """
        return self._limit_type

    @limit_type.setter
    def limit_type(self, limit_type):
        """Sets the limit_type of this ICouponUseLimitInfoV2.

        限制类型。

        :param limit_type: The limit_type of this ICouponUseLimitInfoV2.
        :type limit_type: str
        """
        self._limit_type = limit_type

    @property
    def promotion_plan_id(self):
        """Gets the promotion_plan_id of this ICouponUseLimitInfoV2.

        促销计划ID。

        :return: The promotion_plan_id of this ICouponUseLimitInfoV2.
        :rtype: str
        """
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, promotion_plan_id):
        """Sets the promotion_plan_id of this ICouponUseLimitInfoV2.

        促销计划ID。

        :param promotion_plan_id: The promotion_plan_id of this ICouponUseLimitInfoV2.
        :type promotion_plan_id: str
        """
        self._promotion_plan_id = promotion_plan_id

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
        if not isinstance(other, ICouponUseLimitInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
