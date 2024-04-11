# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowLogDownloadInfo:

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
        'instance_id': 'str',
        'node_id': 'str',
        'workflow_id': 'str',
        'file_name': 'str',
        'file_size': 'str',
        'file_link': 'str',
        'bucket_name': 'str',
        'created_at': 'int',
        'updated_at': 'int',
        'version': 'str',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'workflow_id': 'workflow_id',
        'file_name': 'file_name',
        'file_size': 'file_size',
        'file_link': 'file_link',
        'bucket_name': 'bucket_name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'version': 'version',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, id=None, instance_id=None, node_id=None, workflow_id=None, file_name=None, file_size=None, file_link=None, bucket_name=None, created_at=None, updated_at=None, version=None, status=None, message=None):
        """SlowLogDownloadInfo

        The model defined in huaweicloud sdk

        :param id: 慢日志ID
        :type id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param node_id: 节点ID
        :type node_id: str
        :param workflow_id: 工作流ID
        :type workflow_id: str
        :param file_name: 文件名
        :type file_name: str
        :param file_size: 文件大小, 单位：Byte
        :type file_size: str
        :param file_link: 文件下载链接
        :type file_link: str
        :param bucket_name: 桶名称
        :type bucket_name: str
        :param created_at: 创建时间
        :type created_at: int
        :param updated_at: 更新时间
        :type updated_at: int
        :param version: 版本
        :type version: str
        :param status: 状态
        :type status: str
        :param message: 消息
        :type message: str
        """
        
        

        self._id = None
        self._instance_id = None
        self._node_id = None
        self._workflow_id = None
        self._file_name = None
        self._file_size = None
        self._file_link = None
        self._bucket_name = None
        self._created_at = None
        self._updated_at = None
        self._version = None
        self._status = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if file_name is not None:
            self.file_name = file_name
        if file_size is not None:
            self.file_size = file_size
        if file_link is not None:
            self.file_link = file_link
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if version is not None:
            self.version = version
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def id(self):
        """Gets the id of this SlowLogDownloadInfo.

        慢日志ID

        :return: The id of this SlowLogDownloadInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlowLogDownloadInfo.

        慢日志ID

        :param id: The id of this SlowLogDownloadInfo.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this SlowLogDownloadInfo.

        实例ID

        :return: The instance_id of this SlowLogDownloadInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this SlowLogDownloadInfo.

        实例ID

        :param instance_id: The instance_id of this SlowLogDownloadInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        """Gets the node_id of this SlowLogDownloadInfo.

        节点ID

        :return: The node_id of this SlowLogDownloadInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this SlowLogDownloadInfo.

        节点ID

        :param node_id: The node_id of this SlowLogDownloadInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this SlowLogDownloadInfo.

        工作流ID

        :return: The workflow_id of this SlowLogDownloadInfo.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this SlowLogDownloadInfo.

        工作流ID

        :param workflow_id: The workflow_id of this SlowLogDownloadInfo.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def file_name(self):
        """Gets the file_name of this SlowLogDownloadInfo.

        文件名

        :return: The file_name of this SlowLogDownloadInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this SlowLogDownloadInfo.

        文件名

        :param file_name: The file_name of this SlowLogDownloadInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_size(self):
        """Gets the file_size of this SlowLogDownloadInfo.

        文件大小, 单位：Byte

        :return: The file_size of this SlowLogDownloadInfo.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this SlowLogDownloadInfo.

        文件大小, 单位：Byte

        :param file_size: The file_size of this SlowLogDownloadInfo.
        :type file_size: str
        """
        self._file_size = file_size

    @property
    def file_link(self):
        """Gets the file_link of this SlowLogDownloadInfo.

        文件下载链接

        :return: The file_link of this SlowLogDownloadInfo.
        :rtype: str
        """
        return self._file_link

    @file_link.setter
    def file_link(self, file_link):
        """Sets the file_link of this SlowLogDownloadInfo.

        文件下载链接

        :param file_link: The file_link of this SlowLogDownloadInfo.
        :type file_link: str
        """
        self._file_link = file_link

    @property
    def bucket_name(self):
        """Gets the bucket_name of this SlowLogDownloadInfo.

        桶名称

        :return: The bucket_name of this SlowLogDownloadInfo.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this SlowLogDownloadInfo.

        桶名称

        :param bucket_name: The bucket_name of this SlowLogDownloadInfo.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def created_at(self):
        """Gets the created_at of this SlowLogDownloadInfo.

        创建时间

        :return: The created_at of this SlowLogDownloadInfo.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SlowLogDownloadInfo.

        创建时间

        :param created_at: The created_at of this SlowLogDownloadInfo.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SlowLogDownloadInfo.

        更新时间

        :return: The updated_at of this SlowLogDownloadInfo.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SlowLogDownloadInfo.

        更新时间

        :param updated_at: The updated_at of this SlowLogDownloadInfo.
        :type updated_at: int
        """
        self._updated_at = updated_at

    @property
    def version(self):
        """Gets the version of this SlowLogDownloadInfo.

        版本

        :return: The version of this SlowLogDownloadInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SlowLogDownloadInfo.

        版本

        :param version: The version of this SlowLogDownloadInfo.
        :type version: str
        """
        self._version = version

    @property
    def status(self):
        """Gets the status of this SlowLogDownloadInfo.

        状态

        :return: The status of this SlowLogDownloadInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SlowLogDownloadInfo.

        状态

        :param status: The status of this SlowLogDownloadInfo.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        """Gets the message of this SlowLogDownloadInfo.

        消息

        :return: The message of this SlowLogDownloadInfo.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SlowLogDownloadInfo.

        消息

        :param message: The message of this SlowLogDownloadInfo.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, SlowLogDownloadInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
