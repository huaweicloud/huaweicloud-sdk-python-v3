# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShrinkLogicalClusterRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_rings': 'list[ClusterRing]',
        'parallel_jobs': 'int',
        'mode': 'str'
    }

    attribute_map = {
        'cluster_rings': 'cluster_rings',
        'parallel_jobs': 'parallel_jobs',
        'mode': 'mode'
    }

    def __init__(self, cluster_rings=None, parallel_jobs=None, mode=None):
        r"""ShrinkLogicalClusterRequestBody

        The model defined in huaweicloud sdk

        :param cluster_rings: **参数解释**： 缩容主机环信息。  **约束限制**：  不涉及。 **取值范围**：  不涉及。 **默认取值**：  不涉及。
        :type cluster_rings: list[:class:`huaweicloudsdkdws.v2.ClusterRing`]
        :param parallel_jobs: **参数解释**： 重分布并发配置数。  **约束限制**：  不涉及。 **取值范围**：  1~200。 **默认取值**：  4。
        :type parallel_jobs: int
        :param mode: **参数解释**：  缩容模式。 **约束限制**：  不涉及。 **取值范围**：  read-only：离线模式 insert：在线模式 **默认取值**：  insert
        :type mode: str
        """
        
        

        self._cluster_rings = None
        self._parallel_jobs = None
        self._mode = None
        self.discriminator = None

        self.cluster_rings = cluster_rings
        if parallel_jobs is not None:
            self.parallel_jobs = parallel_jobs
        if mode is not None:
            self.mode = mode

    @property
    def cluster_rings(self):
        r"""Gets the cluster_rings of this ShrinkLogicalClusterRequestBody.

        **参数解释**： 缩容主机环信息。  **约束限制**：  不涉及。 **取值范围**：  不涉及。 **默认取值**：  不涉及。

        :return: The cluster_rings of this ShrinkLogicalClusterRequestBody.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ClusterRing`]
        """
        return self._cluster_rings

    @cluster_rings.setter
    def cluster_rings(self, cluster_rings):
        r"""Sets the cluster_rings of this ShrinkLogicalClusterRequestBody.

        **参数解释**： 缩容主机环信息。  **约束限制**：  不涉及。 **取值范围**：  不涉及。 **默认取值**：  不涉及。

        :param cluster_rings: The cluster_rings of this ShrinkLogicalClusterRequestBody.
        :type cluster_rings: list[:class:`huaweicloudsdkdws.v2.ClusterRing`]
        """
        self._cluster_rings = cluster_rings

    @property
    def parallel_jobs(self):
        r"""Gets the parallel_jobs of this ShrinkLogicalClusterRequestBody.

        **参数解释**： 重分布并发配置数。  **约束限制**：  不涉及。 **取值范围**：  1~200。 **默认取值**：  4。

        :return: The parallel_jobs of this ShrinkLogicalClusterRequestBody.
        :rtype: int
        """
        return self._parallel_jobs

    @parallel_jobs.setter
    def parallel_jobs(self, parallel_jobs):
        r"""Sets the parallel_jobs of this ShrinkLogicalClusterRequestBody.

        **参数解释**： 重分布并发配置数。  **约束限制**：  不涉及。 **取值范围**：  1~200。 **默认取值**：  4。

        :param parallel_jobs: The parallel_jobs of this ShrinkLogicalClusterRequestBody.
        :type parallel_jobs: int
        """
        self._parallel_jobs = parallel_jobs

    @property
    def mode(self):
        r"""Gets the mode of this ShrinkLogicalClusterRequestBody.

        **参数解释**：  缩容模式。 **约束限制**：  不涉及。 **取值范围**：  read-only：离线模式 insert：在线模式 **默认取值**：  insert

        :return: The mode of this ShrinkLogicalClusterRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ShrinkLogicalClusterRequestBody.

        **参数解释**：  缩容模式。 **约束限制**：  不涉及。 **取值范围**：  read-only：离线模式 insert：在线模式 **默认取值**：  insert

        :param mode: The mode of this ShrinkLogicalClusterRequestBody.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, ShrinkLogicalClusterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
