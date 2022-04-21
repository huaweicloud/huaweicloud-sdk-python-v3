# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFailureJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'failure_status': 'str',
        'resource_name': 'str',
        'server_group_id': 'str',
        'resource_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'failure_status': 'failure_status',
        'resource_name': 'resource_name',
        'server_group_id': 'server_group_id',
        'resource_type': 'resource_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, failure_status=None, resource_name=None, server_group_id=None, resource_type=None, limit=None, offset=None):
        """ListFailureJobsRequest

        The model defined in huaweicloud sdk

        :param failure_status: 失败任务状态。createFail：表示创建失败。deleteFail：表示删除失败。attachFail：表示挂载失败。detachFail：表示卸载失败。expandFail：表示扩容失败。resizeFail：表示变更规格失败。startFail：表示开启保护失败。stopFail：表示停止保护失败。reverseFail：表示切换失败。failoverFail：表示故障切换失败。reprotectFail : 表示重保护失败。
        :type failure_status: str
        :param resource_name: 保护组资源名称。
        :type resource_name: str
        :param server_group_id: 保护组ID。
        :type server_group_id: str
        :param resource_type: 资源类型。server_groups：表示保护组。protected_instances：表示保护实例。replications：表示复制对。disaster_recovery_drills：表示容灾演练。
        :type resource_type: str
        :param limit: 每次请求返回结果个数限制。取值范围为[0,1000]的正整数，默认值为1000。
        :type limit: int
        :param offset: 每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。
        :type offset: int
        """
        
        

        self._failure_status = None
        self._resource_name = None
        self._server_group_id = None
        self._resource_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if failure_status is not None:
            self.failure_status = failure_status
        if resource_name is not None:
            self.resource_name = resource_name
        if server_group_id is not None:
            self.server_group_id = server_group_id
        if resource_type is not None:
            self.resource_type = resource_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def failure_status(self):
        """Gets the failure_status of this ListFailureJobsRequest.

        失败任务状态。createFail：表示创建失败。deleteFail：表示删除失败。attachFail：表示挂载失败。detachFail：表示卸载失败。expandFail：表示扩容失败。resizeFail：表示变更规格失败。startFail：表示开启保护失败。stopFail：表示停止保护失败。reverseFail：表示切换失败。failoverFail：表示故障切换失败。reprotectFail : 表示重保护失败。

        :return: The failure_status of this ListFailureJobsRequest.
        :rtype: str
        """
        return self._failure_status

    @failure_status.setter
    def failure_status(self, failure_status):
        """Sets the failure_status of this ListFailureJobsRequest.

        失败任务状态。createFail：表示创建失败。deleteFail：表示删除失败。attachFail：表示挂载失败。detachFail：表示卸载失败。expandFail：表示扩容失败。resizeFail：表示变更规格失败。startFail：表示开启保护失败。stopFail：表示停止保护失败。reverseFail：表示切换失败。failoverFail：表示故障切换失败。reprotectFail : 表示重保护失败。

        :param failure_status: The failure_status of this ListFailureJobsRequest.
        :type failure_status: str
        """
        self._failure_status = failure_status

    @property
    def resource_name(self):
        """Gets the resource_name of this ListFailureJobsRequest.

        保护组资源名称。

        :return: The resource_name of this ListFailureJobsRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ListFailureJobsRequest.

        保护组资源名称。

        :param resource_name: The resource_name of this ListFailureJobsRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ListFailureJobsRequest.

        保护组ID。

        :return: The server_group_id of this ListFailureJobsRequest.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ListFailureJobsRequest.

        保护组ID。

        :param server_group_id: The server_group_id of this ListFailureJobsRequest.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def resource_type(self):
        """Gets the resource_type of this ListFailureJobsRequest.

        资源类型。server_groups：表示保护组。protected_instances：表示保护实例。replications：表示复制对。disaster_recovery_drills：表示容灾演练。

        :return: The resource_type of this ListFailureJobsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListFailureJobsRequest.

        资源类型。server_groups：表示保护组。protected_instances：表示保护实例。replications：表示复制对。disaster_recovery_drills：表示容灾演练。

        :param resource_type: The resource_type of this ListFailureJobsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def limit(self):
        """Gets the limit of this ListFailureJobsRequest.

        每次请求返回结果个数限制。取值范围为[0,1000]的正整数，默认值为1000。

        :return: The limit of this ListFailureJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFailureJobsRequest.

        每次请求返回结果个数限制。取值范围为[0,1000]的正整数，默认值为1000。

        :param limit: The limit of this ListFailureJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListFailureJobsRequest.

        每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。

        :return: The offset of this ListFailureJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFailureJobsRequest.

        每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。

        :param offset: The offset of this ListFailureJobsRequest.
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
        if not isinstance(other, ListFailureJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
