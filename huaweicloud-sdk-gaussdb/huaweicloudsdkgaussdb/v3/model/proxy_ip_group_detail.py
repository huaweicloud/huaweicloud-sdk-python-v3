# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyIpGroupDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'ip_list': 'list[IpGroupItem]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ip_list': 'ip_list'
    }

    def __init__(self, id=None, name=None, ip_list=None):
        """ProxyIpGroupDetail

        The model defined in huaweicloud sdk

        :param id: ipGroup的id
        :type id: str
        :param name: ipGroup的名称
        :type name: str
        :param ip_list: ipGroup内部的ip列表
        :type ip_list: list[:class:`huaweicloudsdkgaussdb.v3.IpGroupItem`]
        """
        
        

        self._id = None
        self._name = None
        self._ip_list = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.ip_list = ip_list

    @property
    def id(self):
        """Gets the id of this ProxyIpGroupDetail.

        ipGroup的id

        :return: The id of this ProxyIpGroupDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProxyIpGroupDetail.

        ipGroup的id

        :param id: The id of this ProxyIpGroupDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ProxyIpGroupDetail.

        ipGroup的名称

        :return: The name of this ProxyIpGroupDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProxyIpGroupDetail.

        ipGroup的名称

        :param name: The name of this ProxyIpGroupDetail.
        :type name: str
        """
        self._name = name

    @property
    def ip_list(self):
        """Gets the ip_list of this ProxyIpGroupDetail.

        ipGroup内部的ip列表

        :return: The ip_list of this ProxyIpGroupDetail.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.IpGroupItem`]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this ProxyIpGroupDetail.

        ipGroup内部的ip列表

        :param ip_list: The ip_list of this ProxyIpGroupDetail.
        :type ip_list: list[:class:`huaweicloudsdkgaussdb.v3.IpGroupItem`]
        """
        self._ip_list = ip_list

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
        if not isinstance(other, ProxyIpGroupDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
