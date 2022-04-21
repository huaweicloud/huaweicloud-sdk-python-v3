# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReinstallServerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_tags': 'list[UserTag]',
        'root_volume': 'ReinstallVolumeSpec'
    }

    attribute_map = {
        'user_tags': 'userTags',
        'root_volume': 'rootVolume'
    }

    def __init__(self, user_tags=None, root_volume=None):
        """ReinstallServerConfig

        The model defined in huaweicloud sdk

        :param user_tags: 云服务器标签，键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为5个。
        :type user_tags: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkcce.v3.ReinstallVolumeSpec`
        """
        
        

        self._user_tags = None
        self._root_volume = None
        self.discriminator = None

        if user_tags is not None:
            self.user_tags = user_tags
        if root_volume is not None:
            self.root_volume = root_volume

    @property
    def user_tags(self):
        """Gets the user_tags of this ReinstallServerConfig.

        云服务器标签，键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为5个。

        :return: The user_tags of this ReinstallServerConfig.
        :rtype: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        """
        return self._user_tags

    @user_tags.setter
    def user_tags(self, user_tags):
        """Sets the user_tags of this ReinstallServerConfig.

        云服务器标签，键必须唯一，CCE支持的最大用户自定义标签数量依region而定，自定义标签数上限为5个。

        :param user_tags: The user_tags of this ReinstallServerConfig.
        :type user_tags: list[:class:`huaweicloudsdkcce.v3.UserTag`]
        """
        self._user_tags = user_tags

    @property
    def root_volume(self):
        """Gets the root_volume of this ReinstallServerConfig.


        :return: The root_volume of this ReinstallServerConfig.
        :rtype: :class:`huaweicloudsdkcce.v3.ReinstallVolumeSpec`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        """Sets the root_volume of this ReinstallServerConfig.


        :param root_volume: The root_volume of this ReinstallServerConfig.
        :type root_volume: :class:`huaweicloudsdkcce.v3.ReinstallVolumeSpec`
        """
        self._root_volume = root_volume

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
        if not isinstance(other, ReinstallServerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
