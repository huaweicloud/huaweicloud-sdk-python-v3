# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordInfoResponseResult:

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
        'action': 'str',
        'status': 'str',
        'message': 'str',
        'entity_id': 'str',
        'entity_type': 'str',
        'job_id': 'str',
        'instance_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'extended_info': 'object'
    }

    attribute_map = {
        'id': 'id',
        'action': 'action',
        'status': 'status',
        'message': 'message',
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'job_id': 'job_id',
        'instance_id': 'instance_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'extended_info': 'extended_info'
    }

    def __init__(self, id=None, action=None, status=None, message=None, entity_id=None, entity_type=None, job_id=None, instance_id=None, created_at=None, updated_at=None, extended_info=None):
        r"""RecordInfoResponseResult

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 主键id。 **取值范围**: 不涉及。
        :type id: str
        :param action: **参数解释**: 动作。 **取值范围**: 不涉及。
        :type action: str
        :param status: **参数解释**: 操作状态。 **取值范围**: 不涉及。
        :type status: str
        :param message: **参数解释**: 信息。 **取值范围**: 不涉及。
        :type message: str
        :param entity_id: **参数解释**: 实体id。 **取值范围**: 不涉及。
        :type entity_id: str
        :param entity_type: **参数解释**: 实体类型。 **取值范围**: 不涉及。
        :type entity_type: str
        :param job_id: **参数解释**: 工作流id。 **取值范围**: 不涉及。
        :type job_id: str
        :param instance_id: **参数解释**: 实例id。 **取值范围**: 不涉及。
        :type instance_id: str
        :param created_at: **参数解释**: 创建时间。 **取值范围**: 不涉及。
        :type created_at: str
        :param updated_at: **参数解释**: 更新时间。 **取值范围**: 不涉及。
        :type updated_at: str
        :param extended_info: **参数解释**: 扩展信息。 **取值范围**: 不涉及。
        :type extended_info: object
        """
        
        

        self._id = None
        self._action = None
        self._status = None
        self._message = None
        self._entity_id = None
        self._entity_type = None
        self._job_id = None
        self._instance_id = None
        self._created_at = None
        self._updated_at = None
        self._extended_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if action is not None:
            self.action = action
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if entity_id is not None:
            self.entity_id = entity_id
        if entity_type is not None:
            self.entity_type = entity_type
        if job_id is not None:
            self.job_id = job_id
        if instance_id is not None:
            self.instance_id = instance_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if extended_info is not None:
            self.extended_info = extended_info

    @property
    def id(self):
        r"""Gets the id of this RecordInfoResponseResult.

        **参数解释**: 主键id。 **取值范围**: 不涉及。

        :return: The id of this RecordInfoResponseResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RecordInfoResponseResult.

        **参数解释**: 主键id。 **取值范围**: 不涉及。

        :param id: The id of this RecordInfoResponseResult.
        :type id: str
        """
        self._id = id

    @property
    def action(self):
        r"""Gets the action of this RecordInfoResponseResult.

        **参数解释**: 动作。 **取值范围**: 不涉及。

        :return: The action of this RecordInfoResponseResult.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this RecordInfoResponseResult.

        **参数解释**: 动作。 **取值范围**: 不涉及。

        :param action: The action of this RecordInfoResponseResult.
        :type action: str
        """
        self._action = action

    @property
    def status(self):
        r"""Gets the status of this RecordInfoResponseResult.

        **参数解释**: 操作状态。 **取值范围**: 不涉及。

        :return: The status of this RecordInfoResponseResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RecordInfoResponseResult.

        **参数解释**: 操作状态。 **取值范围**: 不涉及。

        :param status: The status of this RecordInfoResponseResult.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this RecordInfoResponseResult.

        **参数解释**: 信息。 **取值范围**: 不涉及。

        :return: The message of this RecordInfoResponseResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this RecordInfoResponseResult.

        **参数解释**: 信息。 **取值范围**: 不涉及。

        :param message: The message of this RecordInfoResponseResult.
        :type message: str
        """
        self._message = message

    @property
    def entity_id(self):
        r"""Gets the entity_id of this RecordInfoResponseResult.

        **参数解释**: 实体id。 **取值范围**: 不涉及。

        :return: The entity_id of this RecordInfoResponseResult.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        r"""Sets the entity_id of this RecordInfoResponseResult.

        **参数解释**: 实体id。 **取值范围**: 不涉及。

        :param entity_id: The entity_id of this RecordInfoResponseResult.
        :type entity_id: str
        """
        self._entity_id = entity_id

    @property
    def entity_type(self):
        r"""Gets the entity_type of this RecordInfoResponseResult.

        **参数解释**: 实体类型。 **取值范围**: 不涉及。

        :return: The entity_type of this RecordInfoResponseResult.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        r"""Sets the entity_type of this RecordInfoResponseResult.

        **参数解释**: 实体类型。 **取值范围**: 不涉及。

        :param entity_type: The entity_type of this RecordInfoResponseResult.
        :type entity_type: str
        """
        self._entity_type = entity_type

    @property
    def job_id(self):
        r"""Gets the job_id of this RecordInfoResponseResult.

        **参数解释**: 工作流id。 **取值范围**: 不涉及。

        :return: The job_id of this RecordInfoResponseResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this RecordInfoResponseResult.

        **参数解释**: 工作流id。 **取值范围**: 不涉及。

        :param job_id: The job_id of this RecordInfoResponseResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RecordInfoResponseResult.

        **参数解释**: 实例id。 **取值范围**: 不涉及。

        :return: The instance_id of this RecordInfoResponseResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RecordInfoResponseResult.

        **参数解释**: 实例id。 **取值范围**: 不涉及。

        :param instance_id: The instance_id of this RecordInfoResponseResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def created_at(self):
        r"""Gets the created_at of this RecordInfoResponseResult.

        **参数解释**: 创建时间。 **取值范围**: 不涉及。

        :return: The created_at of this RecordInfoResponseResult.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RecordInfoResponseResult.

        **参数解释**: 创建时间。 **取值范围**: 不涉及。

        :param created_at: The created_at of this RecordInfoResponseResult.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this RecordInfoResponseResult.

        **参数解释**: 更新时间。 **取值范围**: 不涉及。

        :return: The updated_at of this RecordInfoResponseResult.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this RecordInfoResponseResult.

        **参数解释**: 更新时间。 **取值范围**: 不涉及。

        :param updated_at: The updated_at of this RecordInfoResponseResult.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def extended_info(self):
        r"""Gets the extended_info of this RecordInfoResponseResult.

        **参数解释**: 扩展信息。 **取值范围**: 不涉及。

        :return: The extended_info of this RecordInfoResponseResult.
        :rtype: object
        """
        return self._extended_info

    @extended_info.setter
    def extended_info(self, extended_info):
        r"""Sets the extended_info of this RecordInfoResponseResult.

        **参数解释**: 扩展信息。 **取值范围**: 不涉及。

        :param extended_info: The extended_info of this RecordInfoResponseResult.
        :type extended_info: object
        """
        self._extended_info = extended_info

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
        if not isinstance(other, RecordInfoResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
