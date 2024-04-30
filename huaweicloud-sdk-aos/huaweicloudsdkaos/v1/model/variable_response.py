# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VariableResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'description': 'str',
        'default': 'object',
        'sensitive': 'bool',
        'nullable': 'bool',
        'validations': 'list[VariableValidationResponse]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'default': 'default',
        'sensitive': 'sensitive',
        'nullable': 'nullable',
        'validations': 'validations'
    }

    def __init__(self, name=None, type=None, description=None, default=None, sensitive=None, nullable=None, validations=None):
        """VariableResponse

        The model defined in huaweicloud sdk

        :param name: 参数的名字  以HCL格式的模板为例，name 为 &#x60;my_hello_world_variable&#x60;  &#x60;&#x60;&#x60;hcl variable \&quot;my_hello_world_variable\&quot; {   type &#x3D; string   description &#x3D; \&quot;this is a variable\&quot;   default &#x3D; \&quot;hello world\&quot;   sensitive &#x3D; false   nullable &#x3D; false   validation {     condition     &#x3D; length(var.my_hello_world_variable) &gt; 0 &amp;&amp; substr(var.my_hello_world_variable, 0, 5) &#x3D;&#x3D; \&quot;hello\&quot;     error_message &#x3D; \&quot;my_hello_world_variable should start with &#39;hello&#39;.\&quot;   } } &#x60;&#x60;&#x60;  以json格式的模板为例，name 为 &#x60;my_hello_world_variable&#x60;  &#x60;&#x60;&#x60;json {   \&quot;variable\&quot;: {     \&quot;my_hello_world_variable\&quot;: [       {         \&quot;default\&quot;: \&quot;hello world\&quot;,         \&quot;description\&quot;: \&quot;this is a variable\&quot;,         \&quot;nullable\&quot;: false,         \&quot;sensitive\&quot;: false,         \&quot;type\&quot;: \&quot;string\&quot;,         \&quot;validation\&quot;: [           {             \&quot;condition\&quot;: \&quot;${length(var.my_hello_world_variable) &gt; 0 &amp;&amp; substr(var.my_hello_world_variable, 0, 5) &#x3D;&#x3D; \\\&quot;hello\\\&quot;}\&quot;,             \&quot;error_message\&quot;: \&quot;my_hello_world_variable should start with &#39;hello&#39;.\&quot;           }         ]       }     ]   } } &#x60;&#x60;&#x60;
        :type name: str
        :param type: 参数的类型  以HCL格式的模板为例，type 为 &#x60;string&#x60;  &#x60;&#x60;&#x60;hcl variable \&quot;my_hello_world_variable\&quot; {   type &#x3D; string   description &#x3D; \&quot;this is a variable\&quot;   default &#x3D; \&quot;hello world\&quot;   sensitive &#x3D; false   nullable &#x3D; false   validation {     condition     &#x3D; length(var.my_hello_world_variable) &gt; 0 &amp;&amp; substr(var.my_hello_world_variable, 0, 5) &#x3D;&#x3D; \&quot;hello\&quot;     error_message &#x3D; \&quot;my_hello_world_variable should start with &#39;hello&#39;.\&quot;   } } &#x60;&#x60;&#x60;  以json格式的模板为例，type 为 &#x60;string&#x60;  &#x60;&#x60;&#x60;json {   \&quot;variable\&quot;: {     \&quot;my_hello_world_variable\&quot;: [       {         \&quot;default\&quot;: \&quot;hello world\&quot;,         \&quot;description\&quot;: \&quot;this is a variable\&quot;,         \&quot;nullable\&quot;: false,         \&quot;sensitive\&quot;: false,         \&quot;type\&quot;: \&quot;string\&quot;,         \&quot;validation\&quot;: [           {             \&quot;condition\&quot;: \&quot;${length(var.my_hello_world_variable) &gt; 0 &amp;&amp; substr(var.my_hello_world_variable, 0, 5) &#x3D;&#x3D; \\\&quot;hello\\\&quot;}\&quot;,             \&quot;error_message\&quot;: \&quot;my_hello_world_variable should start with &#39;hello&#39;.\&quot;           }         ]       }     ]   } } &#x60;&#x60;&#x60;
        :type type: str
        :param description: 参数的描述  以HCL格式的模板为例，description 为 &#x60;this is a variable&#x60;  &#x60;&#x60;&#x60;hcl variable \&quot;my_hello_world_variable\&quot; {   type &#x3D; string   description &#x3D; \&quot;this is a variable\&quot;   default &#x3D; \&quot;hello world\&quot;   sensitive &#x3D; false   nullable &#x3D; false   validation {     condition     &#x3D; length(var.my_hello_world_variable) &gt; 0 &amp;&amp; substr(var.my_hello_world_variable, 0, 5) &#x3D;&#x3D; \&quot;hello\&quot;     error_message &#x3D; \&quot;my_hello_world_variable should start with &#39;hello&#39;.\&quot;   } } &#x60;&#x60;&#x60;  以json格式的模板为例，description 为 &#x60;this is a variable&#x60;  &#x60;&#x60;&#x60;json {   \&quot;variable\&quot;: {     \&quot;my_hello_world_variable\&quot;: [       {         \&quot;default\&quot;: \&quot;hello world\&quot;,         \&quot;description\&quot;: \&quot;this is a variable\&quot;,         \&quot;nullable\&quot;: false,         \&quot;sensitive\&quot;: false,         \&quot;type\&quot;: \&quot;string\&quot;,         \&quot;validation\&quot;: [           {             \&quot;condition\&quot;: \&quot;${length(var.my_hello_world_variable) &gt; 0 &amp;&amp; substr(var.my_hello_world_variable, 0, 5) &#x3D;&#x3D; \\\&quot;hello\\\&quot;}\&quot;,             \&quot;error_message\&quot;: \&quot;my_hello_world_variable should start with &#39;hello&#39;.\&quot;           }         ]       }     ]   } } &#x60;&#x60;&#x60;
        :type description: str
        :param default: 参数默认值。此返回值的类型将与type保持一致  例如，对于type为string的变量，此值的返回类型为string；对于type为number的变量，此值的返回类型为number  以HCL格式的模板为例，default 为 &#x60;hello world&#x60;  &#x60;&#x60;&#x60;hcl variable \&quot;my_hello_world_variable\&quot; {   type &#x3D; string   description &#x3D; \&quot;this is a variable\&quot;   default &#x3D; \&quot;hello world\&quot;   sensitive &#x3D; false   nullable &#x3D; false   validation {     condition     &#x3D; length(var.my_hello_world_variable) &gt; 0 &amp;&amp; substr(var.my_hello_world_variable, 0, 5) &#x3D;&#x3D; \&quot;hello\&quot;     error_message &#x3D; \&quot;my_hello_world_variable should start with &#39;hello&#39;.\&quot;   } } &#x60;&#x60;&#x60;  以json格式的模板为例，default 为 &#x60;hello world&#x60;  &#x60;&#x60;&#x60;json {   \&quot;variable\&quot;: {     \&quot;my_hello_world_variable\&quot;: [       {         \&quot;default\&quot;: \&quot;hello world\&quot;,         \&quot;description\&quot;: \&quot;this is a variable\&quot;,         \&quot;nullable\&quot;: false,         \&quot;sensitive\&quot;: false,         \&quot;type\&quot;: \&quot;string\&quot;,         \&quot;validation\&quot;: [           {             \&quot;condition\&quot;: \&quot;${length(var.my_hello_world_variable) &gt; 0 &amp;&amp; substr(var.my_hello_world_variable, 0, 5) &#x3D;&#x3D; \\\&quot;hello\\\&quot;}\&quot;,             \&quot;error_message\&quot;: \&quot;my_hello_world_variable should start with &#39;hello&#39;.\&quot;           }         ]       }     ]   } } &#x60;&#x60;&#x60;
        :type default: object
        :param sensitive: 参数是否为敏感字段  如果variable中没有定义sensitive，默认返回false。  以HCL格式的模板为例，sensitive 为 &#x60;false&#x60;  &#x60;&#x60;&#x60;hcl variable \&quot;my_hello_world_variable\&quot; {   type &#x3D; string   description &#x3D; \&quot;this is a variable\&quot;   default &#x3D; \&quot;hello world\&quot;   sensitive &#x3D; false   nullable &#x3D; false   validation {     condition     &#x3D; length(var.my_hello_world_variable) &gt; 0 &amp;&amp; substr(var.my_hello_world_variable, 0, 5) &#x3D;&#x3D; \&quot;hello\&quot;     error_message &#x3D; \&quot;my_hello_world_variable should start with &#39;hello&#39;.\&quot;   } } &#x60;&#x60;&#x60;  以json格式的模板为例，sensitive 为 &#x60;false&#x60;  &#x60;&#x60;&#x60;json {   \&quot;variable\&quot;: {     \&quot;my_hello_world_variable\&quot;: [       {         \&quot;default\&quot;: \&quot;hello world\&quot;,         \&quot;description\&quot;: \&quot;this is a variable\&quot;,         \&quot;nullable\&quot;: false,         \&quot;sensitive\&quot;: false,         \&quot;type\&quot;: \&quot;string\&quot;,         \&quot;validation\&quot;: [           {             \&quot;condition\&quot;: \&quot;${length(var.my_hello_world_variable) &gt; 0 &amp;&amp; substr(var.my_hello_world_variable, 0, 5) &#x3D;&#x3D; \\\&quot;hello\\\&quot;}\&quot;,             \&quot;error_message\&quot;: \&quot;my_hello_world_variable should start with &#39;hello&#39;.\&quot;           }         ]       }     ]   } } &#x60;&#x60;&#x60;
        :type sensitive: bool
        :param nullable: 参数是否可设置为null。  如果variable中没有定义nullable，默认返回true。  以HCL格式的模板为例，nullable 为 &#x60;false&#x60;  &#x60;&#x60;&#x60;hcl variable \&quot;my_hello_world_variable\&quot; {   type &#x3D; string   description &#x3D; \&quot;this is a variable\&quot;   default &#x3D; \&quot;hello world\&quot;   sensitive &#x3D; false   nullable &#x3D; false   validation {     condition     &#x3D; length(var.my_hello_world_variable) &gt; 0 &amp;&amp; substr(var.my_hello_world_variable, 0, 5) &#x3D;&#x3D; \&quot;hello\&quot;     error_message &#x3D; \&quot;my_hello_world_variable should start with &#39;hello&#39;.\&quot;   } } &#x60;&#x60;&#x60;  以json格式的模板为例，nullable 为 &#x60;false&#x60;  &#x60;&#x60;&#x60;json {   \&quot;variable\&quot;: {     \&quot;my_hello_world_variable\&quot;: [       {         \&quot;default\&quot;: \&quot;hello world\&quot;,         \&quot;description\&quot;: \&quot;this is a variable\&quot;,         \&quot;nullable\&quot;: false,         \&quot;sensitive\&quot;: false,         \&quot;type\&quot;: \&quot;string\&quot;,         \&quot;validation\&quot;: [           {             \&quot;condition\&quot;: \&quot;${length(var.my_hello_world_variable) &gt; 0 &amp;&amp; substr(var.my_hello_world_variable, 0, 5) &#x3D;&#x3D; \\\&quot;hello\\\&quot;}\&quot;,             \&quot;error_message\&quot;: \&quot;my_hello_world_variable should start with &#39;hello&#39;.\&quot;           }         ]       }     ]   } } &#x60;&#x60;&#x60;
        :type nullable: bool
        :param validations: 参数的校验模块
        :type validations: list[:class:`huaweicloudsdkaos.v1.VariableValidationResponse`]
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._default = None
        self._sensitive = None
        self._nullable = None
        self._validations = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if default is not None:
            self.default = default
        if sensitive is not None:
            self.sensitive = sensitive
        if nullable is not None:
            self.nullable = nullable
        if validations is not None:
            self.validations = validations

    @property
    def name(self):
        """Gets the name of this VariableResponse.

        参数的名字  以HCL格式的模板为例，name 为 `my_hello_world_variable`  ```hcl variable \"my_hello_world_variable\" {   type = string   description = \"this is a variable\"   default = \"hello world\"   sensitive = false   nullable = false   validation {     condition     = length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \"hello\"     error_message = \"my_hello_world_variable should start with 'hello'.\"   } } ```  以json格式的模板为例，name 为 `my_hello_world_variable`  ```json {   \"variable\": {     \"my_hello_world_variable\": [       {         \"default\": \"hello world\",         \"description\": \"this is a variable\",         \"nullable\": false,         \"sensitive\": false,         \"type\": \"string\",         \"validation\": [           {             \"condition\": \"${length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \\\"hello\\\"}\",             \"error_message\": \"my_hello_world_variable should start with 'hello'.\"           }         ]       }     ]   } } ```

        :return: The name of this VariableResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariableResponse.

        参数的名字  以HCL格式的模板为例，name 为 `my_hello_world_variable`  ```hcl variable \"my_hello_world_variable\" {   type = string   description = \"this is a variable\"   default = \"hello world\"   sensitive = false   nullable = false   validation {     condition     = length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \"hello\"     error_message = \"my_hello_world_variable should start with 'hello'.\"   } } ```  以json格式的模板为例，name 为 `my_hello_world_variable`  ```json {   \"variable\": {     \"my_hello_world_variable\": [       {         \"default\": \"hello world\",         \"description\": \"this is a variable\",         \"nullable\": false,         \"sensitive\": false,         \"type\": \"string\",         \"validation\": [           {             \"condition\": \"${length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \\\"hello\\\"}\",             \"error_message\": \"my_hello_world_variable should start with 'hello'.\"           }         ]       }     ]   } } ```

        :param name: The name of this VariableResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this VariableResponse.

        参数的类型  以HCL格式的模板为例，type 为 `string`  ```hcl variable \"my_hello_world_variable\" {   type = string   description = \"this is a variable\"   default = \"hello world\"   sensitive = false   nullable = false   validation {     condition     = length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \"hello\"     error_message = \"my_hello_world_variable should start with 'hello'.\"   } } ```  以json格式的模板为例，type 为 `string`  ```json {   \"variable\": {     \"my_hello_world_variable\": [       {         \"default\": \"hello world\",         \"description\": \"this is a variable\",         \"nullable\": false,         \"sensitive\": false,         \"type\": \"string\",         \"validation\": [           {             \"condition\": \"${length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \\\"hello\\\"}\",             \"error_message\": \"my_hello_world_variable should start with 'hello'.\"           }         ]       }     ]   } } ```

        :return: The type of this VariableResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VariableResponse.

        参数的类型  以HCL格式的模板为例，type 为 `string`  ```hcl variable \"my_hello_world_variable\" {   type = string   description = \"this is a variable\"   default = \"hello world\"   sensitive = false   nullable = false   validation {     condition     = length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \"hello\"     error_message = \"my_hello_world_variable should start with 'hello'.\"   } } ```  以json格式的模板为例，type 为 `string`  ```json {   \"variable\": {     \"my_hello_world_variable\": [       {         \"default\": \"hello world\",         \"description\": \"this is a variable\",         \"nullable\": false,         \"sensitive\": false,         \"type\": \"string\",         \"validation\": [           {             \"condition\": \"${length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \\\"hello\\\"}\",             \"error_message\": \"my_hello_world_variable should start with 'hello'.\"           }         ]       }     ]   } } ```

        :param type: The type of this VariableResponse.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this VariableResponse.

        参数的描述  以HCL格式的模板为例，description 为 `this is a variable`  ```hcl variable \"my_hello_world_variable\" {   type = string   description = \"this is a variable\"   default = \"hello world\"   sensitive = false   nullable = false   validation {     condition     = length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \"hello\"     error_message = \"my_hello_world_variable should start with 'hello'.\"   } } ```  以json格式的模板为例，description 为 `this is a variable`  ```json {   \"variable\": {     \"my_hello_world_variable\": [       {         \"default\": \"hello world\",         \"description\": \"this is a variable\",         \"nullable\": false,         \"sensitive\": false,         \"type\": \"string\",         \"validation\": [           {             \"condition\": \"${length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \\\"hello\\\"}\",             \"error_message\": \"my_hello_world_variable should start with 'hello'.\"           }         ]       }     ]   } } ```

        :return: The description of this VariableResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariableResponse.

        参数的描述  以HCL格式的模板为例，description 为 `this is a variable`  ```hcl variable \"my_hello_world_variable\" {   type = string   description = \"this is a variable\"   default = \"hello world\"   sensitive = false   nullable = false   validation {     condition     = length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \"hello\"     error_message = \"my_hello_world_variable should start with 'hello'.\"   } } ```  以json格式的模板为例，description 为 `this is a variable`  ```json {   \"variable\": {     \"my_hello_world_variable\": [       {         \"default\": \"hello world\",         \"description\": \"this is a variable\",         \"nullable\": false,         \"sensitive\": false,         \"type\": \"string\",         \"validation\": [           {             \"condition\": \"${length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \\\"hello\\\"}\",             \"error_message\": \"my_hello_world_variable should start with 'hello'.\"           }         ]       }     ]   } } ```

        :param description: The description of this VariableResponse.
        :type description: str
        """
        self._description = description

    @property
    def default(self):
        """Gets the default of this VariableResponse.

        参数默认值。此返回值的类型将与type保持一致  例如，对于type为string的变量，此值的返回类型为string；对于type为number的变量，此值的返回类型为number  以HCL格式的模板为例，default 为 `hello world`  ```hcl variable \"my_hello_world_variable\" {   type = string   description = \"this is a variable\"   default = \"hello world\"   sensitive = false   nullable = false   validation {     condition     = length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \"hello\"     error_message = \"my_hello_world_variable should start with 'hello'.\"   } } ```  以json格式的模板为例，default 为 `hello world`  ```json {   \"variable\": {     \"my_hello_world_variable\": [       {         \"default\": \"hello world\",         \"description\": \"this is a variable\",         \"nullable\": false,         \"sensitive\": false,         \"type\": \"string\",         \"validation\": [           {             \"condition\": \"${length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \\\"hello\\\"}\",             \"error_message\": \"my_hello_world_variable should start with 'hello'.\"           }         ]       }     ]   } } ```

        :return: The default of this VariableResponse.
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this VariableResponse.

        参数默认值。此返回值的类型将与type保持一致  例如，对于type为string的变量，此值的返回类型为string；对于type为number的变量，此值的返回类型为number  以HCL格式的模板为例，default 为 `hello world`  ```hcl variable \"my_hello_world_variable\" {   type = string   description = \"this is a variable\"   default = \"hello world\"   sensitive = false   nullable = false   validation {     condition     = length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \"hello\"     error_message = \"my_hello_world_variable should start with 'hello'.\"   } } ```  以json格式的模板为例，default 为 `hello world`  ```json {   \"variable\": {     \"my_hello_world_variable\": [       {         \"default\": \"hello world\",         \"description\": \"this is a variable\",         \"nullable\": false,         \"sensitive\": false,         \"type\": \"string\",         \"validation\": [           {             \"condition\": \"${length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \\\"hello\\\"}\",             \"error_message\": \"my_hello_world_variable should start with 'hello'.\"           }         ]       }     ]   } } ```

        :param default: The default of this VariableResponse.
        :type default: object
        """
        self._default = default

    @property
    def sensitive(self):
        """Gets the sensitive of this VariableResponse.

        参数是否为敏感字段  如果variable中没有定义sensitive，默认返回false。  以HCL格式的模板为例，sensitive 为 `false`  ```hcl variable \"my_hello_world_variable\" {   type = string   description = \"this is a variable\"   default = \"hello world\"   sensitive = false   nullable = false   validation {     condition     = length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \"hello\"     error_message = \"my_hello_world_variable should start with 'hello'.\"   } } ```  以json格式的模板为例，sensitive 为 `false`  ```json {   \"variable\": {     \"my_hello_world_variable\": [       {         \"default\": \"hello world\",         \"description\": \"this is a variable\",         \"nullable\": false,         \"sensitive\": false,         \"type\": \"string\",         \"validation\": [           {             \"condition\": \"${length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \\\"hello\\\"}\",             \"error_message\": \"my_hello_world_variable should start with 'hello'.\"           }         ]       }     ]   } } ```

        :return: The sensitive of this VariableResponse.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """Sets the sensitive of this VariableResponse.

        参数是否为敏感字段  如果variable中没有定义sensitive，默认返回false。  以HCL格式的模板为例，sensitive 为 `false`  ```hcl variable \"my_hello_world_variable\" {   type = string   description = \"this is a variable\"   default = \"hello world\"   sensitive = false   nullable = false   validation {     condition     = length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \"hello\"     error_message = \"my_hello_world_variable should start with 'hello'.\"   } } ```  以json格式的模板为例，sensitive 为 `false`  ```json {   \"variable\": {     \"my_hello_world_variable\": [       {         \"default\": \"hello world\",         \"description\": \"this is a variable\",         \"nullable\": false,         \"sensitive\": false,         \"type\": \"string\",         \"validation\": [           {             \"condition\": \"${length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \\\"hello\\\"}\",             \"error_message\": \"my_hello_world_variable should start with 'hello'.\"           }         ]       }     ]   } } ```

        :param sensitive: The sensitive of this VariableResponse.
        :type sensitive: bool
        """
        self._sensitive = sensitive

    @property
    def nullable(self):
        """Gets the nullable of this VariableResponse.

        参数是否可设置为null。  如果variable中没有定义nullable，默认返回true。  以HCL格式的模板为例，nullable 为 `false`  ```hcl variable \"my_hello_world_variable\" {   type = string   description = \"this is a variable\"   default = \"hello world\"   sensitive = false   nullable = false   validation {     condition     = length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \"hello\"     error_message = \"my_hello_world_variable should start with 'hello'.\"   } } ```  以json格式的模板为例，nullable 为 `false`  ```json {   \"variable\": {     \"my_hello_world_variable\": [       {         \"default\": \"hello world\",         \"description\": \"this is a variable\",         \"nullable\": false,         \"sensitive\": false,         \"type\": \"string\",         \"validation\": [           {             \"condition\": \"${length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \\\"hello\\\"}\",             \"error_message\": \"my_hello_world_variable should start with 'hello'.\"           }         ]       }     ]   } } ```

        :return: The nullable of this VariableResponse.
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        """Sets the nullable of this VariableResponse.

        参数是否可设置为null。  如果variable中没有定义nullable，默认返回true。  以HCL格式的模板为例，nullable 为 `false`  ```hcl variable \"my_hello_world_variable\" {   type = string   description = \"this is a variable\"   default = \"hello world\"   sensitive = false   nullable = false   validation {     condition     = length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \"hello\"     error_message = \"my_hello_world_variable should start with 'hello'.\"   } } ```  以json格式的模板为例，nullable 为 `false`  ```json {   \"variable\": {     \"my_hello_world_variable\": [       {         \"default\": \"hello world\",         \"description\": \"this is a variable\",         \"nullable\": false,         \"sensitive\": false,         \"type\": \"string\",         \"validation\": [           {             \"condition\": \"${length(var.my_hello_world_variable) > 0 && substr(var.my_hello_world_variable, 0, 5) == \\\"hello\\\"}\",             \"error_message\": \"my_hello_world_variable should start with 'hello'.\"           }         ]       }     ]   } } ```

        :param nullable: The nullable of this VariableResponse.
        :type nullable: bool
        """
        self._nullable = nullable

    @property
    def validations(self):
        """Gets the validations of this VariableResponse.

        参数的校验模块

        :return: The validations of this VariableResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.VariableValidationResponse`]
        """
        return self._validations

    @validations.setter
    def validations(self, validations):
        """Sets the validations of this VariableResponse.

        参数的校验模块

        :param validations: The validations of this VariableResponse.
        :type validations: list[:class:`huaweicloudsdkaos.v1.VariableValidationResponse`]
        """
        self._validations = validations

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
        if not isinstance(other, VariableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
