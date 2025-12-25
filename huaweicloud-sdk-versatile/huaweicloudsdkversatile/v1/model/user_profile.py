# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserProfile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_retrieve': 'bool',
        'enable_extract': 'bool'
    }

    attribute_map = {
        'enable_retrieve': 'enable_retrieve',
        'enable_extract': 'enable_extract'
    }

    def __init__(self, enable_retrieve=None, enable_extract=None):
        r"""UserProfile

        The model defined in huaweicloud sdk

        :param enable_retrieve: 运行时, 是否读取用户画像
        :type enable_retrieve: bool
        :param enable_extract: 运行时, 是否构建用户画像
        :type enable_extract: bool
        """
        
        

        self._enable_retrieve = None
        self._enable_extract = None
        self.discriminator = None

        if enable_retrieve is not None:
            self.enable_retrieve = enable_retrieve
        if enable_extract is not None:
            self.enable_extract = enable_extract

    @property
    def enable_retrieve(self):
        r"""Gets the enable_retrieve of this UserProfile.

        运行时, 是否读取用户画像

        :return: The enable_retrieve of this UserProfile.
        :rtype: bool
        """
        return self._enable_retrieve

    @enable_retrieve.setter
    def enable_retrieve(self, enable_retrieve):
        r"""Sets the enable_retrieve of this UserProfile.

        运行时, 是否读取用户画像

        :param enable_retrieve: The enable_retrieve of this UserProfile.
        :type enable_retrieve: bool
        """
        self._enable_retrieve = enable_retrieve

    @property
    def enable_extract(self):
        r"""Gets the enable_extract of this UserProfile.

        运行时, 是否构建用户画像

        :return: The enable_extract of this UserProfile.
        :rtype: bool
        """
        return self._enable_extract

    @enable_extract.setter
    def enable_extract(self, enable_extract):
        r"""Sets the enable_extract of this UserProfile.

        运行时, 是否构建用户画像

        :param enable_extract: The enable_extract of this UserProfile.
        :type enable_extract: bool
        """
        self._enable_extract = enable_extract

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
        if not isinstance(other, UserProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
