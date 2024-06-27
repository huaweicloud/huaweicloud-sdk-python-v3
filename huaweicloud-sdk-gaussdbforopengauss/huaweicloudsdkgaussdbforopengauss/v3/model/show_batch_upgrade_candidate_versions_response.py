# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBatchUpgradeCandidateVersionsResponse(SdkResponse):

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
        'target_version': 'str',
        'upgrade_candidate_versions': 'list[str]',
        'hotfix_upgrade_infos': 'list[HotfixInfo]'
    }

    attribute_map = {
        'upgrade_type_list': 'upgrade_type_list',
        'target_version': 'target_version',
        'upgrade_candidate_versions': 'upgrade_candidate_versions',
        'hotfix_upgrade_infos': 'hotfix_upgrade_infos'
    }

    def __init__(self, upgrade_type_list=None, target_version=None, upgrade_candidate_versions=None, hotfix_upgrade_infos=None):
        """ShowBatchUpgradeCandidateVersionsResponse

        The model defined in huaweicloud sdk

        :param upgrade_type_list: 升级类型信息列表
        :type upgrade_type_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeTypeInfo`]
        :param target_version: 升级目标版本，没有在滚动升级中返回null
        :type target_version: str
        :param upgrade_candidate_versions: 可以升级的版本，包括大小版本
        :type upgrade_candidate_versions: list[str]
        :param hotfix_upgrade_infos: 可以升级的热补丁信息
        :type hotfix_upgrade_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HotfixInfo`]
        """
        
        super(ShowBatchUpgradeCandidateVersionsResponse, self).__init__()

        self._upgrade_type_list = None
        self._target_version = None
        self._upgrade_candidate_versions = None
        self._hotfix_upgrade_infos = None
        self.discriminator = None

        if upgrade_type_list is not None:
            self.upgrade_type_list = upgrade_type_list
        if target_version is not None:
            self.target_version = target_version
        if upgrade_candidate_versions is not None:
            self.upgrade_candidate_versions = upgrade_candidate_versions
        if hotfix_upgrade_infos is not None:
            self.hotfix_upgrade_infos = hotfix_upgrade_infos

    @property
    def upgrade_type_list(self):
        """Gets the upgrade_type_list of this ShowBatchUpgradeCandidateVersionsResponse.

        升级类型信息列表

        :return: The upgrade_type_list of this ShowBatchUpgradeCandidateVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeTypeInfo`]
        """
        return self._upgrade_type_list

    @upgrade_type_list.setter
    def upgrade_type_list(self, upgrade_type_list):
        """Sets the upgrade_type_list of this ShowBatchUpgradeCandidateVersionsResponse.

        升级类型信息列表

        :param upgrade_type_list: The upgrade_type_list of this ShowBatchUpgradeCandidateVersionsResponse.
        :type upgrade_type_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.UpgradeTypeInfo`]
        """
        self._upgrade_type_list = upgrade_type_list

    @property
    def target_version(self):
        """Gets the target_version of this ShowBatchUpgradeCandidateVersionsResponse.

        升级目标版本，没有在滚动升级中返回null

        :return: The target_version of this ShowBatchUpgradeCandidateVersionsResponse.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        """Sets the target_version of this ShowBatchUpgradeCandidateVersionsResponse.

        升级目标版本，没有在滚动升级中返回null

        :param target_version: The target_version of this ShowBatchUpgradeCandidateVersionsResponse.
        :type target_version: str
        """
        self._target_version = target_version

    @property
    def upgrade_candidate_versions(self):
        """Gets the upgrade_candidate_versions of this ShowBatchUpgradeCandidateVersionsResponse.

        可以升级的版本，包括大小版本

        :return: The upgrade_candidate_versions of this ShowBatchUpgradeCandidateVersionsResponse.
        :rtype: list[str]
        """
        return self._upgrade_candidate_versions

    @upgrade_candidate_versions.setter
    def upgrade_candidate_versions(self, upgrade_candidate_versions):
        """Sets the upgrade_candidate_versions of this ShowBatchUpgradeCandidateVersionsResponse.

        可以升级的版本，包括大小版本

        :param upgrade_candidate_versions: The upgrade_candidate_versions of this ShowBatchUpgradeCandidateVersionsResponse.
        :type upgrade_candidate_versions: list[str]
        """
        self._upgrade_candidate_versions = upgrade_candidate_versions

    @property
    def hotfix_upgrade_infos(self):
        """Gets the hotfix_upgrade_infos of this ShowBatchUpgradeCandidateVersionsResponse.

        可以升级的热补丁信息

        :return: The hotfix_upgrade_infos of this ShowBatchUpgradeCandidateVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HotfixInfo`]
        """
        return self._hotfix_upgrade_infos

    @hotfix_upgrade_infos.setter
    def hotfix_upgrade_infos(self, hotfix_upgrade_infos):
        """Sets the hotfix_upgrade_infos of this ShowBatchUpgradeCandidateVersionsResponse.

        可以升级的热补丁信息

        :param hotfix_upgrade_infos: The hotfix_upgrade_infos of this ShowBatchUpgradeCandidateVersionsResponse.
        :type hotfix_upgrade_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HotfixInfo`]
        """
        self._hotfix_upgrade_infos = hotfix_upgrade_infos

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
        if not isinstance(other, ShowBatchUpgradeCandidateVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
