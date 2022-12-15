# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BillingCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_type': 'str',
        'consistent_level': 'str',
        'object_type': 'str',
        'protect_type': 'str',
        'size': 'int',
        'charging_mode': 'str',
        'period_type': 'str',
        'period_num': 'int',
        'is_auto_renew': 'bool',
        'is_auto_pay': 'bool',
        'console_url': 'str',
        'extra_info': 'BillbingCreateExtraInfo',
        'is_multi_az': 'bool'
    }

    attribute_map = {
        'cloud_type': 'cloud_type',
        'consistent_level': 'consistent_level',
        'object_type': 'object_type',
        'protect_type': 'protect_type',
        'size': 'size',
        'charging_mode': 'charging_mode',
        'period_type': 'period_type',
        'period_num': 'period_num',
        'is_auto_renew': 'is_auto_renew',
        'is_auto_pay': 'is_auto_pay',
        'console_url': 'console_url',
        'extra_info': 'extra_info',
        'is_multi_az': 'is_multi_az'
    }

    def __init__(self, cloud_type=None, consistent_level=None, object_type=None, protect_type=None, size=None, charging_mode=None, period_type=None, period_num=None, is_auto_renew=None, is_auto_pay=None, console_url=None, extra_info=None, is_multi_az=None):
        """BillingCreate

        The model defined in huaweicloud sdk

        :param cloud_type: 云平台，公有云或者混合云
        :type cloud_type: str
        :param consistent_level: 规格，崩溃一致性（crash_consistent）或应用一致性（app_consistent）
        :type consistent_level: str
        :param object_type: 对象类型：云服务器（server），云硬盘（disk），文件系统（turbo），云桌面（workspace）。
        :type object_type: str
        :param protect_type: 保护类型：备份（backup）、复制(replication)
        :type protect_type: str
        :param size: 容量，单位GB
        :type size: int
        :param charging_mode: 创建模式，按需：post_paid，包周期：pre_paid，默认为post_paid
        :type charging_mode: str
        :param period_type: 创建类型，charging_mode为pre_paid必填，按年(year)或者按月(month)
        :type period_type: str
        :param period_num: 创建类型的数量，charging_mode为pre_paid必填
        :type period_num: int
        :param is_auto_renew: 到期后是否自动续期，默认不续期
        :type is_auto_renew: bool
        :param is_auto_pay: 是否自动付费，默认为不自动付费
        :type is_auto_pay: bool
        :param console_url: 跳转URL
        :type console_url: str
        :param extra_info: 
        :type extra_info: :class:`huaweicloudsdkcbr.v1.BillbingCreateExtraInfo`
        :param is_multi_az: 存储库多az属性，默认为false
        :type is_multi_az: bool
        """
        
        

        self._cloud_type = None
        self._consistent_level = None
        self._object_type = None
        self._protect_type = None
        self._size = None
        self._charging_mode = None
        self._period_type = None
        self._period_num = None
        self._is_auto_renew = None
        self._is_auto_pay = None
        self._console_url = None
        self._extra_info = None
        self._is_multi_az = None
        self.discriminator = None

        if cloud_type is not None:
            self.cloud_type = cloud_type
        self.consistent_level = consistent_level
        self.object_type = object_type
        self.protect_type = protect_type
        self.size = size
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay
        if console_url is not None:
            self.console_url = console_url
        if extra_info is not None:
            self.extra_info = extra_info
        if is_multi_az is not None:
            self.is_multi_az = is_multi_az

    @property
    def cloud_type(self):
        """Gets the cloud_type of this BillingCreate.

        云平台，公有云或者混合云

        :return: The cloud_type of this BillingCreate.
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this BillingCreate.

        云平台，公有云或者混合云

        :param cloud_type: The cloud_type of this BillingCreate.
        :type cloud_type: str
        """
        self._cloud_type = cloud_type

    @property
    def consistent_level(self):
        """Gets the consistent_level of this BillingCreate.

        规格，崩溃一致性（crash_consistent）或应用一致性（app_consistent）

        :return: The consistent_level of this BillingCreate.
        :rtype: str
        """
        return self._consistent_level

    @consistent_level.setter
    def consistent_level(self, consistent_level):
        """Sets the consistent_level of this BillingCreate.

        规格，崩溃一致性（crash_consistent）或应用一致性（app_consistent）

        :param consistent_level: The consistent_level of this BillingCreate.
        :type consistent_level: str
        """
        self._consistent_level = consistent_level

    @property
    def object_type(self):
        """Gets the object_type of this BillingCreate.

        对象类型：云服务器（server），云硬盘（disk），文件系统（turbo），云桌面（workspace）。

        :return: The object_type of this BillingCreate.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this BillingCreate.

        对象类型：云服务器（server），云硬盘（disk），文件系统（turbo），云桌面（workspace）。

        :param object_type: The object_type of this BillingCreate.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def protect_type(self):
        """Gets the protect_type of this BillingCreate.

        保护类型：备份（backup）、复制(replication)

        :return: The protect_type of this BillingCreate.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        """Sets the protect_type of this BillingCreate.

        保护类型：备份（backup）、复制(replication)

        :param protect_type: The protect_type of this BillingCreate.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def size(self):
        """Gets the size of this BillingCreate.

        容量，单位GB

        :return: The size of this BillingCreate.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BillingCreate.

        容量，单位GB

        :param size: The size of this BillingCreate.
        :type size: int
        """
        self._size = size

    @property
    def charging_mode(self):
        """Gets the charging_mode of this BillingCreate.

        创建模式，按需：post_paid，包周期：pre_paid，默认为post_paid

        :return: The charging_mode of this BillingCreate.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this BillingCreate.

        创建模式，按需：post_paid，包周期：pre_paid，默认为post_paid

        :param charging_mode: The charging_mode of this BillingCreate.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def period_type(self):
        """Gets the period_type of this BillingCreate.

        创建类型，charging_mode为pre_paid必填，按年(year)或者按月(month)

        :return: The period_type of this BillingCreate.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this BillingCreate.

        创建类型，charging_mode为pre_paid必填，按年(year)或者按月(month)

        :param period_type: The period_type of this BillingCreate.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        """Gets the period_num of this BillingCreate.

        创建类型的数量，charging_mode为pre_paid必填

        :return: The period_num of this BillingCreate.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this BillingCreate.

        创建类型的数量，charging_mode为pre_paid必填

        :param period_num: The period_num of this BillingCreate.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def is_auto_renew(self):
        """Gets the is_auto_renew of this BillingCreate.

        到期后是否自动续期，默认不续期

        :return: The is_auto_renew of this BillingCreate.
        :rtype: bool
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        """Sets the is_auto_renew of this BillingCreate.

        到期后是否自动续期，默认不续期

        :param is_auto_renew: The is_auto_renew of this BillingCreate.
        :type is_auto_renew: bool
        """
        self._is_auto_renew = is_auto_renew

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this BillingCreate.

        是否自动付费，默认为不自动付费

        :return: The is_auto_pay of this BillingCreate.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this BillingCreate.

        是否自动付费，默认为不自动付费

        :param is_auto_pay: The is_auto_pay of this BillingCreate.
        :type is_auto_pay: bool
        """
        self._is_auto_pay = is_auto_pay

    @property
    def console_url(self):
        """Gets the console_url of this BillingCreate.

        跳转URL

        :return: The console_url of this BillingCreate.
        :rtype: str
        """
        return self._console_url

    @console_url.setter
    def console_url(self, console_url):
        """Sets the console_url of this BillingCreate.

        跳转URL

        :param console_url: The console_url of this BillingCreate.
        :type console_url: str
        """
        self._console_url = console_url

    @property
    def extra_info(self):
        """Gets the extra_info of this BillingCreate.

        :return: The extra_info of this BillingCreate.
        :rtype: :class:`huaweicloudsdkcbr.v1.BillbingCreateExtraInfo`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this BillingCreate.

        :param extra_info: The extra_info of this BillingCreate.
        :type extra_info: :class:`huaweicloudsdkcbr.v1.BillbingCreateExtraInfo`
        """
        self._extra_info = extra_info

    @property
    def is_multi_az(self):
        """Gets the is_multi_az of this BillingCreate.

        存储库多az属性，默认为false

        :return: The is_multi_az of this BillingCreate.
        :rtype: bool
        """
        return self._is_multi_az

    @is_multi_az.setter
    def is_multi_az(self, is_multi_az):
        """Sets the is_multi_az of this BillingCreate.

        存储库多az属性，默认为false

        :param is_multi_az: The is_multi_az of this BillingCreate.
        :type is_multi_az: bool
        """
        self._is_multi_az = is_multi_az

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
        if not isinstance(other, BillingCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
