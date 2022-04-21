# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVolumeSchedulerHints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dedicated_storage_id': 'str'
    }

    attribute_map = {
        'dedicated_storage_id': 'dedicated_storage_id'
    }

    def __init__(self, dedicated_storage_id=None):
        """CreateVolumeSchedulerHints

        The model defined in huaweicloud sdk

        :param dedicated_storage_id: 指定专属存储池ID，表示将云硬盘创建在该ID对应的存储池中。
        :type dedicated_storage_id: str
        """
        
        

        self._dedicated_storage_id = None
        self.discriminator = None

        if dedicated_storage_id is not None:
            self.dedicated_storage_id = dedicated_storage_id

    @property
    def dedicated_storage_id(self):
        """Gets the dedicated_storage_id of this CreateVolumeSchedulerHints.

        指定专属存储池ID，表示将云硬盘创建在该ID对应的存储池中。

        :return: The dedicated_storage_id of this CreateVolumeSchedulerHints.
        :rtype: str
        """
        return self._dedicated_storage_id

    @dedicated_storage_id.setter
    def dedicated_storage_id(self, dedicated_storage_id):
        """Sets the dedicated_storage_id of this CreateVolumeSchedulerHints.

        指定专属存储池ID，表示将云硬盘创建在该ID对应的存储池中。

        :param dedicated_storage_id: The dedicated_storage_id of this CreateVolumeSchedulerHints.
        :type dedicated_storage_id: str
        """
        self._dedicated_storage_id = dedicated_storage_id

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
        if not isinstance(other, CreateVolumeSchedulerHints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
