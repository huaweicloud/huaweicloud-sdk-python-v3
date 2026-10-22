# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountAutoSnapshotPoliciesRequest:

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
        'tag_key': 'str',
        'tags': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tag_key': 'tag_key',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, tag_key=None, tags=None, enterprise_project_id=None):
        r"""CountAutoSnapshotPoliciesRequest

        The model defined in huaweicloud sdk

        :param id: 自动快照策略ID。
        :type id: str
        :param name: 自动快照策略名称。
        :type name: str
        :param tag_key: 自动快照策略的标签的key。
        :type tag_key: str
        :param tags: 自动快照策略的标签的key/value对，例如[{\&quot;key1\&quot;:\&quot;value1\&quot;}]。
        :type tags: str
        :param enterprise_project_id: 自动快照策略的企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._tag_key = None
        self._tags = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tag_key is not None:
            self.tag_key = tag_key
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this CountAutoSnapshotPoliciesRequest.

        自动快照策略ID。

        :return: The id of this CountAutoSnapshotPoliciesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CountAutoSnapshotPoliciesRequest.

        自动快照策略ID。

        :param id: The id of this CountAutoSnapshotPoliciesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CountAutoSnapshotPoliciesRequest.

        自动快照策略名称。

        :return: The name of this CountAutoSnapshotPoliciesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CountAutoSnapshotPoliciesRequest.

        自动快照策略名称。

        :param name: The name of this CountAutoSnapshotPoliciesRequest.
        :type name: str
        """
        self._name = name

    @property
    def tag_key(self):
        r"""Gets the tag_key of this CountAutoSnapshotPoliciesRequest.

        自动快照策略的标签的key。

        :return: The tag_key of this CountAutoSnapshotPoliciesRequest.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        r"""Sets the tag_key of this CountAutoSnapshotPoliciesRequest.

        自动快照策略的标签的key。

        :param tag_key: The tag_key of this CountAutoSnapshotPoliciesRequest.
        :type tag_key: str
        """
        self._tag_key = tag_key

    @property
    def tags(self):
        r"""Gets the tags of this CountAutoSnapshotPoliciesRequest.

        自动快照策略的标签的key/value对，例如[{\"key1\":\"value1\"}]。

        :return: The tags of this CountAutoSnapshotPoliciesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CountAutoSnapshotPoliciesRequest.

        自动快照策略的标签的key/value对，例如[{\"key1\":\"value1\"}]。

        :param tags: The tags of this CountAutoSnapshotPoliciesRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CountAutoSnapshotPoliciesRequest.

        自动快照策略的企业项目ID。

        :return: The enterprise_project_id of this CountAutoSnapshotPoliciesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CountAutoSnapshotPoliciesRequest.

        自动快照策略的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CountAutoSnapshotPoliciesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CountAutoSnapshotPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
