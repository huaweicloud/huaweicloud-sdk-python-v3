# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachmentFileVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'path': 'str',
        'project_id': 'str',
        'file_path': 'str',
        'file_type': 'str',
        'doc_name': 'str',
        'store_name': 'str',
        'doc_id': 'int',
        'doc_size': 'str',
        'related_type': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'path': 'path',
        'project_id': 'project_id',
        'file_path': 'file_path',
        'file_type': 'file_type',
        'doc_name': 'doc_name',
        'store_name': 'store_name',
        'doc_id': 'doc_id',
        'doc_size': 'doc_size',
        'related_type': 'related_type'
    }

    def __init__(self, uri=None, path=None, project_id=None, file_path=None, file_type=None, doc_name=None, store_name=None, doc_id=None, doc_size=None, related_type=None):
        r"""AttachmentFileVo

        The model defined in huaweicloud sdk

        :param uri: 附件Uri
        :type uri: str
        :param path: 文件路径
        :type path: str
        :param project_id: 项目ID
        :type project_id: str
        :param file_path: 文件路径
        :type file_path: str
        :param file_type: 文件类型
        :type file_type: str
        :param doc_name: 文档名
        :type doc_name: str
        :param store_name: 保存文件名
        :type store_name: str
        :param doc_id: 文档id
        :type doc_id: int
        :param doc_size: 文档大小
        :type doc_size: str
        :param related_type: 相关类型
        :type related_type: str
        """
        
        

        self._uri = None
        self._path = None
        self._project_id = None
        self._file_path = None
        self._file_type = None
        self._doc_name = None
        self._store_name = None
        self._doc_id = None
        self._doc_size = None
        self._related_type = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if path is not None:
            self.path = path
        if project_id is not None:
            self.project_id = project_id
        if file_path is not None:
            self.file_path = file_path
        if file_type is not None:
            self.file_type = file_type
        if doc_name is not None:
            self.doc_name = doc_name
        if store_name is not None:
            self.store_name = store_name
        if doc_id is not None:
            self.doc_id = doc_id
        if doc_size is not None:
            self.doc_size = doc_size
        if related_type is not None:
            self.related_type = related_type

    @property
    def uri(self):
        r"""Gets the uri of this AttachmentFileVo.

        附件Uri

        :return: The uri of this AttachmentFileVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this AttachmentFileVo.

        附件Uri

        :param uri: The uri of this AttachmentFileVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def path(self):
        r"""Gets the path of this AttachmentFileVo.

        文件路径

        :return: The path of this AttachmentFileVo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this AttachmentFileVo.

        文件路径

        :param path: The path of this AttachmentFileVo.
        :type path: str
        """
        self._path = path

    @property
    def project_id(self):
        r"""Gets the project_id of this AttachmentFileVo.

        项目ID

        :return: The project_id of this AttachmentFileVo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AttachmentFileVo.

        项目ID

        :param project_id: The project_id of this AttachmentFileVo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def file_path(self):
        r"""Gets the file_path of this AttachmentFileVo.

        文件路径

        :return: The file_path of this AttachmentFileVo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this AttachmentFileVo.

        文件路径

        :param file_path: The file_path of this AttachmentFileVo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_type(self):
        r"""Gets the file_type of this AttachmentFileVo.

        文件类型

        :return: The file_type of this AttachmentFileVo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this AttachmentFileVo.

        文件类型

        :param file_type: The file_type of this AttachmentFileVo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def doc_name(self):
        r"""Gets the doc_name of this AttachmentFileVo.

        文档名

        :return: The doc_name of this AttachmentFileVo.
        :rtype: str
        """
        return self._doc_name

    @doc_name.setter
    def doc_name(self, doc_name):
        r"""Sets the doc_name of this AttachmentFileVo.

        文档名

        :param doc_name: The doc_name of this AttachmentFileVo.
        :type doc_name: str
        """
        self._doc_name = doc_name

    @property
    def store_name(self):
        r"""Gets the store_name of this AttachmentFileVo.

        保存文件名

        :return: The store_name of this AttachmentFileVo.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this AttachmentFileVo.

        保存文件名

        :param store_name: The store_name of this AttachmentFileVo.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def doc_id(self):
        r"""Gets the doc_id of this AttachmentFileVo.

        文档id

        :return: The doc_id of this AttachmentFileVo.
        :rtype: int
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        r"""Sets the doc_id of this AttachmentFileVo.

        文档id

        :param doc_id: The doc_id of this AttachmentFileVo.
        :type doc_id: int
        """
        self._doc_id = doc_id

    @property
    def doc_size(self):
        r"""Gets the doc_size of this AttachmentFileVo.

        文档大小

        :return: The doc_size of this AttachmentFileVo.
        :rtype: str
        """
        return self._doc_size

    @doc_size.setter
    def doc_size(self, doc_size):
        r"""Sets the doc_size of this AttachmentFileVo.

        文档大小

        :param doc_size: The doc_size of this AttachmentFileVo.
        :type doc_size: str
        """
        self._doc_size = doc_size

    @property
    def related_type(self):
        r"""Gets the related_type of this AttachmentFileVo.

        相关类型

        :return: The related_type of this AttachmentFileVo.
        :rtype: str
        """
        return self._related_type

    @related_type.setter
    def related_type(self, related_type):
        r"""Sets the related_type of this AttachmentFileVo.

        相关类型

        :param related_type: The related_type of this AttachmentFileVo.
        :type related_type: str
        """
        self._related_type = related_type

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
        if not isinstance(other, AttachmentFileVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
