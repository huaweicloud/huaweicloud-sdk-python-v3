# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListItaSubJobsRequest:

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
        'job_id': 'str',
        'job_type': 'str',
        'desktop_pool_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'status': 'status',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'desktop_pool_id': 'desktop_pool_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, status=None, job_id=None, job_type=None, desktop_pool_id=None, limit=None, offset=None):
        r"""ListItaSubJobsRequest

        The model defined in huaweicloud sdk

        :param status: 任务状态 - SUCCESS：成功。 - RUNNING：运行中。 - FAILED：失败。 - WAITING：等待。
        :type status: str
        :param job_id: 任务ID。
        :type job_id: str
        :param job_type: 任务类型  - createDesktops：创建桌面任务。  - applyWorkspace：开通云桌面服务。  - cancelWorkspace：注销云桌面服务。  - expandVolumes:  扩容磁盘。  - addVolumes: 添加磁盘。
        :type job_type: str
        :param desktop_pool_id: 桌面池ID。
        :type desktop_pool_id: str
        :param limit: 用于分页查询，取值范围0~1000，默认1000。
        :type limit: int
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        """
        
        

        self._status = None
        self._job_id = None
        self._job_type = None
        self._desktop_pool_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if desktop_pool_id is not None:
            self.desktop_pool_id = desktop_pool_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def status(self):
        r"""Gets the status of this ListItaSubJobsRequest.

        任务状态 - SUCCESS：成功。 - RUNNING：运行中。 - FAILED：失败。 - WAITING：等待。

        :return: The status of this ListItaSubJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListItaSubJobsRequest.

        任务状态 - SUCCESS：成功。 - RUNNING：运行中。 - FAILED：失败。 - WAITING：等待。

        :param status: The status of this ListItaSubJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def job_id(self):
        r"""Gets the job_id of this ListItaSubJobsRequest.

        任务ID。

        :return: The job_id of this ListItaSubJobsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListItaSubJobsRequest.

        任务ID。

        :param job_id: The job_id of this ListItaSubJobsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this ListItaSubJobsRequest.

        任务类型  - createDesktops：创建桌面任务。  - applyWorkspace：开通云桌面服务。  - cancelWorkspace：注销云桌面服务。  - expandVolumes:  扩容磁盘。  - addVolumes: 添加磁盘。

        :return: The job_type of this ListItaSubJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListItaSubJobsRequest.

        任务类型  - createDesktops：创建桌面任务。  - applyWorkspace：开通云桌面服务。  - cancelWorkspace：注销云桌面服务。  - expandVolumes:  扩容磁盘。  - addVolumes: 添加磁盘。

        :param job_type: The job_type of this ListItaSubJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def desktop_pool_id(self):
        r"""Gets the desktop_pool_id of this ListItaSubJobsRequest.

        桌面池ID。

        :return: The desktop_pool_id of this ListItaSubJobsRequest.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        r"""Sets the desktop_pool_id of this ListItaSubJobsRequest.

        桌面池ID。

        :param desktop_pool_id: The desktop_pool_id of this ListItaSubJobsRequest.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def limit(self):
        r"""Gets the limit of this ListItaSubJobsRequest.

        用于分页查询，取值范围0~1000，默认1000。

        :return: The limit of this ListItaSubJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListItaSubJobsRequest.

        用于分页查询，取值范围0~1000，默认1000。

        :param limit: The limit of this ListItaSubJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListItaSubJobsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListItaSubJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListItaSubJobsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListItaSubJobsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListItaSubJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
