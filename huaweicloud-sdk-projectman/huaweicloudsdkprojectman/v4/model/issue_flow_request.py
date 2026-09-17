# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueFlowRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status_id': 'int',
        'assigned_to_id': 'str',
        'notes': 'str',
        'project_uu_id': 'str',
        'id': 'int',
        'type': 'str'
    }

    attribute_map = {
        'status_id': 'status_id',
        'assigned_to_id': 'assigned_to_id',
        'notes': 'notes',
        'project_uu_id': 'projectUUId',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, status_id=None, assigned_to_id=None, notes=None, project_uu_id=None, id=None, type=None):
        r"""IssueFlowRequest

        The model defined in huaweicloud sdk

        :param status_id: **参数解释**： 状态id。 **约束限制**： 不涉及。 **取值范围**： 1（新建） 2（进行中） 3（已解决） 4（测试中） 5（已关闭） 6（已拒绝）。 **默认取值**： 不涉及。
        :type status_id: int
        :param assigned_to_id: **参数解释：** 模块的负责人id，通过[获取指定项目的成员用户列表](ListProjectMembersV4.xml)接口获取，响应消息体中的**user_id**字段的值就是模块的负责人id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type assigned_to_id: str
        :param notes: **参数解释：** 与日志记录相关的备注或注释。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type notes: str
        :param project_uu_id: **参数解释**： 项目的32位uuid，项目唯一标识，通过[查询项目列表](ListProjectsV4.xml)接口获取，响应消息体中的**project_id**字段的值就是项目ID。 **约束限制**： 32位的数字和字母组成的字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type project_uu_id: str
        :param id: **参数解释：** 工作项id，可通过[高级查询工作项](ListIssuesV4.xml)接口获取，响应消息体中的**id**字段的值就是工作项id。 **约束限制：** 长度在1位到10位之间的纯数字。 **取值范围：** 最小长度：1，最大长度：10。 **默认取值：** 不涉及。
        :type id: int
        :param type: **参数解释：** 项目状态。 **约束限制**： 不涉及。 **取值范围**： scrum。 **默认取值**： 不涉及。
        :type type: str
        """
        
        

        self._status_id = None
        self._assigned_to_id = None
        self._notes = None
        self._project_uu_id = None
        self._id = None
        self._type = None
        self.discriminator = None

        if status_id is not None:
            self.status_id = status_id
        if assigned_to_id is not None:
            self.assigned_to_id = assigned_to_id
        if notes is not None:
            self.notes = notes
        if project_uu_id is not None:
            self.project_uu_id = project_uu_id
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type

    @property
    def status_id(self):
        r"""Gets the status_id of this IssueFlowRequest.

        **参数解释**： 状态id。 **约束限制**： 不涉及。 **取值范围**： 1（新建） 2（进行中） 3（已解决） 4（测试中） 5（已关闭） 6（已拒绝）。 **默认取值**： 不涉及。

        :return: The status_id of this IssueFlowRequest.
        :rtype: int
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        r"""Sets the status_id of this IssueFlowRequest.

        **参数解释**： 状态id。 **约束限制**： 不涉及。 **取值范围**： 1（新建） 2（进行中） 3（已解决） 4（测试中） 5（已关闭） 6（已拒绝）。 **默认取值**： 不涉及。

        :param status_id: The status_id of this IssueFlowRequest.
        :type status_id: int
        """
        self._status_id = status_id

    @property
    def assigned_to_id(self):
        r"""Gets the assigned_to_id of this IssueFlowRequest.

        **参数解释：** 模块的负责人id，通过[获取指定项目的成员用户列表](ListProjectMembersV4.xml)接口获取，响应消息体中的**user_id**字段的值就是模块的负责人id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The assigned_to_id of this IssueFlowRequest.
        :rtype: str
        """
        return self._assigned_to_id

    @assigned_to_id.setter
    def assigned_to_id(self, assigned_to_id):
        r"""Sets the assigned_to_id of this IssueFlowRequest.

        **参数解释：** 模块的负责人id，通过[获取指定项目的成员用户列表](ListProjectMembersV4.xml)接口获取，响应消息体中的**user_id**字段的值就是模块的负责人id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param assigned_to_id: The assigned_to_id of this IssueFlowRequest.
        :type assigned_to_id: str
        """
        self._assigned_to_id = assigned_to_id

    @property
    def notes(self):
        r"""Gets the notes of this IssueFlowRequest.

        **参数解释：** 与日志记录相关的备注或注释。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The notes of this IssueFlowRequest.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        r"""Sets the notes of this IssueFlowRequest.

        **参数解释：** 与日志记录相关的备注或注释。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param notes: The notes of this IssueFlowRequest.
        :type notes: str
        """
        self._notes = notes

    @property
    def project_uu_id(self):
        r"""Gets the project_uu_id of this IssueFlowRequest.

        **参数解释**： 项目的32位uuid，项目唯一标识，通过[查询项目列表](ListProjectsV4.xml)接口获取，响应消息体中的**project_id**字段的值就是项目ID。 **约束限制**： 32位的数字和字母组成的字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The project_uu_id of this IssueFlowRequest.
        :rtype: str
        """
        return self._project_uu_id

    @project_uu_id.setter
    def project_uu_id(self, project_uu_id):
        r"""Sets the project_uu_id of this IssueFlowRequest.

        **参数解释**： 项目的32位uuid，项目唯一标识，通过[查询项目列表](ListProjectsV4.xml)接口获取，响应消息体中的**project_id**字段的值就是项目ID。 **约束限制**： 32位的数字和字母组成的字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param project_uu_id: The project_uu_id of this IssueFlowRequest.
        :type project_uu_id: str
        """
        self._project_uu_id = project_uu_id

    @property
    def id(self):
        r"""Gets the id of this IssueFlowRequest.

        **参数解释：** 工作项id，可通过[高级查询工作项](ListIssuesV4.xml)接口获取，响应消息体中的**id**字段的值就是工作项id。 **约束限制：** 长度在1位到10位之间的纯数字。 **取值范围：** 最小长度：1，最大长度：10。 **默认取值：** 不涉及。

        :return: The id of this IssueFlowRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IssueFlowRequest.

        **参数解释：** 工作项id，可通过[高级查询工作项](ListIssuesV4.xml)接口获取，响应消息体中的**id**字段的值就是工作项id。 **约束限制：** 长度在1位到10位之间的纯数字。 **取值范围：** 最小长度：1，最大长度：10。 **默认取值：** 不涉及。

        :param id: The id of this IssueFlowRequest.
        :type id: int
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this IssueFlowRequest.

        **参数解释：** 项目状态。 **约束限制**： 不涉及。 **取值范围**： scrum。 **默认取值**： 不涉及。

        :return: The type of this IssueFlowRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IssueFlowRequest.

        **参数解释：** 项目状态。 **约束限制**： 不涉及。 **取值范围**： scrum。 **默认取值**： 不涉及。

        :param type: The type of this IssueFlowRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, IssueFlowRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
