# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUpgradeCandidateVersionsDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upgrade_type_list': 'list[UpgradeTypeInfo]',
        'rollback_enabled': 'bool',
        'source_version': 'str',
        'target_version': 'str',
        'roll_upgrade_progress': 'RollUpgradeProgress',
        'upgrade_candidate_versions': 'list[str]',
        'hotfix_upgrade_candidate_versions': 'list[str]',
        'hotfix_rollback_candidate_versions': 'list[str]',
        'hotfix_upgrade_infos': 'list[CanBeUpgradedHotfixDetail]',
        'hotfix_rollback_infos': 'list[CanBeRollbackedHotfixDetail]'
    }

    attribute_map = {
        'upgrade_type_list': 'upgrade_type_list',
        'rollback_enabled': 'rollback_enabled',
        'source_version': 'source_version',
        'target_version': 'target_version',
        'roll_upgrade_progress': 'roll_upgrade_progress',
        'upgrade_candidate_versions': 'upgrade_candidate_versions',
        'hotfix_upgrade_candidate_versions': 'hotfix_upgrade_candidate_versions',
        'hotfix_rollback_candidate_versions': 'hotfix_rollback_candidate_versions',
        'hotfix_upgrade_infos': 'hotfix_upgrade_infos',
        'hotfix_rollback_infos': 'hotfix_rollback_infos'
    }

    def __init__(self, upgrade_type_list=None, rollback_enabled=None, source_version=None, target_version=None, roll_upgrade_progress=None, upgrade_candidate_versions=None, hotfix_upgrade_candidate_versions=None, hotfix_rollback_candidate_versions=None, hotfix_upgrade_infos=None, hotfix_rollback_infos=None):
        r"""ShowUpgradeCandidateVersionsDetailsResponse

        The model defined in huaweicloud sdk

        :param upgrade_type_list: 升级类型信息列表
        :type upgrade_type_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeTypeInfo`]
        :param rollback_enabled: 是否可以回滚，true可以回滚，false不可以回滚。
        :type rollback_enabled: bool
        :param source_version: 原版本
        :type source_version: str
        :param target_version: 升级目标版本，没有在滚动升级中返回null。
        :type target_version: str
        :param roll_upgrade_progress: 
        :type roll_upgrade_progress: :class:`huaweicloudsdkgaussdbforopengauss.v3.RollUpgradeProgress`
        :param upgrade_candidate_versions: 可以升级的版本，包括大小版本，滚动升级中返回空数组。
        :type upgrade_candidate_versions: list[str]
        :param hotfix_upgrade_candidate_versions: 可以升级的热补丁版本，滚动升级中返回空数组。
        :type hotfix_upgrade_candidate_versions: list[str]
        :param hotfix_rollback_candidate_versions: 可以回滚的热补丁版本，滚动升级中返回空数组。
        :type hotfix_rollback_candidate_versions: list[str]
        :param hotfix_upgrade_infos: 可以升级的热补丁信息。
        :type hotfix_upgrade_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CanBeUpgradedHotfixDetail`]
        :param hotfix_rollback_infos: 可以回滚的热补丁信息。
        :type hotfix_rollback_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CanBeRollbackedHotfixDetail`]
        """
        
        super(ShowUpgradeCandidateVersionsDetailsResponse, self).__init__()

        self._upgrade_type_list = None
        self._rollback_enabled = None
        self._source_version = None
        self._target_version = None
        self._roll_upgrade_progress = None
        self._upgrade_candidate_versions = None
        self._hotfix_upgrade_candidate_versions = None
        self._hotfix_rollback_candidate_versions = None
        self._hotfix_upgrade_infos = None
        self._hotfix_rollback_infos = None
        self.discriminator = None

        if upgrade_type_list is not None:
            self.upgrade_type_list = upgrade_type_list
        if rollback_enabled is not None:
            self.rollback_enabled = rollback_enabled
        if source_version is not None:
            self.source_version = source_version
        if target_version is not None:
            self.target_version = target_version
        if roll_upgrade_progress is not None:
            self.roll_upgrade_progress = roll_upgrade_progress
        if upgrade_candidate_versions is not None:
            self.upgrade_candidate_versions = upgrade_candidate_versions
        if hotfix_upgrade_candidate_versions is not None:
            self.hotfix_upgrade_candidate_versions = hotfix_upgrade_candidate_versions
        if hotfix_rollback_candidate_versions is not None:
            self.hotfix_rollback_candidate_versions = hotfix_rollback_candidate_versions
        if hotfix_upgrade_infos is not None:
            self.hotfix_upgrade_infos = hotfix_upgrade_infos
        if hotfix_rollback_infos is not None:
            self.hotfix_rollback_infos = hotfix_rollback_infos

    @property
    def upgrade_type_list(self):
        r"""Gets the upgrade_type_list of this ShowUpgradeCandidateVersionsDetailsResponse.

        升级类型信息列表

        :return: The upgrade_type_list of this ShowUpgradeCandidateVersionsDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeTypeInfo`]
        """
        return self._upgrade_type_list

    @upgrade_type_list.setter
    def upgrade_type_list(self, upgrade_type_list):
        r"""Sets the upgrade_type_list of this ShowUpgradeCandidateVersionsDetailsResponse.

        升级类型信息列表

        :param upgrade_type_list: The upgrade_type_list of this ShowUpgradeCandidateVersionsDetailsResponse.
        :type upgrade_type_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeTypeInfo`]
        """
        self._upgrade_type_list = upgrade_type_list

    @property
    def rollback_enabled(self):
        r"""Gets the rollback_enabled of this ShowUpgradeCandidateVersionsDetailsResponse.

        是否可以回滚，true可以回滚，false不可以回滚。

        :return: The rollback_enabled of this ShowUpgradeCandidateVersionsDetailsResponse.
        :rtype: bool
        """
        return self._rollback_enabled

    @rollback_enabled.setter
    def rollback_enabled(self, rollback_enabled):
        r"""Sets the rollback_enabled of this ShowUpgradeCandidateVersionsDetailsResponse.

        是否可以回滚，true可以回滚，false不可以回滚。

        :param rollback_enabled: The rollback_enabled of this ShowUpgradeCandidateVersionsDetailsResponse.
        :type rollback_enabled: bool
        """
        self._rollback_enabled = rollback_enabled

    @property
    def source_version(self):
        r"""Gets the source_version of this ShowUpgradeCandidateVersionsDetailsResponse.

        原版本

        :return: The source_version of this ShowUpgradeCandidateVersionsDetailsResponse.
        :rtype: str
        """
        return self._source_version

    @source_version.setter
    def source_version(self, source_version):
        r"""Sets the source_version of this ShowUpgradeCandidateVersionsDetailsResponse.

        原版本

        :param source_version: The source_version of this ShowUpgradeCandidateVersionsDetailsResponse.
        :type source_version: str
        """
        self._source_version = source_version

    @property
    def target_version(self):
        r"""Gets the target_version of this ShowUpgradeCandidateVersionsDetailsResponse.

        升级目标版本，没有在滚动升级中返回null。

        :return: The target_version of this ShowUpgradeCandidateVersionsDetailsResponse.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this ShowUpgradeCandidateVersionsDetailsResponse.

        升级目标版本，没有在滚动升级中返回null。

        :param target_version: The target_version of this ShowUpgradeCandidateVersionsDetailsResponse.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def roll_upgrade_progress(self):
        r"""Gets the roll_upgrade_progress of this ShowUpgradeCandidateVersionsDetailsResponse.

        :return: The roll_upgrade_progress of this ShowUpgradeCandidateVersionsDetailsResponse.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.RollUpgradeProgress`
        """
        return self._roll_upgrade_progress

    @roll_upgrade_progress.setter
    def roll_upgrade_progress(self, roll_upgrade_progress):
        r"""Sets the roll_upgrade_progress of this ShowUpgradeCandidateVersionsDetailsResponse.

        :param roll_upgrade_progress: The roll_upgrade_progress of this ShowUpgradeCandidateVersionsDetailsResponse.
        :type roll_upgrade_progress: :class:`huaweicloudsdkgaussdbforopengauss.v3.RollUpgradeProgress`
        """
        self._roll_upgrade_progress = roll_upgrade_progress

    @property
    def upgrade_candidate_versions(self):
        r"""Gets the upgrade_candidate_versions of this ShowUpgradeCandidateVersionsDetailsResponse.

        可以升级的版本，包括大小版本，滚动升级中返回空数组。

        :return: The upgrade_candidate_versions of this ShowUpgradeCandidateVersionsDetailsResponse.
        :rtype: list[str]
        """
        return self._upgrade_candidate_versions

    @upgrade_candidate_versions.setter
    def upgrade_candidate_versions(self, upgrade_candidate_versions):
        r"""Sets the upgrade_candidate_versions of this ShowUpgradeCandidateVersionsDetailsResponse.

        可以升级的版本，包括大小版本，滚动升级中返回空数组。

        :param upgrade_candidate_versions: The upgrade_candidate_versions of this ShowUpgradeCandidateVersionsDetailsResponse.
        :type upgrade_candidate_versions: list[str]
        """
        self._upgrade_candidate_versions = upgrade_candidate_versions

    @property
    def hotfix_upgrade_candidate_versions(self):
        r"""Gets the hotfix_upgrade_candidate_versions of this ShowUpgradeCandidateVersionsDetailsResponse.

        可以升级的热补丁版本，滚动升级中返回空数组。

        :return: The hotfix_upgrade_candidate_versions of this ShowUpgradeCandidateVersionsDetailsResponse.
        :rtype: list[str]
        """
        return self._hotfix_upgrade_candidate_versions

    @hotfix_upgrade_candidate_versions.setter
    def hotfix_upgrade_candidate_versions(self, hotfix_upgrade_candidate_versions):
        r"""Sets the hotfix_upgrade_candidate_versions of this ShowUpgradeCandidateVersionsDetailsResponse.

        可以升级的热补丁版本，滚动升级中返回空数组。

        :param hotfix_upgrade_candidate_versions: The hotfix_upgrade_candidate_versions of this ShowUpgradeCandidateVersionsDetailsResponse.
        :type hotfix_upgrade_candidate_versions: list[str]
        """
        self._hotfix_upgrade_candidate_versions = hotfix_upgrade_candidate_versions

    @property
    def hotfix_rollback_candidate_versions(self):
        r"""Gets the hotfix_rollback_candidate_versions of this ShowUpgradeCandidateVersionsDetailsResponse.

        可以回滚的热补丁版本，滚动升级中返回空数组。

        :return: The hotfix_rollback_candidate_versions of this ShowUpgradeCandidateVersionsDetailsResponse.
        :rtype: list[str]
        """
        return self._hotfix_rollback_candidate_versions

    @hotfix_rollback_candidate_versions.setter
    def hotfix_rollback_candidate_versions(self, hotfix_rollback_candidate_versions):
        r"""Sets the hotfix_rollback_candidate_versions of this ShowUpgradeCandidateVersionsDetailsResponse.

        可以回滚的热补丁版本，滚动升级中返回空数组。

        :param hotfix_rollback_candidate_versions: The hotfix_rollback_candidate_versions of this ShowUpgradeCandidateVersionsDetailsResponse.
        :type hotfix_rollback_candidate_versions: list[str]
        """
        self._hotfix_rollback_candidate_versions = hotfix_rollback_candidate_versions

    @property
    def hotfix_upgrade_infos(self):
        r"""Gets the hotfix_upgrade_infos of this ShowUpgradeCandidateVersionsDetailsResponse.

        可以升级的热补丁信息。

        :return: The hotfix_upgrade_infos of this ShowUpgradeCandidateVersionsDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CanBeUpgradedHotfixDetail`]
        """
        return self._hotfix_upgrade_infos

    @hotfix_upgrade_infos.setter
    def hotfix_upgrade_infos(self, hotfix_upgrade_infos):
        r"""Sets the hotfix_upgrade_infos of this ShowUpgradeCandidateVersionsDetailsResponse.

        可以升级的热补丁信息。

        :param hotfix_upgrade_infos: The hotfix_upgrade_infos of this ShowUpgradeCandidateVersionsDetailsResponse.
        :type hotfix_upgrade_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CanBeUpgradedHotfixDetail`]
        """
        self._hotfix_upgrade_infos = hotfix_upgrade_infos

    @property
    def hotfix_rollback_infos(self):
        r"""Gets the hotfix_rollback_infos of this ShowUpgradeCandidateVersionsDetailsResponse.

        可以回滚的热补丁信息。

        :return: The hotfix_rollback_infos of this ShowUpgradeCandidateVersionsDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CanBeRollbackedHotfixDetail`]
        """
        return self._hotfix_rollback_infos

    @hotfix_rollback_infos.setter
    def hotfix_rollback_infos(self, hotfix_rollback_infos):
        r"""Sets the hotfix_rollback_infos of this ShowUpgradeCandidateVersionsDetailsResponse.

        可以回滚的热补丁信息。

        :param hotfix_rollback_infos: The hotfix_rollback_infos of this ShowUpgradeCandidateVersionsDetailsResponse.
        :type hotfix_rollback_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CanBeRollbackedHotfixDetail`]
        """
        self._hotfix_rollback_infos = hotfix_rollback_infos

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
        if not isinstance(other, ShowUpgradeCandidateVersionsDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
