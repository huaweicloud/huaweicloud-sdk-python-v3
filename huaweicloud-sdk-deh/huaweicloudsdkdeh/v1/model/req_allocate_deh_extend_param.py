# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqAllocateDehExtendParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charging_mode': 'str',
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_pay': 'bool',
        'is_auto_renew': 'bool',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'charging_mode': 'charging_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_pay': 'is_auto_pay',
        'is_auto_renew': 'is_auto_renew',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, charging_mode=None, period_type=None, period_num=None, is_auto_pay=None, is_auto_renew=None, enterprise_project_id=None):
        r"""ReqAllocateDehExtendParam

        The model defined in huaweicloud sdk

        :param charging_mode: 专属主机计费模式，不传该参数时默认为postPaid。 - prePaid：包周期 - postPaid：按需
        :type charging_mode: str
        :param period_type: 订购周期类型。 - month：包月 - year：包年
        :type period_type: str
        :param period_num: 订购周期数，大于0的整数，当charging_mode为prePaid时生效，且该字段必选。
        :type period_num: int
        :param is_auto_pay: 是否自动支付。
        :type is_auto_pay: bool
        :param is_auto_renew: 是否自动续费。
        :type is_auto_renew: bool
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._charging_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_pay = None
        self._is_auto_renew = None
        self._enterprise_project_id = None
        self.discriminator = None

        if charging_mode is not None:
            self.charging_mode = charging_mode
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ReqAllocateDehExtendParam.

        专属主机计费模式，不传该参数时默认为postPaid。 - prePaid：包周期 - postPaid：按需

        :return: The charging_mode of this ReqAllocateDehExtendParam.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ReqAllocateDehExtendParam.

        专属主机计费模式，不传该参数时默认为postPaid。 - prePaid：包周期 - postPaid：按需

        :param charging_mode: The charging_mode of this ReqAllocateDehExtendParam.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def period_type(self):
        r"""Gets the period_type of this ReqAllocateDehExtendParam.

        订购周期类型。 - month：包月 - year：包年

        :return: The period_type of this ReqAllocateDehExtendParam.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ReqAllocateDehExtendParam.

        订购周期类型。 - month：包月 - year：包年

        :param period_type: The period_type of this ReqAllocateDehExtendParam.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this ReqAllocateDehExtendParam.

        订购周期数，大于0的整数，当charging_mode为prePaid时生效，且该字段必选。

        :return: The period_num of this ReqAllocateDehExtendParam.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this ReqAllocateDehExtendParam.

        订购周期数，大于0的整数，当charging_mode为prePaid时生效，且该字段必选。

        :param period_num: The period_num of this ReqAllocateDehExtendParam.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this ReqAllocateDehExtendParam.

        是否自动支付。

        :return: The is_auto_pay of this ReqAllocateDehExtendParam.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this ReqAllocateDehExtendParam.

        是否自动支付。

        :param is_auto_pay: The is_auto_pay of this ReqAllocateDehExtendParam.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this ReqAllocateDehExtendParam.

        是否自动续费。

        :return: The is_auto_renew of this ReqAllocateDehExtendParam.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this ReqAllocateDehExtendParam.

        是否自动续费。

        :param is_auto_renew: The is_auto_renew of this ReqAllocateDehExtendParam.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ReqAllocateDehExtendParam.

        企业项目ID。

        :return: The enterprise_project_id of this ReqAllocateDehExtendParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ReqAllocateDehExtendParam.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ReqAllocateDehExtendParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ReqAllocateDehExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
