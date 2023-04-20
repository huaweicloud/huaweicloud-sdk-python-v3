# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClustersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'state': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'state': 'state',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, cluster_name=None, state=None, limit=None, offset=None):
        """ListClustersRequest

        The model defined in huaweicloud sdk

        :param cluster_name: 边缘集群名称
        :type cluster_name: str
        :param state: 边缘集群状态
        :type state: str
        :param limit: 每页记录数，默认值为10，取值区间为1-1000。
        :type limit: int
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0。
        :type offset: int
        """
        
        

        self._cluster_name = None
        self._state = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name
        if state is not None:
            self.state = state
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ListClustersRequest.

        边缘集群名称

        :return: The cluster_name of this ListClustersRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ListClustersRequest.

        边缘集群名称

        :param cluster_name: The cluster_name of this ListClustersRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def state(self):
        """Gets the state of this ListClustersRequest.

        边缘集群状态

        :return: The state of this ListClustersRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListClustersRequest.

        边缘集群状态

        :param state: The state of this ListClustersRequest.
        :type state: str
        """
        self._state = state

    @property
    def limit(self):
        """Gets the limit of this ListClustersRequest.

        每页记录数，默认值为10，取值区间为1-1000。

        :return: The limit of this ListClustersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListClustersRequest.

        每页记录数，默认值为10，取值区间为1-1000。

        :param limit: The limit of this ListClustersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListClustersRequest.

        查询的起始位置，取值范围为非负整数，默认为0。

        :return: The offset of this ListClustersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListClustersRequest.

        查询的起始位置，取值范围为非负整数，默认为0。

        :param offset: The offset of this ListClustersRequest.
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
        if not isinstance(other, ListClustersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
