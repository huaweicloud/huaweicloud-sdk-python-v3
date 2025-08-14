# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudStorageAssignment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_storage_assignment_id': 'str',
        'attach_name': 'str',
        'used_quota': 'int',
        'quota': 'int',
        'create_time': 'datetime',
        'action_put': 'bool',
        'action_get': 'bool',
        'roam_action_put': 'bool',
        'roam_action_get': 'bool'
    }

    attribute_map = {
        'cloud_storage_assignment_id': 'cloud_storage_assignment_id',
        'attach_name': 'attach_name',
        'used_quota': 'used_quota',
        'quota': 'quota',
        'create_time': 'create_time',
        'action_put': 'action_put',
        'action_get': 'action_get',
        'roam_action_put': 'roam_action_put',
        'roam_action_get': 'roam_action_get'
    }

    def __init__(self, cloud_storage_assignment_id=None, attach_name=None, used_quota=None, quota=None, create_time=None, action_put=None, action_get=None, roam_action_put=None, roam_action_get=None):
        r"""CloudStorageAssignment

        The model defined in huaweicloud sdk

        :param cloud_storage_assignment_id: id。
        :type cloud_storage_assignment_id: str
        :param attach_name: 用户名称(单位/B)。
        :type attach_name: str
        :param used_quota: 已用容量(单位/B)。
        :type used_quota: int
        :param quota: 总容量(单位/B)。
        :type quota: int
        :param create_time: 添加时间。
        :type create_time: datetime
        :param action_put: 云存储于本地设备的权限，上传： true : 允许上传。 false: 不允许上传。
        :type action_put: bool
        :param action_get: 云存储于本地设备的权限，下载： true : 允许下载。 false: 不允许下载。
        :type action_get: bool
        :param roam_action_put: 云存储于云桌面/云应用权限，上传： true : 允许上传。 false: 不允许上传。
        :type roam_action_put: bool
        :param roam_action_get: 云存储于云桌面/云应用权限，下载： true : 允许下载。 false: 不允许下载。
        :type roam_action_get: bool
        """
        
        

        self._cloud_storage_assignment_id = None
        self._attach_name = None
        self._used_quota = None
        self._quota = None
        self._create_time = None
        self._action_put = None
        self._action_get = None
        self._roam_action_put = None
        self._roam_action_get = None
        self.discriminator = None

        if cloud_storage_assignment_id is not None:
            self.cloud_storage_assignment_id = cloud_storage_assignment_id
        if attach_name is not None:
            self.attach_name = attach_name
        if used_quota is not None:
            self.used_quota = used_quota
        if quota is not None:
            self.quota = quota
        if create_time is not None:
            self.create_time = create_time
        if action_put is not None:
            self.action_put = action_put
        if action_get is not None:
            self.action_get = action_get
        if roam_action_put is not None:
            self.roam_action_put = roam_action_put
        if roam_action_get is not None:
            self.roam_action_get = roam_action_get

    @property
    def cloud_storage_assignment_id(self):
        r"""Gets the cloud_storage_assignment_id of this CloudStorageAssignment.

        id。

        :return: The cloud_storage_assignment_id of this CloudStorageAssignment.
        :rtype: str
        """
        return self._cloud_storage_assignment_id

    @cloud_storage_assignment_id.setter
    def cloud_storage_assignment_id(self, cloud_storage_assignment_id):
        r"""Sets the cloud_storage_assignment_id of this CloudStorageAssignment.

        id。

        :param cloud_storage_assignment_id: The cloud_storage_assignment_id of this CloudStorageAssignment.
        :type cloud_storage_assignment_id: str
        """
        self._cloud_storage_assignment_id = cloud_storage_assignment_id

    @property
    def attach_name(self):
        r"""Gets the attach_name of this CloudStorageAssignment.

        用户名称(单位/B)。

        :return: The attach_name of this CloudStorageAssignment.
        :rtype: str
        """
        return self._attach_name

    @attach_name.setter
    def attach_name(self, attach_name):
        r"""Sets the attach_name of this CloudStorageAssignment.

        用户名称(单位/B)。

        :param attach_name: The attach_name of this CloudStorageAssignment.
        :type attach_name: str
        """
        self._attach_name = attach_name

    @property
    def used_quota(self):
        r"""Gets the used_quota of this CloudStorageAssignment.

        已用容量(单位/B)。

        :return: The used_quota of this CloudStorageAssignment.
        :rtype: int
        """
        return self._used_quota

    @used_quota.setter
    def used_quota(self, used_quota):
        r"""Sets the used_quota of this CloudStorageAssignment.

        已用容量(单位/B)。

        :param used_quota: The used_quota of this CloudStorageAssignment.
        :type used_quota: int
        """
        self._used_quota = used_quota

    @property
    def quota(self):
        r"""Gets the quota of this CloudStorageAssignment.

        总容量(单位/B)。

        :return: The quota of this CloudStorageAssignment.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this CloudStorageAssignment.

        总容量(单位/B)。

        :param quota: The quota of this CloudStorageAssignment.
        :type quota: int
        """
        self._quota = quota

    @property
    def create_time(self):
        r"""Gets the create_time of this CloudStorageAssignment.

        添加时间。

        :return: The create_time of this CloudStorageAssignment.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CloudStorageAssignment.

        添加时间。

        :param create_time: The create_time of this CloudStorageAssignment.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def action_put(self):
        r"""Gets the action_put of this CloudStorageAssignment.

        云存储于本地设备的权限，上传： true : 允许上传。 false: 不允许上传。

        :return: The action_put of this CloudStorageAssignment.
        :rtype: bool
        """
        return self._action_put

    @action_put.setter
    def action_put(self, action_put):
        r"""Sets the action_put of this CloudStorageAssignment.

        云存储于本地设备的权限，上传： true : 允许上传。 false: 不允许上传。

        :param action_put: The action_put of this CloudStorageAssignment.
        :type action_put: bool
        """
        self._action_put = action_put

    @property
    def action_get(self):
        r"""Gets the action_get of this CloudStorageAssignment.

        云存储于本地设备的权限，下载： true : 允许下载。 false: 不允许下载。

        :return: The action_get of this CloudStorageAssignment.
        :rtype: bool
        """
        return self._action_get

    @action_get.setter
    def action_get(self, action_get):
        r"""Sets the action_get of this CloudStorageAssignment.

        云存储于本地设备的权限，下载： true : 允许下载。 false: 不允许下载。

        :param action_get: The action_get of this CloudStorageAssignment.
        :type action_get: bool
        """
        self._action_get = action_get

    @property
    def roam_action_put(self):
        r"""Gets the roam_action_put of this CloudStorageAssignment.

        云存储于云桌面/云应用权限，上传： true : 允许上传。 false: 不允许上传。

        :return: The roam_action_put of this CloudStorageAssignment.
        :rtype: bool
        """
        return self._roam_action_put

    @roam_action_put.setter
    def roam_action_put(self, roam_action_put):
        r"""Sets the roam_action_put of this CloudStorageAssignment.

        云存储于云桌面/云应用权限，上传： true : 允许上传。 false: 不允许上传。

        :param roam_action_put: The roam_action_put of this CloudStorageAssignment.
        :type roam_action_put: bool
        """
        self._roam_action_put = roam_action_put

    @property
    def roam_action_get(self):
        r"""Gets the roam_action_get of this CloudStorageAssignment.

        云存储于云桌面/云应用权限，下载： true : 允许下载。 false: 不允许下载。

        :return: The roam_action_get of this CloudStorageAssignment.
        :rtype: bool
        """
        return self._roam_action_get

    @roam_action_get.setter
    def roam_action_get(self, roam_action_get):
        r"""Sets the roam_action_get of this CloudStorageAssignment.

        云存储于云桌面/云应用权限，下载： true : 允许下载。 false: 不允许下载。

        :param roam_action_get: The roam_action_get of this CloudStorageAssignment.
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
        if not isinstance(other, CloudStorageAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
