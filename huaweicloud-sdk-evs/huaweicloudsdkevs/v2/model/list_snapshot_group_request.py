# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotGroupRequest:

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
        'status': 'str',
        'tag_key': 'str',
        'tags': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'server_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'tag_key': 'tag_key',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'server_id': 'server_id'
    }

    def __init__(self, id=None, name=None, status=None, tag_key=None, tags=None, enterprise_project_id=None, limit=None, offset=None, sort_key=None, sort_dir=None, server_id=None):
        r"""ListSnapshotGroupRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释** 指定的快照一致性组ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type id: str
        :param name: **参数解释** 快照一致性组名称。 **约束限制** 最大支持255个字节。 最小长度：0 最大长度：255 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type name: str
        :param status: **参数解释** 快照一致性组的状态。 **约束限制** 不涉及。 **取值范围** - creating：创建中。 - available：创建成功。 - error：创建失败。 - deleting: 删除中。 - deleted：删除成功。 - error_deleting：删除失败。 **默认取值** 不涉及。
        :type status: str
        :param tag_key: **参数解释** 快照一致性组的标签的key。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type tag_key: str
        :param tags: **参数解释** 快照一致性组的标签的key/value对，例如[{\&quot;key\&quot;:\&quot;bbb\&quot;,\&quot;value\&quot;:\&quot;bbb\&quot;}]。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type tags: str
        :param enterprise_project_id: **参数解释** 快照一致性组的企业项目ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type enterprise_project_id: str
        :param limit: **参数解释** 返回结果个数限制。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type limit: int
        :param offset: **参数解释** 偏移量。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type offset: int
        :param sort_key: **参数解释** 返回结果按该关键字排序。 **约束限制** 不涉及。 **取值范围** - id：快照一致性组的ID。 - status：快照一致性组的状态。 - created_at：快照一致性组的创建时间。 **默认取值** created_at
        :type sort_key: str
        :param sort_dir: **参数解释** 返回结果按照降序或升序排列。 **约束限制** 不涉及。 **取值范围** - desc：降序。 - asc：升序。 **默认取值** desc
        :type sort_dir: str
        :param server_id: **参数解释** 云服务器ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type server_id: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._tag_key = None
        self._tags = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._sort_key = None
        self._sort_dir = None
        self._server_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if tag_key is not None:
            self.tag_key = tag_key
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if server_id is not None:
            self.server_id = server_id

    @property
    def id(self):
        r"""Gets the id of this ListSnapshotGroupRequest.

        **参数解释** 指定的快照一致性组ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The id of this ListSnapshotGroupRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSnapshotGroupRequest.

        **参数解释** 指定的快照一致性组ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param id: The id of this ListSnapshotGroupRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListSnapshotGroupRequest.

        **参数解释** 快照一致性组名称。 **约束限制** 最大支持255个字节。 最小长度：0 最大长度：255 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The name of this ListSnapshotGroupRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSnapshotGroupRequest.

        **参数解释** 快照一致性组名称。 **约束限制** 最大支持255个字节。 最小长度：0 最大长度：255 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param name: The name of this ListSnapshotGroupRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListSnapshotGroupRequest.

        **参数解释** 快照一致性组的状态。 **约束限制** 不涉及。 **取值范围** - creating：创建中。 - available：创建成功。 - error：创建失败。 - deleting: 删除中。 - deleted：删除成功。 - error_deleting：删除失败。 **默认取值** 不涉及。

        :return: The status of this ListSnapshotGroupRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSnapshotGroupRequest.

        **参数解释** 快照一致性组的状态。 **约束限制** 不涉及。 **取值范围** - creating：创建中。 - available：创建成功。 - error：创建失败。 - deleting: 删除中。 - deleted：删除成功。 - error_deleting：删除失败。 **默认取值** 不涉及。

        :param status: The status of this ListSnapshotGroupRequest.
        :type status: str
        """
        self._status = status

    @property
    def tag_key(self):
        r"""Gets the tag_key of this ListSnapshotGroupRequest.

        **参数解释** 快照一致性组的标签的key。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The tag_key of this ListSnapshotGroupRequest.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        r"""Sets the tag_key of this ListSnapshotGroupRequest.

        **参数解释** 快照一致性组的标签的key。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param tag_key: The tag_key of this ListSnapshotGroupRequest.
        :type tag_key: str
        """
        self._tag_key = tag_key

    @property
    def tags(self):
        r"""Gets the tags of this ListSnapshotGroupRequest.

        **参数解释** 快照一致性组的标签的key/value对，例如[{\"key\":\"bbb\",\"value\":\"bbb\"}]。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The tags of this ListSnapshotGroupRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListSnapshotGroupRequest.

        **参数解释** 快照一致性组的标签的key/value对，例如[{\"key\":\"bbb\",\"value\":\"bbb\"}]。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param tags: The tags of this ListSnapshotGroupRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListSnapshotGroupRequest.

        **参数解释** 快照一致性组的企业项目ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The enterprise_project_id of this ListSnapshotGroupRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListSnapshotGroupRequest.

        **参数解释** 快照一致性组的企业项目ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this ListSnapshotGroupRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListSnapshotGroupRequest.

        **参数解释** 返回结果个数限制。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The limit of this ListSnapshotGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSnapshotGroupRequest.

        **参数解释** 返回结果个数限制。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param limit: The limit of this ListSnapshotGroupRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSnapshotGroupRequest.

        **参数解释** 偏移量。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The offset of this ListSnapshotGroupRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSnapshotGroupRequest.

        **参数解释** 偏移量。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param offset: The offset of this ListSnapshotGroupRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListSnapshotGroupRequest.

        **参数解释** 返回结果按该关键字排序。 **约束限制** 不涉及。 **取值范围** - id：快照一致性组的ID。 - status：快照一致性组的状态。 - created_at：快照一致性组的创建时间。 **默认取值** created_at

        :return: The sort_key of this ListSnapshotGroupRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListSnapshotGroupRequest.

        **参数解释** 返回结果按该关键字排序。 **约束限制** 不涉及。 **取值范围** - id：快照一致性组的ID。 - status：快照一致性组的状态。 - created_at：快照一致性组的创建时间。 **默认取值** created_at

        :param sort_key: The sort_key of this ListSnapshotGroupRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListSnapshotGroupRequest.

        **参数解释** 返回结果按照降序或升序排列。 **约束限制** 不涉及。 **取值范围** - desc：降序。 - asc：升序。 **默认取值** desc

        :return: The sort_dir of this ListSnapshotGroupRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListSnapshotGroupRequest.

        **参数解释** 返回结果按照降序或升序排列。 **约束限制** 不涉及。 **取值范围** - desc：降序。 - asc：升序。 **默认取值** desc

        :param sort_dir: The sort_dir of this ListSnapshotGroupRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def server_id(self):
        r"""Gets the server_id of this ListSnapshotGroupRequest.

        **参数解释** 云服务器ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The server_id of this ListSnapshotGroupRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ListSnapshotGroupRequest.

        **参数解释** 云服务器ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param server_id: The server_id of this ListSnapshotGroupRequest.
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
        if not isinstance(other, ListSnapshotGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
