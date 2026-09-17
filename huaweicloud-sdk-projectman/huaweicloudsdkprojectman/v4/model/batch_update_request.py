# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'assigned_to_id': 'str',
        'issue_ids': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'assigned_to_id': 'assigned_to_id',
        'issue_ids': 'issue_ids',
        'project_id': 'project_id'
    }

    def __init__(self, assigned_to_id=None, issue_ids=None, project_id=None):
        r"""BatchUpdateRequest

        The model defined in huaweicloud sdk

        :param assigned_to_id: **参数解释：** 模块的负责人数字id，通过[获取指定项目的成员用户列表](ListProjectMembersV4.xml)接口获取，响应消息体中的**user_num_id**字段的值就是模块的负责人数字id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type assigned_to_id: str
        :param issue_ids: **参数解释：** 工作项id，可通过[高级查询工作项](ListIssuesV4.xml)接口获取，响应消息体中的**id**字段的值就是工作项id。 **约束限制：** 长度在1位到10位之间的纯数字。 **取值范围：** 最小长度：1，最大长度：10。 **默认取值：** 不涉及。
        :type issue_ids: str
        :param project_id: **参数解释**： 项目的32位uuid，项目唯一标识，通过[查询项目列表](ListProjectsV4.xml)接口获取，响应消息体中的**project_id**字段的值就是项目ID。 **约束限制**： 32位的数字和字母组成的字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type project_id: str
        """
        
        

        self._assigned_to_id = None
        self._issue_ids = None
        self._project_id = None
        self.discriminator = None

        if assigned_to_id is not None:
            self.assigned_to_id = assigned_to_id
        if issue_ids is not None:
            self.issue_ids = issue_ids
        if project_id is not None:
            self.project_id = project_id

    @property
    def assigned_to_id(self):
        r"""Gets the assigned_to_id of this BatchUpdateRequest.

        **参数解释：** 模块的负责人数字id，通过[获取指定项目的成员用户列表](ListProjectMembersV4.xml)接口获取，响应消息体中的**user_num_id**字段的值就是模块的负责人数字id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The assigned_to_id of this BatchUpdateRequest.
        :rtype: str
        """
        return self._assigned_to_id

    @assigned_to_id.setter
    def assigned_to_id(self, assigned_to_id):
        r"""Sets the assigned_to_id of this BatchUpdateRequest.

        **参数解释：** 模块的负责人数字id，通过[获取指定项目的成员用户列表](ListProjectMembersV4.xml)接口获取，响应消息体中的**user_num_id**字段的值就是模块的负责人数字id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param assigned_to_id: The assigned_to_id of this BatchUpdateRequest.
        :type assigned_to_id: str
        """
        self._assigned_to_id = assigned_to_id

    @property
    def issue_ids(self):
        r"""Gets the issue_ids of this BatchUpdateRequest.

        **参数解释：** 工作项id，可通过[高级查询工作项](ListIssuesV4.xml)接口获取，响应消息体中的**id**字段的值就是工作项id。 **约束限制：** 长度在1位到10位之间的纯数字。 **取值范围：** 最小长度：1，最大长度：10。 **默认取值：** 不涉及。

        :return: The issue_ids of this BatchUpdateRequest.
        :rtype: str
        """
        return self._issue_ids

    @issue_ids.setter
    def issue_ids(self, issue_ids):
        r"""Sets the issue_ids of this BatchUpdateRequest.

        **参数解释：** 工作项id，可通过[高级查询工作项](ListIssuesV4.xml)接口获取，响应消息体中的**id**字段的值就是工作项id。 **约束限制：** 长度在1位到10位之间的纯数字。 **取值范围：** 最小长度：1，最大长度：10。 **默认取值：** 不涉及。

        :param issue_ids: The issue_ids of this BatchUpdateRequest.
        :type issue_ids: str
        """
        self._issue_ids = issue_ids

    @property
    def project_id(self):
        r"""Gets the project_id of this BatchUpdateRequest.

        **参数解释**： 项目的32位uuid，项目唯一标识，通过[查询项目列表](ListProjectsV4.xml)接口获取，响应消息体中的**project_id**字段的值就是项目ID。 **约束限制**： 32位的数字和字母组成的字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The project_id of this BatchUpdateRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BatchUpdateRequest.

        **参数解释**： 项目的32位uuid，项目唯一标识，通过[查询项目列表](ListProjectsV4.xml)接口获取，响应消息体中的**project_id**字段的值就是项目ID。 **约束限制**： 32位的数字和字母组成的字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param project_id: The project_id of this BatchUpdateRequest.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, BatchUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
