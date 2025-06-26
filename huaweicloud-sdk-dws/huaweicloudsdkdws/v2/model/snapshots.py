# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Snapshots:

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
        'description': 'str',
        'started': 'str',
        'finished': 'str',
        'size': 'float',
        'status': 'str',
        'type': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'started': 'started',
        'finished': 'finished',
        'size': 'size',
        'status': 'status',
        'type': 'type',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, id=None, name=None, description=None, started=None, finished=None, size=None, status=None, type=None, cluster_id=None):
        r"""Snapshots

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 快照ID。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 快照名称。 **取值范围**： 不涉及。
        :type name: str
        :param description: **参数解释**： 快照描述。 **取值范围**： 不涉及。
        :type description: str
        :param started: **参数解释**： 快照创建的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。 **取值范围**： 不涉及。
        :type started: str
        :param finished: **参数解释**： 快照完成的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。 **取值范围**： 不涉及。
        :type finished: str
        :param size: **参数解释**： 快照大小，单位 GB。 **取值范围**： 不涉及。
        :type size: float
        :param status: **参数解释**： 快照状态。 **取值范围**： - CREATING：创建中。 - AVAILABLE：可用。 - UNAVAILABLE：不可用。 - FROZEN： 普通冻结。 - POLICE_FROZEN： 公安冻结。
        :type status: str
        :param type: **参数解释**： 快照创建类型。 **取值范围**： 不涉及。
        :type type: str
        :param cluster_id: **参数解释**： 快照对应的集群ID。 **取值范围**： 不涉及。
        :type cluster_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._started = None
        self._finished = None
        self._size = None
        self._status = None
        self._type = None
        self._cluster_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.started = started
        self.finished = finished
        self.size = size
        self.status = status
        self.type = type
        self.cluster_id = cluster_id

    @property
    def id(self):
        r"""Gets the id of this Snapshots.

        **参数解释**： 快照ID。 **取值范围**： 不涉及。

        :return: The id of this Snapshots.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Snapshots.

        **参数解释**： 快照ID。 **取值范围**： 不涉及。

        :param id: The id of this Snapshots.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Snapshots.

        **参数解释**： 快照名称。 **取值范围**： 不涉及。

        :return: The name of this Snapshots.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Snapshots.

        **参数解释**： 快照名称。 **取值范围**： 不涉及。

        :param name: The name of this Snapshots.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Snapshots.

        **参数解释**： 快照描述。 **取值范围**： 不涉及。

        :return: The description of this Snapshots.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Snapshots.

        **参数解释**： 快照描述。 **取值范围**： 不涉及。

        :param description: The description of this Snapshots.
        :type description: str
        """
        self._description = description

    @property
    def started(self):
        r"""Gets the started of this Snapshots.

        **参数解释**： 快照创建的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。 **取值范围**： 不涉及。

        :return: The started of this Snapshots.
        :rtype: str
        """
        return self._started

    @started.setter
    def started(self, started):
        r"""Sets the started of this Snapshots.

        **参数解释**： 快照创建的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。 **取值范围**： 不涉及。

        :param started: The started of this Snapshots.
        :type started: str
        """
        self._started = started

    @property
    def finished(self):
        r"""Gets the finished of this Snapshots.

        **参数解释**： 快照完成的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。 **取值范围**： 不涉及。

        :return: The finished of this Snapshots.
        :rtype: str
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        r"""Sets the finished of this Snapshots.

        **参数解释**： 快照完成的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。 **取值范围**： 不涉及。

        :param finished: The finished of this Snapshots.
        :type finished: str
        """
        self._finished = finished

    @property
    def size(self):
        r"""Gets the size of this Snapshots.

        **参数解释**： 快照大小，单位 GB。 **取值范围**： 不涉及。

        :return: The size of this Snapshots.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Snapshots.

        **参数解释**： 快照大小，单位 GB。 **取值范围**： 不涉及。

        :param size: The size of this Snapshots.
        :type size: float
        """
        self._size = size

    @property
    def status(self):
        r"""Gets the status of this Snapshots.

        **参数解释**： 快照状态。 **取值范围**： - CREATING：创建中。 - AVAILABLE：可用。 - UNAVAILABLE：不可用。 - FROZEN： 普通冻结。 - POLICE_FROZEN： 公安冻结。

        :return: The status of this Snapshots.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Snapshots.

        **参数解释**： 快照状态。 **取值范围**： - CREATING：创建中。 - AVAILABLE：可用。 - UNAVAILABLE：不可用。 - FROZEN： 普通冻结。 - POLICE_FROZEN： 公安冻结。

        :param status: The status of this Snapshots.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this Snapshots.

        **参数解释**： 快照创建类型。 **取值范围**： 不涉及。

        :return: The type of this Snapshots.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Snapshots.

        **参数解释**： 快照创建类型。 **取值范围**： 不涉及。

        :param type: The type of this Snapshots.
        :type type: str
        """
        self._type = type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this Snapshots.

        **参数解释**： 快照对应的集群ID。 **取值范围**： 不涉及。

        :return: The cluster_id of this Snapshots.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this Snapshots.

        **参数解释**： 快照对应的集群ID。 **取值范围**： 不涉及。

        :param cluster_id: The cluster_id of this Snapshots.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, Snapshots):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
