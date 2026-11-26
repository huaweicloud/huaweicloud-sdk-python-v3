# coding: utf-8

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
        r"""FlexibleOrigins

        The model defined in huaweicloud sdk

        :param match_type: **参数解释：** URI的匹配方式 **约束限制：** 不涉及 **取值范围：** - file_extension: 文件后缀匹配 - file_path: 目录路径 - all: 匹配所有文件  **默认取值：** 不涉及
        :type match_type: str
        :param match_pattern: **参数解释：** URI的匹配规则 **约束限制：** match_type为file_extension时：   - 支持所有格式的文件类型   - 输入首字符为“.”，以“;”进行分隔   - 输入的文件后缀名总数不能超过20个  match_type为file_path时：   - 要求以“/”作为首字符   - 以“;”进行分隔   - 输入的目录路径总数不能超过20个  match_type为all时：置空  &gt; 文件名后缀英文字符大、小写代表不同资源  **取值范围：** 1-512个字符 **默认取值：** 不涉及
        :type match_pattern: str
        :param priority: **参数解释：** 优先级 &gt; 数值越大优先级越高  **约束限制：** 不涉及 **取值范围：** 1-1000 **默认取值：** 不涉及
        :type priority: int
        :param back_sources: **参数解释：** 配置客户端请求匹配当前规则时，CDN节点回源访问的源站 **约束限制：** 每条规则的回源源站数量不超过1个 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type back_sources: list[:class:`huaweicloudsdkcdn.v2.BackSources`]
        """
        
        

        self._match_type = None
        self._match_pattern = None
        self._priority = None
        self._back_sources = None
        self.discriminator = None

        self.match_type = match_type
        if match_pattern is not None:
            self.match_pattern = match_pattern
        self.priority = priority
        self.back_sources = back_sources

    @property
    def match_type(self):
        r"""Gets the match_type of this FlexibleOrigins.

        **参数解释：** URI的匹配方式 **约束限制：** 不涉及 **取值范围：** - file_extension: 文件后缀匹配 - file_path: 目录路径 - all: 匹配所有文件  **默认取值：** 不涉及

        :return: The match_type of this FlexibleOrigins.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this FlexibleOrigins.

        **参数解释：** URI的匹配方式 **约束限制：** 不涉及 **取值范围：** - file_extension: 文件后缀匹配 - file_path: 目录路径 - all: 匹配所有文件  **默认取值：** 不涉及

        :param match_type: The match_type of this FlexibleOrigins.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def match_pattern(self):
        r"""Gets the match_pattern of this FlexibleOrigins.

        **参数解释：** URI的匹配规则 **约束限制：** match_type为file_extension时：   - 支持所有格式的文件类型   - 输入首字符为“.”，以“;”进行分隔   - 输入的文件后缀名总数不能超过20个  match_type为file_path时：   - 要求以“/”作为首字符   - 以“;”进行分隔   - 输入的目录路径总数不能超过20个  match_type为all时：置空  > 文件名后缀英文字符大、小写代表不同资源  **取值范围：** 1-512个字符 **默认取值：** 不涉及

        :return: The match_pattern of this FlexibleOrigins.
        :rtype: str
        """
        return self._match_pattern

    @match_pattern.setter
    def match_pattern(self, match_pattern):
        r"""Sets the match_pattern of this FlexibleOrigins.

        **参数解释：** URI的匹配规则 **约束限制：** match_type为file_extension时：   - 支持所有格式的文件类型   - 输入首字符为“.”，以“;”进行分隔   - 输入的文件后缀名总数不能超过20个  match_type为file_path时：   - 要求以“/”作为首字符   - 以“;”进行分隔   - 输入的目录路径总数不能超过20个  match_type为all时：置空  > 文件名后缀英文字符大、小写代表不同资源  **取值范围：** 1-512个字符 **默认取值：** 不涉及

        :param match_pattern: The match_pattern of this FlexibleOrigins.
        :type match_pattern: str
        """
        self._match_pattern = match_pattern

    @property
    def priority(self):
        r"""Gets the priority of this FlexibleOrigins.

        **参数解释：** 优先级 > 数值越大优先级越高  **约束限制：** 不涉及 **取值范围：** 1-1000 **默认取值：** 不涉及

        :return: The priority of this FlexibleOrigins.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this FlexibleOrigins.

        **参数解释：** 优先级 > 数值越大优先级越高  **约束限制：** 不涉及 **取值范围：** 1-1000 **默认取值：** 不涉及

        :param priority: The priority of this FlexibleOrigins.
        :type priority: int
        """
        self._priority = priority

    @property
    def back_sources(self):
        r"""Gets the back_sources of this FlexibleOrigins.

        **参数解释：** 配置客户端请求匹配当前规则时，CDN节点回源访问的源站 **约束限制：** 每条规则的回源源站数量不超过1个 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The back_sources of this FlexibleOrigins.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.BackSources`]
        """
        return self._back_sources

    @back_sources.setter
    def back_sources(self, back_sources):
        r"""Sets the back_sources of this FlexibleOrigins.

        **参数解释：** 配置客户端请求匹配当前规则时，CDN节点回源访问的源站 **约束限制：** 每条规则的回源源站数量不超过1个 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param back_sources: The back_sources of this FlexibleOrigins.
        :type back_sources: list[:class:`huaweicloudsdkcdn.v2.BackSources`]
        """
        self._back_sources = back_sources

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
