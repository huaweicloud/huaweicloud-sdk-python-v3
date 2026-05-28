# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreInstSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_time': 'float'
    }

    attribute_map = {
        'restore_time': 'restore_time'
    }

    def __init__(self, restore_time=None):
        r"""RestoreInstSource

        The model defined in huaweicloud sdk

        :param restore_time: 恢复时间。
        :type restore_time: float
        """
        
        

        self._restore_time = None
        self.discriminator = None

        self.restore_time = restore_time

    @property
    def restore_time(self):
        r"""Gets the restore_time of this RestoreInstSource.

        恢复时间。

        :return: The restore_time of this RestoreInstSource.
        :rtype: float
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        r"""Sets the restore_time of this RestoreInstSource.

        恢复时间。

        :param restore_time: The restore_time of this RestoreInstSource.
        :type restore_time: float
        """
        self._restore_time = restore_time

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
        if not isinstance(other, RestoreInstSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
