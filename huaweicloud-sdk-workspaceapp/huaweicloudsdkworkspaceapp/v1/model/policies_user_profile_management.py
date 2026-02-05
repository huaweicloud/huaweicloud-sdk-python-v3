# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesUserProfileManagement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upm_status': 'int',
        'options': 'UserProfileManagementOptions'
    }

    attribute_map = {
        'upm_status': 'upm_status',
        'options': 'options'
    }

    def __init__(self, upm_status=None, options=None):
        r"""PoliciesUserProfileManagement

        The model defined in huaweicloud sdk

        :param upm_status: 用户配置状态： 0: 已禁用 1: 已启用 2: 未配置
        :type upm_status: int
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.UserProfileManagementOptions`
        """
        
        

        self._upm_status = None
        self._options = None
        self.discriminator = None

        if upm_status is not None:
            self.upm_status = upm_status
        if options is not None:
            self.options = options

    @property
    def upm_status(self):
        r"""Gets the upm_status of this PoliciesUserProfileManagement.

        用户配置状态： 0: 已禁用 1: 已启用 2: 未配置

        :return: The upm_status of this PoliciesUserProfileManagement.
        :rtype: int
        """
        return self._upm_status

    @upm_status.setter
    def upm_status(self, upm_status):
        r"""Sets the upm_status of this PoliciesUserProfileManagement.

        用户配置状态： 0: 已禁用 1: 已启用 2: 未配置

        :param upm_status: The upm_status of this PoliciesUserProfileManagement.
        :type upm_status: int
        """
        self._upm_status = upm_status

    @property
    def options(self):
        r"""Gets the options of this PoliciesUserProfileManagement.

        :return: The options of this PoliciesUserProfileManagement.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UserProfileManagementOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this PoliciesUserProfileManagement.

        :param options: The options of this PoliciesUserProfileManagement.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.UserProfileManagementOptions`
        """
        self._options = options

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
        if not isinstance(other, PoliciesUserProfileManagement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
