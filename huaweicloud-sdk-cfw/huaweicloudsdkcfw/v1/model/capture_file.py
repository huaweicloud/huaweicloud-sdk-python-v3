# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaptureFile:

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
        'url': 'str',
        'file_path': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'url': 'url',
        'file_path': 'file_path'
    }

    def __init__(self, file_name=None, url=None, file_path=None):
        """CaptureFile

        The model defined in huaweicloud sdk

        :param file_name: 文件名称
        :type file_name: str
        :param url: 下载链接
        :type url: str
        :param file_path: 文件路径
        :type file_path: str
        """
        
        

        self._file_name = None
        self._url = None
        self._file_path = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if url is not None:
            self.url = url
        if file_path is not None:
            self.file_path = file_path

    @property
    def file_name(self):
        """Gets the file_name of this CaptureFile.

        文件名称

        :return: The file_name of this CaptureFile.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this CaptureFile.

        文件名称

        :param file_name: The file_name of this CaptureFile.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def url(self):
        """Gets the url of this CaptureFile.

        下载链接

        :return: The url of this CaptureFile.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CaptureFile.

        下载链接

        :param url: The url of this CaptureFile.
        :type url: str
        """
        self._url = url

    @property
    def file_path(self):
        """Gets the file_path of this CaptureFile.

        文件路径

        :return: The file_path of this CaptureFile.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this CaptureFile.

        文件路径

        :param file_path: The file_path of this CaptureFile.
        :type file_path: str
        """
        self._file_path = file_path

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
        if not isinstance(other, CaptureFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
