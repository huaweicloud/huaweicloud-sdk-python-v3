# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostClustersResponse(SdkResponse):

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
        'total': 'int',
        'result': 'list[HostClusterInfo]'
    }

    attribute_map = {
        'status': 'status',
        'total': 'total',
        'result': 'result'
    }

    def __init__(self, status=None, total=None, result=None):
        """ListHostClustersResponse

        The model defined in huaweicloud sdk

        :param status: 请求状态
        :type status: str
        :param total: 主机集群个数
        :type total: int
        :param result: 主机集群详情响应体
        :type result: list[:class:`huaweicloudsdkcodeartsdeploy.v2.HostClusterInfo`]
        """
        
        super(ListHostClustersResponse, self).__init__()

        self._status = None
        self._total = None
        self._result = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if total is not None:
            self.total = total
        if result is not None:
            self.result = result

    @property
    def status(self):
        """Gets the status of this ListHostClustersResponse.

        请求状态

        :return: The status of this ListHostClustersResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListHostClustersResponse.

        请求状态

        :param status: The status of this ListHostClustersResponse.
        :type status: str
        """
        self._status = status

    @property
    def total(self):
        """Gets the total of this ListHostClustersResponse.

        主机集群个数

        :return: The total of this ListHostClustersResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListHostClustersResponse.

        主机集群个数

        :param total: The total of this ListHostClustersResponse.
        :type total: int
        """
        self._total = total

    @property
    def result(self):
        """Gets the result of this ListHostClustersResponse.

        主机集群详情响应体

        :return: The result of this ListHostClustersResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.HostClusterInfo`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ListHostClustersResponse.

        主机集群详情响应体

        :param result: The result of this ListHostClustersResponse.
        :type result: list[:class:`huaweicloudsdkcodeartsdeploy.v2.HostClusterInfo`]
        """
        self._result = result

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
        if not isinstance(other, ListHostClustersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
