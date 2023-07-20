# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesSupportFastRestoreRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_time': 'str',
        'instance_ids': 'list[str]'
    }

    attribute_map = {
        'restore_time': 'restore_time',
        'instance_ids': 'instance_ids'
    }

    def __init__(self, restore_time=None, instance_ids=None):
        """ListInstancesSupportFastRestoreRequestBody

        The model defined in huaweicloud sdk

        :param restore_time: 要恢复的时间点，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type restore_time: str
        :param instance_ids: 实例id列表。
        :type instance_ids: list[str]
        """
        
        

        self._restore_time = None
        self._instance_ids = None
        self.discriminator = None

        self.restore_time = restore_time
        self.instance_ids = instance_ids

    @property
    def restore_time(self):
        """Gets the restore_time of this ListInstancesSupportFastRestoreRequestBody.

        要恢复的时间点，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The restore_time of this ListInstancesSupportFastRestoreRequestBody.
        :rtype: str
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this ListInstancesSupportFastRestoreRequestBody.

        要恢复的时间点，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param restore_time: The restore_time of this ListInstancesSupportFastRestoreRequestBody.
        :type restore_time: str
        """
        self._restore_time = restore_time

    @property
    def instance_ids(self):
        """Gets the instance_ids of this ListInstancesSupportFastRestoreRequestBody.

        实例id列表。

        :return: The instance_ids of this ListInstancesSupportFastRestoreRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this ListInstancesSupportFastRestoreRequestBody.

        实例id列表。

        :param instance_ids: The instance_ids of this ListInstancesSupportFastRestoreRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

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
        if not isinstance(other, ListInstancesSupportFastRestoreRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
