# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'host_groups': 'list[DeploymentGroupDetail]'
    }

    attribute_map = {
        'total': 'total',
        'host_groups': 'host_groups'
    }

    def __init__(self, total=None, host_groups=None):
        """ListHostGroupsResponse

        The model defined in huaweicloud sdk

        :param total: 主机集群个数
        :type total: int
        :param host_groups: 主机集群详情响应体
        :type host_groups: list[:class:`huaweicloudsdkcodeartsdeploy.v2.DeploymentGroupDetail`]
        """
        
        super(ListHostGroupsResponse, self).__init__()

        self._total = None
        self._host_groups = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if host_groups is not None:
            self.host_groups = host_groups

    @property
    def total(self):
        """Gets the total of this ListHostGroupsResponse.

        主机集群个数

        :return: The total of this ListHostGroupsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListHostGroupsResponse.

        主机集群个数

        :param total: The total of this ListHostGroupsResponse.
        :type total: int
        """
        self._total = total

    @property
    def host_groups(self):
        """Gets the host_groups of this ListHostGroupsResponse.

        主机集群详情响应体

        :return: The host_groups of this ListHostGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.DeploymentGroupDetail`]
        """
        return self._host_groups

    @host_groups.setter
    def host_groups(self, host_groups):
        """Sets the host_groups of this ListHostGroupsResponse.

        主机集群详情响应体

        :param host_groups: The host_groups of this ListHostGroupsResponse.
        :type host_groups: list[:class:`huaweicloudsdkcodeartsdeploy.v2.DeploymentGroupDetail`]
        """
        self._host_groups = host_groups

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
        if not isinstance(other, ListHostGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
