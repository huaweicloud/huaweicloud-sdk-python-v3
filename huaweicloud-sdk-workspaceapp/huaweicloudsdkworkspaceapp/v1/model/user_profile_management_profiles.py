# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserProfileManagementProfiles:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vhd_write_back': 'str'
    }

    attribute_map = {
        'vhd_write_back': 'vhd_write_back'
    }

    def __init__(self, vhd_write_back=None):
        r"""UserProfileManagementProfiles

        The model defined in huaweicloud sdk

        :param vhd_write_back: 配置VHD会话回写状态： 0: 已禁用 1: 已启用 2: 未配置
        :type vhd_write_back: str
        """
        
        

        self._vhd_write_back = None
        self.discriminator = None

        if vhd_write_back is not None:
            self.vhd_write_back = vhd_write_back

    @property
    def vhd_write_back(self):
        r"""Gets the vhd_write_back of this UserProfileManagementProfiles.

        配置VHD会话回写状态： 0: 已禁用 1: 已启用 2: 未配置

        :return: The vhd_write_back of this UserProfileManagementProfiles.
        :rtype: str
        """
        return self._vhd_write_back

    @vhd_write_back.setter
    def vhd_write_back(self, vhd_write_back):
        r"""Sets the vhd_write_back of this UserProfileManagementProfiles.

        配置VHD会话回写状态： 0: 已禁用 1: 已启用 2: 未配置

        :param vhd_write_back: The vhd_write_back of this UserProfileManagementProfiles.
        :type vhd_write_back: str
        """
        self._vhd_write_back = vhd_write_back

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
        if not isinstance(other, UserProfileManagementProfiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
