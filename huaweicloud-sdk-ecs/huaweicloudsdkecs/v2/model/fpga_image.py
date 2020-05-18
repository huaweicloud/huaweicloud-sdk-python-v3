# coding: utf-8

import pprint
import re

import six


class FpgaImage(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'size': 'int',
        'created_at': 'str',
        'protected': 'bool',
        'message': 'str',
        'metadata': 'dict(str, str)',
        'log_directory': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'size': 'size',
        'created_at': 'createdAt',
        'protected': 'protected',
        'message': 'message',
        'metadata': 'metadata',
        'log_directory': 'log_directory'
    }

    def __init__(self, id=None, name=None, description=None, status=None, size=None, created_at=None, protected=None, message=None, metadata=None, log_directory=None):  # noqa: E501
        """FpgaImage - a model defined in huaweicloud sdk"""

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._size = None
        self._created_at = None
        self._protected = None
        self._message = None
        self._metadata = None
        self._log_directory = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.size = size
        if created_at is not None:
            self.created_at = created_at
        self.protected = protected
        self.message = message
        self.metadata = metadata
        self.log_directory = log_directory

    @property
    def id(self):
        """Gets the id of this FpgaImage.

        FPGA镜像的ID。

        :return: The id of this FpgaImage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FpgaImage.

        FPGA镜像的ID。

        :param id: The id of this FpgaImage.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this FpgaImage.

        FPGA镜像的名称。

        :return: The name of this FpgaImage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FpgaImage.

        FPGA镜像的名称。

        :param name: The name of this FpgaImage.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this FpgaImage.

        FPGA镜像的描述信息。

        :return: The description of this FpgaImage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FpgaImage.

        FPGA镜像的描述信息。

        :param description: The description of this FpgaImage.
        :type: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this FpgaImage.

        FPGA镜像状态。取值如下：  - initialling：表示创建FPGA镜像任务初始化中。  - scheduling：表示FPGA镜像等待调度创建。  - creating：表示FPGA镜像正在创建中。  - saving：表示FPGA镜像正在上传文件到后端存储。  - deleting：表示FPGA镜像正在删除中。  - error：表示FPGA镜像创建失败。  - active：表示FPGA镜像可以正常使用。

        :return: The status of this FpgaImage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FpgaImage.

        FPGA镜像状态。取值如下：  - initialling：表示创建FPGA镜像任务初始化中。  - scheduling：表示FPGA镜像等待调度创建。  - creating：表示FPGA镜像正在创建中。  - saving：表示FPGA镜像正在上传文件到后端存储。  - deleting：表示FPGA镜像正在删除中。  - error：表示FPGA镜像创建失败。  - active：表示FPGA镜像可以正常使用。

        :param status: The status of this FpgaImage.
        :type: str
        """
        self._status = status

    @property
    def size(self):
        """Gets the size of this FpgaImage.

        FPGA镜像的文件大小，单位为MB。

        :return: The size of this FpgaImage.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FpgaImage.

        FPGA镜像的文件大小，单位为MB。

        :param size: The size of this FpgaImage.
        :type: int
        """
        self._size = size

    @property
    def created_at(self):
        """Gets the created_at of this FpgaImage.

        FPGA镜像的创建时间。  使用UTC（Coordinated Universal Time）时间。

        :return: The created_at of this FpgaImage.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FpgaImage.

        FPGA镜像的创建时间。  使用UTC（Coordinated Universal Time）时间。

        :param created_at: The created_at of this FpgaImage.
        :type: str
        """
        self._created_at = created_at

    @property
    def protected(self):
        """Gets the protected of this FpgaImage.

        该FPGA镜像是否受保护。  受保护是指，该FPGA镜像与创建弹性云服务器使用的镜像关联，此时，不可以执行删除FPGA镜像的操作。

        :return: The protected of this FpgaImage.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        """Sets the protected of this FpgaImage.

        该FPGA镜像是否受保护。  受保护是指，该FPGA镜像与创建弹性云服务器使用的镜像关联，此时，不可以执行删除FPGA镜像的操作。

        :param protected: The protected of this FpgaImage.
        :type: bool
        """
        self._protected = protected

    @property
    def message(self):
        """Gets the message of this FpgaImage.

        FPGA镜像的附加信息。

        :return: The message of this FpgaImage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this FpgaImage.

        FPGA镜像的附加信息。

        :param message: The message of this FpgaImage.
        :type: str
        """
        self._message = message

    @property
    def metadata(self):
        """Gets the metadata of this FpgaImage.

        FPGA镜像的元数据信息。

        :return: The metadata of this FpgaImage.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FpgaImage.

        FPGA镜像的元数据信息。

        :param metadata: The metadata of this FpgaImage.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def log_directory(self):
        """Gets the log_directory of this FpgaImage.

        FPGA镜像的构建日志文件在OBS中的目录路径，格式为“桶名:目录路径”，例如“obs-fpga:vu9p/log”。

        :return: The log_directory of this FpgaImage.
        :rtype: str
        """
        return self._log_directory

    @log_directory.setter
    def log_directory(self, log_directory):
        """Sets the log_directory of this FpgaImage.

        FPGA镜像的构建日志文件在OBS中的目录路径，格式为“桶名:目录路径”，例如“obs-fpga:vu9p/log”。

        :param log_directory: The log_directory of this FpgaImage.
        :type: str
        """
        self._log_directory = log_directory

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
        if not isinstance(other, FpgaImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
