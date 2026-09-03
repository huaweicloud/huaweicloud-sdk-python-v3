# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKernelUpgradeCheckResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upgrade_precheck_result': 'str',
        'updated_at': 'int',
        'upgrade_precheck_detail': 'list[UpgradeDatabasePrecheckResult]'
    }

    attribute_map = {
        'upgrade_precheck_result': 'upgrade_precheck_result',
        'updated_at': 'updated_at',
        'upgrade_precheck_detail': 'upgrade_precheck_detail'
    }

    def __init__(self, upgrade_precheck_result=None, updated_at=None, upgrade_precheck_detail=None):
        r"""ShowKernelUpgradeCheckResultResponse

        The model defined in huaweicloud sdk

        :param upgrade_precheck_result: **参数解释**：  预检查结果。  **取值范围**：  - true：成功。 - false：失败。
        :type upgrade_precheck_result: str
        :param updated_at: **参数解释**：  预检查完成时间。  **取值范围**：  格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区。
        :type updated_at: int
        :param upgrade_precheck_detail: **参数解释**：  实例预检查详情。
        :type upgrade_precheck_detail: list[:class:`huaweicloudsdkgaussdb.v3.UpgradeDatabasePrecheckResult`]
        """
        
        super().__init__()

        self._upgrade_precheck_result = None
        self._updated_at = None
        self._upgrade_precheck_detail = None
        self.discriminator = None

        if upgrade_precheck_result is not None:
            self.upgrade_precheck_result = upgrade_precheck_result
        if updated_at is not None:
            self.updated_at = updated_at
        if upgrade_precheck_detail is not None:
            self.upgrade_precheck_detail = upgrade_precheck_detail

    @property
    def upgrade_precheck_result(self):
        r"""Gets the upgrade_precheck_result of this ShowKernelUpgradeCheckResultResponse.

        **参数解释**：  预检查结果。  **取值范围**：  - true：成功。 - false：失败。

        :return: The upgrade_precheck_result of this ShowKernelUpgradeCheckResultResponse.
        :rtype: str
        """
        return self._upgrade_precheck_result

    @upgrade_precheck_result.setter
    def upgrade_precheck_result(self, upgrade_precheck_result):
        r"""Sets the upgrade_precheck_result of this ShowKernelUpgradeCheckResultResponse.

        **参数解释**：  预检查结果。  **取值范围**：  - true：成功。 - false：失败。

        :param upgrade_precheck_result: The upgrade_precheck_result of this ShowKernelUpgradeCheckResultResponse.
        :type upgrade_precheck_result: str
        """
        self._upgrade_precheck_result = upgrade_precheck_result

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowKernelUpgradeCheckResultResponse.

        **参数解释**：  预检查完成时间。  **取值范围**：  格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区。

        :return: The updated_at of this ShowKernelUpgradeCheckResultResponse.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowKernelUpgradeCheckResultResponse.

        **参数解释**：  预检查完成时间。  **取值范围**：  格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区。

        :param updated_at: The updated_at of this ShowKernelUpgradeCheckResultResponse.
        :type updated_at: int
        """
        self._updated_at = updated_at

    @property
    def upgrade_precheck_detail(self):
        r"""Gets the upgrade_precheck_detail of this ShowKernelUpgradeCheckResultResponse.

        **参数解释**：  实例预检查详情。

        :return: The upgrade_precheck_detail of this ShowKernelUpgradeCheckResultResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.UpgradeDatabasePrecheckResult`]
        """
        return self._upgrade_precheck_detail

    @upgrade_precheck_detail.setter
    def upgrade_precheck_detail(self, upgrade_precheck_detail):
        r"""Sets the upgrade_precheck_detail of this ShowKernelUpgradeCheckResultResponse.

        **参数解释**：  实例预检查详情。

        :param upgrade_precheck_detail: The upgrade_precheck_detail of this ShowKernelUpgradeCheckResultResponse.
        :type upgrade_precheck_detail: list[:class:`huaweicloudsdkgaussdb.v3.UpgradeDatabasePrecheckResult`]
        """
        self._upgrade_precheck_detail = upgrade_precheck_detail

    def to_dict(self):
        import warnings
        warnings.warn("ShowKernelUpgradeCheckResultResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowKernelUpgradeCheckResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
