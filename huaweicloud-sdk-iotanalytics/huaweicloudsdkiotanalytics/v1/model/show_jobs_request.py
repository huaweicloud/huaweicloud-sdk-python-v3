# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_input_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'sync_status': 'bool'
    }

    attribute_map = {
        'job_input_type': 'job_input_type',
        'offset': 'offset',
        'limit': 'limit',
        'sync_status': 'sync_status'
    }

    def __init__(self, job_input_type=None, offset=None, limit=None, sync_status=None):
        r"""ShowJobsRequest

        The model defined in huaweicloud sdk

        :param job_input_type: 接收数据类型，支持两种接收数据类型：“管道数据”、“资产数据”。管道数据：“实时分析”使用来自“数据管道”的数据进行分析，并可将数据输出到其他云服务。资产数据：“实时分析”使用来自“资产模型”的数据进行分析，并将分析后的结果返回给“资产模型”，丰富资产模型。
        :type job_input_type: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param sync_status: 立即同步作业状态，默认是false
        :type sync_status: bool
        """
        
        

        self._job_input_type = None
        self._offset = None
        self._limit = None
        self._sync_status = None
        self.discriminator = None

        if job_input_type is not None:
            self.job_input_type = job_input_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sync_status is not None:
            self.sync_status = sync_status

    @property
    def job_input_type(self):
        r"""Gets the job_input_type of this ShowJobsRequest.

        接收数据类型，支持两种接收数据类型：“管道数据”、“资产数据”。管道数据：“实时分析”使用来自“数据管道”的数据进行分析，并可将数据输出到其他云服务。资产数据：“实时分析”使用来自“资产模型”的数据进行分析，并将分析后的结果返回给“资产模型”，丰富资产模型。

        :return: The job_input_type of this ShowJobsRequest.
        :rtype: str
        """
        return self._job_input_type

    @job_input_type.setter
    def job_input_type(self, job_input_type):
        r"""Sets the job_input_type of this ShowJobsRequest.

        接收数据类型，支持两种接收数据类型：“管道数据”、“资产数据”。管道数据：“实时分析”使用来自“数据管道”的数据进行分析，并可将数据输出到其他云服务。资产数据：“实时分析”使用来自“资产模型”的数据进行分析，并将分析后的结果返回给“资产模型”，丰富资产模型。

        :param job_input_type: The job_input_type of this ShowJobsRequest.
        :type job_input_type: str
        """
        self._job_input_type = job_input_type

    @property
    def offset(self):
        r"""Gets the offset of this ShowJobsRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :return: The offset of this ShowJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowJobsRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :param offset: The offset of this ShowJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowJobsRequest.

        每页显示的条目数量

        :return: The limit of this ShowJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowJobsRequest.

        每页显示的条目数量

        :param limit: The limit of this ShowJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sync_status(self):
        r"""Gets the sync_status of this ShowJobsRequest.

        立即同步作业状态，默认是false

        :return: The sync_status of this ShowJobsRequest.
        :rtype: bool
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        r"""Sets the sync_status of this ShowJobsRequest.

        立即同步作业状态，默认是false

        :param sync_status: The sync_status of this ShowJobsRequest.
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
        if not isinstance(other, ShowJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
