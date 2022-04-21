# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicipInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ip_version': 'int',
        'publicip_address': 'str',
        'publicip_id': 'str',
        'publicip_type': 'str'
    }

    attribute_map = {
        'ip_version': 'ip_version',
        'publicip_address': 'publicip_address',
        'publicip_id': 'publicip_id',
        'publicip_type': 'publicip_type'
    }

    def __init__(self, ip_version=None, publicip_address=None, publicip_id=None, publicip_type=None):
        """PublicipInfo

        The model defined in huaweicloud sdk

        :param ip_version:   IP版本的信息
        :type ip_version: int
        :param publicip_address: 弹性公网IP
        :type publicip_address: str
        :param publicip_id: 弹性公网IP的ID。
        :type publicip_id: str
        :param publicip_type: 功能说明：弹性公网IP的类型
        :type publicip_type: str
        """
        
        

        self._ip_version = None
        self._publicip_address = None
        self._publicip_id = None
        self._publicip_type = None
        self.discriminator = None

        if ip_version is not None:
            self.ip_version = ip_version
        if publicip_address is not None:
            self.publicip_address = publicip_address
        if publicip_id is not None:
            self.publicip_id = publicip_id
        if publicip_type is not None:
            self.publicip_type = publicip_type

    @property
    def ip_version(self):
        """Gets the ip_version of this PublicipInfo.

          IP版本的信息

        :return: The ip_version of this PublicipInfo.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this PublicipInfo.

          IP版本的信息

        :param ip_version: The ip_version of this PublicipInfo.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def publicip_address(self):
        """Gets the publicip_address of this PublicipInfo.

        弹性公网IP

        :return: The publicip_address of this PublicipInfo.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        """Sets the publicip_address of this PublicipInfo.

        弹性公网IP

        :param publicip_address: The publicip_address of this PublicipInfo.
        :type publicip_address: str
        """
        self._publicip_address = publicip_address

    @property
    def publicip_id(self):
        """Gets the publicip_id of this PublicipInfo.

        弹性公网IP的ID。

        :return: The publicip_id of this PublicipInfo.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this PublicipInfo.

        弹性公网IP的ID。

        :param publicip_id: The publicip_id of this PublicipInfo.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def publicip_type(self):
        """Gets the publicip_type of this PublicipInfo.

        功能说明：弹性公网IP的类型

        :return: The publicip_type of this PublicipInfo.
        :rtype: str
        """
        return self._publicip_type

    @publicip_type.setter
    def publicip_type(self, publicip_type):
        """Sets the publicip_type of this PublicipInfo.

        功能说明：弹性公网IP的类型

        :param publicip_type: The publicip_type of this PublicipInfo.
        :type publicip_type: str
        """
        self._publicip_type = publicip_type

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
        if not isinstance(other, PublicipInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
