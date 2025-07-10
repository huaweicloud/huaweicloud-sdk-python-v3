# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeInfo:

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
        'type': 'str',
        'size': 'int',
        'resource_spec_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'size': 'size',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, id=None, type=None, size=None, resource_spec_code=None):
        r"""VolumeInfo

        The model defined in huaweicloud sdk

        :param id: 批量操作磁盘的磁盘集合id。
        :type id: str
        :param type: 桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。 - SAS：高IO。 - SSD：超高IO。
        :type type: str
        :param size: 磁盘容量，单位GB。
        :type size: int
        :param resource_spec_code: 规格。
        :type resource_spec_code: str
        """
        
        

        self._id = None
        self._type = None
        self._size = None
        self._resource_spec_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.type = type
        self.size = size
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code

    @property
    def id(self):
        r"""Gets the id of this VolumeInfo.

        批量操作磁盘的磁盘集合id。

        :return: The id of this VolumeInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VolumeInfo.

        批量操作磁盘的磁盘集合id。

        :param id: The id of this VolumeInfo.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this VolumeInfo.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。 - SAS：高IO。 - SSD：超高IO。

        :return: The type of this VolumeInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this VolumeInfo.

        桌面数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。 - SAS：高IO。 - SSD：超高IO。

        :param type: The type of this VolumeInfo.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this VolumeInfo.

        磁盘容量，单位GB。

        :return: The size of this VolumeInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this VolumeInfo.

        磁盘容量，单位GB。

        :param size: The size of this VolumeInfo.
        :type size: int
        """
        self._size = size

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this VolumeInfo.

        规格。

        :return: The resource_spec_code of this VolumeInfo.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this VolumeInfo.

        规格。

        :param resource_spec_code: The resource_spec_code of this VolumeInfo.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

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
        if not isinstance(other, VolumeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
