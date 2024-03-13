# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkloadQueueUsersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workload_res_code': 'int',
        'workload_res_str': 'str',
        'queue_name': 'str',
        'user_list': 'list[WorkloadQueueUser]',
        'count': 'int'
    }

    attribute_map = {
        'workload_res_code': 'workload_res_code',
        'workload_res_str': 'workload_res_str',
        'queue_name': 'queue_name',
        'user_list': 'user_list',
        'count': 'count'
    }

    def __init__(self, workload_res_code=None, workload_res_str=None, queue_name=None, user_list=None, count=None):
        """ListWorkloadQueueUsersResponse

        The model defined in huaweicloud sdk

        :param workload_res_code: 结果状态码。
        :type workload_res_code: int
        :param workload_res_str: 结果描述。
        :type workload_res_str: str
        :param queue_name: 队列名称。
        :type queue_name: str
        :param user_list: 队列用户列表。
        :type user_list: list[:class:`huaweicloudsdkdws.v2.WorkloadQueueUser`]
        :param count: 总数量
        :type count: int
        """
        
        super(ListWorkloadQueueUsersResponse, self).__init__()

        self._workload_res_code = None
        self._workload_res_str = None
        self._queue_name = None
        self._user_list = None
        self._count = None
        self.discriminator = None

        if workload_res_code is not None:
            self.workload_res_code = workload_res_code
        if workload_res_str is not None:
            self.workload_res_str = workload_res_str
        if queue_name is not None:
            self.queue_name = queue_name
        if user_list is not None:
            self.user_list = user_list
        if count is not None:
            self.count = count

    @property
    def workload_res_code(self):
        """Gets the workload_res_code of this ListWorkloadQueueUsersResponse.

        结果状态码。

        :return: The workload_res_code of this ListWorkloadQueueUsersResponse.
        :rtype: int
        """
        return self._workload_res_code

    @workload_res_code.setter
    def workload_res_code(self, workload_res_code):
        """Sets the workload_res_code of this ListWorkloadQueueUsersResponse.

        结果状态码。

        :param workload_res_code: The workload_res_code of this ListWorkloadQueueUsersResponse.
        :type workload_res_code: int
        """
        self._workload_res_code = workload_res_code

    @property
    def workload_res_str(self):
        """Gets the workload_res_str of this ListWorkloadQueueUsersResponse.

        结果描述。

        :return: The workload_res_str of this ListWorkloadQueueUsersResponse.
        :rtype: str
        """
        return self._workload_res_str

    @workload_res_str.setter
    def workload_res_str(self, workload_res_str):
        """Sets the workload_res_str of this ListWorkloadQueueUsersResponse.

        结果描述。

        :param workload_res_str: The workload_res_str of this ListWorkloadQueueUsersResponse.
        :type workload_res_str: str
        """
        self._workload_res_str = workload_res_str

    @property
    def queue_name(self):
        """Gets the queue_name of this ListWorkloadQueueUsersResponse.

        队列名称。

        :return: The queue_name of this ListWorkloadQueueUsersResponse.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ListWorkloadQueueUsersResponse.

        队列名称。

        :param queue_name: The queue_name of this ListWorkloadQueueUsersResponse.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def user_list(self):
        """Gets the user_list of this ListWorkloadQueueUsersResponse.

        队列用户列表。

        :return: The user_list of this ListWorkloadQueueUsersResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.WorkloadQueueUser`]
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        """Sets the user_list of this ListWorkloadQueueUsersResponse.

        队列用户列表。

        :param user_list: The user_list of this ListWorkloadQueueUsersResponse.
        :type user_list: list[:class:`huaweicloudsdkdws.v2.WorkloadQueueUser`]
        """
        self._user_list = user_list

    @property
    def count(self):
        """Gets the count of this ListWorkloadQueueUsersResponse.

        总数量

        :return: The count of this ListWorkloadQueueUsersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListWorkloadQueueUsersResponse.

        总数量

        :param count: The count of this ListWorkloadQueueUsersResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListWorkloadQueueUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
