# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountSnapshotsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_id': 'str',
        'availability_zone': 'str',
        'name': 'str',
        'status': 'str',
        'id': 'str',
        'snapshot_type': 'str',
        'enterprise_project_id': 'str',
        'tag_key': 'str',
        'tags': 'str',
        'snapshot_chain_id': 'str'
    }

    attribute_map = {
        'volume_id': 'volume_id',
        'availability_zone': 'availability_zone',
        'name': 'name',
        'status': 'status',
        'id': 'id',
        'snapshot_type': 'snapshot_type',
        'enterprise_project_id': 'enterprise_project_id',
        'tag_key': 'tag_key',
        'tags': 'tags',
        'snapshot_chain_id': 'snapshot_chain_id'
    }

    def __init__(self, volume_id=None, availability_zone=None, name=None, status=None, id=None, snapshot_type=None, enterprise_project_id=None, tag_key=None, tags=None, snapshot_chain_id=None):
        r"""CountSnapshotsRequest

        The model defined in huaweicloud sdk

        :param volume_id: **参数解释** 快照对应的云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type volume_id: str
        :param availability_zone: **参数解释** 快照对应的云硬盘所在的可用区。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type availability_zone: str
        :param name: **参数解释** 快照名称。 **约束限制** 不涉及。 **取值范围** 最大支持64个字符。 **默认取值** 不涉及。
        :type name: str
        :param status: **参数解释** 快照状态。 **约束限制** 最大支持255个字符。 **取值范围** [具体请参见[云硬盘快照状态](evs_04_0041.xml)。] **默认取值** 不涉及。
        :type status: str
        :param id: **参数解释** 快照ID。 可通过[查询云硬盘快照详情列表](evs_04_2021.xml)接口获取云硬盘快照ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type id: str
        :param snapshot_type: **参数解释** 快照来源。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type snapshot_type: str
        :param enterprise_project_id: **参数解释** 快照的企业项目ID。  关于企业项目ID的获取及企业项目特性的详细信息，请参考：\&quot;[[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws)[[企业管理用户指南](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws_hk)\&quot;。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type enterprise_project_id: str
        :param tag_key: **参数解释** 快照标签的key。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type tag_key: str
        :param tags: **参数解释** 快照标签的key/value对，例如[{\&quot;key\&quot;:\&quot;bbb\&quot;,\&quot;value\&quot;:\&quot;bbb\&quot;}]。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type tags: str
        :param snapshot_chain_id: **参数解释** 快照链ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type snapshot_chain_id: str
        """
        
        

        self._volume_id = None
        self._availability_zone = None
        self._name = None
        self._status = None
        self._id = None
        self._snapshot_type = None
        self._enterprise_project_id = None
        self._tag_key = None
        self._tags = None
        self._snapshot_chain_id = None
        self.discriminator = None

        if volume_id is not None:
            self.volume_id = volume_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if snapshot_type is not None:
            self.snapshot_type = snapshot_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tag_key is not None:
            self.tag_key = tag_key
        if tags is not None:
            self.tags = tags
        if snapshot_chain_id is not None:
            self.snapshot_chain_id = snapshot_chain_id

    @property
    def volume_id(self):
        r"""Gets the volume_id of this CountSnapshotsRequest.

        **参数解释** 快照对应的云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The volume_id of this CountSnapshotsRequest.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this CountSnapshotsRequest.

        **参数解释** 快照对应的云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param volume_id: The volume_id of this CountSnapshotsRequest.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CountSnapshotsRequest.

        **参数解释** 快照对应的云硬盘所在的可用区。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The availability_zone of this CountSnapshotsRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CountSnapshotsRequest.

        **参数解释** 快照对应的云硬盘所在的可用区。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param availability_zone: The availability_zone of this CountSnapshotsRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def name(self):
        r"""Gets the name of this CountSnapshotsRequest.

        **参数解释** 快照名称。 **约束限制** 不涉及。 **取值范围** 最大支持64个字符。 **默认取值** 不涉及。

        :return: The name of this CountSnapshotsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CountSnapshotsRequest.

        **参数解释** 快照名称。 **约束限制** 不涉及。 **取值范围** 最大支持64个字符。 **默认取值** 不涉及。

        :param name: The name of this CountSnapshotsRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this CountSnapshotsRequest.

        **参数解释** 快照状态。 **约束限制** 最大支持255个字符。 **取值范围** [具体请参见[云硬盘快照状态](evs_04_0041.xml)。] **默认取值** 不涉及。

        :return: The status of this CountSnapshotsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CountSnapshotsRequest.

        **参数解释** 快照状态。 **约束限制** 最大支持255个字符。 **取值范围** [具体请参见[云硬盘快照状态](evs_04_0041.xml)。] **默认取值** 不涉及。

        :param status: The status of this CountSnapshotsRequest.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        r"""Gets the id of this CountSnapshotsRequest.

        **参数解释** 快照ID。 可通过[查询云硬盘快照详情列表](evs_04_2021.xml)接口获取云硬盘快照ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The id of this CountSnapshotsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CountSnapshotsRequest.

        **参数解释** 快照ID。 可通过[查询云硬盘快照详情列表](evs_04_2021.xml)接口获取云硬盘快照ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param id: The id of this CountSnapshotsRequest.
        :type id: str
        """
        self._id = id

    @property
    def snapshot_type(self):
        r"""Gets the snapshot_type of this CountSnapshotsRequest.

        **参数解释** 快照来源。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The snapshot_type of this CountSnapshotsRequest.
        :rtype: str
        """
        return self._snapshot_type

    @snapshot_type.setter
    def snapshot_type(self, snapshot_type):
        r"""Sets the snapshot_type of this CountSnapshotsRequest.

        **参数解释** 快照来源。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param snapshot_type: The snapshot_type of this CountSnapshotsRequest.
        :type snapshot_type: str
        """
        self._snapshot_type = snapshot_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CountSnapshotsRequest.

        **参数解释** 快照的企业项目ID。  关于企业项目ID的获取及企业项目特性的详细信息，请参考：\"[[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws)[[企业管理用户指南](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws_hk)\"。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The enterprise_project_id of this CountSnapshotsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CountSnapshotsRequest.

        **参数解释** 快照的企业项目ID。  关于企业项目ID的获取及企业项目特性的详细信息，请参考：\"[[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws)[[企业管理用户指南](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws_hk)\"。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this CountSnapshotsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tag_key(self):
        r"""Gets the tag_key of this CountSnapshotsRequest.

        **参数解释** 快照标签的key。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The tag_key of this CountSnapshotsRequest.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        r"""Sets the tag_key of this CountSnapshotsRequest.

        **参数解释** 快照标签的key。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param tag_key: The tag_key of this CountSnapshotsRequest.
        :type tag_key: str
        """
        self._tag_key = tag_key

    @property
    def tags(self):
        r"""Gets the tags of this CountSnapshotsRequest.

        **参数解释** 快照标签的key/value对，例如[{\"key\":\"bbb\",\"value\":\"bbb\"}]。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The tags of this CountSnapshotsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CountSnapshotsRequest.

        **参数解释** 快照标签的key/value对，例如[{\"key\":\"bbb\",\"value\":\"bbb\"}]。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param tags: The tags of this CountSnapshotsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def snapshot_chain_id(self):
        r"""Gets the snapshot_chain_id of this CountSnapshotsRequest.

        **参数解释** 快照链ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The snapshot_chain_id of this CountSnapshotsRequest.
        :rtype: str
        """
        return self._snapshot_chain_id

    @snapshot_chain_id.setter
    def snapshot_chain_id(self, snapshot_chain_id):
        r"""Sets the snapshot_chain_id of this CountSnapshotsRequest.

        **参数解释** 快照链ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param snapshot_chain_id: The snapshot_chain_id of this CountSnapshotsRequest.
        :type snapshot_chain_id: str
        """
        self._snapshot_chain_id = snapshot_chain_id

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
        if not isinstance(other, CountSnapshotsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
