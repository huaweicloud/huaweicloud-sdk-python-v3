# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandDesktopPoolVolumesReqVolumes:

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
        'size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'size': 'size'
    }

    def __init__(self, id=None, size=None):
        r"""ExpandDesktopPoolVolumesReqVolumes

        The model defined in huaweicloud sdk

        :param id: 批量操作磁盘的磁盘集合id。
        :type id: str
        :param size: 磁盘容量，单位GB。
        :type size: int
        """
        
        

        self._id = None
        self._size = None
        self.discriminator = None

        self.id = id
        self.size = size

    @property
    def id(self):
        r"""Gets the id of this ExpandDesktopPoolVolumesReqVolumes.

        批量操作磁盘的磁盘集合id。

        :return: The id of this ExpandDesktopPoolVolumesReqVolumes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExpandDesktopPoolVolumesReqVolumes.

        批量操作磁盘的磁盘集合id。

        :param id: The id of this ExpandDesktopPoolVolumesReqVolumes.
        :type id: str
        """
        self._id = id

    @property
    def size(self):
        r"""Gets the size of this ExpandDesktopPoolVolumesReqVolumes.

        磁盘容量，单位GB。

        :return: The size of this ExpandDesktopPoolVolumesReqVolumes.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ExpandDesktopPoolVolumesReqVolumes.

        磁盘容量，单位GB。

        :param size: The size of this ExpandDesktopPoolVolumesReqVolumes.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ExpandDesktopPoolVolumesReqVolumes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
