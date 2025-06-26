# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSnapshotFlavorInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshot_id': 'str',
        'type': 'str',
        'az_code': 'str',
        'fine_grained_restore': 'bool'
    }

    attribute_map = {
        'snapshot_id': 'snapshot_id',
        'type': 'type',
        'az_code': 'az_code',
        'fine_grained_restore': 'fine_grained_restore'
    }

    def __init__(self, snapshot_id=None, type=None, az_code=None, fine_grained_restore=None):
        r"""ListSnapshotFlavorInfoRequest

        The model defined in huaweicloud sdk

        :param snapshot_id: **参数解释**： 快照ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type snapshot_id: str
        :param type: **参数解释**： 过滤快照规格类型，用于区分仅查询快照原始规格，还是包含可恢复的规格。 **约束限制**： 不涉及。 **取值范围**： snapshot：仅查询快照的规格信息 restore：同时查询恢复快照可用的规格信息 **默认取值**： snapshot
        :type type: str
        :param az_code: **参数解释**： 恢复时的目标可用区，用以过滤目标可用区下可恢复的规格。 恢复3az集群时需传递3个可用区编码，英文逗号分割（无空格）。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 快照原始集群所在可用区。
        :type az_code: str
        :param fine_grained_restore: **参数解释**： 是否是细粒度备份恢复，用以过滤恢复时的可用规格。 **约束限制**： 不涉及。 **取值范围**： true|false **默认取值**： false
        :type fine_grained_restore: bool
        """
        
        

        self._snapshot_id = None
        self._type = None
        self._az_code = None
        self._fine_grained_restore = None
        self.discriminator = None

        self.snapshot_id = snapshot_id
        if type is not None:
            self.type = type
        if az_code is not None:
            self.az_code = az_code
        if fine_grained_restore is not None:
            self.fine_grained_restore = fine_grained_restore

    @property
    def snapshot_id(self):
        r"""Gets the snapshot_id of this ListSnapshotFlavorInfoRequest.

        **参数解释**： 快照ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The snapshot_id of this ListSnapshotFlavorInfoRequest.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        r"""Sets the snapshot_id of this ListSnapshotFlavorInfoRequest.

        **参数解释**： 快照ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param snapshot_id: The snapshot_id of this ListSnapshotFlavorInfoRequest.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

    @property
    def type(self):
        r"""Gets the type of this ListSnapshotFlavorInfoRequest.

        **参数解释**： 过滤快照规格类型，用于区分仅查询快照原始规格，还是包含可恢复的规格。 **约束限制**： 不涉及。 **取值范围**： snapshot：仅查询快照的规格信息 restore：同时查询恢复快照可用的规格信息 **默认取值**： snapshot

        :return: The type of this ListSnapshotFlavorInfoRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListSnapshotFlavorInfoRequest.

        **参数解释**： 过滤快照规格类型，用于区分仅查询快照原始规格，还是包含可恢复的规格。 **约束限制**： 不涉及。 **取值范围**： snapshot：仅查询快照的规格信息 restore：同时查询恢复快照可用的规格信息 **默认取值**： snapshot

        :param type: The type of this ListSnapshotFlavorInfoRequest.
        :type type: str
        """
        self._type = type

    @property
    def az_code(self):
        r"""Gets the az_code of this ListSnapshotFlavorInfoRequest.

        **参数解释**： 恢复时的目标可用区，用以过滤目标可用区下可恢复的规格。 恢复3az集群时需传递3个可用区编码，英文逗号分割（无空格）。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 快照原始集群所在可用区。

        :return: The az_code of this ListSnapshotFlavorInfoRequest.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this ListSnapshotFlavorInfoRequest.

        **参数解释**： 恢复时的目标可用区，用以过滤目标可用区下可恢复的规格。 恢复3az集群时需传递3个可用区编码，英文逗号分割（无空格）。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 快照原始集群所在可用区。

        :param az_code: The az_code of this ListSnapshotFlavorInfoRequest.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def fine_grained_restore(self):
        r"""Gets the fine_grained_restore of this ListSnapshotFlavorInfoRequest.

        **参数解释**： 是否是细粒度备份恢复，用以过滤恢复时的可用规格。 **约束限制**： 不涉及。 **取值范围**： true|false **默认取值**： false

        :return: The fine_grained_restore of this ListSnapshotFlavorInfoRequest.
        :rtype: bool
        """
        return self._fine_grained_restore

    @fine_grained_restore.setter
    def fine_grained_restore(self, fine_grained_restore):
        r"""Sets the fine_grained_restore of this ListSnapshotFlavorInfoRequest.

        **参数解释**： 是否是细粒度备份恢复，用以过滤恢复时的可用规格。 **约束限制**： 不涉及。 **取值范围**： true|false **默认取值**： false

        :param fine_grained_restore: The fine_grained_restore of this ListSnapshotFlavorInfoRequest.
        :type fine_grained_restore: bool
        """
        self._fine_grained_restore = fine_grained_restore

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSnapshotFlavorInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
