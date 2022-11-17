# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueAccessory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attachment_id': 'int',
        'issue_id': 'int',
        'creator_num_id': 'int',
        'created_date': 'str',
        'file_name': 'str',
        'container_type': 'str',
        'disk_file_name': 'str',
        'digest': 'str',
        'disk_directory': 'str',
        'creator_id': 'str'
    }

    attribute_map = {
        'attachment_id': 'attachment_id',
        'issue_id': 'issue_id',
        'creator_num_id': 'creator_num_id',
        'created_date': 'created_date',
        'file_name': 'file_name',
        'container_type': 'container_type',
        'disk_file_name': 'disk_file_name',
        'digest': 'digest',
        'disk_directory': 'disk_directory',
        'creator_id': 'creator_id'
    }

    def __init__(self, attachment_id=None, issue_id=None, creator_num_id=None, created_date=None, file_name=None, container_type=None, disk_file_name=None, digest=None, disk_directory=None, creator_id=None):
        """IssueAccessory

        The model defined in huaweicloud sdk

        :param attachment_id: 附件id
        :type attachment_id: int
        :param issue_id: 工作鞋ID
        :type issue_id: int
        :param creator_num_id: 创建者数字ID
        :type creator_num_id: int
        :param created_date: 附件创建时间
        :type created_date: str
        :param file_name: 上传时文件名
        :type file_name: str
        :param container_type: 附件id
        :type container_type: str
        :param disk_file_name: 附件名称
        :type disk_file_name: str
        :param digest: 附件id
        :type digest: str
        :param disk_directory: 附件路径
        :type disk_directory: str
        :param creator_id: 创建这用户uuid
        :type creator_id: str
        """
        
        

        self._attachment_id = None
        self._issue_id = None
        self._creator_num_id = None
        self._created_date = None
        self._file_name = None
        self._container_type = None
        self._disk_file_name = None
        self._digest = None
        self._disk_directory = None
        self._creator_id = None
        self.discriminator = None

        if attachment_id is not None:
            self.attachment_id = attachment_id
        if issue_id is not None:
            self.issue_id = issue_id
        if creator_num_id is not None:
            self.creator_num_id = creator_num_id
        if created_date is not None:
            self.created_date = created_date
        if file_name is not None:
            self.file_name = file_name
        if container_type is not None:
            self.container_type = container_type
        if disk_file_name is not None:
            self.disk_file_name = disk_file_name
        if digest is not None:
            self.digest = digest
        if disk_directory is not None:
            self.disk_directory = disk_directory
        if creator_id is not None:
            self.creator_id = creator_id

    @property
    def attachment_id(self):
        """Gets the attachment_id of this IssueAccessory.

        附件id

        :return: The attachment_id of this IssueAccessory.
        :rtype: int
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this IssueAccessory.

        附件id

        :param attachment_id: The attachment_id of this IssueAccessory.
        :type attachment_id: int
        """
        self._attachment_id = attachment_id

    @property
    def issue_id(self):
        """Gets the issue_id of this IssueAccessory.

        工作鞋ID

        :return: The issue_id of this IssueAccessory.
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this IssueAccessory.

        工作鞋ID

        :param issue_id: The issue_id of this IssueAccessory.
        :type issue_id: int
        """
        self._issue_id = issue_id

    @property
    def creator_num_id(self):
        """Gets the creator_num_id of this IssueAccessory.

        创建者数字ID

        :return: The creator_num_id of this IssueAccessory.
        :rtype: int
        """
        return self._creator_num_id

    @creator_num_id.setter
    def creator_num_id(self, creator_num_id):
        """Sets the creator_num_id of this IssueAccessory.

        创建者数字ID

        :param creator_num_id: The creator_num_id of this IssueAccessory.
        :type creator_num_id: int
        """
        self._creator_num_id = creator_num_id

    @property
    def created_date(self):
        """Gets the created_date of this IssueAccessory.

        附件创建时间

        :return: The created_date of this IssueAccessory.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this IssueAccessory.

        附件创建时间

        :param created_date: The created_date of this IssueAccessory.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def file_name(self):
        """Gets the file_name of this IssueAccessory.

        上传时文件名

        :return: The file_name of this IssueAccessory.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this IssueAccessory.

        上传时文件名

        :param file_name: The file_name of this IssueAccessory.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def container_type(self):
        """Gets the container_type of this IssueAccessory.

        附件id

        :return: The container_type of this IssueAccessory.
        :rtype: str
        """
        return self._container_type

    @container_type.setter
    def container_type(self, container_type):
        """Sets the container_type of this IssueAccessory.

        附件id

        :param container_type: The container_type of this IssueAccessory.
        :type container_type: str
        """
        self._container_type = container_type

    @property
    def disk_file_name(self):
        """Gets the disk_file_name of this IssueAccessory.

        附件名称

        :return: The disk_file_name of this IssueAccessory.
        :rtype: str
        """
        return self._disk_file_name

    @disk_file_name.setter
    def disk_file_name(self, disk_file_name):
        """Sets the disk_file_name of this IssueAccessory.

        附件名称

        :param disk_file_name: The disk_file_name of this IssueAccessory.
        :type disk_file_name: str
        """
        self._disk_file_name = disk_file_name

    @property
    def digest(self):
        """Gets the digest of this IssueAccessory.

        附件id

        :return: The digest of this IssueAccessory.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this IssueAccessory.

        附件id

        :param digest: The digest of this IssueAccessory.
        :type digest: str
        """
        self._digest = digest

    @property
    def disk_directory(self):
        """Gets the disk_directory of this IssueAccessory.

        附件路径

        :return: The disk_directory of this IssueAccessory.
        :rtype: str
        """
        return self._disk_directory

    @disk_directory.setter
    def disk_directory(self, disk_directory):
        """Sets the disk_directory of this IssueAccessory.

        附件路径

        :param disk_directory: The disk_directory of this IssueAccessory.
        :type disk_directory: str
        """
        self._disk_directory = disk_directory

    @property
    def creator_id(self):
        """Gets the creator_id of this IssueAccessory.

        创建这用户uuid

        :return: The creator_id of this IssueAccessory.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this IssueAccessory.

        创建这用户uuid

        :param creator_id: The creator_id of this IssueAccessory.
        :type creator_id: str
        """
        self._creator_id = creator_id

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
        if not isinstance(other, IssueAccessory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
