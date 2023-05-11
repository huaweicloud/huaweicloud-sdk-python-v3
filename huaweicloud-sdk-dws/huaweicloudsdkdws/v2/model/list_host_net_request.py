# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostNetRequest:

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
        'instance_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'instance_name': 'instance_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, cluster_id=None, instance_name=None, limit=None, offset=None):
        """ListHostNetRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID。获取方法，请参见9.6-获取集群ID。
        :type cluster_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param limit: 数据条目数。
        :type limit: int
        :param offset: 数据偏移量。
        :type offset: int
        """
        
        

        self._cluster_id = None
        self._instance_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if instance_name is not None:
            self.instance_name = instance_name
        self.limit = limit
        self.offset = offset

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListHostNetRequest.

        集群ID。获取方法，请参见9.6-获取集群ID。

        :return: The cluster_id of this ListHostNetRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListHostNetRequest.

        集群ID。获取方法，请参见9.6-获取集群ID。

        :param cluster_id: The cluster_id of this ListHostNetRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def instance_name(self):
        """Gets the instance_name of this ListHostNetRequest.

        实例名称。

        :return: The instance_name of this ListHostNetRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ListHostNetRequest.

        实例名称。

        :param instance_name: The instance_name of this ListHostNetRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def limit(self):
        """Gets the limit of this ListHostNetRequest.

        数据条目数。

        :return: The limit of this ListHostNetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHostNetRequest.

        数据条目数。

        :param limit: The limit of this ListHostNetRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListHostNetRequest.

        数据偏移量。

        :return: The offset of this ListHostNetRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHostNetRequest.

        数据偏移量。

        :param offset: The offset of this ListHostNetRequest.
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
        if not isinstance(other, ListHostNetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
