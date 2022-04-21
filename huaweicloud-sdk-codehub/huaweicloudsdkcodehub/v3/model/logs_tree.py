# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogsTree:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'blob_id': 'str',
        'commit': 'Commit',
        'file_name': 'str',
        'file_path': 'str',
        'md5': 'str',
        'type': 'str'
    }

    attribute_map = {
        'blob_id': 'blob_id',
        'commit': 'commit',
        'file_name': 'file_name',
        'file_path': 'file_path',
        'md5': 'md5',
        'type': 'type'
    }

    def __init__(self, blob_id=None, commit=None, file_name=None, file_path=None, md5=None, type=None):
        """LogsTree

        The model defined in huaweicloud sdk

        :param blob_id: 存储块id
        :type blob_id: str
        :param commit: 
        :type commit: :class:`huaweicloudsdkcodehub.v3.Commit`
        :param file_name: 文件名称
        :type file_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param md5: MD5
        :type md5: str
        :param type: 存储类型
        :type type: str
        """
        
        

        self._blob_id = None
        self._commit = None
        self._file_name = None
        self._file_path = None
        self._md5 = None
        self._type = None
        self.discriminator = None

        if blob_id is not None:
            self.blob_id = blob_id
        if commit is not None:
            self.commit = commit
        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if md5 is not None:
            self.md5 = md5
        if type is not None:
            self.type = type

    @property
    def blob_id(self):
        """Gets the blob_id of this LogsTree.

        存储块id

        :return: The blob_id of this LogsTree.
        :rtype: str
        """
        return self._blob_id

    @blob_id.setter
    def blob_id(self, blob_id):
        """Sets the blob_id of this LogsTree.

        存储块id

        :param blob_id: The blob_id of this LogsTree.
        :type blob_id: str
        """
        self._blob_id = blob_id

    @property
    def commit(self):
        """Gets the commit of this LogsTree.


        :return: The commit of this LogsTree.
        :rtype: :class:`huaweicloudsdkcodehub.v3.Commit`
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this LogsTree.


        :param commit: The commit of this LogsTree.
        :type commit: :class:`huaweicloudsdkcodehub.v3.Commit`
        """
        self._commit = commit

    @property
    def file_name(self):
        """Gets the file_name of this LogsTree.

        文件名称

        :return: The file_name of this LogsTree.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this LogsTree.

        文件名称

        :param file_name: The file_name of this LogsTree.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        """Gets the file_path of this LogsTree.

        文件路径

        :return: The file_path of this LogsTree.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this LogsTree.

        文件路径

        :param file_path: The file_path of this LogsTree.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def md5(self):
        """Gets the md5 of this LogsTree.

        MD5

        :return: The md5 of this LogsTree.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this LogsTree.

        MD5

        :param md5: The md5 of this LogsTree.
        :type md5: str
        """
        self._md5 = md5

    @property
    def type(self):
        """Gets the type of this LogsTree.

        存储类型

        :return: The type of this LogsTree.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LogsTree.

        存储类型

        :param type: The type of this LogsTree.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, LogsTree):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
