# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSinkTaskDetailRespObsDestinationDescriptor:

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
        'obs_bucket_name': 'str',
        'obs_path': 'str',
        'partition_format': 'str',
        'record_delimiter': 'str',
        'deliver_time_interval': 'int',
        'obs_part_size': 'int'
    }

    attribute_map = {
        'consumer_strategy': 'consumer_strategy',
        'destination_file_type': 'destination_file_type',
        'obs_bucket_name': 'obs_bucket_name',
        'obs_path': 'obs_path',
        'partition_format': 'partition_format',
        'record_delimiter': 'record_delimiter',
        'deliver_time_interval': 'deliver_time_interval',
        'obs_part_size': 'obs_part_size'
    }

    def __init__(self, consumer_strategy=None, destination_file_type=None, obs_bucket_name=None, obs_path=None, partition_format=None, record_delimiter=None, deliver_time_interval=None, obs_part_size=None):
        """ShowSinkTaskDetailRespObsDestinationDescriptor

        The model defined in huaweicloud sdk

        :param consumer_strategy: 消费启动策略：  - latest：从Topic最后端开始消费。  - earliest: 从Topic最前端消息开始消费。  默认是latest。 
        :type consumer_strategy: str
        :param destination_file_type: 转储文件格式。目前只支持text格式。 
        :type destination_file_type: str
        :param obs_bucket_name: 存储该通道数据的OBS桶名称。 
        :type obs_bucket_name: str
        :param obs_path: 存储在obs的路径。 
        :type obs_path: str
        :param partition_format: 将转储文件的生成时间使用“yyyy/MM/dd/HH/mm”格式生成分区字符串，用来定义写到OBS的Object文件所在的目录层次结构。   - N/A：置空，不使用日期时间目录。   - yyyy：年   - yyyy/MM：年/月   - yyyy/MM/dd：年/月/日   - yyyy/MM/dd/HH：年/月/日/时   - yyyy/MM/dd/HH/mm：年/月/日/时/分，例如：2017/11/10/14/49，目录结构就是“2017 &gt; 11 &gt; 10 &gt; 14 &gt; 49”，“2017”表示最外层文件夹。  默认值：空 &gt; 数据转储成功后，存储的目录结构为“obs_bucket_path/file_prefix/partition_format”。默认时间是GMT+8 时间 
        :type partition_format: str
        :param record_delimiter: 转储文件的记录分隔符，用于分隔写入转储文件的用户数据。 取值范围：   - 逗号“,”   - 分号“;”   - 竖线“|”   - 换行符“\\n”   - NULL  默认值：换行符“\\n”。 
        :type record_delimiter: str
        :param deliver_time_interval: 根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。 取值范围：30～900 缺省值：300 单位：秒。 &gt; 使用OBS通道转储流式数据时该参数为必选配置。 
        :type deliver_time_interval: int
        :param obs_part_size: 每个传输文件多大后就开始上传，单位为byte。 默认值5242880。 
        :type obs_part_size: int
        """
        
        

        self._consumer_strategy = None
        self._destination_file_type = None
        self._obs_bucket_name = None
        self._obs_path = None
        self._partition_format = None
        self._record_delimiter = None
        self._deliver_time_interval = None
        self._obs_part_size = None
        self.discriminator = None

        if consumer_strategy is not None:
            self.consumer_strategy = consumer_strategy
        if destination_file_type is not None:
            self.destination_file_type = destination_file_type
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if obs_path is not None:
            self.obs_path = obs_path
        if partition_format is not None:
            self.partition_format = partition_format
        if record_delimiter is not None:
            self.record_delimiter = record_delimiter
        if deliver_time_interval is not None:
            self.deliver_time_interval = deliver_time_interval
        if obs_part_size is not None:
            self.obs_part_size = obs_part_size

    @property
    def consumer_strategy(self):
        """Gets the consumer_strategy of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        消费启动策略：  - latest：从Topic最后端开始消费。  - earliest: 从Topic最前端消息开始消费。  默认是latest。 

        :return: The consumer_strategy of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :rtype: str
        """
        return self._consumer_strategy

    @consumer_strategy.setter
    def consumer_strategy(self, consumer_strategy):
        """Sets the consumer_strategy of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        消费启动策略：  - latest：从Topic最后端开始消费。  - earliest: 从Topic最前端消息开始消费。  默认是latest。 

        :param consumer_strategy: The consumer_strategy of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :type consumer_strategy: str
        """
        self._consumer_strategy = consumer_strategy

    @property
    def destination_file_type(self):
        """Gets the destination_file_type of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        转储文件格式。目前只支持text格式。 

        :return: The destination_file_type of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :rtype: str
        """
        return self._destination_file_type

    @destination_file_type.setter
    def destination_file_type(self, destination_file_type):
        """Sets the destination_file_type of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        转储文件格式。目前只支持text格式。 

        :param destination_file_type: The destination_file_type of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :type destination_file_type: str
        """
        self._destination_file_type = destination_file_type

    @property
    def obs_bucket_name(self):
        """Gets the obs_bucket_name of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        存储该通道数据的OBS桶名称。 

        :return: The obs_bucket_name of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        """Sets the obs_bucket_name of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        存储该通道数据的OBS桶名称。 

        :param obs_bucket_name: The obs_bucket_name of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def obs_path(self):
        """Gets the obs_path of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        存储在obs的路径。 

        :return: The obs_path of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :rtype: str
        """
        return self._obs_path

    @obs_path.setter
    def obs_path(self, obs_path):
        """Sets the obs_path of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        存储在obs的路径。 

        :param obs_path: The obs_path of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :type obs_path: str
        """
        self._obs_path = obs_path

    @property
    def partition_format(self):
        """Gets the partition_format of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        将转储文件的生成时间使用“yyyy/MM/dd/HH/mm”格式生成分区字符串，用来定义写到OBS的Object文件所在的目录层次结构。   - N/A：置空，不使用日期时间目录。   - yyyy：年   - yyyy/MM：年/月   - yyyy/MM/dd：年/月/日   - yyyy/MM/dd/HH：年/月/日/时   - yyyy/MM/dd/HH/mm：年/月/日/时/分，例如：2017/11/10/14/49，目录结构就是“2017 > 11 > 10 > 14 > 49”，“2017”表示最外层文件夹。  默认值：空 > 数据转储成功后，存储的目录结构为“obs_bucket_path/file_prefix/partition_format”。默认时间是GMT+8 时间 

        :return: The partition_format of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :rtype: str
        """
        return self._partition_format

    @partition_format.setter
    def partition_format(self, partition_format):
        """Sets the partition_format of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        将转储文件的生成时间使用“yyyy/MM/dd/HH/mm”格式生成分区字符串，用来定义写到OBS的Object文件所在的目录层次结构。   - N/A：置空，不使用日期时间目录。   - yyyy：年   - yyyy/MM：年/月   - yyyy/MM/dd：年/月/日   - yyyy/MM/dd/HH：年/月/日/时   - yyyy/MM/dd/HH/mm：年/月/日/时/分，例如：2017/11/10/14/49，目录结构就是“2017 > 11 > 10 > 14 > 49”，“2017”表示最外层文件夹。  默认值：空 > 数据转储成功后，存储的目录结构为“obs_bucket_path/file_prefix/partition_format”。默认时间是GMT+8 时间 

        :param partition_format: The partition_format of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :type partition_format: str
        """
        self._partition_format = partition_format

    @property
    def record_delimiter(self):
        """Gets the record_delimiter of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        转储文件的记录分隔符，用于分隔写入转储文件的用户数据。 取值范围：   - 逗号“,”   - 分号“;”   - 竖线“|”   - 换行符“\\n”   - NULL  默认值：换行符“\\n”。 

        :return: The record_delimiter of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :rtype: str
        """
        return self._record_delimiter

    @record_delimiter.setter
    def record_delimiter(self, record_delimiter):
        """Sets the record_delimiter of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        转储文件的记录分隔符，用于分隔写入转储文件的用户数据。 取值范围：   - 逗号“,”   - 分号“;”   - 竖线“|”   - 换行符“\\n”   - NULL  默认值：换行符“\\n”。 

        :param record_delimiter: The record_delimiter of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :type record_delimiter: str
        """
        self._record_delimiter = record_delimiter

    @property
    def deliver_time_interval(self):
        """Gets the deliver_time_interval of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。 取值范围：30～900 缺省值：300 单位：秒。 > 使用OBS通道转储流式数据时该参数为必选配置。 

        :return: The deliver_time_interval of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :rtype: int
        """
        return self._deliver_time_interval

    @deliver_time_interval.setter
    def deliver_time_interval(self, deliver_time_interval):
        """Sets the deliver_time_interval of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。 取值范围：30～900 缺省值：300 单位：秒。 > 使用OBS通道转储流式数据时该参数为必选配置。 

        :param deliver_time_interval: The deliver_time_interval of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :type deliver_time_interval: int
        """
        self._deliver_time_interval = deliver_time_interval

    @property
    def obs_part_size(self):
        """Gets the obs_part_size of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        每个传输文件多大后就开始上传，单位为byte。 默认值5242880。 

        :return: The obs_part_size of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :rtype: int
        """
        return self._obs_part_size

    @obs_part_size.setter
    def obs_part_size(self, obs_part_size):
        """Sets the obs_part_size of this ShowSinkTaskDetailRespObsDestinationDescriptor.

        每个传输文件多大后就开始上传，单位为byte。 默认值5242880。 

        :param obs_part_size: The obs_part_size of this ShowSinkTaskDetailRespObsDestinationDescriptor.
        :type obs_part_size: int
        """
        self._obs_part_size = obs_part_size

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
        if not isinstance(other, ShowSinkTaskDetailRespObsDestinationDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
