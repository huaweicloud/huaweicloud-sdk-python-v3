# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MRConflictFileDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'old_path': 'str',
        'new_path': 'str',
        'blob_icon': 'str',
        'blob_path': 'str',
        'conflict_type': 'str',
        'content': 'str',
        'content_path': 'str',
        'sections': 'list[ConflictSectionDto]',
        'type': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'old_path': 'old_path',
        'new_path': 'new_path',
        'blob_icon': 'blob_icon',
        'blob_path': 'blob_path',
        'conflict_type': 'conflict_type',
        'content': 'content',
        'content_path': 'content_path',
        'sections': 'sections',
        'type': 'type',
        'error_message': 'error_message'
    }

    def __init__(self, old_path=None, new_path=None, blob_icon=None, blob_path=None, conflict_type=None, content=None, content_path=None, sections=None, type=None, error_message=None):
        r"""MRConflictFileDto

        The model defined in huaweicloud sdk

        :param old_path: **参数解释：** 旧文件名称。
        :type old_path: str
        :param new_path: **参数解释：** 新文件名称。
        :type new_path: str
        :param blob_icon: blob_icon
        :type blob_icon: str
        :param blob_path: blob 路径
        :type blob_path: str
        :param conflict_type: 冲突类型
        :type conflict_type: str
        :param content: 内容
        :type content: str
        :param content_path: 内容路径
        :type content_path: str
        :param sections: 片段
        :type sections: list[:class:`huaweicloudsdkcodehub.v4.ConflictSectionDto`]
        :param type: 类型
        :type type: str
        :param error_message: 错误信息
        :type error_message: str
        """
        
        

        self._old_path = None
        self._new_path = None
        self._blob_icon = None
        self._blob_path = None
        self._conflict_type = None
        self._content = None
        self._content_path = None
        self._sections = None
        self._type = None
        self._error_message = None
        self.discriminator = None

        if old_path is not None:
            self.old_path = old_path
        if new_path is not None:
            self.new_path = new_path
        if blob_icon is not None:
            self.blob_icon = blob_icon
        if blob_path is not None:
            self.blob_path = blob_path
        if conflict_type is not None:
            self.conflict_type = conflict_type
        if content is not None:
            self.content = content
        if content_path is not None:
            self.content_path = content_path
        if sections is not None:
            self.sections = sections
        if type is not None:
            self.type = type
        if error_message is not None:
            self.error_message = error_message

    @property
    def old_path(self):
        r"""Gets the old_path of this MRConflictFileDto.

        **参数解释：** 旧文件名称。

        :return: The old_path of this MRConflictFileDto.
        :rtype: str
        """
        return self._old_path

    @old_path.setter
    def old_path(self, old_path):
        r"""Sets the old_path of this MRConflictFileDto.

        **参数解释：** 旧文件名称。

        :param old_path: The old_path of this MRConflictFileDto.
        :type old_path: str
        """
        self._old_path = old_path

    @property
    def new_path(self):
        r"""Gets the new_path of this MRConflictFileDto.

        **参数解释：** 新文件名称。

        :return: The new_path of this MRConflictFileDto.
        :rtype: str
        """
        return self._new_path

    @new_path.setter
    def new_path(self, new_path):
        r"""Sets the new_path of this MRConflictFileDto.

        **参数解释：** 新文件名称。

        :param new_path: The new_path of this MRConflictFileDto.
        :type new_path: str
        """
        self._new_path = new_path

    @property
    def blob_icon(self):
        r"""Gets the blob_icon of this MRConflictFileDto.

        blob_icon

        :return: The blob_icon of this MRConflictFileDto.
        :rtype: str
        """
        return self._blob_icon

    @blob_icon.setter
    def blob_icon(self, blob_icon):
        r"""Sets the blob_icon of this MRConflictFileDto.

        blob_icon

        :param blob_icon: The blob_icon of this MRConflictFileDto.
        :type blob_icon: str
        """
        self._blob_icon = blob_icon

    @property
    def blob_path(self):
        r"""Gets the blob_path of this MRConflictFileDto.

        blob 路径

        :return: The blob_path of this MRConflictFileDto.
        :rtype: str
        """
        return self._blob_path

    @blob_path.setter
    def blob_path(self, blob_path):
        r"""Sets the blob_path of this MRConflictFileDto.

        blob 路径

        :param blob_path: The blob_path of this MRConflictFileDto.
        :type blob_path: str
        """
        self._blob_path = blob_path

    @property
    def conflict_type(self):
        r"""Gets the conflict_type of this MRConflictFileDto.

        冲突类型

        :return: The conflict_type of this MRConflictFileDto.
        :rtype: str
        """
        return self._conflict_type

    @conflict_type.setter
    def conflict_type(self, conflict_type):
        r"""Sets the conflict_type of this MRConflictFileDto.

        冲突类型

        :param conflict_type: The conflict_type of this MRConflictFileDto.
        :type conflict_type: str
        """
        self._conflict_type = conflict_type

    @property
    def content(self):
        r"""Gets the content of this MRConflictFileDto.

        内容

        :return: The content of this MRConflictFileDto.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this MRConflictFileDto.

        内容

        :param content: The content of this MRConflictFileDto.
        :type content: str
        """
        self._content = content

    @property
    def content_path(self):
        r"""Gets the content_path of this MRConflictFileDto.

        内容路径

        :return: The content_path of this MRConflictFileDto.
        :rtype: str
        """
        return self._content_path

    @content_path.setter
    def content_path(self, content_path):
        r"""Sets the content_path of this MRConflictFileDto.

        内容路径

        :param content_path: The content_path of this MRConflictFileDto.
        :type content_path: str
        """
        self._content_path = content_path

    @property
    def sections(self):
        r"""Gets the sections of this MRConflictFileDto.

        片段

        :return: The sections of this MRConflictFileDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.ConflictSectionDto`]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        r"""Sets the sections of this MRConflictFileDto.

        片段

        :param sections: The sections of this MRConflictFileDto.
        :type sections: list[:class:`huaweicloudsdkcodehub.v4.ConflictSectionDto`]
        """
        self._sections = sections

    @property
    def type(self):
        r"""Gets the type of this MRConflictFileDto.

        类型

        :return: The type of this MRConflictFileDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MRConflictFileDto.

        类型

        :param type: The type of this MRConflictFileDto.
        :type type: str
        """
        self._type = type

    @property
    def error_message(self):
        r"""Gets the error_message of this MRConflictFileDto.

        错误信息

        :return: The error_message of this MRConflictFileDto.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this MRConflictFileDto.

        错误信息

        :param error_message: The error_message of this MRConflictFileDto.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, MRConflictFileDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
