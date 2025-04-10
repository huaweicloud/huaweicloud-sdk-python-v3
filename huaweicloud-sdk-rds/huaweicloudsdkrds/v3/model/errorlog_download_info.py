# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorlogDownloadInfo:

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
        r"""ErrorlogDownloadInfo

        The model defined in huaweicloud sdk

        :param workflow_id: 任务ID
        :type workflow_id: str
        :param file_name: 生成的下载文件名
        :type file_name: str
        :param status: 生成链接的生成状态
        :type status: str
        :param file_size: 文件大小
        :type file_size: str
        :param file_link: 下载链接
        :type file_link: str
        :param create_at: 生成时间
        :type create_at: int
        :param update_at: 更新时间
        :type update_at: int
        """
        
        

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
        r"""Gets the workflow_id of this ErrorlogDownloadInfo.

        任务ID

        :return: The workflow_id of this ErrorlogDownloadInfo.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this ErrorlogDownloadInfo.

        任务ID

        :param workflow_id: The workflow_id of this ErrorlogDownloadInfo.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def file_name(self):
        r"""Gets the file_name of this ErrorlogDownloadInfo.

        生成的下载文件名

        :return: The file_name of this ErrorlogDownloadInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ErrorlogDownloadInfo.

        生成的下载文件名

        :param file_name: The file_name of this ErrorlogDownloadInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def status(self):
        r"""Gets the status of this ErrorlogDownloadInfo.

        生成链接的生成状态

        :return: The status of this ErrorlogDownloadInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ErrorlogDownloadInfo.

        生成链接的生成状态

        :param status: The status of this ErrorlogDownloadInfo.
        :type status: str
        """
        self._status = status

    @property
    def file_size(self):
        r"""Gets the file_size of this ErrorlogDownloadInfo.

        文件大小

        :return: The file_size of this ErrorlogDownloadInfo.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this ErrorlogDownloadInfo.

        文件大小

        :param file_size: The file_size of this ErrorlogDownloadInfo.
        :type file_size: str
        """
        self._file_size = file_size

    @property
    def file_link(self):
        r"""Gets the file_link of this ErrorlogDownloadInfo.

        下载链接

        :return: The file_link of this ErrorlogDownloadInfo.
        :rtype: str
        """
        return self._file_link

    @file_link.setter
    def file_link(self, file_link):
        r"""Sets the file_link of this ErrorlogDownloadInfo.

        下载链接

        :param file_link: The file_link of this ErrorlogDownloadInfo.
        :type file_link: str
        """
        self._file_link = file_link

    @property
    def create_at(self):
        r"""Gets the create_at of this ErrorlogDownloadInfo.

        生成时间

        :return: The create_at of this ErrorlogDownloadInfo.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this ErrorlogDownloadInfo.

        生成时间

        :param create_at: The create_at of this ErrorlogDownloadInfo.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this ErrorlogDownloadInfo.

        更新时间

        :return: The update_at of this ErrorlogDownloadInfo.
        :rtype: int
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ErrorlogDownloadInfo.

        更新时间

        :param update_at: The update_at of this ErrorlogDownloadInfo.
        :type update_at: int
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
        if not isinstance(other, ErrorlogDownloadInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
