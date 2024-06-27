# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseAttachmentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'override': 'bool',
        'doc_id': 'str',
        'file_name': 'str',
        'file_path': 'str',
        'file_type': 'str',
        'file_size': 'str',
        'override_id': 'str',
        'related_type': 'str',
        'store_file_name': 'str',
        'system_type': 'str',
        'storage_system': 'str'
    }

    attribute_map = {
        'override': 'override',
        'doc_id': 'doc_id',
        'file_name': 'file_name',
        'file_path': 'file_path',
        'file_type': 'file_type',
        'file_size': 'file_size',
        'override_id': 'override_id',
        'related_type': 'related_type',
        'store_file_name': 'store_file_name',
        'system_type': 'system_type',
        'storage_system': 'storage_system'
    }

    def __init__(self, override=None, doc_id=None, file_name=None, file_path=None, file_type=None, file_size=None, override_id=None, related_type=None, store_file_name=None, system_type=None, storage_system=None):
        """TestCaseAttachmentInfo

        The model defined in huaweicloud sdk

        :param override: 附件是否要被覆盖
        :type override: bool
        :param doc_id: 文档id
        :type doc_id: str
        :param file_name: 文件名
        :type file_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param file_type: 文件类型
        :type file_type: str
        :param file_size: 文件大小
        :type file_size: str
        :param override_id: 重复用例ID
        :type override_id: str
        :param related_type: 相关类型
        :type related_type: str
        :param store_file_name: 保存文件名
        :type store_file_name: str
        :param system_type: 系统区分
        :type system_type: str
        :param storage_system: 区分文件存储系统
        :type storage_system: str
        """
        
        

        self._override = None
        self._doc_id = None
        self._file_name = None
        self._file_path = None
        self._file_type = None
        self._file_size = None
        self._override_id = None
        self._related_type = None
        self._store_file_name = None
        self._system_type = None
        self._storage_system = None
        self.discriminator = None

        if override is not None:
            self.override = override
        if doc_id is not None:
            self.doc_id = doc_id
        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if file_type is not None:
            self.file_type = file_type
        if file_size is not None:
            self.file_size = file_size
        if override_id is not None:
            self.override_id = override_id
        if related_type is not None:
            self.related_type = related_type
        if store_file_name is not None:
            self.store_file_name = store_file_name
        if system_type is not None:
            self.system_type = system_type
        if storage_system is not None:
            self.storage_system = storage_system

    @property
    def override(self):
        """Gets the override of this TestCaseAttachmentInfo.

        附件是否要被覆盖

        :return: The override of this TestCaseAttachmentInfo.
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        """Sets the override of this TestCaseAttachmentInfo.

        附件是否要被覆盖

        :param override: The override of this TestCaseAttachmentInfo.
        :type override: bool
        """
        self._override = override

    @property
    def doc_id(self):
        """Gets the doc_id of this TestCaseAttachmentInfo.

        文档id

        :return: The doc_id of this TestCaseAttachmentInfo.
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        """Sets the doc_id of this TestCaseAttachmentInfo.

        文档id

        :param doc_id: The doc_id of this TestCaseAttachmentInfo.
        :type doc_id: str
        """
        self._doc_id = doc_id

    @property
    def file_name(self):
        """Gets the file_name of this TestCaseAttachmentInfo.

        文件名

        :return: The file_name of this TestCaseAttachmentInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this TestCaseAttachmentInfo.

        文件名

        :param file_name: The file_name of this TestCaseAttachmentInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        """Gets the file_path of this TestCaseAttachmentInfo.

        文件路径

        :return: The file_path of this TestCaseAttachmentInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this TestCaseAttachmentInfo.

        文件路径

        :param file_path: The file_path of this TestCaseAttachmentInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_type(self):
        """Gets the file_type of this TestCaseAttachmentInfo.

        文件类型

        :return: The file_type of this TestCaseAttachmentInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this TestCaseAttachmentInfo.

        文件类型

        :param file_type: The file_type of this TestCaseAttachmentInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def file_size(self):
        """Gets the file_size of this TestCaseAttachmentInfo.

        文件大小

        :return: The file_size of this TestCaseAttachmentInfo.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this TestCaseAttachmentInfo.

        文件大小

        :param file_size: The file_size of this TestCaseAttachmentInfo.
        :type file_size: str
        """
        self._file_size = file_size

    @property
    def override_id(self):
        """Gets the override_id of this TestCaseAttachmentInfo.

        重复用例ID

        :return: The override_id of this TestCaseAttachmentInfo.
        :rtype: str
        """
        return self._override_id

    @override_id.setter
    def override_id(self, override_id):
        """Sets the override_id of this TestCaseAttachmentInfo.

        重复用例ID

        :param override_id: The override_id of this TestCaseAttachmentInfo.
        :type override_id: str
        """
        self._override_id = override_id

    @property
    def related_type(self):
        """Gets the related_type of this TestCaseAttachmentInfo.

        相关类型

        :return: The related_type of this TestCaseAttachmentInfo.
        :rtype: str
        """
        return self._related_type

    @related_type.setter
    def related_type(self, related_type):
        """Sets the related_type of this TestCaseAttachmentInfo.

        相关类型

        :param related_type: The related_type of this TestCaseAttachmentInfo.
        :type related_type: str
        """
        self._related_type = related_type

    @property
    def store_file_name(self):
        """Gets the store_file_name of this TestCaseAttachmentInfo.

        保存文件名

        :return: The store_file_name of this TestCaseAttachmentInfo.
        :rtype: str
        """
        return self._store_file_name

    @store_file_name.setter
    def store_file_name(self, store_file_name):
        """Sets the store_file_name of this TestCaseAttachmentInfo.

        保存文件名

        :param store_file_name: The store_file_name of this TestCaseAttachmentInfo.
        :type store_file_name: str
        """
        self._store_file_name = store_file_name

    @property
    def system_type(self):
        """Gets the system_type of this TestCaseAttachmentInfo.

        系统区分

        :return: The system_type of this TestCaseAttachmentInfo.
        :rtype: str
        """
        return self._system_type

    @system_type.setter
    def system_type(self, system_type):
        """Sets the system_type of this TestCaseAttachmentInfo.

        系统区分

        :param system_type: The system_type of this TestCaseAttachmentInfo.
        :type system_type: str
        """
        self._system_type = system_type

    @property
    def storage_system(self):
        """Gets the storage_system of this TestCaseAttachmentInfo.

        区分文件存储系统

        :return: The storage_system of this TestCaseAttachmentInfo.
        :rtype: str
        """
        return self._storage_system

    @storage_system.setter
    def storage_system(self, storage_system):
        """Sets the storage_system of this TestCaseAttachmentInfo.

        区分文件存储系统

        :param storage_system: The storage_system of this TestCaseAttachmentInfo.
        :type storage_system: str
        """
        self._storage_system = storage_system

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
        if not isinstance(other, TestCaseAttachmentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
