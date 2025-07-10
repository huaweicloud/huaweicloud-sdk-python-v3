# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Criteria:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'match_target_type': 'str',
        'match_target_name': 'str',
        'match_type': 'str',
        'match_pattern': 'list[str]',
        'negate': 'bool',
        'case_sensitive': 'bool',
        'logic': 'str',
        'sub_criteria': 'list[Criteria]'
    }

    attribute_map = {
        'match_target_type': 'match_target_type',
        'match_target_name': 'match_target_name',
        'match_type': 'match_type',
        'match_pattern': 'match_pattern',
        'negate': 'negate',
        'case_sensitive': 'case_sensitive',
        'logic': 'logic',
        'sub_criteria': 'sub_criteria'
    }

    def __init__(self, match_target_type=None, match_target_name=None, match_type=None, match_pattern=None, negate=None, case_sensitive=None, logic=None, sub_criteria=None):
        r"""Criteria

        The model defined in huaweicloud sdk

        :param match_target_type: **参数解释：** 匹配目标类型 **约束限制：** 不涉及 **取值范围：** - schema: 客户端请求使用的协议类型 - method: 客户端请求IP使用的请求方法 - path: 客户端请求URL路径 - arg: 客户端请求URL中的查询参数 - extension: 客户端请求IP内容的文件后缀 - filename: 客户端请求IP内容的文件名称 - header: HTTP请求头部 - clientip: 客户端请求IP的客户端IP - clientip_version: 客户端请求IP的客户端IP版本 - ua: 客户端请求IP头中的User-Agent - ngx_variable: Nginx变量 **默认取值：** 不涉及
        :type match_target_type: str
        :param match_target_name: **参数解释：** 匹配目标名称 **约束限制：** 不涉及 **取值范围：** - 当匹配目标类型为schema、method、path、extension、filename、ua时，该值为空 - 当匹配目标类型为arg时表示查询参数名，长度1-100，由数字，大小写字母，中划线和下划线组成，只能以字母开头 - 当匹配目标类型为header时表示请求头的名称，长度1-100，由数字，大小写字母，中划线和下划线组成，只能以字母开头 - 当匹配目标类型为clientip时表示ip来源，取值：connect：建联IP；xff：x-forwarded-for头 - 当匹配目标类型为clientip_version时表示ip版本来源，取值：connect：建联IP；xff：x-forwarded-for头 - 当匹配目标类型为ngx_variable时表示Nginx变量名，仅支持$protocol、$arg_、$http_、$scheme、$uri、$ssl_protocol、$ssl_server_name、$remote_addr、$http2、$request_method、$sent_http_ **默认取值：** 不涉及
        :type match_target_name: str
        :param match_type: **参数解释：** 匹配算法 **约束限制：** 不涉及 **取值范围：** contains：包含匹配，匹配到match_pattern任意一个条件即匹配成功 **默认取值：** 不涉及
        :type match_type: str
        :param match_pattern: **参数解释：** 匹配内容 **约束限制：** 不涉及 **取值范围：** - 当匹配目标类型为schema时，取值：HTTP，HTTPS - 当匹配目标类型为method时，取值：GET，PUT，POST，DELETE，HEAD，OPTIONS，PATCH，TRACE，CONNECT - 当匹配目标类型为clientip_version时，取值：IPv4，IPv6 - 当匹配目标类型为path和ua时，支持配置通配符“*” **默认取值：** 不涉及
        :type match_pattern: list[str]
        :param negate: **参数解释：** 是否取反，与match_type配合使用。例：negate配置为true，match_type配置为contains，则实际业务逻辑将转换为not_contains **约束限制：** 不涉及 **取值范围：** - true: 取反 - false: 不取反 **默认取值：** false: 不取反
        :type negate: bool
        :param case_sensitive: **参数解释：** 是否区分大小写 **约束限制：** 不涉及 **取值范围：** - true: 区分大小写 - false: 不区分大小写 **默认取值：** false: 不区分大小写
        :type case_sensitive: bool
        :param logic: **参数解释：** 嵌套条件逻辑运算符 **约束限制：** 不涉及 **取值范围：** - and: 与关系 - or: 或关系 **默认取值：** 不涉及
        :type logic: str
        :param sub_criteria: **参数解释：** 嵌套条件列表 **约束限制：** 不涉及
        :type sub_criteria: list[:class:`huaweicloudsdkcdn.v2.Criteria`]
        """
        
        

        self._match_target_type = None
        self._match_target_name = None
        self._match_type = None
        self._match_pattern = None
        self._negate = None
        self._case_sensitive = None
        self._logic = None
        self._sub_criteria = None
        self.discriminator = None

        if match_target_type is not None:
            self.match_target_type = match_target_type
        if match_target_name is not None:
            self.match_target_name = match_target_name
        if match_type is not None:
            self.match_type = match_type
        if match_pattern is not None:
            self.match_pattern = match_pattern
        if negate is not None:
            self.negate = negate
        if case_sensitive is not None:
            self.case_sensitive = case_sensitive
        if logic is not None:
            self.logic = logic
        if sub_criteria is not None:
            self.sub_criteria = sub_criteria

    @property
    def match_target_type(self):
        r"""Gets the match_target_type of this Criteria.

        **参数解释：** 匹配目标类型 **约束限制：** 不涉及 **取值范围：** - schema: 客户端请求使用的协议类型 - method: 客户端请求IP使用的请求方法 - path: 客户端请求URL路径 - arg: 客户端请求URL中的查询参数 - extension: 客户端请求IP内容的文件后缀 - filename: 客户端请求IP内容的文件名称 - header: HTTP请求头部 - clientip: 客户端请求IP的客户端IP - clientip_version: 客户端请求IP的客户端IP版本 - ua: 客户端请求IP头中的User-Agent - ngx_variable: Nginx变量 **默认取值：** 不涉及

        :return: The match_target_type of this Criteria.
        :rtype: str
        """
        return self._match_target_type

    @match_target_type.setter
    def match_target_type(self, match_target_type):
        r"""Sets the match_target_type of this Criteria.

        **参数解释：** 匹配目标类型 **约束限制：** 不涉及 **取值范围：** - schema: 客户端请求使用的协议类型 - method: 客户端请求IP使用的请求方法 - path: 客户端请求URL路径 - arg: 客户端请求URL中的查询参数 - extension: 客户端请求IP内容的文件后缀 - filename: 客户端请求IP内容的文件名称 - header: HTTP请求头部 - clientip: 客户端请求IP的客户端IP - clientip_version: 客户端请求IP的客户端IP版本 - ua: 客户端请求IP头中的User-Agent - ngx_variable: Nginx变量 **默认取值：** 不涉及

        :param match_target_type: The match_target_type of this Criteria.
        :type match_target_type: str
        """
        self._match_target_type = match_target_type

    @property
    def match_target_name(self):
        r"""Gets the match_target_name of this Criteria.

        **参数解释：** 匹配目标名称 **约束限制：** 不涉及 **取值范围：** - 当匹配目标类型为schema、method、path、extension、filename、ua时，该值为空 - 当匹配目标类型为arg时表示查询参数名，长度1-100，由数字，大小写字母，中划线和下划线组成，只能以字母开头 - 当匹配目标类型为header时表示请求头的名称，长度1-100，由数字，大小写字母，中划线和下划线组成，只能以字母开头 - 当匹配目标类型为clientip时表示ip来源，取值：connect：建联IP；xff：x-forwarded-for头 - 当匹配目标类型为clientip_version时表示ip版本来源，取值：connect：建联IP；xff：x-forwarded-for头 - 当匹配目标类型为ngx_variable时表示Nginx变量名，仅支持$protocol、$arg_、$http_、$scheme、$uri、$ssl_protocol、$ssl_server_name、$remote_addr、$http2、$request_method、$sent_http_ **默认取值：** 不涉及

        :return: The match_target_name of this Criteria.
        :rtype: str
        """
        return self._match_target_name

    @match_target_name.setter
    def match_target_name(self, match_target_name):
        r"""Sets the match_target_name of this Criteria.

        **参数解释：** 匹配目标名称 **约束限制：** 不涉及 **取值范围：** - 当匹配目标类型为schema、method、path、extension、filename、ua时，该值为空 - 当匹配目标类型为arg时表示查询参数名，长度1-100，由数字，大小写字母，中划线和下划线组成，只能以字母开头 - 当匹配目标类型为header时表示请求头的名称，长度1-100，由数字，大小写字母，中划线和下划线组成，只能以字母开头 - 当匹配目标类型为clientip时表示ip来源，取值：connect：建联IP；xff：x-forwarded-for头 - 当匹配目标类型为clientip_version时表示ip版本来源，取值：connect：建联IP；xff：x-forwarded-for头 - 当匹配目标类型为ngx_variable时表示Nginx变量名，仅支持$protocol、$arg_、$http_、$scheme、$uri、$ssl_protocol、$ssl_server_name、$remote_addr、$http2、$request_method、$sent_http_ **默认取值：** 不涉及

        :param match_target_name: The match_target_name of this Criteria.
        :type match_target_name: str
        """
        self._match_target_name = match_target_name

    @property
    def match_type(self):
        r"""Gets the match_type of this Criteria.

        **参数解释：** 匹配算法 **约束限制：** 不涉及 **取值范围：** contains：包含匹配，匹配到match_pattern任意一个条件即匹配成功 **默认取值：** 不涉及

        :return: The match_type of this Criteria.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this Criteria.

        **参数解释：** 匹配算法 **约束限制：** 不涉及 **取值范围：** contains：包含匹配，匹配到match_pattern任意一个条件即匹配成功 **默认取值：** 不涉及

        :param match_type: The match_type of this Criteria.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def match_pattern(self):
        r"""Gets the match_pattern of this Criteria.

        **参数解释：** 匹配内容 **约束限制：** 不涉及 **取值范围：** - 当匹配目标类型为schema时，取值：HTTP，HTTPS - 当匹配目标类型为method时，取值：GET，PUT，POST，DELETE，HEAD，OPTIONS，PATCH，TRACE，CONNECT - 当匹配目标类型为clientip_version时，取值：IPv4，IPv6 - 当匹配目标类型为path和ua时，支持配置通配符“*” **默认取值：** 不涉及

        :return: The match_pattern of this Criteria.
        :rtype: list[str]
        """
        return self._match_pattern

    @match_pattern.setter
    def match_pattern(self, match_pattern):
        r"""Sets the match_pattern of this Criteria.

        **参数解释：** 匹配内容 **约束限制：** 不涉及 **取值范围：** - 当匹配目标类型为schema时，取值：HTTP，HTTPS - 当匹配目标类型为method时，取值：GET，PUT，POST，DELETE，HEAD，OPTIONS，PATCH，TRACE，CONNECT - 当匹配目标类型为clientip_version时，取值：IPv4，IPv6 - 当匹配目标类型为path和ua时，支持配置通配符“*” **默认取值：** 不涉及

        :param match_pattern: The match_pattern of this Criteria.
        :type match_pattern: list[str]
        """
        self._match_pattern = match_pattern

    @property
    def negate(self):
        r"""Gets the negate of this Criteria.

        **参数解释：** 是否取反，与match_type配合使用。例：negate配置为true，match_type配置为contains，则实际业务逻辑将转换为not_contains **约束限制：** 不涉及 **取值范围：** - true: 取反 - false: 不取反 **默认取值：** false: 不取反

        :return: The negate of this Criteria.
        :rtype: bool
        """
        return self._negate

    @negate.setter
    def negate(self, negate):
        r"""Sets the negate of this Criteria.

        **参数解释：** 是否取反，与match_type配合使用。例：negate配置为true，match_type配置为contains，则实际业务逻辑将转换为not_contains **约束限制：** 不涉及 **取值范围：** - true: 取反 - false: 不取反 **默认取值：** false: 不取反

        :param negate: The negate of this Criteria.
        :type negate: bool
        """
        self._negate = negate

    @property
    def case_sensitive(self):
        r"""Gets the case_sensitive of this Criteria.

        **参数解释：** 是否区分大小写 **约束限制：** 不涉及 **取值范围：** - true: 区分大小写 - false: 不区分大小写 **默认取值：** false: 不区分大小写

        :return: The case_sensitive of this Criteria.
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        r"""Sets the case_sensitive of this Criteria.

        **参数解释：** 是否区分大小写 **约束限制：** 不涉及 **取值范围：** - true: 区分大小写 - false: 不区分大小写 **默认取值：** false: 不区分大小写

        :param case_sensitive: The case_sensitive of this Criteria.
        :type case_sensitive: bool
        """
        self._case_sensitive = case_sensitive

    @property
    def logic(self):
        r"""Gets the logic of this Criteria.

        **参数解释：** 嵌套条件逻辑运算符 **约束限制：** 不涉及 **取值范围：** - and: 与关系 - or: 或关系 **默认取值：** 不涉及

        :return: The logic of this Criteria.
        :rtype: str
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        r"""Sets the logic of this Criteria.

        **参数解释：** 嵌套条件逻辑运算符 **约束限制：** 不涉及 **取值范围：** - and: 与关系 - or: 或关系 **默认取值：** 不涉及

        :param logic: The logic of this Criteria.
        :type logic: str
        """
        self._logic = logic

    @property
    def sub_criteria(self):
        r"""Gets the sub_criteria of this Criteria.

        **参数解释：** 嵌套条件列表 **约束限制：** 不涉及

        :return: The sub_criteria of this Criteria.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.Criteria`]
        """
        return self._sub_criteria

    @sub_criteria.setter
    def sub_criteria(self, sub_criteria):
        r"""Sets the sub_criteria of this Criteria.

        **参数解释：** 嵌套条件列表 **约束限制：** 不涉及

        :param sub_criteria: The sub_criteria of this Criteria.
        :type sub_criteria: list[:class:`huaweicloudsdkcdn.v2.Criteria`]
        """
        self._sub_criteria = sub_criteria

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
        if not isinstance(other, Criteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
