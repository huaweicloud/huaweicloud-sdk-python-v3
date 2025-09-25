# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'release_version': 'str',
        'release_note': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'release_version': 'release_version',
        'release_note': 'release_note',
        'update_time': 'update_time'
    }

    def __init__(self, release_version=None, release_note=None, update_time=None):
        r"""VersionList

        The model defined in huaweicloud sdk

        :param release_version: 版本号
        :type release_version: str
        :param release_note: 版本说明
        :type release_note: str
        :param update_time: 更新时间，毫秒
        :type update_time: int
        """
        
        

        self._release_version = None
        self._release_note = None
        self._update_time = None
        self.discriminator = None

        if release_version is not None:
            self.release_version = release_version
        if release_note is not None:
            self.release_note = release_note
        if update_time is not None:
            self.update_time = update_time

    @property
    def release_version(self):
        r"""Gets the release_version of this VersionList.

        版本号

        :return: The release_version of this VersionList.
        :rtype: str
        """
        return self._release_version

    @release_version.setter
    def release_version(self, release_version):
        r"""Sets the release_version of this VersionList.

        版本号

        :param release_version: The release_version of this VersionList.
        :type release_version: str
        """
        self._release_version = release_version

    @property
    def release_note(self):
        r"""Gets the release_note of this VersionList.

        版本说明

        :return: The release_note of this VersionList.
        :rtype: str
        """
        return self._release_note

    @release_note.setter
    def release_note(self, release_note):
        r"""Sets the release_note of this VersionList.

        版本说明

        :param release_note: The release_note of this VersionList.
        :type release_note: str
        """
        self._release_note = release_note

    @property
    def update_time(self):
        r"""Gets the update_time of this VersionList.

        更新时间，毫秒

        :return: The update_time of this VersionList.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this VersionList.

        更新时间，毫秒

        :param update_time: The update_time of this VersionList.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, VersionList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
