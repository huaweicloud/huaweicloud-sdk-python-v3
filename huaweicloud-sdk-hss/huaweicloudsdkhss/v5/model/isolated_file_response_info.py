# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsolatedFileResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'file_hash': 'str',
        'file_path': 'str',
        'isolation_status': 'str',
        'file_attr': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'file_hash': 'file_hash',
        'file_path': 'file_path',
        'isolation_status': 'isolation_status',
        'file_attr': 'file_attr',
        'update_time': 'update_time'
    }

    def __init__(self, host_id=None, host_name=None, file_hash=None, file_path=None, isolation_status=None, file_attr=None, update_time=None):
        """IsolatedFileResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: 服务器ID
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param file_hash: 文件哈希
        :type file_hash: str
        :param file_path: 文件路径
        :type file_path: str
        :param isolation_status: 隔离状态，包含如下:   - isolated : 已隔离   - restored : 已恢复   - isolating : 已下发隔离任务   - restoring : 已下发恢复任务
        :type isolation_status: str
        :param file_attr: 文件属性
        :type file_attr: str
        :param update_time: 更新时间，毫秒
        :type update_time: int
        """
        
        

        self._host_id = None
        self._host_name = None
        self._file_hash = None
        self._file_path = None
        self._isolation_status = None
        self._file_attr = None
        self._update_time = None
        self.discriminator = None

        self.host_id = host_id
        self.host_name = host_name
        self.file_hash = file_hash
        self.file_path = file_path
        self.isolation_status = isolation_status
        self.file_attr = file_attr
        self.update_time = update_time

    @property
    def host_id(self):
        """Gets the host_id of this IsolatedFileResponseInfo.

        服务器ID

        :return: The host_id of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this IsolatedFileResponseInfo.

        服务器ID

        :param host_id: The host_id of this IsolatedFileResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this IsolatedFileResponseInfo.

        服务器名称

        :return: The host_name of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this IsolatedFileResponseInfo.

        服务器名称

        :param host_name: The host_name of this IsolatedFileResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def file_hash(self):
        """Gets the file_hash of this IsolatedFileResponseInfo.

        文件哈希

        :return: The file_hash of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        """Sets the file_hash of this IsolatedFileResponseInfo.

        文件哈希

        :param file_hash: The file_hash of this IsolatedFileResponseInfo.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def file_path(self):
        """Gets the file_path of this IsolatedFileResponseInfo.

        文件路径

        :return: The file_path of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this IsolatedFileResponseInfo.

        文件路径

        :param file_path: The file_path of this IsolatedFileResponseInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def isolation_status(self):
        """Gets the isolation_status of this IsolatedFileResponseInfo.

        隔离状态，包含如下:   - isolated : 已隔离   - restored : 已恢复   - isolating : 已下发隔离任务   - restoring : 已下发恢复任务

        :return: The isolation_status of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._isolation_status

    @isolation_status.setter
    def isolation_status(self, isolation_status):
        """Sets the isolation_status of this IsolatedFileResponseInfo.

        隔离状态，包含如下:   - isolated : 已隔离   - restored : 已恢复   - isolating : 已下发隔离任务   - restoring : 已下发恢复任务

        :param isolation_status: The isolation_status of this IsolatedFileResponseInfo.
        :type isolation_status: str
        """
        self._isolation_status = isolation_status

    @property
    def file_attr(self):
        """Gets the file_attr of this IsolatedFileResponseInfo.

        文件属性

        :return: The file_attr of this IsolatedFileResponseInfo.
        :rtype: str
        """
        return self._file_attr

    @file_attr.setter
    def file_attr(self, file_attr):
        """Sets the file_attr of this IsolatedFileResponseInfo.

        文件属性

        :param file_attr: The file_attr of this IsolatedFileResponseInfo.
        :type file_attr: str
        """
        self._file_attr = file_attr

    @property
    def update_time(self):
        """Gets the update_time of this IsolatedFileResponseInfo.

        更新时间，毫秒

        :return: The update_time of this IsolatedFileResponseInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this IsolatedFileResponseInfo.

        更新时间，毫秒

        :param update_time: The update_time of this IsolatedFileResponseInfo.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, IsolatedFileResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
