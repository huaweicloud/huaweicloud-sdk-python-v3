# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WhitelistResp:

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
        'tenant_id': 'str',
        'listener_id': 'str',
        'enable_whitelist': 'bool',
        'whitelist': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'listener_id': 'listener_id',
        'enable_whitelist': 'enable_whitelist',
        'whitelist': 'whitelist'
    }

    def __init__(self, id=None, tenant_id=None, listener_id=None, enable_whitelist=None, whitelist=None):
        r"""WhitelistResp

        The model defined in huaweicloud sdk

        :param id: 白名单id
        :type id: str
        :param tenant_id: 白名单所在的项目ID
        :type tenant_id: str
        :param listener_id: 白名单关联的监听器ID
        :type listener_id: str
        :param enable_whitelist: 是否开启白名单访问控制开关。true：开启；false：关闭
        :type enable_whitelist: bool
        :param whitelist: 白名单IP列表。可以是ip，例如192.168.10.123；也可以是一个网段，例如192.168.10.1/24；不同的值之间用逗号分隔
        :type whitelist: str
        """
        
        

        self._id = None
        self._tenant_id = None
        self._listener_id = None
        self._enable_whitelist = None
        self._whitelist = None
        self.discriminator = None

        self.id = id
        self.tenant_id = tenant_id
        self.listener_id = listener_id
        self.enable_whitelist = enable_whitelist
        self.whitelist = whitelist

    @property
    def id(self):
        r"""Gets the id of this WhitelistResp.

        白名单id

        :return: The id of this WhitelistResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WhitelistResp.

        白名单id

        :param id: The id of this WhitelistResp.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this WhitelistResp.

        白名单所在的项目ID

        :return: The tenant_id of this WhitelistResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this WhitelistResp.

        白名单所在的项目ID

        :param tenant_id: The tenant_id of this WhitelistResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def listener_id(self):
        r"""Gets the listener_id of this WhitelistResp.

        白名单关联的监听器ID

        :return: The listener_id of this WhitelistResp.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this WhitelistResp.

        白名单关联的监听器ID

        :param listener_id: The listener_id of this WhitelistResp.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def enable_whitelist(self):
        r"""Gets the enable_whitelist of this WhitelistResp.

        是否开启白名单访问控制开关。true：开启；false：关闭

        :return: The enable_whitelist of this WhitelistResp.
        :rtype: bool
        """
        return self._enable_whitelist

    @enable_whitelist.setter
    def enable_whitelist(self, enable_whitelist):
        r"""Sets the enable_whitelist of this WhitelistResp.

        是否开启白名单访问控制开关。true：开启；false：关闭

        :param enable_whitelist: The enable_whitelist of this WhitelistResp.
        :type enable_whitelist: bool
        """
        self._enable_whitelist = enable_whitelist

    @property
    def whitelist(self):
        r"""Gets the whitelist of this WhitelistResp.

        白名单IP列表。可以是ip，例如192.168.10.123；也可以是一个网段，例如192.168.10.1/24；不同的值之间用逗号分隔

        :return: The whitelist of this WhitelistResp.
        :rtype: str
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        r"""Sets the whitelist of this WhitelistResp.

        白名单IP列表。可以是ip，例如192.168.10.123；也可以是一个网段，例如192.168.10.1/24；不同的值之间用逗号分隔

        :param whitelist: The whitelist of this WhitelistResp.
        :type whitelist: str
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
        if not isinstance(other, WhitelistResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
