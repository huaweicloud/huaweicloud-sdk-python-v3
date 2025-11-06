# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteClusterPortRequest:

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
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, cluster_id=None, id=None, type=None):
        r"""DeleteClusterPortRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param id: 端口的id
        :type id: str
        :param type: DELETE_DB 仅删除CPCS数据库中的记录，不删除elb资源。 TRY_DELETE 当被删除的端口的wrong字段为false时，删除elb资源。不为false时仅删除数据库。 FORCE_DELETE 删除cpcs数据库和elb资源
        :type type: str
        """
        
        

        self._cluster_id = None
        self._id = None
        self._type = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.id = id
        self.type = type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this DeleteClusterPortRequest.

        集群ID

        :return: The cluster_id of this DeleteClusterPortRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this DeleteClusterPortRequest.

        集群ID

        :param cluster_id: The cluster_id of this DeleteClusterPortRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def id(self):
        r"""Gets the id of this DeleteClusterPortRequest.

        端口的id

        :return: The id of this DeleteClusterPortRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteClusterPortRequest.

        端口的id

        :param id: The id of this DeleteClusterPortRequest.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this DeleteClusterPortRequest.

        DELETE_DB 仅删除CPCS数据库中的记录，不删除elb资源。 TRY_DELETE 当被删除的端口的wrong字段为false时，删除elb资源。不为false时仅删除数据库。 FORCE_DELETE 删除cpcs数据库和elb资源

        :return: The type of this DeleteClusterPortRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DeleteClusterPortRequest.

        DELETE_DB 仅删除CPCS数据库中的记录，不删除elb资源。 TRY_DELETE 当被删除的端口的wrong字段为false时，删除elb资源。不为false时仅删除数据库。 FORCE_DELETE 删除cpcs数据库和elb资源

        :param type: The type of this DeleteClusterPortRequest.
        :type type: str
        """
        self._type = type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteClusterPortRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
