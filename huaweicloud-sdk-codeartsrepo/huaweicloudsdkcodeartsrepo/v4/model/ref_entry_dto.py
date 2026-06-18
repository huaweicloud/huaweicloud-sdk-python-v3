# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RefEntryDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_name': 'str',
        'file_path': 'str',
        'blob': 'str',
        'line_image': 'str',
        'line_number': 'int',
        'syntax_type': 'str',
        'revision': 'str',
        'extend': 'str'
    }

    attribute_map = {
        'tag_name': 'tag_name',
        'file_path': 'file_path',
        'blob': 'blob',
        'line_image': 'line_image',
        'line_number': 'line_number',
        'syntax_type': 'syntax_type',
        'revision': 'revision',
        'extend': 'extend'
    }

    def __init__(self, tag_name=None, file_path=None, blob=None, line_image=None, line_number=None, syntax_type=None, revision=None, extend=None):
        r"""RefEntryDto

        The model defined in huaweicloud sdk

        :param tag_name: **参数解释：** 标记名称。 **约束限制：** 不涉及。
        :type tag_name: str
        :param file_path: **参数解释：** 文件路径。 **约束限制：** 不涉及。
        :type file_path: str
        :param blob: **参数解释：** blob文件ID。 **约束限制：** 不涉及。
        :type blob: str
        :param line_image: **参数解释：** 索引行简要内容。 **约束限制：** 不涉及。
        :type line_image: str
        :param line_number: **参数解释：** 行号。 **约束限制：** 不涉及。
        :type line_number: int
        :param syntax_type: **参数解释：** 语法类型。 **约束限制：** 不涉及。
        :type syntax_type: str
        :param revision: **参数解释：** 所在版本号（commit id）。 **约束限制：** 不涉及。
        :type revision: str
        :param extend: **参数解释：** 其他信息。 **约束限制：** 不涉及。    
        :type extend: str
        """
        
        

        self._tag_name = None
        self._file_path = None
        self._blob = None
        self._line_image = None
        self._line_number = None
        self._syntax_type = None
        self._revision = None
        self._extend = None
        self.discriminator = None

        if tag_name is not None:
            self.tag_name = tag_name
        if file_path is not None:
            self.file_path = file_path
        if blob is not None:
            self.blob = blob
        if line_image is not None:
            self.line_image = line_image
        if line_number is not None:
            self.line_number = line_number
        if syntax_type is not None:
            self.syntax_type = syntax_type
        if revision is not None:
            self.revision = revision
        if extend is not None:
            self.extend = extend

    @property
    def tag_name(self):
        r"""Gets the tag_name of this RefEntryDto.

        **参数解释：** 标记名称。 **约束限制：** 不涉及。

        :return: The tag_name of this RefEntryDto.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        r"""Sets the tag_name of this RefEntryDto.

        **参数解释：** 标记名称。 **约束限制：** 不涉及。

        :param tag_name: The tag_name of this RefEntryDto.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def file_path(self):
        r"""Gets the file_path of this RefEntryDto.

        **参数解释：** 文件路径。 **约束限制：** 不涉及。

        :return: The file_path of this RefEntryDto.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this RefEntryDto.

        **参数解释：** 文件路径。 **约束限制：** 不涉及。

        :param file_path: The file_path of this RefEntryDto.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def blob(self):
        r"""Gets the blob of this RefEntryDto.

        **参数解释：** blob文件ID。 **约束限制：** 不涉及。

        :return: The blob of this RefEntryDto.
        :rtype: str
        """
        return self._blob

    @blob.setter
    def blob(self, blob):
        r"""Sets the blob of this RefEntryDto.

        **参数解释：** blob文件ID。 **约束限制：** 不涉及。

        :param blob: The blob of this RefEntryDto.
        :type blob: str
        """
        self._blob = blob

    @property
    def line_image(self):
        r"""Gets the line_image of this RefEntryDto.

        **参数解释：** 索引行简要内容。 **约束限制：** 不涉及。

        :return: The line_image of this RefEntryDto.
        :rtype: str
        """
        return self._line_image

    @line_image.setter
    def line_image(self, line_image):
        r"""Sets the line_image of this RefEntryDto.

        **参数解释：** 索引行简要内容。 **约束限制：** 不涉及。

        :param line_image: The line_image of this RefEntryDto.
        :type line_image: str
        """
        self._line_image = line_image

    @property
    def line_number(self):
        r"""Gets the line_number of this RefEntryDto.

        **参数解释：** 行号。 **约束限制：** 不涉及。

        :return: The line_number of this RefEntryDto.
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        r"""Sets the line_number of this RefEntryDto.

        **参数解释：** 行号。 **约束限制：** 不涉及。

        :param line_number: The line_number of this RefEntryDto.
        :type line_number: int
        """
        self._line_number = line_number

    @property
    def syntax_type(self):
        r"""Gets the syntax_type of this RefEntryDto.

        **参数解释：** 语法类型。 **约束限制：** 不涉及。

        :return: The syntax_type of this RefEntryDto.
        :rtype: str
        """
        return self._syntax_type

    @syntax_type.setter
    def syntax_type(self, syntax_type):
        r"""Sets the syntax_type of this RefEntryDto.

        **参数解释：** 语法类型。 **约束限制：** 不涉及。

        :param syntax_type: The syntax_type of this RefEntryDto.
        :type syntax_type: str
        """
        self._syntax_type = syntax_type

    @property
    def revision(self):
        r"""Gets the revision of this RefEntryDto.

        **参数解释：** 所在版本号（commit id）。 **约束限制：** 不涉及。

        :return: The revision of this RefEntryDto.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        r"""Sets the revision of this RefEntryDto.

        **参数解释：** 所在版本号（commit id）。 **约束限制：** 不涉及。

        :param revision: The revision of this RefEntryDto.
        :type revision: str
        """
        self._revision = revision

    @property
    def extend(self):
        r"""Gets the extend of this RefEntryDto.

        **参数解释：** 其他信息。 **约束限制：** 不涉及。    

        :return: The extend of this RefEntryDto.
        :rtype: str
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        r"""Sets the extend of this RefEntryDto.

        **参数解释：** 其他信息。 **约束限制：** 不涉及。    

        :param extend: The extend of this RefEntryDto.
        :type extend: str
        """
        self._extend = extend

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
        if not isinstance(other, RefEntryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
