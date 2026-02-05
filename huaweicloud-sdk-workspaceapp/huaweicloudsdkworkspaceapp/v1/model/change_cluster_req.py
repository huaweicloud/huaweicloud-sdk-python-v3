# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeClusterReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_cluster_group_id': 'str',
        'target_project_config_id': 'str',
        'cloud_storage_assignment_ids': 'list[str]'
    }

    attribute_map = {
        'target_cluster_group_id': 'target_cluster_group_id',
        'target_project_config_id': 'target_project_config_id',
        'cloud_storage_assignment_ids': 'cloud_storage_assignment_ids'
    }

    def __init__(self, target_cluster_group_id=None, target_project_config_id=None, cloud_storage_assignment_ids=None):
        r"""ChangeClusterReq

        The model defined in huaweicloud sdk

        :param target_cluster_group_id: 目标集群ID
        :type target_cluster_group_id: str
        :param target_project_config_id: 目标项目配置ID
        :type target_project_config_id: str
        :param cloud_storage_assignment_ids: 文件系统id,数量区间 [1, 50]。
        :type cloud_storage_assignment_ids: list[str]
        """
        
        

        self._target_cluster_group_id = None
        self._target_project_config_id = None
        self._cloud_storage_assignment_ids = None
        self.discriminator = None

        self.target_cluster_group_id = target_cluster_group_id
        self.target_project_config_id = target_project_config_id
        self.cloud_storage_assignment_ids = cloud_storage_assignment_ids

    @property
    def target_cluster_group_id(self):
        r"""Gets the target_cluster_group_id of this ChangeClusterReq.

        目标集群ID

        :return: The target_cluster_group_id of this ChangeClusterReq.
        :rtype: str
        """
        return self._target_cluster_group_id

    @target_cluster_group_id.setter
    def target_cluster_group_id(self, target_cluster_group_id):
        r"""Sets the target_cluster_group_id of this ChangeClusterReq.

        目标集群ID

        :param target_cluster_group_id: The target_cluster_group_id of this ChangeClusterReq.
        :type target_cluster_group_id: str
        """
        self._target_cluster_group_id = target_cluster_group_id

    @property
    def target_project_config_id(self):
        r"""Gets the target_project_config_id of this ChangeClusterReq.

        目标项目配置ID

        :return: The target_project_config_id of this ChangeClusterReq.
        :rtype: str
        """
        return self._target_project_config_id

    @target_project_config_id.setter
    def target_project_config_id(self, target_project_config_id):
        r"""Sets the target_project_config_id of this ChangeClusterReq.

        目标项目配置ID

        :param target_project_config_id: The target_project_config_id of this ChangeClusterReq.
        :type target_project_config_id: str
        """
        self._target_project_config_id = target_project_config_id

    @property
    def cloud_storage_assignment_ids(self):
        r"""Gets the cloud_storage_assignment_ids of this ChangeClusterReq.

        文件系统id,数量区间 [1, 50]。

        :return: The cloud_storage_assignment_ids of this ChangeClusterReq.
        :rtype: list[str]
        """
        return self._cloud_storage_assignment_ids

    @cloud_storage_assignment_ids.setter
    def cloud_storage_assignment_ids(self, cloud_storage_assignment_ids):
        r"""Sets the cloud_storage_assignment_ids of this ChangeClusterReq.

        文件系统id,数量区间 [1, 50]。

        :param cloud_storage_assignment_ids: The cloud_storage_assignment_ids of this ChangeClusterReq.
        :type cloud_storage_assignment_ids: list[str]
        """
        self._cloud_storage_assignment_ids = cloud_storage_assignment_ids

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
        if not isinstance(other, ChangeClusterReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
