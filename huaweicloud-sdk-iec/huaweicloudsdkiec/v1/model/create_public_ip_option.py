# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePublicIpOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_id': 'str',
        'ip_version': 'str',
        'type': 'str'
    }

    attribute_map = {
        'site_id': 'site_id',
        'ip_version': 'ip_version',
        'type': 'type'
    }

    def __init__(self, site_id=None, ip_version=None, type=None):
        """CreatePublicIpOption

        The model defined in huaweicloud sdk

        :param site_id: 边缘站点的ID。
        :type site_id: str
        :param ip_version: 弹性公网IP的版本。目前IEC服务只支持4，即ipv4。
        :type ip_version: str
        :param type: 线路ID。 不传时默认取当前站点第一条线路
        :type type: str
        """
        
        

        self._site_id = None
        self._ip_version = None
        self._type = None
        self.discriminator = None

        self.site_id = site_id
        if ip_version is not None:
            self.ip_version = ip_version
        if type is not None:
            self.type = type

    @property
    def site_id(self):
        """Gets the site_id of this CreatePublicIpOption.

        边缘站点的ID。

        :return: The site_id of this CreatePublicIpOption.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this CreatePublicIpOption.

        边缘站点的ID。

        :param site_id: The site_id of this CreatePublicIpOption.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def ip_version(self):
        """Gets the ip_version of this CreatePublicIpOption.

        弹性公网IP的版本。目前IEC服务只支持4，即ipv4。

        :return: The ip_version of this CreatePublicIpOption.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this CreatePublicIpOption.

        弹性公网IP的版本。目前IEC服务只支持4，即ipv4。

        :param ip_version: The ip_version of this CreatePublicIpOption.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def type(self):
        """Gets the type of this CreatePublicIpOption.

        线路ID。 不传时默认取当前站点第一条线路

        :return: The type of this CreatePublicIpOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreatePublicIpOption.

        线路ID。 不传时默认取当前站点第一条线路

        :param type: The type of this CreatePublicIpOption.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, CreatePublicIpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
