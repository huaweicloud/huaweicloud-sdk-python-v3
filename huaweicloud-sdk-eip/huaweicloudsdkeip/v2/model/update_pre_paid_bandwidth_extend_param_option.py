# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePrePaidBandwidthExtendParamOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_pay': 'bool'
    }

    attribute_map = {
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, period_type=None, period_num=None, is_auto_pay=None):
        r"""UpdatePrePaidBandwidthExtendParamOption

        The model defined in huaweicloud sdk

        :param period_type: - 功能说明：变更资源的周期类型（包年、包月等）,可选字段。 - 取值范围：    - month-月    - year-年 - 约束：只有在资源续费降配的时候必须传，其他场景不需要传，如果传入默认忽略。
        :type period_type: str
        :param period_num: - 功能说明：订购周期数，和period_type同步传入，可选字段 - 取值范围：(后续会随运营策略变化)    - period_type为month时，为[1,9]    - period_type为year时，为[1,3] - 约束：只有在资源续费降配的时候必须传，其他场景不需要传，如果传入默认忽略。该字段需要和period_type同步传入或同步不传
        :type period_num: int
        :param is_auto_pay: - 功能说明：下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付；系统默认是“非自动支付”。 - 取值范围：    - true：是（自动支付，从账户余额自动扣费）    - false：否（默认值，需要客户手动去支付） - 约束：资源升配或续费降配时，该参数为必传字段。自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择不自动支付，然后在用户费用中心，选择代金券支付。
        :type is_auto_pay: bool
        """
        
        

        self._period_type = None
        self._period_num = None
        self._is_auto_pay = None
        self.discriminator = None

        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def period_type(self):
        r"""Gets the period_type of this UpdatePrePaidBandwidthExtendParamOption.

        - 功能说明：变更资源的周期类型（包年、包月等）,可选字段。 - 取值范围：    - month-月    - year-年 - 约束：只有在资源续费降配的时候必须传，其他场景不需要传，如果传入默认忽略。

        :return: The period_type of this UpdatePrePaidBandwidthExtendParamOption.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this UpdatePrePaidBandwidthExtendParamOption.

        - 功能说明：变更资源的周期类型（包年、包月等）,可选字段。 - 取值范围：    - month-月    - year-年 - 约束：只有在资源续费降配的时候必须传，其他场景不需要传，如果传入默认忽略。

        :param period_type: The period_type of this UpdatePrePaidBandwidthExtendParamOption.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this UpdatePrePaidBandwidthExtendParamOption.

        - 功能说明：订购周期数，和period_type同步传入，可选字段 - 取值范围：(后续会随运营策略变化)    - period_type为month时，为[1,9]    - period_type为year时，为[1,3] - 约束：只有在资源续费降配的时候必须传，其他场景不需要传，如果传入默认忽略。该字段需要和period_type同步传入或同步不传

        :return: The period_num of this UpdatePrePaidBandwidthExtendParamOption.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this UpdatePrePaidBandwidthExtendParamOption.

        - 功能说明：订购周期数，和period_type同步传入，可选字段 - 取值范围：(后续会随运营策略变化)    - period_type为month时，为[1,9]    - period_type为year时，为[1,3] - 约束：只有在资源续费降配的时候必须传，其他场景不需要传，如果传入默认忽略。该字段需要和period_type同步传入或同步不传

        :param period_num: The period_num of this UpdatePrePaidBandwidthExtendParamOption.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this UpdatePrePaidBandwidthExtendParamOption.

        - 功能说明：下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付；系统默认是“非自动支付”。 - 取值范围：    - true：是（自动支付，从账户余额自动扣费）    - false：否（默认值，需要客户手动去支付） - 约束：资源升配或续费降配时，该参数为必传字段。自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择不自动支付，然后在用户费用中心，选择代金券支付。

        :return: The is_auto_pay of this UpdatePrePaidBandwidthExtendParamOption.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this UpdatePrePaidBandwidthExtendParamOption.

        - 功能说明：下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付；系统默认是“非自动支付”。 - 取值范围：    - true：是（自动支付，从账户余额自动扣费）    - false：否（默认值，需要客户手动去支付） - 约束：资源升配或续费降配时，该参数为必传字段。自动支付时，只能使用账户的现金支付；如果要使用代金券，请选择不自动支付，然后在用户费用中心，选择代金券支付。

        :param is_auto_pay: The is_auto_pay of this UpdatePrePaidBandwidthExtendParamOption.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, UpdatePrePaidBandwidthExtendParamOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
