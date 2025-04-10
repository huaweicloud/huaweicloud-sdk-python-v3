# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CronConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'cron': 'str',
        'count': 'int',
        'start_time': 'int',
        'expired_time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'cron': 'cron',
        'count': 'count',
        'start_time': 'start_time',
        'expired_time': 'expired_time'
    }

    def __init__(self, name=None, cron=None, count=None, start_time=None, expired_time=None):
        r"""CronConfig

        The model defined in huaweicloud sdk

        :param name: 定时配置名称
        :type name: str
        :param cron: 定时表达式
        :type cron: str
        :param count: 拉起预留实例个数
        :type count: int
        :param start_time: 开始时间戳
        :type start_time: int
        :param expired_time: 失效时间戳
        :type expired_time: int
        """
        
        

        self._name = None
        self._cron = None
        self._count = None
        self._start_time = None
        self._expired_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if cron is not None:
            self.cron = cron
        if count is not None:
            self.count = count
        if start_time is not None:
            self.start_time = start_time
        if expired_time is not None:
            self.expired_time = expired_time

    @property
    def name(self):
        r"""Gets the name of this CronConfig.

        定时配置名称

        :return: The name of this CronConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CronConfig.

        定时配置名称

        :param name: The name of this CronConfig.
        :type name: str
        """
        self._name = name

    @property
    def cron(self):
        r"""Gets the cron of this CronConfig.

        定时表达式

        :return: The cron of this CronConfig.
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        r"""Sets the cron of this CronConfig.

        定时表达式

        :param cron: The cron of this CronConfig.
        :type cron: str
        """
        self._cron = cron

    @property
    def count(self):
        r"""Gets the count of this CronConfig.

        拉起预留实例个数

        :return: The count of this CronConfig.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this CronConfig.

        拉起预留实例个数

        :param count: The count of this CronConfig.
        :type count: int
        """
        self._count = count

    @property
    def start_time(self):
        r"""Gets the start_time of this CronConfig.

        开始时间戳

        :return: The start_time of this CronConfig.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CronConfig.

        开始时间戳

        :param start_time: The start_time of this CronConfig.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def expired_time(self):
        r"""Gets the expired_time of this CronConfig.

        失效时间戳

        :return: The expired_time of this CronConfig.
        :rtype: int
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        r"""Sets the expired_time of this CronConfig.

        失效时间戳

        :param expired_time: The expired_time of this CronConfig.
        :type expired_time: int
        """
        self._expired_time = expired_time

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
        if not isinstance(other, CronConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
