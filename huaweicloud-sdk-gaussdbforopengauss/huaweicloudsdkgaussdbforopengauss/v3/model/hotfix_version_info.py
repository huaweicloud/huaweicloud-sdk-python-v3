# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HotfixVersionInfo:

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
        'upgrade_finished_time': 'str'
    }

    attribute_map = {
        'version': 'version',
        'upgrade_finished_time': 'upgrade_finished_time'
    }

    def __init__(self, version=None, upgrade_finished_time=None):
        r"""HotfixVersionInfo

        The model defined in huaweicloud sdk

        :param version: 热补丁版本。
        :type version: str
        :param upgrade_finished_time: 热补丁升级完成时间列表。  热补丁升级完成时间，格式为“yyyy-mm-dd hh:mm:ss timezone”。  其中timezone是指时区。
        :type upgrade_finished_time: str
        """
        
        

        self._version = None
        self._upgrade_finished_time = None
        self.discriminator = None

        self.version = version
        if upgrade_finished_time is not None:
            self.upgrade_finished_time = upgrade_finished_time

    @property
    def version(self):
        r"""Gets the version of this HotfixVersionInfo.

        热补丁版本。

        :return: The version of this HotfixVersionInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this HotfixVersionInfo.

        热补丁版本。

        :param version: The version of this HotfixVersionInfo.
        :type version: str
        """
        self._version = version

    @property
    def upgrade_finished_time(self):
        r"""Gets the upgrade_finished_time of this HotfixVersionInfo.

        热补丁升级完成时间列表。  热补丁升级完成时间，格式为“yyyy-mm-dd hh:mm:ss timezone”。  其中timezone是指时区。

        :return: The upgrade_finished_time of this HotfixVersionInfo.
        :rtype: str
        """
        return self._upgrade_finished_time

    @upgrade_finished_time.setter
    def upgrade_finished_time(self, upgrade_finished_time):
        r"""Sets the upgrade_finished_time of this HotfixVersionInfo.

        热补丁升级完成时间列表。  热补丁升级完成时间，格式为“yyyy-mm-dd hh:mm:ss timezone”。  其中timezone是指时区。

        :param upgrade_finished_time: The upgrade_finished_time of this HotfixVersionInfo.
        :type upgrade_finished_time: str
        """
        self._upgrade_finished_time = upgrade_finished_time

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
        if not isinstance(other, HotfixVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
