# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledTaskEntity:

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
        'user_name': 'str',
        'user_id': 'str',
        'params': 'str',
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'schedule_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user_name': 'user_name',
        'user_id': 'user_id',
        'params': 'params',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'schedule_at': 'schedule_at'
    }

    def __init__(self, id=None, name=None, user_name=None, user_id=None, params=None, status=None, created_at=None, updated_at=None, schedule_at=None):
        r"""ScheduledTaskEntity

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 任务ID。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 任务名称。 **取值范围**： 不涉及。
        :type name: str
        :param user_name: **参数解释**： 用户名称。 **取值范围**： 不涉及。
        :type user_name: str
        :param user_id: **参数解释**： 用户ID。 **取值范围**： 不涉及。
        :type user_id: str
        :param params: **参数解释**： 任务参数。 **取值范围**： 不涉及。
        :type params: str
        :param status: **参数解释**： 任务状态。 **取值范围**： - CREATED：定时任务状态为创建成功。 - SUCCESS：定时任务状态为成功。 - FAILED：定时任务状态为失败。 - DELETED：定时任务状态为已删除。 - EXECUTING：定时任务状态为执行中。 - CANCELLED：定时任务状态为取消。
        :type status: str
        :param created_at: **参数解释**： 创建时间。 **取值范围**： 不涉及。
        :type created_at: str
        :param updated_at: **参数解释**： 更新时间。 **取值范围**： 不涉及。
        :type updated_at: str
        :param schedule_at: **参数解释**： 定时执行时间。 **取值范围**： 不涉及。
        :type schedule_at: str
        """
        
        

        self._id = None
        self._name = None
        self._user_name = None
        self._user_id = None
        self._params = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._schedule_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if user_name is not None:
            self.user_name = user_name
        if user_id is not None:
            self.user_id = user_id
        if params is not None:
            self.params = params
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if schedule_at is not None:
            self.schedule_at = schedule_at

    @property
    def id(self):
        r"""Gets the id of this ScheduledTaskEntity.

        **参数解释**： 任务ID。 **取值范围**： 不涉及。

        :return: The id of this ScheduledTaskEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScheduledTaskEntity.

        **参数解释**： 任务ID。 **取值范围**： 不涉及。

        :param id: The id of this ScheduledTaskEntity.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ScheduledTaskEntity.

        **参数解释**： 任务名称。 **取值范围**： 不涉及。

        :return: The name of this ScheduledTaskEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScheduledTaskEntity.

        **参数解释**： 任务名称。 **取值范围**： 不涉及。

        :param name: The name of this ScheduledTaskEntity.
        :type name: str
        """
        self._name = name

    @property
    def user_name(self):
        r"""Gets the user_name of this ScheduledTaskEntity.

        **参数解释**： 用户名称。 **取值范围**： 不涉及。

        :return: The user_name of this ScheduledTaskEntity.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ScheduledTaskEntity.

        **参数解释**： 用户名称。 **取值范围**： 不涉及。

        :param user_name: The user_name of this ScheduledTaskEntity.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_id(self):
        r"""Gets the user_id of this ScheduledTaskEntity.

        **参数解释**： 用户ID。 **取值范围**： 不涉及。

        :return: The user_id of this ScheduledTaskEntity.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ScheduledTaskEntity.

        **参数解释**： 用户ID。 **取值范围**： 不涉及。

        :param user_id: The user_id of this ScheduledTaskEntity.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def params(self):
        r"""Gets the params of this ScheduledTaskEntity.

        **参数解释**： 任务参数。 **取值范围**： 不涉及。

        :return: The params of this ScheduledTaskEntity.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this ScheduledTaskEntity.

        **参数解释**： 任务参数。 **取值范围**： 不涉及。

        :param params: The params of this ScheduledTaskEntity.
        :type params: str
        """
        self._params = params

    @property
    def status(self):
        r"""Gets the status of this ScheduledTaskEntity.

        **参数解释**： 任务状态。 **取值范围**： - CREATED：定时任务状态为创建成功。 - SUCCESS：定时任务状态为成功。 - FAILED：定时任务状态为失败。 - DELETED：定时任务状态为已删除。 - EXECUTING：定时任务状态为执行中。 - CANCELLED：定时任务状态为取消。

        :return: The status of this ScheduledTaskEntity.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScheduledTaskEntity.

        **参数解释**： 任务状态。 **取值范围**： - CREATED：定时任务状态为创建成功。 - SUCCESS：定时任务状态为成功。 - FAILED：定时任务状态为失败。 - DELETED：定时任务状态为已删除。 - EXECUTING：定时任务状态为执行中。 - CANCELLED：定时任务状态为取消。

        :param status: The status of this ScheduledTaskEntity.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this ScheduledTaskEntity.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :return: The created_at of this ScheduledTaskEntity.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ScheduledTaskEntity.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :param created_at: The created_at of this ScheduledTaskEntity.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ScheduledTaskEntity.

        **参数解释**： 更新时间。 **取值范围**： 不涉及。

        :return: The updated_at of this ScheduledTaskEntity.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ScheduledTaskEntity.

        **参数解释**： 更新时间。 **取值范围**： 不涉及。

        :param updated_at: The updated_at of this ScheduledTaskEntity.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def schedule_at(self):
        r"""Gets the schedule_at of this ScheduledTaskEntity.

        **参数解释**： 定时执行时间。 **取值范围**： 不涉及。

        :return: The schedule_at of this ScheduledTaskEntity.
        :rtype: str
        """
        return self._schedule_at

    @schedule_at.setter
    def schedule_at(self, schedule_at):
        r"""Sets the schedule_at of this ScheduledTaskEntity.

        **参数解释**： 定时执行时间。 **取值范围**： 不涉及。

        :param schedule_at: The schedule_at of this ScheduledTaskEntity.
        :type schedule_at: str
        """
        self._schedule_at = schedule_at

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
        if not isinstance(other, ScheduledTaskEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
