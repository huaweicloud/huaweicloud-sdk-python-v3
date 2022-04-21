# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RankETLFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'filter_type': 'str',
        'time_type': 'str',
        'is_monday_first': 'bool'
    }

    attribute_map = {
        'filter_type': 'filter_type',
        'time_type': 'time_type',
        'is_monday_first': 'is_monday_first'
    }

    def __init__(self, filter_type=None, time_type=None, is_monday_first=None):
        """RankETLFilter

        The model defined in huaweicloud sdk

        :param filter_type: 行为去重方式： - abs_weight，权重绝对值 - date，日期
        :type filter_type: str
        :param time_type: 时间类型： - day，天 - week，周 - month，月 
        :type time_type: str
        :param is_monday_first: 周一是否是第一天。
        :type is_monday_first: bool
        """
        
        

        self._filter_type = None
        self._time_type = None
        self._is_monday_first = None
        self.discriminator = None

        self.filter_type = filter_type
        self.time_type = time_type
        if is_monday_first is not None:
            self.is_monday_first = is_monday_first

    @property
    def filter_type(self):
        """Gets the filter_type of this RankETLFilter.

        行为去重方式： - abs_weight，权重绝对值 - date，日期

        :return: The filter_type of this RankETLFilter.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this RankETLFilter.

        行为去重方式： - abs_weight，权重绝对值 - date，日期

        :param filter_type: The filter_type of this RankETLFilter.
        :type filter_type: str
        """
        self._filter_type = filter_type

    @property
    def time_type(self):
        """Gets the time_type of this RankETLFilter.

        时间类型： - day，天 - week，周 - month，月 

        :return: The time_type of this RankETLFilter.
        :rtype: str
        """
        return self._time_type

    @time_type.setter
    def time_type(self, time_type):
        """Sets the time_type of this RankETLFilter.

        时间类型： - day，天 - week，周 - month，月 

        :param time_type: The time_type of this RankETLFilter.
        :type time_type: str
        """
        self._time_type = time_type

    @property
    def is_monday_first(self):
        """Gets the is_monday_first of this RankETLFilter.

        周一是否是第一天。

        :return: The is_monday_first of this RankETLFilter.
        :rtype: bool
        """
        return self._is_monday_first

    @is_monday_first.setter
    def is_monday_first(self, is_monday_first):
        """Sets the is_monday_first of this RankETLFilter.

        周一是否是第一天。

        :param is_monday_first: The is_monday_first of this RankETLFilter.
        :type is_monday_first: bool
        """
        self._is_monday_first = is_monday_first

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
        if not isinstance(other, RankETLFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
