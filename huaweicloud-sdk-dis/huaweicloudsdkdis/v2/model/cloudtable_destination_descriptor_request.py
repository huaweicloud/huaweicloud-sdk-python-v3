# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudtableDestinationDescriptorRequest:

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
        'cloudtable_cluster_name': 'str',
        'cloudtable_cluster_id': 'str',
        'cloudtable_table_name': 'str',
        'cloudtable_schema': 'CloudtableSchema',
        'opentsdb_schema': 'list[OpenTSDBSchema]',
        'cloudtable_row_key_delimiter': 'str',
        'obs_backup_bucket_path': 'str',
        'backup_file_prefix': 'str',
        'retry_duration': 'str'
    }

    attribute_map = {
        'task_name': 'task_name',
        'agency_name': 'agency_name',
        'deliver_time_interval': 'deliver_time_interval',
        'consumer_strategy': 'consumer_strategy',
        'cloudtable_cluster_name': 'cloudtable_cluster_name',
        'cloudtable_cluster_id': 'cloudtable_cluster_id',
        'cloudtable_table_name': 'cloudtable_table_name',
        'cloudtable_schema': 'cloudtable_schema',
        'opentsdb_schema': 'opentsdb_schema',
        'cloudtable_row_key_delimiter': 'cloudtable_row_key_delimiter',
        'obs_backup_bucket_path': 'obs_backup_bucket_path',
        'backup_file_prefix': 'backup_file_prefix',
        'retry_duration': 'retry_duration'
    }

    def __init__(self, task_name=None, agency_name=None, deliver_time_interval=None, consumer_strategy=None, cloudtable_cluster_name=None, cloudtable_cluster_id=None, cloudtable_table_name=None, cloudtable_schema=None, opentsdb_schema=None, cloudtable_row_key_delimiter=None, obs_backup_bucket_path=None, backup_file_prefix=None, retry_duration=None):
        """CloudtableDestinationDescriptorRequest

        The model defined in huaweicloud sdk

        :param task_name: 转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。
        :type task_name: str
        :param agency_name: 在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency
        :type agency_name: str
        :param deliver_time_interval: 根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒
        :type deliver_time_interval: int
        :param consumer_strategy: 偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。
        :type consumer_strategy: str
        :param cloudtable_cluster_name: 存储该通道数据的CloudTable集群名称。  如果选择转储OpenTSDB，则集群必须开启OpenTSDB。
        :type cloudtable_cluster_name: str
        :param cloudtable_cluster_id: 存储该通道数据的CloudTable集群ID。  如果选择转储OpenTSDB，则集群必须开启OpenTSDB。
        :type cloudtable_cluster_id: str
        :param cloudtable_table_name: 转储HBase时必选，表示存储该通道数据的CloudTable集群HBase表名称。
        :type cloudtable_table_name: str
        :param cloudtable_schema: 
        :type cloudtable_schema: :class:`huaweicloudsdkdis.v2.CloudtableSchema`
        :param opentsdb_schema: 转储OpenTSDB时必选，与“cloudtable_schema”二选一，表示CloudTable集群OpenTSDB数据的Schema配置。用于将通道内的JSON数据进行格式转换并导入Cloudtable的OpenTSDB。
        :type opentsdb_schema: list[:class:`huaweicloudsdkdis.v2.OpenTSDBSchema`]
        :param cloudtable_row_key_delimiter: 转储HBase的rowkey分隔符，用于分隔生成rowKey的用户数据。取值范围：”, ”、 ”. ”、 ”|”、 ”; ”、 ”\\”、 ”-”、 ”_”、 ”~”  缺省值：”.”
        :type cloudtable_row_key_delimiter: str
        :param obs_backup_bucket_path: 用户数据转储CloudTable服务失败时，可选择将转储失败的数据备份至OBS服务，此参数为OBS服务的桶名称。
        :type obs_backup_bucket_path: str
        :param backup_file_prefix: 用户数据转储CloudTable服务失败时，可选择将转储失败的数据备份至OBS服务，此参数为OBS桶下的自定义目录，多级目录可用“/”进行分隔，不可以“/”开头。  取值范围：英文字母、数字和下划线。  最大长度：最大长度为50个字符。  默认配置为空。
        :type backup_file_prefix: str
        :param retry_duration: 用户数据导入CloudTable服务失败的失效重试时间。超出此时效，转储CloudTable失败的数据将备份至“OBS桶/ backup_file_prefix /cloudtable_error”或“OBS桶/ backup_file_prefix /opentsdb_error”目录下。  取值范围： 0～7200。  单位：秒。  默认配置为1800。
        :type retry_duration: str
        """
        
        

        self._task_name = None
        self._agency_name = None
        self._deliver_time_interval = None
        self._consumer_strategy = None
        self._cloudtable_cluster_name = None
        self._cloudtable_cluster_id = None
        self._cloudtable_table_name = None
        self._cloudtable_schema = None
        self._opentsdb_schema = None
        self._cloudtable_row_key_delimiter = None
        self._obs_backup_bucket_path = None
        self._backup_file_prefix = None
        self._retry_duration = None
        self.discriminator = None

        self.task_name = task_name
        self.agency_name = agency_name
        self.deliver_time_interval = deliver_time_interval
        if consumer_strategy is not None:
            self.consumer_strategy = consumer_strategy
        self.cloudtable_cluster_name = cloudtable_cluster_name
        self.cloudtable_cluster_id = cloudtable_cluster_id
        if cloudtable_table_name is not None:
            self.cloudtable_table_name = cloudtable_table_name
        if cloudtable_schema is not None:
            self.cloudtable_schema = cloudtable_schema
        if opentsdb_schema is not None:
            self.opentsdb_schema = opentsdb_schema
        if cloudtable_row_key_delimiter is not None:
            self.cloudtable_row_key_delimiter = cloudtable_row_key_delimiter
        if obs_backup_bucket_path is not None:
            self.obs_backup_bucket_path = obs_backup_bucket_path
        if backup_file_prefix is not None:
            self.backup_file_prefix = backup_file_prefix
        if retry_duration is not None:
            self.retry_duration = retry_duration

    @property
    def task_name(self):
        """Gets the task_name of this CloudtableDestinationDescriptorRequest.

        转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。

        :return: The task_name of this CloudtableDestinationDescriptorRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CloudtableDestinationDescriptorRequest.

        转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。

        :param task_name: The task_name of this CloudtableDestinationDescriptorRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def agency_name(self):
        """Gets the agency_name of this CloudtableDestinationDescriptorRequest.

        在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency

        :return: The agency_name of this CloudtableDestinationDescriptorRequest.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this CloudtableDestinationDescriptorRequest.

        在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency

        :param agency_name: The agency_name of this CloudtableDestinationDescriptorRequest.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def deliver_time_interval(self):
        """Gets the deliver_time_interval of this CloudtableDestinationDescriptorRequest.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒

        :return: The deliver_time_interval of this CloudtableDestinationDescriptorRequest.
        :rtype: int
        """
        return self._deliver_time_interval

    @deliver_time_interval.setter
    def deliver_time_interval(self, deliver_time_interval):
        """Sets the deliver_time_interval of this CloudtableDestinationDescriptorRequest.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒

        :param deliver_time_interval: The deliver_time_interval of this CloudtableDestinationDescriptorRequest.
        :type deliver_time_interval: int
        """
        self._deliver_time_interval = deliver_time_interval

    @property
    def consumer_strategy(self):
        """Gets the consumer_strategy of this CloudtableDestinationDescriptorRequest.

        偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。

        :return: The consumer_strategy of this CloudtableDestinationDescriptorRequest.
        :rtype: str
        """
        return self._consumer_strategy

    @consumer_strategy.setter
    def consumer_strategy(self, consumer_strategy):
        """Sets the consumer_strategy of this CloudtableDestinationDescriptorRequest.

        偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。

        :param consumer_strategy: The consumer_strategy of this CloudtableDestinationDescriptorRequest.
        :type consumer_strategy: str
        """
        self._consumer_strategy = consumer_strategy

    @property
    def cloudtable_cluster_name(self):
        """Gets the cloudtable_cluster_name of this CloudtableDestinationDescriptorRequest.

        存储该通道数据的CloudTable集群名称。  如果选择转储OpenTSDB，则集群必须开启OpenTSDB。

        :return: The cloudtable_cluster_name of this CloudtableDestinationDescriptorRequest.
        :rtype: str
        """
        return self._cloudtable_cluster_name

    @cloudtable_cluster_name.setter
    def cloudtable_cluster_name(self, cloudtable_cluster_name):
        """Sets the cloudtable_cluster_name of this CloudtableDestinationDescriptorRequest.

        存储该通道数据的CloudTable集群名称。  如果选择转储OpenTSDB，则集群必须开启OpenTSDB。

        :param cloudtable_cluster_name: The cloudtable_cluster_name of this CloudtableDestinationDescriptorRequest.
        :type cloudtable_cluster_name: str
        """
        self._cloudtable_cluster_name = cloudtable_cluster_name

    @property
    def cloudtable_cluster_id(self):
        """Gets the cloudtable_cluster_id of this CloudtableDestinationDescriptorRequest.

        存储该通道数据的CloudTable集群ID。  如果选择转储OpenTSDB，则集群必须开启OpenTSDB。

        :return: The cloudtable_cluster_id of this CloudtableDestinationDescriptorRequest.
        :rtype: str
        """
        return self._cloudtable_cluster_id

    @cloudtable_cluster_id.setter
    def cloudtable_cluster_id(self, cloudtable_cluster_id):
        """Sets the cloudtable_cluster_id of this CloudtableDestinationDescriptorRequest.

        存储该通道数据的CloudTable集群ID。  如果选择转储OpenTSDB，则集群必须开启OpenTSDB。

        :param cloudtable_cluster_id: The cloudtable_cluster_id of this CloudtableDestinationDescriptorRequest.
        :type cloudtable_cluster_id: str
        """
        self._cloudtable_cluster_id = cloudtable_cluster_id

    @property
    def cloudtable_table_name(self):
        """Gets the cloudtable_table_name of this CloudtableDestinationDescriptorRequest.

        转储HBase时必选，表示存储该通道数据的CloudTable集群HBase表名称。

        :return: The cloudtable_table_name of this CloudtableDestinationDescriptorRequest.
        :rtype: str
        """
        return self._cloudtable_table_name

    @cloudtable_table_name.setter
    def cloudtable_table_name(self, cloudtable_table_name):
        """Sets the cloudtable_table_name of this CloudtableDestinationDescriptorRequest.

        转储HBase时必选，表示存储该通道数据的CloudTable集群HBase表名称。

        :param cloudtable_table_name: The cloudtable_table_name of this CloudtableDestinationDescriptorRequest.
        :type cloudtable_table_name: str
        """
        self._cloudtable_table_name = cloudtable_table_name

    @property
    def cloudtable_schema(self):
        """Gets the cloudtable_schema of this CloudtableDestinationDescriptorRequest.

        :return: The cloudtable_schema of this CloudtableDestinationDescriptorRequest.
        :rtype: :class:`huaweicloudsdkdis.v2.CloudtableSchema`
        """
        return self._cloudtable_schema

    @cloudtable_schema.setter
    def cloudtable_schema(self, cloudtable_schema):
        """Sets the cloudtable_schema of this CloudtableDestinationDescriptorRequest.

        :param cloudtable_schema: The cloudtable_schema of this CloudtableDestinationDescriptorRequest.
        :type cloudtable_schema: :class:`huaweicloudsdkdis.v2.CloudtableSchema`
        """
        self._cloudtable_schema = cloudtable_schema

    @property
    def opentsdb_schema(self):
        """Gets the opentsdb_schema of this CloudtableDestinationDescriptorRequest.

        转储OpenTSDB时必选，与“cloudtable_schema”二选一，表示CloudTable集群OpenTSDB数据的Schema配置。用于将通道内的JSON数据进行格式转换并导入Cloudtable的OpenTSDB。

        :return: The opentsdb_schema of this CloudtableDestinationDescriptorRequest.
        :rtype: list[:class:`huaweicloudsdkdis.v2.OpenTSDBSchema`]
        """
        return self._opentsdb_schema

    @opentsdb_schema.setter
    def opentsdb_schema(self, opentsdb_schema):
        """Sets the opentsdb_schema of this CloudtableDestinationDescriptorRequest.

        转储OpenTSDB时必选，与“cloudtable_schema”二选一，表示CloudTable集群OpenTSDB数据的Schema配置。用于将通道内的JSON数据进行格式转换并导入Cloudtable的OpenTSDB。

        :param opentsdb_schema: The opentsdb_schema of this CloudtableDestinationDescriptorRequest.
        :type opentsdb_schema: list[:class:`huaweicloudsdkdis.v2.OpenTSDBSchema`]
        """
        self._opentsdb_schema = opentsdb_schema

    @property
    def cloudtable_row_key_delimiter(self):
        """Gets the cloudtable_row_key_delimiter of this CloudtableDestinationDescriptorRequest.

        转储HBase的rowkey分隔符，用于分隔生成rowKey的用户数据。取值范围：”, ”、 ”. ”、 ”|”、 ”; ”、 ”\\”、 ”-”、 ”_”、 ”~”  缺省值：”.”

        :return: The cloudtable_row_key_delimiter of this CloudtableDestinationDescriptorRequest.
        :rtype: str
        """
        return self._cloudtable_row_key_delimiter

    @cloudtable_row_key_delimiter.setter
    def cloudtable_row_key_delimiter(self, cloudtable_row_key_delimiter):
        """Sets the cloudtable_row_key_delimiter of this CloudtableDestinationDescriptorRequest.

        转储HBase的rowkey分隔符，用于分隔生成rowKey的用户数据。取值范围：”, ”、 ”. ”、 ”|”、 ”; ”、 ”\\”、 ”-”、 ”_”、 ”~”  缺省值：”.”

        :param cloudtable_row_key_delimiter: The cloudtable_row_key_delimiter of this CloudtableDestinationDescriptorRequest.
        :type cloudtable_row_key_delimiter: str
        """
        self._cloudtable_row_key_delimiter = cloudtable_row_key_delimiter

    @property
    def obs_backup_bucket_path(self):
        """Gets the obs_backup_bucket_path of this CloudtableDestinationDescriptorRequest.

        用户数据转储CloudTable服务失败时，可选择将转储失败的数据备份至OBS服务，此参数为OBS服务的桶名称。

        :return: The obs_backup_bucket_path of this CloudtableDestinationDescriptorRequest.
        :rtype: str
        """
        return self._obs_backup_bucket_path

    @obs_backup_bucket_path.setter
    def obs_backup_bucket_path(self, obs_backup_bucket_path):
        """Sets the obs_backup_bucket_path of this CloudtableDestinationDescriptorRequest.

        用户数据转储CloudTable服务失败时，可选择将转储失败的数据备份至OBS服务，此参数为OBS服务的桶名称。

        :param obs_backup_bucket_path: The obs_backup_bucket_path of this CloudtableDestinationDescriptorRequest.
        :type obs_backup_bucket_path: str
        """
        self._obs_backup_bucket_path = obs_backup_bucket_path

    @property
    def backup_file_prefix(self):
        """Gets the backup_file_prefix of this CloudtableDestinationDescriptorRequest.

        用户数据转储CloudTable服务失败时，可选择将转储失败的数据备份至OBS服务，此参数为OBS桶下的自定义目录，多级目录可用“/”进行分隔，不可以“/”开头。  取值范围：英文字母、数字和下划线。  最大长度：最大长度为50个字符。  默认配置为空。

        :return: The backup_file_prefix of this CloudtableDestinationDescriptorRequest.
        :rtype: str
        """
        return self._backup_file_prefix

    @backup_file_prefix.setter
    def backup_file_prefix(self, backup_file_prefix):
        """Sets the backup_file_prefix of this CloudtableDestinationDescriptorRequest.

        用户数据转储CloudTable服务失败时，可选择将转储失败的数据备份至OBS服务，此参数为OBS桶下的自定义目录，多级目录可用“/”进行分隔，不可以“/”开头。  取值范围：英文字母、数字和下划线。  最大长度：最大长度为50个字符。  默认配置为空。

        :param backup_file_prefix: The backup_file_prefix of this CloudtableDestinationDescriptorRequest.
        :type backup_file_prefix: str
        """
        self._backup_file_prefix = backup_file_prefix

    @property
    def retry_duration(self):
        """Gets the retry_duration of this CloudtableDestinationDescriptorRequest.

        用户数据导入CloudTable服务失败的失效重试时间。超出此时效，转储CloudTable失败的数据将备份至“OBS桶/ backup_file_prefix /cloudtable_error”或“OBS桶/ backup_file_prefix /opentsdb_error”目录下。  取值范围： 0～7200。  单位：秒。  默认配置为1800。

        :return: The retry_duration of this CloudtableDestinationDescriptorRequest.
        :rtype: str
        """
        return self._retry_duration

    @retry_duration.setter
    def retry_duration(self, retry_duration):
        """Sets the retry_duration of this CloudtableDestinationDescriptorRequest.

        用户数据导入CloudTable服务失败的失效重试时间。超出此时效，转储CloudTable失败的数据将备份至“OBS桶/ backup_file_prefix /cloudtable_error”或“OBS桶/ backup_file_prefix /opentsdb_error”目录下。  取值范围： 0～7200。  单位：秒。  默认配置为1800。

        :param retry_duration: The retry_duration of this CloudtableDestinationDescriptorRequest.
        :type retry_duration: str
        """
        self._retry_duration = retry_duration

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
        if not isinstance(other, CloudtableDestinationDescriptorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
