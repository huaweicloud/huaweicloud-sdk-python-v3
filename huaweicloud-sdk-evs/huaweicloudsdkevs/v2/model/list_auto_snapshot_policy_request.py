# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAutoSnapshotPolicyRequest:

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
        'tags': 'str',
        'tag_key': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tags': 'tags',
        'tag_key': 'tag_key',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, id=None, name=None, tags=None, tag_key=None, enterprise_project_id=None, limit=None, offset=None, sort_key=None, sort_dir=None):
        r"""ListAutoSnapshotPolicyRequest

        The model defined in huaweicloud sdk

        :param id: 自动快照策略ID。
        :type id: str
        :param name: 自动快照策略名称。
        :type name: str
        :param tags: 自动快照策略的标签的key/value对，例如[{\&quot;key1\&quot;:\&quot;value1\&quot;}]。
        :type tags: str
        :param tag_key: 自动快照策略的标签的key。
        :type tag_key: str
        :param enterprise_project_id: 自动快照策略的企业项目ID。
        :type enterprise_project_id: str
        :param limit: 返回结果个数限制。
        :type limit: int
        :param offset: 偏移量。
        :type offset: int
        :param sort_key: 返回结果按该关键字排序，支持id，created_at等关键字，默认为“created_at”。
        :type sort_key: str
        :param sort_dir: 返回结果按照降序或升序排列，默认为“desc”。 降序：desc 升序：asc
        :type sort_dir: str
        """
        
        

        self._id = None
        self._name = None
        self._tags = None
        self._tag_key = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        if tag_key is not None:
            self.tag_key = tag_key
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

    @property
    def id(self):
        r"""Gets the id of this ListAutoSnapshotPolicyRequest.

        自动快照策略ID。

        :return: The id of this ListAutoSnapshotPolicyRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAutoSnapshotPolicyRequest.

        自动快照策略ID。

        :param id: The id of this ListAutoSnapshotPolicyRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListAutoSnapshotPolicyRequest.

        自动快照策略名称。

        :return: The name of this ListAutoSnapshotPolicyRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAutoSnapshotPolicyRequest.

        自动快照策略名称。

        :param name: The name of this ListAutoSnapshotPolicyRequest.
        :type name: str
        """
        self._name = name

    @property
    def tags(self):
        r"""Gets the tags of this ListAutoSnapshotPolicyRequest.

        自动快照策略的标签的key/value对，例如[{\"key1\":\"value1\"}]。

        :return: The tags of this ListAutoSnapshotPolicyRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListAutoSnapshotPolicyRequest.

        自动快照策略的标签的key/value对，例如[{\"key1\":\"value1\"}]。

        :param tags: The tags of this ListAutoSnapshotPolicyRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def tag_key(self):
        r"""Gets the tag_key of this ListAutoSnapshotPolicyRequest.

        自动快照策略的标签的key。

        :return: The tag_key of this ListAutoSnapshotPolicyRequest.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        r"""Sets the tag_key of this ListAutoSnapshotPolicyRequest.

        自动快照策略的标签的key。

        :param tag_key: The tag_key of this ListAutoSnapshotPolicyRequest.
        :type tag_key: str
        """
        self._tag_key = tag_key

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAutoSnapshotPolicyRequest.

        自动快照策略的企业项目ID。

        :return: The enterprise_project_id of this ListAutoSnapshotPolicyRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAutoSnapshotPolicyRequest.

        自动快照策略的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListAutoSnapshotPolicyRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAutoSnapshotPolicyRequest.

        返回结果个数限制。

        :return: The limit of this ListAutoSnapshotPolicyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAutoSnapshotPolicyRequest.

        返回结果个数限制。

        :param limit: The limit of this ListAutoSnapshotPolicyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAutoSnapshotPolicyRequest.

        偏移量。

        :return: The offset of this ListAutoSnapshotPolicyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAutoSnapshotPolicyRequest.

        偏移量。

        :param offset: The offset of this ListAutoSnapshotPolicyRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListAutoSnapshotPolicyRequest.

        返回结果按该关键字排序，支持id，created_at等关键字，默认为“created_at”。

        :return: The sort_key of this ListAutoSnapshotPolicyRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListAutoSnapshotPolicyRequest.

        返回结果按该关键字排序，支持id，created_at等关键字，默认为“created_at”。

        :param sort_key: The sort_key of this ListAutoSnapshotPolicyRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListAutoSnapshotPolicyRequest.

        返回结果按照降序或升序排列，默认为“desc”。 降序：desc 升序：asc

        :return: The sort_dir of this ListAutoSnapshotPolicyRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListAutoSnapshotPolicyRequest.

        返回结果按照降序或升序排列，默认为“desc”。 降序：desc 升序：asc

        :param sort_dir: The sort_dir of this ListAutoSnapshotPolicyRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListAutoSnapshotPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
