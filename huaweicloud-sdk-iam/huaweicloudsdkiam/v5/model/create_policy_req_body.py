# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePolicyReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'path': 'str',
        'policy_document': 'str',
        'description': 'str'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'path': 'path',
        'policy_document': 'policy_document',
        'description': 'description'
    }

    def __init__(self, policy_name=None, path=None, policy_document=None, description=None):
        r"""CreatePolicyReqBody

        The model defined in huaweicloud sdk

        :param policy_name: 身份策略名称，长度为1到128个字符，只包含字母、数字、\&quot;_\&quot;、\&quot;+\&quot;、\&quot;&#x3D;\&quot;、\&quot;.\&quot;、\&quot;@\&quot;和\&quot;-\&quot;的字符串。
        :type policy_name: str
        :param path: 资源路径，默认为空串。由若干段字符串拼接而成，每段先包含一个或多个字母、数字、\&quot;.\&quot;、\&quot;,\&quot;、\&quot;+\&quot;、\&quot;@\&quot;、\&quot;&#x3D;\&quot;、\&quot;_\&quot;或\&quot;-\&quot;，并以\&quot;/\&quot;结尾，例如\&quot;foo/bar/\&quot;。
        :type path: str
        :param policy_document: 自定义身份策略或系统预置身份策略的策略文档的json格式。下面的字符&#x60;&#x3D; &lt; &gt; ( ) |&#x60;是语法中的特殊字符，不包含在身份策略中。  问号&#x60;?&#x60;表示元素是可选的。例如&#x60;sid_block?&#x60;。  竖线&#x60;|&#x60;表示可选项，括号定义了可选项的范围。例如&#x60;(\&quot;Allow\&quot; | \&quot;Deny\&quot;)&#x60;。  当一个元素允许多个值时，使用重复值&#x60;,&#x60;以及&#x60;...&#x60;表示。例如&#x60;[ &lt;policy_statement&gt;, &lt;policy_statement&gt;, ... ]&#x60;。  下面的递归文法描述了身份策略的语法： &#x60;&#x60;&#x60; policy &#x3D; {   &lt;version_block&gt;,   &lt;statement_block&gt; }  &lt;version_block&gt; &#x3D; \&quot;Version\&quot; : (\&quot;5.0\&quot;)  &lt;statement_block&gt; &#x3D; \&quot;Statement\&quot; : [ &lt;policy_statement&gt;, &lt;policy_statement&gt;, ... ]  &lt;policy_statement&gt; &#x3D; {   &lt;sid_block?&gt;,   &lt;effect_block&gt;,   &lt;action_block&gt;,   &lt;resource_block?&gt;,   &lt;condition_block?&gt; }  &lt;sid_block&gt; &#x3D; \&quot;Sid\&quot; : &lt;sid_string&gt;  &lt;effect_block&gt; &#x3D; \&quot;Effect\&quot; : (\&quot;Allow\&quot; | \&quot;Deny\&quot;)  &lt;action_block&gt; &#x3D; (\&quot;Action\&quot; | \&quot;NotAction\&quot;) : [ &lt;action_string&gt;, &lt;action_string&gt;, ... ]  &lt;resource_block&gt; &#x3D; (\&quot;Resource\&quot; | \&quot;NotResource\&quot;) : [ &lt;resource_string&gt;, &lt;resource_string&gt;, ... ]  &lt;condition_block&gt; &#x3D; \&quot;Condition\&quot; : { &lt;condition_map&gt; }  &lt;condition_map&gt; &#x3D; {   &lt;condition_type_string&gt; : { &lt;condition_key_string&gt; : &lt;condition_value_list&gt; },   &lt;condition_type_string&gt; : { &lt;condition_key_string&gt; : &lt;condition_value_list&gt; },   ... }  &lt;condition_value_list&gt; &#x3D; ( &lt;condition_value&gt; | [ &lt;condition_value&gt;, &lt;condition_value&gt;, ... ] )  &lt;condition_value&gt; &#x3D; \&quot;string\&quot; &#x60;&#x60;&#x60; 
        :type policy_document: str
        :param description: 身份策略描述。
        :type description: str
        """
        
        

        self._policy_name = None
        self._path = None
        self._policy_document = None
        self._description = None
        self.discriminator = None

        self.policy_name = policy_name
        if path is not None:
            self.path = path
        self.policy_document = policy_document
        if description is not None:
            self.description = description

    @property
    def policy_name(self):
        r"""Gets the policy_name of this CreatePolicyReqBody.

        身份策略名称，长度为1到128个字符，只包含字母、数字、\"_\"、\"+\"、\"=\"、\".\"、\"@\"和\"-\"的字符串。

        :return: The policy_name of this CreatePolicyReqBody.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this CreatePolicyReqBody.

        身份策略名称，长度为1到128个字符，只包含字母、数字、\"_\"、\"+\"、\"=\"、\".\"、\"@\"和\"-\"的字符串。

        :param policy_name: The policy_name of this CreatePolicyReqBody.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def path(self):
        r"""Gets the path of this CreatePolicyReqBody.

        资源路径，默认为空串。由若干段字符串拼接而成，每段先包含一个或多个字母、数字、\".\"、\",\"、\"+\"、\"@\"、\"=\"、\"_\"或\"-\"，并以\"/\"结尾，例如\"foo/bar/\"。

        :return: The path of this CreatePolicyReqBody.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this CreatePolicyReqBody.

        资源路径，默认为空串。由若干段字符串拼接而成，每段先包含一个或多个字母、数字、\".\"、\",\"、\"+\"、\"@\"、\"=\"、\"_\"或\"-\"，并以\"/\"结尾，例如\"foo/bar/\"。

        :param path: The path of this CreatePolicyReqBody.
        :type path: str
        """
        self._path = path

    @property
    def policy_document(self):
        r"""Gets the policy_document of this CreatePolicyReqBody.

        自定义身份策略或系统预置身份策略的策略文档的json格式。下面的字符`= < > ( ) |`是语法中的特殊字符，不包含在身份策略中。  问号`?`表示元素是可选的。例如`sid_block?`。  竖线`|`表示可选项，括号定义了可选项的范围。例如`(\"Allow\" | \"Deny\")`。  当一个元素允许多个值时，使用重复值`,`以及`...`表示。例如`[ <policy_statement>, <policy_statement>, ... ]`。  下面的递归文法描述了身份策略的语法： ``` policy = {   <version_block>,   <statement_block> }  <version_block> = \"Version\" : (\"5.0\")  <statement_block> = \"Statement\" : [ <policy_statement>, <policy_statement>, ... ]  <policy_statement> = {   <sid_block?>,   <effect_block>,   <action_block>,   <resource_block?>,   <condition_block?> }  <sid_block> = \"Sid\" : <sid_string>  <effect_block> = \"Effect\" : (\"Allow\" | \"Deny\")  <action_block> = (\"Action\" | \"NotAction\") : [ <action_string>, <action_string>, ... ]  <resource_block> = (\"Resource\" | \"NotResource\") : [ <resource_string>, <resource_string>, ... ]  <condition_block> = \"Condition\" : { <condition_map> }  <condition_map> = {   <condition_type_string> : { <condition_key_string> : <condition_value_list> },   <condition_type_string> : { <condition_key_string> : <condition_value_list> },   ... }  <condition_value_list> = ( <condition_value> | [ <condition_value>, <condition_value>, ... ] )  <condition_value> = \"string\" ``` 

        :return: The policy_document of this CreatePolicyReqBody.
        :rtype: str
        """
        return self._policy_document

    @policy_document.setter
    def policy_document(self, policy_document):
        r"""Sets the policy_document of this CreatePolicyReqBody.

        自定义身份策略或系统预置身份策略的策略文档的json格式。下面的字符`= < > ( ) |`是语法中的特殊字符，不包含在身份策略中。  问号`?`表示元素是可选的。例如`sid_block?`。  竖线`|`表示可选项，括号定义了可选项的范围。例如`(\"Allow\" | \"Deny\")`。  当一个元素允许多个值时，使用重复值`,`以及`...`表示。例如`[ <policy_statement>, <policy_statement>, ... ]`。  下面的递归文法描述了身份策略的语法： ``` policy = {   <version_block>,   <statement_block> }  <version_block> = \"Version\" : (\"5.0\")  <statement_block> = \"Statement\" : [ <policy_statement>, <policy_statement>, ... ]  <policy_statement> = {   <sid_block?>,   <effect_block>,   <action_block>,   <resource_block?>,   <condition_block?> }  <sid_block> = \"Sid\" : <sid_string>  <effect_block> = \"Effect\" : (\"Allow\" | \"Deny\")  <action_block> = (\"Action\" | \"NotAction\") : [ <action_string>, <action_string>, ... ]  <resource_block> = (\"Resource\" | \"NotResource\") : [ <resource_string>, <resource_string>, ... ]  <condition_block> = \"Condition\" : { <condition_map> }  <condition_map> = {   <condition_type_string> : { <condition_key_string> : <condition_value_list> },   <condition_type_string> : { <condition_key_string> : <condition_value_list> },   ... }  <condition_value_list> = ( <condition_value> | [ <condition_value>, <condition_value>, ... ] )  <condition_value> = \"string\" ``` 

        :param policy_document: The policy_document of this CreatePolicyReqBody.
        :type policy_document: str
        """
        self._policy_document = policy_document

    @property
    def description(self):
        r"""Gets the description of this CreatePolicyReqBody.

        身份策略描述。

        :return: The description of this CreatePolicyReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePolicyReqBody.

        身份策略描述。

        :param description: The description of this CreatePolicyReqBody.
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
        if not isinstance(other, CreatePolicyReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
