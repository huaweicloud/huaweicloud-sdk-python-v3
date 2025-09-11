# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachmentVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attachment_type': 'str',
        'created_by': 'object',
        'created_date': 'str',
        'description': 'str',
        'disk_directory': 'str',
        'filesize': 'str',
        'id': 'str',
        'modified_by': 'object',
        'store_filename': 'str',
        'title': 'str',
        'workitem_id': 'str'
    }

    attribute_map = {
        'attachment_type': 'attachment_type',
        'created_by': 'created_by',
        'created_date': 'created_date',
        'description': 'description',
        'disk_directory': 'disk_directory',
        'filesize': 'filesize',
        'id': 'id',
        'modified_by': 'modified_by',
        'store_filename': 'store_filename',
        'title': 'title',
        'workitem_id': 'workitem_id'
    }

    def __init__(self, attachment_type=None, created_by=None, created_date=None, description=None, disk_directory=None, filesize=None, id=None, modified_by=None, store_filename=None, title=None, workitem_id=None):
        r"""AttachmentVO

        The model defined in huaweicloud sdk

        :param attachment_type: 附件类型
        :type attachment_type: str
        :param created_by: 创建人信息
        :type created_by: object
        :param created_date: 创建时间
        :type created_date: str
        :param description: 附件描述
        :type description: str
        :param disk_directory: 存储路径
        :type disk_directory: str
        :param filesize: 文件大小
        :type filesize: str
        :param id: 文件id
        :type id: str
        :param modified_by: 更新人信息
        :type modified_by: object
        :param store_filename: 文件名称
        :type store_filename: str
        :param title: 文件hash名称
        :type title: str
        :param workitem_id: 工作项id
        :type workitem_id: str
        """
        
        

        self._attachment_type = None
        self._created_by = None
        self._created_date = None
        self._description = None
        self._disk_directory = None
        self._filesize = None
        self._id = None
        self._modified_by = None
        self._store_filename = None
        self._title = None
        self._workitem_id = None
        self.discriminator = None

        if attachment_type is not None:
            self.attachment_type = attachment_type
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if description is not None:
            self.description = description
        if disk_directory is not None:
            self.disk_directory = disk_directory
        if filesize is not None:
            self.filesize = filesize
        if id is not None:
            self.id = id
        if modified_by is not None:
            self.modified_by = modified_by
        if store_filename is not None:
            self.store_filename = store_filename
        if title is not None:
            self.title = title
        if workitem_id is not None:
            self.workitem_id = workitem_id

    @property
    def attachment_type(self):
        r"""Gets the attachment_type of this AttachmentVO.

        附件类型

        :return: The attachment_type of this AttachmentVO.
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        r"""Sets the attachment_type of this AttachmentVO.

        附件类型

        :param attachment_type: The attachment_type of this AttachmentVO.
        :type attachment_type: str
        """
        self._attachment_type = attachment_type

    @property
    def created_by(self):
        r"""Gets the created_by of this AttachmentVO.

        创建人信息

        :return: The created_by of this AttachmentVO.
        :rtype: object
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this AttachmentVO.

        创建人信息

        :param created_by: The created_by of this AttachmentVO.
        :type created_by: object
        """
        self._created_by = created_by

    @property
    def created_date(self):
        r"""Gets the created_date of this AttachmentVO.

        创建时间

        :return: The created_date of this AttachmentVO.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this AttachmentVO.

        创建时间

        :param created_date: The created_date of this AttachmentVO.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def description(self):
        r"""Gets the description of this AttachmentVO.

        附件描述

        :return: The description of this AttachmentVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AttachmentVO.

        附件描述

        :param description: The description of this AttachmentVO.
        :type description: str
        """
        self._description = description

    @property
    def disk_directory(self):
        r"""Gets the disk_directory of this AttachmentVO.

        存储路径

        :return: The disk_directory of this AttachmentVO.
        :rtype: str
        """
        return self._disk_directory

    @disk_directory.setter
    def disk_directory(self, disk_directory):
        r"""Sets the disk_directory of this AttachmentVO.

        存储路径

        :param disk_directory: The disk_directory of this AttachmentVO.
        :type disk_directory: str
        """
        self._disk_directory = disk_directory

    @property
    def filesize(self):
        r"""Gets the filesize of this AttachmentVO.

        文件大小

        :return: The filesize of this AttachmentVO.
        :rtype: str
        """
        return self._filesize

    @filesize.setter
    def filesize(self, filesize):
        r"""Sets the filesize of this AttachmentVO.

        文件大小

        :param filesize: The filesize of this AttachmentVO.
        :type filesize: str
        """
        self._filesize = filesize

    @property
    def id(self):
        r"""Gets the id of this AttachmentVO.

        文件id

        :return: The id of this AttachmentVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AttachmentVO.

        文件id

        :param id: The id of this AttachmentVO.
        :type id: str
        """
        self._id = id

    @property
    def modified_by(self):
        r"""Gets the modified_by of this AttachmentVO.

        更新人信息

        :return: The modified_by of this AttachmentVO.
        :rtype: object
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this AttachmentVO.

        更新人信息

        :param modified_by: The modified_by of this AttachmentVO.
        :type modified_by: object
        """
        self._modified_by = modified_by

    @property
    def store_filename(self):
        r"""Gets the store_filename of this AttachmentVO.

        文件名称

        :return: The store_filename of this AttachmentVO.
        :rtype: str
        """
        return self._store_filename

    @store_filename.setter
    def store_filename(self, store_filename):
        r"""Sets the store_filename of this AttachmentVO.

        文件名称

        :param store_filename: The store_filename of this AttachmentVO.
        :type store_filename: str
        """
        self._store_filename = store_filename

    @property
    def title(self):
        r"""Gets the title of this AttachmentVO.

        文件hash名称

        :return: The title of this AttachmentVO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this AttachmentVO.

        文件hash名称

        :param title: The title of this AttachmentVO.
        :type title: str
        """
        self._title = title

    @property
    def workitem_id(self):
        r"""Gets the workitem_id of this AttachmentVO.

        工作项id

        :return: The workitem_id of this AttachmentVO.
        :rtype: str
        """
        return self._workitem_id

    @workitem_id.setter
    def workitem_id(self, workitem_id):
        r"""Sets the workitem_id of this AttachmentVO.

        工作项id

        :param workitem_id: The workitem_id of this AttachmentVO.
        :type workitem_id: str
        """
        self._workitem_id = workitem_id

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
        if not isinstance(other, AttachmentVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
