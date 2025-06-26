# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDwsClusterRequest:

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
        'keep_last_manual_backup': 'str',
        'release_eip_type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'keep_last_manual_backup': 'keep_last_manual_backup',
        'release_eip_type': 'release_eip_type'
    }

    def __init__(self, cluster_id=None, keep_last_manual_backup=None, release_eip_type=None):
        r"""DeleteDwsClusterRequest

        The model defined in huaweicloud sdk

        :param cluster_id: **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。
        :type cluster_id: str
        :param keep_last_manual_backup: **参数解释**： 集群需要保留的快照数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0
        :type keep_last_manual_backup: str
        :param release_eip_type: **参数解释**： 集群是否释放弹性公网IP，默认是NO_RELEASE，不释放绑定的弹性公网IP。 **约束限制**： 不涉及。 **取值范围**： NO_RELEASE：不释放绑定的弹性公网IP； RELEASE_BINDING：释放绑定的弹性公网IP； **默认取值**： NO_RELEASE
        :type release_eip_type: str
        """
        
        

        self._cluster_id = None
        self._keep_last_manual_backup = None
        self._release_eip_type = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if keep_last_manual_backup is not None:
            self.keep_last_manual_backup = keep_last_manual_backup
        if release_eip_type is not None:
            self.release_eip_type = release_eip_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this DeleteDwsClusterRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :return: The cluster_id of this DeleteDwsClusterRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this DeleteDwsClusterRequest.

        **参数解释**： 集群ID。获取方法请参见[获取集群ID](dws_02_00068.xml)。 **约束限制**： 必须是有效的dws集群ID。 **取值范围**： 36位UUID。 **默认取值**： 不涉及。

        :param cluster_id: The cluster_id of this DeleteDwsClusterRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def keep_last_manual_backup(self):
        r"""Gets the keep_last_manual_backup of this DeleteDwsClusterRequest.

        **参数解释**： 集群需要保留的快照数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0

        :return: The keep_last_manual_backup of this DeleteDwsClusterRequest.
        :rtype: str
        """
        return self._keep_last_manual_backup

    @keep_last_manual_backup.setter
    def keep_last_manual_backup(self, keep_last_manual_backup):
        r"""Sets the keep_last_manual_backup of this DeleteDwsClusterRequest.

        **参数解释**： 集群需要保留的快照数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 0

        :param keep_last_manual_backup: The keep_last_manual_backup of this DeleteDwsClusterRequest.
        :type keep_last_manual_backup: str
        """
        self._keep_last_manual_backup = keep_last_manual_backup

    @property
    def release_eip_type(self):
        r"""Gets the release_eip_type of this DeleteDwsClusterRequest.

        **参数解释**： 集群是否释放弹性公网IP，默认是NO_RELEASE，不释放绑定的弹性公网IP。 **约束限制**： 不涉及。 **取值范围**： NO_RELEASE：不释放绑定的弹性公网IP； RELEASE_BINDING：释放绑定的弹性公网IP； **默认取值**： NO_RELEASE

        :return: The release_eip_type of this DeleteDwsClusterRequest.
        :rtype: str
        """
        return self._release_eip_type

    @release_eip_type.setter
    def release_eip_type(self, release_eip_type):
        r"""Sets the release_eip_type of this DeleteDwsClusterRequest.

        **参数解释**： 集群是否释放弹性公网IP，默认是NO_RELEASE，不释放绑定的弹性公网IP。 **约束限制**： 不涉及。 **取值范围**： NO_RELEASE：不释放绑定的弹性公网IP； RELEASE_BINDING：释放绑定的弹性公网IP； **默认取值**： NO_RELEASE

        :param release_eip_type: The release_eip_type of this DeleteDwsClusterRequest.
        :type release_eip_type: str
        """
        self._release_eip_type = release_eip_type

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
        if not isinstance(other, DeleteDwsClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
