# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetDevServerJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_at': 'str',
        'update_at': 'str',
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'status': 'str',
        'items': 'list[DevServerJobItem]',
        'tasks': 'list[DevServerTaskResponse]',
        'template_id': 'str',
        'user_name': 'str',
        'abnormal_count': 'int',
        'description': 'str'
    }

    attribute_map = {
        'create_at': 'create_at',
        'update_at': 'update_at',
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'status': 'status',
        'items': 'items',
        'tasks': 'tasks',
        'template_id': 'template_id',
        'user_name': 'user_name',
        'abnormal_count': 'abnormal_count',
        'description': 'description'
    }

    def __init__(self, create_at=None, update_at=None, id=None, name=None, type=None, status=None, items=None, tasks=None, template_id=None, user_name=None, abnormal_count=None, description=None):
        r"""GetDevServerJobResponse

        The model defined in huaweicloud sdk

        :param create_at: **参数解释**：创建时间。 **取值范围**：不涉及。
        :type create_at: str
        :param update_at: **参数解释**：更新时间。 **取值范围**：不涉及。
        :type update_at: str
        :param id: **参数解释**：任务ID。 **取值范围**：不涉及。
        :type id: str
        :param name: **参数解释**：任务名称。 **取值范围**：不涉及。
        :type name: str
        :param type: **参数解释**：任务模板类型。 **取值范围**：- COMMON  -SERVICE_DEPLOY 等。
        :type type: str
        :param status: **参数解释**：状态。 **取值范围**：- ACTIVE。
        :type status: str
        :param items: **参数解释**：任务实例列表信息。
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.DevServerJobItem`]
        :param tasks: **参数解释**：task详情列表。
        :type tasks: list[:class:`huaweicloudsdkmodelarts.v1.DevServerTaskResponse`]
        :param template_id: **参数解释**：任务模板ID。 **取值范围**：不涉及。
        :type template_id: str
        :param user_name: **参数解释**：下发任务的用户信息。 **取值范围**：不涉及。
        :type user_name: str
        :param abnormal_count: **参数解释**：task失败的节点数量。 **取值范围**：不涉及。
        :type abnormal_count: int
        :param description: **参数解释**：描述。 **取值范围**：不涉及。
        :type description: str
        """
        
        super().__init__()

        self._create_at = None
        self._update_at = None
        self._id = None
        self._name = None
        self._type = None
        self._status = None
        self._items = None
        self._tasks = None
        self._template_id = None
        self._user_name = None
        self._abnormal_count = None
        self._description = None
        self.discriminator = None

        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if items is not None:
            self.items = items
        if tasks is not None:
            self.tasks = tasks
        if template_id is not None:
            self.template_id = template_id
        if user_name is not None:
            self.user_name = user_name
        if abnormal_count is not None:
            self.abnormal_count = abnormal_count
        if description is not None:
            self.description = description

    @property
    def create_at(self):
        r"""Gets the create_at of this GetDevServerJobResponse.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :return: The create_at of this GetDevServerJobResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this GetDevServerJobResponse.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :param create_at: The create_at of this GetDevServerJobResponse.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this GetDevServerJobResponse.

        **参数解释**：更新时间。 **取值范围**：不涉及。

        :return: The update_at of this GetDevServerJobResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this GetDevServerJobResponse.

        **参数解释**：更新时间。 **取值范围**：不涉及。

        :param update_at: The update_at of this GetDevServerJobResponse.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this GetDevServerJobResponse.

        **参数解释**：任务ID。 **取值范围**：不涉及。

        :return: The id of this GetDevServerJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetDevServerJobResponse.

        **参数解释**：任务ID。 **取值范围**：不涉及。

        :param id: The id of this GetDevServerJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GetDevServerJobResponse.

        **参数解释**：任务名称。 **取值范围**：不涉及。

        :return: The name of this GetDevServerJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetDevServerJobResponse.

        **参数解释**：任务名称。 **取值范围**：不涉及。

        :param name: The name of this GetDevServerJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this GetDevServerJobResponse.

        **参数解释**：任务模板类型。 **取值范围**：- COMMON  -SERVICE_DEPLOY 等。

        :return: The type of this GetDevServerJobResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GetDevServerJobResponse.

        **参数解释**：任务模板类型。 **取值范围**：- COMMON  -SERVICE_DEPLOY 等。

        :param type: The type of this GetDevServerJobResponse.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this GetDevServerJobResponse.

        **参数解释**：状态。 **取值范围**：- ACTIVE。

        :return: The status of this GetDevServerJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetDevServerJobResponse.

        **参数解释**：状态。 **取值范围**：- ACTIVE。

        :param status: The status of this GetDevServerJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def items(self):
        r"""Gets the items of this GetDevServerJobResponse.

        **参数解释**：任务实例列表信息。

        :return: The items of this GetDevServerJobResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DevServerJobItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this GetDevServerJobResponse.

        **参数解释**：任务实例列表信息。

        :param items: The items of this GetDevServerJobResponse.
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.DevServerJobItem`]
        """
        self._items = items

    @property
    def tasks(self):
        r"""Gets the tasks of this GetDevServerJobResponse.

        **参数解释**：task详情列表。

        :return: The tasks of this GetDevServerJobResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DevServerTaskResponse`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this GetDevServerJobResponse.

        **参数解释**：task详情列表。

        :param tasks: The tasks of this GetDevServerJobResponse.
        :type tasks: list[:class:`huaweicloudsdkmodelarts.v1.DevServerTaskResponse`]
        """
        self._tasks = tasks

    @property
    def template_id(self):
        r"""Gets the template_id of this GetDevServerJobResponse.

        **参数解释**：任务模板ID。 **取值范围**：不涉及。

        :return: The template_id of this GetDevServerJobResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this GetDevServerJobResponse.

        **参数解释**：任务模板ID。 **取值范围**：不涉及。

        :param template_id: The template_id of this GetDevServerJobResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def user_name(self):
        r"""Gets the user_name of this GetDevServerJobResponse.

        **参数解释**：下发任务的用户信息。 **取值范围**：不涉及。

        :return: The user_name of this GetDevServerJobResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this GetDevServerJobResponse.

        **参数解释**：下发任务的用户信息。 **取值范围**：不涉及。

        :param user_name: The user_name of this GetDevServerJobResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def abnormal_count(self):
        r"""Gets the abnormal_count of this GetDevServerJobResponse.

        **参数解释**：task失败的节点数量。 **取值范围**：不涉及。

        :return: The abnormal_count of this GetDevServerJobResponse.
        :rtype: int
        """
        return self._abnormal_count

    @abnormal_count.setter
    def abnormal_count(self, abnormal_count):
        r"""Sets the abnormal_count of this GetDevServerJobResponse.

        **参数解释**：task失败的节点数量。 **取值范围**：不涉及。

        :param abnormal_count: The abnormal_count of this GetDevServerJobResponse.
        :type abnormal_count: int
        """
        self._abnormal_count = abnormal_count

    @property
    def description(self):
        r"""Gets the description of this GetDevServerJobResponse.

        **参数解释**：描述。 **取值范围**：不涉及。

        :return: The description of this GetDevServerJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this GetDevServerJobResponse.

        **参数解释**：描述。 **取值范围**：不涉及。

        :param description: The description of this GetDevServerJobResponse.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        import warnings
        warnings.warn("GetDevServerJobResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetDevServerJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
