# coding: utf-8

import re
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
        'cluster_id': 'str',
        'size': 'float',
        'name': 'str',
        'description': 'str',
        'finished': 'str',
        'started': 'str',
        'id': 'str',
        'type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'size': 'size',
        'name': 'name',
        'description': 'description',
        'finished': 'finished',
        'started': 'started',
        'id': 'id',
        'type': 'type',
        'status': 'status'
    }

    def __init__(self, cluster_id=None, size=None, name=None, description=None, finished=None, started=None, id=None, type=None, status=None):
        """Snapshots - a model defined in huaweicloud sdk"""
        
        

        self._cluster_id = None
        self._size = None
        self._name = None
        self._description = None
        self._finished = None
        self._started = None
        self._id = None
        self._type = None
        self._status = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.size = size
        self.name = name
        self.description = description
        self.finished = finished
        self.started = started
        self.id = id
        self.type = type
        self.status = status

    @property
    def cluster_id(self):
        """Gets the cluster_id of this Snapshots.

        快照对应的集群ID

        :return: The cluster_id of this Snapshots.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this Snapshots.

        快照对应的集群ID

        :param cluster_id: The cluster_id of this Snapshots.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def size(self):
        """Gets the size of this Snapshots.

        快照大小，单位 GB

        :return: The size of this Snapshots.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Snapshots.

        快照大小，单位 GB

        :param size: The size of this Snapshots.
        :type: float
        """
        self._size = size

    @property
    def name(self):
        """Gets the name of this Snapshots.

        快照名称

        :return: The name of this Snapshots.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Snapshots.

        快照名称

        :param name: The name of this Snapshots.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Snapshots.

        快照描述

        :return: The description of this Snapshots.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Snapshots.

        快照描述

        :param description: The description of this Snapshots.
        :type: str
        """
        self._description = description

    @property
    def finished(self):
        """Gets the finished of this Snapshots.

        快照完成的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。

        :return: The finished of this Snapshots.
        :rtype: str
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this Snapshots.

        快照完成的日期时间，格式为 ISO8601: YYYY-MM-DDThh:mm:ssZ。

        :param finished: The finished of this Snapshots.
        :type: str
        """
        self._finished = finished

    @property
    def started(self):
        """Gets the started of this Snapshots.

        快照创建的日期时间

        :return: The started of this Snapshots.
        :rtype: str
        """
        return self._started

    @started.setter
    def started(self, started):
        """Sets the started of this Snapshots.

        快照创建的日期时间

        :param started: The started of this Snapshots.
        :type: str
        """
        self._started = started

    @property
    def id(self):
        """Gets the id of this Snapshots.

        快照 ID

        :return: The id of this Snapshots.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Snapshots.

        快照 ID

        :param id: The id of this Snapshots.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this Snapshots.

        快照创建类型

        :return: The type of this Snapshots.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Snapshots.

        快照创建类型

        :param type: The type of this Snapshots.
        :type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this Snapshots.

        快照状态

        :return: The status of this Snapshots.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Snapshots.

        快照状态

        :param status: The status of this Snapshots.
        :type: str
        """
        self._status = status

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
