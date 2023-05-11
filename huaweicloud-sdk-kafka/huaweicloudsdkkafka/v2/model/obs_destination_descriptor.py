# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsDestinationDescriptor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topics': 'str',
        'topics_regex': 'str',
        'consumer_strategy': 'str',
        'destination_file_type': 'str',
        'access_key': 'str',
        'secret_key': 'str',
        'obs_bucket_name': 'str',
        'obs_path': 'str',
        'partition_format': 'str',
        'record_delimiter': 'str',
        'deliver_time_interval': 'int'
    }

    attribute_map = {
        'topics': 'topics',
        'topics_regex': 'topics_regex',
        'consumer_strategy': 'consumer_strategy',
        'destination_file_type': 'destination_file_type',
        'access_key': 'access_key',
        'secret_key': 'secret_key',
        'obs_bucket_name': 'obs_bucket_name',
        'obs_path': 'obs_path',
        'partition_format': 'partition_format',
        'record_delimiter': 'record_delimiter',
        'deliver_time_interval': 'deliver_time_interval'
    }

    def __init__(self, topics=None, topics_regex=None, consumer_strategy=None, destination_file_type=None, access_key=None, secret_key=None, obs_bucket_name=None, obs_path=None, partition_format=None, record_delimiter=None, deliver_time_interval=None):
        """ObsDestinationDescriptor

        The model defined in huaweicloud sdk

        :param topics: 转存的topic列表名称，支持多个topic同时放置，以逗号“,”分隔。同时支持正则表达式。 例如topic1,topic2。 
        :type topics: str
        :param topics_regex: 转存topic的正则表达式，与topics必须二选一，不能同时都设置或者“.*”。 
        :type topics_regex: str
        :param consumer_strategy: 转储启动偏移量：   - latest: 从Topic最后端开始消费。   - earliest: 从Topic最前端消息开始消费。  默认是latest。 
        :type consumer_strategy: str
        :param destination_file_type: 转储文件格式。当前只支持text。 
        :type destination_file_type: str
        :param access_key: 访问密钥AK。 
        :type access_key: str
        :param secret_key: 访问密钥SK。 
        :type secret_key: str
        :param obs_bucket_name: 存储该通道数据的OBS桶名称。 
        :type obs_bucket_name: str
        :param obs_path: 存储在obs的路径，默认可以不填。 取值范围：英文字母、数字、下划线、中划线和斜杠，最大长度为64个字符。 默认配置为空。 
        :type obs_path: str
        :param partition_format: 将转储文件的生成时间使用“yyyy/MM/dd/HH/mm”格式生成分区字符串，用来定义写到OBS的Object文件所在的目录层次结构。   - N/A：置空，不使用日期时间目录。   - yyyy：年   - yyyy/MM：年/月   - yyyy/MM/dd：年/月/日   - yyyy/MM/dd/HH：年/月/日/时   - yyyy/MM/dd/HH/mm：年/月/日/时/分，例如：2017/11/10/14/49，目录结构就是“2017 &gt; 11 &gt; 10 &gt; 14 &gt; 49”，“2017”表示最外层文件夹。  默认值：空 &gt; 数据转储成功后，存储的目录结构为“obs_bucket_path/file_prefix/partition_format”。默认时间是GMT+8 时间 
        :type partition_format: str
        :param record_delimiter: 转储文件的记录分隔符，用于分隔写入转储文件的用户数据。 取值范围：   - 逗号“,”   - 分号“;”   - 竖线“|”   - 换行符“\\n”   - NULL  默认值：换行符“\\n”。 
        :type record_delimiter: str
        :param deliver_time_interval: 根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。 取值范围：30～900 单位：秒。 &gt; 使用OBS通道转储流式数据时该参数为必选配置。 
        :type deliver_time_interval: int
        """
        
        

        self._topics = None
        self._topics_regex = None
        self._consumer_strategy = None
        self._destination_file_type = None
        self._access_key = None
        self._secret_key = None
        self._obs_bucket_name = None
        self._obs_path = None
        self._partition_format = None
        self._record_delimiter = None
        self._deliver_time_interval = None
        self.discriminator = None

        self.topics = topics
        if topics_regex is not None:
            self.topics_regex = topics_regex
        self.consumer_strategy = consumer_strategy
        self.destination_file_type = destination_file_type
        self.access_key = access_key
        self.secret_key = secret_key
        self.obs_bucket_name = obs_bucket_name
        if obs_path is not None:
            self.obs_path = obs_path
        if partition_format is not None:
            self.partition_format = partition_format
        if record_delimiter is not None:
            self.record_delimiter = record_delimiter
        self.deliver_time_interval = deliver_time_interval

    @property
    def topics(self):
        """Gets the topics of this ObsDestinationDescriptor.

        转存的topic列表名称，支持多个topic同时放置，以逗号“,”分隔。同时支持正则表达式。 例如topic1,topic2。 

        :return: The topics of this ObsDestinationDescriptor.
        :rtype: str
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this ObsDestinationDescriptor.

        转存的topic列表名称，支持多个topic同时放置，以逗号“,”分隔。同时支持正则表达式。 例如topic1,topic2。 

        :param topics: The topics of this ObsDestinationDescriptor.
        :type topics: str
        """
        self._topics = topics

    @property
    def topics_regex(self):
        """Gets the topics_regex of this ObsDestinationDescriptor.

        转存topic的正则表达式，与topics必须二选一，不能同时都设置或者“.*”。 

        :return: The topics_regex of this ObsDestinationDescriptor.
        :rtype: str
        """
        return self._topics_regex

    @topics_regex.setter
    def topics_regex(self, topics_regex):
        """Sets the topics_regex of this ObsDestinationDescriptor.

        转存topic的正则表达式，与topics必须二选一，不能同时都设置或者“.*”。 

        :param topics_regex: The topics_regex of this ObsDestinationDescriptor.
        :type topics_regex: str
        """
        self._topics_regex = topics_regex

    @property
    def consumer_strategy(self):
        """Gets the consumer_strategy of this ObsDestinationDescriptor.

        转储启动偏移量：   - latest: 从Topic最后端开始消费。   - earliest: 从Topic最前端消息开始消费。  默认是latest。 

        :return: The consumer_strategy of this ObsDestinationDescriptor.
        :rtype: str
        """
        return self._consumer_strategy

    @consumer_strategy.setter
    def consumer_strategy(self, consumer_strategy):
        """Sets the consumer_strategy of this ObsDestinationDescriptor.

        转储启动偏移量：   - latest: 从Topic最后端开始消费。   - earliest: 从Topic最前端消息开始消费。  默认是latest。 

        :param consumer_strategy: The consumer_strategy of this ObsDestinationDescriptor.
        :type consumer_strategy: str
        """
        self._consumer_strategy = consumer_strategy

    @property
    def destination_file_type(self):
        """Gets the destination_file_type of this ObsDestinationDescriptor.

        转储文件格式。当前只支持text。 

        :return: The destination_file_type of this ObsDestinationDescriptor.
        :rtype: str
        """
        return self._destination_file_type

    @destination_file_type.setter
    def destination_file_type(self, destination_file_type):
        """Sets the destination_file_type of this ObsDestinationDescriptor.

        转储文件格式。当前只支持text。 

        :param destination_file_type: The destination_file_type of this ObsDestinationDescriptor.
        :type destination_file_type: str
        """
        self._destination_file_type = destination_file_type

    @property
    def access_key(self):
        """Gets the access_key of this ObsDestinationDescriptor.

        访问密钥AK。 

        :return: The access_key of this ObsDestinationDescriptor.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this ObsDestinationDescriptor.

        访问密钥AK。 

        :param access_key: The access_key of this ObsDestinationDescriptor.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def secret_key(self):
        """Gets the secret_key of this ObsDestinationDescriptor.

        访问密钥SK。 

        :return: The secret_key of this ObsDestinationDescriptor.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this ObsDestinationDescriptor.

        访问密钥SK。 

        :param secret_key: The secret_key of this ObsDestinationDescriptor.
        :type secret_key: str
        """
        self._secret_key = secret_key

    @property
    def obs_bucket_name(self):
        """Gets the obs_bucket_name of this ObsDestinationDescriptor.

        存储该通道数据的OBS桶名称。 

        :return: The obs_bucket_name of this ObsDestinationDescriptor.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        """Sets the obs_bucket_name of this ObsDestinationDescriptor.

        存储该通道数据的OBS桶名称。 

        :param obs_bucket_name: The obs_bucket_name of this ObsDestinationDescriptor.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def obs_path(self):
        """Gets the obs_path of this ObsDestinationDescriptor.

        存储在obs的路径，默认可以不填。 取值范围：英文字母、数字、下划线、中划线和斜杠，最大长度为64个字符。 默认配置为空。 

        :return: The obs_path of this ObsDestinationDescriptor.
        :rtype: str
        """
        return self._obs_path

    @obs_path.setter
    def obs_path(self, obs_path):
        """Sets the obs_path of this ObsDestinationDescriptor.

        存储在obs的路径，默认可以不填。 取值范围：英文字母、数字、下划线、中划线和斜杠，最大长度为64个字符。 默认配置为空。 

        :param obs_path: The obs_path of this ObsDestinationDescriptor.
        :type obs_path: str
        """
        self._obs_path = obs_path

    @property
    def partition_format(self):
        """Gets the partition_format of this ObsDestinationDescriptor.

        将转储文件的生成时间使用“yyyy/MM/dd/HH/mm”格式生成分区字符串，用来定义写到OBS的Object文件所在的目录层次结构。   - N/A：置空，不使用日期时间目录。   - yyyy：年   - yyyy/MM：年/月   - yyyy/MM/dd：年/月/日   - yyyy/MM/dd/HH：年/月/日/时   - yyyy/MM/dd/HH/mm：年/月/日/时/分，例如：2017/11/10/14/49，目录结构就是“2017 > 11 > 10 > 14 > 49”，“2017”表示最外层文件夹。  默认值：空 > 数据转储成功后，存储的目录结构为“obs_bucket_path/file_prefix/partition_format”。默认时间是GMT+8 时间 

        :return: The partition_format of this ObsDestinationDescriptor.
        :rtype: str
        """
        return self._partition_format

    @partition_format.setter
    def partition_format(self, partition_format):
        """Sets the partition_format of this ObsDestinationDescriptor.

        将转储文件的生成时间使用“yyyy/MM/dd/HH/mm”格式生成分区字符串，用来定义写到OBS的Object文件所在的目录层次结构。   - N/A：置空，不使用日期时间目录。   - yyyy：年   - yyyy/MM：年/月   - yyyy/MM/dd：年/月/日   - yyyy/MM/dd/HH：年/月/日/时   - yyyy/MM/dd/HH/mm：年/月/日/时/分，例如：2017/11/10/14/49，目录结构就是“2017 > 11 > 10 > 14 > 49”，“2017”表示最外层文件夹。  默认值：空 > 数据转储成功后，存储的目录结构为“obs_bucket_path/file_prefix/partition_format”。默认时间是GMT+8 时间 

        :param partition_format: The partition_format of this ObsDestinationDescriptor.
        :type partition_format: str
        """
        self._partition_format = partition_format

    @property
    def record_delimiter(self):
        """Gets the record_delimiter of this ObsDestinationDescriptor.

        转储文件的记录分隔符，用于分隔写入转储文件的用户数据。 取值范围：   - 逗号“,”   - 分号“;”   - 竖线“|”   - 换行符“\\n”   - NULL  默认值：换行符“\\n”。 

        :return: The record_delimiter of this ObsDestinationDescriptor.
        :rtype: str
        """
        return self._record_delimiter

    @record_delimiter.setter
    def record_delimiter(self, record_delimiter):
        """Sets the record_delimiter of this ObsDestinationDescriptor.

        转储文件的记录分隔符，用于分隔写入转储文件的用户数据。 取值范围：   - 逗号“,”   - 分号“;”   - 竖线“|”   - 换行符“\\n”   - NULL  默认值：换行符“\\n”。 

        :param record_delimiter: The record_delimiter of this ObsDestinationDescriptor.
        :type record_delimiter: str
        """
        self._record_delimiter = record_delimiter

    @property
    def deliver_time_interval(self):
        """Gets the deliver_time_interval of this ObsDestinationDescriptor.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。 取值范围：30～900 单位：秒。 > 使用OBS通道转储流式数据时该参数为必选配置。 

        :return: The deliver_time_interval of this ObsDestinationDescriptor.
        :rtype: int
        """
        return self._deliver_time_interval

    @deliver_time_interval.setter
    def deliver_time_interval(self, deliver_time_interval):
        """Sets the deliver_time_interval of this ObsDestinationDescriptor.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。 取值范围：30～900 单位：秒。 > 使用OBS通道转储流式数据时该参数为必选配置。 

        :param deliver_time_interval: The deliver_time_interval of this ObsDestinationDescriptor.
        :type deliver_time_interval: int
        """
        self._deliver_time_interval = deliver_time_interval

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
        if not isinstance(other, ObsDestinationDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
