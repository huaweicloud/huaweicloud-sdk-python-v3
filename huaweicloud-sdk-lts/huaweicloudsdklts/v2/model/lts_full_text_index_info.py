# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LTSFullTextIndexInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'case_sensitive': 'bool',
        'include_chinese': 'bool',
        'tokenizer': 'str',
        'ascii': 'list[str]'
    }

    attribute_map = {
        'enable': 'enable',
        'case_sensitive': 'caseSensitive',
        'include_chinese': 'includeChinese',
        'tokenizer': 'tokenizer',
        'ascii': 'ascii'
    }

    def __init__(self, enable=None, case_sensitive=None, include_chinese=None, tokenizer=None, ascii=None):
        """LTSFullTextIndexInfo

        The model defined in huaweicloud sdk

        :param enable: 是否开启全文索引
        :type enable: bool
        :param case_sensitive: 是否大小写敏感
        :type case_sensitive: bool
        :param include_chinese: 是否包含中文
        :type include_chinese: bool
        :param tokenizer: 自定义分词符
        :type tokenizer: str
        :param ascii: 特殊分词符
        :type ascii: list[str]
        """
        
        

        self._enable = None
        self._case_sensitive = None
        self._include_chinese = None
        self._tokenizer = None
        self._ascii = None
        self.discriminator = None

        self.enable = enable
        self.case_sensitive = case_sensitive
        self.include_chinese = include_chinese
        self.tokenizer = tokenizer
        if ascii is not None:
            self.ascii = ascii

    @property
    def enable(self):
        """Gets the enable of this LTSFullTextIndexInfo.

        是否开启全文索引

        :return: The enable of this LTSFullTextIndexInfo.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this LTSFullTextIndexInfo.

        是否开启全文索引

        :param enable: The enable of this LTSFullTextIndexInfo.
        :type enable: bool
        """
        self._enable = enable

    @property
    def case_sensitive(self):
        """Gets the case_sensitive of this LTSFullTextIndexInfo.

        是否大小写敏感

        :return: The case_sensitive of this LTSFullTextIndexInfo.
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        """Sets the case_sensitive of this LTSFullTextIndexInfo.

        是否大小写敏感

        :param case_sensitive: The case_sensitive of this LTSFullTextIndexInfo.
        :type case_sensitive: bool
        """
        self._case_sensitive = case_sensitive

    @property
    def include_chinese(self):
        """Gets the include_chinese of this LTSFullTextIndexInfo.

        是否包含中文

        :return: The include_chinese of this LTSFullTextIndexInfo.
        :rtype: bool
        """
        return self._include_chinese

    @include_chinese.setter
    def include_chinese(self, include_chinese):
        """Sets the include_chinese of this LTSFullTextIndexInfo.

        是否包含中文

        :param include_chinese: The include_chinese of this LTSFullTextIndexInfo.
        :type include_chinese: bool
        """
        self._include_chinese = include_chinese

    @property
    def tokenizer(self):
        """Gets the tokenizer of this LTSFullTextIndexInfo.

        自定义分词符

        :return: The tokenizer of this LTSFullTextIndexInfo.
        :rtype: str
        """
        return self._tokenizer

    @tokenizer.setter
    def tokenizer(self, tokenizer):
        """Sets the tokenizer of this LTSFullTextIndexInfo.

        自定义分词符

        :param tokenizer: The tokenizer of this LTSFullTextIndexInfo.
        :type tokenizer: str
        """
        self._tokenizer = tokenizer

    @property
    def ascii(self):
        """Gets the ascii of this LTSFullTextIndexInfo.

        特殊分词符

        :return: The ascii of this LTSFullTextIndexInfo.
        :rtype: list[str]
        """
        return self._ascii

    @ascii.setter
    def ascii(self, ascii):
        """Sets the ascii of this LTSFullTextIndexInfo.

        特殊分词符

        :param ascii: The ascii of this LTSFullTextIndexInfo.
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
        if not isinstance(other, LTSFullTextIndexInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
