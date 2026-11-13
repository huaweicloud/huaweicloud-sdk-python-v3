# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Application:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'icon': 'str',
        'description': 'str',
        'release_note': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'create_user_id': 'str',
        'update_user_id': 'str',
        'release_state': 'int',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'icon': 'icon',
        'description': 'description',
        'release_note': 'release_note',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'create_user_id': 'create_user_id',
        'update_user_id': 'update_user_id',
        'release_state': 'release_state',
        'version': 'version'
    }

    def __init__(self, id=None, name=None, icon=None, description=None, release_note=None, created_at=None, updated_at=None, create_user_id=None, update_user_id=None, release_state=None, version=None):
        r"""Application

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 应用编码。 **取值范围**： [1-256]字符。
        :type id: str
        :param name: **参数解释**： 应用名称。 **取值范围**： [1-200]字符。
        :type name: str
        :param icon: **参数解释**： 应用图标URL，当前仅支持预置应用图标，取值为0~9的数字，分别标识第1到第10张预置图标。 **取值范围**： [1-200]字符。
        :type icon: str
        :param description: **参数解释**： 应用描述。 **取值范围**： [1-200]字符。
        :type description: str
        :param release_note: **参数解释**： 发布说明。 **取值范围**： [1-500]字符。
        :type release_note: str
        :param created_at: **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。
        :type created_at: datetime
        :param updated_at: **参数解释**： [更新时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [更新时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。
        :type updated_at: datetime
        :param create_user_id: **参数解释**： 创建用户ID。 **取值范围**： [1-50]个字符。
        :type create_user_id: str
        :param update_user_id: **参数解释**： 更新用户ID。 **取值范围**： [1-50]个字符。
        :type update_user_id: str
        :param release_state: **参数解释**： 应用状态。 **取值范围**： - 0：待发布。 - 1：已发布，生效状态。 - 2：已发布，失效状态。
        :type release_state: int
        :param version: **参数解释**： 版本号。 **取值范围**： [1-50]个字符。
        :type version: str
        """
        
        

        self._id = None
        self._name = None
        self._icon = None
        self._description = None
        self._release_note = None
        self._created_at = None
        self._updated_at = None
        self._create_user_id = None
        self._update_user_id = None
        self._release_state = None
        self._version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if icon is not None:
            self.icon = icon
        if description is not None:
            self.description = description
        if release_note is not None:
            self.release_note = release_note
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if create_user_id is not None:
            self.create_user_id = create_user_id
        if update_user_id is not None:
            self.update_user_id = update_user_id
        if release_state is not None:
            self.release_state = release_state
        if version is not None:
            self.version = version

    @property
    def id(self):
        r"""Gets the id of this Application.

        **参数解释**： 应用编码。 **取值范围**： [1-256]字符。

        :return: The id of this Application.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Application.

        **参数解释**： 应用编码。 **取值范围**： [1-256]字符。

        :param id: The id of this Application.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Application.

        **参数解释**： 应用名称。 **取值范围**： [1-200]字符。

        :return: The name of this Application.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Application.

        **参数解释**： 应用名称。 **取值范围**： [1-200]字符。

        :param name: The name of this Application.
        :type name: str
        """
        self._name = name

    @property
    def icon(self):
        r"""Gets the icon of this Application.

        **参数解释**： 应用图标URL，当前仅支持预置应用图标，取值为0~9的数字，分别标识第1到第10张预置图标。 **取值范围**： [1-200]字符。

        :return: The icon of this Application.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        r"""Sets the icon of this Application.

        **参数解释**： 应用图标URL，当前仅支持预置应用图标，取值为0~9的数字，分别标识第1到第10张预置图标。 **取值范围**： [1-200]字符。

        :param icon: The icon of this Application.
        :type icon: str
        """
        self._icon = icon

    @property
    def description(self):
        r"""Gets the description of this Application.

        **参数解释**： 应用描述。 **取值范围**： [1-200]字符。

        :return: The description of this Application.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Application.

        **参数解释**： 应用描述。 **取值范围**： [1-200]字符。

        :param description: The description of this Application.
        :type description: str
        """
        self._description = description

    @property
    def release_note(self):
        r"""Gets the release_note of this Application.

        **参数解释**： 发布说明。 **取值范围**： [1-500]字符。

        :return: The release_note of this Application.
        :rtype: str
        """
        return self._release_note

    @release_note.setter
    def release_note(self, release_note):
        r"""Sets the release_note of this Application.

        **参数解释**： 发布说明。 **取值范围**： [1-500]字符。

        :param release_note: The release_note of this Application.
        :type release_note: str
        """
        self._release_note = release_note

    @property
    def created_at(self):
        r"""Gets the created_at of this Application.

        **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。

        :return: The created_at of this Application.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Application.

        **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。

        :param created_at: The created_at of this Application.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Application.

        **参数解释**： [更新时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [更新时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。

        :return: The updated_at of this Application.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Application.

        **参数解释**： [更新时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [更新时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。

        :param updated_at: The updated_at of this Application.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def create_user_id(self):
        r"""Gets the create_user_id of this Application.

        **参数解释**： 创建用户ID。 **取值范围**： [1-50]个字符。

        :return: The create_user_id of this Application.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        r"""Sets the create_user_id of this Application.

        **参数解释**： 创建用户ID。 **取值范围**： [1-50]个字符。

        :param create_user_id: The create_user_id of this Application.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def update_user_id(self):
        r"""Gets the update_user_id of this Application.

        **参数解释**： 更新用户ID。 **取值范围**： [1-50]个字符。

        :return: The update_user_id of this Application.
        :rtype: str
        """
        return self._update_user_id

    @update_user_id.setter
    def update_user_id(self, update_user_id):
        r"""Sets the update_user_id of this Application.

        **参数解释**： 更新用户ID。 **取值范围**： [1-50]个字符。

        :param update_user_id: The update_user_id of this Application.
        :type update_user_id: str
        """
        self._update_user_id = update_user_id

    @property
    def release_state(self):
        r"""Gets the release_state of this Application.

        **参数解释**： 应用状态。 **取值范围**： - 0：待发布。 - 1：已发布，生效状态。 - 2：已发布，失效状态。

        :return: The release_state of this Application.
        :rtype: int
        """
        return self._release_state

    @release_state.setter
    def release_state(self, release_state):
        r"""Sets the release_state of this Application.

        **参数解释**： 应用状态。 **取值范围**： - 0：待发布。 - 1：已发布，生效状态。 - 2：已发布，失效状态。

        :param release_state: The release_state of this Application.
        :type release_state: int
        """
        self._release_state = release_state

    @property
    def version(self):
        r"""Gets the version of this Application.

        **参数解释**： 版本号。 **取值范围**： [1-50]个字符。

        :return: The version of this Application.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Application.

        **参数解释**： 版本号。 **取值范围**： [1-50]个字符。

        :param version: The version of this Application.
        :type version: str
        """
        self._version = version

    def to_dict(self):
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
        if not isinstance(other, Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
