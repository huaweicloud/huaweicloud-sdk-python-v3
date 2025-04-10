# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OBSDestinationDescriptorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'agency_name': 'str',
        'deliver_time_interval': 'int',
        'consumer_strategy': 'str',
        'file_prefix': 'str',
        'partition_format': 'str',
        'obs_bucket_path': 'str',
        'destination_file_type': 'str',
        'processing_schema': 'ProcessingSchema',
        'record_delimiter': 'str'
    }

    attribute_map = {
        'task_name': 'task_name',
        'agency_name': 'agency_name',
        'deliver_time_interval': 'deliver_time_interval',
        'consumer_strategy': 'consumer_strategy',
        'file_prefix': 'file_prefix',
        'partition_format': 'partition_format',
        'obs_bucket_path': 'obs_bucket_path',
        'destination_file_type': 'destination_file_type',
        'processing_schema': 'processing_schema',
        'record_delimiter': 'record_delimiter'
    }

    def __init__(self, task_name=None, agency_name=None, deliver_time_interval=None, consumer_strategy=None, file_prefix=None, partition_format=None, obs_bucket_path=None, destination_file_type=None, processing_schema=None, record_delimiter=None):
        r"""OBSDestinationDescriptorRequest

        The model defined in huaweicloud sdk

        :param task_name: 转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。
        :type task_name: str
        :param agency_name: 在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency
        :type agency_name: str
        :param deliver_time_interval: 根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒
        :type deliver_time_interval: int
        :param consumer_strategy: 偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。
        :type consumer_strategy: str
        :param file_prefix: 在OBS中存储通道文件的自定义目录，多级目录可用“/”进行分隔，不可以“/”开头。  取值范围：英文字母、数字、下划线和斜杠，最大长度为50个字符。  默认配置为空。
        :type file_prefix: str
        :param partition_format: 将转储文件的生成时间使用“yyyy/MM/dd/HH/mm”格式生成分区字符串，用来定义写到OBS的Object文件所在的目录层次结构。  - N/A：置空，不使用日期时间目录。 - yyyy：年 - yyyy/MM：年/ - yyyy/MM/dd：年/月/日 - yyyy/MM/dd/HH：年/月/日/时 - yyyy/MM/dd/HH/mm：年/月/日/时/分  例如：2017/11/10/14/49，目录结构就是“2017 &gt; 11 &gt; 10 &gt; 14 &gt; 49”，“2017”表示最外层文件夹。  默认值：空  说明：  数据转储成功后，存储的目录结构为“obs_bucket_path/file_prefix/partition_format”。
        :type partition_format: str
        :param obs_bucket_path: 存储该通道数据的OBS桶名称。
        :type obs_bucket_path: str
        :param destination_file_type: 转储文件格式。  - text：转储目标格式为TEXT，缺省值 - parquet：转储目标格式为Parquet - carbon：转储目标格式为Carbon  说明：  “源数据类型”为“JSON”，“转储服务类型”为“OBS”时才可选择“parquet”或“carbon”格式。
        :type destination_file_type: str
        :param processing_schema: 
        :type processing_schema: :class:`huaweicloudsdkdis.v2.ProcessingSchema`
        :param record_delimiter: 转储文件的记录分隔符，用于分隔写入转储文件的用户数据。  取值范围：  - 逗号 \&quot;,\&quot;，默认值 - 分号 \&quot;;\&quot; - 竖线 \&quot;|\&quot; - 换行符 \&quot;\\n\&quot;
        :type record_delimiter: str
        """
        
        

        self._task_name = None
        self._agency_name = None
        self._deliver_time_interval = None
        self._consumer_strategy = None
        self._file_prefix = None
        self._partition_format = None
        self._obs_bucket_path = None
        self._destination_file_type = None
        self._processing_schema = None
        self._record_delimiter = None
        self.discriminator = None

        self.task_name = task_name
        self.agency_name = agency_name
        self.deliver_time_interval = deliver_time_interval
        if consumer_strategy is not None:
            self.consumer_strategy = consumer_strategy
        if file_prefix is not None:
            self.file_prefix = file_prefix
        if partition_format is not None:
            self.partition_format = partition_format
        self.obs_bucket_path = obs_bucket_path
        if destination_file_type is not None:
            self.destination_file_type = destination_file_type
        if processing_schema is not None:
            self.processing_schema = processing_schema
        if record_delimiter is not None:
            self.record_delimiter = record_delimiter

    @property
    def task_name(self):
        r"""Gets the task_name of this OBSDestinationDescriptorRequest.

        转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。

        :return: The task_name of this OBSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this OBSDestinationDescriptorRequest.

        转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。

        :param task_name: The task_name of this OBSDestinationDescriptorRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this OBSDestinationDescriptorRequest.

        在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency

        :return: The agency_name of this OBSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this OBSDestinationDescriptorRequest.

        在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency

        :param agency_name: The agency_name of this OBSDestinationDescriptorRequest.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def deliver_time_interval(self):
        r"""Gets the deliver_time_interval of this OBSDestinationDescriptorRequest.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒

        :return: The deliver_time_interval of this OBSDestinationDescriptorRequest.
        :rtype: int
        """
        return self._deliver_time_interval

    @deliver_time_interval.setter
    def deliver_time_interval(self, deliver_time_interval):
        r"""Sets the deliver_time_interval of this OBSDestinationDescriptorRequest.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒

        :param deliver_time_interval: The deliver_time_interval of this OBSDestinationDescriptorRequest.
        :type deliver_time_interval: int
        """
        self._deliver_time_interval = deliver_time_interval

    @property
    def consumer_strategy(self):
        r"""Gets the consumer_strategy of this OBSDestinationDescriptorRequest.

        偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。

        :return: The consumer_strategy of this OBSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._consumer_strategy

    @consumer_strategy.setter
    def consumer_strategy(self, consumer_strategy):
        r"""Sets the consumer_strategy of this OBSDestinationDescriptorRequest.

        偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。

        :param consumer_strategy: The consumer_strategy of this OBSDestinationDescriptorRequest.
        :type consumer_strategy: str
        """
        self._consumer_strategy = consumer_strategy

    @property
    def file_prefix(self):
        r"""Gets the file_prefix of this OBSDestinationDescriptorRequest.

        在OBS中存储通道文件的自定义目录，多级目录可用“/”进行分隔，不可以“/”开头。  取值范围：英文字母、数字、下划线和斜杠，最大长度为50个字符。  默认配置为空。

        :return: The file_prefix of this OBSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._file_prefix

    @file_prefix.setter
    def file_prefix(self, file_prefix):
        r"""Sets the file_prefix of this OBSDestinationDescriptorRequest.

        在OBS中存储通道文件的自定义目录，多级目录可用“/”进行分隔，不可以“/”开头。  取值范围：英文字母、数字、下划线和斜杠，最大长度为50个字符。  默认配置为空。

        :param file_prefix: The file_prefix of this OBSDestinationDescriptorRequest.
        :type file_prefix: str
        """
        self._file_prefix = file_prefix

    @property
    def partition_format(self):
        r"""Gets the partition_format of this OBSDestinationDescriptorRequest.

        将转储文件的生成时间使用“yyyy/MM/dd/HH/mm”格式生成分区字符串，用来定义写到OBS的Object文件所在的目录层次结构。  - N/A：置空，不使用日期时间目录。 - yyyy：年 - yyyy/MM：年/ - yyyy/MM/dd：年/月/日 - yyyy/MM/dd/HH：年/月/日/时 - yyyy/MM/dd/HH/mm：年/月/日/时/分  例如：2017/11/10/14/49，目录结构就是“2017 > 11 > 10 > 14 > 49”，“2017”表示最外层文件夹。  默认值：空  说明：  数据转储成功后，存储的目录结构为“obs_bucket_path/file_prefix/partition_format”。

        :return: The partition_format of this OBSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._partition_format

    @partition_format.setter
    def partition_format(self, partition_format):
        r"""Sets the partition_format of this OBSDestinationDescriptorRequest.

        将转储文件的生成时间使用“yyyy/MM/dd/HH/mm”格式生成分区字符串，用来定义写到OBS的Object文件所在的目录层次结构。  - N/A：置空，不使用日期时间目录。 - yyyy：年 - yyyy/MM：年/ - yyyy/MM/dd：年/月/日 - yyyy/MM/dd/HH：年/月/日/时 - yyyy/MM/dd/HH/mm：年/月/日/时/分  例如：2017/11/10/14/49，目录结构就是“2017 > 11 > 10 > 14 > 49”，“2017”表示最外层文件夹。  默认值：空  说明：  数据转储成功后，存储的目录结构为“obs_bucket_path/file_prefix/partition_format”。

        :param partition_format: The partition_format of this OBSDestinationDescriptorRequest.
        :type partition_format: str
        """
        self._partition_format = partition_format

    @property
    def obs_bucket_path(self):
        r"""Gets the obs_bucket_path of this OBSDestinationDescriptorRequest.

        存储该通道数据的OBS桶名称。

        :return: The obs_bucket_path of this OBSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._obs_bucket_path

    @obs_bucket_path.setter
    def obs_bucket_path(self, obs_bucket_path):
        r"""Sets the obs_bucket_path of this OBSDestinationDescriptorRequest.

        存储该通道数据的OBS桶名称。

        :param obs_bucket_path: The obs_bucket_path of this OBSDestinationDescriptorRequest.
        :type obs_bucket_path: str
        """
        self._obs_bucket_path = obs_bucket_path

    @property
    def destination_file_type(self):
        r"""Gets the destination_file_type of this OBSDestinationDescriptorRequest.

        转储文件格式。  - text：转储目标格式为TEXT，缺省值 - parquet：转储目标格式为Parquet - carbon：转储目标格式为Carbon  说明：  “源数据类型”为“JSON”，“转储服务类型”为“OBS”时才可选择“parquet”或“carbon”格式。

        :return: The destination_file_type of this OBSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._destination_file_type

    @destination_file_type.setter
    def destination_file_type(self, destination_file_type):
        r"""Sets the destination_file_type of this OBSDestinationDescriptorRequest.

        转储文件格式。  - text：转储目标格式为TEXT，缺省值 - parquet：转储目标格式为Parquet - carbon：转储目标格式为Carbon  说明：  “源数据类型”为“JSON”，“转储服务类型”为“OBS”时才可选择“parquet”或“carbon”格式。

        :param destination_file_type: The destination_file_type of this OBSDestinationDescriptorRequest.
        :type destination_file_type: str
        """
        self._destination_file_type = destination_file_type

    @property
    def processing_schema(self):
        r"""Gets the processing_schema of this OBSDestinationDescriptorRequest.

        :return: The processing_schema of this OBSDestinationDescriptorRequest.
        :rtype: :class:`huaweicloudsdkdis.v2.ProcessingSchema`
        """
        return self._processing_schema

    @processing_schema.setter
    def processing_schema(self, processing_schema):
        r"""Sets the processing_schema of this OBSDestinationDescriptorRequest.

        :param processing_schema: The processing_schema of this OBSDestinationDescriptorRequest.
        :type processing_schema: :class:`huaweicloudsdkdis.v2.ProcessingSchema`
        """
        self._processing_schema = processing_schema

    @property
    def record_delimiter(self):
        r"""Gets the record_delimiter of this OBSDestinationDescriptorRequest.

        转储文件的记录分隔符，用于分隔写入转储文件的用户数据。  取值范围：  - 逗号 \",\"，默认值 - 分号 \";\" - 竖线 \"|\" - 换行符 \"\\n\"

        :return: The record_delimiter of this OBSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._record_delimiter

    @record_delimiter.setter
    def record_delimiter(self, record_delimiter):
        r"""Sets the record_delimiter of this OBSDestinationDescriptorRequest.

        转储文件的记录分隔符，用于分隔写入转储文件的用户数据。  取值范围：  - 逗号 \",\"，默认值 - 分号 \";\" - 竖线 \"|\" - 换行符 \"\\n\"

        :param record_delimiter: The record_delimiter of this OBSDestinationDescriptorRequest.
        :type record_delimiter: str
        """
        self._record_delimiter = record_delimiter

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
        if not isinstance(other, OBSDestinationDescriptorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
