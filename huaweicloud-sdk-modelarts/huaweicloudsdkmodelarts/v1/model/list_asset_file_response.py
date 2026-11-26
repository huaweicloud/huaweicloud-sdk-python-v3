# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'contents': 'list[Content]',
        'is_truncated': 'bool',
        'marker': 'str',
        'next_marker': 'str',
        'max_keys': 'int',
        'bucket_name': 'str',
        'prefix': 'str',
        'common_prefixes': 'list[str]'
    }

    attribute_map = {
        'contents': 'contents',
        'is_truncated': 'is_truncated',
        'marker': 'marker',
        'next_marker': 'next_marker',
        'max_keys': 'max_keys',
        'bucket_name': 'bucket_name',
        'prefix': 'prefix',
        'common_prefixes': 'common_prefixes'
    }

    def __init__(self, contents=None, is_truncated=None, marker=None, next_marker=None, max_keys=None, bucket_name=None, prefix=None, common_prefixes=None):
        r"""ListAssetFileResponse

        The model defined in huaweicloud sdk

        :param contents: **参数解释**：列举的对象内容。
        :type contents: list[:class:`huaweicloudsdkmodelarts.v1.Content`]
        :param is_truncated: **参数解释**：表明本次返回的结果列表是否被截断。“true”表示本次没有返回全部结果；“false”表示本次已经返回了全部结果。 **取值范围**：true,false。
        :type is_truncated: bool
        :param marker: **参数解释**：列举桶内对象列表时，指定一个标识符，作为列举时的起始位置，从该标识符以后按对象名的字典顺序返回对象列表。 **取值范围**：长度大于0且不超过1024的字符串。
        :type marker: str
        :param next_marker: **参数解释**：如果本次没有返回全部结果，响应请求中将包含此字段，用于标明本次请求列举到的最后一个对象。后续请求可以指定Marker等于该值来列举剩余的对象。 **取值范围**：长度大于0且不超过1024的字符串。
        :type next_marker: str
        :param max_keys: **参数解释**：列举对象的最大数目，返回的对象列表将是按照字典顺序的最多前max_keys个对象。 **取值范围**：1-1000。
        :type max_keys: int
        :param bucket_name: **参数解释**：本次请求的桶名。 **约束限制**：桶的名字需全局唯一，不能与已有的任何桶名称重复，包括其他用户创建的桶。   桶命名规则如下：   - 3～63个字符，数字或字母开头，支持小写字母、数字、“-”、“.”。   - 禁止使用IP地址。   - 禁止以“-”或“.”开头及结尾。   - 禁止两个“.”相邻（如：“my..bucket”）。   - 禁止“.”和“-”相邻（如：“my-.bucket”和“my.-bucket”）。   - 同一用户在同一个区域多次创建同名桶不会报错，创建的桶属性以第一次请求为准。 **取值范围**：不涉及。
        :type bucket_name: str
        :param prefix: **参数解释**：列举桶内对象列表时，指定一个前缀，限定返回的对象名必须带有prefix前缀。 **取值范围**：不涉及。
        :type prefix: str
        :param common_prefixes: **参数解释**：列举桶内对象列表时，指定前缀列表，限定返回的对象名必须带有prefix前缀。
        :type common_prefixes: list[str]
        """
        
        super().__init__()

        self._contents = None
        self._is_truncated = None
        self._marker = None
        self._next_marker = None
        self._max_keys = None
        self._bucket_name = None
        self._prefix = None
        self._common_prefixes = None
        self.discriminator = None

        if contents is not None:
            self.contents = contents
        if is_truncated is not None:
            self.is_truncated = is_truncated
        if marker is not None:
            self.marker = marker
        if next_marker is not None:
            self.next_marker = next_marker
        if max_keys is not None:
            self.max_keys = max_keys
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if prefix is not None:
            self.prefix = prefix
        if common_prefixes is not None:
            self.common_prefixes = common_prefixes

    @property
    def contents(self):
        r"""Gets the contents of this ListAssetFileResponse.

        **参数解释**：列举的对象内容。

        :return: The contents of this ListAssetFileResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Content`]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this ListAssetFileResponse.

        **参数解释**：列举的对象内容。

        :param contents: The contents of this ListAssetFileResponse.
        :type contents: list[:class:`huaweicloudsdkmodelarts.v1.Content`]
        """
        self._contents = contents

    @property
    def is_truncated(self):
        r"""Gets the is_truncated of this ListAssetFileResponse.

        **参数解释**：表明本次返回的结果列表是否被截断。“true”表示本次没有返回全部结果；“false”表示本次已经返回了全部结果。 **取值范围**：true,false。

        :return: The is_truncated of this ListAssetFileResponse.
        :rtype: bool
        """
        return self._is_truncated

    @is_truncated.setter
    def is_truncated(self, is_truncated):
        r"""Sets the is_truncated of this ListAssetFileResponse.

        **参数解释**：表明本次返回的结果列表是否被截断。“true”表示本次没有返回全部结果；“false”表示本次已经返回了全部结果。 **取值范围**：true,false。

        :param is_truncated: The is_truncated of this ListAssetFileResponse.
        :type is_truncated: bool
        """
        self._is_truncated = is_truncated

    @property
    def marker(self):
        r"""Gets the marker of this ListAssetFileResponse.

        **参数解释**：列举桶内对象列表时，指定一个标识符，作为列举时的起始位置，从该标识符以后按对象名的字典顺序返回对象列表。 **取值范围**：长度大于0且不超过1024的字符串。

        :return: The marker of this ListAssetFileResponse.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAssetFileResponse.

        **参数解释**：列举桶内对象列表时，指定一个标识符，作为列举时的起始位置，从该标识符以后按对象名的字典顺序返回对象列表。 **取值范围**：长度大于0且不超过1024的字符串。

        :param marker: The marker of this ListAssetFileResponse.
        :type marker: str
        """
        self._marker = marker

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListAssetFileResponse.

        **参数解释**：如果本次没有返回全部结果，响应请求中将包含此字段，用于标明本次请求列举到的最后一个对象。后续请求可以指定Marker等于该值来列举剩余的对象。 **取值范围**：长度大于0且不超过1024的字符串。

        :return: The next_marker of this ListAssetFileResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListAssetFileResponse.

        **参数解释**：如果本次没有返回全部结果，响应请求中将包含此字段，用于标明本次请求列举到的最后一个对象。后续请求可以指定Marker等于该值来列举剩余的对象。 **取值范围**：长度大于0且不超过1024的字符串。

        :param next_marker: The next_marker of this ListAssetFileResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def max_keys(self):
        r"""Gets the max_keys of this ListAssetFileResponse.

        **参数解释**：列举对象的最大数目，返回的对象列表将是按照字典顺序的最多前max_keys个对象。 **取值范围**：1-1000。

        :return: The max_keys of this ListAssetFileResponse.
        :rtype: int
        """
        return self._max_keys

    @max_keys.setter
    def max_keys(self, max_keys):
        r"""Sets the max_keys of this ListAssetFileResponse.

        **参数解释**：列举对象的最大数目，返回的对象列表将是按照字典顺序的最多前max_keys个对象。 **取值范围**：1-1000。

        :param max_keys: The max_keys of this ListAssetFileResponse.
        :type max_keys: int
        """
        self._max_keys = max_keys

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ListAssetFileResponse.

        **参数解释**：本次请求的桶名。 **约束限制**：桶的名字需全局唯一，不能与已有的任何桶名称重复，包括其他用户创建的桶。   桶命名规则如下：   - 3～63个字符，数字或字母开头，支持小写字母、数字、“-”、“.”。   - 禁止使用IP地址。   - 禁止以“-”或“.”开头及结尾。   - 禁止两个“.”相邻（如：“my..bucket”）。   - 禁止“.”和“-”相邻（如：“my-.bucket”和“my.-bucket”）。   - 同一用户在同一个区域多次创建同名桶不会报错，创建的桶属性以第一次请求为准。 **取值范围**：不涉及。

        :return: The bucket_name of this ListAssetFileResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ListAssetFileResponse.

        **参数解释**：本次请求的桶名。 **约束限制**：桶的名字需全局唯一，不能与已有的任何桶名称重复，包括其他用户创建的桶。   桶命名规则如下：   - 3～63个字符，数字或字母开头，支持小写字母、数字、“-”、“.”。   - 禁止使用IP地址。   - 禁止以“-”或“.”开头及结尾。   - 禁止两个“.”相邻（如：“my..bucket”）。   - 禁止“.”和“-”相邻（如：“my-.bucket”和“my.-bucket”）。   - 同一用户在同一个区域多次创建同名桶不会报错，创建的桶属性以第一次请求为准。 **取值范围**：不涉及。

        :param bucket_name: The bucket_name of this ListAssetFileResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def prefix(self):
        r"""Gets the prefix of this ListAssetFileResponse.

        **参数解释**：列举桶内对象列表时，指定一个前缀，限定返回的对象名必须带有prefix前缀。 **取值范围**：不涉及。

        :return: The prefix of this ListAssetFileResponse.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this ListAssetFileResponse.

        **参数解释**：列举桶内对象列表时，指定一个前缀，限定返回的对象名必须带有prefix前缀。 **取值范围**：不涉及。

        :param prefix: The prefix of this ListAssetFileResponse.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def common_prefixes(self):
        r"""Gets the common_prefixes of this ListAssetFileResponse.

        **参数解释**：列举桶内对象列表时，指定前缀列表，限定返回的对象名必须带有prefix前缀。

        :return: The common_prefixes of this ListAssetFileResponse.
        :rtype: list[str]
        """
        return self._common_prefixes

    @common_prefixes.setter
    def common_prefixes(self, common_prefixes):
        r"""Sets the common_prefixes of this ListAssetFileResponse.

        **参数解释**：列举桶内对象列表时，指定前缀列表，限定返回的对象名必须带有prefix前缀。

        :param common_prefixes: The common_prefixes of this ListAssetFileResponse.
        :type common_prefixes: list[str]
        """
        self._common_prefixes = common_prefixes

    def to_dict(self):
        import warnings
        warnings.warn("ListAssetFileResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListAssetFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
