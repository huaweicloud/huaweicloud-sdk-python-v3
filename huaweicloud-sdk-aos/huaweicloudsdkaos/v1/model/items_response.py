# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ItemsResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_name': 'str',
        'index': 'str',
        'module_address': 'str',
        'supported': 'bool',
        'unsupported_message': 'str',
        'resource_price': 'list[ResourcePriceResponse]'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_name': 'resource_name',
        'index': 'index',
        'module_address': 'module_address',
        'supported': 'supported',
        'unsupported_message': 'unsupported_message',
        'resource_price': 'resource_price'
    }

    def __init__(self, resource_type=None, resource_name=None, index=None, module_address=None, supported=None, unsupported_message=None, resource_price=None):
        r"""ItemsResponse

        The model defined in huaweicloud sdk

        :param resource_type: 资源的类型  以HCL格式的模板为例，resource_type 为 huaweicloud_vpc  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   name &#x3D; \&quot;test_vpc\&quot; } &#x60;&#x60;&#x60;  以json格式的模板为例，resource_type 为 huaweicloud_vpc  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;name\&quot;: \&quot;test_vpc\&quot;       }     }   } } &#x60;&#x60;&#x60;
        :type resource_type: str
        :param resource_name: 资源的名称，默认为资源的逻辑名称  以HCL格式的模板为例，resource_name 为 my_hello_world_vpc  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   name &#x3D; \&quot;test_vpc\&quot; } &#x60;&#x60;&#x60;  以json格式的模板为例，resource_name 为 my_hello_world_vpc  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;name\&quot;: \&quot;test_vpc\&quot;       }     }   } } &#x60;&#x60;&#x60;
        :type resource_name: str
        :param index: 资源的索引，如果用户在模板中使用了count或for_each则会返回index。如果index出现，则resource_name + index可以作为该资源的一种标识  如果用户在模板中使用count，则index为从0开始的数字  以HCL格式的模板为例，用户在模板中可以通过&#x60;huaweicloud_vpc.my_hello_world_vpc[0]&#x60;和&#x60;huaweicloud_vpc.my_hello_world_vpc[1]&#x60;标识两个资源  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   count &#x3D; 2   name &#x3D; \&quot;test_vpc\&quot; } &#x60;&#x60;&#x60;  以json格式的模板为例，用户在模板中可以通过&#x60;huaweicloud_vpc.my_hello_world_vpc[0]&#x60;和&#x60;huaweicloud_vpc.my_hello_world_vpc[1]&#x60;标识两个资源  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;name\&quot;: \&quot;test_vpc\&quot;,         \&quot;count\&quot;: 2       }     }   } } &#x60;&#x60;&#x60;  如果用户在模板中使用for_each，则index为用户自定义的字符串  以HCL格式的模板为例，用户在模板中可以通过&#x60;huaweicloud_vpc.my_hello_world_vpc[\&quot;vpc1\&quot;]&#x60;和&#x60;huaweicloud_vpc.my_hello_world_vpc[\&quot;vpc2\&quot;]&#x60;标识两个资源  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   for_each &#x3D; {     \&quot;vpc1\&quot; &#x3D; \&quot;test_vpc\&quot;     \&quot;vpc2\&quot; &#x3D; \&quot;test_vpc\&quot;   }   name &#x3D; each.value } &#x60;&#x60;&#x60;  以json格式的模板为例，用户在模板中可以通过&#x60;huaweicloud_vpc.my_hello_world_vpc[\&quot;vpc1\&quot;]&#x60;和&#x60;huaweicloud_vpc.my_hello_world_vpc[\&quot;vpc2\&quot;]&#x60;标识两个资源  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;for_each\&quot;: {           \&quot;vpc1\&quot;: \&quot;test_vpc\&quot;,           \&quot;vpc2\&quot;: \&quot;test_vpc\&quot;         }         \&quot;name\&quot;: \&quot;${each.value}\&quot;       }     }   } } &#x60;&#x60;&#x60;
        :type index: str
        :param module_address: 该资源的模块地址
        :type module_address: str
        :param supported: 该资源或该资源当前所给予的参数是否支持进行询价
        :type supported: bool
        :param unsupported_message: 该资源不支持询价的具体原因
        :type unsupported_message: str
        :param resource_price: 该资源的询价信息  如果该资源支持包周期计费或按需计费，或者该资源为免费资源，则返回该字段；如果该资源不支持询价，则不返回该字段。
        :type resource_price: list[:class:`huaweicloudsdkaos.v1.ResourcePriceResponse`]
        """
        
        

        self._resource_type = None
        self._resource_name = None
        self._index = None
        self._module_address = None
        self._supported = None
        self._unsupported_message = None
        self._resource_price = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if resource_name is not None:
            self.resource_name = resource_name
        if index is not None:
            self.index = index
        if module_address is not None:
            self.module_address = module_address
        if supported is not None:
            self.supported = supported
        if unsupported_message is not None:
            self.unsupported_message = unsupported_message
        if resource_price is not None:
            self.resource_price = resource_price

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ItemsResponse.

        资源的类型  以HCL格式的模板为例，resource_type 为 huaweicloud_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，resource_type 为 huaweicloud_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :return: The resource_type of this ItemsResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ItemsResponse.

        资源的类型  以HCL格式的模板为例，resource_type 为 huaweicloud_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，resource_type 为 huaweicloud_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :param resource_type: The resource_type of this ItemsResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ItemsResponse.

        资源的名称，默认为资源的逻辑名称  以HCL格式的模板为例，resource_name 为 my_hello_world_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，resource_name 为 my_hello_world_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :return: The resource_name of this ItemsResponse.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ItemsResponse.

        资源的名称，默认为资源的逻辑名称  以HCL格式的模板为例，resource_name 为 my_hello_world_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，resource_name 为 my_hello_world_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :param resource_name: The resource_name of this ItemsResponse.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def index(self):
        r"""Gets the index of this ItemsResponse.

        资源的索引，如果用户在模板中使用了count或for_each则会返回index。如果index出现，则resource_name + index可以作为该资源的一种标识  如果用户在模板中使用count，则index为从0开始的数字  以HCL格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[0]`和`huaweicloud_vpc.my_hello_world_vpc[1]`标识两个资源  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   count = 2   name = \"test_vpc\" } ```  以json格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[0]`和`huaweicloud_vpc.my_hello_world_vpc[1]`标识两个资源  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\",         \"count\": 2       }     }   } } ```  如果用户在模板中使用for_each，则index为用户自定义的字符串  以HCL格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[\"vpc1\"]`和`huaweicloud_vpc.my_hello_world_vpc[\"vpc2\"]`标识两个资源  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   for_each = {     \"vpc1\" = \"test_vpc\"     \"vpc2\" = \"test_vpc\"   }   name = each.value } ```  以json格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[\"vpc1\"]`和`huaweicloud_vpc.my_hello_world_vpc[\"vpc2\"]`标识两个资源  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"for_each\": {           \"vpc1\": \"test_vpc\",           \"vpc2\": \"test_vpc\"         }         \"name\": \"${each.value}\"       }     }   } } ```

        :return: The index of this ItemsResponse.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this ItemsResponse.

        资源的索引，如果用户在模板中使用了count或for_each则会返回index。如果index出现，则resource_name + index可以作为该资源的一种标识  如果用户在模板中使用count，则index为从0开始的数字  以HCL格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[0]`和`huaweicloud_vpc.my_hello_world_vpc[1]`标识两个资源  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   count = 2   name = \"test_vpc\" } ```  以json格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[0]`和`huaweicloud_vpc.my_hello_world_vpc[1]`标识两个资源  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\",         \"count\": 2       }     }   } } ```  如果用户在模板中使用for_each，则index为用户自定义的字符串  以HCL格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[\"vpc1\"]`和`huaweicloud_vpc.my_hello_world_vpc[\"vpc2\"]`标识两个资源  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   for_each = {     \"vpc1\" = \"test_vpc\"     \"vpc2\" = \"test_vpc\"   }   name = each.value } ```  以json格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[\"vpc1\"]`和`huaweicloud_vpc.my_hello_world_vpc[\"vpc2\"]`标识两个资源  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"for_each\": {           \"vpc1\": \"test_vpc\",           \"vpc2\": \"test_vpc\"         }         \"name\": \"${each.value}\"       }     }   } } ```

        :param index: The index of this ItemsResponse.
        :type index: str
        """
        self._index = index

    @property
    def module_address(self):
        r"""Gets the module_address of this ItemsResponse.

        该资源的模块地址

        :return: The module_address of this ItemsResponse.
        :rtype: str
        """
        return self._module_address

    @module_address.setter
    def module_address(self, module_address):
        r"""Sets the module_address of this ItemsResponse.

        该资源的模块地址

        :param module_address: The module_address of this ItemsResponse.
        :type module_address: str
        """
        self._module_address = module_address

    @property
    def supported(self):
        r"""Gets the supported of this ItemsResponse.

        该资源或该资源当前所给予的参数是否支持进行询价

        :return: The supported of this ItemsResponse.
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        r"""Sets the supported of this ItemsResponse.

        该资源或该资源当前所给予的参数是否支持进行询价

        :param supported: The supported of this ItemsResponse.
        :type supported: bool
        """
        self._supported = supported

    @property
    def unsupported_message(self):
        r"""Gets the unsupported_message of this ItemsResponse.

        该资源不支持询价的具体原因

        :return: The unsupported_message of this ItemsResponse.
        :rtype: str
        """
        return self._unsupported_message

    @unsupported_message.setter
    def unsupported_message(self, unsupported_message):
        r"""Sets the unsupported_message of this ItemsResponse.

        该资源不支持询价的具体原因

        :param unsupported_message: The unsupported_message of this ItemsResponse.
        :type unsupported_message: str
        """
        self._unsupported_message = unsupported_message

    @property
    def resource_price(self):
        r"""Gets the resource_price of this ItemsResponse.

        该资源的询价信息  如果该资源支持包周期计费或按需计费，或者该资源为免费资源，则返回该字段；如果该资源不支持询价，则不返回该字段。

        :return: The resource_price of this ItemsResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.ResourcePriceResponse`]
        """
        return self._resource_price

    @resource_price.setter
    def resource_price(self, resource_price):
        r"""Sets the resource_price of this ItemsResponse.

        该资源的询价信息  如果该资源支持包周期计费或按需计费，或者该资源为免费资源，则返回该字段；如果该资源不支持询价，则不返回该字段。

        :param resource_price: The resource_price of this ItemsResponse.
        :type resource_price: list[:class:`huaweicloudsdkaos.v1.ResourcePriceResponse`]
        """
        self._resource_price = resource_price

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
        if not isinstance(other, ItemsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
