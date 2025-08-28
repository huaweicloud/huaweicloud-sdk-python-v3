# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePolicyVersionReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_document': 'str',
        'set_as_default': 'bool'
    }

    attribute_map = {
        'policy_document': 'policy_document',
        'set_as_default': 'set_as_default'
    }

    def __init__(self, policy_document=None, set_as_default=None):
        r"""CreatePolicyVersionReqBody

        The model defined in huaweicloud sdk

        :param policy_document: 自定义身份策略或系统预置身份策略的策略文档的json格式。下面的字符&#x60;&#x3D; &lt; &gt; ( ) |&#x60;是语法中的特殊字符，不包含在身份策略中。  问号&#x60;?&#x60;表示元素是可选的。例如&#x60;sid_block?&#x60;。  竖线&#x60;|&#x60;表示可选项，括号定义了可选项的范围。例如&#x60;(\&quot;Allow\&quot; | \&quot;Deny\&quot;)&#x60;。  当一个元素允许多个值时，使用重复值&#x60;,&#x60;以及&#x60;...&#x60;表示。例如&#x60;[ &lt;policy_statement&gt;, &lt;policy_statement&gt;, ... ]&#x60;。  下面的递归文法描述了身份策略的语法： &#x60;&#x60;&#x60; policy &#x3D; {   &lt;version_block&gt;,   &lt;statement_block&gt; }  &lt;version_block&gt; &#x3D; \&quot;Version\&quot; : (\&quot;5.0\&quot;)  &lt;statement_block&gt; &#x3D; \&quot;Statement\&quot; : [ &lt;policy_statement&gt;, &lt;policy_statement&gt;, ... ]  &lt;policy_statement&gt; &#x3D; {   &lt;sid_block?&gt;,   &lt;effect_block&gt;,   &lt;action_block&gt;,   &lt;resource_block?&gt;,   &lt;condition_block?&gt; }  &lt;sid_block&gt; &#x3D; \&quot;Sid\&quot; : &lt;sid_string&gt;  &lt;effect_block&gt; &#x3D; \&quot;Effect\&quot; : (\&quot;Allow\&quot; | \&quot;Deny\&quot;)  &lt;action_block&gt; &#x3D; (\&quot;Action\&quot; | \&quot;NotAction\&quot;) : [ &lt;action_string&gt;, &lt;action_string&gt;, ... ]  &lt;resource_block&gt; &#x3D; (\&quot;Resource\&quot; | \&quot;NotResource\&quot;) : [ &lt;resource_string&gt;, &lt;resource_string&gt;, ... ]  &lt;condition_block&gt; &#x3D; \&quot;Condition\&quot; : { &lt;condition_map&gt; }  &lt;condition_map&gt; &#x3D; {   &lt;condition_type_string&gt; : { &lt;condition_key_string&gt; : &lt;condition_value_list&gt; },   &lt;condition_type_string&gt; : { &lt;condition_key_string&gt; : &lt;condition_value_list&gt; },   ... }  &lt;condition_value_list&gt; &#x3D; ( &lt;condition_value&gt; | [ &lt;condition_value&gt;, &lt;condition_value&gt;, ... ] )  &lt;condition_value&gt; &#x3D; \&quot;string\&quot; &#x60;&#x60;&#x60; 
        :type policy_document: str
        :param set_as_default: 是否设置为默认版本。
        :type set_as_default: bool
        """
        
        

        self._policy_document = None
        self._set_as_default = None
        self.discriminator = None

        self.policy_document = policy_document
        if set_as_default is not None:
            self.set_as_default = set_as_default

    @property
    def policy_document(self):
        r"""Gets the policy_document of this CreatePolicyVersionReqBody.

        自定义身份策略或系统预置身份策略的策略文档的json格式。下面的字符`= < > ( ) |`是语法中的特殊字符，不包含在身份策略中。  问号`?`表示元素是可选的。例如`sid_block?`。  竖线`|`表示可选项，括号定义了可选项的范围。例如`(\"Allow\" | \"Deny\")`。  当一个元素允许多个值时，使用重复值`,`以及`...`表示。例如`[ <policy_statement>, <policy_statement>, ... ]`。  下面的递归文法描述了身份策略的语法： ``` policy = {   <version_block>,   <statement_block> }  <version_block> = \"Version\" : (\"5.0\")  <statement_block> = \"Statement\" : [ <policy_statement>, <policy_statement>, ... ]  <policy_statement> = {   <sid_block?>,   <effect_block>,   <action_block>,   <resource_block?>,   <condition_block?> }  <sid_block> = \"Sid\" : <sid_string>  <effect_block> = \"Effect\" : (\"Allow\" | \"Deny\")  <action_block> = (\"Action\" | \"NotAction\") : [ <action_string>, <action_string>, ... ]  <resource_block> = (\"Resource\" | \"NotResource\") : [ <resource_string>, <resource_string>, ... ]  <condition_block> = \"Condition\" : { <condition_map> }  <condition_map> = {   <condition_type_string> : { <condition_key_string> : <condition_value_list> },   <condition_type_string> : { <condition_key_string> : <condition_value_list> },   ... }  <condition_value_list> = ( <condition_value> | [ <condition_value>, <condition_value>, ... ] )  <condition_value> = \"string\" ``` 

        :return: The policy_document of this CreatePolicyVersionReqBody.
        :rtype: str
        """
        return self._policy_document

    @policy_document.setter
    def policy_document(self, policy_document):
        r"""Sets the policy_document of this CreatePolicyVersionReqBody.

        自定义身份策略或系统预置身份策略的策略文档的json格式。下面的字符`= < > ( ) |`是语法中的特殊字符，不包含在身份策略中。  问号`?`表示元素是可选的。例如`sid_block?`。  竖线`|`表示可选项，括号定义了可选项的范围。例如`(\"Allow\" | \"Deny\")`。  当一个元素允许多个值时，使用重复值`,`以及`...`表示。例如`[ <policy_statement>, <policy_statement>, ... ]`。  下面的递归文法描述了身份策略的语法： ``` policy = {   <version_block>,   <statement_block> }  <version_block> = \"Version\" : (\"5.0\")  <statement_block> = \"Statement\" : [ <policy_statement>, <policy_statement>, ... ]  <policy_statement> = {   <sid_block?>,   <effect_block>,   <action_block>,   <resource_block?>,   <condition_block?> }  <sid_block> = \"Sid\" : <sid_string>  <effect_block> = \"Effect\" : (\"Allow\" | \"Deny\")  <action_block> = (\"Action\" | \"NotAction\") : [ <action_string>, <action_string>, ... ]  <resource_block> = (\"Resource\" | \"NotResource\") : [ <resource_string>, <resource_string>, ... ]  <condition_block> = \"Condition\" : { <condition_map> }  <condition_map> = {   <condition_type_string> : { <condition_key_string> : <condition_value_list> },   <condition_type_string> : { <condition_key_string> : <condition_value_list> },   ... }  <condition_value_list> = ( <condition_value> | [ <condition_value>, <condition_value>, ... ] )  <condition_value> = \"string\" ``` 

        :param policy_document: The policy_document of this CreatePolicyVersionReqBody.
        :type policy_document: str
        """
        self._policy_document = policy_document

    @property
    def set_as_default(self):
        r"""Gets the set_as_default of this CreatePolicyVersionReqBody.

        是否设置为默认版本。

        :return: The set_as_default of this CreatePolicyVersionReqBody.
        :rtype: bool
        """
        return self._set_as_default

    @set_as_default.setter
    def set_as_default(self, set_as_default):
        r"""Sets the set_as_default of this CreatePolicyVersionReqBody.

        是否设置为默认版本。

        :param set_as_default: The set_as_default of this CreatePolicyVersionReqBody.
        :type set_as_default: bool
        """
        self._set_as_default = set_as_default

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
        if not isinstance(other, CreatePolicyVersionReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
