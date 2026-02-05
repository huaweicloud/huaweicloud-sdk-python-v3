# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectConfigClusterGroupIdEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_group_id': 'str',
        'project_config_id': 'str'
    }

    attribute_map = {
        'cluster_group_id': 'cluster_group_id',
        'project_config_id': 'project_config_id'
    }

    def __init__(self, cluster_group_id=None, project_config_id=None):
        r"""ProjectConfigClusterGroupIdEntity

        The model defined in huaweicloud sdk

        :param cluster_group_id: 集群ID
        :type cluster_group_id: str
        :param project_config_id: 项目配置ID
        :type project_config_id: str
        """
        
        

        self._cluster_group_id = None
        self._project_config_id = None
        self.discriminator = None

        if cluster_group_id is not None:
            self.cluster_group_id = cluster_group_id
        if project_config_id is not None:
            self.project_config_id = project_config_id

    @property
    def cluster_group_id(self):
        r"""Gets the cluster_group_id of this ProjectConfigClusterGroupIdEntity.

        集群ID

        :return: The cluster_group_id of this ProjectConfigClusterGroupIdEntity.
        :rtype: str
        """
        return self._cluster_group_id

    @cluster_group_id.setter
    def cluster_group_id(self, cluster_group_id):
        r"""Sets the cluster_group_id of this ProjectConfigClusterGroupIdEntity.

        集群ID

        :param cluster_group_id: The cluster_group_id of this ProjectConfigClusterGroupIdEntity.
        :type cluster_group_id: str
        """
        self._cluster_group_id = cluster_group_id

    @property
    def project_config_id(self):
        r"""Gets the project_config_id of this ProjectConfigClusterGroupIdEntity.

        项目配置ID

        :return: The project_config_id of this ProjectConfigClusterGroupIdEntity.
        :rtype: str
        """
        return self._project_config_id

    @project_config_id.setter
    def project_config_id(self, project_config_id):
        r"""Sets the project_config_id of this ProjectConfigClusterGroupIdEntity.

        项目配置ID

        :param project_config_id: The project_config_id of this ProjectConfigClusterGroupIdEntity.
        :type project_config_id: str
        """
        self._project_config_id = project_config_id

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
        if not isinstance(other, ProjectConfigClusterGroupIdEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
