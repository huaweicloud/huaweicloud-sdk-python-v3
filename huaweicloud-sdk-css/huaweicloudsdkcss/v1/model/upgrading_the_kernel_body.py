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
        'check_load': 'bool'
    }

    attribute_map = {
        'target_image_id': 'target_image_id',
        'upgrade_type': 'upgrade_type',
        'indices_backup_check': 'indices_backup_check',
        'agency': 'agency',
        'check_load': 'check_load'
    }

    def __init__(self, target_image_id=None, upgrade_type=None, indices_backup_check=None, agency=None, check_load=None):
        """UpgradingTheKernelBody

        The model defined in huaweicloud sdk

        :param target_image_id: 目标镜像版本ID。
        :type target_image_id: str
        :param upgrade_type: 升级类型。 - same：同版本。 - cross：跨版本。
        :type upgrade_type: str
        :param indices_backup_check: 是否进行备份校验。 - true：进行校验。 - false：不进行校验。
        :type indices_backup_check: bool
        :param agency: 委托名称，委托给CSS，允许CSS调用您的其他云服务。
        :type agency: str
        :param check_load: 是否校验负载。默认为true。 - true：进行校验。 - false：不进行校验。
        :type check_load: bool
        """
        
        

        self._target_image_id = None
        self._upgrade_type = None
        self._indices_backup_check = None
        self._agency = None
        self._check_load = None
        self.discriminator = None

        self.target_image_id = target_image_id
        self.upgrade_type = upgrade_type
        self.indices_backup_check = indices_backup_check
        self.agency = agency
        if check_load is not None:
            self.check_load = check_load

    @property
    def target_image_id(self):
        """Gets the target_image_id of this UpgradingTheKernelBody.

        目标镜像版本ID。

        :return: The target_image_id of this UpgradingTheKernelBody.
        :rtype: str
        """
        return self._target_image_id

    @target_image_id.setter
    def target_image_id(self, target_image_id):
        """Sets the target_image_id of this UpgradingTheKernelBody.

        目标镜像版本ID。

        :param target_image_id: The target_image_id of this UpgradingTheKernelBody.
        :type target_image_id: str
        """
        self._target_image_id = target_image_id

    @property
    def upgrade_type(self):
        """Gets the upgrade_type of this UpgradingTheKernelBody.

        升级类型。 - same：同版本。 - cross：跨版本。

        :return: The upgrade_type of this UpgradingTheKernelBody.
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """Sets the upgrade_type of this UpgradingTheKernelBody.

        升级类型。 - same：同版本。 - cross：跨版本。

        :param upgrade_type: The upgrade_type of this UpgradingTheKernelBody.
        :type upgrade_type: str
        """
        self._upgrade_type = upgrade_type

    @property
    def indices_backup_check(self):
        """Gets the indices_backup_check of this UpgradingTheKernelBody.

        是否进行备份校验。 - true：进行校验。 - false：不进行校验。

        :return: The indices_backup_check of this UpgradingTheKernelBody.
        :rtype: bool
        """
        return self._indices_backup_check

    @indices_backup_check.setter
    def indices_backup_check(self, indices_backup_check):
        """Sets the indices_backup_check of this UpgradingTheKernelBody.

        是否进行备份校验。 - true：进行校验。 - false：不进行校验。

        :param indices_backup_check: The indices_backup_check of this UpgradingTheKernelBody.
        :type indices_backup_check: bool
        """
        self._indices_backup_check = indices_backup_check

    @property
    def agency(self):
        """Gets the agency of this UpgradingTheKernelBody.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :return: The agency of this UpgradingTheKernelBody.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this UpgradingTheKernelBody.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :param agency: The agency of this UpgradingTheKernelBody.
        :type agency: str
        """
        self._agency = agency

    @property
    def check_load(self):
        """Gets the check_load of this UpgradingTheKernelBody.

        是否校验负载。默认为true。 - true：进行校验。 - false：不进行校验。

        :return: The check_load of this UpgradingTheKernelBody.
        :rtype: bool
        """
        return self._check_load

    @check_load.setter
    def check_load(self, check_load):
        """Sets the check_load of this UpgradingTheKernelBody.

        是否校验负载。默认为true。 - true：进行校验。 - false：不进行校验。

        :param check_load: The check_load of this UpgradingTheKernelBody.
        :type check_load: bool
        """
        self._check_load = check_load

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
