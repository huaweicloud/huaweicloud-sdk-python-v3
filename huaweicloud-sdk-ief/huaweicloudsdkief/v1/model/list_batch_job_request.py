# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBatchJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort': 'str',
        'ief_instance_id': 'str'
    }

    attribute_map = {
        'job_type': 'job_type',
        'limit': 'limit',
        'offset': 'offset',
        'sort': 'sort',
        'ief_instance_id': 'ief-instance-id'
    }

    def __init__(self, job_type=None, limit=None, offset=None, sort=None, ief_instance_id=None):
        """ListBatchJobRequest

        The model defined in huaweicloud sdk

        :param job_type: 批量处理作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级
        :type job_type: str
        :param limit: 查询返回记录的数量限制
        :type limit: int
        :param offset: 偏移量，表示查询该偏移量后面的记录
        :type offset: int
        :param sort: 查询结果排序，如按照创建时间降序排序为created_at:desc，升序排序为created_at:asc
        :type sort: str
        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        """
        
        

        self._job_type = None
        self._limit = None
        self._offset = None
        self._sort = None
        self._ief_instance_id = None
        self.discriminator = None

        if job_type is not None:
            self.job_type = job_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort is not None:
            self.sort = sort
        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id

    @property
    def job_type(self):
        """Gets the job_type of this ListBatchJobRequest.

        批量处理作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级

        :return: The job_type of this ListBatchJobRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ListBatchJobRequest.

        批量处理作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级

        :param job_type: The job_type of this ListBatchJobRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def limit(self):
        """Gets the limit of this ListBatchJobRequest.

        查询返回记录的数量限制

        :return: The limit of this ListBatchJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBatchJobRequest.

        查询返回记录的数量限制

        :param limit: The limit of this ListBatchJobRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListBatchJobRequest.

        偏移量，表示查询该偏移量后面的记录

        :return: The offset of this ListBatchJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBatchJobRequest.

        偏移量，表示查询该偏移量后面的记录

        :param offset: The offset of this ListBatchJobRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort(self):
        """Gets the sort of this ListBatchJobRequest.

        查询结果排序，如按照创建时间降序排序为created_at:desc，升序排序为created_at:asc

        :return: The sort of this ListBatchJobRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListBatchJobRequest.

        查询结果排序，如按照创建时间降序排序为created_at:desc，升序排序为created_at:asc

        :param sort: The sort of this ListBatchJobRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this ListBatchJobRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this ListBatchJobRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this ListBatchJobRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this ListBatchJobRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

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
        if not isinstance(other, ListBatchJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
