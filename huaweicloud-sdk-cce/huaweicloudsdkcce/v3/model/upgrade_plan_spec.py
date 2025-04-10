# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradePlanSpec:

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
        'cluster_version': 'str',
        'target_version': 'str',
        'not_before': 'str',
        'not_after': 'str',
        'not_before_deadline': 'str'
    }

    attribute_map = {
        'cluster_id': 'clusterID',
        'cluster_version': 'clusterVersion',
        'target_version': 'targetVersion',
        'not_before': 'notBefore',
        'not_after': 'notAfter',
        'not_before_deadline': 'notBeforeDeadline'
    }

    def __init__(self, cluster_id=None, cluster_version=None, target_version=None, not_before=None, not_after=None, not_before_deadline=None):
        r"""UpgradePlanSpec

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_version: 当前集群版本
        :type cluster_version: str
        :param target_version: 本次集群升级的目标版本
        :type target_version: str
        :param not_before: 自动升级计划的最早时间（UTC时间），需要早于notBeforeDeadline
        :type not_before: str
        :param not_after: 自动升级计划的最晚时间（UTC时间）
        :type not_after: str
        :param not_before_deadline: 自动升级计划开始的截止时间（UTC时间）
        :type not_before_deadline: str
        """
        
        

        self._cluster_id = None
        self._cluster_version = None
        self._target_version = None
        self._not_before = None
        self._not_after = None
        self._not_before_deadline = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.cluster_version = cluster_version
        self.target_version = target_version
        self.not_before = not_before
        self.not_after = not_after
        self.not_before_deadline = not_before_deadline

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpgradePlanSpec.

        集群ID

        :return: The cluster_id of this UpgradePlanSpec.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpgradePlanSpec.

        集群ID

        :param cluster_id: The cluster_id of this UpgradePlanSpec.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_version(self):
        r"""Gets the cluster_version of this UpgradePlanSpec.

        当前集群版本

        :return: The cluster_version of this UpgradePlanSpec.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        r"""Sets the cluster_version of this UpgradePlanSpec.

        当前集群版本

        :param cluster_version: The cluster_version of this UpgradePlanSpec.
        :type cluster_version: str
        """
        self._cluster_version = cluster_version

    @property
    def target_version(self):
        r"""Gets the target_version of this UpgradePlanSpec.

        本次集群升级的目标版本

        :return: The target_version of this UpgradePlanSpec.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this UpgradePlanSpec.

        本次集群升级的目标版本

        :param target_version: The target_version of this UpgradePlanSpec.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def not_before(self):
        r"""Gets the not_before of this UpgradePlanSpec.

        自动升级计划的最早时间（UTC时间），需要早于notBeforeDeadline

        :return: The not_before of this UpgradePlanSpec.
        :rtype: str
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        r"""Sets the not_before of this UpgradePlanSpec.

        自动升级计划的最早时间（UTC时间），需要早于notBeforeDeadline

        :param not_before: The not_before of this UpgradePlanSpec.
        :type not_before: str
        """
        self._not_before = not_before

    @property
    def not_after(self):
        r"""Gets the not_after of this UpgradePlanSpec.

        自动升级计划的最晚时间（UTC时间）

        :return: The not_after of this UpgradePlanSpec.
        :rtype: str
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        r"""Sets the not_after of this UpgradePlanSpec.

        自动升级计划的最晚时间（UTC时间）

        :param not_after: The not_after of this UpgradePlanSpec.
        :type not_after: str
        """
        self._not_after = not_after

    @property
    def not_before_deadline(self):
        r"""Gets the not_before_deadline of this UpgradePlanSpec.

        自动升级计划开始的截止时间（UTC时间）

        :return: The not_before_deadline of this UpgradePlanSpec.
        :rtype: str
        """
        return self._not_before_deadline

    @not_before_deadline.setter
    def not_before_deadline(self, not_before_deadline):
        r"""Sets the not_before_deadline of this UpgradePlanSpec.

        自动升级计划开始的截止时间（UTC时间）

        :param not_before_deadline: The not_before_deadline of this UpgradePlanSpec.
        :type not_before_deadline: str
        """
        self._not_before_deadline = not_before_deadline

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
        if not isinstance(other, UpgradePlanSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
