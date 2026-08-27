# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopVersionStatistic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'os_type': 'str',
        'desktop_count': 'int'
    }

    attribute_map = {
        'version': 'version',
        'os_type': 'os_type',
        'desktop_count': 'desktop_count'
    }

    def __init__(self, version=None, os_type=None, desktop_count=None):
        r"""DesktopVersionStatistic

        The model defined in huaweicloud sdk

        :param version: 桌面版本号。
        :type version: str
        :param os_type: 操作系统。
        :type os_type: str
        :param desktop_count: 该版本下的桌面数量。
        :type desktop_count: int
        """
        
        

        self._version = None
        self._os_type = None
        self._desktop_count = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if os_type is not None:
            self.os_type = os_type
        if desktop_count is not None:
            self.desktop_count = desktop_count

    @property
    def version(self):
        r"""Gets the version of this DesktopVersionStatistic.

        桌面版本号。

        :return: The version of this DesktopVersionStatistic.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this DesktopVersionStatistic.

        桌面版本号。

        :param version: The version of this DesktopVersionStatistic.
        :type version: str
        """
        self._version = version

    @property
    def os_type(self):
        r"""Gets the os_type of this DesktopVersionStatistic.

        操作系统。

        :return: The os_type of this DesktopVersionStatistic.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this DesktopVersionStatistic.

        操作系统。

        :param os_type: The os_type of this DesktopVersionStatistic.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def desktop_count(self):
        r"""Gets the desktop_count of this DesktopVersionStatistic.

        该版本下的桌面数量。

        :return: The desktop_count of this DesktopVersionStatistic.
        :rtype: int
        """
        return self._desktop_count

    @desktop_count.setter
    def desktop_count(self, desktop_count):
        r"""Sets the desktop_count of this DesktopVersionStatistic.

        该版本下的桌面数量。

        :param desktop_count: The desktop_count of this DesktopVersionStatistic.
        :type desktop_count: int
        """
        self._desktop_count = desktop_count

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
        if not isinstance(other, DesktopVersionStatistic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
