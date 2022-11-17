# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpsItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ips': 'list[str]',
        'update_time': 'int'
    }

    attribute_map = {
        'ips': 'ips',
        'update_time': 'update_time'
    }

    def __init__(self, ips=None, update_time=None):
        """IpsItem

        The model defined in huaweicloud sdk

        :param ips: waf回源Ip
        :type ips: list[str]
        :param update_time: 回源Ip更新时间
        :type update_time: int
        """
        
        

        self._ips = None
        self._update_time = None
        self.discriminator = None

        if ips is not None:
            self.ips = ips
        if update_time is not None:
            self.update_time = update_time

    @property
    def ips(self):
        """Gets the ips of this IpsItem.

        waf回源Ip

        :return: The ips of this IpsItem.
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this IpsItem.

        waf回源Ip

        :param ips: The ips of this IpsItem.
        :type ips: list[str]
        """
        self._ips = ips

    @property
    def update_time(self):
        """Gets the update_time of this IpsItem.

        回源Ip更新时间

        :return: The update_time of this IpsItem.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this IpsItem.

        回源Ip更新时间

        :param update_time: The update_time of this IpsItem.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, IpsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
