# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelineJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_store_id': 'str',
        'data_store_group_id': 'str',
        'data_source_id': 'str',
        'pipeline_name': 'str',
        'operator_class_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'sync_status': 'bool'
    }

    attribute_map = {
        'data_store_id': 'data_store_id',
        'data_store_group_id': 'data_store_group_id',
        'data_source_id': 'data_source_id',
        'pipeline_name': 'pipeline_name',
        'operator_class_name': 'operator_class_name',
        'offset': 'offset',
        'limit': 'limit',
        'sync_status': 'sync_status'
    }

    def __init__(self, data_store_id=None, data_store_group_id=None, data_source_id=None, pipeline_name=None, operator_class_name=None, offset=None, limit=None, sync_status=None):
        """ListPipelineJobsRequest

        The model defined in huaweicloud sdk

        :param data_store_id: 数据存储Id
        :type data_store_id: str
        :param data_store_group_id: 存储组Id
        :type data_store_group_id: str
        :param data_source_id: 数据源Id
        :type data_source_id: str
        :param pipeline_name: 管道名称
        :type pipeline_name: str
        :param operator_class_name: 包含的管道类名
        :type operator_class_name: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param sync_status: 立即同步作业状态，默认是false
        :type sync_status: bool
        """
        
        

        self._data_store_id = None
        self._data_store_group_id = None
        self._data_source_id = None
        self._pipeline_name = None
        self._operator_class_name = None
        self._offset = None
        self._limit = None
        self._sync_status = None
        self.discriminator = None

        if data_store_id is not None:
            self.data_store_id = data_store_id
        if data_store_group_id is not None:
            self.data_store_group_id = data_store_group_id
        if data_source_id is not None:
            self.data_source_id = data_source_id
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name
        if operator_class_name is not None:
            self.operator_class_name = operator_class_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sync_status is not None:
            self.sync_status = sync_status

    @property
    def data_store_id(self):
        """Gets the data_store_id of this ListPipelineJobsRequest.

        数据存储Id

        :return: The data_store_id of this ListPipelineJobsRequest.
        :rtype: str
        """
        return self._data_store_id

    @data_store_id.setter
    def data_store_id(self, data_store_id):
        """Sets the data_store_id of this ListPipelineJobsRequest.

        数据存储Id

        :param data_store_id: The data_store_id of this ListPipelineJobsRequest.
        :type data_store_id: str
        """
        self._data_store_id = data_store_id

    @property
    def data_store_group_id(self):
        """Gets the data_store_group_id of this ListPipelineJobsRequest.

        存储组Id

        :return: The data_store_group_id of this ListPipelineJobsRequest.
        :rtype: str
        """
        return self._data_store_group_id

    @data_store_group_id.setter
    def data_store_group_id(self, data_store_group_id):
        """Sets the data_store_group_id of this ListPipelineJobsRequest.

        存储组Id

        :param data_store_group_id: The data_store_group_id of this ListPipelineJobsRequest.
        :type data_store_group_id: str
        """
        self._data_store_group_id = data_store_group_id

    @property
    def data_source_id(self):
        """Gets the data_source_id of this ListPipelineJobsRequest.

        数据源Id

        :return: The data_source_id of this ListPipelineJobsRequest.
        :rtype: str
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this ListPipelineJobsRequest.

        数据源Id

        :param data_source_id: The data_source_id of this ListPipelineJobsRequest.
        :type data_source_id: str
        """
        self._data_source_id = data_source_id

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this ListPipelineJobsRequest.

        管道名称

        :return: The pipeline_name of this ListPipelineJobsRequest.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this ListPipelineJobsRequest.

        管道名称

        :param pipeline_name: The pipeline_name of this ListPipelineJobsRequest.
        :type pipeline_name: str
        """
        self._pipeline_name = pipeline_name

    @property
    def operator_class_name(self):
        """Gets the operator_class_name of this ListPipelineJobsRequest.

        包含的管道类名

        :return: The operator_class_name of this ListPipelineJobsRequest.
        :rtype: str
        """
        return self._operator_class_name

    @operator_class_name.setter
    def operator_class_name(self, operator_class_name):
        """Sets the operator_class_name of this ListPipelineJobsRequest.

        包含的管道类名

        :param operator_class_name: The operator_class_name of this ListPipelineJobsRequest.
        :type operator_class_name: str
        """
        self._operator_class_name = operator_class_name

    @property
    def offset(self):
        """Gets the offset of this ListPipelineJobsRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :return: The offset of this ListPipelineJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPipelineJobsRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :param offset: The offset of this ListPipelineJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPipelineJobsRequest.

        每页显示的条目数量

        :return: The limit of this ListPipelineJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPipelineJobsRequest.

        每页显示的条目数量

        :param limit: The limit of this ListPipelineJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sync_status(self):
        """Gets the sync_status of this ListPipelineJobsRequest.

        立即同步作业状态，默认是false

        :return: The sync_status of this ListPipelineJobsRequest.
        :rtype: bool
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """Sets the sync_status of this ListPipelineJobsRequest.

        立即同步作业状态，默认是false

        :param sync_status: The sync_status of this ListPipelineJobsRequest.
        :type sync_status: bool
        """
        self._sync_status = sync_status

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
        if not isinstance(other, ListPipelineJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
