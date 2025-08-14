# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserAssignmentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_system_quota': 'int',
        'action_put': 'bool',
        'action_get': 'bool',
        'roam_action_put': 'bool',
        'roam_action_get': 'bool'
    }

    attribute_map = {
        'file_system_quota': 'file_system_quota',
        'action_put': 'action_put',
        'action_get': 'action_get',
        'roam_action_put': 'roam_action_put',
        'roam_action_get': 'roam_action_get'
    }

    def __init__(self, file_system_quota=None, action_put=None, action_get=None, roam_action_put=None, roam_action_get=None):
        r"""UpdateUserAssignmentInfo

        The model defined in huaweicloud sdk

        :param file_system_quota: 配额。
        :type file_system_quota: int
        :param action_put: 云存储于本地设备的权限，上传： true : 允许上传。 false: 不允许上传。
        :type action_put: bool
        :param action_get: 云存储于本地设备的权限，下载： true : 允许下载。 false: 不允许下载。
        :type action_get: bool
        :param roam_action_put: 云存储于云桌面/云应用权限，上传： true : 允许上传。 false: 不允许上传。
        :type roam_action_put: bool
        :param roam_action_get: 云存储于云桌面/云应用权限，下载： true : 允许下载。 false: 不允许下载。
        :type roam_action_get: bool
        """
        
        

        self._file_system_quota = None
        self._action_put = None
        self._action_get = None
        self._roam_action_put = None
        self._roam_action_get = None
        self.discriminator = None

        if file_system_quota is not None:
            self.file_system_quota = file_system_quota
        if action_put is not None:
            self.action_put = action_put
        if action_get is not None:
            self.action_get = action_get
        if roam_action_put is not None:
            self.roam_action_put = roam_action_put
        if roam_action_get is not None:
            self.roam_action_get = roam_action_get

    @property
    def file_system_quota(self):
        r"""Gets the file_system_quota of this UpdateUserAssignmentInfo.

        配额。

        :return: The file_system_quota of this UpdateUserAssignmentInfo.
        :rtype: int
        """
        return self._file_system_quota

    @file_system_quota.setter
    def file_system_quota(self, file_system_quota):
        r"""Sets the file_system_quota of this UpdateUserAssignmentInfo.

        配额。

        :param file_system_quota: The file_system_quota of this UpdateUserAssignmentInfo.
        :type file_system_quota: int
        """
        self._file_system_quota = file_system_quota

    @property
    def action_put(self):
        r"""Gets the action_put of this UpdateUserAssignmentInfo.

        云存储于本地设备的权限，上传： true : 允许上传。 false: 不允许上传。

        :return: The action_put of this UpdateUserAssignmentInfo.
        :rtype: bool
        """
        return self._action_put

    @action_put.setter
    def action_put(self, action_put):
        r"""Sets the action_put of this UpdateUserAssignmentInfo.

        云存储于本地设备的权限，上传： true : 允许上传。 false: 不允许上传。

        :param action_put: The action_put of this UpdateUserAssignmentInfo.
        :type action_put: bool
        """
        self._action_put = action_put

    @property
    def action_get(self):
        r"""Gets the action_get of this UpdateUserAssignmentInfo.

        云存储于本地设备的权限，下载： true : 允许下载。 false: 不允许下载。

        :return: The action_get of this UpdateUserAssignmentInfo.
        :rtype: bool
        """
        return self._action_get

    @action_get.setter
    def action_get(self, action_get):
        r"""Sets the action_get of this UpdateUserAssignmentInfo.

        云存储于本地设备的权限，下载： true : 允许下载。 false: 不允许下载。

        :param action_get: The action_get of this UpdateUserAssignmentInfo.
        :type action_get: bool
        """
        self._action_get = action_get

    @property
    def roam_action_put(self):
        r"""Gets the roam_action_put of this UpdateUserAssignmentInfo.

        云存储于云桌面/云应用权限，上传： true : 允许上传。 false: 不允许上传。

        :return: The roam_action_put of this UpdateUserAssignmentInfo.
        :rtype: bool
        """
        return self._roam_action_put

    @roam_action_put.setter
    def roam_action_put(self, roam_action_put):
        r"""Sets the roam_action_put of this UpdateUserAssignmentInfo.

        云存储于云桌面/云应用权限，上传： true : 允许上传。 false: 不允许上传。

        :param roam_action_put: The roam_action_put of this UpdateUserAssignmentInfo.
        :type roam_action_put: bool
        """
        self._roam_action_put = roam_action_put

    @property
    def roam_action_get(self):
        r"""Gets the roam_action_get of this UpdateUserAssignmentInfo.

        云存储于云桌面/云应用权限，下载： true : 允许下载。 false: 不允许下载。

        :return: The roam_action_get of this UpdateUserAssignmentInfo.
        :rtype: bool
        """
        return self._roam_action_get

    @roam_action_get.setter
    def roam_action_get(self, roam_action_get):
        r"""Sets the roam_action_get of this UpdateUserAssignmentInfo.

        云存储于云桌面/云应用权限，下载： true : 允许下载。 false: 不允许下载。

        :param roam_action_get: The roam_action_get of this UpdateUserAssignmentInfo.
        :type roam_action_get: bool
        """
        self._roam_action_get = roam_action_get

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
        if not isinstance(other, UpdateUserAssignmentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
