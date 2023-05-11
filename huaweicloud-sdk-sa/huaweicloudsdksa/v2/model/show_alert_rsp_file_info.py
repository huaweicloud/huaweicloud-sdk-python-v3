# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlertRspFileInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_path': 'str',
        'file_content': 'str',
        'file_new_path': 'str',
        'file_hash': 'str',
        'file_md5': 'str',
        'file_sha256': 'str',
        'file_attr': 'str'
    }

    attribute_map = {
        'file_path': 'file_path',
        'file_content': 'file_content',
        'file_new_path': 'file_new_path',
        'file_hash': 'file_hash',
        'file_md5': 'file_md5',
        'file_sha256': 'file_sha256',
        'file_attr': 'file_attr'
    }

    def __init__(self, file_path=None, file_content=None, file_new_path=None, file_hash=None, file_md5=None, file_sha256=None, file_attr=None):
        """ShowAlertRspFileInfo

        The model defined in huaweicloud sdk

        :param file_path: The name, display only
        :type file_path: str
        :param file_content: The name, display only
        :type file_content: str
        :param file_new_path: The name, display only
        :type file_new_path: str
        :param file_hash: The name, display only
        :type file_hash: str
        :param file_md5: The name, display only
        :type file_md5: str
        :param file_sha256: The name, display only
        :type file_sha256: str
        :param file_attr: The name, display only
        :type file_attr: str
        """
        
        

        self._file_path = None
        self._file_content = None
        self._file_new_path = None
        self._file_hash = None
        self._file_md5 = None
        self._file_sha256 = None
        self._file_attr = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path
        if file_content is not None:
            self.file_content = file_content
        if file_new_path is not None:
            self.file_new_path = file_new_path
        if file_hash is not None:
            self.file_hash = file_hash
        if file_md5 is not None:
            self.file_md5 = file_md5
        if file_sha256 is not None:
            self.file_sha256 = file_sha256
        if file_attr is not None:
            self.file_attr = file_attr

    @property
    def file_path(self):
        """Gets the file_path of this ShowAlertRspFileInfo.

        The name, display only

        :return: The file_path of this ShowAlertRspFileInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this ShowAlertRspFileInfo.

        The name, display only

        :param file_path: The file_path of this ShowAlertRspFileInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_content(self):
        """Gets the file_content of this ShowAlertRspFileInfo.

        The name, display only

        :return: The file_content of this ShowAlertRspFileInfo.
        :rtype: str
        """
        return self._file_content

    @file_content.setter
    def file_content(self, file_content):
        """Sets the file_content of this ShowAlertRspFileInfo.

        The name, display only

        :param file_content: The file_content of this ShowAlertRspFileInfo.
        :type file_content: str
        """
        self._file_content = file_content

    @property
    def file_new_path(self):
        """Gets the file_new_path of this ShowAlertRspFileInfo.

        The name, display only

        :return: The file_new_path of this ShowAlertRspFileInfo.
        :rtype: str
        """
        return self._file_new_path

    @file_new_path.setter
    def file_new_path(self, file_new_path):
        """Sets the file_new_path of this ShowAlertRspFileInfo.

        The name, display only

        :param file_new_path: The file_new_path of this ShowAlertRspFileInfo.
        :type file_new_path: str
        """
        self._file_new_path = file_new_path

    @property
    def file_hash(self):
        """Gets the file_hash of this ShowAlertRspFileInfo.

        The name, display only

        :return: The file_hash of this ShowAlertRspFileInfo.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        """Sets the file_hash of this ShowAlertRspFileInfo.

        The name, display only

        :param file_hash: The file_hash of this ShowAlertRspFileInfo.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def file_md5(self):
        """Gets the file_md5 of this ShowAlertRspFileInfo.

        The name, display only

        :return: The file_md5 of this ShowAlertRspFileInfo.
        :rtype: str
        """
        return self._file_md5

    @file_md5.setter
    def file_md5(self, file_md5):
        """Sets the file_md5 of this ShowAlertRspFileInfo.

        The name, display only

        :param file_md5: The file_md5 of this ShowAlertRspFileInfo.
        :type file_md5: str
        """
        self._file_md5 = file_md5

    @property
    def file_sha256(self):
        """Gets the file_sha256 of this ShowAlertRspFileInfo.

        The name, display only

        :return: The file_sha256 of this ShowAlertRspFileInfo.
        :rtype: str
        """
        return self._file_sha256

    @file_sha256.setter
    def file_sha256(self, file_sha256):
        """Sets the file_sha256 of this ShowAlertRspFileInfo.

        The name, display only

        :param file_sha256: The file_sha256 of this ShowAlertRspFileInfo.
        :type file_sha256: str
        """
        self._file_sha256 = file_sha256

    @property
    def file_attr(self):
        """Gets the file_attr of this ShowAlertRspFileInfo.

        The name, display only

        :return: The file_attr of this ShowAlertRspFileInfo.
        :rtype: str
        """
        return self._file_attr

    @file_attr.setter
    def file_attr(self, file_attr):
        """Sets the file_attr of this ShowAlertRspFileInfo.

        The name, display only

        :param file_attr: The file_attr of this ShowAlertRspFileInfo.
        :type file_attr: str
        """
        self._file_attr = file_attr

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
        if not isinstance(other, ShowAlertRspFileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
