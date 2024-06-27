# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_aw_available': 'bool',
        'public_aw_available': 'bool',
        'refresh_aw_available': 'bool'
    }

    attribute_map = {
        'custom_aw_available': 'custom_aw_available',
        'public_aw_available': 'public_aw_available',
        'refresh_aw_available': 'refresh_aw_available'
    }

    def __init__(self, custom_aw_available=None, public_aw_available=None, refresh_aw_available=None):
        """AvailableConfig

        The model defined in huaweicloud sdk

        :param custom_aw_available: 自定义关键字是否开通
        :type custom_aw_available: bool
        :param public_aw_available: 系统关键字是否开通
        :type public_aw_available: bool
        :param refresh_aw_available: 一键刷新功能是否开通
        :type refresh_aw_available: bool
        """
        
        

        self._custom_aw_available = None
        self._public_aw_available = None
        self._refresh_aw_available = None
        self.discriminator = None

        if custom_aw_available is not None:
            self.custom_aw_available = custom_aw_available
        if public_aw_available is not None:
            self.public_aw_available = public_aw_available
        if refresh_aw_available is not None:
            self.refresh_aw_available = refresh_aw_available

    @property
    def custom_aw_available(self):
        """Gets the custom_aw_available of this AvailableConfig.

        自定义关键字是否开通

        :return: The custom_aw_available of this AvailableConfig.
        :rtype: bool
        """
        return self._custom_aw_available

    @custom_aw_available.setter
    def custom_aw_available(self, custom_aw_available):
        """Sets the custom_aw_available of this AvailableConfig.

        自定义关键字是否开通

        :param custom_aw_available: The custom_aw_available of this AvailableConfig.
        :type custom_aw_available: bool
        """
        self._custom_aw_available = custom_aw_available

    @property
    def public_aw_available(self):
        """Gets the public_aw_available of this AvailableConfig.

        系统关键字是否开通

        :return: The public_aw_available of this AvailableConfig.
        :rtype: bool
        """
        return self._public_aw_available

    @public_aw_available.setter
    def public_aw_available(self, public_aw_available):
        """Sets the public_aw_available of this AvailableConfig.

        系统关键字是否开通

        :param public_aw_available: The public_aw_available of this AvailableConfig.
        :type public_aw_available: bool
        """
        self._public_aw_available = public_aw_available

    @property
    def refresh_aw_available(self):
        """Gets the refresh_aw_available of this AvailableConfig.

        一键刷新功能是否开通

        :return: The refresh_aw_available of this AvailableConfig.
        :rtype: bool
        """
        return self._refresh_aw_available

    @refresh_aw_available.setter
    def refresh_aw_available(self, refresh_aw_available):
        """Sets the refresh_aw_available of this AvailableConfig.

        一键刷新功能是否开通

        :param refresh_aw_available: The refresh_aw_available of this AvailableConfig.
        :type refresh_aw_available: bool
        """
        self._refresh_aw_available = refresh_aw_available

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
        if not isinstance(other, AvailableConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
