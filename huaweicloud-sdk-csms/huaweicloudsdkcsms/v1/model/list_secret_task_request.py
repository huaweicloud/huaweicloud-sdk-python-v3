# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecretTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secret_name': 'str',
        'status': 'str',
        'task_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'secret_name': 'secret_name',
        'status': 'status',
        'task_id': 'task_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, secret_name=None, status=None, task_id=None, limit=None, marker=None):
        r"""ListSecretTaskRequest

        The model defined in huaweicloud sdk

        :param secret_name: 凭据的名称。
        :type secret_name: str
        :param status: 任务状态。取值 ：  - SUCCESS ：任务轮转成功。 - FAILED ：任务轮转失败。
        :type status: str
        :param task_id: 任务ID。 该参数与其他参数不能同时存在。
        :type task_id: str
        :param limit: 每页返回的个数。 默认值：50。
        :type limit: int
        :param marker: 分页查询起始的任务ID，为空时为查询第一页。
        :type marker: str
        """
        
        

        self._secret_name = None
        self._status = None
        self._task_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if secret_name is not None:
            self.secret_name = secret_name
        if status is not None:
            self.status = status
        if task_id is not None:
            self.task_id = task_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def secret_name(self):
        r"""Gets the secret_name of this ListSecretTaskRequest.

        凭据的名称。

        :return: The secret_name of this ListSecretTaskRequest.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        r"""Sets the secret_name of this ListSecretTaskRequest.

        凭据的名称。

        :param secret_name: The secret_name of this ListSecretTaskRequest.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def status(self):
        r"""Gets the status of this ListSecretTaskRequest.

        任务状态。取值 ：  - SUCCESS ：任务轮转成功。 - FAILED ：任务轮转失败。

        :return: The status of this ListSecretTaskRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSecretTaskRequest.

        任务状态。取值 ：  - SUCCESS ：任务轮转成功。 - FAILED ：任务轮转失败。

        :param status: The status of this ListSecretTaskRequest.
        :type status: str
        """
        self._status = status

    @property
    def task_id(self):
        r"""Gets the task_id of this ListSecretTaskRequest.

        任务ID。 该参数与其他参数不能同时存在。

        :return: The task_id of this ListSecretTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListSecretTaskRequest.

        任务ID。 该参数与其他参数不能同时存在。

        :param task_id: The task_id of this ListSecretTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def limit(self):
        r"""Gets the limit of this ListSecretTaskRequest.

        每页返回的个数。 默认值：50。

        :return: The limit of this ListSecretTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecretTaskRequest.

        每页返回的个数。 默认值：50。

        :param limit: The limit of this ListSecretTaskRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListSecretTaskRequest.

        分页查询起始的任务ID，为空时为查询第一页。

        :return: The marker of this ListSecretTaskRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListSecretTaskRequest.

        分页查询起始的任务ID，为空时为查询第一页。

        :param marker: The marker of this ListSecretTaskRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListSecretTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
