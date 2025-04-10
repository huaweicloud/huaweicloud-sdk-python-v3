# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueueSrcAssignCreateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_type': 'str',
        'queue_name': 'list[str]',
        'conn_id': 'str',
        'cluster_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'source_type': 'source_type',
        'queue_name': 'queue_name',
        'conn_id': 'conn_id',
        'cluster_id': 'cluster_id',
        'description': 'description'
    }

    def __init__(self, source_type=None, queue_name=None, conn_id=None, cluster_id=None, description=None):
        r"""QueueSrcAssignCreateDTO

        The model defined in huaweicloud sdk

        :param source_type: 队列资源服务(当前只支持mrs、dli)。
        :type source_type: str
        :param queue_name: 队列名称。
        :type queue_name: list[str]
        :param conn_id: 数据连接id。
        :type conn_id: str
        :param cluster_id: 集群id。
        :type cluster_id: str
        :param description: 当前空间分配资源附加的描述信息。
        :type description: str
        """
        
        

        self._source_type = None
        self._queue_name = None
        self._conn_id = None
        self._cluster_id = None
        self._description = None
        self.discriminator = None

        if source_type is not None:
            self.source_type = source_type
        if queue_name is not None:
            self.queue_name = queue_name
        if conn_id is not None:
            self.conn_id = conn_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if description is not None:
            self.description = description

    @property
    def source_type(self):
        r"""Gets the source_type of this QueueSrcAssignCreateDTO.

        队列资源服务(当前只支持mrs、dli)。

        :return: The source_type of this QueueSrcAssignCreateDTO.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this QueueSrcAssignCreateDTO.

        队列资源服务(当前只支持mrs、dli)。

        :param source_type: The source_type of this QueueSrcAssignCreateDTO.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def queue_name(self):
        r"""Gets the queue_name of this QueueSrcAssignCreateDTO.

        队列名称。

        :return: The queue_name of this QueueSrcAssignCreateDTO.
        :rtype: list[str]
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this QueueSrcAssignCreateDTO.

        队列名称。

        :param queue_name: The queue_name of this QueueSrcAssignCreateDTO.
        :type queue_name: list[str]
        """
        self._queue_name = queue_name

    @property
    def conn_id(self):
        r"""Gets the conn_id of this QueueSrcAssignCreateDTO.

        数据连接id。

        :return: The conn_id of this QueueSrcAssignCreateDTO.
        :rtype: str
        """
        return self._conn_id

    @conn_id.setter
    def conn_id(self, conn_id):
        r"""Sets the conn_id of this QueueSrcAssignCreateDTO.

        数据连接id。

        :param conn_id: The conn_id of this QueueSrcAssignCreateDTO.
        :type conn_id: str
        """
        self._conn_id = conn_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this QueueSrcAssignCreateDTO.

        集群id。

        :return: The cluster_id of this QueueSrcAssignCreateDTO.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this QueueSrcAssignCreateDTO.

        集群id。

        :param cluster_id: The cluster_id of this QueueSrcAssignCreateDTO.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def description(self):
        r"""Gets the description of this QueueSrcAssignCreateDTO.

        当前空间分配资源附加的描述信息。

        :return: The description of this QueueSrcAssignCreateDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this QueueSrcAssignCreateDTO.

        当前空间分配资源附加的描述信息。

        :param description: The description of this QueueSrcAssignCreateDTO.
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
        if not isinstance(other, QueueSrcAssignCreateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
