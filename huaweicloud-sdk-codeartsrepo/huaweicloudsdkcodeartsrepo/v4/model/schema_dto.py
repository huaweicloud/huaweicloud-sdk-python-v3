# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SchemaDto:

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
        'maximum_file_size': 'int',
        'maximum_line_length': 'int',
        'maximum_truncate_line': 'int',
        'create_at': 'str',
        'update_at': 'str',
        'rebuild_at': 'str',
        'last_build_at': 'str',
        'build_times': 'int',
        'query_times': 'int',
        'outline_times': 'int'
    }

    attribute_map = {
        'version': 'version',
        'maximum_file_size': 'maximum_file_size',
        'maximum_line_length': 'maximum_line_length',
        'maximum_truncate_line': 'maximum_truncate_line',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'rebuild_at': 'rebuild_at',
        'last_build_at': 'last_build_at',
        'build_times': 'build_times',
        'query_times': 'query_times',
        'outline_times': 'outline_times'
    }

    def __init__(self, version=None, maximum_file_size=None, maximum_line_length=None, maximum_truncate_line=None, create_at=None, update_at=None, rebuild_at=None, last_build_at=None, build_times=None, query_times=None, outline_times=None):
        r"""SchemaDto

        The model defined in huaweicloud sdk

        :param version: **参数解释：** 代码导航版本。 **约束限制：** 不涉及。
        :type version: str
        :param maximum_file_size: **参数解释：** 支持的最大文件大小。 **约束限制：** 不涉及。
        :type maximum_file_size: int
        :param maximum_line_length: **参数解释：** 支持的最大行数。 **约束限制：** 不涉及。
        :type maximum_line_length: int
        :param maximum_truncate_line: **参数解释：** 每行支持的最大字符数，超过将截断。 **约束限制：** 不涉及。
        :type maximum_truncate_line: int
        :param create_at: **参数解释：** 索引创建时间。 **约束限制：** 不涉及。
        :type create_at: str
        :param update_at: **参数解释：** 索引更新时间。 **约束限制：** 不涉及。
        :type update_at: str
        :param rebuild_at: **参数解释：** 索引重建时间。 **约束限制：** 不涉及。
        :type rebuild_at: str
        :param last_build_at: **参数解释：** 索引最近构建时间。 **约束限制：** 不涉及。
        :type last_build_at: str
        :param build_times: **参数解释：** 索引构建次数。 **约束限制：** 不涉及。
        :type build_times: int
        :param query_times: **参数解释：** 请求次数。 **约束限制：** 不涉及。
        :type query_times: int
        :param outline_times: **参数解释：** 索引大纲请求次数。 **约束限制：** 不涉及。
        :type outline_times: int
        """
        
        

        self._version = None
        self._maximum_file_size = None
        self._maximum_line_length = None
        self._maximum_truncate_line = None
        self._create_at = None
        self._update_at = None
        self._rebuild_at = None
        self._last_build_at = None
        self._build_times = None
        self._query_times = None
        self._outline_times = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if maximum_file_size is not None:
            self.maximum_file_size = maximum_file_size
        if maximum_line_length is not None:
            self.maximum_line_length = maximum_line_length
        if maximum_truncate_line is not None:
            self.maximum_truncate_line = maximum_truncate_line
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if rebuild_at is not None:
            self.rebuild_at = rebuild_at
        if last_build_at is not None:
            self.last_build_at = last_build_at
        if build_times is not None:
            self.build_times = build_times
        if query_times is not None:
            self.query_times = query_times
        if outline_times is not None:
            self.outline_times = outline_times

    @property
    def version(self):
        r"""Gets the version of this SchemaDto.

        **参数解释：** 代码导航版本。 **约束限制：** 不涉及。

        :return: The version of this SchemaDto.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this SchemaDto.

        **参数解释：** 代码导航版本。 **约束限制：** 不涉及。

        :param version: The version of this SchemaDto.
        :type version: str
        """
        self._version = version

    @property
    def maximum_file_size(self):
        r"""Gets the maximum_file_size of this SchemaDto.

        **参数解释：** 支持的最大文件大小。 **约束限制：** 不涉及。

        :return: The maximum_file_size of this SchemaDto.
        :rtype: int
        """
        return self._maximum_file_size

    @maximum_file_size.setter
    def maximum_file_size(self, maximum_file_size):
        r"""Sets the maximum_file_size of this SchemaDto.

        **参数解释：** 支持的最大文件大小。 **约束限制：** 不涉及。

        :param maximum_file_size: The maximum_file_size of this SchemaDto.
        :type maximum_file_size: int
        """
        self._maximum_file_size = maximum_file_size

    @property
    def maximum_line_length(self):
        r"""Gets the maximum_line_length of this SchemaDto.

        **参数解释：** 支持的最大行数。 **约束限制：** 不涉及。

        :return: The maximum_line_length of this SchemaDto.
        :rtype: int
        """
        return self._maximum_line_length

    @maximum_line_length.setter
    def maximum_line_length(self, maximum_line_length):
        r"""Sets the maximum_line_length of this SchemaDto.

        **参数解释：** 支持的最大行数。 **约束限制：** 不涉及。

        :param maximum_line_length: The maximum_line_length of this SchemaDto.
        :type maximum_line_length: int
        """
        self._maximum_line_length = maximum_line_length

    @property
    def maximum_truncate_line(self):
        r"""Gets the maximum_truncate_line of this SchemaDto.

        **参数解释：** 每行支持的最大字符数，超过将截断。 **约束限制：** 不涉及。

        :return: The maximum_truncate_line of this SchemaDto.
        :rtype: int
        """
        return self._maximum_truncate_line

    @maximum_truncate_line.setter
    def maximum_truncate_line(self, maximum_truncate_line):
        r"""Sets the maximum_truncate_line of this SchemaDto.

        **参数解释：** 每行支持的最大字符数，超过将截断。 **约束限制：** 不涉及。

        :param maximum_truncate_line: The maximum_truncate_line of this SchemaDto.
        :type maximum_truncate_line: int
        """
        self._maximum_truncate_line = maximum_truncate_line

    @property
    def create_at(self):
        r"""Gets the create_at of this SchemaDto.

        **参数解释：** 索引创建时间。 **约束限制：** 不涉及。

        :return: The create_at of this SchemaDto.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this SchemaDto.

        **参数解释：** 索引创建时间。 **约束限制：** 不涉及。

        :param create_at: The create_at of this SchemaDto.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this SchemaDto.

        **参数解释：** 索引更新时间。 **约束限制：** 不涉及。

        :return: The update_at of this SchemaDto.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this SchemaDto.

        **参数解释：** 索引更新时间。 **约束限制：** 不涉及。

        :param update_at: The update_at of this SchemaDto.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def rebuild_at(self):
        r"""Gets the rebuild_at of this SchemaDto.

        **参数解释：** 索引重建时间。 **约束限制：** 不涉及。

        :return: The rebuild_at of this SchemaDto.
        :rtype: str
        """
        return self._rebuild_at

    @rebuild_at.setter
    def rebuild_at(self, rebuild_at):
        r"""Sets the rebuild_at of this SchemaDto.

        **参数解释：** 索引重建时间。 **约束限制：** 不涉及。

        :param rebuild_at: The rebuild_at of this SchemaDto.
        :type rebuild_at: str
        """
        self._rebuild_at = rebuild_at

    @property
    def last_build_at(self):
        r"""Gets the last_build_at of this SchemaDto.

        **参数解释：** 索引最近构建时间。 **约束限制：** 不涉及。

        :return: The last_build_at of this SchemaDto.
        :rtype: str
        """
        return self._last_build_at

    @last_build_at.setter
    def last_build_at(self, last_build_at):
        r"""Sets the last_build_at of this SchemaDto.

        **参数解释：** 索引最近构建时间。 **约束限制：** 不涉及。

        :param last_build_at: The last_build_at of this SchemaDto.
        :type last_build_at: str
        """
        self._last_build_at = last_build_at

    @property
    def build_times(self):
        r"""Gets the build_times of this SchemaDto.

        **参数解释：** 索引构建次数。 **约束限制：** 不涉及。

        :return: The build_times of this SchemaDto.
        :rtype: int
        """
        return self._build_times

    @build_times.setter
    def build_times(self, build_times):
        r"""Sets the build_times of this SchemaDto.

        **参数解释：** 索引构建次数。 **约束限制：** 不涉及。

        :param build_times: The build_times of this SchemaDto.
        :type build_times: int
        """
        self._build_times = build_times

    @property
    def query_times(self):
        r"""Gets the query_times of this SchemaDto.

        **参数解释：** 请求次数。 **约束限制：** 不涉及。

        :return: The query_times of this SchemaDto.
        :rtype: int
        """
        return self._query_times

    @query_times.setter
    def query_times(self, query_times):
        r"""Sets the query_times of this SchemaDto.

        **参数解释：** 请求次数。 **约束限制：** 不涉及。

        :param query_times: The query_times of this SchemaDto.
        :type query_times: int
        """
        self._query_times = query_times

    @property
    def outline_times(self):
        r"""Gets the outline_times of this SchemaDto.

        **参数解释：** 索引大纲请求次数。 **约束限制：** 不涉及。

        :return: The outline_times of this SchemaDto.
        :rtype: int
        """
        return self._outline_times

    @outline_times.setter
    def outline_times(self, outline_times):
        r"""Sets the outline_times of this SchemaDto.

        **参数解释：** 索引大纲请求次数。 **约束限制：** 不涉及。

        :param outline_times: The outline_times of this SchemaDto.
        :type outline_times: int
        """
        self._outline_times = outline_times

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
        if not isinstance(other, SchemaDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
