# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubJobsRequest:

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
        'limit': 'int',
        'job_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'job_type': 'job_type',
        'offset': 'offset',
        'limit': 'limit',
        'job_id': 'job_id'
    }

    def __init__(self, status=None, job_type=None, offset=None, limit=None, job_id=None):
        """ListSubJobsRequest

        The model defined in huaweicloud sdk

        :param status: job详情的状态： * &#x60;WAITING&#x60; - 等待 * &#x60;RUNNING&#x60; - 运行中 * &#x60;SUCCESS&#x60; - 成功 * &#x60;FAILED&#x60; - 失败 * &#x60;ABNORMAL&#x60; - 异常 * &#x60;ROLLBACK&#x60; - 回滚中 * &#x60;ABORTING&#x60; - 取消
        :type status: str
        :param job_type: job类型 * &#x60;CREATE_SERVER&#x60; - 创建服务器 * &#x60;DELETE_SERVER&#x60; - 删除服务器 * &#x60;REJOIN_DOMAIN&#x60; - 服务器重新加域 * &#x60;CHANGE_SERVER_IMAGE&#x60; - 修改服务器镜像 * &#x60;REINSTALL_OS&#x60; - 服务器重装操作系统 * &#x60;MIGRATE_SERVER&#x60; - 迁移服务器 * &#x60;UPDATE_SERVER_TSVI&#x60; - 更新虚拟IP配置 * &#x60;UPGRADE_ACCESS_AGENT&#x60; - hda升级 * &#x60;SCHEDULED_TASK&#x60; - 定时任务 * &#x60;UPDATE_FREEZE_STATUS&#x60; - 更新服务器冻结状态
        :type job_type: str
        :param offset: 查询的偏移量。
        :type offset: int
        :param limit: 查询的数量，值区间[1-100]。
        :type limit: int
        :param job_id: 任务ID。
        :type job_id: str
        """
        
        

        self._status = None
        self._job_type = None
        self._offset = None
        self._limit = None
        self._job_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        self.job_type = job_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if job_id is not None:
            self.job_id = job_id

    @property
    def status(self):
        """Gets the status of this ListSubJobsRequest.

        job详情的状态： * `WAITING` - 等待 * `RUNNING` - 运行中 * `SUCCESS` - 成功 * `FAILED` - 失败 * `ABNORMAL` - 异常 * `ROLLBACK` - 回滚中 * `ABORTING` - 取消

        :return: The status of this ListSubJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListSubJobsRequest.

        job详情的状态： * `WAITING` - 等待 * `RUNNING` - 运行中 * `SUCCESS` - 成功 * `FAILED` - 失败 * `ABNORMAL` - 异常 * `ROLLBACK` - 回滚中 * `ABORTING` - 取消

        :param status: The status of this ListSubJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def job_type(self):
        """Gets the job_type of this ListSubJobsRequest.

        job类型 * `CREATE_SERVER` - 创建服务器 * `DELETE_SERVER` - 删除服务器 * `REJOIN_DOMAIN` - 服务器重新加域 * `CHANGE_SERVER_IMAGE` - 修改服务器镜像 * `REINSTALL_OS` - 服务器重装操作系统 * `MIGRATE_SERVER` - 迁移服务器 * `UPDATE_SERVER_TSVI` - 更新虚拟IP配置 * `UPGRADE_ACCESS_AGENT` - hda升级 * `SCHEDULED_TASK` - 定时任务 * `UPDATE_FREEZE_STATUS` - 更新服务器冻结状态

        :return: The job_type of this ListSubJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ListSubJobsRequest.

        job类型 * `CREATE_SERVER` - 创建服务器 * `DELETE_SERVER` - 删除服务器 * `REJOIN_DOMAIN` - 服务器重新加域 * `CHANGE_SERVER_IMAGE` - 修改服务器镜像 * `REINSTALL_OS` - 服务器重装操作系统 * `MIGRATE_SERVER` - 迁移服务器 * `UPDATE_SERVER_TSVI` - 更新虚拟IP配置 * `UPGRADE_ACCESS_AGENT` - hda升级 * `SCHEDULED_TASK` - 定时任务 * `UPDATE_FREEZE_STATUS` - 更新服务器冻结状态

        :param job_type: The job_type of this ListSubJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def offset(self):
        """Gets the offset of this ListSubJobsRequest.

        查询的偏移量。

        :return: The offset of this ListSubJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSubJobsRequest.

        查询的偏移量。

        :param offset: The offset of this ListSubJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSubJobsRequest.

        查询的数量，值区间[1-100]。

        :return: The limit of this ListSubJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubJobsRequest.

        查询的数量，值区间[1-100]。

        :param limit: The limit of this ListSubJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def job_id(self):
        """Gets the job_id of this ListSubJobsRequest.

        任务ID。

        :return: The job_id of this ListSubJobsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListSubJobsRequest.

        任务ID。

        :param job_id: The job_id of this ListSubJobsRequest.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ListSubJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
