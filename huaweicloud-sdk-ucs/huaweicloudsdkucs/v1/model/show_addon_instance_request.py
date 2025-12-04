# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAddonInstanceRequest:

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
        'is_database_status': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'is_database_status': 'is_database_status',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, id=None, is_database_status=None, cluster_id=None):
        r"""ShowAddonInstanceRequest

        The model defined in huaweicloud sdk

        :param id: 插件实例id
        :type id: str
        :param is_database_status: 是否使用数据库存储的插件状态
        :type is_database_status: str
        :param cluster_id: 集群id
        :type cluster_id: str
        """
        
        

        self._id = None
        self._is_database_status = None
        self._cluster_id = None
        self.discriminator = None

        self.id = id
        if is_database_status is not None:
            self.is_database_status = is_database_status
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def id(self):
        r"""Gets the id of this ShowAddonInstanceRequest.

        插件实例id

        :return: The id of this ShowAddonInstanceRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAddonInstanceRequest.

        插件实例id

        :param id: The id of this ShowAddonInstanceRequest.
        :type id: str
        """
        self._id = id

    @property
    def is_database_status(self):
        r"""Gets the is_database_status of this ShowAddonInstanceRequest.

        是否使用数据库存储的插件状态

        :return: The is_database_status of this ShowAddonInstanceRequest.
        :rtype: str
        """
        return self._is_database_status

    @is_database_status.setter
    def is_database_status(self, is_database_status):
        r"""Sets the is_database_status of this ShowAddonInstanceRequest.

        是否使用数据库存储的插件状态

        :param is_database_status: The is_database_status of this ShowAddonInstanceRequest.
        :type is_database_status: str
        """
        self._is_database_status = is_database_status

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowAddonInstanceRequest.

        集群id

        :return: The cluster_id of this ShowAddonInstanceRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowAddonInstanceRequest.

        集群id

        :param cluster_id: The cluster_id of this ShowAddonInstanceRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, ShowAddonInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
