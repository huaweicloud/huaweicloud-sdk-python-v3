# coding: utf-8

import pprint
import re

import six





class CreateWhitelistReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'listener_id': 'str',
        'enable_whitelist': 'bool',
        'whitelist': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'listener_id': 'listener_id',
        'enable_whitelist': 'enable_whitelist',
        'whitelist': 'whitelist'
    }

    def __init__(self, tenant_id=None, listener_id=None, enable_whitelist=None, whitelist=None):
        """CreateWhitelistReq - a model defined in huaweicloud sdk"""
        
        

        self._tenant_id = None
        self._listener_id = None
        self._enable_whitelist = None
        self._whitelist = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.listener_id = listener_id
        if enable_whitelist is not None:
            self.enable_whitelist = enable_whitelist
        if whitelist is not None:
            self.whitelist = whitelist

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreateWhitelistReq.

        白名单所在的项目ID

        :return: The tenant_id of this CreateWhitelistReq.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreateWhitelistReq.

        白名单所在的项目ID

        :param tenant_id: The tenant_id of this CreateWhitelistReq.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def listener_id(self):
        """Gets the listener_id of this CreateWhitelistReq.

        白名单关联的监听器ID

        :return: The listener_id of this CreateWhitelistReq.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this CreateWhitelistReq.

        白名单关联的监听器ID

        :param listener_id: The listener_id of this CreateWhitelistReq.
        :type: str
        """
        self._listener_id = listener_id

    @property
    def enable_whitelist(self):
        """Gets the enable_whitelist of this CreateWhitelistReq.

        是否开启白名单访问控制开关。true：开启；false：关闭

        :return: The enable_whitelist of this CreateWhitelistReq.
        :rtype: bool
        """
        return self._enable_whitelist

    @enable_whitelist.setter
    def enable_whitelist(self, enable_whitelist):
        """Sets the enable_whitelist of this CreateWhitelistReq.

        是否开启白名单访问控制开关。true：开启；false：关闭

        :param enable_whitelist: The enable_whitelist of this CreateWhitelistReq.
        :type: bool
        """
        self._enable_whitelist = enable_whitelist

    @property
    def whitelist(self):
        """Gets the whitelist of this CreateWhitelistReq.

        白名单IP列表。可以是ip，例如192.168.10.123；也可以是一个网段，例如192.168.10.1/24；不同的值之间用逗号分隔

        :return: The whitelist of this CreateWhitelistReq.
        :rtype: str
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this CreateWhitelistReq.

        白名单IP列表。可以是ip，例如192.168.10.123；也可以是一个网段，例如192.168.10.1/24；不同的值之间用逗号分隔

        :param whitelist: The whitelist of this CreateWhitelistReq.
        :type: str
        """
        self._whitelist = whitelist

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateWhitelistReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
