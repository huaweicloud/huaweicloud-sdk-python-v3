# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'param': 'str'
    }

    attribute_map = {
        'type': 'type',
        'param': 'param'
    }

    def __init__(self, type=None, param=None):
        """TemplateRule

        The model defined in huaweicloud sdk

        :param type: 结构化类型，只支持custom_regex,json,split,nginx
        :type type: str
        :param param: 具体结构化规则，每种结构化类型都有自己独有的结构，具体结构如下： 手动正则为json字符串，包含keyObject对象和regex_rules对象，keyObject内为键值对，键为demo_fields数组中元素的index，值为field_name，regex_rules对象为正则表达式字符串，整体例子为{\\\&quot;keyObject\\\&quot;:{\\\&quot;1\\\&quot;:\\\&quot;date\\\&quot;,\\\&quot;2\\\&quot;:\\\&quot;num\\\&quot;},\\\&quot;regex_rules\\\&quot;:\\\&quot;^(?&lt;date&gt;[^/]+)(?:[^ ]* ){8}(?&lt;num&gt;\\\\\\\\d+)\\\&quot;}； json方式时param为一个json字符串，包含keyObject对象和layers对象，keyObject内为键值对，键为demo_fields数组中元素的field_name，值为user_defined_name，layers为最大解析层数，当前最大值为4，整体例子为{\\\&quot;keyObject\\\&quot;:{\\\&quot;metadata.dimention\\\&quot;:\\\&quot;dimention\\\&quot;,\\\&quot;metadata.value\\\&quot;:\\\&quot;\\\&quot;,\\\&quot;metadata.unit\\\&quot;:\\\&quot;\\\&quot;,\\\&quot;collectionTime\\\&quot;:\\\&quot;\\\&quot;},\\\&quot;layers\\\&quot;:3}； 分隔符方式时为json字符串，包含keyObject对象和tokenizer对象，keyObject内为键值对，键为demo_fields数组中元素的index，值为field_name，tokenizer对象为所用分隔符，整体例子为{\\\&quot;keyObject\\\&quot;:{\\\&quot;0\\\&quot;:\\\&quot;field1\\\&quot;,\\\&quot;1\\\&quot;:\\\&quot;field2\\\&quot;,\\\&quot;2\\\&quot;:\\\&quot;field3\\\&quot;,\\\&quot;3\\\&quot;:\\\&quot;field4\\\&quot;,\\\&quot;4\\\&quot;:\\\&quot;field5\\\&quot;,\\\&quot;5\\\&quot;:\\\&quot;field6\\\&quot;,\\\&quot;6\\\&quot;:\\\&quot;field7\\\&quot;,\\\&quot;7\\\&quot;:\\\&quot;field8\\\&quot;,\\\&quot;8\\\&quot;:\\\&quot;field9\\\&quot;},\\\&quot;tokenizer\\\&quot;:\\\&quot; \\\&quot;}； nginx方式时为json字符串，包含keyObject对象，regex对象，field_names对象及log_format对象，keyObject内为键值对，键为demo_fields数组中元素的field_name，值为user_defined_name，regex为正则表达式字符串，field_names对象为demo_fields数组中各元素的field_name的拼接字符串，每个field_name以&#39;,&#39;分隔，log_format对象为nginx日志格式化方式，具体方式参考https://support.huaweicloud.com/usermanual-lts/lts_0820.html#lts_0820__section1151119552549进行配置，整体例子为\&quot;{\\\&quot;keyObject\\\&quot;:{\\\&quot;http_host\\\&quot;:\\\&quot;host\\\&quot;,\\\&quot;remote_addr\\\&quot;:\\\&quot;\\\&quot;,\\\&quot;request_method\\\&quot;:\\\&quot;\\\&quot;,\\\&quot;request_uri\\\&quot;:\\\&quot;\\\&quot;,\\\&quot;time_local\\\&quot;:\\\&quot;\\\&quot;},\\\&quot;regex\\\&quot;:\\\&quot;(\\\\\\\\d+/\\\\\\\\S+/\\\\\\\\d+:\\\\\\\\d+:\\\\\\\\d+:\\\\\\\\d+)\\\\\\\\s+\\\\\\\\S+\\\\\\\\s+(\\\\\\\\S*)\\\\\\\\s+(\\\\\\\\S*)\\\\\\\\s+(\\\\\\\\S*)\\\\\\\\s+\\\\\\\&quot;([^\\\\\\\&quot;]*)\\\\\\\&quot;.*\\\&quot;,\\\&quot;fieldNames\\\&quot;:\\\&quot;time_local,remote_addr,request_method,http_host,request_uri\\\&quot;,\\\&quot;log_format\\\&quot;:\\\&quot;log_format upstreaminfo &#39;$time_local $remote_addr  $request_method $http_host \\\\\\\&quot;$request_uri\\\\\\\&quot;&#39;;\\\&quot;}\&quot;
        :type param: str
        """
        
        

        self._type = None
        self._param = None
        self.discriminator = None

        self.type = type
        self.param = param

    @property
    def type(self):
        """Gets the type of this TemplateRule.

        结构化类型，只支持custom_regex,json,split,nginx

        :return: The type of this TemplateRule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TemplateRule.

        结构化类型，只支持custom_regex,json,split,nginx

        :param type: The type of this TemplateRule.
        :type type: str
        """
        self._type = type

    @property
    def param(self):
        """Gets the param of this TemplateRule.

        具体结构化规则，每种结构化类型都有自己独有的结构，具体结构如下： 手动正则为json字符串，包含keyObject对象和regex_rules对象，keyObject内为键值对，键为demo_fields数组中元素的index，值为field_name，regex_rules对象为正则表达式字符串，整体例子为{\\\"keyObject\\\":{\\\"1\\\":\\\"date\\\",\\\"2\\\":\\\"num\\\"},\\\"regex_rules\\\":\\\"^(?<date>[^/]+)(?:[^ ]* ){8}(?<num>\\\\\\\\d+)\\\"}； json方式时param为一个json字符串，包含keyObject对象和layers对象，keyObject内为键值对，键为demo_fields数组中元素的field_name，值为user_defined_name，layers为最大解析层数，当前最大值为4，整体例子为{\\\"keyObject\\\":{\\\"metadata.dimention\\\":\\\"dimention\\\",\\\"metadata.value\\\":\\\"\\\",\\\"metadata.unit\\\":\\\"\\\",\\\"collectionTime\\\":\\\"\\\"},\\\"layers\\\":3}； 分隔符方式时为json字符串，包含keyObject对象和tokenizer对象，keyObject内为键值对，键为demo_fields数组中元素的index，值为field_name，tokenizer对象为所用分隔符，整体例子为{\\\"keyObject\\\":{\\\"0\\\":\\\"field1\\\",\\\"1\\\":\\\"field2\\\",\\\"2\\\":\\\"field3\\\",\\\"3\\\":\\\"field4\\\",\\\"4\\\":\\\"field5\\\",\\\"5\\\":\\\"field6\\\",\\\"6\\\":\\\"field7\\\",\\\"7\\\":\\\"field8\\\",\\\"8\\\":\\\"field9\\\"},\\\"tokenizer\\\":\\\" \\\"}； nginx方式时为json字符串，包含keyObject对象，regex对象，field_names对象及log_format对象，keyObject内为键值对，键为demo_fields数组中元素的field_name，值为user_defined_name，regex为正则表达式字符串，field_names对象为demo_fields数组中各元素的field_name的拼接字符串，每个field_name以','分隔，log_format对象为nginx日志格式化方式，具体方式参考https://support.huaweicloud.com/usermanual-lts/lts_0820.html#lts_0820__section1151119552549进行配置，整体例子为\"{\\\"keyObject\\\":{\\\"http_host\\\":\\\"host\\\",\\\"remote_addr\\\":\\\"\\\",\\\"request_method\\\":\\\"\\\",\\\"request_uri\\\":\\\"\\\",\\\"time_local\\\":\\\"\\\"},\\\"regex\\\":\\\"(\\\\\\\\d+/\\\\\\\\S+/\\\\\\\\d+:\\\\\\\\d+:\\\\\\\\d+:\\\\\\\\d+)\\\\\\\\s+\\\\\\\\S+\\\\\\\\s+(\\\\\\\\S*)\\\\\\\\s+(\\\\\\\\S*)\\\\\\\\s+(\\\\\\\\S*)\\\\\\\\s+\\\\\\\"([^\\\\\\\"]*)\\\\\\\".*\\\",\\\"fieldNames\\\":\\\"time_local,remote_addr,request_method,http_host,request_uri\\\",\\\"log_format\\\":\\\"log_format upstreaminfo '$time_local $remote_addr  $request_method $http_host \\\\\\\"$request_uri\\\\\\\"';\\\"}\"

        :return: The param of this TemplateRule.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this TemplateRule.

        具体结构化规则，每种结构化类型都有自己独有的结构，具体结构如下： 手动正则为json字符串，包含keyObject对象和regex_rules对象，keyObject内为键值对，键为demo_fields数组中元素的index，值为field_name，regex_rules对象为正则表达式字符串，整体例子为{\\\"keyObject\\\":{\\\"1\\\":\\\"date\\\",\\\"2\\\":\\\"num\\\"},\\\"regex_rules\\\":\\\"^(?<date>[^/]+)(?:[^ ]* ){8}(?<num>\\\\\\\\d+)\\\"}； json方式时param为一个json字符串，包含keyObject对象和layers对象，keyObject内为键值对，键为demo_fields数组中元素的field_name，值为user_defined_name，layers为最大解析层数，当前最大值为4，整体例子为{\\\"keyObject\\\":{\\\"metadata.dimention\\\":\\\"dimention\\\",\\\"metadata.value\\\":\\\"\\\",\\\"metadata.unit\\\":\\\"\\\",\\\"collectionTime\\\":\\\"\\\"},\\\"layers\\\":3}； 分隔符方式时为json字符串，包含keyObject对象和tokenizer对象，keyObject内为键值对，键为demo_fields数组中元素的index，值为field_name，tokenizer对象为所用分隔符，整体例子为{\\\"keyObject\\\":{\\\"0\\\":\\\"field1\\\",\\\"1\\\":\\\"field2\\\",\\\"2\\\":\\\"field3\\\",\\\"3\\\":\\\"field4\\\",\\\"4\\\":\\\"field5\\\",\\\"5\\\":\\\"field6\\\",\\\"6\\\":\\\"field7\\\",\\\"7\\\":\\\"field8\\\",\\\"8\\\":\\\"field9\\\"},\\\"tokenizer\\\":\\\" \\\"}； nginx方式时为json字符串，包含keyObject对象，regex对象，field_names对象及log_format对象，keyObject内为键值对，键为demo_fields数组中元素的field_name，值为user_defined_name，regex为正则表达式字符串，field_names对象为demo_fields数组中各元素的field_name的拼接字符串，每个field_name以','分隔，log_format对象为nginx日志格式化方式，具体方式参考https://support.huaweicloud.com/usermanual-lts/lts_0820.html#lts_0820__section1151119552549进行配置，整体例子为\"{\\\"keyObject\\\":{\\\"http_host\\\":\\\"host\\\",\\\"remote_addr\\\":\\\"\\\",\\\"request_method\\\":\\\"\\\",\\\"request_uri\\\":\\\"\\\",\\\"time_local\\\":\\\"\\\"},\\\"regex\\\":\\\"(\\\\\\\\d+/\\\\\\\\S+/\\\\\\\\d+:\\\\\\\\d+:\\\\\\\\d+:\\\\\\\\d+)\\\\\\\\s+\\\\\\\\S+\\\\\\\\s+(\\\\\\\\S*)\\\\\\\\s+(\\\\\\\\S*)\\\\\\\\s+(\\\\\\\\S*)\\\\\\\\s+\\\\\\\"([^\\\\\\\"]*)\\\\\\\".*\\\",\\\"fieldNames\\\":\\\"time_local,remote_addr,request_method,http_host,request_uri\\\",\\\"log_format\\\":\\\"log_format upstreaminfo '$time_local $remote_addr  $request_method $http_host \\\\\\\"$request_uri\\\\\\\"';\\\"}\"

        :param param: The param of this TemplateRule.
        :type param: str
        """
        self._param = param

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
        if not isinstance(other, TemplateRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
