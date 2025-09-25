# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RealTimeLogCollect:

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
        'cluster_id': 'str',
        'index_prefix': 'str',
        'keep_days': 'int',
        'target_cluster_id': 'str',
        'status': 'str',
        'create_at': 'int',
        'update_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'cluster_id': 'clusterId',
        'index_prefix': 'indexPrefix',
        'keep_days': 'keepDays',
        'target_cluster_id': 'targetClusterId',
        'status': 'status',
        'create_at': 'createAt',
        'update_at': 'updateAt'
    }

    def __init__(self, id=None, cluster_id=None, index_prefix=None, keep_days=None, target_cluster_id=None, status=None, create_at=None, update_at=None):
        r"""RealTimeLogCollect

        The model defined in huaweicloud sdk

        :param id: 日志采集ID，通过系统UUID生成。
        :type id: str
        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param index_prefix: 日志保存索引的前缀。
        :type index_prefix: str
        :param keep_days: 日志保存时间。
        :type keep_days: int
        :param target_cluster_id: 保存日志的目标集群ID。
        :type target_cluster_id: str
        :param status: 日志实时采集任务状态。
        :type status: str
        :param create_at: 日志实时采集任务开启时间。
        :type create_at: int
        :param update_at: 日志实时采集任务更新时间。
        :type update_at: int
        """
        
        

        self._id = None
        self._cluster_id = None
        self._index_prefix = None
        self._keep_days = None
        self._target_cluster_id = None
        self._status = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        self.index_prefix = index_prefix
        self.keep_days = keep_days
        self.target_cluster_id = target_cluster_id
        self.status = status
        self.create_at = create_at
        self.update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this RealTimeLogCollect.

        日志采集ID，通过系统UUID生成。

        :return: The id of this RealTimeLogCollect.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RealTimeLogCollect.

        日志采集ID，通过系统UUID生成。

        :param id: The id of this RealTimeLogCollect.
        :type id: str
        """
        self._id = id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this RealTimeLogCollect.

        集群ID。

        :return: The cluster_id of this RealTimeLogCollect.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this RealTimeLogCollect.

        集群ID。

        :param cluster_id: The cluster_id of this RealTimeLogCollect.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def index_prefix(self):
        r"""Gets the index_prefix of this RealTimeLogCollect.

        日志保存索引的前缀。

        :return: The index_prefix of this RealTimeLogCollect.
        :rtype: str
        """
        return self._index_prefix

    @index_prefix.setter
    def index_prefix(self, index_prefix):
        r"""Sets the index_prefix of this RealTimeLogCollect.

        日志保存索引的前缀。

        :param index_prefix: The index_prefix of this RealTimeLogCollect.
        :type index_prefix: str
        """
        self._index_prefix = index_prefix

    @property
    def keep_days(self):
        r"""Gets the keep_days of this RealTimeLogCollect.

        日志保存时间。

        :return: The keep_days of this RealTimeLogCollect.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this RealTimeLogCollect.

        日志保存时间。

        :param keep_days: The keep_days of this RealTimeLogCollect.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def target_cluster_id(self):
        r"""Gets the target_cluster_id of this RealTimeLogCollect.

        保存日志的目标集群ID。

        :return: The target_cluster_id of this RealTimeLogCollect.
        :rtype: str
        """
        return self._target_cluster_id

    @target_cluster_id.setter
    def target_cluster_id(self, target_cluster_id):
        r"""Sets the target_cluster_id of this RealTimeLogCollect.

        保存日志的目标集群ID。

        :param target_cluster_id: The target_cluster_id of this RealTimeLogCollect.
        :type target_cluster_id: str
        """
        self._target_cluster_id = target_cluster_id

    @property
    def status(self):
        r"""Gets the status of this RealTimeLogCollect.

        日志实时采集任务状态。

        :return: The status of this RealTimeLogCollect.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RealTimeLogCollect.

        日志实时采集任务状态。

        :param status: The status of this RealTimeLogCollect.
        :type status: str
        """
        self._status = status

    @property
    def create_at(self):
        r"""Gets the create_at of this RealTimeLogCollect.

        日志实时采集任务开启时间。

        :return: The create_at of this RealTimeLogCollect.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this RealTimeLogCollect.

        日志实时采集任务开启时间。

        :param create_at: The create_at of this RealTimeLogCollect.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this RealTimeLogCollect.

        日志实时采集任务更新时间。

        :return: The update_at of this RealTimeLogCollect.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this RealTimeLogCollect.

        日志实时采集任务更新时间。

        :param update_at: The update_at of this RealTimeLogCollect.
        :type update_at: int
        """
        self._update_at = update_at

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
        if not isinstance(other, RealTimeLogCollect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
