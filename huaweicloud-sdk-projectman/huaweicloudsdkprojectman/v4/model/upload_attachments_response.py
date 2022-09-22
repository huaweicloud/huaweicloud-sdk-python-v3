# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadAttachmentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'issue_id': 'int',
        'project_id': 'str',
        'disk_filename': 'str',
        'file_name': 'str',
        'size': 'str'
    }

    attribute_map = {
        'id': 'id',
        'issue_id': 'issue_id',
        'project_id': 'project_id',
        'disk_filename': 'disk_filename',
        'file_name': 'file_name',
        'size': 'size'
    }

    def __init__(self, id=None, issue_id=None, project_id=None, disk_filename=None, file_name=None, size=None):
        """UploadAttachmentsResponse

        The model defined in huaweicloud sdk

        :param id: 关联id
        :type id: int
        :param issue_id: 工作项id
        :type issue_id: int
        :param project_id: 项目id
        :type project_id: str
        :param disk_filename: 云盘存贮名
        :type disk_filename: str
        :param file_name: 文件名
        :type file_name: str
        :param size: 文件大小
        :type size: str
        """
        
        super(UploadAttachmentsResponse, self).__init__()

        self._id = None
        self._issue_id = None
        self._project_id = None
        self._disk_filename = None
        self._file_name = None
        self._size = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if issue_id is not None:
            self.issue_id = issue_id
        if project_id is not None:
            self.project_id = project_id
        if disk_filename is not None:
            self.disk_filename = disk_filename
        if file_name is not None:
            self.file_name = file_name
        if size is not None:
            self.size = size

    @property
    def id(self):
        """Gets the id of this UploadAttachmentsResponse.

        关联id

        :return: The id of this UploadAttachmentsResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UploadAttachmentsResponse.

        关联id

        :param id: The id of this UploadAttachmentsResponse.
        :type id: int
        """
        self._id = id

    @property
    def issue_id(self):
        """Gets the issue_id of this UploadAttachmentsResponse.

        工作项id

        :return: The issue_id of this UploadAttachmentsResponse.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this UploadAttachmentsResponse.

        工作项id

        :param issue_id: The issue_id of this UploadAttachmentsResponse.
        :type issue_id: int
        """
        self._issue_id = issue_id

    @property
    def project_id(self):
        """Gets the project_id of this UploadAttachmentsResponse.

        项目id

        :return: The project_id of this UploadAttachmentsResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UploadAttachmentsResponse.

        项目id

        :param project_id: The project_id of this UploadAttachmentsResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def disk_filename(self):
        """Gets the disk_filename of this UploadAttachmentsResponse.

        云盘存贮名

        :return: The disk_filename of this UploadAttachmentsResponse.
        :rtype: str
        """
        return self._disk_filename

    @disk_filename.setter
    def disk_filename(self, disk_filename):
        """Sets the disk_filename of this UploadAttachmentsResponse.

        云盘存贮名

        :param disk_filename: The disk_filename of this UploadAttachmentsResponse.
        :type disk_filename: str
        """
        self._disk_filename = disk_filename

    @property
    def file_name(self):
        """Gets the file_name of this UploadAttachmentsResponse.

        文件名

        :return: The file_name of this UploadAttachmentsResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this UploadAttachmentsResponse.

        文件名

        :param file_name: The file_name of this UploadAttachmentsResponse.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def size(self):
        """Gets the size of this UploadAttachmentsResponse.

        文件大小

        :return: The size of this UploadAttachmentsResponse.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this UploadAttachmentsResponse.

        文件大小

        :param size: The size of this UploadAttachmentsResponse.
        :type size: str
        """
        self._size = size

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
        if not isinstance(other, UploadAttachmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
