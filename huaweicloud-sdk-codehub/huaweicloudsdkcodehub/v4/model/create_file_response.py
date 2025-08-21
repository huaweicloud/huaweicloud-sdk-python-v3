# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFileResponse(SdkResponse):

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
        'branch': 'str'
    }

    attribute_map = {
        'file_path': 'file_path',
        'branch': 'branch'
    }

    def __init__(self, file_path=None, branch=None):
        r"""CreateFileResponse

        The model defined in huaweicloud sdk

        :param file_path: 文件路径
        :type file_path: str
        :param branch: 分支名称
        :type branch: str
        """
        
        super(CreateFileResponse, self).__init__()

        self._file_path = None
        self._branch = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path
        if branch is not None:
            self.branch = branch

    @property
    def file_path(self):
        r"""Gets the file_path of this CreateFileResponse.

        文件路径

        :return: The file_path of this CreateFileResponse.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this CreateFileResponse.

        文件路径

        :param file_path: The file_path of this CreateFileResponse.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def branch(self):
        r"""Gets the branch of this CreateFileResponse.

        分支名称

        :return: The branch of this CreateFileResponse.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this CreateFileResponse.

        分支名称

        :param branch: The branch of this CreateFileResponse.
        :type branch: str
        """
        self._branch = branch

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
        if not isinstance(other, CreateFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
