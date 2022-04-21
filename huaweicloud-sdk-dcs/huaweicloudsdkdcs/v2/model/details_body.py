# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetailsBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'old_capacity': 'str',
        'new_capacity': 'str',
        'enable_public_ip': 'bool',
        'public_ip_id': 'str',
        'public_ip_address': 'str',
        'enable_ssl': 'bool',
        'old_cache_mode': 'str',
        'new_cache_mode': 'str'
    }

    attribute_map = {
        'old_capacity': 'old_capacity',
        'new_capacity': 'new_capacity',
        'enable_public_ip': 'enable_public_ip',
        'public_ip_id': 'public_ip_id',
        'public_ip_address': 'public_ip_address',
        'enable_ssl': 'enable_ssl',
        'old_cache_mode': 'old_cache_mode',
        'new_cache_mode': 'new_cache_mode'
    }

    def __init__(self, old_capacity=None, new_capacity=None, enable_public_ip=None, public_ip_id=None, public_ip_address=None, enable_ssl=None, old_cache_mode=None, new_cache_mode=None):
        """DetailsBody

        The model defined in huaweicloud sdk

        :param old_capacity: 变更前的容量，仅在变更规格时有值
        :type old_capacity: str
        :param new_capacity: 变更后的容量，仅在变更规格时有值
        :type new_capacity: str
        :param enable_public_ip: 是否开启公网访问，仅在开启公网访问时有值
        :type enable_public_ip: bool
        :param public_ip_id: 公网IP的ID，仅在开启公网访问时有值
        :type public_ip_id: str
        :param public_ip_address: 公网IP地址，仅在开启公网访问时有值
        :type public_ip_address: str
        :param enable_ssl: 是否开启ssl，仅在开启ssl时有值
        :type enable_ssl: bool
        :param old_cache_mode: 变更前的缓存类型，仅在变更规格时有值
        :type old_cache_mode: str
        :param new_cache_mode: 变更后的缓存类型，仅在变更规格时有值
        :type new_cache_mode: str
        """
        
        

        self._old_capacity = None
        self._new_capacity = None
        self._enable_public_ip = None
        self._public_ip_id = None
        self._public_ip_address = None
        self._enable_ssl = None
        self._old_cache_mode = None
        self._new_cache_mode = None
        self.discriminator = None

        if old_capacity is not None:
            self.old_capacity = old_capacity
        if new_capacity is not None:
            self.new_capacity = new_capacity
        if enable_public_ip is not None:
            self.enable_public_ip = enable_public_ip
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if old_cache_mode is not None:
            self.old_cache_mode = old_cache_mode
        if new_cache_mode is not None:
            self.new_cache_mode = new_cache_mode

    @property
    def old_capacity(self):
        """Gets the old_capacity of this DetailsBody.

        变更前的容量，仅在变更规格时有值

        :return: The old_capacity of this DetailsBody.
        :rtype: str
        """
        return self._old_capacity

    @old_capacity.setter
    def old_capacity(self, old_capacity):
        """Sets the old_capacity of this DetailsBody.

        变更前的容量，仅在变更规格时有值

        :param old_capacity: The old_capacity of this DetailsBody.
        :type old_capacity: str
        """
        self._old_capacity = old_capacity

    @property
    def new_capacity(self):
        """Gets the new_capacity of this DetailsBody.

        变更后的容量，仅在变更规格时有值

        :return: The new_capacity of this DetailsBody.
        :rtype: str
        """
        return self._new_capacity

    @new_capacity.setter
    def new_capacity(self, new_capacity):
        """Sets the new_capacity of this DetailsBody.

        变更后的容量，仅在变更规格时有值

        :param new_capacity: The new_capacity of this DetailsBody.
        :type new_capacity: str
        """
        self._new_capacity = new_capacity

    @property
    def enable_public_ip(self):
        """Gets the enable_public_ip of this DetailsBody.

        是否开启公网访问，仅在开启公网访问时有值

        :return: The enable_public_ip of this DetailsBody.
        :rtype: bool
        """
        return self._enable_public_ip

    @enable_public_ip.setter
    def enable_public_ip(self, enable_public_ip):
        """Sets the enable_public_ip of this DetailsBody.

        是否开启公网访问，仅在开启公网访问时有值

        :param enable_public_ip: The enable_public_ip of this DetailsBody.
        :type enable_public_ip: bool
        """
        self._enable_public_ip = enable_public_ip

    @property
    def public_ip_id(self):
        """Gets the public_ip_id of this DetailsBody.

        公网IP的ID，仅在开启公网访问时有值

        :return: The public_ip_id of this DetailsBody.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        """Sets the public_ip_id of this DetailsBody.

        公网IP的ID，仅在开启公网访问时有值

        :param public_ip_id: The public_ip_id of this DetailsBody.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this DetailsBody.

        公网IP地址，仅在开启公网访问时有值

        :return: The public_ip_address of this DetailsBody.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this DetailsBody.

        公网IP地址，仅在开启公网访问时有值

        :param public_ip_address: The public_ip_address of this DetailsBody.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def enable_ssl(self):
        """Gets the enable_ssl of this DetailsBody.

        是否开启ssl，仅在开启ssl时有值

        :return: The enable_ssl of this DetailsBody.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        """Sets the enable_ssl of this DetailsBody.

        是否开启ssl，仅在开启ssl时有值

        :param enable_ssl: The enable_ssl of this DetailsBody.
        :type enable_ssl: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def old_cache_mode(self):
        """Gets the old_cache_mode of this DetailsBody.

        变更前的缓存类型，仅在变更规格时有值

        :return: The old_cache_mode of this DetailsBody.
        :rtype: str
        """
        return self._old_cache_mode

    @old_cache_mode.setter
    def old_cache_mode(self, old_cache_mode):
        """Sets the old_cache_mode of this DetailsBody.

        变更前的缓存类型，仅在变更规格时有值

        :param old_cache_mode: The old_cache_mode of this DetailsBody.
        :type old_cache_mode: str
        """
        self._old_cache_mode = old_cache_mode

    @property
    def new_cache_mode(self):
        """Gets the new_cache_mode of this DetailsBody.

        变更后的缓存类型，仅在变更规格时有值

        :return: The new_cache_mode of this DetailsBody.
        :rtype: str
        """
        return self._new_cache_mode

    @new_cache_mode.setter
    def new_cache_mode(self, new_cache_mode):
        """Sets the new_cache_mode of this DetailsBody.

        变更后的缓存类型，仅在变更规格时有值

        :param new_cache_mode: The new_cache_mode of this DetailsBody.
        :type new_cache_mode: str
        """
        self._new_cache_mode = new_cache_mode

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
        if not isinstance(other, DetailsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
