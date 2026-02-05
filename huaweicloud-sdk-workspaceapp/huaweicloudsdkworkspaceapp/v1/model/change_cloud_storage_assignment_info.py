# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeCloudStorageAssignmentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'attach_id': 'str',
        'attach': 'str',
        'quota': 'int',
        'action_put': 'bool',
        'action_get': 'bool',
        'roam_action_put': 'bool',
        'roam_action_get': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'attach_id': 'attach_id',
        'attach': 'attach',
        'quota': 'quota',
        'action_put': 'action_put',
        'action_get': 'action_get',
        'roam_action_put': 'roam_action_put',
        'roam_action_get': 'roam_action_get'
    }

    def __init__(self, id=None, attach_id=None, attach=None, quota=None, action_put=None, action_get=None, roam_action_put=None, roam_action_get=None):
        r"""ChangeCloudStorageAssignmentInfo

        The model defined in huaweicloud sdk

        :param id: 存储分配的唯一标识符。
        :type id: str
        :param attach_id: 目标用户id。
        :type attach_id: str
        :param attach: 目标用户。
        :type attach: str
        :param quota: 配额。
        :type quota: int
        :param action_put: 云存储于本地设备的权限，上传： true : 允许上传。 false: 不允许上传。
        :type action_put: bool
        :param action_get: 云存储于本地设备的权限，下载： true : 允许下载。 false: 不允许下载。
        :type action_get: bool
        :param roam_action_put: 云存储于云桌面/云应用权限，上传： true : 允许上传。 false: 不允许上传。
        :type roam_action_put: bool
        :param roam_action_get: 云存储于云桌面/云应用权限，下载： true : 允许下载。 false: 不允许下载。
        :type roam_action_get: bool
        """
        
        

        self._id = None
        self._attach_id = None
        self._attach = None
        self._quota = None
        self._action_put = None
        self._action_get = None
        self._roam_action_put = None
        self._roam_action_get = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if attach_id is not None:
            self.attach_id = attach_id
        if attach is not None:
            self.attach = attach
        if quota is not None:
            self.quota = quota
        if action_put is not None:
            self.action_put = action_put
        if action_get is not None:
            self.action_get = action_get
        if roam_action_put is not None:
            self.roam_action_put = roam_action_put
        if roam_action_get is not None:
            self.roam_action_get = roam_action_get

    @property
    def id(self):
        r"""Gets the id of this ChangeCloudStorageAssignmentInfo.

        存储分配的唯一标识符。

        :return: The id of this ChangeCloudStorageAssignmentInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ChangeCloudStorageAssignmentInfo.

        存储分配的唯一标识符。

        :param id: The id of this ChangeCloudStorageAssignmentInfo.
        :type id: str
        """
        self._id = id

    @property
    def attach_id(self):
        r"""Gets the attach_id of this ChangeCloudStorageAssignmentInfo.

        目标用户id。

        :return: The attach_id of this ChangeCloudStorageAssignmentInfo.
        :rtype: str
        """
        return self._attach_id

    @attach_id.setter
    def attach_id(self, attach_id):
        r"""Sets the attach_id of this ChangeCloudStorageAssignmentInfo.

        目标用户id。

        :param attach_id: The attach_id of this ChangeCloudStorageAssignmentInfo.
        :type attach_id: str
        """
        self._attach_id = attach_id

    @property
    def attach(self):
        r"""Gets the attach of this ChangeCloudStorageAssignmentInfo.

        目标用户。

        :return: The attach of this ChangeCloudStorageAssignmentInfo.
        :rtype: str
        """
        return self._attach

    @attach.setter
    def attach(self, attach):
        r"""Sets the attach of this ChangeCloudStorageAssignmentInfo.

        目标用户。

        :param attach: The attach of this ChangeCloudStorageAssignmentInfo.
        :type attach: str
        """
        self._attach = attach

    @property
    def quota(self):
        r"""Gets the quota of this ChangeCloudStorageAssignmentInfo.

        配额。

        :return: The quota of this ChangeCloudStorageAssignmentInfo.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ChangeCloudStorageAssignmentInfo.

        配额。

        :param quota: The quota of this ChangeCloudStorageAssignmentInfo.
        :type quota: int
        """
        self._quota = quota

    @property
    def action_put(self):
        r"""Gets the action_put of this ChangeCloudStorageAssignmentInfo.

        云存储于本地设备的权限，上传： true : 允许上传。 false: 不允许上传。

        :return: The action_put of this ChangeCloudStorageAssignmentInfo.
        :rtype: bool
        """
        return self._action_put

    @action_put.setter
    def action_put(self, action_put):
        r"""Sets the action_put of this ChangeCloudStorageAssignmentInfo.

        云存储于本地设备的权限，上传： true : 允许上传。 false: 不允许上传。

        :param action_put: The action_put of this ChangeCloudStorageAssignmentInfo.
        :type action_put: bool
        """
        self._action_put = action_put

    @property
    def action_get(self):
        r"""Gets the action_get of this ChangeCloudStorageAssignmentInfo.

        云存储于本地设备的权限，下载： true : 允许下载。 false: 不允许下载。

        :return: The action_get of this ChangeCloudStorageAssignmentInfo.
        :rtype: bool
        """
        return self._action_get

    @action_get.setter
    def action_get(self, action_get):
        r"""Sets the action_get of this ChangeCloudStorageAssignmentInfo.

        云存储于本地设备的权限，下载： true : 允许下载。 false: 不允许下载。

        :param action_get: The action_get of this ChangeCloudStorageAssignmentInfo.
        :type action_get: bool
        """
        self._action_get = action_get

    @property
    def roam_action_put(self):
        r"""Gets the roam_action_put of this ChangeCloudStorageAssignmentInfo.

        云存储于云桌面/云应用权限，上传： true : 允许上传。 false: 不允许上传。

        :return: The roam_action_put of this ChangeCloudStorageAssignmentInfo.
        :rtype: bool
        """
        return self._roam_action_put

    @roam_action_put.setter
    def roam_action_put(self, roam_action_put):
        r"""Sets the roam_action_put of this ChangeCloudStorageAssignmentInfo.

        云存储于云桌面/云应用权限，上传： true : 允许上传。 false: 不允许上传。

        :param roam_action_put: The roam_action_put of this ChangeCloudStorageAssignmentInfo.
        :type roam_action_put: bool
        """
        self._roam_action_put = roam_action_put

    @property
    def roam_action_get(self):
        r"""Gets the roam_action_get of this ChangeCloudStorageAssignmentInfo.

        云存储于云桌面/云应用权限，下载： true : 允许下载。 false: 不允许下载。

        :return: The roam_action_get of this ChangeCloudStorageAssignmentInfo.
        :rtype: bool
        """
        return self._roam_action_get

    @roam_action_get.setter
    def roam_action_get(self, roam_action_get):
        r"""Sets the roam_action_get of this ChangeCloudStorageAssignmentInfo.

        云存储于云桌面/云应用权限，下载： true : 允许下载。 false: 不允许下载。

        :param roam_action_get: The roam_action_get of this ChangeCloudStorageAssignmentInfo.
        :type roam_action_get: bool
        """
        self._roam_action_get = roam_action_get

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
        if not isinstance(other, ChangeCloudStorageAssignmentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
