# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopsStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_type': 'list[str]',
        'statistics_type': 'list[str]'
    }

    attribute_map = {
        'desktop_type': 'desktop_type',
        'statistics_type': 'statistics_type'
    }

    def __init__(self, desktop_type=None, statistics_type=None):
        r"""ListDesktopsStatisticsRequest

        The model defined in huaweicloud sdk

        :param desktop_type: 桌面类型，为空时查所有桌面。 - DEDICATED：普通桌面，包括专享桌面、专属桌面等 - POOLED：池桌面，即桌面池里的桌面
        :type desktop_type: list[str]
        :param statistics_type: 统计类型，为空时仅统计桌面总数 |- - attach-state 按照分配状态统计 - login-state 按照登录状态统计 - run-state 按照运行状态统计。
        :type statistics_type: list[str]
        """
        
        

        self._desktop_type = None
        self._statistics_type = None
        self.discriminator = None

        if desktop_type is not None:
            self.desktop_type = desktop_type
        if statistics_type is not None:
            self.statistics_type = statistics_type

    @property
    def desktop_type(self):
        r"""Gets the desktop_type of this ListDesktopsStatisticsRequest.

        桌面类型，为空时查所有桌面。 - DEDICATED：普通桌面，包括专享桌面、专属桌面等 - POOLED：池桌面，即桌面池里的桌面

        :return: The desktop_type of this ListDesktopsStatisticsRequest.
        :rtype: list[str]
        """
        return self._desktop_type

    @desktop_type.setter
    def desktop_type(self, desktop_type):
        r"""Sets the desktop_type of this ListDesktopsStatisticsRequest.

        桌面类型，为空时查所有桌面。 - DEDICATED：普通桌面，包括专享桌面、专属桌面等 - POOLED：池桌面，即桌面池里的桌面

        :param desktop_type: The desktop_type of this ListDesktopsStatisticsRequest.
        :type desktop_type: list[str]
        """
        self._desktop_type = desktop_type

    @property
    def statistics_type(self):
        r"""Gets the statistics_type of this ListDesktopsStatisticsRequest.

        统计类型，为空时仅统计桌面总数 |- - attach-state 按照分配状态统计 - login-state 按照登录状态统计 - run-state 按照运行状态统计。

        :return: The statistics_type of this ListDesktopsStatisticsRequest.
        :rtype: list[str]
        """
        return self._statistics_type

    @statistics_type.setter
    def statistics_type(self, statistics_type):
        r"""Sets the statistics_type of this ListDesktopsStatisticsRequest.

        统计类型，为空时仅统计桌面总数 |- - attach-state 按照分配状态统计 - login-state 按照登录状态统计 - run-state 按照运行状态统计。

        :param statistics_type: The statistics_type of this ListDesktopsStatisticsRequest.
        :type statistics_type: list[str]
        """
        self._statistics_type = statistics_type

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
        if not isinstance(other, ListDesktopsStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
