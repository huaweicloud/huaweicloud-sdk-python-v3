# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradingTheKernelBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_image_id': 'str',
        'upgrade_type': 'str',
        'indices_backup_check': 'bool',
        'agency': 'str',
        'cluster_load_check': 'bool',
        'batch_size': 'int'
    }

    attribute_map = {
        'target_image_id': 'target_image_id',
        'upgrade_type': 'upgrade_type',
        'indices_backup_check': 'indices_backup_check',
        'agency': 'agency',
        'cluster_load_check': 'cluster_load_check',
        'batch_size': 'batch_size'
    }

    def __init__(self, target_image_id=None, upgrade_type=None, indices_backup_check=None, agency=None, cluster_load_check=None, batch_size=None):
        r"""UpgradingTheKernelBody

        The model defined in huaweicloud sdk

        :param target_image_id: 目标镜像版本ID。
        :type target_image_id: str
        :param upgrade_type: 升级类型。 - same：同版本。 - cross：跨版本。
        :type upgrade_type: str
        :param indices_backup_check: 是否进行备份校验。 - true：进行校验。 - false：不进行校验。
        :type indices_backup_check: bool
        :param agency: 委托名称，委托给CSS，允许CSS调用您的其他云服务。
        :type agency: str
        :param cluster_load_check: 是否校验负载。默认为true。 - true：进行校验。 - false：不进行校验。
        :type cluster_load_check: bool
        :param batch_size: 数据节点迁移数据并发度。
        :type batch_size: int
        """
        
        

        self._target_image_id = None
        self._upgrade_type = None
        self._indices_backup_check = None
        self._agency = None
        self._cluster_load_check = None
        self._batch_size = None
        self.discriminator = None

        self.target_image_id = target_image_id
        self.upgrade_type = upgrade_type
        self.indices_backup_check = indices_backup_check
        self.agency = agency
        if cluster_load_check is not None:
            self.cluster_load_check = cluster_load_check
        if batch_size is not None:
            self.batch_size = batch_size

    @property
    def target_image_id(self):
        r"""Gets the target_image_id of this UpgradingTheKernelBody.

        目标镜像版本ID。

        :return: The target_image_id of this UpgradingTheKernelBody.
        :rtype: str
        """
        return self._target_image_id

    @target_image_id.setter
    def target_image_id(self, target_image_id):
        r"""Sets the target_image_id of this UpgradingTheKernelBody.

        目标镜像版本ID。

        :param target_image_id: The target_image_id of this UpgradingTheKernelBody.
        :type target_image_id: str
        """
        self._target_image_id = target_image_id

    @property
    def upgrade_type(self):
        r"""Gets the upgrade_type of this UpgradingTheKernelBody.

        升级类型。 - same：同版本。 - cross：跨版本。

        :return: The upgrade_type of this UpgradingTheKernelBody.
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        r"""Sets the upgrade_type of this UpgradingTheKernelBody.

        升级类型。 - same：同版本。 - cross：跨版本。

        :param upgrade_type: The upgrade_type of this UpgradingTheKernelBody.
        :type upgrade_type: str
        """
        self._upgrade_type = upgrade_type

    @property
    def indices_backup_check(self):
        r"""Gets the indices_backup_check of this UpgradingTheKernelBody.

        是否进行备份校验。 - true：进行校验。 - false：不进行校验。

        :return: The indices_backup_check of this UpgradingTheKernelBody.
        :rtype: bool
        """
        return self._indices_backup_check

    @indices_backup_check.setter
    def indices_backup_check(self, indices_backup_check):
        r"""Sets the indices_backup_check of this UpgradingTheKernelBody.

        是否进行备份校验。 - true：进行校验。 - false：不进行校验。

        :param indices_backup_check: The indices_backup_check of this UpgradingTheKernelBody.
        :type indices_backup_check: bool
        """
        self._indices_backup_check = indices_backup_check

    @property
    def agency(self):
        r"""Gets the agency of this UpgradingTheKernelBody.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :return: The agency of this UpgradingTheKernelBody.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this UpgradingTheKernelBody.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :param agency: The agency of this UpgradingTheKernelBody.
        :type agency: str
        """
        self._agency = agency

    @property
    def cluster_load_check(self):
        r"""Gets the cluster_load_check of this UpgradingTheKernelBody.

        是否校验负载。默认为true。 - true：进行校验。 - false：不进行校验。

        :return: The cluster_load_check of this UpgradingTheKernelBody.
        :rtype: bool
        """
        return self._cluster_load_check

    @cluster_load_check.setter
    def cluster_load_check(self, cluster_load_check):
        r"""Sets the cluster_load_check of this UpgradingTheKernelBody.

        是否校验负载。默认为true。 - true：进行校验。 - false：不进行校验。

        :param cluster_load_check: The cluster_load_check of this UpgradingTheKernelBody.
        :type cluster_load_check: bool
        """
        self._cluster_load_check = cluster_load_check

    @property
    def batch_size(self):
        r"""Gets the batch_size of this UpgradingTheKernelBody.

        数据节点迁移数据并发度。

        :return: The batch_size of this UpgradingTheKernelBody.
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        r"""Sets the batch_size of this UpgradingTheKernelBody.

        数据节点迁移数据并发度。

        :param batch_size: The batch_size of this UpgradingTheKernelBody.
        :type batch_size: int
        """
        self._batch_size = batch_size

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
        if not isinstance(other, UpgradingTheKernelBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
