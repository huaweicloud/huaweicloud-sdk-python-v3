# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpsContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'depth': 'int',
        'is_hex': 'bool',
        'is_ignore': 'bool',
        'is_uri': 'bool',
        'offset': 'int',
        'relative_position': 'int'
    }

    attribute_map = {
        'content': 'content',
        'depth': 'depth',
        'is_hex': 'is_hex',
        'is_ignore': 'is_ignore',
        'is_uri': 'is_uri',
        'offset': 'offset',
        'relative_position': 'relative_position'
    }

    def __init__(self, content=None, depth=None, is_hex=None, is_ignore=None, is_uri=None, offset=None, relative_position=None):
        r"""IpsContent

        The model defined in huaweicloud sdk

        :param content: **参数解释**： 内容 **取值范围**： 不涉及
        :type content: str
        :param depth: **参数解释**： 深度 **取值范围**： 不涉及
        :type depth: int
        :param is_hex: **参数解释**： 报文内容是否为十六进制 **取值范围**： 不涉及
        :type is_hex: bool
        :param is_ignore: **参数解释**： 是否忽略大小写 **取值范围**： 不涉及
        :type is_ignore: bool
        :param is_uri: **参数解释**： 是否在uri中截取报文 **取值范围**： 不涉及
        :type is_uri: bool
        :param offset: **参数解释**： 偏移量 **取值范围**： 不涉及
        :type offset: int
        :param relative_position: **参数解释**： 相对位置 **取值范围**： 不涉及
        :type relative_position: int
        """
        
        

        self._content = None
        self._depth = None
        self._is_hex = None
        self._is_ignore = None
        self._is_uri = None
        self._offset = None
        self._relative_position = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if depth is not None:
            self.depth = depth
        if is_hex is not None:
            self.is_hex = is_hex
        if is_ignore is not None:
            self.is_ignore = is_ignore
        if is_uri is not None:
            self.is_uri = is_uri
        if offset is not None:
            self.offset = offset
        if relative_position is not None:
            self.relative_position = relative_position

    @property
    def content(self):
        r"""Gets the content of this IpsContent.

        **参数解释**： 内容 **取值范围**： 不涉及

        :return: The content of this IpsContent.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this IpsContent.

        **参数解释**： 内容 **取值范围**： 不涉及

        :param content: The content of this IpsContent.
        :type content: str
        """
        self._content = content

    @property
    def depth(self):
        r"""Gets the depth of this IpsContent.

        **参数解释**： 深度 **取值范围**： 不涉及

        :return: The depth of this IpsContent.
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        r"""Sets the depth of this IpsContent.

        **参数解释**： 深度 **取值范围**： 不涉及

        :param depth: The depth of this IpsContent.
        :type depth: int
        """
        self._depth = depth

    @property
    def is_hex(self):
        r"""Gets the is_hex of this IpsContent.

        **参数解释**： 报文内容是否为十六进制 **取值范围**： 不涉及

        :return: The is_hex of this IpsContent.
        :rtype: bool
        """
        return self._is_hex

    @is_hex.setter
    def is_hex(self, is_hex):
        r"""Sets the is_hex of this IpsContent.

        **参数解释**： 报文内容是否为十六进制 **取值范围**： 不涉及

        :param is_hex: The is_hex of this IpsContent.
        :type is_hex: bool
        """
        self._is_hex = is_hex

    @property
    def is_ignore(self):
        r"""Gets the is_ignore of this IpsContent.

        **参数解释**： 是否忽略大小写 **取值范围**： 不涉及

        :return: The is_ignore of this IpsContent.
        :rtype: bool
        """
        return self._is_ignore

    @is_ignore.setter
    def is_ignore(self, is_ignore):
        r"""Sets the is_ignore of this IpsContent.

        **参数解释**： 是否忽略大小写 **取值范围**： 不涉及

        :param is_ignore: The is_ignore of this IpsContent.
        :type is_ignore: bool
        """
        self._is_ignore = is_ignore

    @property
    def is_uri(self):
        r"""Gets the is_uri of this IpsContent.

        **参数解释**： 是否在uri中截取报文 **取值范围**： 不涉及

        :return: The is_uri of this IpsContent.
        :rtype: bool
        """
        return self._is_uri

    @is_uri.setter
    def is_uri(self, is_uri):
        r"""Sets the is_uri of this IpsContent.

        **参数解释**： 是否在uri中截取报文 **取值范围**： 不涉及

        :param is_uri: The is_uri of this IpsContent.
        :type is_uri: bool
        """
        self._is_uri = is_uri

    @property
    def offset(self):
        r"""Gets the offset of this IpsContent.

        **参数解释**： 偏移量 **取值范围**： 不涉及

        :return: The offset of this IpsContent.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this IpsContent.

        **参数解释**： 偏移量 **取值范围**： 不涉及

        :param offset: The offset of this IpsContent.
        :type offset: int
        """
        self._offset = offset

    @property
    def relative_position(self):
        r"""Gets the relative_position of this IpsContent.

        **参数解释**： 相对位置 **取值范围**： 不涉及

        :return: The relative_position of this IpsContent.
        :rtype: int
        """
        return self._relative_position

    @relative_position.setter
    def relative_position(self, relative_position):
        r"""Sets the relative_position of this IpsContent.

        **参数解释**： 相对位置 **取值范围**： 不涉及

        :param relative_position: The relative_position of this IpsContent.
        :type relative_position: int
        """
        self._relative_position = relative_position

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
        if not isinstance(other, IpsContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
