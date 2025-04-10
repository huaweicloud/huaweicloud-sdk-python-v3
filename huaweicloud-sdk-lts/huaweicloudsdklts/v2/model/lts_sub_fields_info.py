# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LTSSubFieldsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_type': 'str',
        'field_name': 'str',
        'case_sensitive': 'bool',
        'include_chinese': 'bool',
        'tokenizer': 'str',
        'quick_analysis': 'bool',
        'ascii': 'list[str]'
    }

    attribute_map = {
        'field_type': 'fieldType',
        'field_name': 'fieldName',
        'case_sensitive': 'caseSensitive',
        'include_chinese': 'includeChinese',
        'tokenizer': 'tokenizer',
        'quick_analysis': 'quickAnalysis',
        'ascii': 'ascii'
    }

    def __init__(self, field_type=None, field_name=None, case_sensitive=None, include_chinese=None, tokenizer=None, quick_analysis=None, ascii=None):
        r"""LTSSubFieldsInfo

        The model defined in huaweicloud sdk

        :param field_type: 字段类型
        :type field_type: str
        :param field_name: 字段名称
        :type field_name: str
        :param case_sensitive: 是否大小写敏感
        :type case_sensitive: bool
        :param include_chinese: 是否包含中文
        :type include_chinese: bool
        :param tokenizer: 分词符
        :type tokenizer: str
        :param quick_analysis: 是否快速分析
        :type quick_analysis: bool
        :param ascii: 特殊分词符
        :type ascii: list[str]
        """
        
        

        self._field_type = None
        self._field_name = None
        self._case_sensitive = None
        self._include_chinese = None
        self._tokenizer = None
        self._quick_analysis = None
        self._ascii = None
        self.discriminator = None

        self.field_type = field_type
        self.field_name = field_name
        if case_sensitive is not None:
            self.case_sensitive = case_sensitive
        if include_chinese is not None:
            self.include_chinese = include_chinese
        if tokenizer is not None:
            self.tokenizer = tokenizer
        if quick_analysis is not None:
            self.quick_analysis = quick_analysis
        if ascii is not None:
            self.ascii = ascii

    @property
    def field_type(self):
        r"""Gets the field_type of this LTSSubFieldsInfo.

        字段类型

        :return: The field_type of this LTSSubFieldsInfo.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        r"""Sets the field_type of this LTSSubFieldsInfo.

        字段类型

        :param field_type: The field_type of this LTSSubFieldsInfo.
        :type field_type: str
        """
        self._field_type = field_type

    @property
    def field_name(self):
        r"""Gets the field_name of this LTSSubFieldsInfo.

        字段名称

        :return: The field_name of this LTSSubFieldsInfo.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this LTSSubFieldsInfo.

        字段名称

        :param field_name: The field_name of this LTSSubFieldsInfo.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def case_sensitive(self):
        r"""Gets the case_sensitive of this LTSSubFieldsInfo.

        是否大小写敏感

        :return: The case_sensitive of this LTSSubFieldsInfo.
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        r"""Sets the case_sensitive of this LTSSubFieldsInfo.

        是否大小写敏感

        :param case_sensitive: The case_sensitive of this LTSSubFieldsInfo.
        :type case_sensitive: bool
        """
        self._case_sensitive = case_sensitive

    @property
    def include_chinese(self):
        r"""Gets the include_chinese of this LTSSubFieldsInfo.

        是否包含中文

        :return: The include_chinese of this LTSSubFieldsInfo.
        :rtype: bool
        """
        return self._include_chinese

    @include_chinese.setter
    def include_chinese(self, include_chinese):
        r"""Sets the include_chinese of this LTSSubFieldsInfo.

        是否包含中文

        :param include_chinese: The include_chinese of this LTSSubFieldsInfo.
        :type include_chinese: bool
        """
        self._include_chinese = include_chinese

    @property
    def tokenizer(self):
        r"""Gets the tokenizer of this LTSSubFieldsInfo.

        分词符

        :return: The tokenizer of this LTSSubFieldsInfo.
        :rtype: str
        """
        return self._tokenizer

    @tokenizer.setter
    def tokenizer(self, tokenizer):
        r"""Sets the tokenizer of this LTSSubFieldsInfo.

        分词符

        :param tokenizer: The tokenizer of this LTSSubFieldsInfo.
        :type tokenizer: str
        """
        self._tokenizer = tokenizer

    @property
    def quick_analysis(self):
        r"""Gets the quick_analysis of this LTSSubFieldsInfo.

        是否快速分析

        :return: The quick_analysis of this LTSSubFieldsInfo.
        :rtype: bool
        """
        return self._quick_analysis

    @quick_analysis.setter
    def quick_analysis(self, quick_analysis):
        r"""Sets the quick_analysis of this LTSSubFieldsInfo.

        是否快速分析

        :param quick_analysis: The quick_analysis of this LTSSubFieldsInfo.
        :type quick_analysis: bool
        """
        self._quick_analysis = quick_analysis

    @property
    def ascii(self):
        r"""Gets the ascii of this LTSSubFieldsInfo.

        特殊分词符

        :return: The ascii of this LTSSubFieldsInfo.
        :rtype: list[str]
        """
        return self._ascii

    @ascii.setter
    def ascii(self, ascii):
        r"""Sets the ascii of this LTSSubFieldsInfo.

        特殊分词符

        :param ascii: The ascii of this LTSSubFieldsInfo.
        :type ascii: list[str]
        """
        self._ascii = ascii

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
        if not isinstance(other, LTSSubFieldsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
