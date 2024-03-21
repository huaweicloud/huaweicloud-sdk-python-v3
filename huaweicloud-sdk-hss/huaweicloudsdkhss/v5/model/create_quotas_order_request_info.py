# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateQuotasOrderRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_spec_code': 'str',
        'period_type': 'int',
        'period_num': 'int',
        'is_auto_renew': 'bool',
        'is_auto_pay': 'bool',
        'subscription_num': 'int'
    }

    attribute_map = {
        'resource_spec_code': 'resource_spec_code',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'is_auto_pay': 'is_auto_pay',
        'subscription_num': 'subscription_num'
    }

    def __init__(self, resource_spec_code=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None, subscription_num=None):
        """CreateQuotasOrderRequestInfo

        The model defined in huaweicloud sdk

        :param resource_spec_code: 资源规格   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。
        :type resource_spec_code: str
        :param period_type: 订购周期类型   - 2 : 月   - 3 : 年
        :type period_type: int
        :param period_num: 订购周期数
        :type period_num: int
        :param is_auto_renew: 是否支持自动续订，true表示自动续订，false表示不自动续订，默认值为false
        :type is_auto_renew: bool
        :param is_auto_pay: 是否支持自动支付，true表示支持，false表示不支持，默认值为false
        :type is_auto_pay: bool
        :param subscription_num: 订购数量
        :type subscription_num: int
        """
        
        

        self._resource_spec_code = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._subscription_num = None
        self.discriminator = None

        self.resource_spec_code = resource_spec_code
        self.period_type = period_type
        self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        self.subscription_num = subscription_num

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this CreateQuotasOrderRequestInfo.

        资源规格   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。

        :return: The resource_spec_code of this CreateQuotasOrderRequestInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this CreateQuotasOrderRequestInfo.

        资源规格   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。

        :param resource_spec_code: The resource_spec_code of this CreateQuotasOrderRequestInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def period_type(self):
        """Gets the period_type of this CreateQuotasOrderRequestInfo.

        订购周期类型   - 2 : 月   - 3 : 年

        :return: The period_type of this CreateQuotasOrderRequestInfo.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this CreateQuotasOrderRequestInfo.

        订购周期类型   - 2 : 月   - 3 : 年

        :param period_type: The period_type of this CreateQuotasOrderRequestInfo.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this CreateQuotasOrderRequestInfo.

        订购周期数

        :return: The period_num of this CreateQuotasOrderRequestInfo.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this CreateQuotasOrderRequestInfo.

        订购周期数

        :param period_num: The period_num of this CreateQuotasOrderRequestInfo.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this CreateQuotasOrderRequestInfo.

        是否支持自动续订，true表示自动续订，false表示不自动续订，默认值为false

        :return: The is_auto_renew of this CreateQuotasOrderRequestInfo.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this CreateQuotasOrderRequestInfo.

        是否支持自动续订，true表示自动续订，false表示不自动续订，默认值为false

        :param is_auto_renew: The is_auto_renew of this CreateQuotasOrderRequestInfo.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this CreateQuotasOrderRequestInfo.

        是否支持自动支付，true表示支持，false表示不支持，默认值为false

        :return: The is_auto_pay of this CreateQuotasOrderRequestInfo.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this CreateQuotasOrderRequestInfo.

        是否支持自动支付，true表示支持，false表示不支持，默认值为false

        :param is_auto_pay: The is_auto_pay of this CreateQuotasOrderRequestInfo.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def subscription_num(self):
        """Gets the subscription_num of this CreateQuotasOrderRequestInfo.

        订购数量

        :return: The subscription_num of this CreateQuotasOrderRequestInfo.
        :rtype: int
        """
        return self._subscription_num

    @subscription_num.setter
    def subscription_num(self, subscription_num):
        """Sets the subscription_num of this CreateQuotasOrderRequestInfo.

        订购数量

        :param subscription_num: The subscription_num of this CreateQuotasOrderRequestInfo.
        :type subscription_num: int
        """
        self._subscription_num = subscription_num

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
        if not isinstance(other, CreateQuotasOrderRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
