# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeToPeriod:

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
        'is_auto_renew': 'bool',
        'is_auto_pay': 'bool',
        'console_url': 'str',
        'vault_ids': 'list[str]'
    }

    attribute_map = {
        'charging_mode': 'charging_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'is_auto_pay': 'is_auto_pay',
        'console_url': 'console_url',
        'vault_ids': 'vault_ids'
    }

    def __init__(self, charging_mode=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None, console_url=None, vault_ids=None):
        r"""ChangeToPeriod

        The model defined in huaweicloud sdk

        :param charging_mode: 付费模式，当前仅可选择：pre_paid
        :type charging_mode: str
        :param period_type: 创建类型，按年(year)或者按月(month)
        :type period_type: str
        :param period_num: 创建类型的数量，按年或按月的个数
        :type period_num: int
        :param is_auto_renew: 到期后是否自动续期，默认不续期
        :type is_auto_renew: bool
        :param is_auto_pay: 是否自动付费，默认为不自动付费
        :type is_auto_pay: bool
        :param console_url: 跳转URL
        :type console_url: str
        :param vault_ids: 资源列表
        :type vault_ids: list[str]
        """
        
        

        self._charging_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._console_url = None
        self._vault_ids = None
        self.discriminator = None

        if charging_mode is not None:
            self.charging_mode = charging_mode
        self.period_type = period_type
        self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if console_url is not None:
            self.console_url = console_url
        self.vault_ids = vault_ids

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ChangeToPeriod.

        付费模式，当前仅可选择：pre_paid

        :return: The charging_mode of this ChangeToPeriod.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ChangeToPeriod.

        付费模式，当前仅可选择：pre_paid

        :param charging_mode: The charging_mode of this ChangeToPeriod.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def period_type(self):
        r"""Gets the period_type of this ChangeToPeriod.

        创建类型，按年(year)或者按月(month)

        :return: The period_type of this ChangeToPeriod.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this ChangeToPeriod.

        创建类型，按年(year)或者按月(month)

        :param period_type: The period_type of this ChangeToPeriod.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this ChangeToPeriod.

        创建类型的数量，按年或按月的个数

        :return: The period_num of this ChangeToPeriod.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this ChangeToPeriod.

        创建类型的数量，按年或按月的个数

        :param period_num: The period_num of this ChangeToPeriod.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this ChangeToPeriod.

        到期后是否自动续期，默认不续期

        :return: The is_auto_renew of this ChangeToPeriod.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this ChangeToPeriod.

        到期后是否自动续期，默认不续期

        :param is_auto_renew: The is_auto_renew of this ChangeToPeriod.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this ChangeToPeriod.

        是否自动付费，默认为不自动付费

        :return: The is_auto_pay of this ChangeToPeriod.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this ChangeToPeriod.

        是否自动付费，默认为不自动付费

        :param is_auto_pay: The is_auto_pay of this ChangeToPeriod.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def console_url(self):
        r"""Gets the console_url of this ChangeToPeriod.

        跳转URL

        :return: The console_url of this ChangeToPeriod.
        :rtype: str
        """
        return self._console_url

    @console_url.setter
    def console_url(self, console_url):
        r"""Sets the console_url of this ChangeToPeriod.

        跳转URL

        :param console_url: The console_url of this ChangeToPeriod.
        :type console_url: str
        """
        self._console_url = console_url

    @property
    def vault_ids(self):
        r"""Gets the vault_ids of this ChangeToPeriod.

        资源列表

        :return: The vault_ids of this ChangeToPeriod.
        :rtype: list[str]
        """
        return self._vault_ids

    @vault_ids.setter
    def vault_ids(self, vault_ids):
        r"""Sets the vault_ids of this ChangeToPeriod.

        资源列表

        :param vault_ids: The vault_ids of this ChangeToPeriod.
        :type vault_ids: list[str]
        """
        self._vault_ids = vault_ids

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
        if not isinstance(other, ChangeToPeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
