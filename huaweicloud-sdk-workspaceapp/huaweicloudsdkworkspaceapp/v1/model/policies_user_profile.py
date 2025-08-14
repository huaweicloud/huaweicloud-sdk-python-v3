# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesUserProfile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_profile_enable': 'bool',
        'options': 'UpmOptions'
    }

    attribute_map = {
        'user_profile_enable': 'user_profile_enable',
        'options': 'options'
    }

    def __init__(self, user_profile_enable=None, options=None):
        r"""PoliciesUserProfile

        The model defined in huaweicloud sdk

        :param user_profile_enable: 配置文件漫游技术配置开关： false: 表示关闭 true: 表示开启
        :type user_profile_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.UpmOptions`
        """
        
        

        self._user_profile_enable = None
        self._options = None
        self.discriminator = None

        if user_profile_enable is not None:
            self.user_profile_enable = user_profile_enable
        if options is not None:
            self.options = options

    @property
    def user_profile_enable(self):
        r"""Gets the user_profile_enable of this PoliciesUserProfile.

        配置文件漫游技术配置开关： false: 表示关闭 true: 表示开启

        :return: The user_profile_enable of this PoliciesUserProfile.
        :rtype: bool
        """
        return self._user_profile_enable

    @user_profile_enable.setter
    def user_profile_enable(self, user_profile_enable):
        r"""Sets the user_profile_enable of this PoliciesUserProfile.

        配置文件漫游技术配置开关： false: 表示关闭 true: 表示开启

        :param user_profile_enable: The user_profile_enable of this PoliciesUserProfile.
        :type user_profile_enable: bool
        """
        self._user_profile_enable = user_profile_enable

    @property
    def options(self):
        r"""Gets the options of this PoliciesUserProfile.

        :return: The options of this PoliciesUserProfile.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.UpmOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this PoliciesUserProfile.

        :param options: The options of this PoliciesUserProfile.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.UpmOptions`
        """
        self._options = options

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
        if not isinstance(other, PoliciesUserProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
