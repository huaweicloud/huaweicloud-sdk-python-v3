# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShrinkClusterReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shrink': 'list[ShrinkNodeReq]',
        'agency_name': 'str',
        'operation_type': 'str',
        'cluster_load_check': 'bool'
    }

    attribute_map = {
        'shrink': 'shrink',
        'agency_name': 'agency_name',
        'operation_type': 'operation_type',
        'cluster_load_check': 'cluster_load_check'
    }

    def __init__(self, shrink=None, agency_name=None, operation_type=None, cluster_load_check=None):
        r"""ShrinkClusterReq

        The model defined in huaweicloud sdk

        :param shrink: 需要缩容的节点类型和数量集合。
        :type shrink: list[:class:`huaweicloudsdkcss.v1.ShrinkNodeReq`]
        :param agency_name: 委托名称，委托给CSS服务，允许CSS调用您的其他云服务。
        :type agency_name: str
        :param operation_type: 操作类型。
        :type operation_type: str
        :param cluster_load_check: 是否需要检查集群负载。
        :type cluster_load_check: bool
        """
        
        

        self._shrink = None
        self._agency_name = None
        self._operation_type = None
        self._cluster_load_check = None
        self.discriminator = None

        self.shrink = shrink
        if agency_name is not None:
            self.agency_name = agency_name
        if operation_type is not None:
            self.operation_type = operation_type
        if cluster_load_check is not None:
            self.cluster_load_check = cluster_load_check

    @property
    def shrink(self):
        r"""Gets the shrink of this ShrinkClusterReq.

        需要缩容的节点类型和数量集合。

        :return: The shrink of this ShrinkClusterReq.
        :rtype: list[:class:`huaweicloudsdkcss.v1.ShrinkNodeReq`]
        """
        return self._shrink

    @shrink.setter
    def shrink(self, shrink):
        r"""Sets the shrink of this ShrinkClusterReq.

        需要缩容的节点类型和数量集合。

        :param shrink: The shrink of this ShrinkClusterReq.
        :type shrink: list[:class:`huaweicloudsdkcss.v1.ShrinkNodeReq`]
        """
        self._shrink = shrink

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ShrinkClusterReq.

        委托名称，委托给CSS服务，允许CSS调用您的其他云服务。

        :return: The agency_name of this ShrinkClusterReq.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ShrinkClusterReq.

        委托名称，委托给CSS服务，允许CSS调用您的其他云服务。

        :param agency_name: The agency_name of this ShrinkClusterReq.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def operation_type(self):
        r"""Gets the operation_type of this ShrinkClusterReq.

        操作类型。

        :return: The operation_type of this ShrinkClusterReq.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this ShrinkClusterReq.

        操作类型。

        :param operation_type: The operation_type of this ShrinkClusterReq.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def cluster_load_check(self):
        r"""Gets the cluster_load_check of this ShrinkClusterReq.

        是否需要检查集群负载。

        :return: The cluster_load_check of this ShrinkClusterReq.
        :rtype: bool
        """
        return self._cluster_load_check

    @cluster_load_check.setter
    def cluster_load_check(self, cluster_load_check):
        r"""Sets the cluster_load_check of this ShrinkClusterReq.

        是否需要检查集群负载。

        :param cluster_load_check: The cluster_load_check of this ShrinkClusterReq.
        :type cluster_load_check: bool
        """
        self._cluster_load_check = cluster_load_check

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
        if not isinstance(other, ShrinkClusterReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
