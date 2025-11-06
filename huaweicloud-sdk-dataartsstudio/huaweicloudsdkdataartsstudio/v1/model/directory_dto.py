# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DirectoryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'directory_id': 'str',
        'directory_name': 'str'
    }

    attribute_map = {
        'directory_id': 'directory_id',
        'directory_name': 'directory_name'
    }

    def __init__(self, directory_id=None, directory_name=None):
        r"""DirectoryDTO

        The model defined in huaweicloud sdk

        :param directory_id: 目录ID。
        :type directory_id: str
        :param directory_name: 目录名称。
        :type directory_name: str
        """
        
        

        self._directory_id = None
        self._directory_name = None
        self.discriminator = None

        if directory_id is not None:
            self.directory_id = directory_id
        if directory_name is not None:
            self.directory_name = directory_name

    @property
    def directory_id(self):
        r"""Gets the directory_id of this DirectoryDTO.

        目录ID。

        :return: The directory_id of this DirectoryDTO.
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        r"""Sets the directory_id of this DirectoryDTO.

        目录ID。

        :param directory_id: The directory_id of this DirectoryDTO.
        :type directory_id: str
        """
        self._directory_id = directory_id

    @property
    def directory_name(self):
        r"""Gets the directory_name of this DirectoryDTO.

        目录名称。

        :return: The directory_name of this DirectoryDTO.
        :rtype: str
        """
        return self._directory_name

    @directory_name.setter
    def directory_name(self, directory_name):
        r"""Sets the directory_name of this DirectoryDTO.

        目录名称。

        :param directory_name: The directory_name of this DirectoryDTO.
        :type directory_name: str
        """
        self._directory_name = directory_name

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
        if not isinstance(other, DirectoryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
