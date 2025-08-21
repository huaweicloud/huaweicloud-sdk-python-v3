# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadFileInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'file_id': 'str',
        'file_type': 'str',
        'size': 'int'
    }

    attribute_map = {
        'file_name': 'file_name',
        'file_id': 'file_id',
        'file_type': 'file_type',
        'size': 'size'
    }

    def __init__(self, file_name=None, file_id=None, file_type=None, size=None):
        r"""UploadFileInfo

        The model defined in huaweicloud sdk

        :param file_name: 用户上传附件名称
        :type file_name: str
        :param file_id: 用户上传附件唯一id
        :type file_id: str
        :param file_type: 文件类型
        :type file_type: str
        :param size: 用户上传附件大小
        :type size: int
        """
        
        

        self._file_name = None
        self._file_id = None
        self._file_type = None
        self._size = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        self.file_id = file_id
        if file_type is not None:
            self.file_type = file_type
        if size is not None:
            self.size = size

    @property
    def file_name(self):
        r"""Gets the file_name of this UploadFileInfo.

        用户上传附件名称

        :return: The file_name of this UploadFileInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this UploadFileInfo.

        用户上传附件名称

        :param file_name: The file_name of this UploadFileInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_id(self):
        r"""Gets the file_id of this UploadFileInfo.

        用户上传附件唯一id

        :return: The file_id of this UploadFileInfo.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this UploadFileInfo.

        用户上传附件唯一id

        :param file_id: The file_id of this UploadFileInfo.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def file_type(self):
        r"""Gets the file_type of this UploadFileInfo.

        文件类型

        :return: The file_type of this UploadFileInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this UploadFileInfo.

        文件类型

        :param file_type: The file_type of this UploadFileInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def size(self):
        r"""Gets the size of this UploadFileInfo.

        用户上传附件大小

        :return: The size of this UploadFileInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this UploadFileInfo.

        用户上传附件大小

        :param size: The size of this UploadFileInfo.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, UploadFileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
