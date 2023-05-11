# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigListRsp:

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
        'create_at': 'str',
        'status': 'str',
        'finished_at': 'str',
        'modify_delete_reset': 'str',
        'failed_msg': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cluster_id': 'clusterId',
        'create_at': 'createAt',
        'status': 'status',
        'finished_at': 'finishedAt',
        'modify_delete_reset': 'modifyDeleteReset',
        'failed_msg': 'failedMsg'
    }

    def __init__(self, id=None, cluster_id=None, create_at=None, status=None, finished_at=None, modify_delete_reset=None, failed_msg=None):
        """ConfigListRsp

        The model defined in huaweicloud sdk

        :param id: 操作ID
        :type id: str
        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param create_at: 创建时间。格式：Unix时间戳格式。
        :type create_at: str
        :param status: 任务执行状态。 - true: 执行成功。 - false: 执行失败。
        :type status: str
        :param finished_at: 结束时间，当创建未结束时结束时间为null。格式：Unix时间戳格式。
        :type finished_at: str
        :param modify_delete_reset: 修改参数配置记录。
        :type modify_delete_reset: str
        :param failed_msg: 返回错误信息。当状态为success时该参数为null。
        :type failed_msg: str
        """
        
        

        self._id = None
        self._cluster_id = None
        self._create_at = None
        self._status = None
        self._finished_at = None
        self._modify_delete_reset = None
        self._failed_msg = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if create_at is not None:
            self.create_at = create_at
        if status is not None:
            self.status = status
        if finished_at is not None:
            self.finished_at = finished_at
        if modify_delete_reset is not None:
            self.modify_delete_reset = modify_delete_reset
        if failed_msg is not None:
            self.failed_msg = failed_msg

    @property
    def id(self):
        """Gets the id of this ConfigListRsp.

        操作ID

        :return: The id of this ConfigListRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigListRsp.

        操作ID

        :param id: The id of this ConfigListRsp.
        :type id: str
        """
        self._id = id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ConfigListRsp.

        集群ID。

        :return: The cluster_id of this ConfigListRsp.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ConfigListRsp.

        集群ID。

        :param cluster_id: The cluster_id of this ConfigListRsp.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def create_at(self):
        """Gets the create_at of this ConfigListRsp.

        创建时间。格式：Unix时间戳格式。

        :return: The create_at of this ConfigListRsp.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this ConfigListRsp.

        创建时间。格式：Unix时间戳格式。

        :param create_at: The create_at of this ConfigListRsp.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def status(self):
        """Gets the status of this ConfigListRsp.

        任务执行状态。 - true: 执行成功。 - false: 执行失败。

        :return: The status of this ConfigListRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConfigListRsp.

        任务执行状态。 - true: 执行成功。 - false: 执行失败。

        :param status: The status of this ConfigListRsp.
        :type status: str
        """
        self._status = status

    @property
    def finished_at(self):
        """Gets the finished_at of this ConfigListRsp.

        结束时间，当创建未结束时结束时间为null。格式：Unix时间戳格式。

        :return: The finished_at of this ConfigListRsp.
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this ConfigListRsp.

        结束时间，当创建未结束时结束时间为null。格式：Unix时间戳格式。

        :param finished_at: The finished_at of this ConfigListRsp.
        :type finished_at: str
        """
        self._finished_at = finished_at

    @property
    def modify_delete_reset(self):
        """Gets the modify_delete_reset of this ConfigListRsp.

        修改参数配置记录。

        :return: The modify_delete_reset of this ConfigListRsp.
        :rtype: str
        """
        return self._modify_delete_reset

    @modify_delete_reset.setter
    def modify_delete_reset(self, modify_delete_reset):
        """Sets the modify_delete_reset of this ConfigListRsp.

        修改参数配置记录。

        :param modify_delete_reset: The modify_delete_reset of this ConfigListRsp.
        :type modify_delete_reset: str
        """
        self._modify_delete_reset = modify_delete_reset

    @property
    def failed_msg(self):
        """Gets the failed_msg of this ConfigListRsp.

        返回错误信息。当状态为success时该参数为null。

        :return: The failed_msg of this ConfigListRsp.
        :rtype: str
        """
        return self._failed_msg

    @failed_msg.setter
    def failed_msg(self, failed_msg):
        """Sets the failed_msg of this ConfigListRsp.

        返回错误信息。当状态为success时该参数为null。

        :param failed_msg: The failed_msg of this ConfigListRsp.
        :type failed_msg: str
        """
        self._failed_msg = failed_msg

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
        if not isinstance(other, ConfigListRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
