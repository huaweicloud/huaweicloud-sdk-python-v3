# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotGroupDetail:

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
        'project_id': 'str',
        'created_at': 'str',
        'status': 'str',
        'updated_at': 'str',
        'name': 'str',
        'description': 'str',
        'enterprise_project_id': 'str',
        'tags': 'dict(str, str)',
        'server_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'created_at': 'created_at',
        'status': 'status',
        'updated_at': 'updated_at',
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'server_id': 'server_id'
    }

    def __init__(self, id=None, project_id=None, created_at=None, status=None, updated_at=None, name=None, description=None, enterprise_project_id=None, tags=None, server_id=None):
        r"""SnapshotGroupDetail

        The model defined in huaweicloud sdk

        :param id: **参数解释** 快照一致性组的ID。 **取值范围** 不涉及。
        :type id: str
        :param project_id: **参数解释** 快照一致性组的项目ID。 **取值范围** 不涉及。
        :type project_id: str
        :param created_at: **参数解释** 快照一致性组的创建时间。 **取值范围** 不涉及。
        :type created_at: str
        :param status: **参数解释** 快照一致性组的状态。 **取值范围** - creating：创建中。 - available：创建成功。 - error：创建失败。 - deleting: 删除中。 - deleted：删除成功。 - error_deleting：删除失败。
        :type status: str
        :param updated_at: **参数解释** 快照一致性组的更新时间。 **取值范围** 不涉及。
        :type updated_at: str
        :param name: **参数解释** 快照一致性组的名称。 **取值范围** 不涉及。
        :type name: str
        :param description: **参数解释** 快照一致性组的描述。 **取值范围** 不涉及。
        :type description: str
        :param enterprise_project_id: **参数解释** 快照一致性组的企业项目id。 **取值范围** 不涉及。
        :type enterprise_project_id: str
        :param tags: **参数解释** 快照一致性组的标签。 标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。  标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。 **取值范围** 不涉及。
        :type tags: dict(str, str)
        :param server_id: **参数解释** 云服务器id。 **取值范围** 不涉及。
        :type server_id: str
        """
        
        

        self._id = None
        self._project_id = None
        self._created_at = None
        self._status = None
        self._updated_at = None
        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self._tags = None
        self._server_id = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.created_at = created_at
        self.status = status
        self.updated_at = updated_at
        self.name = name
        self.description = description
        self.enterprise_project_id = enterprise_project_id
        self.tags = tags
        self.server_id = server_id

    @property
    def id(self):
        r"""Gets the id of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的ID。 **取值范围** 不涉及。

        :return: The id of this SnapshotGroupDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的ID。 **取值范围** 不涉及。

        :param id: The id of this SnapshotGroupDetail.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的项目ID。 **取值范围** 不涉及。

        :return: The project_id of this SnapshotGroupDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的项目ID。 **取值范围** 不涉及。

        :param project_id: The project_id of this SnapshotGroupDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def created_at(self):
        r"""Gets the created_at of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的创建时间。 **取值范围** 不涉及。

        :return: The created_at of this SnapshotGroupDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的创建时间。 **取值范围** 不涉及。

        :param created_at: The created_at of this SnapshotGroupDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def status(self):
        r"""Gets the status of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的状态。 **取值范围** - creating：创建中。 - available：创建成功。 - error：创建失败。 - deleting: 删除中。 - deleted：删除成功。 - error_deleting：删除失败。

        :return: The status of this SnapshotGroupDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的状态。 **取值范围** - creating：创建中。 - available：创建成功。 - error：创建失败。 - deleting: 删除中。 - deleted：删除成功。 - error_deleting：删除失败。

        :param status: The status of this SnapshotGroupDetail.
        :type status: str
        """
        self._status = status

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的更新时间。 **取值范围** 不涉及。

        :return: The updated_at of this SnapshotGroupDetail.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的更新时间。 **取值范围** 不涉及。

        :param updated_at: The updated_at of this SnapshotGroupDetail.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def name(self):
        r"""Gets the name of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的名称。 **取值范围** 不涉及。

        :return: The name of this SnapshotGroupDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的名称。 **取值范围** 不涉及。

        :param name: The name of this SnapshotGroupDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的描述。 **取值范围** 不涉及。

        :return: The description of this SnapshotGroupDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的描述。 **取值范围** 不涉及。

        :param description: The description of this SnapshotGroupDetail.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的企业项目id。 **取值范围** 不涉及。

        :return: The enterprise_project_id of this SnapshotGroupDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的企业项目id。 **取值范围** 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this SnapshotGroupDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的标签。 标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。  标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。 **取值范围** 不涉及。

        :return: The tags of this SnapshotGroupDetail.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SnapshotGroupDetail.

        **参数解释** 快照一致性组的标签。 标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。  标签的value：String类型，最大长度43个字符，可以为空字符串。 由英文字母、数字、下划线、点、中划线、UNICODE字符（\\u4E00-\\u9FFF）组成。 **取值范围** 不涉及。

        :param tags: The tags of this SnapshotGroupDetail.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def server_id(self):
        r"""Gets the server_id of this SnapshotGroupDetail.

        **参数解释** 云服务器id。 **取值范围** 不涉及。

        :return: The server_id of this SnapshotGroupDetail.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this SnapshotGroupDetail.

        **参数解释** 云服务器id。 **取值范围** 不涉及。

        :param server_id: The server_id of this SnapshotGroupDetail.
        :type server_id: str
        """
        self._server_id = server_id

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
        if not isinstance(other, SnapshotGroupDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
