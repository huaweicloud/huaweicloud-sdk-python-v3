# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DefaultSop:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_cn_name': 'str',
        'file_cn_id': 'str',
        'file_en_name': 'str',
        'file_en_id': 'str',
        'ownership': 'str',
        'default_options': 'bool'
    }

    attribute_map = {
        'file_cn_name': 'file_cn_name',
        'file_cn_id': 'file_cn_id',
        'file_en_name': 'file_en_name',
        'file_en_id': 'file_en_id',
        'ownership': 'ownership',
        'default_options': 'default_options'
    }

    def __init__(self, file_cn_name=None, file_cn_id=None, file_en_name=None, file_en_id=None, ownership=None, default_options=None):
        r"""DefaultSop

        The model defined in huaweicloud sdk

        :param file_cn_name: 中文版本文件名称
        :type file_cn_name: str
        :param file_cn_id: 中文版本文件id
        :type file_cn_id: str
        :param file_en_name: 英文版本文件名称
        :type file_en_name: str
        :param file_en_id: 英文版本文件id
        :type file_en_id: str
        :param ownership: 归属组织
        :type ownership: str
        :param default_options: 是否默认
        :type default_options: bool
        """
        
        

        self._file_cn_name = None
        self._file_cn_id = None
        self._file_en_name = None
        self._file_en_id = None
        self._ownership = None
        self._default_options = None
        self.discriminator = None

        if file_cn_name is not None:
            self.file_cn_name = file_cn_name
        if file_cn_id is not None:
            self.file_cn_id = file_cn_id
        if file_en_name is not None:
            self.file_en_name = file_en_name
        if file_en_id is not None:
            self.file_en_id = file_en_id
        if ownership is not None:
            self.ownership = ownership
        self.default_options = default_options

    @property
    def file_cn_name(self):
        r"""Gets the file_cn_name of this DefaultSop.

        中文版本文件名称

        :return: The file_cn_name of this DefaultSop.
        :rtype: str
        """
        return self._file_cn_name

    @file_cn_name.setter
    def file_cn_name(self, file_cn_name):
        r"""Sets the file_cn_name of this DefaultSop.

        中文版本文件名称

        :param file_cn_name: The file_cn_name of this DefaultSop.
        :type file_cn_name: str
        """
        self._file_cn_name = file_cn_name

    @property
    def file_cn_id(self):
        r"""Gets the file_cn_id of this DefaultSop.

        中文版本文件id

        :return: The file_cn_id of this DefaultSop.
        :rtype: str
        """
        return self._file_cn_id

    @file_cn_id.setter
    def file_cn_id(self, file_cn_id):
        r"""Sets the file_cn_id of this DefaultSop.

        中文版本文件id

        :param file_cn_id: The file_cn_id of this DefaultSop.
        :type file_cn_id: str
        """
        self._file_cn_id = file_cn_id

    @property
    def file_en_name(self):
        r"""Gets the file_en_name of this DefaultSop.

        英文版本文件名称

        :return: The file_en_name of this DefaultSop.
        :rtype: str
        """
        return self._file_en_name

    @file_en_name.setter
    def file_en_name(self, file_en_name):
        r"""Sets the file_en_name of this DefaultSop.

        英文版本文件名称

        :param file_en_name: The file_en_name of this DefaultSop.
        :type file_en_name: str
        """
        self._file_en_name = file_en_name

    @property
    def file_en_id(self):
        r"""Gets the file_en_id of this DefaultSop.

        英文版本文件id

        :return: The file_en_id of this DefaultSop.
        :rtype: str
        """
        return self._file_en_id

    @file_en_id.setter
    def file_en_id(self, file_en_id):
        r"""Sets the file_en_id of this DefaultSop.

        英文版本文件id

        :param file_en_id: The file_en_id of this DefaultSop.
        :type file_en_id: str
        """
        self._file_en_id = file_en_id

    @property
    def ownership(self):
        r"""Gets the ownership of this DefaultSop.

        归属组织

        :return: The ownership of this DefaultSop.
        :rtype: str
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        r"""Sets the ownership of this DefaultSop.

        归属组织

        :param ownership: The ownership of this DefaultSop.
        :type ownership: str
        """
        self._ownership = ownership

    @property
    def default_options(self):
        r"""Gets the default_options of this DefaultSop.

        是否默认

        :return: The default_options of this DefaultSop.
        :rtype: bool
        """
        return self._default_options

    @default_options.setter
    def default_options(self, default_options):
        r"""Sets the default_options of this DefaultSop.

        是否默认

        :param default_options: The default_options of this DefaultSop.
        :type default_options: bool
        """
        self._default_options = default_options

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
        if not isinstance(other, DefaultSop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
