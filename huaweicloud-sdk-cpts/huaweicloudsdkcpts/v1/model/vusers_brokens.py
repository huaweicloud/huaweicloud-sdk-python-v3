# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VusersBrokens:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vusers': 'list[float]'
    }

    attribute_map = {
        'vusers': 'vusers'
    }

    def __init__(self, vusers=None):
        r"""VusersBrokens

        The model defined in huaweicloud sdk

        :param vusers: 虚拟用户数
        :type vusers: list[float]
        """
        
        

        self._vusers = None
        self.discriminator = None

        if vusers is not None:
            self.vusers = vusers

    @property
    def vusers(self):
        r"""Gets the vusers of this VusersBrokens.

        虚拟用户数

        :return: The vusers of this VusersBrokens.
        :rtype: list[float]
        """
        return self._vusers

    @vusers.setter
    def vusers(self, vusers):
        r"""Sets the vusers of this VusersBrokens.

        虚拟用户数

        :param vusers: The vusers of this VusersBrokens.
        :type vusers: list[float]
        """
        self._vusers = vusers

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
        if not isinstance(other, VusersBrokens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
