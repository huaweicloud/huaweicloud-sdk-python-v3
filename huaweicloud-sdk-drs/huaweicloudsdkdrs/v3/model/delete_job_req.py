# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_type': 'str',
        'job_id': 'str',
        'is_show_breakpoint_position': 'bool'
    }

    attribute_map = {
        'delete_type': 'delete_type',
        'job_id': 'job_id',
        'is_show_breakpoint_position': 'is_show_breakpoint_position'
    }

    def __init__(self, delete_type=None, job_id=None, is_show_breakpoint_position=None):
        r"""DeleteJobReq

        The model defined in huaweicloud sdk

        :param delete_type: **参数解释**：  批量结束或删除任务的操作类型，指定对任务执行结束还是删除操作。  **约束限制**：  包年/包月任务需要先手动退订，然后delete_type参数设置为delete调用该接口删除任务。  **取值范围**：  - terminate：结束任务 - force_terminate：强制结束任务 - delete：删除任务 - roll_back_upgrade_active_standby：转主备任务回滚  **默认取值**：  不涉及
        :type delete_type: str
        :param job_id: **参数解释**：  任务ID，用于唯一标识需要结束或删除的数据复制任务。  **约束限制**：  不涉及。  **取值范围**：  UUID格式字符串。  **默认取值**：  不涉及
        :type job_id: str
        :param is_show_breakpoint_position: **参数解释**：  MySQL为源的数据复制任务，结束任务时是否展示断点信息。  **约束限制**：  仅MySQL为源的实时迁移、实时同步、实时灾备任务适用。  **取值范围**：  - true：展示断点信息 - false：不展示断点信息  **默认取值**：  不涉及
        :type is_show_breakpoint_position: bool
        """
        
        

        self._delete_type = None
        self._job_id = None
        self._is_show_breakpoint_position = None
        self.discriminator = None

        self.delete_type = delete_type
        self.job_id = job_id
        if is_show_breakpoint_position is not None:
            self.is_show_breakpoint_position = is_show_breakpoint_position

    @property
    def delete_type(self):
        r"""Gets the delete_type of this DeleteJobReq.

        **参数解释**：  批量结束或删除任务的操作类型，指定对任务执行结束还是删除操作。  **约束限制**：  包年/包月任务需要先手动退订，然后delete_type参数设置为delete调用该接口删除任务。  **取值范围**：  - terminate：结束任务 - force_terminate：强制结束任务 - delete：删除任务 - roll_back_upgrade_active_standby：转主备任务回滚  **默认取值**：  不涉及

        :return: The delete_type of this DeleteJobReq.
        :rtype: str
        """
        return self._delete_type

    @delete_type.setter
    def delete_type(self, delete_type):
        r"""Sets the delete_type of this DeleteJobReq.

        **参数解释**：  批量结束或删除任务的操作类型，指定对任务执行结束还是删除操作。  **约束限制**：  包年/包月任务需要先手动退订，然后delete_type参数设置为delete调用该接口删除任务。  **取值范围**：  - terminate：结束任务 - force_terminate：强制结束任务 - delete：删除任务 - roll_back_upgrade_active_standby：转主备任务回滚  **默认取值**：  不涉及

        :param delete_type: The delete_type of this DeleteJobReq.
        :type delete_type: str
        """
        self._delete_type = delete_type

    @property
    def job_id(self):
        r"""Gets the job_id of this DeleteJobReq.

        **参数解释**：  任务ID，用于唯一标识需要结束或删除的数据复制任务。  **约束限制**：  不涉及。  **取值范围**：  UUID格式字符串。  **默认取值**：  不涉及

        :return: The job_id of this DeleteJobReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DeleteJobReq.

        **参数解释**：  任务ID，用于唯一标识需要结束或删除的数据复制任务。  **约束限制**：  不涉及。  **取值范围**：  UUID格式字符串。  **默认取值**：  不涉及

        :param job_id: The job_id of this DeleteJobReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def is_show_breakpoint_position(self):
        r"""Gets the is_show_breakpoint_position of this DeleteJobReq.

        **参数解释**：  MySQL为源的数据复制任务，结束任务时是否展示断点信息。  **约束限制**：  仅MySQL为源的实时迁移、实时同步、实时灾备任务适用。  **取值范围**：  - true：展示断点信息 - false：不展示断点信息  **默认取值**：  不涉及

        :return: The is_show_breakpoint_position of this DeleteJobReq.
        :rtype: bool
        """
        return self._is_show_breakpoint_position

    @is_show_breakpoint_position.setter
    def is_show_breakpoint_position(self, is_show_breakpoint_position):
        r"""Sets the is_show_breakpoint_position of this DeleteJobReq.

        **参数解释**：  MySQL为源的数据复制任务，结束任务时是否展示断点信息。  **约束限制**：  仅MySQL为源的实时迁移、实时同步、实时灾备任务适用。  **取值范围**：  - true：展示断点信息 - false：不展示断点信息  **默认取值**：  不涉及

        :param is_show_breakpoint_position: The is_show_breakpoint_position of this DeleteJobReq.
        :type is_show_breakpoint_position: bool
        """
        self._is_show_breakpoint_position = is_show_breakpoint_position

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
        if not isinstance(other, DeleteJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
