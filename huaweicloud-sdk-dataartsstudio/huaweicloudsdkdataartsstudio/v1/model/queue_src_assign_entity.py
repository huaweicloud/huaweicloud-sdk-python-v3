# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueueSrcAssignEntity:

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
        'source_type': 'str',
        'queue_name': 'str',
        'queue_type': 'str',
        'queue_attr': 'int',
        'conn_id': 'str',
        'conn_name': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str',
        'create_time': 'int',
        'create_user': 'str',
        'update_time': 'int',
        'update_user': 'str',
        'project_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'source_type': 'source_type',
        'queue_name': 'queue_name',
        'queue_type': 'queue_type',
        'queue_attr': 'queue_attr',
        'conn_id': 'conn_id',
        'conn_name': 'conn_name',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'update_time': 'update_time',
        'update_user': 'update_user',
        'project_id': 'project_id',
        'description': 'description'
    }

    def __init__(self, id=None, source_type=None, queue_name=None, queue_type=None, queue_attr=None, conn_id=None, conn_name=None, cluster_id=None, cluster_name=None, create_time=None, create_user=None, update_time=None, update_user=None, project_id=None, description=None):
        """QueueSrcAssignEntity

        The model defined in huaweicloud sdk

        :param id: 队列资源id。
        :type id: str
        :param source_type: 队列资源服务名称。
        :type source_type: str
        :param queue_name: 队列名称。
        :type queue_name: str
        :param queue_type: 队列类型。
        :type queue_type: str
        :param queue_attr: 队列属性(0:默认,1:实时队列,2:离线队列), 当前只有yarn队列涉及。
        :type queue_attr: int
        :param conn_id: 数据连接id。
        :type conn_id: str
        :param conn_name: 数据连接名称。
        :type conn_name: str
        :param cluster_id: 集群id。
        :type cluster_id: str
        :param cluster_name: 集群名称。
        :type cluster_name: str
        :param create_time: 队列加入此空间的时间。
        :type create_time: int
        :param create_user: 队列加入此的操作人。
        :type create_user: str
        :param update_time: 当前空间下管理的队列更新时间。
        :type update_time: int
        :param update_user: 当前空间下管理的队列更新人。
        :type update_user: str
        :param project_id: 项目id。
        :type project_id: str
        :param description: 当前空间分配资源附加的描述信息。
        :type description: str
        """
        
        

        self._id = None
        self._source_type = None
        self._queue_name = None
        self._queue_type = None
        self._queue_attr = None
        self._conn_id = None
        self._conn_name = None
        self._cluster_id = None
        self._cluster_name = None
        self._create_time = None
        self._create_user = None
        self._update_time = None
        self._update_user = None
        self._project_id = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if source_type is not None:
            self.source_type = source_type
        if queue_name is not None:
            self.queue_name = queue_name
        if queue_type is not None:
            self.queue_type = queue_type
        if queue_attr is not None:
            self.queue_attr = queue_attr
        if conn_id is not None:
            self.conn_id = conn_id
        if conn_name is not None:
            self.conn_name = conn_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user
        if project_id is not None:
            self.project_id = project_id
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this QueueSrcAssignEntity.

        队列资源id。

        :return: The id of this QueueSrcAssignEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueueSrcAssignEntity.

        队列资源id。

        :param id: The id of this QueueSrcAssignEntity.
        :type id: str
        """
        self._id = id

    @property
    def source_type(self):
        """Gets the source_type of this QueueSrcAssignEntity.

        队列资源服务名称。

        :return: The source_type of this QueueSrcAssignEntity.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this QueueSrcAssignEntity.

        队列资源服务名称。

        :param source_type: The source_type of this QueueSrcAssignEntity.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def queue_name(self):
        """Gets the queue_name of this QueueSrcAssignEntity.

        队列名称。

        :return: The queue_name of this QueueSrcAssignEntity.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this QueueSrcAssignEntity.

        队列名称。

        :param queue_name: The queue_name of this QueueSrcAssignEntity.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def queue_type(self):
        """Gets the queue_type of this QueueSrcAssignEntity.

        队列类型。

        :return: The queue_type of this QueueSrcAssignEntity.
        :rtype: str
        """
        return self._queue_type

    @queue_type.setter
    def queue_type(self, queue_type):
        """Sets the queue_type of this QueueSrcAssignEntity.

        队列类型。

        :param queue_type: The queue_type of this QueueSrcAssignEntity.
        :type queue_type: str
        """
        self._queue_type = queue_type

    @property
    def queue_attr(self):
        """Gets the queue_attr of this QueueSrcAssignEntity.

        队列属性(0:默认,1:实时队列,2:离线队列), 当前只有yarn队列涉及。

        :return: The queue_attr of this QueueSrcAssignEntity.
        :rtype: int
        """
        return self._queue_attr

    @queue_attr.setter
    def queue_attr(self, queue_attr):
        """Sets the queue_attr of this QueueSrcAssignEntity.

        队列属性(0:默认,1:实时队列,2:离线队列), 当前只有yarn队列涉及。

        :param queue_attr: The queue_attr of this QueueSrcAssignEntity.
        :type queue_attr: int
        """
        self._queue_attr = queue_attr

    @property
    def conn_id(self):
        """Gets the conn_id of this QueueSrcAssignEntity.

        数据连接id。

        :return: The conn_id of this QueueSrcAssignEntity.
        :rtype: str
        """
        return self._conn_id

    @conn_id.setter
    def conn_id(self, conn_id):
        """Sets the conn_id of this QueueSrcAssignEntity.

        数据连接id。

        :param conn_id: The conn_id of this QueueSrcAssignEntity.
        :type conn_id: str
        """
        self._conn_id = conn_id

    @property
    def conn_name(self):
        """Gets the conn_name of this QueueSrcAssignEntity.

        数据连接名称。

        :return: The conn_name of this QueueSrcAssignEntity.
        :rtype: str
        """
        return self._conn_name

    @conn_name.setter
    def conn_name(self, conn_name):
        """Sets the conn_name of this QueueSrcAssignEntity.

        数据连接名称。

        :param conn_name: The conn_name of this QueueSrcAssignEntity.
        :type conn_name: str
        """
        self._conn_name = conn_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this QueueSrcAssignEntity.

        集群id。

        :return: The cluster_id of this QueueSrcAssignEntity.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this QueueSrcAssignEntity.

        集群id。

        :param cluster_id: The cluster_id of this QueueSrcAssignEntity.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this QueueSrcAssignEntity.

        集群名称。

        :return: The cluster_name of this QueueSrcAssignEntity.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this QueueSrcAssignEntity.

        集群名称。

        :param cluster_name: The cluster_name of this QueueSrcAssignEntity.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def create_time(self):
        """Gets the create_time of this QueueSrcAssignEntity.

        队列加入此空间的时间。

        :return: The create_time of this QueueSrcAssignEntity.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueueSrcAssignEntity.

        队列加入此空间的时间。

        :param create_time: The create_time of this QueueSrcAssignEntity.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this QueueSrcAssignEntity.

        队列加入此的操作人。

        :return: The create_user of this QueueSrcAssignEntity.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this QueueSrcAssignEntity.

        队列加入此的操作人。

        :param create_user: The create_user of this QueueSrcAssignEntity.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def update_time(self):
        """Gets the update_time of this QueueSrcAssignEntity.

        当前空间下管理的队列更新时间。

        :return: The update_time of this QueueSrcAssignEntity.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this QueueSrcAssignEntity.

        当前空间下管理的队列更新时间。

        :param update_time: The update_time of this QueueSrcAssignEntity.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def update_user(self):
        """Gets the update_user of this QueueSrcAssignEntity.

        当前空间下管理的队列更新人。

        :return: The update_user of this QueueSrcAssignEntity.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this QueueSrcAssignEntity.

        当前空间下管理的队列更新人。

        :param update_user: The update_user of this QueueSrcAssignEntity.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def project_id(self):
        """Gets the project_id of this QueueSrcAssignEntity.

        项目id。

        :return: The project_id of this QueueSrcAssignEntity.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this QueueSrcAssignEntity.

        项目id。

        :param project_id: The project_id of this QueueSrcAssignEntity.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def description(self):
        """Gets the description of this QueueSrcAssignEntity.

        当前空间分配资源附加的描述信息。

        :return: The description of this QueueSrcAssignEntity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueueSrcAssignEntity.

        当前空间分配资源附加的描述信息。

        :param description: The description of this QueueSrcAssignEntity.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, QueueSrcAssignEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
