# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAgencyReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency_name': 'str',
        'path': 'str',
        'trust_policy': 'str',
        'max_session_duration': 'int',
        'description': 'str'
    }

    attribute_map = {
        'agency_name': 'agency_name',
        'path': 'path',
        'trust_policy': 'trust_policy',
        'max_session_duration': 'max_session_duration',
        'description': 'description'
    }

    def __init__(self, agency_name=None, path=None, trust_policy=None, max_session_duration=None, description=None):
        r"""CreateAgencyReqBody

        The model defined in huaweicloud sdk

        :param agency_name: 信任委托名称，长度为1到64个字符，只包含字母、数字、\&quot;_\&quot;、\&quot;+\&quot;、\&quot;&#x3D;\&quot;、\&quot;,\&quot;、\&quot;.\&quot;、\&quot;@\&quot;和\&quot;-\&quot;的字符串。
        :type agency_name: str
        :param path: 资源路径，默认为空串。由若干段字符串拼接而成，每段先包含一个或多个字母、数字、\&quot;.\&quot;、\&quot;,\&quot;、\&quot;+\&quot;、\&quot;@\&quot;、\&quot;&#x3D;\&quot;、\&quot;_\&quot;或\&quot;-\&quot;，并以\&quot;/\&quot;结尾，例如\&quot;foo/bar/\&quot;。
        :type path: str
        :param trust_policy: 信任委托信任策略的策略文档的json格式。下面的字符&#x60;&#x3D; &lt; &gt; ( ) |&#x60;是语法中的特殊字符，不包含在信任策略中。  问号&#x60;?&#x60;表示元素是可选的。例如&#x60;sid_block?&#x60;。  竖线&#x60;|&#x60;表示可选项，括号定义了可选项的范围。例如&#x60;(\&quot;Allow\&quot; | \&quot;Deny\&quot;)&#x60;。  当一个元素允许多个值时，使用重复值&#x60;,&#x60;以及&#x60;...&#x60;表示。例如&#x60;[ &lt;policy_statement&gt;, &lt;policy_statement&gt;, ... ]&#x60;。  下面的递归文法描述了信任策略的语法： &#x60;&#x60;&#x60; policy &#x3D; {   &lt;version_block&gt;,   &lt;statement_block&gt; }  &lt;version_block&gt; &#x3D; \&quot;Version\&quot; : (\&quot;5.0\&quot;)  &lt;statement_block&gt; &#x3D; \&quot;Statement\&quot; : [ &lt;policy_statement&gt;, &lt;policy_statement&gt;, ... ]  &lt;policy_statement&gt; &#x3D; {   &lt;sid_block?&gt;,   &lt;principal_block&gt;,   &lt;effect_block&gt;,   &lt;action_block&gt;,   &lt;resource_block?&gt;,   &lt;condition_block?&gt; }  &lt;sid_block&gt; &#x3D; \&quot;Sid\&quot; : &lt;sid_string&gt;  &lt;principal_block&gt; &#x3D; (\&quot;Principal\&quot; | \&quot;NotPrincipal\&quot;) : &lt;principal_map&gt;  &lt;principal_map&gt; &#x3D; { &lt;principal_map_entry&gt;, &lt;principal_map_entry&gt;, ... }  &lt;principal_map_entry&gt; &#x3D; (\&quot;IAM\&quot; | \&quot;Service\&quot;) : [ &lt;principal_id_string&gt;, ... | &lt;service_principal_string&gt;, ... ]  &lt;effect_block&gt; &#x3D; \&quot;Effect\&quot; : (\&quot;Allow\&quot; | \&quot;Deny\&quot;)  &lt;action_block&gt; &#x3D; (\&quot;Action\&quot; | \&quot;NotAction\&quot;) : [ &lt;action_string&gt;, &lt;action_string&gt;, ... ]  &lt;resource_block&gt; &#x3D; (\&quot;Resource\&quot; | \&quot;NotResource\&quot;) : [ &lt;resource_string&gt;, &lt;resource_string&gt;, ... ]  &lt;condition_block&gt; &#x3D; \&quot;Condition\&quot; : { &lt;condition_map&gt; }  &lt;condition_map&gt; &#x3D; {   &lt;condition_type_string&gt; : { &lt;condition_key_string&gt; : &lt;condition_value_list&gt; },   &lt;condition_type_string&gt; : { &lt;condition_key_string&gt; : &lt;condition_value_list&gt; },   ... }  &lt;condition_value_list&gt; &#x3D; ( &lt;condition_value&gt; | [ &lt;condition_value&gt;, &lt;condition_value&gt;, ... ] )  &lt;condition_value&gt; &#x3D; \&quot;string\&quot; &#x60;&#x60;&#x60; 
        :type trust_policy: str
        :param max_session_duration: 信任委托最大会话时长，默认为3600秒，取值范围为[3600,43200]。
        :type max_session_duration: int
        :param description: 信任委托描述信息，默认为空串，字符串最大长度为1000。
        :type description: str
        """
        
        

        self._agency_name = None
        self._path = None
        self._trust_policy = None
        self._max_session_duration = None
        self._description = None
        self.discriminator = None

        self.agency_name = agency_name
        if path is not None:
            self.path = path
        self.trust_policy = trust_policy
        if max_session_duration is not None:
            self.max_session_duration = max_session_duration
        if description is not None:
            self.description = description

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CreateAgencyReqBody.

        信任委托名称，长度为1到64个字符，只包含字母、数字、\"_\"、\"+\"、\"=\"、\",\"、\".\"、\"@\"和\"-\"的字符串。

        :return: The agency_name of this CreateAgencyReqBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CreateAgencyReqBody.

        信任委托名称，长度为1到64个字符，只包含字母、数字、\"_\"、\"+\"、\"=\"、\",\"、\".\"、\"@\"和\"-\"的字符串。

        :param agency_name: The agency_name of this CreateAgencyReqBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def path(self):
        r"""Gets the path of this CreateAgencyReqBody.

        资源路径，默认为空串。由若干段字符串拼接而成，每段先包含一个或多个字母、数字、\".\"、\",\"、\"+\"、\"@\"、\"=\"、\"_\"或\"-\"，并以\"/\"结尾，例如\"foo/bar/\"。

        :return: The path of this CreateAgencyReqBody.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this CreateAgencyReqBody.

        资源路径，默认为空串。由若干段字符串拼接而成，每段先包含一个或多个字母、数字、\".\"、\",\"、\"+\"、\"@\"、\"=\"、\"_\"或\"-\"，并以\"/\"结尾，例如\"foo/bar/\"。

        :param path: The path of this CreateAgencyReqBody.
        :type path: str
        """
        self._path = path

    @property
    def trust_policy(self):
        r"""Gets the trust_policy of this CreateAgencyReqBody.

        信任委托信任策略的策略文档的json格式。下面的字符`= < > ( ) |`是语法中的特殊字符，不包含在信任策略中。  问号`?`表示元素是可选的。例如`sid_block?`。  竖线`|`表示可选项，括号定义了可选项的范围。例如`(\"Allow\" | \"Deny\")`。  当一个元素允许多个值时，使用重复值`,`以及`...`表示。例如`[ <policy_statement>, <policy_statement>, ... ]`。  下面的递归文法描述了信任策略的语法： ``` policy = {   <version_block>,   <statement_block> }  <version_block> = \"Version\" : (\"5.0\")  <statement_block> = \"Statement\" : [ <policy_statement>, <policy_statement>, ... ]  <policy_statement> = {   <sid_block?>,   <principal_block>,   <effect_block>,   <action_block>,   <resource_block?>,   <condition_block?> }  <sid_block> = \"Sid\" : <sid_string>  <principal_block> = (\"Principal\" | \"NotPrincipal\") : <principal_map>  <principal_map> = { <principal_map_entry>, <principal_map_entry>, ... }  <principal_map_entry> = (\"IAM\" | \"Service\") : [ <principal_id_string>, ... | <service_principal_string>, ... ]  <effect_block> = \"Effect\" : (\"Allow\" | \"Deny\")  <action_block> = (\"Action\" | \"NotAction\") : [ <action_string>, <action_string>, ... ]  <resource_block> = (\"Resource\" | \"NotResource\") : [ <resource_string>, <resource_string>, ... ]  <condition_block> = \"Condition\" : { <condition_map> }  <condition_map> = {   <condition_type_string> : { <condition_key_string> : <condition_value_list> },   <condition_type_string> : { <condition_key_string> : <condition_value_list> },   ... }  <condition_value_list> = ( <condition_value> | [ <condition_value>, <condition_value>, ... ] )  <condition_value> = \"string\" ``` 

        :return: The trust_policy of this CreateAgencyReqBody.
        :rtype: str
        """
        return self._trust_policy

    @trust_policy.setter
    def trust_policy(self, trust_policy):
        r"""Sets the trust_policy of this CreateAgencyReqBody.

        信任委托信任策略的策略文档的json格式。下面的字符`= < > ( ) |`是语法中的特殊字符，不包含在信任策略中。  问号`?`表示元素是可选的。例如`sid_block?`。  竖线`|`表示可选项，括号定义了可选项的范围。例如`(\"Allow\" | \"Deny\")`。  当一个元素允许多个值时，使用重复值`,`以及`...`表示。例如`[ <policy_statement>, <policy_statement>, ... ]`。  下面的递归文法描述了信任策略的语法： ``` policy = {   <version_block>,   <statement_block> }  <version_block> = \"Version\" : (\"5.0\")  <statement_block> = \"Statement\" : [ <policy_statement>, <policy_statement>, ... ]  <policy_statement> = {   <sid_block?>,   <principal_block>,   <effect_block>,   <action_block>,   <resource_block?>,   <condition_block?> }  <sid_block> = \"Sid\" : <sid_string>  <principal_block> = (\"Principal\" | \"NotPrincipal\") : <principal_map>  <principal_map> = { <principal_map_entry>, <principal_map_entry>, ... }  <principal_map_entry> = (\"IAM\" | \"Service\") : [ <principal_id_string>, ... | <service_principal_string>, ... ]  <effect_block> = \"Effect\" : (\"Allow\" | \"Deny\")  <action_block> = (\"Action\" | \"NotAction\") : [ <action_string>, <action_string>, ... ]  <resource_block> = (\"Resource\" | \"NotResource\") : [ <resource_string>, <resource_string>, ... ]  <condition_block> = \"Condition\" : { <condition_map> }  <condition_map> = {   <condition_type_string> : { <condition_key_string> : <condition_value_list> },   <condition_type_string> : { <condition_key_string> : <condition_value_list> },   ... }  <condition_value_list> = ( <condition_value> | [ <condition_value>, <condition_value>, ... ] )  <condition_value> = \"string\" ``` 

        :param trust_policy: The trust_policy of this CreateAgencyReqBody.
        :type trust_policy: str
        """
        self._trust_policy = trust_policy

    @property
    def max_session_duration(self):
        r"""Gets the max_session_duration of this CreateAgencyReqBody.

        信任委托最大会话时长，默认为3600秒，取值范围为[3600,43200]。

        :return: The max_session_duration of this CreateAgencyReqBody.
        :rtype: int
        """
        return self._max_session_duration

    @max_session_duration.setter
    def max_session_duration(self, max_session_duration):
        r"""Sets the max_session_duration of this CreateAgencyReqBody.

        信任委托最大会话时长，默认为3600秒，取值范围为[3600,43200]。

        :param max_session_duration: The max_session_duration of this CreateAgencyReqBody.
        :type max_session_duration: int
        """
        self._max_session_duration = max_session_duration

    @property
    def description(self):
        r"""Gets the description of this CreateAgencyReqBody.

        信任委托描述信息，默认为空串，字符串最大长度为1000。

        :return: The description of this CreateAgencyReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAgencyReqBody.

        信任委托描述信息，默认为空串，字符串最大长度为1000。

        :param description: The description of this CreateAgencyReqBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateAgencyReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
