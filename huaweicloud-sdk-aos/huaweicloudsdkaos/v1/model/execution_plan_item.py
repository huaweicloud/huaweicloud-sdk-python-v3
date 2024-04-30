# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionPlanItem:

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
        'action': 'str',
        'action_reason': 'str',
        'provider_name': 'str',
        'mode': 'str',
        'drifted': 'bool',
        'imported': 'bool',
        'resource_id': 'str',
        'attributes': 'list[ExecutionPlanDiffAttribute]'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_name': 'resource_name',
        'index': 'index',
        'action': 'action',
        'action_reason': 'action_reason',
        'provider_name': 'provider_name',
        'mode': 'mode',
        'drifted': 'drifted',
        'imported': 'imported',
        'resource_id': 'resource_id',
        'attributes': 'attributes'
    }

    def __init__(self, resource_type=None, resource_name=None, index=None, action=None, action_reason=None, provider_name=None, mode=None, drifted=None, imported=None, resource_id=None, attributes=None):
        """ExecutionPlanItem

        The model defined in huaweicloud sdk

        :param resource_type: 资源的类型  以HCL格式的模板为例，resource_type 为 huaweicloud_vpc  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   name &#x3D; \&quot;test_vpc\&quot; } &#x60;&#x60;&#x60;  以json格式的模板为例，resource_type 为 huaweicloud_vpc  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;name\&quot;: \&quot;test_vpc\&quot;       }     }   } } &#x60;&#x60;&#x60;
        :type resource_type: str
        :param resource_name: 资源的名称，默认为资源的逻辑名称  以HCL格式的模板为例，resource_name 为 my_hello_world_vpc  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   name &#x3D; \&quot;test_vpc\&quot; } &#x60;&#x60;&#x60;  以json格式的模板为例，resource_name 为 my_hello_world_vpc  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;name\&quot;: \&quot;test_vpc\&quot;       }     }   } } &#x60;&#x60;&#x60;
        :type resource_name: str
        :param index: 资源的索引，如果用户在模板中使用了count或for_each则会返回index。如果index出现，则resource_name + index可以作为该资源的一种标识  如果用户在模板中使用count，则index为从0开始的数字  以HCL格式的模板为例，用户在模板中可以通过&#x60;huaweicloud_vpc.my_hello_world_vpc[0]&#x60;和&#x60;huaweicloud_vpc.my_hello_world_vpc[1]&#x60;标识两个资源  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   count &#x3D; 2   name &#x3D; \&quot;test_vpc\&quot; } &#x60;&#x60;&#x60;  以json格式的模板为例，用户在模板中可以通过&#x60;huaweicloud_vpc.my_hello_world_vpc[0]&#x60;和&#x60;huaweicloud_vpc.my_hello_world_vpc[1]&#x60;标识两个资源  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;name\&quot;: \&quot;test_vpc\&quot;,         \&quot;count\&quot;: 2       }     }   } } &#x60;&#x60;&#x60;  如果用户在模板中使用for_each，则index为用户自定义的字符串  以HCL格式的模板为例，用户在模板中可以通过&#x60;huaweicloud_vpc.my_hello_world_vpc[\&quot;vpc1\&quot;]&#x60;和&#x60;huaweicloud_vpc.my_hello_world_vpc[\&quot;vpc2\&quot;]&#x60;标识两个资源  &#x60;&#x60;&#x60;hcl resource \&quot;huaweicloud_vpc\&quot; \&quot;my_hello_world_vpc\&quot; {   for_each &#x3D; {     \&quot;vpc1\&quot; &#x3D; \&quot;test_vpc\&quot;     \&quot;vpc2\&quot; &#x3D; \&quot;test_vpc\&quot;   }   name &#x3D; each.value } &#x60;&#x60;&#x60;  以json格式的模板为例，用户在模板中可以通过&#x60;huaweicloud_vpc.my_hello_world_vpc[\&quot;vpc1\&quot;]&#x60;和&#x60;huaweicloud_vpc.my_hello_world_vpc[\&quot;vpc2\&quot;]&#x60;标识两个资源  &#x60;&#x60;&#x60;json {   \&quot;resource\&quot;: {     \&quot;huaweicloud_vpc\&quot;: {       \&quot;my_hello_world_vpc\&quot;: {         \&quot;for_each\&quot;: {           \&quot;vpc1\&quot;: \&quot;test_vpc\&quot;,           \&quot;vpc2\&quot;: \&quot;test_vpc\&quot;         }         \&quot;name\&quot;: \&quot;${each.value}\&quot;       }     }   } } &#x60;&#x60;&#x60;
        :type index: str
        :param action: 资源变更的类型   * &#x60;ADD&#x60; - 新增资源   * &#x60;ADD_THEN_DELETE&#x60; - 由不可更新的资源返回，先创建新资源，再删除旧资源   * &#x60;DELETE &#x60; - 删除资源   * &#x60;DELETE_THEN_ADD&#x60; - 由不可更新的资源返回，先删除旧资源，再创建新资源   * &#x60;UPDATE&#x60; - 更新资源    * &#x60;NO_OPERATION&#x60; - 仅变更资源的依赖关系，但是对资源本身并无修改的操作
        :type action: str
        :param action_reason: 触发该项目变更的原因，例如用户更新模板；远端删除资源等等
        :type action_reason: str
        :param provider_name: 该项目所属的provider名称。
        :type provider_name: str
        :param mode: 资源模式   * &#x60;DATA&#x60; - 指可以在模板解析期间运行和获取服务端数据的资源类型，不会操作基础设施组件   * &#x60;RESOURCE&#x60; - 指通过模板管理的由服务定义的基础设施组件抽象，可以是物理资源也可以是逻辑资源
        :type mode: str
        :param drifted: 当前资源的变更是否由偏差导致。  偏差，也叫漂移。指的是资源被资源编排服务创建以后，又经历过非资源编排服务触发的修改，如手动修改、调用SDK修改等，使得资源的配置与本服务所记录的资源的配置不一致。这种不一致便称为偏差。  当资源产生偏差以后： * 如果用户试图创建执行计划，则会提示用户产生偏差 * 如果用户直接部署，则偏差有可能被覆盖，资源编排服务只保证资源和模板最终一致。  资源的偏差有两种类型： * 资源定位属性被修改：如果是定位属性被修改，常见于删除后重建，此时资源已经不属于同一个资源。资源编排服务会认为此资源已经被删除，会尝试创建一个新的资源。 * 资源普通属性被修改：如果是普通属性被修改，则资源编排服务依然可以找到资源，但是下次部署会尝试修复偏差，即将资源保持和模板最终一致。  **注：资源编排服务团队极力推荐，如果资源是通过本服务创建的，请一直使用本服务进行维护和更新以确保资源和模板保持一致。建议非紧急事件以外的情况不要手动调整。**
        :type drifted: bool
        :param imported: 当前资源的变更是否是导入的。
        :type imported: bool
        :param resource_id: 资源的物理id，是唯一id，由为该资源提供服务的provider、云服务或其他服务提供方在资源部署的时候生成
        :type resource_id: str
        :param attributes: 执行计划项目中变更的属性，当无属性变更时为空列表。
        :type attributes: list[:class:`huaweicloudsdkaos.v1.ExecutionPlanDiffAttribute`]
        """
        
        

        self._resource_type = None
        self._resource_name = None
        self._index = None
        self._action = None
        self._action_reason = None
        self._provider_name = None
        self._mode = None
        self._drifted = None
        self._imported = None
        self._resource_id = None
        self._attributes = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if resource_name is not None:
            self.resource_name = resource_name
        if index is not None:
            self.index = index
        if action is not None:
            self.action = action
        if action_reason is not None:
            self.action_reason = action_reason
        if provider_name is not None:
            self.provider_name = provider_name
        if mode is not None:
            self.mode = mode
        if drifted is not None:
            self.drifted = drifted
        if imported is not None:
            self.imported = imported
        if resource_id is not None:
            self.resource_id = resource_id
        if attributes is not None:
            self.attributes = attributes

    @property
    def resource_type(self):
        """Gets the resource_type of this ExecutionPlanItem.

        资源的类型  以HCL格式的模板为例，resource_type 为 huaweicloud_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，resource_type 为 huaweicloud_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :return: The resource_type of this ExecutionPlanItem.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ExecutionPlanItem.

        资源的类型  以HCL格式的模板为例，resource_type 为 huaweicloud_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，resource_type 为 huaweicloud_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :param resource_type: The resource_type of this ExecutionPlanItem.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        """Gets the resource_name of this ExecutionPlanItem.

        资源的名称，默认为资源的逻辑名称  以HCL格式的模板为例，resource_name 为 my_hello_world_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，resource_name 为 my_hello_world_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :return: The resource_name of this ExecutionPlanItem.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ExecutionPlanItem.

        资源的名称，默认为资源的逻辑名称  以HCL格式的模板为例，resource_name 为 my_hello_world_vpc  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   name = \"test_vpc\" } ```  以json格式的模板为例，resource_name 为 my_hello_world_vpc  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\"       }     }   } } ```

        :param resource_name: The resource_name of this ExecutionPlanItem.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def index(self):
        """Gets the index of this ExecutionPlanItem.

        资源的索引，如果用户在模板中使用了count或for_each则会返回index。如果index出现，则resource_name + index可以作为该资源的一种标识  如果用户在模板中使用count，则index为从0开始的数字  以HCL格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[0]`和`huaweicloud_vpc.my_hello_world_vpc[1]`标识两个资源  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   count = 2   name = \"test_vpc\" } ```  以json格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[0]`和`huaweicloud_vpc.my_hello_world_vpc[1]`标识两个资源  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\",         \"count\": 2       }     }   } } ```  如果用户在模板中使用for_each，则index为用户自定义的字符串  以HCL格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[\"vpc1\"]`和`huaweicloud_vpc.my_hello_world_vpc[\"vpc2\"]`标识两个资源  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   for_each = {     \"vpc1\" = \"test_vpc\"     \"vpc2\" = \"test_vpc\"   }   name = each.value } ```  以json格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[\"vpc1\"]`和`huaweicloud_vpc.my_hello_world_vpc[\"vpc2\"]`标识两个资源  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"for_each\": {           \"vpc1\": \"test_vpc\",           \"vpc2\": \"test_vpc\"         }         \"name\": \"${each.value}\"       }     }   } } ```

        :return: The index of this ExecutionPlanItem.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ExecutionPlanItem.

        资源的索引，如果用户在模板中使用了count或for_each则会返回index。如果index出现，则resource_name + index可以作为该资源的一种标识  如果用户在模板中使用count，则index为从0开始的数字  以HCL格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[0]`和`huaweicloud_vpc.my_hello_world_vpc[1]`标识两个资源  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   count = 2   name = \"test_vpc\" } ```  以json格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[0]`和`huaweicloud_vpc.my_hello_world_vpc[1]`标识两个资源  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"name\": \"test_vpc\",         \"count\": 2       }     }   } } ```  如果用户在模板中使用for_each，则index为用户自定义的字符串  以HCL格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[\"vpc1\"]`和`huaweicloud_vpc.my_hello_world_vpc[\"vpc2\"]`标识两个资源  ```hcl resource \"huaweicloud_vpc\" \"my_hello_world_vpc\" {   for_each = {     \"vpc1\" = \"test_vpc\"     \"vpc2\" = \"test_vpc\"   }   name = each.value } ```  以json格式的模板为例，用户在模板中可以通过`huaweicloud_vpc.my_hello_world_vpc[\"vpc1\"]`和`huaweicloud_vpc.my_hello_world_vpc[\"vpc2\"]`标识两个资源  ```json {   \"resource\": {     \"huaweicloud_vpc\": {       \"my_hello_world_vpc\": {         \"for_each\": {           \"vpc1\": \"test_vpc\",           \"vpc2\": \"test_vpc\"         }         \"name\": \"${each.value}\"       }     }   } } ```

        :param index: The index of this ExecutionPlanItem.
        :type index: str
        """
        self._index = index

    @property
    def action(self):
        """Gets the action of this ExecutionPlanItem.

        资源变更的类型   * `ADD` - 新增资源   * `ADD_THEN_DELETE` - 由不可更新的资源返回，先创建新资源，再删除旧资源   * `DELETE ` - 删除资源   * `DELETE_THEN_ADD` - 由不可更新的资源返回，先删除旧资源，再创建新资源   * `UPDATE` - 更新资源    * `NO_OPERATION` - 仅变更资源的依赖关系，但是对资源本身并无修改的操作

        :return: The action of this ExecutionPlanItem.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ExecutionPlanItem.

        资源变更的类型   * `ADD` - 新增资源   * `ADD_THEN_DELETE` - 由不可更新的资源返回，先创建新资源，再删除旧资源   * `DELETE ` - 删除资源   * `DELETE_THEN_ADD` - 由不可更新的资源返回，先删除旧资源，再创建新资源   * `UPDATE` - 更新资源    * `NO_OPERATION` - 仅变更资源的依赖关系，但是对资源本身并无修改的操作

        :param action: The action of this ExecutionPlanItem.
        :type action: str
        """
        self._action = action

    @property
    def action_reason(self):
        """Gets the action_reason of this ExecutionPlanItem.

        触发该项目变更的原因，例如用户更新模板；远端删除资源等等

        :return: The action_reason of this ExecutionPlanItem.
        :rtype: str
        """
        return self._action_reason

    @action_reason.setter
    def action_reason(self, action_reason):
        """Sets the action_reason of this ExecutionPlanItem.

        触发该项目变更的原因，例如用户更新模板；远端删除资源等等

        :param action_reason: The action_reason of this ExecutionPlanItem.
        :type action_reason: str
        """
        self._action_reason = action_reason

    @property
    def provider_name(self):
        """Gets the provider_name of this ExecutionPlanItem.

        该项目所属的provider名称。

        :return: The provider_name of this ExecutionPlanItem.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this ExecutionPlanItem.

        该项目所属的provider名称。

        :param provider_name: The provider_name of this ExecutionPlanItem.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def mode(self):
        """Gets the mode of this ExecutionPlanItem.

        资源模式   * `DATA` - 指可以在模板解析期间运行和获取服务端数据的资源类型，不会操作基础设施组件   * `RESOURCE` - 指通过模板管理的由服务定义的基础设施组件抽象，可以是物理资源也可以是逻辑资源

        :return: The mode of this ExecutionPlanItem.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ExecutionPlanItem.

        资源模式   * `DATA` - 指可以在模板解析期间运行和获取服务端数据的资源类型，不会操作基础设施组件   * `RESOURCE` - 指通过模板管理的由服务定义的基础设施组件抽象，可以是物理资源也可以是逻辑资源

        :param mode: The mode of this ExecutionPlanItem.
        :type mode: str
        """
        self._mode = mode

    @property
    def drifted(self):
        """Gets the drifted of this ExecutionPlanItem.

        当前资源的变更是否由偏差导致。  偏差，也叫漂移。指的是资源被资源编排服务创建以后，又经历过非资源编排服务触发的修改，如手动修改、调用SDK修改等，使得资源的配置与本服务所记录的资源的配置不一致。这种不一致便称为偏差。  当资源产生偏差以后： * 如果用户试图创建执行计划，则会提示用户产生偏差 * 如果用户直接部署，则偏差有可能被覆盖，资源编排服务只保证资源和模板最终一致。  资源的偏差有两种类型： * 资源定位属性被修改：如果是定位属性被修改，常见于删除后重建，此时资源已经不属于同一个资源。资源编排服务会认为此资源已经被删除，会尝试创建一个新的资源。 * 资源普通属性被修改：如果是普通属性被修改，则资源编排服务依然可以找到资源，但是下次部署会尝试修复偏差，即将资源保持和模板最终一致。  **注：资源编排服务团队极力推荐，如果资源是通过本服务创建的，请一直使用本服务进行维护和更新以确保资源和模板保持一致。建议非紧急事件以外的情况不要手动调整。**

        :return: The drifted of this ExecutionPlanItem.
        :rtype: bool
        """
        return self._drifted

    @drifted.setter
    def drifted(self, drifted):
        """Sets the drifted of this ExecutionPlanItem.

        当前资源的变更是否由偏差导致。  偏差，也叫漂移。指的是资源被资源编排服务创建以后，又经历过非资源编排服务触发的修改，如手动修改、调用SDK修改等，使得资源的配置与本服务所记录的资源的配置不一致。这种不一致便称为偏差。  当资源产生偏差以后： * 如果用户试图创建执行计划，则会提示用户产生偏差 * 如果用户直接部署，则偏差有可能被覆盖，资源编排服务只保证资源和模板最终一致。  资源的偏差有两种类型： * 资源定位属性被修改：如果是定位属性被修改，常见于删除后重建，此时资源已经不属于同一个资源。资源编排服务会认为此资源已经被删除，会尝试创建一个新的资源。 * 资源普通属性被修改：如果是普通属性被修改，则资源编排服务依然可以找到资源，但是下次部署会尝试修复偏差，即将资源保持和模板最终一致。  **注：资源编排服务团队极力推荐，如果资源是通过本服务创建的，请一直使用本服务进行维护和更新以确保资源和模板保持一致。建议非紧急事件以外的情况不要手动调整。**

        :param drifted: The drifted of this ExecutionPlanItem.
        :type drifted: bool
        """
        self._drifted = drifted

    @property
    def imported(self):
        """Gets the imported of this ExecutionPlanItem.

        当前资源的变更是否是导入的。

        :return: The imported of this ExecutionPlanItem.
        :rtype: bool
        """
        return self._imported

    @imported.setter
    def imported(self, imported):
        """Sets the imported of this ExecutionPlanItem.

        当前资源的变更是否是导入的。

        :param imported: The imported of this ExecutionPlanItem.
        :type imported: bool
        """
        self._imported = imported

    @property
    def resource_id(self):
        """Gets the resource_id of this ExecutionPlanItem.

        资源的物理id，是唯一id，由为该资源提供服务的provider、云服务或其他服务提供方在资源部署的时候生成

        :return: The resource_id of this ExecutionPlanItem.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ExecutionPlanItem.

        资源的物理id，是唯一id，由为该资源提供服务的provider、云服务或其他服务提供方在资源部署的时候生成

        :param resource_id: The resource_id of this ExecutionPlanItem.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def attributes(self):
        """Gets the attributes of this ExecutionPlanItem.

        执行计划项目中变更的属性，当无属性变更时为空列表。

        :return: The attributes of this ExecutionPlanItem.
        :rtype: list[:class:`huaweicloudsdkaos.v1.ExecutionPlanDiffAttribute`]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ExecutionPlanItem.

        执行计划项目中变更的属性，当无属性变更时为空列表。

        :param attributes: The attributes of this ExecutionPlanItem.
        :type attributes: list[:class:`huaweicloudsdkaos.v1.ExecutionPlanDiffAttribute`]
        """
        self._attributes = attributes

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
        if not isinstance(other, ExecutionPlanItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
