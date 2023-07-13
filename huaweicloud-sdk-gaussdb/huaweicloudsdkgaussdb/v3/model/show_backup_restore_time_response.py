# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupRestoreTimeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_times': 'list[RestoreTimeInfo]'
    }

    attribute_map = {
        'restore_times': 'restore_times'
    }

    def __init__(self, restore_times=None):
        """ShowBackupRestoreTimeResponse

        The model defined in huaweicloud sdk

        :param restore_times: 可恢复时间段列表。
        :type restore_times: list[:class:`huaweicloudsdkgaussdb.v3.RestoreTimeInfo`]
        """
        
        super(ShowBackupRestoreTimeResponse, self).__init__()

        self._restore_times = None
        self.discriminator = None

        if restore_times is not None:
            self.restore_times = restore_times

    @property
    def restore_times(self):
        """Gets the restore_times of this ShowBackupRestoreTimeResponse.

        可恢复时间段列表。

        :return: The restore_times of this ShowBackupRestoreTimeResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.RestoreTimeInfo`]
        """
        return self._restore_times

    @restore_times.setter
    def restore_times(self, restore_times):
        """Sets the restore_times of this ShowBackupRestoreTimeResponse.

        可恢复时间段列表。

        :param restore_times: The restore_times of this ShowBackupRestoreTimeResponse.
        :type restore_times: list[:class:`huaweicloudsdkgaussdb.v3.RestoreTimeInfo`]
        """
        self._restore_times = restore_times

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
        if not isinstance(other, ShowBackupRestoreTimeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
