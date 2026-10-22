# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotsDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'volume_id': 'str',
        'availability_zone': 'str',
        'limit': 'str',
        'name': 'str',
        'offset': 'str',
        'status': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'id': 'str',
        'ids': 'str',
        'snapshot_type': 'str',
        'enterprise_project_id': 'str',
        'tag_key': 'str',
        'tags': 'str',
        'snapshot_chain_id': 'str',
        'snapshot_group_id': 'str'
    }

    attribute_map = {
        'marker': 'marker',
        'volume_id': 'volume_id',
        'availability_zone': 'availability_zone',
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'status': 'status',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'ids': 'ids',
        'snapshot_type': 'snapshot_type',
        'enterprise_project_id': 'enterprise_project_id',
        'tag_key': 'tag_key',
        'tags': 'tags',
        'snapshot_chain_id': 'snapshot_chain_id',
        'snapshot_group_id': 'snapshot_group_id'
    }

    def __init__(self, marker=None, volume_id=None, availability_zone=None, limit=None, name=None, offset=None, status=None, sort_key=None, sort_dir=None, id=None, ids=None, snapshot_type=None, enterprise_project_id=None, tag_key=None, tags=None, snapshot_chain_id=None, snapshot_group_id=None):
        r"""ListSnapshotsDetailsRequest

        The model defined in huaweicloud sdk

        :param marker: **参数解释** 分页查询的起始资源id，取值为上一页最后一条查询记录的资源id。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type marker: str
        :param volume_id: **参数解释** 快照对应的云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type volume_id: str
        :param availability_zone: **参数解释** 快照对应的云硬盘所在的可用区。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type availability_zone: str
        :param limit: **参数解释** 返回结果个数限制。  当租户所有的快照数量大于50个时，为了提升您的查询效率，建议查询的时候使用limit参数，并且参数值最大设置为50。查询示例：  GET /v2/xxx/snapshots/detail?limit&#x3D;50，表示查询第1~50个快照。GET /v2/xxx/snapshots/detail?offset&#x3D;50&amp;limit&#x3D;50，表示查询第51~100个快照。 **约束限制** 不涉及。 **取值范围** 最小值1，最大值1000，默认为1000。返回的结果中记录数不超过limit值。 **默认取值** 不涉及。
        :type limit: str
        :param name: **参数解释** 快照名称。 **约束限制** 不涉及。 **取值范围** 最大支持255个字符。 **默认取值** 不涉及。
        :type name: str
        :param offset: **参数解释** 偏移量。  分页查询快照时使用，与limit配合使用。假如共有30个快照， 设置offset为11，limit为10，即为从第12个快照开始查询， 一次最多可读取10个快照。 **约束限制** 与limit配合使用。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type offset: str
        :param status: **参数解释** 快照状态。 **约束限制** 不涉及。 **取值范围** [具体请参见[云硬盘快照状态](evs_04_0041.xml)。] **默认取值** 不涉及。
        :type status: str
        :param sort_key: **参数解释** 返回结果按该关键字排序。 **约束限制** 不涉及。 **取值范围** - id：云硬盘快照ID。 - status：云硬盘快照状态，取值可参考：\&quot;[云硬盘快照状态。](evs_04_0041.xml)\&quot;。 - size：云硬盘快照大小，单位为GiB。 - created_at：云硬盘快照创建时间。 **默认取值** created_at
        :type sort_key: str
        :param sort_dir: **参数解释** 返回结果按照降序或升序排列，默认为“desc”。  **约束限制** 不涉及。 **取值范围** - desc：降序。 - asc：升序。 **默认取值** desc
        :type sort_dir: str
        :param id: **参数解释** 快照ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type id: str
        :param ids: **参数解释** 快照id列表，多个id直接用,号隔开，格式为ids&#x3D;id1,id2,...,idx。返回有效id对应的快照信息，无效的id会被忽略。 **约束限制** 最多支持一次查询60个id。 如果“id”和“ids”查询参数同时存在，“id”会被忽略。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type ids: str
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
        :param snapshot_group_id: **参数解释** 快照一致性组ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type snapshot_group_id: str
        """
        
        

        self._marker = None
        self._volume_id = None
        self._availability_zone = None
        self._limit = None
        self._name = None
        self._offset = None
        self._status = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._ids = None
        self._snapshot_type = None
        self._enterprise_project_id = None
        self._tag_key = None
        self._tags = None
        self._snapshot_chain_id = None
        self._snapshot_group_id = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if volume_id is not None:
            self.volume_id = volume_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if id is not None:
            self.id = id
        if ids is not None:
            self.ids = ids
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
        if snapshot_group_id is not None:
            self.snapshot_group_id = snapshot_group_id

    @property
    def marker(self):
        r"""Gets the marker of this ListSnapshotsDetailsRequest.

        **参数解释** 分页查询的起始资源id，取值为上一页最后一条查询记录的资源id。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The marker of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListSnapshotsDetailsRequest.

        **参数解释** 分页查询的起始资源id，取值为上一页最后一条查询记录的资源id。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param marker: The marker of this ListSnapshotsDetailsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def volume_id(self):
        r"""Gets the volume_id of this ListSnapshotsDetailsRequest.

        **参数解释** 快照对应的云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The volume_id of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this ListSnapshotsDetailsRequest.

        **参数解释** 快照对应的云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param volume_id: The volume_id of this ListSnapshotsDetailsRequest.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListSnapshotsDetailsRequest.

        **参数解释** 快照对应的云硬盘所在的可用区。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The availability_zone of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListSnapshotsDetailsRequest.

        **参数解释** 快照对应的云硬盘所在的可用区。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param availability_zone: The availability_zone of this ListSnapshotsDetailsRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def limit(self):
        r"""Gets the limit of this ListSnapshotsDetailsRequest.

        **参数解释** 返回结果个数限制。  当租户所有的快照数量大于50个时，为了提升您的查询效率，建议查询的时候使用limit参数，并且参数值最大设置为50。查询示例：  GET /v2/xxx/snapshots/detail?limit=50，表示查询第1~50个快照。GET /v2/xxx/snapshots/detail?offset=50&limit=50，表示查询第51~100个快照。 **约束限制** 不涉及。 **取值范围** 最小值1，最大值1000，默认为1000。返回的结果中记录数不超过limit值。 **默认取值** 不涉及。

        :return: The limit of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSnapshotsDetailsRequest.

        **参数解释** 返回结果个数限制。  当租户所有的快照数量大于50个时，为了提升您的查询效率，建议查询的时候使用limit参数，并且参数值最大设置为50。查询示例：  GET /v2/xxx/snapshots/detail?limit=50，表示查询第1~50个快照。GET /v2/xxx/snapshots/detail?offset=50&limit=50，表示查询第51~100个快照。 **约束限制** 不涉及。 **取值范围** 最小值1，最大值1000，默认为1000。返回的结果中记录数不超过limit值。 **默认取值** 不涉及。

        :param limit: The limit of this ListSnapshotsDetailsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListSnapshotsDetailsRequest.

        **参数解释** 快照名称。 **约束限制** 不涉及。 **取值范围** 最大支持255个字符。 **默认取值** 不涉及。

        :return: The name of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSnapshotsDetailsRequest.

        **参数解释** 快照名称。 **约束限制** 不涉及。 **取值范围** 最大支持255个字符。 **默认取值** 不涉及。

        :param name: The name of this ListSnapshotsDetailsRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListSnapshotsDetailsRequest.

        **参数解释** 偏移量。  分页查询快照时使用，与limit配合使用。假如共有30个快照， 设置offset为11，limit为10，即为从第12个快照开始查询， 一次最多可读取10个快照。 **约束限制** 与limit配合使用。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The offset of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSnapshotsDetailsRequest.

        **参数解释** 偏移量。  分页查询快照时使用，与limit配合使用。假如共有30个快照， 设置offset为11，limit为10，即为从第12个快照开始查询， 一次最多可读取10个快照。 **约束限制** 与limit配合使用。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param offset: The offset of this ListSnapshotsDetailsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def status(self):
        r"""Gets the status of this ListSnapshotsDetailsRequest.

        **参数解释** 快照状态。 **约束限制** 不涉及。 **取值范围** [具体请参见[云硬盘快照状态](evs_04_0041.xml)。] **默认取值** 不涉及。

        :return: The status of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSnapshotsDetailsRequest.

        **参数解释** 快照状态。 **约束限制** 不涉及。 **取值范围** [具体请参见[云硬盘快照状态](evs_04_0041.xml)。] **默认取值** 不涉及。

        :param status: The status of this ListSnapshotsDetailsRequest.
        :type status: str
        """
        self._status = status

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListSnapshotsDetailsRequest.

        **参数解释** 返回结果按该关键字排序。 **约束限制** 不涉及。 **取值范围** - id：云硬盘快照ID。 - status：云硬盘快照状态，取值可参考：\"[云硬盘快照状态。](evs_04_0041.xml)\"。 - size：云硬盘快照大小，单位为GiB。 - created_at：云硬盘快照创建时间。 **默认取值** created_at

        :return: The sort_key of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListSnapshotsDetailsRequest.

        **参数解释** 返回结果按该关键字排序。 **约束限制** 不涉及。 **取值范围** - id：云硬盘快照ID。 - status：云硬盘快照状态，取值可参考：\"[云硬盘快照状态。](evs_04_0041.xml)\"。 - size：云硬盘快照大小，单位为GiB。 - created_at：云硬盘快照创建时间。 **默认取值** created_at

        :param sort_key: The sort_key of this ListSnapshotsDetailsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListSnapshotsDetailsRequest.

        **参数解释** 返回结果按照降序或升序排列，默认为“desc”。  **约束限制** 不涉及。 **取值范围** - desc：降序。 - asc：升序。 **默认取值** desc

        :return: The sort_dir of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListSnapshotsDetailsRequest.

        **参数解释** 返回结果按照降序或升序排列，默认为“desc”。  **约束限制** 不涉及。 **取值范围** - desc：降序。 - asc：升序。 **默认取值** desc

        :param sort_dir: The sort_dir of this ListSnapshotsDetailsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        r"""Gets the id of this ListSnapshotsDetailsRequest.

        **参数解释** 快照ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The id of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSnapshotsDetailsRequest.

        **参数解释** 快照ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param id: The id of this ListSnapshotsDetailsRequest.
        :type id: str
        """
        self._id = id

    @property
    def ids(self):
        r"""Gets the ids of this ListSnapshotsDetailsRequest.

        **参数解释** 快照id列表，多个id直接用,号隔开，格式为ids=id1,id2,...,idx。返回有效id对应的快照信息，无效的id会被忽略。 **约束限制** 最多支持一次查询60个id。 如果“id”和“ids”查询参数同时存在，“id”会被忽略。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The ids of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this ListSnapshotsDetailsRequest.

        **参数解释** 快照id列表，多个id直接用,号隔开，格式为ids=id1,id2,...,idx。返回有效id对应的快照信息，无效的id会被忽略。 **约束限制** 最多支持一次查询60个id。 如果“id”和“ids”查询参数同时存在，“id”会被忽略。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param ids: The ids of this ListSnapshotsDetailsRequest.
        :type ids: str
        """
        self._ids = ids

    @property
    def snapshot_type(self):
        r"""Gets the snapshot_type of this ListSnapshotsDetailsRequest.

        **参数解释** 快照来源。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The snapshot_type of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._snapshot_type

    @snapshot_type.setter
    def snapshot_type(self, snapshot_type):
        r"""Sets the snapshot_type of this ListSnapshotsDetailsRequest.

        **参数解释** 快照来源。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param snapshot_type: The snapshot_type of this ListSnapshotsDetailsRequest.
        :type snapshot_type: str
        """
        self._snapshot_type = snapshot_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListSnapshotsDetailsRequest.

        **参数解释** 快照的企业项目ID。  关于企业项目ID的获取及企业项目特性的详细信息，请参考：\"[[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws)[[企业管理用户指南](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws_hk)\"。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The enterprise_project_id of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListSnapshotsDetailsRequest.

        **参数解释** 快照的企业项目ID。  关于企业项目ID的获取及企业项目特性的详细信息，请参考：\"[[企业管理用户指南](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws)[[企业管理用户指南](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0123692049.html)](tag:hws_hk)\"。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this ListSnapshotsDetailsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tag_key(self):
        r"""Gets the tag_key of this ListSnapshotsDetailsRequest.

        **参数解释** 快照标签的key。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The tag_key of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        r"""Sets the tag_key of this ListSnapshotsDetailsRequest.

        **参数解释** 快照标签的key。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param tag_key: The tag_key of this ListSnapshotsDetailsRequest.
        :type tag_key: str
        """
        self._tag_key = tag_key

    @property
    def tags(self):
        r"""Gets the tags of this ListSnapshotsDetailsRequest.

        **参数解释** 快照标签的key/value对，例如[{\"key\":\"bbb\",\"value\":\"bbb\"}]。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The tags of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListSnapshotsDetailsRequest.

        **参数解释** 快照标签的key/value对，例如[{\"key\":\"bbb\",\"value\":\"bbb\"}]。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param tags: The tags of this ListSnapshotsDetailsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def snapshot_chain_id(self):
        r"""Gets the snapshot_chain_id of this ListSnapshotsDetailsRequest.

        **参数解释** 快照链ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The snapshot_chain_id of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._snapshot_chain_id

    @snapshot_chain_id.setter
    def snapshot_chain_id(self, snapshot_chain_id):
        r"""Sets the snapshot_chain_id of this ListSnapshotsDetailsRequest.

        **参数解释** 快照链ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param snapshot_chain_id: The snapshot_chain_id of this ListSnapshotsDetailsRequest.
        :type snapshot_chain_id: str
        """
        self._snapshot_chain_id = snapshot_chain_id

    @property
    def snapshot_group_id(self):
        r"""Gets the snapshot_group_id of this ListSnapshotsDetailsRequest.

        **参数解释** 快照一致性组ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The snapshot_group_id of this ListSnapshotsDetailsRequest.
        :rtype: str
        """
        return self._snapshot_group_id

    @snapshot_group_id.setter
    def snapshot_group_id(self, snapshot_group_id):
        r"""Sets the snapshot_group_id of this ListSnapshotsDetailsRequest.

        **参数解释** 快照一致性组ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param snapshot_group_id: The snapshot_group_id of this ListSnapshotsDetailsRequest.
        :type snapshot_group_id: str
        """
        self._snapshot_group_id = snapshot_group_id

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
        if not isinstance(other, ListSnapshotsDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
