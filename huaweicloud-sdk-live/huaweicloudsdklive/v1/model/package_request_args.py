# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackageRequestArgs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record': 'list[RecordRequestArgs]',
        'timeshift': 'list[TimeshiftRequestArgs]',
        'live': 'list[LiveRequestArgs]'
    }

    attribute_map = {
        'record': 'record',
        'timeshift': 'timeshift',
        'live': 'live'
    }

    def __init__(self, record=None, timeshift=None, live=None):
        r"""PackageRequestArgs

        The model defined in huaweicloud sdk

        :param record: 录制播放相关配置
        :type record: list[:class:`huaweicloudsdklive.v1.RecordRequestArgs`]
        :param timeshift: 时移播放相关配置
        :type timeshift: list[:class:`huaweicloudsdklive.v1.TimeshiftRequestArgs`]
        :param live: 直播播放相关配置
        :type live: list[:class:`huaweicloudsdklive.v1.LiveRequestArgs`]
        """
        
        

        self._record = None
        self._timeshift = None
        self._live = None
        self.discriminator = None

        if record is not None:
            self.record = record
        if timeshift is not None:
            self.timeshift = timeshift
        if live is not None:
            self.live = live

    @property
    def record(self):
        r"""Gets the record of this PackageRequestArgs.

        录制播放相关配置

        :return: The record of this PackageRequestArgs.
        :rtype: list[:class:`huaweicloudsdklive.v1.RecordRequestArgs`]
        """
        return self._record

    @record.setter
    def record(self, record):
        r"""Sets the record of this PackageRequestArgs.

        录制播放相关配置

        :param record: The record of this PackageRequestArgs.
        :type record: list[:class:`huaweicloudsdklive.v1.RecordRequestArgs`]
        """
        self._record = record

    @property
    def timeshift(self):
        r"""Gets the timeshift of this PackageRequestArgs.

        时移播放相关配置

        :return: The timeshift of this PackageRequestArgs.
        :rtype: list[:class:`huaweicloudsdklive.v1.TimeshiftRequestArgs`]
        """
        return self._timeshift

    @timeshift.setter
    def timeshift(self, timeshift):
        r"""Sets the timeshift of this PackageRequestArgs.

        时移播放相关配置

        :param timeshift: The timeshift of this PackageRequestArgs.
        :type timeshift: list[:class:`huaweicloudsdklive.v1.TimeshiftRequestArgs`]
        """
        self._timeshift = timeshift

    @property
    def live(self):
        r"""Gets the live of this PackageRequestArgs.

        直播播放相关配置

        :return: The live of this PackageRequestArgs.
        :rtype: list[:class:`huaweicloudsdklive.v1.LiveRequestArgs`]
        """
        return self._live

    @live.setter
    def live(self, live):
        r"""Sets the live of this PackageRequestArgs.

        直播播放相关配置

        :param live: The live of this PackageRequestArgs.
        :type live: list[:class:`huaweicloudsdklive.v1.LiveRequestArgs`]
        """
        self._live = live

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
        if not isinstance(other, PackageRequestArgs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
