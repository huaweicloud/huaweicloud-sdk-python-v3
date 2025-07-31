# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileEventResponseInfo:

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
        'file_name': 'str',
        'file_path': 'str',
        'status': 'str',
        'host_name': 'str',
        'change_type': 'str',
        'change_category': 'str',
        'after_change': 'str',
        'before_change': 'str',
        'latest_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'file_name': 'file_name',
        'file_path': 'file_path',
        'status': 'status',
        'host_name': 'host_name',
        'change_type': 'change_type',
        'change_category': 'change_category',
        'after_change': 'after_change',
        'before_change': 'before_change',
        'latest_time': 'latest_time'
    }

    def __init__(self, id=None, file_name=None, file_path=None, status=None, host_name=None, change_type=None, change_category=None, after_change=None, before_change=None, latest_time=None):
        r"""FileEventResponseInfo

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param file_name: 文件名称
        :type file_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param status: status
        :type status: str
        :param host_name: 服务器名称
        :type host_name: str
        :param change_type: 变更类型
        :type change_type: str
        :param change_category: 变更类别
        :type change_category: str
        :param after_change: modified hash
        :type after_change: str
        :param before_change: hash
        :type before_change: str
        :param latest_time: 最后变更时间
        :type latest_time: int
        """
        
        

        self._id = None
        self._file_name = None
        self._file_path = None
        self._status = None
        self._host_name = None
        self._change_type = None
        self._change_category = None
        self._after_change = None
        self._before_change = None
        self._latest_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if file_name is not None:
            self.file_name = file_name
        if file_path is not None:
            self.file_path = file_path
        if status is not None:
            self.status = status
        if host_name is not None:
            self.host_name = host_name
        if change_type is not None:
            self.change_type = change_type
        if change_category is not None:
            self.change_category = change_category
        if after_change is not None:
            self.after_change = after_change
        if before_change is not None:
            self.before_change = before_change
        if latest_time is not None:
            self.latest_time = latest_time

    @property
    def id(self):
        r"""Gets the id of this FileEventResponseInfo.

        id

        :return: The id of this FileEventResponseInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FileEventResponseInfo.

        id

        :param id: The id of this FileEventResponseInfo.
        :type id: int
        """
        self._id = id

    @property
    def file_name(self):
        r"""Gets the file_name of this FileEventResponseInfo.

        文件名称

        :return: The file_name of this FileEventResponseInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this FileEventResponseInfo.

        文件名称

        :param file_name: The file_name of this FileEventResponseInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_path(self):
        r"""Gets the file_path of this FileEventResponseInfo.

        文件路径

        :return: The file_path of this FileEventResponseInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this FileEventResponseInfo.

        文件路径

        :param file_path: The file_path of this FileEventResponseInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def status(self):
        r"""Gets the status of this FileEventResponseInfo.

        status

        :return: The status of this FileEventResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FileEventResponseInfo.

        status

        :param status: The status of this FileEventResponseInfo.
        :type status: str
        """
        self._status = status

    @property
    def host_name(self):
        r"""Gets the host_name of this FileEventResponseInfo.

        服务器名称

        :return: The host_name of this FileEventResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this FileEventResponseInfo.

        服务器名称

        :param host_name: The host_name of this FileEventResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def change_type(self):
        r"""Gets the change_type of this FileEventResponseInfo.

        变更类型

        :return: The change_type of this FileEventResponseInfo.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this FileEventResponseInfo.

        变更类型

        :param change_type: The change_type of this FileEventResponseInfo.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def change_category(self):
        r"""Gets the change_category of this FileEventResponseInfo.

        变更类别

        :return: The change_category of this FileEventResponseInfo.
        :rtype: str
        """
        return self._change_category

    @change_category.setter
    def change_category(self, change_category):
        r"""Sets the change_category of this FileEventResponseInfo.

        变更类别

        :param change_category: The change_category of this FileEventResponseInfo.
        :type change_category: str
        """
        self._change_category = change_category

    @property
    def after_change(self):
        r"""Gets the after_change of this FileEventResponseInfo.

        modified hash

        :return: The after_change of this FileEventResponseInfo.
        :rtype: str
        """
        return self._after_change

    @after_change.setter
    def after_change(self, after_change):
        r"""Sets the after_change of this FileEventResponseInfo.

        modified hash

        :param after_change: The after_change of this FileEventResponseInfo.
        :type after_change: str
        """
        self._after_change = after_change

    @property
    def before_change(self):
        r"""Gets the before_change of this FileEventResponseInfo.

        hash

        :return: The before_change of this FileEventResponseInfo.
        :rtype: str
        """
        return self._before_change

    @before_change.setter
    def before_change(self, before_change):
        r"""Sets the before_change of this FileEventResponseInfo.

        hash

        :param before_change: The before_change of this FileEventResponseInfo.
        :type before_change: str
        """
        self._before_change = before_change

    @property
    def latest_time(self):
        r"""Gets the latest_time of this FileEventResponseInfo.

        最后变更时间

        :return: The latest_time of this FileEventResponseInfo.
        :rtype: int
        """
        return self._latest_time

    @latest_time.setter
    def latest_time(self, latest_time):
        r"""Sets the latest_time of this FileEventResponseInfo.

        最后变更时间

        :param latest_time: The latest_time of this FileEventResponseInfo.
        :type latest_time: int
        """
        self._latest_time = latest_time

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
        if not isinstance(other, FileEventResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
