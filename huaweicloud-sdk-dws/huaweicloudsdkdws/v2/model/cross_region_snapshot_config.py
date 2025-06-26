# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CrossRegionSnapshotConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'cluster_name': 'str',
        'source_region': 'str',
        'source_project_id': 'str',
        'destination_region': 'str',
        'destination_project_id': 'str',
        'status': 'bool',
        'back_keep_day': 'int',
        'total_size': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'source_region': 'source_region',
        'source_project_id': 'source_project_id',
        'destination_region': 'destination_region',
        'destination_project_id': 'destination_project_id',
        'status': 'status',
        'back_keep_day': 'back_keep_day',
        'total_size': 'total_size'
    }

    def __init__(self, cluster_id=None, cluster_name=None, source_region=None, source_project_id=None, destination_region=None, destination_project_id=None, status=None, back_keep_day=None, total_size=None):
        r"""CrossRegionSnapshotConfig

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。 **取值范围**： 36位UUID。
        :type cluster_id: str
        :param cluster_name: **参数解释**： 集群名称。 **取值范围**： 不涉及。
        :type cluster_name: str
        :param source_region: **参数解释**： 源区域。 **取值范围**： 不涉及。
        :type source_region: str
        :param source_project_id: **参数解释**： 源项目ID。 **取值范围**： 不涉及。
        :type source_project_id: str
        :param destination_region: **参数解释**： 目的区域。 **取值范围**： 不涉及。
        :type destination_region: str
        :param destination_project_id: **参数解释**： 目的项目ID。 **取值范围**： 不涉及。
        :type destination_project_id: str
        :param status: **参数解释**： 状态。 **取值范围**： 不涉及。
        :type status: bool
        :param back_keep_day: **参数解释**： 保存时间。 **取值范围**： 不涉及。
        :type back_keep_day: int
        :param total_size: **参数解释**： 总大小。 **取值范围**： 大于等于0。
        :type total_size: int
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._source_region = None
        self._source_project_id = None
        self._destination_region = None
        self._destination_project_id = None
        self._status = None
        self._back_keep_day = None
        self._total_size = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if source_region is not None:
            self.source_region = source_region
        if source_project_id is not None:
            self.source_project_id = source_project_id
        if destination_region is not None:
            self.destination_region = destination_region
        if destination_project_id is not None:
            self.destination_project_id = destination_project_id
        if status is not None:
            self.status = status
        if back_keep_day is not None:
            self.back_keep_day = back_keep_day
        if total_size is not None:
            self.total_size = total_size

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CrossRegionSnapshotConfig.

        **参数解释**： 集群ID。 **取值范围**： 36位UUID。

        :return: The cluster_id of this CrossRegionSnapshotConfig.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CrossRegionSnapshotConfig.

        **参数解释**： 集群ID。 **取值范围**： 36位UUID。

        :param cluster_id: The cluster_id of this CrossRegionSnapshotConfig.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this CrossRegionSnapshotConfig.

        **参数解释**： 集群名称。 **取值范围**： 不涉及。

        :return: The cluster_name of this CrossRegionSnapshotConfig.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this CrossRegionSnapshotConfig.

        **参数解释**： 集群名称。 **取值范围**： 不涉及。

        :param cluster_name: The cluster_name of this CrossRegionSnapshotConfig.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def source_region(self):
        r"""Gets the source_region of this CrossRegionSnapshotConfig.

        **参数解释**： 源区域。 **取值范围**： 不涉及。

        :return: The source_region of this CrossRegionSnapshotConfig.
        :rtype: str
        """
        return self._source_region

    @source_region.setter
    def source_region(self, source_region):
        r"""Sets the source_region of this CrossRegionSnapshotConfig.

        **参数解释**： 源区域。 **取值范围**： 不涉及。

        :param source_region: The source_region of this CrossRegionSnapshotConfig.
        :type source_region: str
        """
        self._source_region = source_region

    @property
    def source_project_id(self):
        r"""Gets the source_project_id of this CrossRegionSnapshotConfig.

        **参数解释**： 源项目ID。 **取值范围**： 不涉及。

        :return: The source_project_id of this CrossRegionSnapshotConfig.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        r"""Sets the source_project_id of this CrossRegionSnapshotConfig.

        **参数解释**： 源项目ID。 **取值范围**： 不涉及。

        :param source_project_id: The source_project_id of this CrossRegionSnapshotConfig.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def destination_region(self):
        r"""Gets the destination_region of this CrossRegionSnapshotConfig.

        **参数解释**： 目的区域。 **取值范围**： 不涉及。

        :return: The destination_region of this CrossRegionSnapshotConfig.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        r"""Sets the destination_region of this CrossRegionSnapshotConfig.

        **参数解释**： 目的区域。 **取值范围**： 不涉及。

        :param destination_region: The destination_region of this CrossRegionSnapshotConfig.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def destination_project_id(self):
        r"""Gets the destination_project_id of this CrossRegionSnapshotConfig.

        **参数解释**： 目的项目ID。 **取值范围**： 不涉及。

        :return: The destination_project_id of this CrossRegionSnapshotConfig.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        r"""Sets the destination_project_id of this CrossRegionSnapshotConfig.

        **参数解释**： 目的项目ID。 **取值范围**： 不涉及。

        :param destination_project_id: The destination_project_id of this CrossRegionSnapshotConfig.
        :type destination_project_id: str
        """
        self._destination_project_id = destination_project_id

    @property
    def status(self):
        r"""Gets the status of this CrossRegionSnapshotConfig.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :return: The status of this CrossRegionSnapshotConfig.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CrossRegionSnapshotConfig.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :param status: The status of this CrossRegionSnapshotConfig.
        :type status: bool
        """
        self._status = status

    @property
    def back_keep_day(self):
        r"""Gets the back_keep_day of this CrossRegionSnapshotConfig.

        **参数解释**： 保存时间。 **取值范围**： 不涉及。

        :return: The back_keep_day of this CrossRegionSnapshotConfig.
        :rtype: int
        """
        return self._back_keep_day

    @back_keep_day.setter
    def back_keep_day(self, back_keep_day):
        r"""Sets the back_keep_day of this CrossRegionSnapshotConfig.

        **参数解释**： 保存时间。 **取值范围**： 不涉及。

        :param back_keep_day: The back_keep_day of this CrossRegionSnapshotConfig.
        :type back_keep_day: int
        """
        self._back_keep_day = back_keep_day

    @property
    def total_size(self):
        r"""Gets the total_size of this CrossRegionSnapshotConfig.

        **参数解释**： 总大小。 **取值范围**： 大于等于0。

        :return: The total_size of this CrossRegionSnapshotConfig.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this CrossRegionSnapshotConfig.

        **参数解释**： 总大小。 **取值范围**： 大于等于0。

        :param total_size: The total_size of this CrossRegionSnapshotConfig.
        :type total_size: int
        """
        self._total_size = total_size

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
        if not isinstance(other, CrossRegionSnapshotConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
