# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountSnapshotsGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'id': 'str',
        'enterprise_project_id': 'str',
        'tag_key': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'id': 'id',
        'enterprise_project_id': 'enterprise_project_id',
        'tag_key': 'tag_key',
        'tags': 'tags'
    }

    def __init__(self, name=None, status=None, id=None, enterprise_project_id=None, tag_key=None, tags=None):
        r"""CountSnapshotsGroupRequest

        The model defined in huaweicloud sdk

        :param name: **参数解释** 快照一致性组的名称。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type name: str
        :param status: **参数解释** 快照一致性组的状态。 **约束限制** 不涉及。 **取值范围** - creating：创建中。 - available：创建成功。 - error：创建失败。 - deleting: 删除中。 - deleted：删除成功。 - error_deleting：删除失败。 **默认取值** 不涉及。
        :type status: str
        :param id: **参数解释** 指定的快照一致性组ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type id: str
        :param enterprise_project_id: **参数解释** 快照一致性组的企业项目ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type enterprise_project_id: str
        :param tag_key: **参数解释** 快照一致性组的标签的key。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type tag_key: str
        :param tags: **参数解释** 快照一致性组的标签的key/value对，例如[{\&quot;key\&quot;:\&quot;bbb\&quot;,\&quot;value\&quot;:\&quot;bbb\&quot;}]。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type tags: str
        """
        
        

        self._name = None
        self._status = None
        self._id = None
        self._enterprise_project_id = None
        self._tag_key = None
        self._tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tag_key is not None:
            self.tag_key = tag_key
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CountSnapshotsGroupRequest.

        **参数解释** 快照一致性组的名称。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The name of this CountSnapshotsGroupRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CountSnapshotsGroupRequest.

        **参数解释** 快照一致性组的名称。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param name: The name of this CountSnapshotsGroupRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this CountSnapshotsGroupRequest.

        **参数解释** 快照一致性组的状态。 **约束限制** 不涉及。 **取值范围** - creating：创建中。 - available：创建成功。 - error：创建失败。 - deleting: 删除中。 - deleted：删除成功。 - error_deleting：删除失败。 **默认取值** 不涉及。

        :return: The status of this CountSnapshotsGroupRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CountSnapshotsGroupRequest.

        **参数解释** 快照一致性组的状态。 **约束限制** 不涉及。 **取值范围** - creating：创建中。 - available：创建成功。 - error：创建失败。 - deleting: 删除中。 - deleted：删除成功。 - error_deleting：删除失败。 **默认取值** 不涉及。

        :param status: The status of this CountSnapshotsGroupRequest.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        r"""Gets the id of this CountSnapshotsGroupRequest.

        **参数解释** 指定的快照一致性组ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The id of this CountSnapshotsGroupRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CountSnapshotsGroupRequest.

        **参数解释** 指定的快照一致性组ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param id: The id of this CountSnapshotsGroupRequest.
        :type id: str
        """
        self._id = id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CountSnapshotsGroupRequest.

        **参数解释** 快照一致性组的企业项目ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The enterprise_project_id of this CountSnapshotsGroupRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CountSnapshotsGroupRequest.

        **参数解释** 快照一致性组的企业项目ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this CountSnapshotsGroupRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tag_key(self):
        r"""Gets the tag_key of this CountSnapshotsGroupRequest.

        **参数解释** 快照一致性组的标签的key。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The tag_key of this CountSnapshotsGroupRequest.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        r"""Sets the tag_key of this CountSnapshotsGroupRequest.

        **参数解释** 快照一致性组的标签的key。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param tag_key: The tag_key of this CountSnapshotsGroupRequest.
        :type tag_key: str
        """
        self._tag_key = tag_key

    @property
    def tags(self):
        r"""Gets the tags of this CountSnapshotsGroupRequest.

        **参数解释** 快照一致性组的标签的key/value对，例如[{\"key\":\"bbb\",\"value\":\"bbb\"}]。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The tags of this CountSnapshotsGroupRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CountSnapshotsGroupRequest.

        **参数解释** 快照一致性组的标签的key/value对，例如[{\"key\":\"bbb\",\"value\":\"bbb\"}]。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param tags: The tags of this CountSnapshotsGroupRequest.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, CountSnapshotsGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
