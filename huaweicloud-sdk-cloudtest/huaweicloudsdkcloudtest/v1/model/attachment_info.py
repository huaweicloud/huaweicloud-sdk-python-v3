# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachmentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'doc_id': 'str',
        'file_name': 'str',
        'file_path': 'str',
        'file_type': 'str',
        'store_file_name': 'str',
        'related_type': 'str',
        'file_size': 'int'
    }

    attribute_map = {
        'doc_id': 'doc_id',
        'file_name': 'file_name',
        'file_path': 'file_path',
        'file_type': 'file_type',
        'store_file_name': 'store_file_name',
        'related_type': 'related_type',
        'file_size': 'file_size'
    }

    def __init__(self, doc_id=None, file_name=None, file_path=None, file_type=None, store_file_name=None, related_type=None, file_size=None):
        r"""AttachmentInfo

        The model defined in huaweicloud sdk

        :param doc_id: 文档id
        :type doc_id: str
        :param file_name: 文件名
        :type file_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param file_type: 文件类型
        :type file_type: str
        :param store_file_name: 保存文件名
        :type store_file_name: str
        :param related_type: 附件类型 0 本地上传  other 关联文档
        :type related_type: str
        :param file_size: 文件大小
        :type file_size: int
        """
        
        

        self._doc_id = None
        self._file_name = None
        self._file_path = None
        self._file_type = None
        self._store_file_name = None
        self._related_type = None
        self._file_size = None
        self.discriminator = None

        if doc_id is not None:
            self.doc_id = doc_id
        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if file_type is not None:
            self.file_type = file_type
        if store_file_name is not None:
            self.store_file_name = store_file_name
        if related_type is not None:
            self.related_type = related_type
        if file_size is not None:
            self.file_size = file_size

    @property
    def doc_id(self):
        r"""Gets the doc_id of this AttachmentInfo.

        文档id

        :return: The doc_id of this AttachmentInfo.
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        r"""Sets the doc_id of this AttachmentInfo.

        文档id

        :param doc_id: The doc_id of this AttachmentInfo.
        :type doc_id: str
        """
        self._doc_id = doc_id

    @property
    def file_name(self):
        r"""Gets the file_name of this AttachmentInfo.

        文件名

        :return: The file_name of this AttachmentInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this AttachmentInfo.

        文件名

        :param file_name: The file_name of this AttachmentInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        r"""Gets the file_path of this AttachmentInfo.

        文件路径

        :return: The file_path of this AttachmentInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this AttachmentInfo.

        文件路径

        :param file_path: The file_path of this AttachmentInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_type(self):
        r"""Gets the file_type of this AttachmentInfo.

        文件类型

        :return: The file_type of this AttachmentInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this AttachmentInfo.

        文件类型

        :param file_type: The file_type of this AttachmentInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def store_file_name(self):
        r"""Gets the store_file_name of this AttachmentInfo.

        保存文件名

        :return: The store_file_name of this AttachmentInfo.
        :rtype: str
        """
        return self._store_file_name

    @store_file_name.setter
    def store_file_name(self, store_file_name):
        r"""Sets the store_file_name of this AttachmentInfo.

        保存文件名

        :param store_file_name: The store_file_name of this AttachmentInfo.
        :type store_file_name: str
        """
        self._store_file_name = store_file_name

    @property
    def related_type(self):
        r"""Gets the related_type of this AttachmentInfo.

        附件类型 0 本地上传  other 关联文档

        :return: The related_type of this AttachmentInfo.
        :rtype: str
        """
        return self._related_type

    @related_type.setter
    def related_type(self, related_type):
        r"""Sets the related_type of this AttachmentInfo.

        附件类型 0 本地上传  other 关联文档

        :param related_type: The related_type of this AttachmentInfo.
        :type related_type: str
        """
        self._related_type = related_type

    @property
    def file_size(self):
        r"""Gets the file_size of this AttachmentInfo.

        文件大小

        :return: The file_size of this AttachmentInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this AttachmentInfo.

        文件大小

        :param file_size: The file_size of this AttachmentInfo.
        :type file_size: int
        """
        self._file_size = file_size

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
        if not isinstance(other, AttachmentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
