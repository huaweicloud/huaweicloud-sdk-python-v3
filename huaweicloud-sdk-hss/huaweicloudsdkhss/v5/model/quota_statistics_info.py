# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaStatisticsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'idle_num': 'int',
        'used_num': 'int',
        'total_num': 'int'
    }

    attribute_map = {
        'version': 'version',
        'idle_num': 'idle_num',
        'used_num': 'used_num',
        'total_num': 'total_num'
    }

    def __init__(self, version=None, idle_num=None, used_num=None, total_num=None):
        r"""QuotaStatisticsInfo

        The model defined in huaweicloud sdk

        :param version: version
        :type version: str
        :param idle_num: 空闲总数
        :type idle_num: int
        :param used_num: 使用中总数
        :type used_num: int
        :param total_num: 总数
        :type total_num: int
        """
        
        

        self._version = None
        self._idle_num = None
        self._used_num = None
        self._total_num = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if idle_num is not None:
            self.idle_num = idle_num
        if used_num is not None:
            self.used_num = used_num
        if total_num is not None:
            self.total_num = total_num

    @property
    def version(self):
        r"""Gets the version of this QuotaStatisticsInfo.

        version

        :return: The version of this QuotaStatisticsInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this QuotaStatisticsInfo.

        version

        :param version: The version of this QuotaStatisticsInfo.
        :type version: str
        """
        self._version = version

    @property
    def idle_num(self):
        r"""Gets the idle_num of this QuotaStatisticsInfo.

        空闲总数

        :return: The idle_num of this QuotaStatisticsInfo.
        :rtype: int
        """
        return self._idle_num

    @idle_num.setter
    def idle_num(self, idle_num):
        r"""Sets the idle_num of this QuotaStatisticsInfo.

        空闲总数

        :param idle_num: The idle_num of this QuotaStatisticsInfo.
        :type idle_num: int
        """
        self._idle_num = idle_num

    @property
    def used_num(self):
        r"""Gets the used_num of this QuotaStatisticsInfo.

        使用中总数

        :return: The used_num of this QuotaStatisticsInfo.
        :rtype: int
        """
        return self._used_num

    @used_num.setter
    def used_num(self, used_num):
        r"""Sets the used_num of this QuotaStatisticsInfo.

        使用中总数

        :param used_num: The used_num of this QuotaStatisticsInfo.
        :type used_num: int
        """
        self._used_num = used_num

    @property
    def total_num(self):
        r"""Gets the total_num of this QuotaStatisticsInfo.

        总数

        :return: The total_num of this QuotaStatisticsInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this QuotaStatisticsInfo.

        总数

        :param total_num: The total_num of this QuotaStatisticsInfo.
        :type total_num: int
        """
        self._total_num = total_num

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
        if not isinstance(other, QuotaStatisticsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
