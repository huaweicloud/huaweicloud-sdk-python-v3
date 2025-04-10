# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IPWhiteList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'allow_list': 'list[IpAllowList]'
    }

    attribute_map = {
        'enable': 'enable',
        'allow_list': 'allow_list'
    }

    def __init__(self, enable=None, allow_list=None):
        r"""IPWhiteList

        The model defined in huaweicloud sdk

        :param enable: **参数说明**：启用Ip白名单访问控制 
        :type enable: bool
        :param allow_list: 允许访问企业版实例的IP地址列表 
        :type allow_list: list[:class:`huaweicloudsdkiotdm.v5.IpAllowList`]
        """
        
        

        self._enable = None
        self._allow_list = None
        self.discriminator = None

        self.enable = enable
        if allow_list is not None:
            self.allow_list = allow_list

    @property
    def enable(self):
        r"""Gets the enable of this IPWhiteList.

        **参数说明**：启用Ip白名单访问控制 

        :return: The enable of this IPWhiteList.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this IPWhiteList.

        **参数说明**：启用Ip白名单访问控制 

        :param enable: The enable of this IPWhiteList.
        :type enable: bool
        """
        self._enable = enable

    @property
    def allow_list(self):
        r"""Gets the allow_list of this IPWhiteList.

        允许访问企业版实例的IP地址列表 

        :return: The allow_list of this IPWhiteList.
        :rtype: list[:class:`huaweicloudsdkiotdm.v5.IpAllowList`]
        """
        return self._allow_list

    @allow_list.setter
    def allow_list(self, allow_list):
        r"""Sets the allow_list of this IPWhiteList.

        允许访问企业版实例的IP地址列表 

        :param allow_list: The allow_list of this IPWhiteList.
        :type allow_list: list[:class:`huaweicloudsdkiotdm.v5.IpAllowList`]
        """
        self._allow_list = allow_list

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
        if not isinstance(other, IPWhiteList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
