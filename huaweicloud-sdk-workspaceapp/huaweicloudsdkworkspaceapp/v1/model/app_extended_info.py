# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppExtendedInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extended_info': 'dict(str, str)'
    }

    attribute_map = {
        'extended_info': 'extended_info'
    }

    def __init__(self, extended_info=None):
        r"""AppExtendedInfo

        The model defined in huaweicloud sdk

        :param extended_info: 扩展信息的键值对映射
        :type extended_info: dict(str, str)
        """
        
        

        self._extended_info = None
        self.discriminator = None

        if extended_info is not None:
            self.extended_info = extended_info

    @property
    def extended_info(self):
        r"""Gets the extended_info of this AppExtendedInfo.

        扩展信息的键值对映射

        :return: The extended_info of this AppExtendedInfo.
        :rtype: dict(str, str)
        """
        return self._extended_info

    @extended_info.setter
    def extended_info(self, extended_info):
        r"""Sets the extended_info of this AppExtendedInfo.

        扩展信息的键值对映射

        :param extended_info: The extended_info of this AppExtendedInfo.
        :type extended_info: dict(str, str)
        """
        self._extended_info = extended_info

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
        if not isinstance(other, AppExtendedInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
