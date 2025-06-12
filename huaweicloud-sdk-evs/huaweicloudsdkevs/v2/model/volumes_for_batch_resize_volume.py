# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumesForBatchResizeVolume:

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
        'new_size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'new_size': 'new_size'
    }

    def __init__(self, id=None, new_size=None):
        r"""VolumesForBatchResizeVolume

        The model defined in huaweicloud sdk

        :param id: The disk ID.
        :type id: str
        :param new_size: The new disk size, in GiB. This parameter value must be greater than the original disk size and less than the maximum size allowed for a disk. The maximum disk size: - Data disk: 32,768 GiB - System disk: 1,024 GiB
        :type new_size: int
        """
        
        

        self._id = None
        self._new_size = None
        self.discriminator = None

        self.id = id
        self.new_size = new_size

    @property
    def id(self):
        r"""Gets the id of this VolumesForBatchResizeVolume.

        The disk ID.

        :return: The id of this VolumesForBatchResizeVolume.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VolumesForBatchResizeVolume.

        The disk ID.

        :param id: The id of this VolumesForBatchResizeVolume.
        :type id: str
        """
        self._id = id

    @property
    def new_size(self):
        r"""Gets the new_size of this VolumesForBatchResizeVolume.

        The new disk size, in GiB. This parameter value must be greater than the original disk size and less than the maximum size allowed for a disk. The maximum disk size: - Data disk: 32,768 GiB - System disk: 1,024 GiB

        :return: The new_size of this VolumesForBatchResizeVolume.
        :rtype: int
        """
        return self._new_size

    @new_size.setter
    def new_size(self, new_size):
        r"""Sets the new_size of this VolumesForBatchResizeVolume.

        The new disk size, in GiB. This parameter value must be greater than the original disk size and less than the maximum size allowed for a disk. The maximum disk size: - Data disk: 32,768 GiB - System disk: 1,024 GiB

        :param new_size: The new_size of this VolumesForBatchResizeVolume.
        :type new_size: int
        """
        self._new_size = new_size

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
        if not isinstance(other, VolumesForBatchResizeVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
