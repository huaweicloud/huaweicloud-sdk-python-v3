# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'instance_id': 'str',
        'app_id': 'str',
        'target': 'str',
        'job_status': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'instance_id': 'instance_id',
        'app_id': 'app_id',
        'target': 'target',
        'job_status': 'job_status'
    }

    def __init__(self, offset=None, limit=None, instance_id=None, app_id=None, target=None, job_status=None):
        r"""ListJobsRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量，默认值0。
        :type offset: int
        :param limit: 单次查询的大小[1-100]，默认值10。
        :type limit: int
        :param instance_id: 实例ID。
        :type instance_id: str
        :param app_id: 应用ID。
        :type app_id: str
        :param target: 安装实例的用户。
        :type target: str
        :param job_status: 任务状态： * &#x60;INIT&#x60; - 初始化中 * &#x60;WAITING&#x60; - 等待安装结束 * &#x60;SUCCESS&#x60; - 成功 * &#x60;FAIL&#x60; - 失败任务状态
        :type job_status: str
        """
        
        

        self._offset = None
        self._limit = None
        self._instance_id = None
        self._app_id = None
        self._target = None
        self._job_status = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if instance_id is not None:
            self.instance_id = instance_id
        if app_id is not None:
            self.app_id = app_id
        if target is not None:
            self.target = target
        if job_status is not None:
            self.job_status = job_status

    @property
    def offset(self):
        r"""Gets the offset of this ListJobsRequest.

        查询的偏移量，默认值0。

        :return: The offset of this ListJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListJobsRequest.

        查询的偏移量，默认值0。

        :param offset: The offset of this ListJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListJobsRequest.

        单次查询的大小[1-100]，默认值10。

        :return: The limit of this ListJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListJobsRequest.

        单次查询的大小[1-100]，默认值10。

        :param limit: The limit of this ListJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListJobsRequest.

        实例ID。

        :return: The instance_id of this ListJobsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListJobsRequest.

        实例ID。

        :param instance_id: The instance_id of this ListJobsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def app_id(self):
        r"""Gets the app_id of this ListJobsRequest.

        应用ID。

        :return: The app_id of this ListJobsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ListJobsRequest.

        应用ID。

        :param app_id: The app_id of this ListJobsRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def target(self):
        r"""Gets the target of this ListJobsRequest.

        安装实例的用户。

        :return: The target of this ListJobsRequest.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this ListJobsRequest.

        安装实例的用户。

        :param target: The target of this ListJobsRequest.
        :type target: str
        """
        self._target = target

    @property
    def job_status(self):
        r"""Gets the job_status of this ListJobsRequest.

        任务状态： * `INIT` - 初始化中 * `WAITING` - 等待安装结束 * `SUCCESS` - 成功 * `FAIL` - 失败任务状态

        :return: The job_status of this ListJobsRequest.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        r"""Sets the job_status of this ListJobsRequest.

        任务状态： * `INIT` - 初始化中 * `WAITING` - 等待安装结束 * `SUCCESS` - 成功 * `FAIL` - 失败任务状态

        :param job_status: The job_status of this ListJobsRequest.
        :type job_status: str
        """
        self._job_status = job_status

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
        if not isinstance(other, ListJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
