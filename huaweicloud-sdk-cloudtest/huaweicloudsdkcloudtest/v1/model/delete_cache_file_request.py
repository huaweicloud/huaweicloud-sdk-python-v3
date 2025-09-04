# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteCacheFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'file_path': 'str',
        'uri': 'str',
        'parent_uri': 'str',
        'bak_up': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'file_path': 'file_path',
        'uri': 'uri',
        'parent_uri': 'parent_uri',
        'bak_up': 'bak_up'
    }

    def __init__(self, project_id=None, file_path=None, uri=None, parent_uri=None, bak_up=None):
        r"""DeleteCacheFileRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param file_path: 删除附件路径
        :type file_path: str
        :param uri: 附件Uri
        :type uri: str
        :param parent_uri: 附件挂载资源Uri
        :type parent_uri: str
        :param bak_up: 是否备份
        :type bak_up: bool
        """
        
        

        self._project_id = None
        self._file_path = None
        self._uri = None
        self._parent_uri = None
        self._bak_up = None
        self.discriminator = None

        self.project_id = project_id
        if file_path is not None:
            self.file_path = file_path
        if uri is not None:
            self.uri = uri
        if parent_uri is not None:
            self.parent_uri = parent_uri
        if bak_up is not None:
            self.bak_up = bak_up

    @property
    def project_id(self):
        r"""Gets the project_id of this DeleteCacheFileRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this DeleteCacheFileRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DeleteCacheFileRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this DeleteCacheFileRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def file_path(self):
        r"""Gets the file_path of this DeleteCacheFileRequest.

        删除附件路径

        :return: The file_path of this DeleteCacheFileRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this DeleteCacheFileRequest.

        删除附件路径

        :param file_path: The file_path of this DeleteCacheFileRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def uri(self):
        r"""Gets the uri of this DeleteCacheFileRequest.

        附件Uri

        :return: The uri of this DeleteCacheFileRequest.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this DeleteCacheFileRequest.

        附件Uri

        :param uri: The uri of this DeleteCacheFileRequest.
        :type uri: str
        """
        self._uri = uri

    @property
    def parent_uri(self):
        r"""Gets the parent_uri of this DeleteCacheFileRequest.

        附件挂载资源Uri

        :return: The parent_uri of this DeleteCacheFileRequest.
        :rtype: str
        """
        return self._parent_uri

    @parent_uri.setter
    def parent_uri(self, parent_uri):
        r"""Sets the parent_uri of this DeleteCacheFileRequest.

        附件挂载资源Uri

        :param parent_uri: The parent_uri of this DeleteCacheFileRequest.
        :type parent_uri: str
        """
        self._parent_uri = parent_uri

    @property
    def bak_up(self):
        r"""Gets the bak_up of this DeleteCacheFileRequest.

        是否备份

        :return: The bak_up of this DeleteCacheFileRequest.
        :rtype: bool
        """
        return self._bak_up

    @bak_up.setter
    def bak_up(self, bak_up):
        r"""Sets the bak_up of this DeleteCacheFileRequest.

        是否备份

        :param bak_up: The bak_up of this DeleteCacheFileRequest.
        :type bak_up: bool
        """
        self._bak_up = bak_up

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
        if not isinstance(other, DeleteCacheFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
