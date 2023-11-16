# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResultsTopnBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index_traffic': 'float',
        'storage': 'float',
        'write_traffic': 'float',
        'log_group_id': 'str',
        'log_group_name': 'str',
        'log_stream_id': 'str',
        'log_stream_name': 'str',
        'basic_transfer': 'float',
        'senior_transfer': 'float',
        'is_agency_transfer': 'bool',
        'cold_storage': 'float'
    }

    attribute_map = {
        'index_traffic': 'index_traffic',
        'storage': 'storage',
        'write_traffic': 'write_traffic',
        'log_group_id': 'log_group_id',
        'log_group_name': 'log_group_name',
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'basic_transfer': 'basic_transfer',
        'senior_transfer': 'senior_transfer',
        'is_agency_transfer': 'is_agency_transfer',
        'cold_storage': 'cold_storage'
    }

    def __init__(self, index_traffic=None, storage=None, write_traffic=None, log_group_id=None, log_group_name=None, log_stream_id=None, log_stream_name=None, basic_transfer=None, senior_transfer=None, is_agency_transfer=None, cold_storage=None):
        """ResultsTopnBody

        The model defined in huaweicloud sdk

        :param index_traffic: 索引流量，byte, 查询数据类型中包含index时返回
        :type index_traffic: float
        :param storage: 存储量，byte, 查询数据类型中包含storage时返回
        :type storage: float
        :param write_traffic: 写入流量，byte, 查询数据类型中包含write时返回
        :type write_traffic: float
        :param log_group_id: 日志组id，资源类型为日志组时返回
        :type log_group_id: str
        :param log_group_name: 日志组名称，资源类型为日志组时返回
        :type log_group_name: str
        :param log_stream_id: 日志流id，资源类型为日志流时返回
        :type log_stream_id: str
        :param log_stream_name: 日志流名称，资源类型为日志流时返回
        :type log_stream_name: str
        :param basic_transfer: 基础转储流量，byte, 查询数据类型中包含basicTransfer时返回
        :type basic_transfer: float
        :param senior_transfer: 基础转储流量，byte, 查询数据类型中包含seniorTransfer时返回
        :type senior_transfer: float
        :param is_agency_transfer: 不是委托转储，true，是委托转储，则前端资源统计展示的流不能跳
        :type is_agency_transfer: bool
        :param cold_storage: 冷存储量
        :type cold_storage: float
        """
        
        

        self._index_traffic = None
        self._storage = None
        self._write_traffic = None
        self._log_group_id = None
        self._log_group_name = None
        self._log_stream_id = None
        self._log_stream_name = None
        self._basic_transfer = None
        self._senior_transfer = None
        self._is_agency_transfer = None
        self._cold_storage = None
        self.discriminator = None

        self.index_traffic = index_traffic
        self.storage = storage
        self.write_traffic = write_traffic
        self.log_group_id = log_group_id
        self.log_group_name = log_group_name
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        if basic_transfer is not None:
            self.basic_transfer = basic_transfer
        if senior_transfer is not None:
            self.senior_transfer = senior_transfer
        if is_agency_transfer is not None:
            self.is_agency_transfer = is_agency_transfer
        if cold_storage is not None:
            self.cold_storage = cold_storage

    @property
    def index_traffic(self):
        """Gets the index_traffic of this ResultsTopnBody.

        索引流量，byte, 查询数据类型中包含index时返回

        :return: The index_traffic of this ResultsTopnBody.
        :rtype: float
        """
        return self._index_traffic

    @index_traffic.setter
    def index_traffic(self, index_traffic):
        """Sets the index_traffic of this ResultsTopnBody.

        索引流量，byte, 查询数据类型中包含index时返回

        :param index_traffic: The index_traffic of this ResultsTopnBody.
        :type index_traffic: float
        """
        self._index_traffic = index_traffic

    @property
    def storage(self):
        """Gets the storage of this ResultsTopnBody.

        存储量，byte, 查询数据类型中包含storage时返回

        :return: The storage of this ResultsTopnBody.
        :rtype: float
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this ResultsTopnBody.

        存储量，byte, 查询数据类型中包含storage时返回

        :param storage: The storage of this ResultsTopnBody.
        :type storage: float
        """
        self._storage = storage

    @property
    def write_traffic(self):
        """Gets the write_traffic of this ResultsTopnBody.

        写入流量，byte, 查询数据类型中包含write时返回

        :return: The write_traffic of this ResultsTopnBody.
        :rtype: float
        """
        return self._write_traffic

    @write_traffic.setter
    def write_traffic(self, write_traffic):
        """Sets the write_traffic of this ResultsTopnBody.

        写入流量，byte, 查询数据类型中包含write时返回

        :param write_traffic: The write_traffic of this ResultsTopnBody.
        :type write_traffic: float
        """
        self._write_traffic = write_traffic

    @property
    def log_group_id(self):
        """Gets the log_group_id of this ResultsTopnBody.

        日志组id，资源类型为日志组时返回

        :return: The log_group_id of this ResultsTopnBody.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this ResultsTopnBody.

        日志组id，资源类型为日志组时返回

        :param log_group_id: The log_group_id of this ResultsTopnBody.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        """Gets the log_group_name of this ResultsTopnBody.

        日志组名称，资源类型为日志组时返回

        :return: The log_group_name of this ResultsTopnBody.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        """Sets the log_group_name of this ResultsTopnBody.

        日志组名称，资源类型为日志组时返回

        :param log_group_name: The log_group_name of this ResultsTopnBody.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this ResultsTopnBody.

        日志流id，资源类型为日志流时返回

        :return: The log_stream_id of this ResultsTopnBody.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this ResultsTopnBody.

        日志流id，资源类型为日志流时返回

        :param log_stream_id: The log_stream_id of this ResultsTopnBody.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        """Gets the log_stream_name of this ResultsTopnBody.

        日志流名称，资源类型为日志流时返回

        :return: The log_stream_name of this ResultsTopnBody.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        """Sets the log_stream_name of this ResultsTopnBody.

        日志流名称，资源类型为日志流时返回

        :param log_stream_name: The log_stream_name of this ResultsTopnBody.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def basic_transfer(self):
        """Gets the basic_transfer of this ResultsTopnBody.

        基础转储流量，byte, 查询数据类型中包含basicTransfer时返回

        :return: The basic_transfer of this ResultsTopnBody.
        :rtype: float
        """
        return self._basic_transfer

    @basic_transfer.setter
    def basic_transfer(self, basic_transfer):
        """Sets the basic_transfer of this ResultsTopnBody.

        基础转储流量，byte, 查询数据类型中包含basicTransfer时返回

        :param basic_transfer: The basic_transfer of this ResultsTopnBody.
        :type basic_transfer: float
        """
        self._basic_transfer = basic_transfer

    @property
    def senior_transfer(self):
        """Gets the senior_transfer of this ResultsTopnBody.

        基础转储流量，byte, 查询数据类型中包含seniorTransfer时返回

        :return: The senior_transfer of this ResultsTopnBody.
        :rtype: float
        """
        return self._senior_transfer

    @senior_transfer.setter
    def senior_transfer(self, senior_transfer):
        """Sets the senior_transfer of this ResultsTopnBody.

        基础转储流量，byte, 查询数据类型中包含seniorTransfer时返回

        :param senior_transfer: The senior_transfer of this ResultsTopnBody.
        :type senior_transfer: float
        """
        self._senior_transfer = senior_transfer

    @property
    def is_agency_transfer(self):
        """Gets the is_agency_transfer of this ResultsTopnBody.

        不是委托转储，true，是委托转储，则前端资源统计展示的流不能跳

        :return: The is_agency_transfer of this ResultsTopnBody.
        :rtype: bool
        """
        return self._is_agency_transfer

    @is_agency_transfer.setter
    def is_agency_transfer(self, is_agency_transfer):
        """Sets the is_agency_transfer of this ResultsTopnBody.

        不是委托转储，true，是委托转储，则前端资源统计展示的流不能跳

        :param is_agency_transfer: The is_agency_transfer of this ResultsTopnBody.
        :type is_agency_transfer: bool
        """
        self._is_agency_transfer = is_agency_transfer

    @property
    def cold_storage(self):
        """Gets the cold_storage of this ResultsTopnBody.

        冷存储量

        :return: The cold_storage of this ResultsTopnBody.
        :rtype: float
        """
        return self._cold_storage

    @cold_storage.setter
    def cold_storage(self, cold_storage):
        """Sets the cold_storage of this ResultsTopnBody.

        冷存储量

        :param cold_storage: The cold_storage of this ResultsTopnBody.
        :type cold_storage: float
        """
        self._cold_storage = cold_storage

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
        if not isinstance(other, ResultsTopnBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
