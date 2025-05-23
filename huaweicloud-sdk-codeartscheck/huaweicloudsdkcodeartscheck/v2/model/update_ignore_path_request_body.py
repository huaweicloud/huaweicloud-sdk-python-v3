# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIgnorePathRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ignore_path_settings': 'list[IgnorePathSettingItem]'
    }

    attribute_map = {
        'ignore_path_settings': 'ignore_path_settings'
    }

    def __init__(self, ignore_path_settings=None):
        r"""UpdateIgnorePathRequestBody

        The model defined in huaweicloud sdk

        :param ignore_path_settings: 屏蔽目录的节点信息列表
        :type ignore_path_settings: list[:class:`huaweicloudsdkcodeartscheck.v2.IgnorePathSettingItem`]
        """
        
        

        self._ignore_path_settings = None
        self.discriminator = None

        self.ignore_path_settings = ignore_path_settings

    @property
    def ignore_path_settings(self):
        r"""Gets the ignore_path_settings of this UpdateIgnorePathRequestBody.

        屏蔽目录的节点信息列表

        :return: The ignore_path_settings of this UpdateIgnorePathRequestBody.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.IgnorePathSettingItem`]
        """
        return self._ignore_path_settings

    @ignore_path_settings.setter
    def ignore_path_settings(self, ignore_path_settings):
        r"""Sets the ignore_path_settings of this UpdateIgnorePathRequestBody.

        屏蔽目录的节点信息列表

        :param ignore_path_settings: The ignore_path_settings of this UpdateIgnorePathRequestBody.
        :type ignore_path_settings: list[:class:`huaweicloudsdkcodeartscheck.v2.IgnorePathSettingItem`]
        """
        self._ignore_path_settings = ignore_path_settings

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
        if not isinstance(other, UpdateIgnorePathRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
