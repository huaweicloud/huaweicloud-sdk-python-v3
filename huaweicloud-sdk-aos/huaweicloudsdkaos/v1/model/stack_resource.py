# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StackResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'physical_resource_id': 'str',
        'physical_resource_name': 'str',
        'logical_resource_name': 'str',
        'logical_resource_type': 'str',
        'index_key': 'str',
        'resource_status': 'str',
        'status_message': 'str',
        'resource_attributes': 'list[ResourceAttribute]'
    }

    attribute_map = {
        'physical_resource_id': 'physical_resource_id',
        'physical_resource_name': 'physical_resource_name',
        'logical_resource_name': 'logical_resource_name',
        'logical_resource_type': 'logical_resource_type',
        'index_key': 'index_key',
        'resource_status': 'resource_status',
        'status_message': 'status_message',
        'resource_attributes': 'resource_attributes'
    }

    def __init__(self, physical_resource_id=None, physical_resource_name=None, logical_resource_name=None, logical_resource_type=None, index_key=None, resource_status=None, status_message=None, resource_attributes=None):
        r"""StackResource

        The model defined in huaweicloud sdk

        :param physical_resource_id: 资源的物理id，由该资源的provider、云服务或其他服务提供方在资源部署的时候生成  注：与physical相关的参数可以在模板以外的地方，作为该资源的一种标识
        :type physical_resource_id: str
        :param physical_resource_name: 资源的物理名称，由该资源的provider、云服务或其他服务提供方在资源部署的时候定义  注：与physical相关的参数可以在模板以外的地方，作为该资源的一种标识
        :type physical_resource_name: str
        :param logical_resource_name: 资源的逻辑名称，由用户在模板中定义  注：与 logical 相关的参数仅仅在模板内部，作为该资源的一种标识  以HCL格式的模板为例，logical_resource_name 为 my_hello_world_vpc  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   name &#x3D; \&quot;test_vpc\&quot; } &#x60;&#x60;&#x60;  以json格式的模板为例，logical_resource_name 为 my_hello_world_vpc  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;name\&quot;: \&quot;test_vpc\&quot;       }     }   } } &#x60;&#x60;&#x60;
        :type logical_resource_name: str
        :param logical_resource_type: 资源的类型  注：与 logical 相关的参数仅仅在模板内部，作为该资源的一种标识  以HCL格式的模板为例，logical_resource_type 为 huaweicloud_vpc  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   name &#x3D; \&quot;test_vpc\&quot; } &#x60;&#x60;&#x60;  以json格式的模板为例，logical_resource_type 为 huaweicloud_vpc  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;name\&quot;: \&quot;test_vpc\&quot;       }     }   } } &#x60;&#x60;&#x60;
        :type logical_resource_type: str
        :param index_key: 资源的索引，如果用户在模板中使用了count或for_each则会返回index_key。如果index_key出现，则logical_resource_name + index_key可以作为该资源的一种标识  如果用户在模板中使用count，则index_key为从0开始的数字  以HCL格式的模板为例，用户在模板中可以通过&#x60;huaweicloud_vpc.my_hello_world_vpc[0]&#x60;和&#x60;huaweicloud_vpc.my_hello_world_vpc[1]&#x60;标识两个资源  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   count &#x3D; 2   name &#x3D; \&quot;test_vpc\&quot; } &#x60;&#x60;&#x60;  以json格式的模板为例，用户在模板中可以通过&#x60;huaweicloud_vpc.my_hello_world_vpc[0]&#x60;和&#x60;huaweicloud_vpc.my_hello_world_vpc[1]&#x60;标识两个资源  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;name\&quot;: \&quot;test_vpc\&quot;,         \&quot;count\&quot;: 2       }     }   } } &#x60;&#x60;&#x60;  如果用户在模板中使用for_each，则index_key为用户自定义的字符串  以HCL格式的模板为例，用户在模板中可以通过&#x60;huaweicloud_vpc.my_hello_world_vpc[\&quot;vpc1\&quot;]&#x60;和&#x60;huaweicloud_vpc.my_hello_world_vpc[\&quot;vpc2\&quot;]&#x60;标识两个资源  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   for_each &#x3D; {     \&quot;vpc1\&quot; &#x3D; \&quot;test_vpc\&quot;     \&quot;vpc2\&quot; &#x3D; \&quot;test_vpc\&quot;   }   name &#x3D; each.value } &#x60;&#x60;&#x60;  以json格式的模板为例，用户在模板中可以通过&#x60;huaweicloud_vpc.my_hello_world_vpc[\&quot;vpc1\&quot;]&#x60;和&#x60;huaweicloud_vpc.my_hello_world_vpc[\&quot;vpc2\&quot;]&#x60;标识两个资源  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;for_each\&quot;: {           \&quot;vpc1\&quot;: \&quot;test_vpc\&quot;,           \&quot;vpc2\&quot;: \&quot;test_vpc\&quot;         }         \&quot;name\&quot;: \&quot;${each.value}\&quot;       }     }   } } &#x60;&#x60;&#x60;
        :type index_key: str
        :param resource_status: 资源的状态 * &#x60;CREATION_IN_PROGRESS&#x60; - 正在生成 * &#x60;CREATION_FAILED&#x60;      - 生成失败 * &#x60;CREATION_COMPLETE&#x60;    - 生成完成 * &#x60;DELETION_IN_PROGRESS&#x60; - 正在删除 * &#x60;DELETION_FAILED&#x60;      - 删除失败 * &#x60;DELETION_COMPLETE&#x60;    - 已经删除 * &#x60;UPDATE_IN_PROGRESS&#x60;   - 正在更新。此处的更新特指非替换式更新，如果是替换式更新，则使用CREATION后DELETION * &#x60;UPDATE_FAILED&#x60;        - 更新失败。此处的更新特指非替换式更新，如果是替换式更新，则使用CREATION后DELETION * &#x60;UPDATE_COMPLETE&#x60;      - 更新完成。此处的更新特指非替换式更新，如果是替换式更新，则使用CREATION后DELETION
        :type resource_status: str
        :param status_message: 当该资源状态为任意失败状态（即以 &#x60;FAILED&#x60; 结尾时），将会展示简要的错误信息总结以供debug
        :type status_message: str
        :param resource_attributes: 资源属性列表
        :type resource_attributes: list[:class:`huaweicloudsdkaos.v1.ResourceAttribute`]
        """
        
        

        self._physical_resource_id = None
        self._physical_resource_name = None
        self._logical_resource_name = None
        self._logical_resource_type = None
        self._index_key = None
        self._resource_status = None
        self._status_message = None
        self._resource_attributes = None
        self.discriminator = None

        if physical_resource_id is not None:
            self.physical_resource_id = physical_resource_id
        if physical_resource_name is not None:
            self.physical_resource_name = physical_resource_name
        if logical_resource_name is not None:
            self.logical_resource_name = logical_resource_name
        if logical_resource_type is not None:
            self.logical_resource_type = logical_resource_type
        if index_key is not None:
            self.index_key = index_key
        if resource_status is not None:
            self.resource_status = resource_status
        if status_message is not None:
            self.status_message = status_message
        if resource_attributes is not None:
            self.resource_attributes = resource_attributes

    @property
    def physical_resource_id(self):
        r"""Gets the physical_resource_id of this StackResource.

        资源的物理id，由该资源的provider、云服务或其他服务提供方在资源部署的时候生成  注：与physical相关的参数可以在模板以外的地方，作为该资源的一种标识

        :return: The physical_resource_id of this StackResource.
        :rtype: str
        """
        return self._physical_resource_id

    @physical_resource_id.setter
    def physical_resource_id(self, physical_resource_id):
        r"""Sets the physical_resource_id of this StackResource.

        资源的物理id，由该资源的provider、云服务或其他服务提供方在资源部署的时候生成  注：与physical相关的参数可以在模板以外的地方，作为该资源的一种标识

        :param physical_resource_id: The physical_resource_id of this StackResource.
        :type physical_resource_id: str
        """
        self._physical_resource_id = physical_resource_id

    @property
    def physical_resource_name(self):
        r"""Gets the physical_resource_name of this StackResource.

        资源的物理名称，由该资源的provider、云服务或其他服务提供方在资源部署的时候定义  注：与physical相关的参数可以在模板以外的地方，作为该资源的一种标识

        :return: The physical_resource_name of this StackResource.
        :rtype: str
        """
        return self._physical_resource_name

    @physical_resource_name.setter
    def physical_resource_name(self, physical_resource_name):
        r"""Sets the physical_resource_name of this StackResource.

        资源的物理名称，由该资源的provider、云服务或其他服务提供方在资源部署的时候定义  注：与physical相关的参数可以在模板以外的地方，作为该资源的一种标识

        :param physical_resource_name: The physical_resource_name of this StackResource.
        :type physical_resource_name: str
        """
        self._physical_resource_name = physical_resource_name

    @property
    def logical_resource_name(self):
        r"""Gets the logical_resource_name of this StackResource.

        资源的逻辑名称，由用户在模板中定义  注：与 logical 相关的参数仅仅在模板内部，作为该资源的一种标识  以HCL格式的模板为例，logical_resource_name 为 my_hello_world_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，logical_resource_name 为 my_hello_world_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :return: The logical_resource_name of this StackResource.
        :rtype: str
        """
        return self._logical_resource_name

    @logical_resource_name.setter
    def logical_resource_name(self, logical_resource_name):
        r"""Sets the logical_resource_name of this StackResource.

        资源的逻辑名称，由用户在模板中定义  注：与 logical 相关的参数仅仅在模板内部，作为该资源的一种标识  以HCL格式的模板为例，logical_resource_name 为 my_hello_world_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，logical_resource_name 为 my_hello_world_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :param logical_resource_name: The logical_resource_name of this StackResource.
        :type logical_resource_name: str
        """
        self._logical_resource_name = logical_resource_name

    @property
    def logical_resource_type(self):
        r"""Gets the logical_resource_type of this StackResource.

        资源的类型  注：与 logical 相关的参数仅仅在模板内部，作为该资源的一种标识  以HCL格式的模板为例，logical_resource_type 为 huaweicloud_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，logical_resource_type 为 huaweicloud_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :return: The logical_resource_type of this StackResource.
        :rtype: str
        """
        return self._logical_resource_type

    @logical_resource_type.setter
    def logical_resource_type(self, logical_resource_type):
        r"""Sets the logical_resource_type of this StackResource.

        资源的类型  注：与 logical 相关的参数仅仅在模板内部，作为该资源的一种标识  以HCL格式的模板为例，logical_resource_type 为 huaweicloud_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，logical_resource_type 为 huaweicloud_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :param logical_resource_type: The logical_resource_type of this StackResource.
        :type logical_resource_type: str
        """
        self._logical_resource_type = logical_resource_type

    @property
    def index_key(self):
        r"""Gets the index_key of this StackResource.

        资源的索引，如果用户在模板中使用了count或for_each则会返回index_key。如果index_key出现，则logical_resource_name + index_key可以作为该资源的一种标识  如果用户在模板中使用count，则index_key为从0开始的数字  以HCL格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[0]`和`huaweicloud_vpc.my_hello_world_vpc[1]`标识两个资源  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   count = 2   name = \"test_vpc\" } ```  以json格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[0]`和`huaweicloud_vpc.my_hello_world_vpc[1]`标识两个资源  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\",         \"count\": 2       }     }   } } ```  如果用户在模板中使用for_each，则index_key为用户自定义的字符串  以HCL格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[\"vpc1\"]`和`huaweicloud_vpc.my_hello_world_vpc[\"vpc2\"]`标识两个资源  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   for_each = {     \"vpc1\" = \"test_vpc\"     \"vpc2\" = \"test_vpc\"   }   name = each.value } ```  以json格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[\"vpc1\"]`和`huaweicloud_vpc.my_hello_world_vpc[\"vpc2\"]`标识两个资源  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"for_each\": {           \"vpc1\": \"test_vpc\",           \"vpc2\": \"test_vpc\"         }         \"name\": \"${each.value}\"       }     }   } } ```

        :return: The index_key of this StackResource.
        :rtype: str
        """
        return self._index_key

    @index_key.setter
    def index_key(self, index_key):
        r"""Sets the index_key of this StackResource.

        资源的索引，如果用户在模板中使用了count或for_each则会返回index_key。如果index_key出现，则logical_resource_name + index_key可以作为该资源的一种标识  如果用户在模板中使用count，则index_key为从0开始的数字  以HCL格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[0]`和`huaweicloud_vpc.my_hello_world_vpc[1]`标识两个资源  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   count = 2   name = \"test_vpc\" } ```  以json格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[0]`和`huaweicloud_vpc.my_hello_world_vpc[1]`标识两个资源  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\",         \"count\": 2       }     }   } } ```  如果用户在模板中使用for_each，则index_key为用户自定义的字符串  以HCL格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[\"vpc1\"]`和`huaweicloud_vpc.my_hello_world_vpc[\"vpc2\"]`标识两个资源  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   for_each = {     \"vpc1\" = \"test_vpc\"     \"vpc2\" = \"test_vpc\"   }   name = each.value } ```  以json格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[\"vpc1\"]`和`huaweicloud_vpc.my_hello_world_vpc[\"vpc2\"]`标识两个资源  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"for_each\": {           \"vpc1\": \"test_vpc\",           \"vpc2\": \"test_vpc\"         }         \"name\": \"${each.value}\"       }     }   } } ```

        :param index_key: The index_key of this StackResource.
        :type index_key: str
        """
        self._index_key = index_key

    @property
    def resource_status(self):
        r"""Gets the resource_status of this StackResource.

        资源的状态 * `CREATION_IN_PROGRESS` - 正在生成 * `CREATION_FAILED`      - 生成失败 * `CREATION_COMPLETE`    - 生成完成 * `DELETION_IN_PROGRESS` - 正在删除 * `DELETION_FAILED`      - 删除失败 * `DELETION_COMPLETE`    - 已经删除 * `UPDATE_IN_PROGRESS`   - 正在更新。此处的更新特指非替换式更新，如果是替换式更新，则使用CREATION后DELETION * `UPDATE_FAILED`        - 更新失败。此处的更新特指非替换式更新，如果是替换式更新，则使用CREATION后DELETION * `UPDATE_COMPLETE`      - 更新完成。此处的更新特指非替换式更新，如果是替换式更新，则使用CREATION后DELETION

        :return: The resource_status of this StackResource.
        :rtype: str
        """
        return self._resource_status

    @resource_status.setter
    def resource_status(self, resource_status):
        r"""Sets the resource_status of this StackResource.

        资源的状态 * `CREATION_IN_PROGRESS` - 正在生成 * `CREATION_FAILED`      - 生成失败 * `CREATION_COMPLETE`    - 生成完成 * `DELETION_IN_PROGRESS` - 正在删除 * `DELETION_FAILED`      - 删除失败 * `DELETION_COMPLETE`    - 已经删除 * `UPDATE_IN_PROGRESS`   - 正在更新。此处的更新特指非替换式更新，如果是替换式更新，则使用CREATION后DELETION * `UPDATE_FAILED`        - 更新失败。此处的更新特指非替换式更新，如果是替换式更新，则使用CREATION后DELETION * `UPDATE_COMPLETE`      - 更新完成。此处的更新特指非替换式更新，如果是替换式更新，则使用CREATION后DELETION

        :param resource_status: The resource_status of this StackResource.
        :type resource_status: str
        """
        self._resource_status = resource_status

    @property
    def status_message(self):
        r"""Gets the status_message of this StackResource.

        当该资源状态为任意失败状态（即以 `FAILED` 结尾时），将会展示简要的错误信息总结以供debug

        :return: The status_message of this StackResource.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        r"""Sets the status_message of this StackResource.

        当该资源状态为任意失败状态（即以 `FAILED` 结尾时），将会展示简要的错误信息总结以供debug

        :param status_message: The status_message of this StackResource.
        :type status_message: str
        """
        self._status_message = status_message

    @property
    def resource_attributes(self):
        r"""Gets the resource_attributes of this StackResource.

        资源属性列表

        :return: The resource_attributes of this StackResource.
        :rtype: list[:class:`huaweicloudsdkaos.v1.ResourceAttribute`]
        """
        return self._resource_attributes

    @resource_attributes.setter
    def resource_attributes(self, resource_attributes):
        r"""Sets the resource_attributes of this StackResource.

        资源属性列表

        :param resource_attributes: The resource_attributes of this StackResource.
        :type resource_attributes: list[:class:`huaweicloudsdkaos.v1.ResourceAttribute`]
        """
        self._resource_attributes = resource_attributes

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
        if not isinstance(other, StackResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
