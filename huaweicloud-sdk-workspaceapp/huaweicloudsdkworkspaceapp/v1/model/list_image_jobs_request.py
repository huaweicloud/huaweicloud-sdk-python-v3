# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'job_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'status': 'status',
        'job_type': 'job_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, status=None, job_type=None, offset=None, limit=None):
        r"""ListImageJobsRequest

        The model defined in huaweicloud sdk

        :param status: job状态： * &#x60;WAITING&#x60; - 等待 * &#x60;RUNNING&#x60; - 运行中 * &#x60;SUCCESS&#x60; - 完成 * &#x60;FAILED&#x60; - 失败
        :type status: str
        :param job_type: job类型： * &#x60;CREATE_SERVER&#x60; - 创建镜像实例 * &#x60;CREATE_SERVER_IMAGE&#x60; - 构建镜像 * &#x60;DELETE_SERVER&#x60; - 删除镜像实例
        :type job_type: str
        :param offset: 查询的偏移量，默认值0。
        :type offset: int
        :param limit: 查询的数量，值区间[1-100]，默认值10。
        :type limit: int
        """
        
        

        self._status = None
        self._job_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if status is not None:
            self.status = status
        self.job_type = job_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def status(self):
        r"""Gets the status of this ListImageJobsRequest.

        job状态： * `WAITING` - 等待 * `RUNNING` - 运行中 * `SUCCESS` - 完成 * `FAILED` - 失败

        :return: The status of this ListImageJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListImageJobsRequest.

        job状态： * `WAITING` - 等待 * `RUNNING` - 运行中 * `SUCCESS` - 完成 * `FAILED` - 失败

        :param status: The status of this ListImageJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def job_type(self):
        r"""Gets the job_type of this ListImageJobsRequest.

        job类型： * `CREATE_SERVER` - 创建镜像实例 * `CREATE_SERVER_IMAGE` - 构建镜像 * `DELETE_SERVER` - 删除镜像实例

        :return: The job_type of this ListImageJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListImageJobsRequest.

        job类型： * `CREATE_SERVER` - 创建镜像实例 * `CREATE_SERVER_IMAGE` - 构建镜像 * `DELETE_SERVER` - 删除镜像实例

        :param job_type: The job_type of this ListImageJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def offset(self):
        r"""Gets the offset of this ListImageJobsRequest.

        查询的偏移量，默认值0。

        :return: The offset of this ListImageJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageJobsRequest.

        查询的偏移量，默认值0。

        :param offset: The offset of this ListImageJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListImageJobsRequest.

        查询的数量，值区间[1-100]，默认值10。

        :return: The limit of this ListImageJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageJobsRequest.

        查询的数量，值区间[1-100]，默认值10。

        :param limit: The limit of this ListImageJobsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListImageJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
