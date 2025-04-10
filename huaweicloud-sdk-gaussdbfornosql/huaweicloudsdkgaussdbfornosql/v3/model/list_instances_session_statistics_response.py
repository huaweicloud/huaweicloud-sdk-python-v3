# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesSessionStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_connection_count': 'int',
        'active_connection_count': 'int',
        'top_source_ips': 'list[ListInstancesSessionStatisticsRespondBodyTopSourceIps]',
        'top_dbs': 'object'
    }

    attribute_map = {
        'total_connection_count': 'total_connection_count',
        'active_connection_count': 'active_connection_count',
        'top_source_ips': 'top_source_ips',
        'top_dbs': 'top_dbs'
    }

    def __init__(self, total_connection_count=None, active_connection_count=None, top_source_ips=None, top_dbs=None):
        r"""ListInstancesSessionStatisticsResponse

        The model defined in huaweicloud sdk

        :param total_connection_count: 总客户端连接数。
        :type total_connection_count: int
        :param active_connection_count: active_connection_count
        :type active_connection_count: int
        :param top_source_ips: 节点连接的各个客户端连接数汇总，从大到小取前十个，最多十个，展示客户端的ip地址和连接总数。
        :type top_source_ips: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesSessionStatisticsRespondBodyTopSourceIps`]
        :param top_dbs: 节点各数据库连接的客户端的ip和该ip连接节点的连接数，按连接数从高到低取前十个，最多十个。
        :type top_dbs: object
        """
        
        super(ListInstancesSessionStatisticsResponse, self).__init__()

        self._total_connection_count = None
        self._active_connection_count = None
        self._top_source_ips = None
        self._top_dbs = None
        self.discriminator = None

        if total_connection_count is not None:
            self.total_connection_count = total_connection_count
        if active_connection_count is not None:
            self.active_connection_count = active_connection_count
        if top_source_ips is not None:
            self.top_source_ips = top_source_ips
        if top_dbs is not None:
            self.top_dbs = top_dbs

    @property
    def total_connection_count(self):
        r"""Gets the total_connection_count of this ListInstancesSessionStatisticsResponse.

        总客户端连接数。

        :return: The total_connection_count of this ListInstancesSessionStatisticsResponse.
        :rtype: int
        """
        return self._total_connection_count

    @total_connection_count.setter
    def total_connection_count(self, total_connection_count):
        r"""Sets the total_connection_count of this ListInstancesSessionStatisticsResponse.

        总客户端连接数。

        :param total_connection_count: The total_connection_count of this ListInstancesSessionStatisticsResponse.
        :type total_connection_count: int
        """
        self._total_connection_count = total_connection_count

    @property
    def active_connection_count(self):
        r"""Gets the active_connection_count of this ListInstancesSessionStatisticsResponse.

        active_connection_count

        :return: The active_connection_count of this ListInstancesSessionStatisticsResponse.
        :rtype: int
        """
        return self._active_connection_count

    @active_connection_count.setter
    def active_connection_count(self, active_connection_count):
        r"""Sets the active_connection_count of this ListInstancesSessionStatisticsResponse.

        active_connection_count

        :param active_connection_count: The active_connection_count of this ListInstancesSessionStatisticsResponse.
        :type active_connection_count: int
        """
        self._active_connection_count = active_connection_count

    @property
    def top_source_ips(self):
        r"""Gets the top_source_ips of this ListInstancesSessionStatisticsResponse.

        节点连接的各个客户端连接数汇总，从大到小取前十个，最多十个，展示客户端的ip地址和连接总数。

        :return: The top_source_ips of this ListInstancesSessionStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesSessionStatisticsRespondBodyTopSourceIps`]
        """
        return self._top_source_ips

    @top_source_ips.setter
    def top_source_ips(self, top_source_ips):
        r"""Sets the top_source_ips of this ListInstancesSessionStatisticsResponse.

        节点连接的各个客户端连接数汇总，从大到小取前十个，最多十个，展示客户端的ip地址和连接总数。

        :param top_source_ips: The top_source_ips of this ListInstancesSessionStatisticsResponse.
        :type top_source_ips: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ListInstancesSessionStatisticsRespondBodyTopSourceIps`]
        """
        self._top_source_ips = top_source_ips

    @property
    def top_dbs(self):
        r"""Gets the top_dbs of this ListInstancesSessionStatisticsResponse.

        节点各数据库连接的客户端的ip和该ip连接节点的连接数，按连接数从高到低取前十个，最多十个。

        :return: The top_dbs of this ListInstancesSessionStatisticsResponse.
        :rtype: object
        """
        return self._top_dbs

    @top_dbs.setter
    def top_dbs(self, top_dbs):
        r"""Sets the top_dbs of this ListInstancesSessionStatisticsResponse.

        节点各数据库连接的客户端的ip和该ip连接节点的连接数，按连接数从高到低取前十个，最多十个。

        :param top_dbs: The top_dbs of this ListInstancesSessionStatisticsResponse.
        :type top_dbs: object
        """
        self._top_dbs = top_dbs

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
        if not isinstance(other, ListInstancesSessionStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
