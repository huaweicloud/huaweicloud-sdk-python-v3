# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopSysprepInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'sysprep_version': 'str',
        'support_hibernate': 'bool',
        'support_update_route': 'bool'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'sysprep_version': 'sysprep_version',
        'support_hibernate': 'support_hibernate',
        'support_update_route': 'support_update_route'
    }

    def __init__(self, desktop_id=None, sysprep_version=None, support_hibernate=None, support_update_route=None):
        r"""DesktopSysprepInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面id。
        :type desktop_id: str
        :param sysprep_version: sysprep版本。
        :type sysprep_version: str
        :param support_hibernate: 是否支持休眠。
        :type support_hibernate: bool
        :param support_update_route: 是否支持修改路由。
        :type support_update_route: bool
        """
        
        

        self._desktop_id = None
        self._sysprep_version = None
        self._support_hibernate = None
        self._support_update_route = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if sysprep_version is not None:
            self.sysprep_version = sysprep_version
        if support_hibernate is not None:
            self.support_hibernate = support_hibernate
        if support_update_route is not None:
            self.support_update_route = support_update_route

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this DesktopSysprepInfo.

        桌面id。

        :return: The desktop_id of this DesktopSysprepInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this DesktopSysprepInfo.

        桌面id。

        :param desktop_id: The desktop_id of this DesktopSysprepInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def sysprep_version(self):
        r"""Gets the sysprep_version of this DesktopSysprepInfo.

        sysprep版本。

        :return: The sysprep_version of this DesktopSysprepInfo.
        :rtype: str
        """
        return self._sysprep_version

    @sysprep_version.setter
    def sysprep_version(self, sysprep_version):
        r"""Sets the sysprep_version of this DesktopSysprepInfo.

        sysprep版本。

        :param sysprep_version: The sysprep_version of this DesktopSysprepInfo.
        :type sysprep_version: str
        """
        self._sysprep_version = sysprep_version

    @property
    def support_hibernate(self):
        r"""Gets the support_hibernate of this DesktopSysprepInfo.

        是否支持休眠。

        :return: The support_hibernate of this DesktopSysprepInfo.
        :rtype: bool
        """
        return self._support_hibernate

    @support_hibernate.setter
    def support_hibernate(self, support_hibernate):
        r"""Sets the support_hibernate of this DesktopSysprepInfo.

        是否支持休眠。

        :param support_hibernate: The support_hibernate of this DesktopSysprepInfo.
        :type support_hibernate: bool
        """
        self._support_hibernate = support_hibernate

    @property
    def support_update_route(self):
        r"""Gets the support_update_route of this DesktopSysprepInfo.

        是否支持修改路由。

        :return: The support_update_route of this DesktopSysprepInfo.
        :rtype: bool
        """
        return self._support_update_route

    @support_update_route.setter
    def support_update_route(self, support_update_route):
        r"""Sets the support_update_route of this DesktopSysprepInfo.

        是否支持修改路由。

        :param support_update_route: The support_update_route of this DesktopSysprepInfo.
        :type support_update_route: bool
        """
        self._support_update_route = support_update_route

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
        if not isinstance(other, DesktopSysprepInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
