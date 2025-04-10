# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReleaseProjectFilesRequest:

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
        'limit': 'int',
        'offset': 'int',
        'project_id': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'limit': 'limit',
        'offset': 'offset',
        'project_id': 'project_id'
    }

    def __init__(self, file_name=None, limit=None, offset=None, project_id=None):
        r"""ShowReleaseProjectFilesRequest

        The model defined in huaweicloud sdk

        :param file_name: 文件名称，模糊搜索
        :type file_name: str
        :param limit: 每页显示的条目数量
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param project_id: 项目id
        :type project_id: str
        """
        
        

        self._file_name = None
        self._limit = None
        self._offset = None
        self._project_id = None
        self.discriminator = None

        self.file_name = file_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.project_id = project_id

    @property
    def file_name(self):
        r"""Gets the file_name of this ShowReleaseProjectFilesRequest.

        文件名称，模糊搜索

        :return: The file_name of this ShowReleaseProjectFilesRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ShowReleaseProjectFilesRequest.

        文件名称，模糊搜索

        :param file_name: The file_name of this ShowReleaseProjectFilesRequest.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def limit(self):
        r"""Gets the limit of this ShowReleaseProjectFilesRequest.

        每页显示的条目数量

        :return: The limit of this ShowReleaseProjectFilesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowReleaseProjectFilesRequest.

        每页显示的条目数量

        :param limit: The limit of this ShowReleaseProjectFilesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowReleaseProjectFilesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ShowReleaseProjectFilesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowReleaseProjectFilesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ShowReleaseProjectFilesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowReleaseProjectFilesRequest.

        项目id

        :return: The project_id of this ShowReleaseProjectFilesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowReleaseProjectFilesRequest.

        项目id

        :param project_id: The project_id of this ShowReleaseProjectFilesRequest.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ShowReleaseProjectFilesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
