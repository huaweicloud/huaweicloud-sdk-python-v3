# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpmOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_profile_rule': 'str',
        'redir_exclude_common_folders': 'str',
        'redir_exclude_copy0s': 'str',
        'redir_exclude_copy1s': 'str',
        'redir_exclude_copy2s': 'str',
        'redir_exclude_copy3s': 'str',
        'redir_exclude_includes': 'str'
    }

    attribute_map = {
        'user_profile_rule': 'user_profile_rule',
        'redir_exclude_common_folders': 'redir_exclude_common_folders',
        'redir_exclude_copy0s': 'redir_exclude_copy0s',
        'redir_exclude_copy1s': 'redir_exclude_copy1s',
        'redir_exclude_copy2s': 'redir_exclude_copy2s',
        'redir_exclude_copy3s': 'redir_exclude_copy3s',
        'redir_exclude_includes': 'redir_exclude_includes'
    }

    def __init__(self, user_profile_rule=None, redir_exclude_common_folders=None, redir_exclude_copy0s=None, redir_exclude_copy1s=None, redir_exclude_copy2s=None, redir_exclude_copy3s=None, redir_exclude_includes=None):
        r"""UpmOptions

        The model defined in huaweicloud sdk

        :param user_profile_rule: 配置项内容。
        :type user_profile_rule: str
        :param redir_exclude_common_folders: 排除常用文件夹。
        :type redir_exclude_common_folders: str
        :param redir_exclude_copy0s: 禁止自定义文件夹/copy base &#x3D; 0,copy back &#x3D; 0。
        :type redir_exclude_copy0s: str
        :param redir_exclude_copy1s: 禁止自定义文件夹/copy base &#x3D; 0,copy back &#x3D; 1。
        :type redir_exclude_copy1s: str
        :param redir_exclude_copy2s: 禁止自定义文件夹/copy base &#x3D; 1,copy back &#x3D; 0。
        :type redir_exclude_copy2s: str
        :param redir_exclude_copy3s: 禁止自定义文件夹/copy base &#x3D; 1,copy back &#x3D; 1。
        :type redir_exclude_copy3s: str
        :param redir_exclude_includes: 允许自定义文件夹
        :type redir_exclude_includes: str
        """
        
        

        self._user_profile_rule = None
        self._redir_exclude_common_folders = None
        self._redir_exclude_copy0s = None
        self._redir_exclude_copy1s = None
        self._redir_exclude_copy2s = None
        self._redir_exclude_copy3s = None
        self._redir_exclude_includes = None
        self.discriminator = None

        if user_profile_rule is not None:
            self.user_profile_rule = user_profile_rule
        if redir_exclude_common_folders is not None:
            self.redir_exclude_common_folders = redir_exclude_common_folders
        if redir_exclude_copy0s is not None:
            self.redir_exclude_copy0s = redir_exclude_copy0s
        if redir_exclude_copy1s is not None:
            self.redir_exclude_copy1s = redir_exclude_copy1s
        if redir_exclude_copy2s is not None:
            self.redir_exclude_copy2s = redir_exclude_copy2s
        if redir_exclude_copy3s is not None:
            self.redir_exclude_copy3s = redir_exclude_copy3s
        if redir_exclude_includes is not None:
            self.redir_exclude_includes = redir_exclude_includes

    @property
    def user_profile_rule(self):
        r"""Gets the user_profile_rule of this UpmOptions.

        配置项内容。

        :return: The user_profile_rule of this UpmOptions.
        :rtype: str
        """
        return self._user_profile_rule

    @user_profile_rule.setter
    def user_profile_rule(self, user_profile_rule):
        r"""Sets the user_profile_rule of this UpmOptions.

        配置项内容。

        :param user_profile_rule: The user_profile_rule of this UpmOptions.
        :type user_profile_rule: str
        """
        self._user_profile_rule = user_profile_rule

    @property
    def redir_exclude_common_folders(self):
        r"""Gets the redir_exclude_common_folders of this UpmOptions.

        排除常用文件夹。

        :return: The redir_exclude_common_folders of this UpmOptions.
        :rtype: str
        """
        return self._redir_exclude_common_folders

    @redir_exclude_common_folders.setter
    def redir_exclude_common_folders(self, redir_exclude_common_folders):
        r"""Sets the redir_exclude_common_folders of this UpmOptions.

        排除常用文件夹。

        :param redir_exclude_common_folders: The redir_exclude_common_folders of this UpmOptions.
        :type redir_exclude_common_folders: str
        """
        self._redir_exclude_common_folders = redir_exclude_common_folders

    @property
    def redir_exclude_copy0s(self):
        r"""Gets the redir_exclude_copy0s of this UpmOptions.

        禁止自定义文件夹/copy base = 0,copy back = 0。

        :return: The redir_exclude_copy0s of this UpmOptions.
        :rtype: str
        """
        return self._redir_exclude_copy0s

    @redir_exclude_copy0s.setter
    def redir_exclude_copy0s(self, redir_exclude_copy0s):
        r"""Sets the redir_exclude_copy0s of this UpmOptions.

        禁止自定义文件夹/copy base = 0,copy back = 0。

        :param redir_exclude_copy0s: The redir_exclude_copy0s of this UpmOptions.
        :type redir_exclude_copy0s: str
        """
        self._redir_exclude_copy0s = redir_exclude_copy0s

    @property
    def redir_exclude_copy1s(self):
        r"""Gets the redir_exclude_copy1s of this UpmOptions.

        禁止自定义文件夹/copy base = 0,copy back = 1。

        :return: The redir_exclude_copy1s of this UpmOptions.
        :rtype: str
        """
        return self._redir_exclude_copy1s

    @redir_exclude_copy1s.setter
    def redir_exclude_copy1s(self, redir_exclude_copy1s):
        r"""Sets the redir_exclude_copy1s of this UpmOptions.

        禁止自定义文件夹/copy base = 0,copy back = 1。

        :param redir_exclude_copy1s: The redir_exclude_copy1s of this UpmOptions.
        :type redir_exclude_copy1s: str
        """
        self._redir_exclude_copy1s = redir_exclude_copy1s

    @property
    def redir_exclude_copy2s(self):
        r"""Gets the redir_exclude_copy2s of this UpmOptions.

        禁止自定义文件夹/copy base = 1,copy back = 0。

        :return: The redir_exclude_copy2s of this UpmOptions.
        :rtype: str
        """
        return self._redir_exclude_copy2s

    @redir_exclude_copy2s.setter
    def redir_exclude_copy2s(self, redir_exclude_copy2s):
        r"""Sets the redir_exclude_copy2s of this UpmOptions.

        禁止自定义文件夹/copy base = 1,copy back = 0。

        :param redir_exclude_copy2s: The redir_exclude_copy2s of this UpmOptions.
        :type redir_exclude_copy2s: str
        """
        self._redir_exclude_copy2s = redir_exclude_copy2s

    @property
    def redir_exclude_copy3s(self):
        r"""Gets the redir_exclude_copy3s of this UpmOptions.

        禁止自定义文件夹/copy base = 1,copy back = 1。

        :return: The redir_exclude_copy3s of this UpmOptions.
        :rtype: str
        """
        return self._redir_exclude_copy3s

    @redir_exclude_copy3s.setter
    def redir_exclude_copy3s(self, redir_exclude_copy3s):
        r"""Sets the redir_exclude_copy3s of this UpmOptions.

        禁止自定义文件夹/copy base = 1,copy back = 1。

        :param redir_exclude_copy3s: The redir_exclude_copy3s of this UpmOptions.
        :type redir_exclude_copy3s: str
        """
        self._redir_exclude_copy3s = redir_exclude_copy3s

    @property
    def redir_exclude_includes(self):
        r"""Gets the redir_exclude_includes of this UpmOptions.

        允许自定义文件夹

        :return: The redir_exclude_includes of this UpmOptions.
        :rtype: str
        """
        return self._redir_exclude_includes

    @redir_exclude_includes.setter
    def redir_exclude_includes(self, redir_exclude_includes):
        r"""Sets the redir_exclude_includes of this UpmOptions.

        允许自定义文件夹

        :param redir_exclude_includes: The redir_exclude_includes of this UpmOptions.
        :type redir_exclude_includes: str
        """
        self._redir_exclude_includes = redir_exclude_includes

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
        if not isinstance(other, UpmOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
