# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StackEvent:

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
        'resource_id_key': 'str',
        'resource_id_value': 'str',
        'resource_key': 'str',
        'time': 'str',
        'event_type': 'str',
        'event_message': 'str',
        'elapsed_seconds': 'int'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_name': 'resource_name',
        'resource_id_key': 'resource_id_key',
        'resource_id_value': 'resource_id_value',
        'resource_key': 'resource_key',
        'time': 'time',
        'event_type': 'event_type',
        'event_message': 'event_message',
        'elapsed_seconds': 'elapsed_seconds'
    }

    def __init__(self, resource_type=None, resource_name=None, resource_id_key=None, resource_id_value=None, resource_key=None, time=None, event_type=None, event_message=None, elapsed_seconds=None):
        r"""StackEvent

        The model defined in huaweicloud sdk

        :param resource_type: 资源的类型  以HCL格式的模板为例，resource_type 为 huaweicloud_vpc  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   name &#x3D; \&quot;test_vpc\&quot; } &#x60;&#x60;&#x60;  以json格式的模板为例，resource_type 为 huaweicloud_vpc  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;name\&quot;: \&quot;test_vpc\&quot;       }     }   } } &#x60;&#x60;&#x60;
        :type resource_type: str
        :param resource_name: 资源的名称，默认为资源的逻辑名称  以HCL格式的模板为例，resource_name 为 my_hello_world_vpc  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   name &#x3D; \&quot;test_vpc\&quot; } &#x60;&#x60;&#x60;  以json格式的模板为例，resource_name 为 my_hello_world_vpc  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;name\&quot;: \&quot;test_vpc\&quot;       }     }   } } &#x60;&#x60;&#x60;
        :type resource_name: str
        :param resource_id_key: 资源id的名称，即对应资源作为id使用的值的名称，当资源未创建的时候，不返回resource_id_key 此id由provider定义，因此不同的provider可能遵循了不同的命名规则，具体的命名规则请与provider开发者确认或阅读provider文档
        :type resource_id_key: str
        :param resource_id_value: 资源id的值，即对应资源作为id使用的值，当资源未创建的时候，不返回resource_id_value
        :type resource_id_value: str
        :param resource_key: 资源键，如果用户在模板中使用了count或for_each则会返回resource_key  如果用户在模板中使用count，则resource_key为从0开始的数字  以HCL格式的模板为例，模板中count为2，意味着将会生成两个资源，对应的resource_key分别为0和1  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   count &#x3D; 2   name &#x3D; \&quot;test_vpc\&quot; } &#x60;&#x60;&#x60;  以json格式的模板为例，模板中count为2，意味着将会生成两个资源，对应的resource_key分别为0和1  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;name\&quot;: \&quot;test_vpc\&quot;,         \&quot;count\&quot;: 2       }     }   } } &#x60;&#x60;&#x60;  如果用户在模板中使用for_each，则resource_key为用户自定义的字符串  以HCL格式的模板为例，resource_key分别为vpc1和vpc2  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   for_each &#x3D; {     \&quot;vpc1\&quot; &#x3D; \&quot;test_vpc\&quot;     \&quot;vpc2\&quot; &#x3D; \&quot;test_vpc\&quot;   }   name &#x3D; each.value } &#x60;&#x60;&#x60;  以json格式的模板为例，resource_key分别为vpc1和vpc2  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;for_each\&quot;: {           \&quot;vpc1\&quot;: \&quot;test_vpc\&quot;,           \&quot;vpc2\&quot;: \&quot;test_vpc\&quot;         }         \&quot;name\&quot;: \&quot;${each.value}\&quot;       }     }   } } &#x60;&#x60;&#x60;
        :type resource_key: str
        :param time: 事件发生的时间 格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z
        :type time: str
        :param event_type: 此次事件的类型 * &#x60;LOG&#x60; - 记录状态信息，比如当前状态，目标状态等。 * &#x60;ERROR&#x60; - 记录失败信息 * &#x60;DRIFT&#x60; - 记录资源偏移信息 * &#x60;SUMMARY&#x60; - 记录资源变更结果总结 * &#x60;CREATION_IN_PROGRESS&#x60; - 正在生成 * &#x60;CREATION_FAILED&#x60; - 生成失败 * &#x60;CREATION_COMPLETE&#x60; - 生成完成 * &#x60;DELETION_IN_PROGRESS&#x60; - 正在删除 * &#x60;DELETION_FAILED&#x60; - 删除失败 * &#x60;DELETION_COMPLETE&#x60; - 已经删除 * &#x60;UPDATE_IN_PROGRESS&#x60; - 正在更新。此处的更新特指非替换式更新，如果是替换式更新，则是DELETION后CREATION，或者CREATION后DELETION，具体以何种行为进行替换式更新由Provider定义。 * &#x60;UPDATE_FAILED&#x60; - 更新失败。此处的更新特指非替换式更新，如果是替换式更新，则是DELETION后CREATION，或者CREATION后DELETION，具体以何种行为进行替换式更新由Provider定义。 * &#x60;UPDATE_COMPLETE&#x60; - 更新完成。此处的更新特指非替换式更新，如果是替换式更新，则是DELETION后CREATION，或者CREATION后DELETION，具体以何种行为进行替换式更新由Provider定义。
        :type event_type: str
        :param event_message: 该资源栈事件对应的详细信息
        :type event_message: str
        :param elapsed_seconds: 此事件执行所花的时间，以秒为单位
        :type elapsed_seconds: int
        """
        
        

        self._resource_type = None
        self._resource_name = None
        self._resource_id_key = None
        self._resource_id_value = None
        self._resource_key = None
        self._time = None
        self._event_type = None
        self._event_message = None
        self._elapsed_seconds = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_id_key is not None:
            self.resource_id_key = resource_id_key
        if resource_id_value is not None:
            self.resource_id_value = resource_id_value
        if resource_key is not None:
            self.resource_key = resource_key
        if time is not None:
            self.time = time
        if event_type is not None:
            self.event_type = event_type
        if event_message is not None:
            self.event_message = event_message
        if elapsed_seconds is not None:
            self.elapsed_seconds = elapsed_seconds

    @property
    def resource_type(self):
        r"""Gets the resource_type of this StackEvent.

        资源的类型  以HCL格式的模板为例，resource_type 为 huaweicloud_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，resource_type 为 huaweicloud_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :return: The resource_type of this StackEvent.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this StackEvent.

        资源的类型  以HCL格式的模板为例，resource_type 为 huaweicloud_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，resource_type 为 huaweicloud_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :param resource_type: The resource_type of this StackEvent.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        r"""Gets the resource_name of this StackEvent.

        资源的名称，默认为资源的逻辑名称  以HCL格式的模板为例，resource_name 为 my_hello_world_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，resource_name 为 my_hello_world_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :return: The resource_name of this StackEvent.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this StackEvent.

        资源的名称，默认为资源的逻辑名称  以HCL格式的模板为例，resource_name 为 my_hello_world_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，resource_name 为 my_hello_world_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :param resource_name: The resource_name of this StackEvent.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_id_key(self):
        r"""Gets the resource_id_key of this StackEvent.

        资源id的名称，即对应资源作为id使用的值的名称，当资源未创建的时候，不返回resource_id_key 此id由provider定义，因此不同的provider可能遵循了不同的命名规则，具体的命名规则请与provider开发者确认或阅读provider文档

        :return: The resource_id_key of this StackEvent.
        :rtype: str
        """
        return self._resource_id_key

    @resource_id_key.setter
    def resource_id_key(self, resource_id_key):
        r"""Sets the resource_id_key of this StackEvent.

        资源id的名称，即对应资源作为id使用的值的名称，当资源未创建的时候，不返回resource_id_key 此id由provider定义，因此不同的provider可能遵循了不同的命名规则，具体的命名规则请与provider开发者确认或阅读provider文档

        :param resource_id_key: The resource_id_key of this StackEvent.
        :type resource_id_key: str
        """
        self._resource_id_key = resource_id_key

    @property
    def resource_id_value(self):
        r"""Gets the resource_id_value of this StackEvent.

        资源id的值，即对应资源作为id使用的值，当资源未创建的时候，不返回resource_id_value

        :return: The resource_id_value of this StackEvent.
        :rtype: str
        """
        return self._resource_id_value

    @resource_id_value.setter
    def resource_id_value(self, resource_id_value):
        r"""Sets the resource_id_value of this StackEvent.

        资源id的值，即对应资源作为id使用的值，当资源未创建的时候，不返回resource_id_value

        :param resource_id_value: The resource_id_value of this StackEvent.
        :type resource_id_value: str
        """
        self._resource_id_value = resource_id_value

    @property
    def resource_key(self):
        r"""Gets the resource_key of this StackEvent.

        资源键，如果用户在模板中使用了count或for_each则会返回resource_key  如果用户在模板中使用count，则resource_key为从0开始的数字  以HCL格式的模板为例，模板中count为2，意味着将会生成两个资源，对应的resource_key分别为0和1  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   count = 2   name = \"test_vpc\" } ```  以json格式的模板为例，模板中count为2，意味着将会生成两个资源，对应的resource_key分别为0和1  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\",         \"count\": 2       }     }   } } ```  如果用户在模板中使用for_each，则resource_key为用户自定义的字符串  以HCL格式的模板为例，resource_key分别为vpc1和vpc2  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   for_each = {     \"vpc1\" = \"test_vpc\"     \"vpc2\" = \"test_vpc\"   }   name = each.value } ```  以json格式的模板为例，resource_key分别为vpc1和vpc2  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"for_each\": {           \"vpc1\": \"test_vpc\",           \"vpc2\": \"test_vpc\"         }         \"name\": \"${each.value}\"       }     }   } } ```

        :return: The resource_key of this StackEvent.
        :rtype: str
        """
        return self._resource_key

    @resource_key.setter
    def resource_key(self, resource_key):
        r"""Sets the resource_key of this StackEvent.

        资源键，如果用户在模板中使用了count或for_each则会返回resource_key  如果用户在模板中使用count，则resource_key为从0开始的数字  以HCL格式的模板为例，模板中count为2，意味着将会生成两个资源，对应的resource_key分别为0和1  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   count = 2   name = \"test_vpc\" } ```  以json格式的模板为例，模板中count为2，意味着将会生成两个资源，对应的resource_key分别为0和1  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\",         \"count\": 2       }     }   } } ```  如果用户在模板中使用for_each，则resource_key为用户自定义的字符串  以HCL格式的模板为例，resource_key分别为vpc1和vpc2  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   for_each = {     \"vpc1\" = \"test_vpc\"     \"vpc2\" = \"test_vpc\"   }   name = each.value } ```  以json格式的模板为例，resource_key分别为vpc1和vpc2  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"for_each\": {           \"vpc1\": \"test_vpc\",           \"vpc2\": \"test_vpc\"         }         \"name\": \"${each.value}\"       }     }   } } ```

        :param resource_key: The resource_key of this StackEvent.
        :type resource_key: str
        """
        self._resource_key = resource_key

    @property
    def time(self):
        r"""Gets the time of this StackEvent.

        事件发生的时间 格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :return: The time of this StackEvent.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this StackEvent.

        事件发生的时间 格式遵循RFC3339，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z

        :param time: The time of this StackEvent.
        :type time: str
        """
        self._time = time

    @property
    def event_type(self):
        r"""Gets the event_type of this StackEvent.

        此次事件的类型 * `LOG` - 记录状态信息，比如当前状态，目标状态等。 * `ERROR` - 记录失败信息 * `DRIFT` - 记录资源偏移信息 * `SUMMARY` - 记录资源变更结果总结 * `CREATION_IN_PROGRESS` - 正在生成 * `CREATION_FAILED` - 生成失败 * `CREATION_COMPLETE` - 生成完成 * `DELETION_IN_PROGRESS` - 正在删除 * `DELETION_FAILED` - 删除失败 * `DELETION_COMPLETE` - 已经删除 * `UPDATE_IN_PROGRESS` - 正在更新。此处的更新特指非替换式更新，如果是替换式更新，则是DELETION后CREATION，或者CREATION后DELETION，具体以何种行为进行替换式更新由Provider定义。 * `UPDATE_FAILED` - 更新失败。此处的更新特指非替换式更新，如果是替换式更新，则是DELETION后CREATION，或者CREATION后DELETION，具体以何种行为进行替换式更新由Provider定义。 * `UPDATE_COMPLETE` - 更新完成。此处的更新特指非替换式更新，如果是替换式更新，则是DELETION后CREATION，或者CREATION后DELETION，具体以何种行为进行替换式更新由Provider定义。

        :return: The event_type of this StackEvent.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this StackEvent.

        此次事件的类型 * `LOG` - 记录状态信息，比如当前状态，目标状态等。 * `ERROR` - 记录失败信息 * `DRIFT` - 记录资源偏移信息 * `SUMMARY` - 记录资源变更结果总结 * `CREATION_IN_PROGRESS` - 正在生成 * `CREATION_FAILED` - 生成失败 * `CREATION_COMPLETE` - 生成完成 * `DELETION_IN_PROGRESS` - 正在删除 * `DELETION_FAILED` - 删除失败 * `DELETION_COMPLETE` - 已经删除 * `UPDATE_IN_PROGRESS` - 正在更新。此处的更新特指非替换式更新，如果是替换式更新，则是DELETION后CREATION，或者CREATION后DELETION，具体以何种行为进行替换式更新由Provider定义。 * `UPDATE_FAILED` - 更新失败。此处的更新特指非替换式更新，如果是替换式更新，则是DELETION后CREATION，或者CREATION后DELETION，具体以何种行为进行替换式更新由Provider定义。 * `UPDATE_COMPLETE` - 更新完成。此处的更新特指非替换式更新，如果是替换式更新，则是DELETION后CREATION，或者CREATION后DELETION，具体以何种行为进行替换式更新由Provider定义。

        :param event_type: The event_type of this StackEvent.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_message(self):
        r"""Gets the event_message of this StackEvent.

        该资源栈事件对应的详细信息

        :return: The event_message of this StackEvent.
        :rtype: str
        """
        return self._event_message

    @event_message.setter
    def event_message(self, event_message):
        r"""Sets the event_message of this StackEvent.

        该资源栈事件对应的详细信息

        :param event_message: The event_message of this StackEvent.
        :type event_message: str
        """
        self._event_message = event_message

    @property
    def elapsed_seconds(self):
        r"""Gets the elapsed_seconds of this StackEvent.

        此事件执行所花的时间，以秒为单位

        :return: The elapsed_seconds of this StackEvent.
        :rtype: int
        """
        return self._elapsed_seconds

    @elapsed_seconds.setter
    def elapsed_seconds(self, elapsed_seconds):
        r"""Sets the elapsed_seconds of this StackEvent.

        此事件执行所花的时间，以秒为单位

        :param elapsed_seconds: The elapsed_seconds of this StackEvent.
        :type elapsed_seconds: int
        """
        self._elapsed_seconds = elapsed_seconds

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
        if not isinstance(other, StackEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
