# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachmentEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'issue_id': 'str',
        'disk_directory': 'str',
        'file_size': 'str',
        'store_filename': 'str',
        'title': 'str',
        'modified_by': 'UserEntity',
        'created_by': 'UserEntity',
        'attachment_type': 'str',
        'created_date': 'str'
    }

    attribute_map = {
        'id': 'id',
        'issue_id': 'issue_id',
        'disk_directory': 'disk_directory',
        'file_size': 'file_size',
        'store_filename': 'store_filename',
        'title': 'title',
        'modified_by': 'modified_by',
        'created_by': 'created_by',
        'attachment_type': 'attachment_type',
        'created_date': 'created_date'
    }

    def __init__(self, id=None, issue_id=None, disk_directory=None, file_size=None, store_filename=None, title=None, modified_by=None, created_by=None, attachment_type=None, created_date=None):
        r"""AttachmentEntity

        The model defined in huaweicloud sdk

        :param id: 附件Id
        :type id: str
        :param issue_id: 附件所属工作项Id
        :type issue_id: str
        :param disk_directory: 在服务器存储的相对路径
        :type disk_directory: str
        :param file_size: 附件大小，单位为Byte，单个附件最大为200MB
        :type file_size: str
        :param store_filename: 附件原名称
        :type store_filename: str
        :param title: 附件在数据库中存储的名称。格式为uuid+.扩展名
        :type title: str
        :param modified_by: 
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param attachment_type: 附件类型，即文件扩展名
        :type attachment_type: str
        :param created_date: 附件上传时间的时间戳
        :type created_date: str
        """
        
        

        self._id = None
        self._issue_id = None
        self._disk_directory = None
        self._file_size = None
        self._store_filename = None
        self._title = None
        self._modified_by = None
        self._created_by = None
        self._attachment_type = None
        self._created_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if issue_id is not None:
            self.issue_id = issue_id
        if disk_directory is not None:
            self.disk_directory = disk_directory
        if file_size is not None:
            self.file_size = file_size
        if store_filename is not None:
            self.store_filename = store_filename
        if title is not None:
            self.title = title
        if modified_by is not None:
            self.modified_by = modified_by
        if created_by is not None:
            self.created_by = created_by
        if attachment_type is not None:
            self.attachment_type = attachment_type
        if created_date is not None:
            self.created_date = created_date

    @property
    def id(self):
        r"""Gets the id of this AttachmentEntity.

        附件Id

        :return: The id of this AttachmentEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AttachmentEntity.

        附件Id

        :param id: The id of this AttachmentEntity.
        :type id: str
        """
        self._id = id

    @property
    def issue_id(self):
        r"""Gets the issue_id of this AttachmentEntity.

        附件所属工作项Id

        :return: The issue_id of this AttachmentEntity.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this AttachmentEntity.

        附件所属工作项Id

        :param issue_id: The issue_id of this AttachmentEntity.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def disk_directory(self):
        r"""Gets the disk_directory of this AttachmentEntity.

        在服务器存储的相对路径

        :return: The disk_directory of this AttachmentEntity.
        :rtype: str
        """
        return self._disk_directory

    @disk_directory.setter
    def disk_directory(self, disk_directory):
        r"""Sets the disk_directory of this AttachmentEntity.

        在服务器存储的相对路径

        :param disk_directory: The disk_directory of this AttachmentEntity.
        :type disk_directory: str
        """
        self._disk_directory = disk_directory

    @property
    def file_size(self):
        r"""Gets the file_size of this AttachmentEntity.

        附件大小，单位为Byte，单个附件最大为200MB

        :return: The file_size of this AttachmentEntity.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this AttachmentEntity.

        附件大小，单位为Byte，单个附件最大为200MB

        :param file_size: The file_size of this AttachmentEntity.
        :type file_size: str
        """
        self._file_size = file_size

    @property
    def store_filename(self):
        r"""Gets the store_filename of this AttachmentEntity.

        附件原名称

        :return: The store_filename of this AttachmentEntity.
        :rtype: str
        """
        return self._store_filename

    @store_filename.setter
    def store_filename(self, store_filename):
        r"""Sets the store_filename of this AttachmentEntity.

        附件原名称

        :param store_filename: The store_filename of this AttachmentEntity.
        :type store_filename: str
        """
        self._store_filename = store_filename

    @property
    def title(self):
        r"""Gets the title of this AttachmentEntity.

        附件在数据库中存储的名称。格式为uuid+.扩展名

        :return: The title of this AttachmentEntity.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this AttachmentEntity.

        附件在数据库中存储的名称。格式为uuid+.扩展名

        :param title: The title of this AttachmentEntity.
        :type title: str
        """
        self._title = title

    @property
    def modified_by(self):
        r"""Gets the modified_by of this AttachmentEntity.

        :return: The modified_by of this AttachmentEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this AttachmentEntity.

        :param modified_by: The modified_by of this AttachmentEntity.
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._modified_by = modified_by

    @property
    def created_by(self):
        r"""Gets the created_by of this AttachmentEntity.

        :return: The created_by of this AttachmentEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this AttachmentEntity.

        :param created_by: The created_by of this AttachmentEntity.
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._created_by = created_by

    @property
    def attachment_type(self):
        r"""Gets the attachment_type of this AttachmentEntity.

        附件类型，即文件扩展名

        :return: The attachment_type of this AttachmentEntity.
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        r"""Sets the attachment_type of this AttachmentEntity.

        附件类型，即文件扩展名

        :param attachment_type: The attachment_type of this AttachmentEntity.
        :type attachment_type: str
        """
        self._attachment_type = attachment_type

    @property
    def created_date(self):
        r"""Gets the created_date of this AttachmentEntity.

        附件上传时间的时间戳

        :return: The created_date of this AttachmentEntity.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this AttachmentEntity.

        附件上传时间的时间戳

        :param created_date: The created_date of this AttachmentEntity.
        :type created_date: str
        """
        self._created_date = created_date

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
        if not isinstance(other, AttachmentEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
