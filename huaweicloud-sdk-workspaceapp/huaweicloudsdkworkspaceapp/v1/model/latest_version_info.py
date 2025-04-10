# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LatestVersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'latest_version': 'str',
        'hda_type': 'str'
    }

    attribute_map = {
        'latest_version': 'latest_version',
        'hda_type': 'hda_type'
    }

    def __init__(self, latest_version=None, hda_type=None):
        r"""LatestVersionInfo

        The model defined in huaweicloud sdk

        :param latest_version: 租户的HDP最新版本。
        :type latest_version: str
        :param hda_type: HDA类型： * &#x60;SBC&#x60; - 非VDI下SBC类型 * &#x60;OA_APP&#x60; - VDI下非GPU类型 * &#x60;PT_APP&#x60; - VDI下GPU类型
        :type hda_type: str
        """
        
        

        self._latest_version = None
        self._hda_type = None
        self.discriminator = None

        if latest_version is not None:
            self.latest_version = latest_version
        if hda_type is not None:
            self.hda_type = hda_type

    @property
    def latest_version(self):
        r"""Gets the latest_version of this LatestVersionInfo.

        租户的HDP最新版本。

        :return: The latest_version of this LatestVersionInfo.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this LatestVersionInfo.

        租户的HDP最新版本。

        :param latest_version: The latest_version of this LatestVersionInfo.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def hda_type(self):
        r"""Gets the hda_type of this LatestVersionInfo.

        HDA类型： * `SBC` - 非VDI下SBC类型 * `OA_APP` - VDI下非GPU类型 * `PT_APP` - VDI下GPU类型

        :return: The hda_type of this LatestVersionInfo.
        :rtype: str
        """
        return self._hda_type

    @hda_type.setter
    def hda_type(self, hda_type):
        r"""Sets the hda_type of this LatestVersionInfo.

        HDA类型： * `SBC` - 非VDI下SBC类型 * `OA_APP` - VDI下非GPU类型 * `PT_APP` - VDI下GPU类型

        :param hda_type: The hda_type of this LatestVersionInfo.
        :type hda_type: str
        """
        self._hda_type = hda_type

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
        if not isinstance(other, LatestVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
