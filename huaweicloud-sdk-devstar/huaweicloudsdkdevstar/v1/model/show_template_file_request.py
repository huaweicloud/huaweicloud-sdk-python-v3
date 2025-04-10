# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTemplateFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'template_id': 'str',
        'file_path': 'str',
        'type': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'template_id': 'template_id',
        'file_path': 'file_path',
        'type': 'type'
    }

    def __init__(self, x_language=None, template_id=None, file_path=None, type=None):
        r"""ShowTemplateFileRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言类型，缺省值为“zh-cn”。  枚举值： - zh-cn：中文 - en-us：英文 
        :type x_language: str
        :param template_id: 模板ID，通过查询模板列表接口可获取相应的模板ID。
        :type template_id: str
        :param file_path: 文件相对路径，基于当前根目录的相对文件路径，例如获取HELP.md文件内容，则文件相对路径为“template-resources/file/HELP.md”。
        :type file_path: str
        :param type: 读取文件来源，缺省值为“source-pachage”。  枚举值： - source-package: 源文件压缩包 - introduction: 说明文件 
        :type type: str
        """
        
        

        self._x_language = None
        self._template_id = None
        self._file_path = None
        self._type = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.template_id = template_id
        self.file_path = file_path
        if type is not None:
            self.type = type

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowTemplateFileRequest.

        语言类型，缺省值为“zh-cn”。  枚举值： - zh-cn：中文 - en-us：英文 

        :return: The x_language of this ShowTemplateFileRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowTemplateFileRequest.

        语言类型，缺省值为“zh-cn”。  枚举值： - zh-cn：中文 - en-us：英文 

        :param x_language: The x_language of this ShowTemplateFileRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def template_id(self):
        r"""Gets the template_id of this ShowTemplateFileRequest.

        模板ID，通过查询模板列表接口可获取相应的模板ID。

        :return: The template_id of this ShowTemplateFileRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ShowTemplateFileRequest.

        模板ID，通过查询模板列表接口可获取相应的模板ID。

        :param template_id: The template_id of this ShowTemplateFileRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def file_path(self):
        r"""Gets the file_path of this ShowTemplateFileRequest.

        文件相对路径，基于当前根目录的相对文件路径，例如获取HELP.md文件内容，则文件相对路径为“template-resources/file/HELP.md”。

        :return: The file_path of this ShowTemplateFileRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ShowTemplateFileRequest.

        文件相对路径，基于当前根目录的相对文件路径，例如获取HELP.md文件内容，则文件相对路径为“template-resources/file/HELP.md”。

        :param file_path: The file_path of this ShowTemplateFileRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def type(self):
        r"""Gets the type of this ShowTemplateFileRequest.

        读取文件来源，缺省值为“source-pachage”。  枚举值： - source-package: 源文件压缩包 - introduction: 说明文件 

        :return: The type of this ShowTemplateFileRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowTemplateFileRequest.

        读取文件来源，缺省值为“source-pachage”。  枚举值： - source-package: 源文件压缩包 - introduction: 说明文件 

        :param type: The type of this ShowTemplateFileRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowTemplateFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
