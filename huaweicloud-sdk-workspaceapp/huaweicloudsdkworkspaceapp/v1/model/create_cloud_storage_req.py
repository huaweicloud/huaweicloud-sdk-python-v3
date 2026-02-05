# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCloudStorageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_config_cluster_group_id_list': 'list[ProjectConfigClusterGroupIdEntity]'
    }

    attribute_map = {
        'project_config_cluster_group_id_list': 'project_config_cluster_group_id_list'
    }

    def __init__(self, project_config_cluster_group_id_list=None):
        r"""CreateCloudStorageReq

        The model defined in huaweicloud sdk

        :param project_config_cluster_group_id_list: 创建项目配置关联ID列表。
        :type project_config_cluster_group_id_list: list[:class:`huaweicloudsdkworkspaceapp.v1.ProjectConfigClusterGroupIdEntity`]
        """
        
        

        self._project_config_cluster_group_id_list = None
        self.discriminator = None

        self.project_config_cluster_group_id_list = project_config_cluster_group_id_list

    @property
    def project_config_cluster_group_id_list(self):
        r"""Gets the project_config_cluster_group_id_list of this CreateCloudStorageReq.

        创建项目配置关联ID列表。

        :return: The project_config_cluster_group_id_list of this CreateCloudStorageReq.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.ProjectConfigClusterGroupIdEntity`]
        """
        return self._project_config_cluster_group_id_list

    @project_config_cluster_group_id_list.setter
    def project_config_cluster_group_id_list(self, project_config_cluster_group_id_list):
        r"""Sets the project_config_cluster_group_id_list of this CreateCloudStorageReq.

        创建项目配置关联ID列表。

        :param project_config_cluster_group_id_list: The project_config_cluster_group_id_list of this CreateCloudStorageReq.
        :type project_config_cluster_group_id_list: list[:class:`huaweicloudsdkworkspaceapp.v1.ProjectConfigClusterGroupIdEntity`]
        """
        self._project_config_cluster_group_id_list = project_config_cluster_group_id_list

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
        if not isinstance(other, CreateCloudStorageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
