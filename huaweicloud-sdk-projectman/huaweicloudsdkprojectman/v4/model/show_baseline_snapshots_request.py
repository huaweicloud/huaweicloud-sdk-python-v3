# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBaselineSnapshotsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'snapshot_version_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'snapshot_version_id': 'snapshot_version_id'
    }

    def __init__(self, project_id=None, snapshot_version_id=None):
        r"""ShowBaselineSnapshotsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。
        :type project_id: str
        :param snapshot_version_id: 特性集快照版本ID，不传则查询当前版本特性集，传值则查询对应版本的特性集
        :type snapshot_version_id: str
        """
        
        

        self._project_id = None
        self._snapshot_version_id = None
        self.discriminator = None

        self.project_id = project_id
        if snapshot_version_id is not None:
            self.snapshot_version_id = snapshot_version_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowBaselineSnapshotsRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :return: The project_id of this ShowBaselineSnapshotsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowBaselineSnapshotsRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :param project_id: The project_id of this ShowBaselineSnapshotsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def snapshot_version_id(self):
        r"""Gets the snapshot_version_id of this ShowBaselineSnapshotsRequest.

        特性集快照版本ID，不传则查询当前版本特性集，传值则查询对应版本的特性集

        :return: The snapshot_version_id of this ShowBaselineSnapshotsRequest.
        :rtype: str
        """
        return self._snapshot_version_id

    @snapshot_version_id.setter
    def snapshot_version_id(self, snapshot_version_id):
        r"""Sets the snapshot_version_id of this ShowBaselineSnapshotsRequest.

        特性集快照版本ID，不传则查询当前版本特性集，传值则查询对应版本的特性集

        :param snapshot_version_id: The snapshot_version_id of this ShowBaselineSnapshotsRequest.
        :type snapshot_version_id: str
        """
        self._snapshot_version_id = snapshot_version_id

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
        if not isinstance(other, ShowBaselineSnapshotsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
