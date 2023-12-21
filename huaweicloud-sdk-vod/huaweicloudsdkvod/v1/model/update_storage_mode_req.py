# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStorageModeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'storage_mode': 'str',
        'restore_mode': 'str',
        'days': 'int',
        'restore_tier': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'storage_mode': 'storage_mode',
        'restore_mode': 'restore_mode',
        'days': 'days',
        'restore_tier': 'restore_tier'
    }

    def __init__(self, asset_id=None, storage_mode=None, restore_mode=None, days=None, restore_tier=None):
        """UpdateStorageModeReq

        The model defined in huaweicloud sdk

        :param asset_id: 原媒资id 
        :type asset_id: str
        :param storage_mode: 存储模式。 取值如下： - STANDARD：标准存储。 - WARM：低频存储。 - COLD：归档存储。 
        :type storage_mode: str
        :param restore_mode: 归档恢复方式。 取值如下： - TEMP：临时 - FOREVER：永久 
        :type restore_mode: str
        :param days: 从归档转标准存储且选择临时恢复时临时恢复时间。 
        :type days: int
        :param restore_tier: 归档恢复选项，快速恢复EXPEDITED，标准恢复STANDARD，默认快速恢复 
        :type restore_tier: str
        """
        
        

        self._asset_id = None
        self._storage_mode = None
        self._restore_mode = None
        self._days = None
        self._restore_tier = None
        self.discriminator = None

        self.asset_id = asset_id
        self.storage_mode = storage_mode
        if restore_mode is not None:
            self.restore_mode = restore_mode
        if days is not None:
            self.days = days
        if restore_tier is not None:
            self.restore_tier = restore_tier

    @property
    def asset_id(self):
        """Gets the asset_id of this UpdateStorageModeReq.

        原媒资id 

        :return: The asset_id of this UpdateStorageModeReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this UpdateStorageModeReq.

        原媒资id 

        :param asset_id: The asset_id of this UpdateStorageModeReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def storage_mode(self):
        """Gets the storage_mode of this UpdateStorageModeReq.

        存储模式。 取值如下： - STANDARD：标准存储。 - WARM：低频存储。 - COLD：归档存储。 

        :return: The storage_mode of this UpdateStorageModeReq.
        :rtype: str
        """
        return self._storage_mode

    @storage_mode.setter
    def storage_mode(self, storage_mode):
        """Sets the storage_mode of this UpdateStorageModeReq.

        存储模式。 取值如下： - STANDARD：标准存储。 - WARM：低频存储。 - COLD：归档存储。 

        :param storage_mode: The storage_mode of this UpdateStorageModeReq.
        :type storage_mode: str
        """
        self._storage_mode = storage_mode

    @property
    def restore_mode(self):
        """Gets the restore_mode of this UpdateStorageModeReq.

        归档恢复方式。 取值如下： - TEMP：临时 - FOREVER：永久 

        :return: The restore_mode of this UpdateStorageModeReq.
        :rtype: str
        """
        return self._restore_mode

    @restore_mode.setter
    def restore_mode(self, restore_mode):
        """Sets the restore_mode of this UpdateStorageModeReq.

        归档恢复方式。 取值如下： - TEMP：临时 - FOREVER：永久 

        :param restore_mode: The restore_mode of this UpdateStorageModeReq.
        :type restore_mode: str
        """
        self._restore_mode = restore_mode

    @property
    def days(self):
        """Gets the days of this UpdateStorageModeReq.

        从归档转标准存储且选择临时恢复时临时恢复时间。 

        :return: The days of this UpdateStorageModeReq.
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this UpdateStorageModeReq.

        从归档转标准存储且选择临时恢复时临时恢复时间。 

        :param days: The days of this UpdateStorageModeReq.
        :type days: int
        """
        self._days = days

    @property
    def restore_tier(self):
        """Gets the restore_tier of this UpdateStorageModeReq.

        归档恢复选项，快速恢复EXPEDITED，标准恢复STANDARD，默认快速恢复 

        :return: The restore_tier of this UpdateStorageModeReq.
        :rtype: str
        """
        return self._restore_tier

    @restore_tier.setter
    def restore_tier(self, restore_tier):
        """Sets the restore_tier of this UpdateStorageModeReq.

        归档恢复选项，快速恢复EXPEDITED，标准恢复STANDARD，默认快速恢复 

        :param restore_tier: The restore_tier of this UpdateStorageModeReq.
        :type restore_tier: str
        """
        self._restore_tier = restore_tier

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
        if not isinstance(other, UpdateStorageModeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
