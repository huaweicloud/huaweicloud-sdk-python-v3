# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DirectoryI18N:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'directory': 'str',
        'directory_en': 'str',
        'directory_fr': 'str'
    }

    attribute_map = {
        'directory': 'directory',
        'directory_en': 'directory_en',
        'directory_fr': 'directory_fr'
    }

    def __init__(self, directory=None, directory_en=None, directory_fr=None):
        r"""DirectoryI18N

        The model defined in huaweicloud sdk

        :param directory: directory 目录分组
        :type directory: str
        :param directory_en: directory 目录分组
        :type directory_en: str
        :param directory_fr: directory 目录分组
        :type directory_fr: str
        """
        
        

        self._directory = None
        self._directory_en = None
        self._directory_fr = None
        self.discriminator = None

        if directory is not None:
            self.directory = directory
        if directory_en is not None:
            self.directory_en = directory_en
        if directory_fr is not None:
            self.directory_fr = directory_fr

    @property
    def directory(self):
        r"""Gets the directory of this DirectoryI18N.

        directory 目录分组

        :return: The directory of this DirectoryI18N.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this DirectoryI18N.

        directory 目录分组

        :param directory: The directory of this DirectoryI18N.
        :type directory: str
        """
        self._directory = directory

    @property
    def directory_en(self):
        r"""Gets the directory_en of this DirectoryI18N.

        directory 目录分组

        :return: The directory_en of this DirectoryI18N.
        :rtype: str
        """
        return self._directory_en

    @directory_en.setter
    def directory_en(self, directory_en):
        r"""Sets the directory_en of this DirectoryI18N.

        directory 目录分组

        :param directory_en: The directory_en of this DirectoryI18N.
        :type directory_en: str
        """
        self._directory_en = directory_en

    @property
    def directory_fr(self):
        r"""Gets the directory_fr of this DirectoryI18N.

        directory 目录分组

        :return: The directory_fr of this DirectoryI18N.
        :rtype: str
        """
        return self._directory_fr

    @directory_fr.setter
    def directory_fr(self, directory_fr):
        r"""Sets the directory_fr of this DirectoryI18N.

        directory 目录分组

        :param directory_fr: The directory_fr of this DirectoryI18N.
        :type directory_fr: str
        """
        self._directory_fr = directory_fr

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
        if not isinstance(other, DirectoryI18N):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
