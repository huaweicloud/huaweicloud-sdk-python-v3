# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'start': 'str',
        'limit': 'str',
        'certs_type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'start': 'start',
        'limit': 'limit',
        'certs_type': 'certsType'
    }

    def __init__(self, cluster_id=None, start=None, limit=None, certs_type=None):
        """ListCertsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 指定待查询的集群ID。
        :type cluster_id: str
        :param start: 指定查询起始值，默认值为1，即从第1个证书开始查询。
        :type start: str
        :param limit: 指定查询个数，默认值为10，即一次查询10个证书信息。
        :type limit: str
        :param certs_type: 证书类型。defaultCerts为默认证书类型，不指定查询证书类型默认查找自定义证书列表。
        :type certs_type: str
        """
        
        

        self._cluster_id = None
        self._start = None
        self._limit = None
        self._certs_type = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit
        if certs_type is not None:
            self.certs_type = certs_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListCertsRequest.

        指定待查询的集群ID。

        :return: The cluster_id of this ListCertsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListCertsRequest.

        指定待查询的集群ID。

        :param cluster_id: The cluster_id of this ListCertsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def start(self):
        """Gets the start of this ListCertsRequest.

        指定查询起始值，默认值为1，即从第1个证书开始查询。

        :return: The start of this ListCertsRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListCertsRequest.

        指定查询起始值，默认值为1，即从第1个证书开始查询。

        :param start: The start of this ListCertsRequest.
        :type start: str
        """
        self._start = start

    @property
    def limit(self):
        """Gets the limit of this ListCertsRequest.

        指定查询个数，默认值为10，即一次查询10个证书信息。

        :return: The limit of this ListCertsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCertsRequest.

        指定查询个数，默认值为10，即一次查询10个证书信息。

        :param limit: The limit of this ListCertsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def certs_type(self):
        """Gets the certs_type of this ListCertsRequest.

        证书类型。defaultCerts为默认证书类型，不指定查询证书类型默认查找自定义证书列表。

        :return: The certs_type of this ListCertsRequest.
        :rtype: str
        """
        return self._certs_type

    @certs_type.setter
    def certs_type(self, certs_type):
        """Sets the certs_type of this ListCertsRequest.

        证书类型。defaultCerts为默认证书类型，不指定查询证书类型默认查找自定义证书列表。

        :param certs_type: The certs_type of this ListCertsRequest.
        :type certs_type: str
        """
        self._certs_type = certs_type

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
        if not isinstance(other, ListCertsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
