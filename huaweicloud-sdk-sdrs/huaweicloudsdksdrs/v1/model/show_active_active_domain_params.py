# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowActiveActiveDomainParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'sold_out': 'bool',
        'local_replication_cluster': 'ReplicationClusterParams',
        'remote_replication_cluster': 'ReplicationClusterParams'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'sold_out': 'sold_out',
        'local_replication_cluster': 'local_replication_cluster',
        'remote_replication_cluster': 'remote_replication_cluster'
    }

    def __init__(self, id=None, name=None, description=None, sold_out=None, local_replication_cluster=None, remote_replication_cluster=None):
        r"""ShowActiveActiveDomainParams

        The model defined in huaweicloud sdk

        :param id: 双活域ID。
        :type id: str
        :param name: 双活域名称。
        :type name: str
        :param description: 双活域描述。
        :type description: str
        :param sold_out: 表示该双活域下的资源是否售罄。
        :type sold_out: bool
        :param local_replication_cluster: 
        :type local_replication_cluster: :class:`huaweicloudsdksdrs.v1.ReplicationClusterParams`
        :param remote_replication_cluster: 
        :type remote_replication_cluster: :class:`huaweicloudsdksdrs.v1.ReplicationClusterParams`
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._sold_out = None
        self._local_replication_cluster = None
        self._remote_replication_cluster = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.sold_out = sold_out
        self.local_replication_cluster = local_replication_cluster
        self.remote_replication_cluster = remote_replication_cluster

    @property
    def id(self):
        r"""Gets the id of this ShowActiveActiveDomainParams.

        双活域ID。

        :return: The id of this ShowActiveActiveDomainParams.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowActiveActiveDomainParams.

        双活域ID。

        :param id: The id of this ShowActiveActiveDomainParams.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowActiveActiveDomainParams.

        双活域名称。

        :return: The name of this ShowActiveActiveDomainParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowActiveActiveDomainParams.

        双活域名称。

        :param name: The name of this ShowActiveActiveDomainParams.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowActiveActiveDomainParams.

        双活域描述。

        :return: The description of this ShowActiveActiveDomainParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowActiveActiveDomainParams.

        双活域描述。

        :param description: The description of this ShowActiveActiveDomainParams.
        :type description: str
        """
        self._description = description

    @property
    def sold_out(self):
        r"""Gets the sold_out of this ShowActiveActiveDomainParams.

        表示该双活域下的资源是否售罄。

        :return: The sold_out of this ShowActiveActiveDomainParams.
        :rtype: bool
        """
        return self._sold_out

    @sold_out.setter
    def sold_out(self, sold_out):
        r"""Sets the sold_out of this ShowActiveActiveDomainParams.

        表示该双活域下的资源是否售罄。

        :param sold_out: The sold_out of this ShowActiveActiveDomainParams.
        :type sold_out: bool
        """
        self._sold_out = sold_out

    @property
    def local_replication_cluster(self):
        r"""Gets the local_replication_cluster of this ShowActiveActiveDomainParams.

        :return: The local_replication_cluster of this ShowActiveActiveDomainParams.
        :rtype: :class:`huaweicloudsdksdrs.v1.ReplicationClusterParams`
        """
        return self._local_replication_cluster

    @local_replication_cluster.setter
    def local_replication_cluster(self, local_replication_cluster):
        r"""Sets the local_replication_cluster of this ShowActiveActiveDomainParams.

        :param local_replication_cluster: The local_replication_cluster of this ShowActiveActiveDomainParams.
        :type local_replication_cluster: :class:`huaweicloudsdksdrs.v1.ReplicationClusterParams`
        """
        self._local_replication_cluster = local_replication_cluster

    @property
    def remote_replication_cluster(self):
        r"""Gets the remote_replication_cluster of this ShowActiveActiveDomainParams.

        :return: The remote_replication_cluster of this ShowActiveActiveDomainParams.
        :rtype: :class:`huaweicloudsdksdrs.v1.ReplicationClusterParams`
        """
        return self._remote_replication_cluster

    @remote_replication_cluster.setter
    def remote_replication_cluster(self, remote_replication_cluster):
        r"""Sets the remote_replication_cluster of this ShowActiveActiveDomainParams.

        :param remote_replication_cluster: The remote_replication_cluster of this ShowActiveActiveDomainParams.
        :type remote_replication_cluster: :class:`huaweicloudsdksdrs.v1.ReplicationClusterParams`
        """
        self._remote_replication_cluster = remote_replication_cluster

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
        if not isinstance(other, ShowActiveActiveDomainParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
