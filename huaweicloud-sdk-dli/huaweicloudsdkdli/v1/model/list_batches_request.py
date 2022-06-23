# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBatchesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'queue_name': 'str',
        'job_id': 'str',
        '_from': 'int',
        'size': 'int',
        'state': 'str'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'queue_name': 'queue_name',
        'job_id': 'job-id',
        '_from': 'from',
        'size': 'size',
        'state': 'state'
    }

    def __init__(self, cluster_name=None, queue_name=None, job_id=None, _from=None, size=None, state=None):
        """ListBatchesRequest

        The model defined in huaweicloud sdk

        :param cluster_name: DLI队列名称，不填写则获取当前Project下所有批处理作业(不推荐使用)。
        :type cluster_name: str
        :param queue_name: 
        :type queue_name: str
        :param job_id: 
        :type job_id: str
        :param _from: 起始批处理作业的索引号，默认从0开始。
        :type _from: int
        :param size: 查询批处理作业的数量。
        :type size: int
        :param state: 
        :type state: str
        """
        
        

        self._cluster_name = None
        self._queue_name = None
        self._job_id = None
        self.__from = None
        self._size = None
        self._state = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name
        if queue_name is not None:
            self.queue_name = queue_name
        if job_id is not None:
            self.job_id = job_id
        if _from is not None:
            self._from = _from
        if size is not None:
            self.size = size
        if state is not None:
            self.state = state

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ListBatchesRequest.

        DLI队列名称，不填写则获取当前Project下所有批处理作业(不推荐使用)。

        :return: The cluster_name of this ListBatchesRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ListBatchesRequest.

        DLI队列名称，不填写则获取当前Project下所有批处理作业(不推荐使用)。

        :param cluster_name: The cluster_name of this ListBatchesRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def queue_name(self):
        """Gets the queue_name of this ListBatchesRequest.


        :return: The queue_name of this ListBatchesRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ListBatchesRequest.


        :param queue_name: The queue_name of this ListBatchesRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def job_id(self):
        """Gets the job_id of this ListBatchesRequest.


        :return: The job_id of this ListBatchesRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListBatchesRequest.


        :param job_id: The job_id of this ListBatchesRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def _from(self):
        """Gets the _from of this ListBatchesRequest.

        起始批处理作业的索引号，默认从0开始。

        :return: The _from of this ListBatchesRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListBatchesRequest.

        起始批处理作业的索引号，默认从0开始。

        :param _from: The _from of this ListBatchesRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def size(self):
        """Gets the size of this ListBatchesRequest.

        查询批处理作业的数量。

        :return: The size of this ListBatchesRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListBatchesRequest.

        查询批处理作业的数量。

        :param size: The size of this ListBatchesRequest.
        :type size: int
        """
        self._size = size

    @property
    def state(self):
        """Gets the state of this ListBatchesRequest.


        :return: The state of this ListBatchesRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListBatchesRequest.


        :param state: The state of this ListBatchesRequest.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, ListBatchesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
