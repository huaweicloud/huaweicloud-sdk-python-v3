# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchAutoEnlargePolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_option': 'bool',
        'limit_volume_size': 'int',
        'min_volume_size': 'int',
        'max_volume_size': 'int',
        'trigger_available_percent': 'int',
        'percents': 'list[int]'
    }

    attribute_map = {
        'switch_option': 'switch_option',
        'limit_volume_size': 'limit_volume_size',
        'min_volume_size': 'min_volume_size',
        'max_volume_size': 'max_volume_size',
        'trigger_available_percent': 'trigger_available_percent',
        'percents': 'percents'
    }

    def __init__(self, switch_option=None, limit_volume_size=None, min_volume_size=None, max_volume_size=None, trigger_available_percent=None, percents=None):
        """SearchAutoEnlargePolicyResponse

        The model defined in huaweicloud sdk

        :param switch_option: 磁盘自动扩容开关。
        :type switch_option: bool
        :param limit_volume_size: 存储自动扩容上限。
        :type limit_volume_size: int
        :param min_volume_size: 最小扩容磁盘容量。
        :type min_volume_size: int
        :param max_volume_size: 最大扩容磁盘容量。
        :type max_volume_size: int
        :param trigger_available_percent: 可用存储空间率。
        :type trigger_available_percent: int
        :param percents: 空间率集合。
        :type percents: list[int]
        """
        
        super(SearchAutoEnlargePolicyResponse, self).__init__()

        self._switch_option = None
        self._limit_volume_size = None
        self._min_volume_size = None
        self._max_volume_size = None
        self._trigger_available_percent = None
        self._percents = None
        self.discriminator = None

        if switch_option is not None:
            self.switch_option = switch_option
        if limit_volume_size is not None:
            self.limit_volume_size = limit_volume_size
        if min_volume_size is not None:
            self.min_volume_size = min_volume_size
        if max_volume_size is not None:
            self.max_volume_size = max_volume_size
        if trigger_available_percent is not None:
            self.trigger_available_percent = trigger_available_percent
        if percents is not None:
            self.percents = percents

    @property
    def switch_option(self):
        """Gets the switch_option of this SearchAutoEnlargePolicyResponse.

        磁盘自动扩容开关。

        :return: The switch_option of this SearchAutoEnlargePolicyResponse.
        :rtype: bool
        """
        return self._switch_option

    @switch_option.setter
    def switch_option(self, switch_option):
        """Sets the switch_option of this SearchAutoEnlargePolicyResponse.

        磁盘自动扩容开关。

        :param switch_option: The switch_option of this SearchAutoEnlargePolicyResponse.
        :type switch_option: bool
        """
        self._switch_option = switch_option

    @property
    def limit_volume_size(self):
        """Gets the limit_volume_size of this SearchAutoEnlargePolicyResponse.

        存储自动扩容上限。

        :return: The limit_volume_size of this SearchAutoEnlargePolicyResponse.
        :rtype: int
        """
        return self._limit_volume_size

    @limit_volume_size.setter
    def limit_volume_size(self, limit_volume_size):
        """Sets the limit_volume_size of this SearchAutoEnlargePolicyResponse.

        存储自动扩容上限。

        :param limit_volume_size: The limit_volume_size of this SearchAutoEnlargePolicyResponse.
        :type limit_volume_size: int
        """
        self._limit_volume_size = limit_volume_size

    @property
    def min_volume_size(self):
        """Gets the min_volume_size of this SearchAutoEnlargePolicyResponse.

        最小扩容磁盘容量。

        :return: The min_volume_size of this SearchAutoEnlargePolicyResponse.
        :rtype: int
        """
        return self._min_volume_size

    @min_volume_size.setter
    def min_volume_size(self, min_volume_size):
        """Sets the min_volume_size of this SearchAutoEnlargePolicyResponse.

        最小扩容磁盘容量。

        :param min_volume_size: The min_volume_size of this SearchAutoEnlargePolicyResponse.
        :type min_volume_size: int
        """
        self._min_volume_size = min_volume_size

    @property
    def max_volume_size(self):
        """Gets the max_volume_size of this SearchAutoEnlargePolicyResponse.

        最大扩容磁盘容量。

        :return: The max_volume_size of this SearchAutoEnlargePolicyResponse.
        :rtype: int
        """
        return self._max_volume_size

    @max_volume_size.setter
    def max_volume_size(self, max_volume_size):
        """Sets the max_volume_size of this SearchAutoEnlargePolicyResponse.

        最大扩容磁盘容量。

        :param max_volume_size: The max_volume_size of this SearchAutoEnlargePolicyResponse.
        :type max_volume_size: int
        """
        self._max_volume_size = max_volume_size

    @property
    def trigger_available_percent(self):
        """Gets the trigger_available_percent of this SearchAutoEnlargePolicyResponse.

        可用存储空间率。

        :return: The trigger_available_percent of this SearchAutoEnlargePolicyResponse.
        :rtype: int
        """
        return self._trigger_available_percent

    @trigger_available_percent.setter
    def trigger_available_percent(self, trigger_available_percent):
        """Sets the trigger_available_percent of this SearchAutoEnlargePolicyResponse.

        可用存储空间率。

        :param trigger_available_percent: The trigger_available_percent of this SearchAutoEnlargePolicyResponse.
        :type trigger_available_percent: int
        """
        self._trigger_available_percent = trigger_available_percent

    @property
    def percents(self):
        """Gets the percents of this SearchAutoEnlargePolicyResponse.

        空间率集合。

        :return: The percents of this SearchAutoEnlargePolicyResponse.
        :rtype: list[int]
        """
        return self._percents

    @percents.setter
    def percents(self, percents):
        """Sets the percents of this SearchAutoEnlargePolicyResponse.

        空间率集合。

        :param percents: The percents of this SearchAutoEnlargePolicyResponse.
        :type percents: list[int]
        """
        self._percents = percents

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
        if not isinstance(other, SearchAutoEnlargePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
