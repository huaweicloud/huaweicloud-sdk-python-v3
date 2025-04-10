# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Detail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_key': 'str',
        'regex': 'str',
        'keys': 'list[str]',
        'multi_line_regex': 'str',
        'keep_source': 'bool',
        'keep_source_if_parse_error': 'bool',
        'split_sep': 'str',
        'split_type': 'str',
        'fields': 'dict(str, str)',
        'drop_keys': 'list[str]',
        'source_keys': 'list[str]',
        'dest_keys': 'list[str]',
        'expand_depth': 'int',
        'expand_connector': 'str',
        'source_format': 'str',
        'source_value': 'str',
        'set_time': 'bool',
        'include': 'dict(str, str)',
        'exclude': 'dict(str, str)'
    }

    attribute_map = {
        'source_key': 'source_key',
        'regex': 'regex',
        'keys': 'keys',
        'multi_line_regex': 'multi_line_regex',
        'keep_source': 'keep_source',
        'keep_source_if_parse_error': 'keep_source_if_parse_error',
        'split_sep': 'split_sep',
        'split_type': 'split_type',
        'fields': 'fields',
        'drop_keys': 'drop_keys',
        'source_keys': 'source_keys',
        'dest_keys': 'dest_keys',
        'expand_depth': 'expand_depth',
        'expand_connector': 'expand_connector',
        'source_format': 'source_format',
        'source_value': 'source_value',
        'set_time': 'set_time',
        'include': 'include',
        'exclude': 'exclude'
    }

    def __init__(self, source_key=None, regex=None, keys=None, multi_line_regex=None, keep_source=None, keep_source_if_parse_error=None, split_sep=None, split_type=None, fields=None, drop_keys=None, source_keys=None, dest_keys=None, expand_depth=None, expand_connector=None, source_format=None, source_value=None, set_time=None, include=None, exclude=None):
        r"""Detail

        The model defined in huaweicloud sdk

        :param source_key: 自定义时间key字段名称
        :type source_key: str
        :param regex: 正则解析正则表达式 单行完全正则，多行完全正则需填此字段
        :type regex: str
        :param keys: 字段名称列表 与field_name字段保持一致
        :type keys: list[str]
        :param multi_line_regex: 首行正则表达式
        :type multi_line_regex: str
        :param keep_source: 是否上传原始日志
        :type keep_source: bool
        :param keep_source_if_parse_error: 是否上传解析失败日志
        :type keep_source_if_parse_error: bool
        :param split_sep: 分隔符 自定义字符最大长度10，自定义字符串最大长度30
        :type split_sep: str
        :param split_type: 分隔符类型：char-自定义字符；special_char-不可见字符；string-自定义字符串
        :type split_type: str
        :param fields: 添加的字段列表：&lt;字段名称 : 字段内容&gt;
        :type fields: dict(str, str)
        :param drop_keys: 删除的字段列表
        :type drop_keys: list[str]
        :param source_keys: 字段重命名源字段名称列表
        :type source_keys: list[str]
        :param dest_keys: 字段重命名替换的字段名称列表
        :type dest_keys: list[str]
        :param expand_depth: json解析深度，默认为1层最大4层
        :type expand_depth: int
        :param expand_connector: json解析字段名称连接符
        :type expand_connector: str
        :param source_format: 自定义时间时间格式
        :type source_format: str
        :param source_value: 自定义时间字段value
        :type source_value: str
        :param set_time: 是否开启自定义时间的开关
        :type set_time: bool
        :param include: 日志过滤白名单规则 key长度最大为256，value最大长度为128，key不可以重复
        :type include: dict(str, str)
        :param exclude: 日志过滤白名单规则 key长度最大为256，value最大长度为128，key不可以重复
        :type exclude: dict(str, str)
        """
        
        

        self._source_key = None
        self._regex = None
        self._keys = None
        self._multi_line_regex = None
        self._keep_source = None
        self._keep_source_if_parse_error = None
        self._split_sep = None
        self._split_type = None
        self._fields = None
        self._drop_keys = None
        self._source_keys = None
        self._dest_keys = None
        self._expand_depth = None
        self._expand_connector = None
        self._source_format = None
        self._source_value = None
        self._set_time = None
        self._include = None
        self._exclude = None
        self.discriminator = None

        if source_key is not None:
            self.source_key = source_key
        if regex is not None:
            self.regex = regex
        if keys is not None:
            self.keys = keys
        if multi_line_regex is not None:
            self.multi_line_regex = multi_line_regex
        if keep_source is not None:
            self.keep_source = keep_source
        if keep_source_if_parse_error is not None:
            self.keep_source_if_parse_error = keep_source_if_parse_error
        if split_sep is not None:
            self.split_sep = split_sep
        if split_type is not None:
            self.split_type = split_type
        if fields is not None:
            self.fields = fields
        if drop_keys is not None:
            self.drop_keys = drop_keys
        if source_keys is not None:
            self.source_keys = source_keys
        if dest_keys is not None:
            self.dest_keys = dest_keys
        if expand_depth is not None:
            self.expand_depth = expand_depth
        if expand_connector is not None:
            self.expand_connector = expand_connector
        if source_format is not None:
            self.source_format = source_format
        if source_value is not None:
            self.source_value = source_value
        if set_time is not None:
            self.set_time = set_time
        if include is not None:
            self.include = include
        if exclude is not None:
            self.exclude = exclude

    @property
    def source_key(self):
        r"""Gets the source_key of this Detail.

        自定义时间key字段名称

        :return: The source_key of this Detail.
        :rtype: str
        """
        return self._source_key

    @source_key.setter
    def source_key(self, source_key):
        r"""Sets the source_key of this Detail.

        自定义时间key字段名称

        :param source_key: The source_key of this Detail.
        :type source_key: str
        """
        self._source_key = source_key

    @property
    def regex(self):
        r"""Gets the regex of this Detail.

        正则解析正则表达式 单行完全正则，多行完全正则需填此字段

        :return: The regex of this Detail.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        r"""Sets the regex of this Detail.

        正则解析正则表达式 单行完全正则，多行完全正则需填此字段

        :param regex: The regex of this Detail.
        :type regex: str
        """
        self._regex = regex

    @property
    def keys(self):
        r"""Gets the keys of this Detail.

        字段名称列表 与field_name字段保持一致

        :return: The keys of this Detail.
        :rtype: list[str]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        r"""Sets the keys of this Detail.

        字段名称列表 与field_name字段保持一致

        :param keys: The keys of this Detail.
        :type keys: list[str]
        """
        self._keys = keys

    @property
    def multi_line_regex(self):
        r"""Gets the multi_line_regex of this Detail.

        首行正则表达式

        :return: The multi_line_regex of this Detail.
        :rtype: str
        """
        return self._multi_line_regex

    @multi_line_regex.setter
    def multi_line_regex(self, multi_line_regex):
        r"""Sets the multi_line_regex of this Detail.

        首行正则表达式

        :param multi_line_regex: The multi_line_regex of this Detail.
        :type multi_line_regex: str
        """
        self._multi_line_regex = multi_line_regex

    @property
    def keep_source(self):
        r"""Gets the keep_source of this Detail.

        是否上传原始日志

        :return: The keep_source of this Detail.
        :rtype: bool
        """
        return self._keep_source

    @keep_source.setter
    def keep_source(self, keep_source):
        r"""Sets the keep_source of this Detail.

        是否上传原始日志

        :param keep_source: The keep_source of this Detail.
        :type keep_source: bool
        """
        self._keep_source = keep_source

    @property
    def keep_source_if_parse_error(self):
        r"""Gets the keep_source_if_parse_error of this Detail.

        是否上传解析失败日志

        :return: The keep_source_if_parse_error of this Detail.
        :rtype: bool
        """
        return self._keep_source_if_parse_error

    @keep_source_if_parse_error.setter
    def keep_source_if_parse_error(self, keep_source_if_parse_error):
        r"""Sets the keep_source_if_parse_error of this Detail.

        是否上传解析失败日志

        :param keep_source_if_parse_error: The keep_source_if_parse_error of this Detail.
        :type keep_source_if_parse_error: bool
        """
        self._keep_source_if_parse_error = keep_source_if_parse_error

    @property
    def split_sep(self):
        r"""Gets the split_sep of this Detail.

        分隔符 自定义字符最大长度10，自定义字符串最大长度30

        :return: The split_sep of this Detail.
        :rtype: str
        """
        return self._split_sep

    @split_sep.setter
    def split_sep(self, split_sep):
        r"""Sets the split_sep of this Detail.

        分隔符 自定义字符最大长度10，自定义字符串最大长度30

        :param split_sep: The split_sep of this Detail.
        :type split_sep: str
        """
        self._split_sep = split_sep

    @property
    def split_type(self):
        r"""Gets the split_type of this Detail.

        分隔符类型：char-自定义字符；special_char-不可见字符；string-自定义字符串

        :return: The split_type of this Detail.
        :rtype: str
        """
        return self._split_type

    @split_type.setter
    def split_type(self, split_type):
        r"""Sets the split_type of this Detail.

        分隔符类型：char-自定义字符；special_char-不可见字符；string-自定义字符串

        :param split_type: The split_type of this Detail.
        :type split_type: str
        """
        self._split_type = split_type

    @property
    def fields(self):
        r"""Gets the fields of this Detail.

        添加的字段列表：<字段名称 : 字段内容>

        :return: The fields of this Detail.
        :rtype: dict(str, str)
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this Detail.

        添加的字段列表：<字段名称 : 字段内容>

        :param fields: The fields of this Detail.
        :type fields: dict(str, str)
        """
        self._fields = fields

    @property
    def drop_keys(self):
        r"""Gets the drop_keys of this Detail.

        删除的字段列表

        :return: The drop_keys of this Detail.
        :rtype: list[str]
        """
        return self._drop_keys

    @drop_keys.setter
    def drop_keys(self, drop_keys):
        r"""Sets the drop_keys of this Detail.

        删除的字段列表

        :param drop_keys: The drop_keys of this Detail.
        :type drop_keys: list[str]
        """
        self._drop_keys = drop_keys

    @property
    def source_keys(self):
        r"""Gets the source_keys of this Detail.

        字段重命名源字段名称列表

        :return: The source_keys of this Detail.
        :rtype: list[str]
        """
        return self._source_keys

    @source_keys.setter
    def source_keys(self, source_keys):
        r"""Sets the source_keys of this Detail.

        字段重命名源字段名称列表

        :param source_keys: The source_keys of this Detail.
        :type source_keys: list[str]
        """
        self._source_keys = source_keys

    @property
    def dest_keys(self):
        r"""Gets the dest_keys of this Detail.

        字段重命名替换的字段名称列表

        :return: The dest_keys of this Detail.
        :rtype: list[str]
        """
        return self._dest_keys

    @dest_keys.setter
    def dest_keys(self, dest_keys):
        r"""Sets the dest_keys of this Detail.

        字段重命名替换的字段名称列表

        :param dest_keys: The dest_keys of this Detail.
        :type dest_keys: list[str]
        """
        self._dest_keys = dest_keys

    @property
    def expand_depth(self):
        r"""Gets the expand_depth of this Detail.

        json解析深度，默认为1层最大4层

        :return: The expand_depth of this Detail.
        :rtype: int
        """
        return self._expand_depth

    @expand_depth.setter
    def expand_depth(self, expand_depth):
        r"""Sets the expand_depth of this Detail.

        json解析深度，默认为1层最大4层

        :param expand_depth: The expand_depth of this Detail.
        :type expand_depth: int
        """
        self._expand_depth = expand_depth

    @property
    def expand_connector(self):
        r"""Gets the expand_connector of this Detail.

        json解析字段名称连接符

        :return: The expand_connector of this Detail.
        :rtype: str
        """
        return self._expand_connector

    @expand_connector.setter
    def expand_connector(self, expand_connector):
        r"""Sets the expand_connector of this Detail.

        json解析字段名称连接符

        :param expand_connector: The expand_connector of this Detail.
        :type expand_connector: str
        """
        self._expand_connector = expand_connector

    @property
    def source_format(self):
        r"""Gets the source_format of this Detail.

        自定义时间时间格式

        :return: The source_format of this Detail.
        :rtype: str
        """
        return self._source_format

    @source_format.setter
    def source_format(self, source_format):
        r"""Sets the source_format of this Detail.

        自定义时间时间格式

        :param source_format: The source_format of this Detail.
        :type source_format: str
        """
        self._source_format = source_format

    @property
    def source_value(self):
        r"""Gets the source_value of this Detail.

        自定义时间字段value

        :return: The source_value of this Detail.
        :rtype: str
        """
        return self._source_value

    @source_value.setter
    def source_value(self, source_value):
        r"""Sets the source_value of this Detail.

        自定义时间字段value

        :param source_value: The source_value of this Detail.
        :type source_value: str
        """
        self._source_value = source_value

    @property
    def set_time(self):
        r"""Gets the set_time of this Detail.

        是否开启自定义时间的开关

        :return: The set_time of this Detail.
        :rtype: bool
        """
        return self._set_time

    @set_time.setter
    def set_time(self, set_time):
        r"""Sets the set_time of this Detail.

        是否开启自定义时间的开关

        :param set_time: The set_time of this Detail.
        :type set_time: bool
        """
        self._set_time = set_time

    @property
    def include(self):
        r"""Gets the include of this Detail.

        日志过滤白名单规则 key长度最大为256，value最大长度为128，key不可以重复

        :return: The include of this Detail.
        :rtype: dict(str, str)
        """
        return self._include

    @include.setter
    def include(self, include):
        r"""Sets the include of this Detail.

        日志过滤白名单规则 key长度最大为256，value最大长度为128，key不可以重复

        :param include: The include of this Detail.
        :type include: dict(str, str)
        """
        self._include = include

    @property
    def exclude(self):
        r"""Gets the exclude of this Detail.

        日志过滤白名单规则 key长度最大为256，value最大长度为128，key不可以重复

        :return: The exclude of this Detail.
        :rtype: dict(str, str)
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        r"""Sets the exclude of this Detail.

        日志过滤白名单规则 key长度最大为256，value最大长度为128，key不可以重复

        :param exclude: The exclude of this Detail.
        :type exclude: dict(str, str)
        """
        self._exclude = exclude

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
        if not isinstance(other, Detail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
