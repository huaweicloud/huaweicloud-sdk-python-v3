# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LTSStructTemplateInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'demo_fields': 'list[StructFieldInfo]',
        'content': 'str',
        'log_group_id': 'str',
        'parse_type': 'str',
        'log_stream_id': 'str',
        'project_id': 'str',
        'regex_rules': 'str',
        'layers': 'int',
        'tokenizer': 'str',
        'log_format': 'str'
    }

    attribute_map = {
        'demo_fields': 'demo_fields',
        'content': 'content',
        'log_group_id': 'log_group_id',
        'parse_type': 'parse_type',
        'log_stream_id': 'log_stream_id',
        'project_id': 'project_id',
        'regex_rules': 'regex_rules',
        'layers': 'layers',
        'tokenizer': 'tokenizer',
        'log_format': 'log_format'
    }

    def __init__(self, demo_fields=None, content=None, log_group_id=None, parse_type=None, log_stream_id=None, project_id=None, regex_rules=None, layers=None, tokenizer=None, log_format=None):
        """LTSStructTemplateInfo - a model defined in huaweicloud sdk"""
        
        

        self._demo_fields = None
        self._content = None
        self._log_group_id = None
        self._parse_type = None
        self._log_stream_id = None
        self._project_id = None
        self._regex_rules = None
        self._layers = None
        self._tokenizer = None
        self._log_format = None
        self.discriminator = None

        self.demo_fields = demo_fields
        self.content = content
        self.log_group_id = log_group_id
        self.parse_type = parse_type
        self.log_stream_id = log_stream_id
        self.project_id = project_id
        if regex_rules is not None:
            self.regex_rules = regex_rules
        if layers is not None:
            self.layers = layers
        if tokenizer is not None:
            self.tokenizer = tokenizer
        if log_format is not None:
            self.log_format = log_format

    @property
    def demo_fields(self):
        """Gets the demo_fields of this LTSStructTemplateInfo.

        结构化字段

        :return: The demo_fields of this LTSStructTemplateInfo.
        :rtype: list[StructFieldInfo]
        """
        return self._demo_fields

    @demo_fields.setter
    def demo_fields(self, demo_fields):
        """Sets the demo_fields of this LTSStructTemplateInfo.

        结构化字段

        :param demo_fields: The demo_fields of this LTSStructTemplateInfo.
        :type: list[StructFieldInfo]
        """
        self._demo_fields = demo_fields

    @property
    def content(self):
        """Gets the content of this LTSStructTemplateInfo.

        示例日志

        :return: The content of this LTSStructTemplateInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this LTSStructTemplateInfo.

        示例日志

        :param content: The content of this LTSStructTemplateInfo.
        :type: str
        """
        self._content = content

    @property
    def log_group_id(self):
        """Gets the log_group_id of this LTSStructTemplateInfo.

        日志组ID

        :return: The log_group_id of this LTSStructTemplateInfo.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this LTSStructTemplateInfo.

        日志组ID

        :param log_group_id: The log_group_id of this LTSStructTemplateInfo.
        :type: str
        """
        self._log_group_id = log_group_id

    @property
    def parse_type(self):
        """Gets the parse_type of this LTSStructTemplateInfo.

        结构化方式

        :return: The parse_type of this LTSStructTemplateInfo.
        :rtype: str
        """
        return self._parse_type

    @parse_type.setter
    def parse_type(self, parse_type):
        """Sets the parse_type of this LTSStructTemplateInfo.

        结构化方式

        :param parse_type: The parse_type of this LTSStructTemplateInfo.
        :type: str
        """
        self._parse_type = parse_type

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this LTSStructTemplateInfo.

        日志流ID

        :return: The log_stream_id of this LTSStructTemplateInfo.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this LTSStructTemplateInfo.

        日志流ID

        :param log_stream_id: The log_stream_id of this LTSStructTemplateInfo.
        :type: str
        """
        self._log_stream_id = log_stream_id

    @property
    def project_id(self):
        """Gets the project_id of this LTSStructTemplateInfo.

        项目ID

        :return: The project_id of this LTSStructTemplateInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this LTSStructTemplateInfo.

        项目ID

        :param project_id: The project_id of this LTSStructTemplateInfo.
        :type: str
        """
        self._project_id = project_id

    @property
    def regex_rules(self):
        """Gets the regex_rules of this LTSStructTemplateInfo.

        parse_type为custom_regex类型时必填，regex提取规则

        :return: The regex_rules of this LTSStructTemplateInfo.
        :rtype: str
        """
        return self._regex_rules

    @regex_rules.setter
    def regex_rules(self, regex_rules):
        """Sets the regex_rules of this LTSStructTemplateInfo.

        parse_type为custom_regex类型时必填，regex提取规则

        :param regex_rules: The regex_rules of this LTSStructTemplateInfo.
        :type: str
        """
        self._regex_rules = regex_rules

    @property
    def layers(self):
        """Gets the layers of this LTSStructTemplateInfo.

        parse_type为json类型时必填，解析层数，目前固定是3

        :return: The layers of this LTSStructTemplateInfo.
        :rtype: int
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this LTSStructTemplateInfo.

        parse_type为json类型时必填，解析层数，目前固定是3

        :param layers: The layers of this LTSStructTemplateInfo.
        :type: int
        """
        self._layers = layers

    @property
    def tokenizer(self):
        """Gets the tokenizer of this LTSStructTemplateInfo.

        parse_type为split类型时必填，分隔符，分词符号

        :return: The tokenizer of this LTSStructTemplateInfo.
        :rtype: str
        """
        return self._tokenizer

    @tokenizer.setter
    def tokenizer(self, tokenizer):
        """Sets the tokenizer of this LTSStructTemplateInfo.

        parse_type为split类型时必填，分隔符，分词符号

        :param tokenizer: The tokenizer of this LTSStructTemplateInfo.
        :type: str
        """
        self._tokenizer = tokenizer

    @property
    def log_format(self):
        """Gets the log_format of this LTSStructTemplateInfo.

        parse_type为nginx类型时必填，nginx日志格式模板

        :return: The log_format of this LTSStructTemplateInfo.
        :rtype: str
        """
        return self._log_format

    @log_format.setter
    def log_format(self, log_format):
        """Sets the log_format of this LTSStructTemplateInfo.

        parse_type为nginx类型时必填，nginx日志格式模板

        :param log_format: The log_format of this LTSStructTemplateInfo.
        :type: str
        """
        self._log_format = log_format

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
        if not isinstance(other, LTSStructTemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
