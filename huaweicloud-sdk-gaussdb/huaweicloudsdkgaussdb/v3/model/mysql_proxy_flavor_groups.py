# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlProxyFlavorGroups:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_type': 'str',
        'proxy_flavors': 'list[MysqlProxyComputeFlavor]'
    }

    attribute_map = {
        'group_type': 'group_type',
        'proxy_flavors': 'proxy_flavors'
    }

    def __init__(self, group_type=None, proxy_flavors=None):
        """MysqlProxyFlavorGroups

        The model defined in huaweicloud sdk

        :param group_type: 规格组类型，如x86、arm。
        :type group_type: str
        :param proxy_flavors: 规格信息。
        :type proxy_flavors: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyComputeFlavor`]
        """
        
        

        self._group_type = None
        self._proxy_flavors = None
        self.discriminator = None

        if group_type is not None:
            self.group_type = group_type
        if proxy_flavors is not None:
            self.proxy_flavors = proxy_flavors

    @property
    def group_type(self):
        """Gets the group_type of this MysqlProxyFlavorGroups.

        规格组类型，如x86、arm。

        :return: The group_type of this MysqlProxyFlavorGroups.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this MysqlProxyFlavorGroups.

        规格组类型，如x86、arm。

        :param group_type: The group_type of this MysqlProxyFlavorGroups.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def proxy_flavors(self):
        """Gets the proxy_flavors of this MysqlProxyFlavorGroups.

        规格信息。

        :return: The proxy_flavors of this MysqlProxyFlavorGroups.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyComputeFlavor`]
        """
        return self._proxy_flavors

    @proxy_flavors.setter
    def proxy_flavors(self, proxy_flavors):
        """Sets the proxy_flavors of this MysqlProxyFlavorGroups.

        规格信息。

        :param proxy_flavors: The proxy_flavors of this MysqlProxyFlavorGroups.
        :type proxy_flavors: list[:class:`huaweicloudsdkgaussdb.v3.MysqlProxyComputeFlavor`]
        """
        self._proxy_flavors = proxy_flavors

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
        if not isinstance(other, MysqlProxyFlavorGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
