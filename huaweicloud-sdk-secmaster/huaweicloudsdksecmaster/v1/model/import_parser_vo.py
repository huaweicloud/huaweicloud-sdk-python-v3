# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportParserVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'parser_title': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'file_name': 'file_name',
        'parser_title': 'parser_title',
        'success': 'success'
    }

    def __init__(self, file_name=None, parser_title=None, success=None):
        r"""ImportParserVo

        The model defined in huaweicloud sdk

        :param file_name: 解析器文件名称
        :type file_name: str
        :param parser_title: 解析器名称
        :type parser_title: str
        :param success: 是否导入成功
        :type success: bool
        """
        
        

        self._file_name = None
        self._parser_title = None
        self._success = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if parser_title is not None:
            self.parser_title = parser_title
        if success is not None:
            self.success = success

    @property
    def file_name(self):
        r"""Gets the file_name of this ImportParserVo.

        解析器文件名称

        :return: The file_name of this ImportParserVo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ImportParserVo.

        解析器文件名称

        :param file_name: The file_name of this ImportParserVo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def parser_title(self):
        r"""Gets the parser_title of this ImportParserVo.

        解析器名称

        :return: The parser_title of this ImportParserVo.
        :rtype: str
        """
        return self._parser_title

    @parser_title.setter
    def parser_title(self, parser_title):
        r"""Sets the parser_title of this ImportParserVo.

        解析器名称

        :param parser_title: The parser_title of this ImportParserVo.
        :type parser_title: str
        """
        self._parser_title = parser_title

    @property
    def success(self):
        r"""Gets the success of this ImportParserVo.

        是否导入成功

        :return: The success of this ImportParserVo.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ImportParserVo.

        是否导入成功

        :param success: The success of this ImportParserVo.
        :type success: bool
        """
        self._success = success

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
        if not isinstance(other, ImportParserVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
