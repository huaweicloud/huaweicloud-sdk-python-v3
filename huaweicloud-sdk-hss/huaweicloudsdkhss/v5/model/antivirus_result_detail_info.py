# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntivirusResultDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_id': 'str',
        'malware_name': 'str',
        'file_path': 'str',
        'file_hash': 'str',
        'file_size': 'int',
        'file_owner': 'str',
        'file_attr': 'str',
        'file_ctime': 'int',
        'file_mtime': 'int',
        'update_time': 'int',
        'agent_id': 'str'
    }

    attribute_map = {
        'result_id': 'result_id',
        'malware_name': 'malware_name',
        'file_path': 'file_path',
        'file_hash': 'file_hash',
        'file_size': 'file_size',
        'file_owner': 'file_owner',
        'file_attr': 'file_attr',
        'file_ctime': 'file_ctime',
        'file_mtime': 'file_mtime',
        'update_time': 'update_time',
        'agent_id': 'agent_id'
    }

    def __init__(self, result_id=None, malware_name=None, file_path=None, file_hash=None, file_size=None, file_owner=None, file_attr=None, file_ctime=None, file_mtime=None, update_time=None, agent_id=None):
        """AntivirusResultDetailInfo

        The model defined in huaweicloud sdk

        :param result_id: 病毒查杀结果ID
        :type result_id: str
        :param malware_name: 病毒名称
        :type malware_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param file_hash: 文件哈希
        :type file_hash: str
        :param file_size: 文件大小
        :type file_size: int
        :param file_owner: 文件属主
        :type file_owner: str
        :param file_attr: 文件属性
        :type file_attr: str
        :param file_ctime: 文件创建时间
        :type file_ctime: int
        :param file_mtime: 文件更新时间
        :type file_mtime: int
        :param update_time: 更新时间，毫秒
        :type update_time: int
        :param agent_id: Agent ID
        :type agent_id: str
        """
        
        

        self._result_id = None
        self._malware_name = None
        self._file_path = None
        self._file_hash = None
        self._file_size = None
        self._file_owner = None
        self._file_attr = None
        self._file_ctime = None
        self._file_mtime = None
        self._update_time = None
        self._agent_id = None
        self.discriminator = None

        if result_id is not None:
            self.result_id = result_id
        if malware_name is not None:
            self.malware_name = malware_name
        if file_path is not None:
            self.file_path = file_path
        if file_hash is not None:
            self.file_hash = file_hash
        if file_size is not None:
            self.file_size = file_size
        if file_owner is not None:
            self.file_owner = file_owner
        if file_attr is not None:
            self.file_attr = file_attr
        if file_ctime is not None:
            self.file_ctime = file_ctime
        if file_mtime is not None:
            self.file_mtime = file_mtime
        if update_time is not None:
            self.update_time = update_time
        if agent_id is not None:
            self.agent_id = agent_id

    @property
    def result_id(self):
        """Gets the result_id of this AntivirusResultDetailInfo.

        病毒查杀结果ID

        :return: The result_id of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        """Sets the result_id of this AntivirusResultDetailInfo.

        病毒查杀结果ID

        :param result_id: The result_id of this AntivirusResultDetailInfo.
        :type result_id: str
        """
        self._result_id = result_id

    @property
    def malware_name(self):
        """Gets the malware_name of this AntivirusResultDetailInfo.

        病毒名称

        :return: The malware_name of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._malware_name

    @malware_name.setter
    def malware_name(self, malware_name):
        """Sets the malware_name of this AntivirusResultDetailInfo.

        病毒名称

        :param malware_name: The malware_name of this AntivirusResultDetailInfo.
        :type malware_name: str
        """
        self._malware_name = malware_name

    @property
    def file_path(self):
        """Gets the file_path of this AntivirusResultDetailInfo.

        文件路径

        :return: The file_path of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this AntivirusResultDetailInfo.

        文件路径

        :param file_path: The file_path of this AntivirusResultDetailInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_hash(self):
        """Gets the file_hash of this AntivirusResultDetailInfo.

        文件哈希

        :return: The file_hash of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        """Sets the file_hash of this AntivirusResultDetailInfo.

        文件哈希

        :param file_hash: The file_hash of this AntivirusResultDetailInfo.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def file_size(self):
        """Gets the file_size of this AntivirusResultDetailInfo.

        文件大小

        :return: The file_size of this AntivirusResultDetailInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this AntivirusResultDetailInfo.

        文件大小

        :param file_size: The file_size of this AntivirusResultDetailInfo.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def file_owner(self):
        """Gets the file_owner of this AntivirusResultDetailInfo.

        文件属主

        :return: The file_owner of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._file_owner

    @file_owner.setter
    def file_owner(self, file_owner):
        """Sets the file_owner of this AntivirusResultDetailInfo.

        文件属主

        :param file_owner: The file_owner of this AntivirusResultDetailInfo.
        :type file_owner: str
        """
        self._file_owner = file_owner

    @property
    def file_attr(self):
        """Gets the file_attr of this AntivirusResultDetailInfo.

        文件属性

        :return: The file_attr of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._file_attr

    @file_attr.setter
    def file_attr(self, file_attr):
        """Sets the file_attr of this AntivirusResultDetailInfo.

        文件属性

        :param file_attr: The file_attr of this AntivirusResultDetailInfo.
        :type file_attr: str
        """
        self._file_attr = file_attr

    @property
    def file_ctime(self):
        """Gets the file_ctime of this AntivirusResultDetailInfo.

        文件创建时间

        :return: The file_ctime of this AntivirusResultDetailInfo.
        :rtype: int
        """
        return self._file_ctime

    @file_ctime.setter
    def file_ctime(self, file_ctime):
        """Sets the file_ctime of this AntivirusResultDetailInfo.

        文件创建时间

        :param file_ctime: The file_ctime of this AntivirusResultDetailInfo.
        :type file_ctime: int
        """
        self._file_ctime = file_ctime

    @property
    def file_mtime(self):
        """Gets the file_mtime of this AntivirusResultDetailInfo.

        文件更新时间

        :return: The file_mtime of this AntivirusResultDetailInfo.
        :rtype: int
        """
        return self._file_mtime

    @file_mtime.setter
    def file_mtime(self, file_mtime):
        """Sets the file_mtime of this AntivirusResultDetailInfo.

        文件更新时间

        :param file_mtime: The file_mtime of this AntivirusResultDetailInfo.
        :type file_mtime: int
        """
        self._file_mtime = file_mtime

    @property
    def update_time(self):
        """Gets the update_time of this AntivirusResultDetailInfo.

        更新时间，毫秒

        :return: The update_time of this AntivirusResultDetailInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AntivirusResultDetailInfo.

        更新时间，毫秒

        :param update_time: The update_time of this AntivirusResultDetailInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def agent_id(self):
        """Gets the agent_id of this AntivirusResultDetailInfo.

        Agent ID

        :return: The agent_id of this AntivirusResultDetailInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this AntivirusResultDetailInfo.

        Agent ID

        :param agent_id: The agent_id of this AntivirusResultDetailInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

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
        if not isinstance(other, AntivirusResultDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
