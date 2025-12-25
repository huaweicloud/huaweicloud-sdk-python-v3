# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageInfoDOV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'used_space_length': 'int',
        'used_space': 'str',
        'files_count': 'int'
    }

    attribute_map = {
        'used_space_length': 'used_space_length',
        'used_space': 'used_space',
        'files_count': 'files_count'
    }

    def __init__(self, used_space_length=None, used_space=None, files_count=None):
        r"""StorageInfoDOV5

        The model defined in huaweicloud sdk

        :param used_space_length: **参数解释**: 使用空间（字节）。 **取值范围**: 不涉及。 
        :type used_space_length: int
        :param used_space: **参数解释**: 使用空间（带单位）。 **取值范围**: 不涉及。 
        :type used_space: str
        :param files_count: **参数解释**: 文件数量。 **取值范围**: 不涉及。 
        :type files_count: int
        """
        
        

        self._used_space_length = None
        self._used_space = None
        self._files_count = None
        self.discriminator = None

        if used_space_length is not None:
            self.used_space_length = used_space_length
        if used_space is not None:
            self.used_space = used_space
        if files_count is not None:
            self.files_count = files_count

    @property
    def used_space_length(self):
        r"""Gets the used_space_length of this StorageInfoDOV5.

        **参数解释**: 使用空间（字节）。 **取值范围**: 不涉及。 

        :return: The used_space_length of this StorageInfoDOV5.
        :rtype: int
        """
        return self._used_space_length

    @used_space_length.setter
    def used_space_length(self, used_space_length):
        r"""Sets the used_space_length of this StorageInfoDOV5.

        **参数解释**: 使用空间（字节）。 **取值范围**: 不涉及。 

        :param used_space_length: The used_space_length of this StorageInfoDOV5.
        :type used_space_length: int
        """
        self._used_space_length = used_space_length

    @property
    def used_space(self):
        r"""Gets the used_space of this StorageInfoDOV5.

        **参数解释**: 使用空间（带单位）。 **取值范围**: 不涉及。 

        :return: The used_space of this StorageInfoDOV5.
        :rtype: str
        """
        return self._used_space

    @used_space.setter
    def used_space(self, used_space):
        r"""Sets the used_space of this StorageInfoDOV5.

        **参数解释**: 使用空间（带单位）。 **取值范围**: 不涉及。 

        :param used_space: The used_space of this StorageInfoDOV5.
        :type used_space: str
        """
        self._used_space = used_space

    @property
    def files_count(self):
        r"""Gets the files_count of this StorageInfoDOV5.

        **参数解释**: 文件数量。 **取值范围**: 不涉及。 

        :return: The files_count of this StorageInfoDOV5.
        :rtype: int
        """
        return self._files_count

    @files_count.setter
    def files_count(self, files_count):
        r"""Sets the files_count of this StorageInfoDOV5.

        **参数解释**: 文件数量。 **取值范围**: 不涉及。 

        :param files_count: The files_count of this StorageInfoDOV5.
        :type files_count: int
        """
        self._files_count = files_count

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
        if not isinstance(other, StorageInfoDOV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
