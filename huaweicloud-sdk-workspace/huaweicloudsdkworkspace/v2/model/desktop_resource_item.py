# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopResourceItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_package_name': 'str',
        'desktop_resource_spec_code': 'str',
        'resource_spec_code': 'str',
        'effective_time': 'str',
        'is_auto_renew': 'int'
    }

    attribute_map = {
        'resource_package_name': 'resource_package_name',
        'desktop_resource_spec_code': 'desktop_resource_spec_code',
        'resource_spec_code': 'resource_spec_code',
        'effective_time': 'effective_time',
        'is_auto_renew': 'is_auto_renew'
    }

    def __init__(self, resource_package_name=None, desktop_resource_spec_code=None, resource_spec_code=None, effective_time=None, is_auto_renew=None):
        r"""DesktopResourceItem

        The model defined in huaweicloud sdk

        :param resource_package_name: 资源包名称。
        :type resource_package_name: str
        :param desktop_resource_spec_code: 桌面产品编码。
        :type desktop_resource_spec_code: str
        :param resource_spec_code: 资源包产品编码。
        :type resource_spec_code: str
        :param effective_time: 生效时间，格式：yyyy-MM-ddTHH:mm:ssZ（2025-04-12T17:30:00Z）。
        :type effective_time: str
        :param is_auto_renew: 是否自动续订。
        :type is_auto_renew: int
        """
        
        

        self._resource_package_name = None
        self._desktop_resource_spec_code = None
        self._resource_spec_code = None
        self._effective_time = None
        self._is_auto_renew = None
        self.discriminator = None

        self.resource_package_name = resource_package_name
        self.desktop_resource_spec_code = desktop_resource_spec_code
        self.resource_spec_code = resource_spec_code
        if effective_time is not None:
            self.effective_time = effective_time
        if is_auto_renew is not None:
            self.is_auto_renew = is_auto_renew

    @property
    def resource_package_name(self):
        r"""Gets the resource_package_name of this DesktopResourceItem.

        资源包名称。

        :return: The resource_package_name of this DesktopResourceItem.
        :rtype: str
        """
        return self._resource_package_name

    @resource_package_name.setter
    def resource_package_name(self, resource_package_name):
        r"""Sets the resource_package_name of this DesktopResourceItem.

        资源包名称。

        :param resource_package_name: The resource_package_name of this DesktopResourceItem.
        :type resource_package_name: str
        """
        self._resource_package_name = resource_package_name

    @property
    def desktop_resource_spec_code(self):
        r"""Gets the desktop_resource_spec_code of this DesktopResourceItem.

        桌面产品编码。

        :return: The desktop_resource_spec_code of this DesktopResourceItem.
        :rtype: str
        """
        return self._desktop_resource_spec_code

    @desktop_resource_spec_code.setter
    def desktop_resource_spec_code(self, desktop_resource_spec_code):
        r"""Sets the desktop_resource_spec_code of this DesktopResourceItem.

        桌面产品编码。

        :param desktop_resource_spec_code: The desktop_resource_spec_code of this DesktopResourceItem.
        :type desktop_resource_spec_code: str
        """
        self._desktop_resource_spec_code = desktop_resource_spec_code

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this DesktopResourceItem.

        资源包产品编码。

        :return: The resource_spec_code of this DesktopResourceItem.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this DesktopResourceItem.

        资源包产品编码。

        :param resource_spec_code: The resource_spec_code of this DesktopResourceItem.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def effective_time(self):
        r"""Gets the effective_time of this DesktopResourceItem.

        生效时间，格式：yyyy-MM-ddTHH:mm:ssZ（2025-04-12T17:30:00Z）。

        :return: The effective_time of this DesktopResourceItem.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this DesktopResourceItem.

        生效时间，格式：yyyy-MM-ddTHH:mm:ssZ（2025-04-12T17:30:00Z）。

        :param effective_time: The effective_time of this DesktopResourceItem.
        :type effective_time: str
        """
        self._effective_time = effective_time

    @property
    def is_auto_renew(self):
        r"""Gets the is_auto_renew of this DesktopResourceItem.

        是否自动续订。

        :return: The is_auto_renew of this DesktopResourceItem.
        :rtype: int
        """
        return self._is_auto_renew

    @is_auto_renew.setter
    def is_auto_renew(self, is_auto_renew):
        r"""Sets the is_auto_renew of this DesktopResourceItem.

        是否自动续订。

        :param is_auto_renew: The is_auto_renew of this DesktopResourceItem.
        :type is_auto_renew: int
        """
        self._is_auto_renew = is_auto_renew

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DesktopResourceItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
