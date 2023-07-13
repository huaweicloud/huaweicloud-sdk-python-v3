# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlexibleOrigins:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'match_type': 'str',
        'match_pattern': 'str',
        'priority': 'int',
        'back_sources': 'list[BackSources]'
    }

    attribute_map = {
        'match_type': 'match_type',
        'match_pattern': 'match_pattern',
        'priority': 'priority',
        'back_sources': 'back_sources'
    }

    def __init__(self, match_type=None, match_pattern=None, priority=None, back_sources=None):
        """FlexibleOrigins

        The model defined in huaweicloud sdk

        :param match_type: URI的匹配方式，支持文件后缀（file_extension）和路径前缀（file_path）。
        :type match_type: str
        :param match_pattern: file_extension（文件后缀）： 支持所有格式的文件类型。 输入首字符为“.”，以“;”进行分隔。 输入的文件后缀名总数不能超过20个。 file_path（目录路径）：输入要求以“/”作为首字符，以“;”进行分隔，输入的目录路径总数不能超过20个。
        :type match_pattern: str
        :param priority: 优先级取值范围为1~100，数值越大优先级越高。
        :type priority: int
        :param back_sources: 回源信息。  &gt; 每个目录的回源源站数量不超过1个。
        :type back_sources: list[:class:`huaweicloudsdkcdn.v2.BackSources`]
        """
        
        

        self._match_type = None
        self._match_pattern = None
        self._priority = None
        self._back_sources = None
        self.discriminator = None

        self.match_type = match_type
        self.match_pattern = match_pattern
        self.priority = priority
        self.back_sources = back_sources

    @property
    def match_type(self):
        """Gets the match_type of this FlexibleOrigins.

        URI的匹配方式，支持文件后缀（file_extension）和路径前缀（file_path）。

        :return: The match_type of this FlexibleOrigins.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this FlexibleOrigins.

        URI的匹配方式，支持文件后缀（file_extension）和路径前缀（file_path）。

        :param match_type: The match_type of this FlexibleOrigins.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def match_pattern(self):
        """Gets the match_pattern of this FlexibleOrigins.

        file_extension（文件后缀）： 支持所有格式的文件类型。 输入首字符为“.”，以“;”进行分隔。 输入的文件后缀名总数不能超过20个。 file_path（目录路径）：输入要求以“/”作为首字符，以“;”进行分隔，输入的目录路径总数不能超过20个。

        :return: The match_pattern of this FlexibleOrigins.
        :rtype: str
        """
        return self._match_pattern

    @match_pattern.setter
    def match_pattern(self, match_pattern):
        """Sets the match_pattern of this FlexibleOrigins.

        file_extension（文件后缀）： 支持所有格式的文件类型。 输入首字符为“.”，以“;”进行分隔。 输入的文件后缀名总数不能超过20个。 file_path（目录路径）：输入要求以“/”作为首字符，以“;”进行分隔，输入的目录路径总数不能超过20个。

        :param match_pattern: The match_pattern of this FlexibleOrigins.
        :type match_pattern: str
        """
        self._match_pattern = match_pattern

    @property
    def priority(self):
        """Gets the priority of this FlexibleOrigins.

        优先级取值范围为1~100，数值越大优先级越高。

        :return: The priority of this FlexibleOrigins.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this FlexibleOrigins.

        优先级取值范围为1~100，数值越大优先级越高。

        :param priority: The priority of this FlexibleOrigins.
        :type priority: int
        """
        self._priority = priority

    @property
    def back_sources(self):
        """Gets the back_sources of this FlexibleOrigins.

        回源信息。  > 每个目录的回源源站数量不超过1个。

        :return: The back_sources of this FlexibleOrigins.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.BackSources`]
        """
        return self._back_sources

    @back_sources.setter
    def back_sources(self, back_sources):
        """Sets the back_sources of this FlexibleOrigins.

        回源信息。  > 每个目录的回源源站数量不超过1个。

        :param back_sources: The back_sources of this FlexibleOrigins.
        :type back_sources: list[:class:`huaweicloudsdkcdn.v2.BackSources`]
        """
        self._back_sources = back_sources

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
        if not isinstance(other, FlexibleOrigins):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
