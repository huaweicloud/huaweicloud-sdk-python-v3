# coding: utf-8

import pprint
import re

import six





class SlowlogDownloadInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'workflow_id': 'str',
        'file_name': 'str',
        'status': 'str',
        'file_size': 'str',
        'file_link': 'str',
        'create_at': 'int',
        'update_at': 'int'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'file_name': 'file_name',
        'status': 'status',
        'file_size': 'file_size',
        'file_link': 'file_link',
        'create_at': 'create_at',
        'update_at': 'update_at'
    }

    def __init__(self, workflow_id=None, file_name=None, status=None, file_size=None, file_link=None, create_at=None, update_at=None):
        """SlowlogDownloadInfo - a model defined in huaweicloud sdk"""
        
        

        self._workflow_id = None
        self._file_name = None
        self._status = None
        self._file_size = None
        self._file_link = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        self.workflow_id = workflow_id
        self.file_name = file_name
        self.status = status
        self.file_size = file_size
        self.file_link = file_link
        self.create_at = create_at
        self.update_at = update_at

    @property
    def workflow_id(self):
        """Gets the workflow_id of this SlowlogDownloadInfo.

        任务ID

        :return: The workflow_id of this SlowlogDownloadInfo.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this SlowlogDownloadInfo.

        任务ID

        :param workflow_id: The workflow_id of this SlowlogDownloadInfo.
        :type: str
        """
        self._workflow_id = workflow_id

    @property
    def file_name(self):
        """Gets the file_name of this SlowlogDownloadInfo.

        生成的下载文件名

        :return: The file_name of this SlowlogDownloadInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this SlowlogDownloadInfo.

        生成的下载文件名

        :param file_name: The file_name of this SlowlogDownloadInfo.
        :type: str
        """
        self._file_name = file_name

    @property
    def status(self):
        """Gets the status of this SlowlogDownloadInfo.

        生成链接的生成状态

        :return: The status of this SlowlogDownloadInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SlowlogDownloadInfo.

        生成链接的生成状态

        :param status: The status of this SlowlogDownloadInfo.
        :type: str
        """
        self._status = status

    @property
    def file_size(self):
        """Gets the file_size of this SlowlogDownloadInfo.

        文件大小

        :return: The file_size of this SlowlogDownloadInfo.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this SlowlogDownloadInfo.

        文件大小

        :param file_size: The file_size of this SlowlogDownloadInfo.
        :type: str
        """
        self._file_size = file_size

    @property
    def file_link(self):
        """Gets the file_link of this SlowlogDownloadInfo.

        下载链接

        :return: The file_link of this SlowlogDownloadInfo.
        :rtype: str
        """
        return self._file_link

    @file_link.setter
    def file_link(self, file_link):
        """Sets the file_link of this SlowlogDownloadInfo.

        下载链接

        :param file_link: The file_link of this SlowlogDownloadInfo.
        :type: str
        """
        self._file_link = file_link

    @property
    def create_at(self):
        """Gets the create_at of this SlowlogDownloadInfo.

        生成时间

        :return: The create_at of this SlowlogDownloadInfo.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this SlowlogDownloadInfo.

        生成时间

        :param create_at: The create_at of this SlowlogDownloadInfo.
        :type: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        """Gets the update_at of this SlowlogDownloadInfo.

        更新时间

        :return: The update_at of this SlowlogDownloadInfo.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this SlowlogDownloadInfo.

        更新时间

        :param update_at: The update_at of this SlowlogDownloadInfo.
        :type: int
        """
        self._update_at = update_at

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SlowlogDownloadInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
