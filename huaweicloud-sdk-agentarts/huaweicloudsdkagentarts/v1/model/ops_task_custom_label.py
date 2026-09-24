# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTaskCustomLabel:

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
        'task_id': 'str',
        'account_id': 'str',
        'tag_id': 'str',
        'tag_type': 'str',
        'create_at': 'datetime',
        'update_at': 'datetime',
        'is_delete': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'task_id': 'task_id',
        'account_id': 'account_id',
        'tag_id': 'tag_id',
        'tag_type': 'tag_type',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'is_delete': 'is_delete'
    }

    def __init__(self, id=None, task_id=None, account_id=None, tag_id=None, tag_type=None, create_at=None, update_at=None, is_delete=None):
        r"""OpsTaskCustomLabel

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 记录唯一标识（MongoDB ObjectId）。 **约束限制：** 不涉及。 **取值范围：** 24位十六进制字符串。 **默认取值：** 不涉及。 
        :type id: str
        :param task_id: **参数解释：** 任务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type task_id: str
        :param account_id: **参数解释：** 租户账号ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type account_id: str
        :param tag_id: **参数解释：** 标签ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type tag_id: str
        :param tag_type: **参数解释：** 标签类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type tag_type: str
        :param create_at: **参数解释：** 创建时间。 **约束限制：** 不涉及。 **取值范围：** ISO 8601 时间格式。 **默认取值：** 不涉及。 
        :type create_at: datetime
        :param update_at: **参数解释：** 更新时间。 **约束限制：** 不涉及。 **取值范围：** ISO 8601 时间格式。 **默认取值：** 不涉及。 
        :type update_at: datetime
        :param is_delete: **参数解释：** 是否已删除标记。 **约束限制：** 不涉及。 **取值范围：** - true：已删除 - false：未删除 **默认取值：** 不涉及。 
        :type is_delete: bool
        """
        
        

        self._id = None
        self._task_id = None
        self._account_id = None
        self._tag_id = None
        self._tag_type = None
        self._create_at = None
        self._update_at = None
        self._is_delete = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_id is not None:
            self.task_id = task_id
        if account_id is not None:
            self.account_id = account_id
        if tag_id is not None:
            self.tag_id = tag_id
        if tag_type is not None:
            self.tag_type = tag_type
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if is_delete is not None:
            self.is_delete = is_delete

    @property
    def id(self):
        r"""Gets the id of this OpsTaskCustomLabel.

        **参数解释：** 记录唯一标识（MongoDB ObjectId）。 **约束限制：** 不涉及。 **取值范围：** 24位十六进制字符串。 **默认取值：** 不涉及。 

        :return: The id of this OpsTaskCustomLabel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsTaskCustomLabel.

        **参数解释：** 记录唯一标识（MongoDB ObjectId）。 **约束限制：** 不涉及。 **取值范围：** 24位十六进制字符串。 **默认取值：** 不涉及。 

        :param id: The id of this OpsTaskCustomLabel.
        :type id: str
        """
        self._id = id

    @property
    def task_id(self):
        r"""Gets the task_id of this OpsTaskCustomLabel.

        **参数解释：** 任务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The task_id of this OpsTaskCustomLabel.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this OpsTaskCustomLabel.

        **参数解释：** 任务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param task_id: The task_id of this OpsTaskCustomLabel.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def account_id(self):
        r"""Gets the account_id of this OpsTaskCustomLabel.

        **参数解释：** 租户账号ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The account_id of this OpsTaskCustomLabel.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this OpsTaskCustomLabel.

        **参数解释：** 租户账号ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param account_id: The account_id of this OpsTaskCustomLabel.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def tag_id(self):
        r"""Gets the tag_id of this OpsTaskCustomLabel.

        **参数解释：** 标签ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The tag_id of this OpsTaskCustomLabel.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        r"""Sets the tag_id of this OpsTaskCustomLabel.

        **参数解释：** 标签ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param tag_id: The tag_id of this OpsTaskCustomLabel.
        :type tag_id: str
        """
        self._tag_id = tag_id

    @property
    def tag_type(self):
        r"""Gets the tag_type of this OpsTaskCustomLabel.

        **参数解释：** 标签类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The tag_type of this OpsTaskCustomLabel.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        r"""Sets the tag_type of this OpsTaskCustomLabel.

        **参数解释：** 标签类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param tag_type: The tag_type of this OpsTaskCustomLabel.
        :type tag_type: str
        """
        self._tag_type = tag_type

    @property
    def create_at(self):
        r"""Gets the create_at of this OpsTaskCustomLabel.

        **参数解释：** 创建时间。 **约束限制：** 不涉及。 **取值范围：** ISO 8601 时间格式。 **默认取值：** 不涉及。 

        :return: The create_at of this OpsTaskCustomLabel.
        :rtype: datetime
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this OpsTaskCustomLabel.

        **参数解释：** 创建时间。 **约束限制：** 不涉及。 **取值范围：** ISO 8601 时间格式。 **默认取值：** 不涉及。 

        :param create_at: The create_at of this OpsTaskCustomLabel.
        :type create_at: datetime
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this OpsTaskCustomLabel.

        **参数解释：** 更新时间。 **约束限制：** 不涉及。 **取值范围：** ISO 8601 时间格式。 **默认取值：** 不涉及。 

        :return: The update_at of this OpsTaskCustomLabel.
        :rtype: datetime
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this OpsTaskCustomLabel.

        **参数解释：** 更新时间。 **约束限制：** 不涉及。 **取值范围：** ISO 8601 时间格式。 **默认取值：** 不涉及。 

        :param update_at: The update_at of this OpsTaskCustomLabel.
        :type update_at: datetime
        """
        self._update_at = update_at

    @property
    def is_delete(self):
        r"""Gets the is_delete of this OpsTaskCustomLabel.

        **参数解释：** 是否已删除标记。 **约束限制：** 不涉及。 **取值范围：** - true：已删除 - false：未删除 **默认取值：** 不涉及。 

        :return: The is_delete of this OpsTaskCustomLabel.
        :rtype: bool
        """
        return self._is_delete

    @is_delete.setter
    def is_delete(self, is_delete):
        r"""Sets the is_delete of this OpsTaskCustomLabel.

        **参数解释：** 是否已删除标记。 **约束限制：** 不涉及。 **取值范围：** - true：已删除 - false：未删除 **默认取值：** 不涉及。 

        :param is_delete: The is_delete of this OpsTaskCustomLabel.
        :type is_delete: bool
        """
        self._is_delete = is_delete

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
        if not isinstance(other, OpsTaskCustomLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
