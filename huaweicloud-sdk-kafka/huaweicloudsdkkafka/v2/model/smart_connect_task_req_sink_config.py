# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartConnectTaskReqSinkConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'consumer_strategy': 'str',
        'destination_file_type': 'str',
        'deliver_time_interval': 'int',
        'access_key': 'str',
        'secret_key': 'str',
        'obs_bucket_name': 'str',
        'obs_path': 'str',
        'partition_format': 'str',
        'record_delimiter': 'str',
        'store_keys': 'bool'
    }

    attribute_map = {
        'consumer_strategy': 'consumer_strategy',
        'destination_file_type': 'destination_file_type',
        'deliver_time_interval': 'deliver_time_interval',
        'access_key': 'access_key',
        'secret_key': 'secret_key',
        'obs_bucket_name': 'obs_bucket_name',
        'obs_path': 'obs_path',
        'partition_format': 'partition_format',
        'record_delimiter': 'record_delimiter',
        'store_keys': 'store_keys'
    }

    def __init__(self, consumer_strategy=None, destination_file_type=None, deliver_time_interval=None, access_key=None, secret_key=None, obs_bucket_name=None, obs_path=None, partition_format=None, record_delimiter=None, store_keys=None):
        r"""SmartConnectTaskReqSinkConfig

        The model defined in huaweicloud sdk

        :param consumer_strategy: 转储启动偏移量，latest为获取最新的数据，earliest为获取最早的数据。（仅目标端类型为OBS时需要填写）
        :type consumer_strategy: str
        :param destination_file_type: 转储文件格式。当前只支持TEXT。（仅目标端类型为OBS时需要填写）
        :type destination_file_type: str
        :param deliver_time_interval: 数据转储周期（秒），默认配置为300秒。（仅目标端类型为OBS时需要填写）
        :type deliver_time_interval: int
        :param access_key: AK，访问密钥ID。（仅目标端类型为OBS时需要填写）
        :type access_key: str
        :param secret_key: SK，与访问密钥ID结合使用的密钥。（仅目标端类型为OBS时需要填写）
        :type secret_key: str
        :param obs_bucket_name: 转储地址，即存储Topic数据的OBS桶的名称。（仅目标端类型为OBS时需要填写）
        :type obs_bucket_name: str
        :param obs_path: 转储目录，即OBS中存储Topic的目录，多级目录可以用“/”进行分隔。（仅目标端类型为OBS时需要填写）
        :type obs_path: str
        :param partition_format: 时间目录格式。（仅目标端类型为OBS时需要填写）   - yyyy：年   - yyyy/MM：年/月   - yyyy/MM/dd：年/月/日   - yyyy/MM/dd/HH：年/月/日/时   - yyyy/MM/dd/HH/mm：年/月/日/时/分 
        :type partition_format: str
        :param record_delimiter:  记录分行符，用于分隔写入转储文件的用户数据。（仅目标端类型为OBS时需要填写）   取值范围：   - 逗号“,”   - 分号“;”   - 竖线“|”   - 换行符“\\n”   - NULL 
        :type record_delimiter: str
        :param store_keys: 是否转储Key，开启表示转储Key，关闭表示不转储Key。（仅目标端类型为OBS时需要填写）
        :type store_keys: bool
        """
        
        

        self._consumer_strategy = None
        self._destination_file_type = None
        self._deliver_time_interval = None
        self._access_key = None
        self._secret_key = None
        self._obs_bucket_name = None
        self._obs_path = None
        self._partition_format = None
        self._record_delimiter = None
        self._store_keys = None
        self.discriminator = None

        if consumer_strategy is not None:
            self.consumer_strategy = consumer_strategy
        if destination_file_type is not None:
            self.destination_file_type = destination_file_type
        if deliver_time_interval is not None:
            self.deliver_time_interval = deliver_time_interval
        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if obs_path is not None:
            self.obs_path = obs_path
        if partition_format is not None:
            self.partition_format = partition_format
        if record_delimiter is not None:
            self.record_delimiter = record_delimiter
        if store_keys is not None:
            self.store_keys = store_keys

    @property
    def consumer_strategy(self):
        r"""Gets the consumer_strategy of this SmartConnectTaskReqSinkConfig.

        转储启动偏移量，latest为获取最新的数据，earliest为获取最早的数据。（仅目标端类型为OBS时需要填写）

        :return: The consumer_strategy of this SmartConnectTaskReqSinkConfig.
        :rtype: str
        """
        return self._consumer_strategy

    @consumer_strategy.setter
    def consumer_strategy(self, consumer_strategy):
        r"""Sets the consumer_strategy of this SmartConnectTaskReqSinkConfig.

        转储启动偏移量，latest为获取最新的数据，earliest为获取最早的数据。（仅目标端类型为OBS时需要填写）

        :param consumer_strategy: The consumer_strategy of this SmartConnectTaskReqSinkConfig.
        :type consumer_strategy: str
        """
        self._consumer_strategy = consumer_strategy

    @property
    def destination_file_type(self):
        r"""Gets the destination_file_type of this SmartConnectTaskReqSinkConfig.

        转储文件格式。当前只支持TEXT。（仅目标端类型为OBS时需要填写）

        :return: The destination_file_type of this SmartConnectTaskReqSinkConfig.
        :rtype: str
        """
        return self._destination_file_type

    @destination_file_type.setter
    def destination_file_type(self, destination_file_type):
        r"""Sets the destination_file_type of this SmartConnectTaskReqSinkConfig.

        转储文件格式。当前只支持TEXT。（仅目标端类型为OBS时需要填写）

        :param destination_file_type: The destination_file_type of this SmartConnectTaskReqSinkConfig.
        :type destination_file_type: str
        """
        self._destination_file_type = destination_file_type

    @property
    def deliver_time_interval(self):
        r"""Gets the deliver_time_interval of this SmartConnectTaskReqSinkConfig.

        数据转储周期（秒），默认配置为300秒。（仅目标端类型为OBS时需要填写）

        :return: The deliver_time_interval of this SmartConnectTaskReqSinkConfig.
        :rtype: int
        """
        return self._deliver_time_interval

    @deliver_time_interval.setter
    def deliver_time_interval(self, deliver_time_interval):
        r"""Sets the deliver_time_interval of this SmartConnectTaskReqSinkConfig.

        数据转储周期（秒），默认配置为300秒。（仅目标端类型为OBS时需要填写）

        :param deliver_time_interval: The deliver_time_interval of this SmartConnectTaskReqSinkConfig.
        :type deliver_time_interval: int
        """
        self._deliver_time_interval = deliver_time_interval

    @property
    def access_key(self):
        r"""Gets the access_key of this SmartConnectTaskReqSinkConfig.

        AK，访问密钥ID。（仅目标端类型为OBS时需要填写）

        :return: The access_key of this SmartConnectTaskReqSinkConfig.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this SmartConnectTaskReqSinkConfig.

        AK，访问密钥ID。（仅目标端类型为OBS时需要填写）

        :param access_key: The access_key of this SmartConnectTaskReqSinkConfig.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def secret_key(self):
        r"""Gets the secret_key of this SmartConnectTaskReqSinkConfig.

        SK，与访问密钥ID结合使用的密钥。（仅目标端类型为OBS时需要填写）

        :return: The secret_key of this SmartConnectTaskReqSinkConfig.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        r"""Sets the secret_key of this SmartConnectTaskReqSinkConfig.

        SK，与访问密钥ID结合使用的密钥。（仅目标端类型为OBS时需要填写）

        :param secret_key: The secret_key of this SmartConnectTaskReqSinkConfig.
        :type secret_key: str
        """
        self._secret_key = secret_key

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this SmartConnectTaskReqSinkConfig.

        转储地址，即存储Topic数据的OBS桶的名称。（仅目标端类型为OBS时需要填写）

        :return: The obs_bucket_name of this SmartConnectTaskReqSinkConfig.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this SmartConnectTaskReqSinkConfig.

        转储地址，即存储Topic数据的OBS桶的名称。（仅目标端类型为OBS时需要填写）

        :param obs_bucket_name: The obs_bucket_name of this SmartConnectTaskReqSinkConfig.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def obs_path(self):
        r"""Gets the obs_path of this SmartConnectTaskReqSinkConfig.

        转储目录，即OBS中存储Topic的目录，多级目录可以用“/”进行分隔。（仅目标端类型为OBS时需要填写）

        :return: The obs_path of this SmartConnectTaskReqSinkConfig.
        :rtype: str
        """
        return self._obs_path

    @obs_path.setter
    def obs_path(self, obs_path):
        r"""Sets the obs_path of this SmartConnectTaskReqSinkConfig.

        转储目录，即OBS中存储Topic的目录，多级目录可以用“/”进行分隔。（仅目标端类型为OBS时需要填写）

        :param obs_path: The obs_path of this SmartConnectTaskReqSinkConfig.
        :type obs_path: str
        """
        self._obs_path = obs_path

    @property
    def partition_format(self):
        r"""Gets the partition_format of this SmartConnectTaskReqSinkConfig.

        时间目录格式。（仅目标端类型为OBS时需要填写）   - yyyy：年   - yyyy/MM：年/月   - yyyy/MM/dd：年/月/日   - yyyy/MM/dd/HH：年/月/日/时   - yyyy/MM/dd/HH/mm：年/月/日/时/分 

        :return: The partition_format of this SmartConnectTaskReqSinkConfig.
        :rtype: str
        """
        return self._partition_format

    @partition_format.setter
    def partition_format(self, partition_format):
        r"""Sets the partition_format of this SmartConnectTaskReqSinkConfig.

        时间目录格式。（仅目标端类型为OBS时需要填写）   - yyyy：年   - yyyy/MM：年/月   - yyyy/MM/dd：年/月/日   - yyyy/MM/dd/HH：年/月/日/时   - yyyy/MM/dd/HH/mm：年/月/日/时/分 

        :param partition_format: The partition_format of this SmartConnectTaskReqSinkConfig.
        :type partition_format: str
        """
        self._partition_format = partition_format

    @property
    def record_delimiter(self):
        r"""Gets the record_delimiter of this SmartConnectTaskReqSinkConfig.

         记录分行符，用于分隔写入转储文件的用户数据。（仅目标端类型为OBS时需要填写）   取值范围：   - 逗号“,”   - 分号“;”   - 竖线“|”   - 换行符“\\n”   - NULL 

        :return: The record_delimiter of this SmartConnectTaskReqSinkConfig.
        :rtype: str
        """
        return self._record_delimiter

    @record_delimiter.setter
    def record_delimiter(self, record_delimiter):
        r"""Sets the record_delimiter of this SmartConnectTaskReqSinkConfig.

         记录分行符，用于分隔写入转储文件的用户数据。（仅目标端类型为OBS时需要填写）   取值范围：   - 逗号“,”   - 分号“;”   - 竖线“|”   - 换行符“\\n”   - NULL 

        :param record_delimiter: The record_delimiter of this SmartConnectTaskReqSinkConfig.
        :type record_delimiter: str
        """
        self._record_delimiter = record_delimiter

    @property
    def store_keys(self):
        r"""Gets the store_keys of this SmartConnectTaskReqSinkConfig.

        是否转储Key，开启表示转储Key，关闭表示不转储Key。（仅目标端类型为OBS时需要填写）

        :return: The store_keys of this SmartConnectTaskReqSinkConfig.
        :rtype: bool
        """
        return self._store_keys

    @store_keys.setter
    def store_keys(self, store_keys):
        r"""Sets the store_keys of this SmartConnectTaskReqSinkConfig.

        是否转储Key，开启表示转储Key，关闭表示不转储Key。（仅目标端类型为OBS时需要填写）

        :param store_keys: The store_keys of this SmartConnectTaskReqSinkConfig.
        :type store_keys: bool
        """
        self._store_keys = store_keys

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
        if not isinstance(other, SmartConnectTaskReqSinkConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
