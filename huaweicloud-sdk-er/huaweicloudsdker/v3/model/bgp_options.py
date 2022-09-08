# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BgpOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'load_balancing_as_path_ignore': 'bool',
        'load_balancing_as_path_relax': 'bool'
    }

    attribute_map = {
        'load_balancing_as_path_ignore': 'load_balancing_as_path_ignore',
        'load_balancing_as_path_relax': 'load_balancing_as_path_relax'
    }

    def __init__(self, load_balancing_as_path_ignore=None, load_balancing_as_path_relax=None):
        """BgpOptions

        The model defined in huaweicloud sdk

        :param load_balancing_as_path_ignore: 配置路由在形成负载分担时不比较路由的AS-Path属性
        :type load_balancing_as_path_ignore: bool
        :param load_balancing_as_path_relax: 配置路由在形成负载分担时不比较相同长度的AS-Path属性
        :type load_balancing_as_path_relax: bool
        """
        
        

        self._load_balancing_as_path_ignore = None
        self._load_balancing_as_path_relax = None
        self.discriminator = None

        if load_balancing_as_path_ignore is not None:
            self.load_balancing_as_path_ignore = load_balancing_as_path_ignore
        if load_balancing_as_path_relax is not None:
            self.load_balancing_as_path_relax = load_balancing_as_path_relax

    @property
    def load_balancing_as_path_ignore(self):
        """Gets the load_balancing_as_path_ignore of this BgpOptions.

        配置路由在形成负载分担时不比较路由的AS-Path属性

        :return: The load_balancing_as_path_ignore of this BgpOptions.
        :rtype: bool
        """
        return self._load_balancing_as_path_ignore

    @load_balancing_as_path_ignore.setter
    def load_balancing_as_path_ignore(self, load_balancing_as_path_ignore):
        """Sets the load_balancing_as_path_ignore of this BgpOptions.

        配置路由在形成负载分担时不比较路由的AS-Path属性

        :param load_balancing_as_path_ignore: The load_balancing_as_path_ignore of this BgpOptions.
        :type load_balancing_as_path_ignore: bool
        """
        self._load_balancing_as_path_ignore = load_balancing_as_path_ignore

    @property
    def load_balancing_as_path_relax(self):
        """Gets the load_balancing_as_path_relax of this BgpOptions.

        配置路由在形成负载分担时不比较相同长度的AS-Path属性

        :return: The load_balancing_as_path_relax of this BgpOptions.
        :rtype: bool
        """
        return self._load_balancing_as_path_relax

    @load_balancing_as_path_relax.setter
    def load_balancing_as_path_relax(self, load_balancing_as_path_relax):
        """Sets the load_balancing_as_path_relax of this BgpOptions.

        配置路由在形成负载分担时不比较相同长度的AS-Path属性

        :param load_balancing_as_path_relax: The load_balancing_as_path_relax of this BgpOptions.
        :type load_balancing_as_path_relax: bool
        """
        self._load_balancing_as_path_relax = load_balancing_as_path_relax

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
        if not isinstance(other, BgpOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
