# coding: utf-8

import re
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
        'action': 'str',
        'action_reason': 'str',
        'provider_name': 'str',
        'resource_type': 'str',
        'resource_name': 'str',
        'index': 'str',
        'mode': 'str',
        'drifted': 'bool',
        'resource_id': 'str',
        'attributes': 'list[ExecutionPlanDiffAttribute]'
    }

    attribute_map = {
        'action': 'action',
        'action_reason': 'action_reason',
        'provider_name': 'provider_name',
        'resource_type': 'resource_type',
        'resource_name': 'resource_name',
        'index': 'index',
        'mode': 'mode',
        'drifted': 'drifted',
        'resource_id': 'resource_id',
        'attributes': 'attributes'
    }

    def __init__(self, action=None, action_reason=None, provider_name=None, resource_type=None, resource_name=None, index=None, mode=None, drifted=None, resource_id=None, attributes=None):
        """ExecutionPlanItem

        The model defined in huaweicloud sdk

        :param action: 资源变更的类型，这里，IN_PLACE_UPDATE、ADD_THEN_DELETE和 DELETE_THEN_ADD均为更新操作，IN_PLACE_UPDATE指原地更新； 而对于不可更新的资源，ADD_THEN_DELETE是先创建新的，再删除旧的；DELETE_THEN_ADD是先删除旧的，再创建新的. 执行计划的执行状态，只有当AVAILABLE的时候才可以使用apply执行 * &#x60;ADD&#x60; - 新建资源 * &#x60;ADD_THEN_DELETE&#x60; - 对于不可更新的资源执行先创建再删除的操作 * &#x60;DELETE &#x60; - 删除资源 * &#x60;DELETE_THEN_ADD&#x60; - 对于不可更新的资源执行先删除在创建的操作 * &#x60;UPDATE&#x60; - 更新资源  * &#x60;IN_PLACE_UPDATE&#x60; - 更新资源的操作 * &#x60;NO_OPERATION&#x60; - 变更资源的依赖关系，但是对资源本身并无修改的操作
        :type action: str
        :param action_reason: 表示该动作触发的原因，例如用户更新模板；远端删除资源等等
        :type action_reason: str
        :param provider_name: 表示该资源所属的provider名字。
        :type provider_name: str
        :param resource_type: 当前资源在HCL模板中对应的类型。
        :type resource_type: str
        :param resource_name: 当前资源的在HCL模板中指定的名字。
        :type resource_name: str
        :param index: 表示资源对应的index，例如对于使用count构建的资源，其类型和名字一样，但是index是从1到count的数值；对于使用for_each创建的资源，index可以是for_each中指定的key名。
        :type index: str
        :param mode: * &#x60;DATA&#x60; - 指可以在模板解析期间运行和获取服务端数据的资源类型，不会操作基础设施组件 * &#x60;RESOURCE&#x60; - 指通过模板管理的由服务定义的基础设施组件抽象，可以是物理资源也可以是逻辑资源
        :type mode: str
        :param drifted: 当前资源的变更是否由配置漂移导致。
        :type drifted: bool
        :param resource_id: 当前资源的唯一ID，当操作类型为创建时为空。当资源为新建时为空。注意resouce_name是资源在HCL模板中定义的名字，resource_id是provider提供的唯一ID。
        :type resource_id: str
        :param attributes: 执行计划元素变更的属性，当无属性变更时为空。
        :type attributes: list[:class:`huaweicloudsdkaos.v1.ExecutionPlanDiffAttribute`]
        """
        
        

        self._action = None
        self._action_reason = None
        self._provider_name = None
        self._resource_type = None
        self._resource_name = None
        self._index = None
        self._mode = None
        self._drifted = None
        self._resource_id = None
        self._attributes = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if action_reason is not None:
            self.action_reason = action_reason
        if provider_name is not None:
            self.provider_name = provider_name
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_name is not None:
            self.resource_name = resource_name
        if index is not None:
            self.index = index
        if mode is not None:
            self.mode = mode
        if drifted is not None:
            self.drifted = drifted
        if resource_id is not None:
            self.resource_id = resource_id
        if attributes is not None:
            self.attributes = attributes

    @property
    def action(self):
        """Gets the action of this ExecutionPlanItem.

        资源变更的类型，这里，IN_PLACE_UPDATE、ADD_THEN_DELETE和 DELETE_THEN_ADD均为更新操作，IN_PLACE_UPDATE指原地更新； 而对于不可更新的资源，ADD_THEN_DELETE是先创建新的，再删除旧的；DELETE_THEN_ADD是先删除旧的，再创建新的. 执行计划的执行状态，只有当AVAILABLE的时候才可以使用apply执行 * `ADD` - 新建资源 * `ADD_THEN_DELETE` - 对于不可更新的资源执行先创建再删除的操作 * `DELETE ` - 删除资源 * `DELETE_THEN_ADD` - 对于不可更新的资源执行先删除在创建的操作 * `UPDATE` - 更新资源  * `IN_PLACE_UPDATE` - 更新资源的操作 * `NO_OPERATION` - 变更资源的依赖关系，但是对资源本身并无修改的操作

        :return: The action of this ExecutionPlanItem.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ExecutionPlanItem.

        资源变更的类型，这里，IN_PLACE_UPDATE、ADD_THEN_DELETE和 DELETE_THEN_ADD均为更新操作，IN_PLACE_UPDATE指原地更新； 而对于不可更新的资源，ADD_THEN_DELETE是先创建新的，再删除旧的；DELETE_THEN_ADD是先删除旧的，再创建新的. 执行计划的执行状态，只有当AVAILABLE的时候才可以使用apply执行 * `ADD` - 新建资源 * `ADD_THEN_DELETE` - 对于不可更新的资源执行先创建再删除的操作 * `DELETE ` - 删除资源 * `DELETE_THEN_ADD` - 对于不可更新的资源执行先删除在创建的操作 * `UPDATE` - 更新资源  * `IN_PLACE_UPDATE` - 更新资源的操作 * `NO_OPERATION` - 变更资源的依赖关系，但是对资源本身并无修改的操作

        :param action: The action of this ExecutionPlanItem.
        :type action: str
        """
        self._action = action

    @property
    def action_reason(self):
        """Gets the action_reason of this ExecutionPlanItem.

        表示该动作触发的原因，例如用户更新模板；远端删除资源等等

        :return: The action_reason of this ExecutionPlanItem.
        :rtype: str
        """
        return self._action_reason

    @action_reason.setter
    def action_reason(self, action_reason):
        """Sets the action_reason of this ExecutionPlanItem.

        表示该动作触发的原因，例如用户更新模板；远端删除资源等等

        :param action_reason: The action_reason of this ExecutionPlanItem.
        :type action_reason: str
        """
        self._action_reason = action_reason

    @property
    def provider_name(self):
        """Gets the provider_name of this ExecutionPlanItem.

        表示该资源所属的provider名字。

        :return: The provider_name of this ExecutionPlanItem.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this ExecutionPlanItem.

        表示该资源所属的provider名字。

        :param provider_name: The provider_name of this ExecutionPlanItem.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def resource_type(self):
        """Gets the resource_type of this ExecutionPlanItem.

        当前资源在HCL模板中对应的类型。

        :return: The resource_type of this ExecutionPlanItem.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ExecutionPlanItem.

        当前资源在HCL模板中对应的类型。

        :param resource_type: The resource_type of this ExecutionPlanItem.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        """Gets the resource_name of this ExecutionPlanItem.

        当前资源的在HCL模板中指定的名字。

        :return: The resource_name of this ExecutionPlanItem.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ExecutionPlanItem.

        当前资源的在HCL模板中指定的名字。

        :param resource_name: The resource_name of this ExecutionPlanItem.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def index(self):
        """Gets the index of this ExecutionPlanItem.

        表示资源对应的index，例如对于使用count构建的资源，其类型和名字一样，但是index是从1到count的数值；对于使用for_each创建的资源，index可以是for_each中指定的key名。

        :return: The index of this ExecutionPlanItem.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ExecutionPlanItem.

        表示资源对应的index，例如对于使用count构建的资源，其类型和名字一样，但是index是从1到count的数值；对于使用for_each创建的资源，index可以是for_each中指定的key名。

        :param index: The index of this ExecutionPlanItem.
        :type index: str
        """
        self._index = index

    @property
    def mode(self):
        """Gets the mode of this ExecutionPlanItem.

        * `DATA` - 指可以在模板解析期间运行和获取服务端数据的资源类型，不会操作基础设施组件 * `RESOURCE` - 指通过模板管理的由服务定义的基础设施组件抽象，可以是物理资源也可以是逻辑资源

        :return: The mode of this ExecutionPlanItem.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ExecutionPlanItem.

        * `DATA` - 指可以在模板解析期间运行和获取服务端数据的资源类型，不会操作基础设施组件 * `RESOURCE` - 指通过模板管理的由服务定义的基础设施组件抽象，可以是物理资源也可以是逻辑资源

        :param mode: The mode of this ExecutionPlanItem.
        :type mode: str
        """
        self._mode = mode

    @property
    def drifted(self):
        """Gets the drifted of this ExecutionPlanItem.

        当前资源的变更是否由配置漂移导致。

        :return: The drifted of this ExecutionPlanItem.
        :rtype: bool
        """
        return self._drifted

    @drifted.setter
    def drifted(self, drifted):
        """Sets the drifted of this ExecutionPlanItem.

        当前资源的变更是否由配置漂移导致。

        :param drifted: The drifted of this ExecutionPlanItem.
        :type drifted: bool
        """
        self._drifted = drifted

    @property
    def resource_id(self):
        """Gets the resource_id of this ExecutionPlanItem.

        当前资源的唯一ID，当操作类型为创建时为空。当资源为新建时为空。注意resouce_name是资源在HCL模板中定义的名字，resource_id是provider提供的唯一ID。

        :return: The resource_id of this ExecutionPlanItem.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ExecutionPlanItem.

        当前资源的唯一ID，当操作类型为创建时为空。当资源为新建时为空。注意resouce_name是资源在HCL模板中定义的名字，resource_id是provider提供的唯一ID。

        :param resource_id: The resource_id of this ExecutionPlanItem.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def attributes(self):
        """Gets the attributes of this ExecutionPlanItem.

        执行计划元素变更的属性，当无属性变更时为空。

        :return: The attributes of this ExecutionPlanItem.
        :rtype: list[:class:`huaweicloudsdkaos.v1.ExecutionPlanDiffAttribute`]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ExecutionPlanItem.

        执行计划元素变更的属性，当无属性变更时为空。

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
