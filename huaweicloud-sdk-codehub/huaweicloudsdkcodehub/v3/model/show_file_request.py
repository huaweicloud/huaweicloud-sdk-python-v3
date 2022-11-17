# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repo_id': 'int',
        'file_path': 'str',
        'ref': 'str'
    }

    attribute_map = {
        'repo_id': 'repo_id',
        'file_path': 'file_path',
        'ref': 'ref'
    }

    def __init__(self, repo_id=None, file_path=None, ref=None):
        """ShowFileRequest

        The model defined in huaweicloud sdk

        :param repo_id: 仓库短id
        :type repo_id: int
        :param file_path: Url编码的新文件的完整路径。
        :type file_path: str
        :param ref: commit id，仓库的branch名或tag名
        :type ref: str
        """
        
        

        self._repo_id = None
        self._file_path = None
        self._ref = None
        self.discriminator = None

        self.repo_id = repo_id
        self.file_path = file_path
        self.ref = ref

    @property
    def repo_id(self):
        """Gets the repo_id of this ShowFileRequest.

        仓库短id

        :return: The repo_id of this ShowFileRequest.
        :rtype: int
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this ShowFileRequest.

        仓库短id

        :param repo_id: The repo_id of this ShowFileRequest.
        :type repo_id: int
        """
        self._repo_id = repo_id

    @property
    def file_path(self):
        """Gets the file_path of this ShowFileRequest.

        Url编码的新文件的完整路径。

        :return: The file_path of this ShowFileRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this ShowFileRequest.

        Url编码的新文件的完整路径。

        :param file_path: The file_path of this ShowFileRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def ref(self):
        """Gets the ref of this ShowFileRequest.

        commit id，仓库的branch名或tag名

        :return: The ref of this ShowFileRequest.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this ShowFileRequest.

        commit id，仓库的branch名或tag名

        :param ref: The ref of this ShowFileRequest.
        :type ref: str
        """
        self._ref = ref

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
        if not isinstance(other, ShowFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
