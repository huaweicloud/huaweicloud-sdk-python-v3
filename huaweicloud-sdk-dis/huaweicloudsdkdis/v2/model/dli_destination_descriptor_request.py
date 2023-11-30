# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DliDestinationDescriptorRequest:

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
        'dli_database_name': 'str',
        'dli_table_name': 'str',
        'obs_bucket_path': 'str',
        'file_prefix': 'str',
        'retry_duration': 'str'
    }

    attribute_map = {
        'task_name': 'task_name',
        'agency_name': 'agency_name',
        'deliver_time_interval': 'deliver_time_interval',
        'consumer_strategy': 'consumer_strategy',
        'dli_database_name': 'dli_database_name',
        'dli_table_name': 'dli_table_name',
        'obs_bucket_path': 'obs_bucket_path',
        'file_prefix': 'file_prefix',
        'retry_duration': 'retry_duration'
    }

    def __init__(self, task_name=None, agency_name=None, deliver_time_interval=None, consumer_strategy=None, dli_database_name=None, dli_table_name=None, obs_bucket_path=None, file_prefix=None, retry_duration=None):
        """DliDestinationDescriptorRequest

        The model defined in huaweicloud sdk

        :param task_name: 转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。
        :type task_name: str
        :param agency_name: 在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency
        :type agency_name: str
        :param deliver_time_interval: 根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒
        :type deliver_time_interval: int
        :param consumer_strategy: 偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。
        :type consumer_strategy: str
        :param dli_database_name: 存储该通道数据的DLI数据库名称。
        :type dli_database_name: str
        :param dli_table_name: 存储该通道数据的DLI表名称。  说明：  仅支持数据位置为DLI的表，且用户需具有该表的插入权限。
        :type dli_table_name: str
        :param obs_bucket_path: 临时存储该通道数据的OBS桶名称。
        :type obs_bucket_path: str
        :param file_prefix: 临时存储该通道数据的OBS桶下的自定义目录，多级目录可用“/”进行分隔，不可以“/”开头。  取值范围：英文字母、数字、下划线和斜杠，最大长度为50个字符。  默认配置为空。
        :type file_prefix: str
        :param retry_duration: 用户数据导入DLI失败的失效重试时间。重试时间超过该配置项配置的值，则将转储失败的数据备份至“OBS桶/ file_prefix/dli_error”目录下。 取值范围：0~7200。 单位：秒。 默认配置为1800。 配置为“0”表示DIS服务不会在转储失败时进行重试。
        :type retry_duration: str
        """
        
        

        self._task_name = None
        self._agency_name = None
        self._deliver_time_interval = None
        self._consumer_strategy = None
        self._dli_database_name = None
        self._dli_table_name = None
        self._obs_bucket_path = None
        self._file_prefix = None
        self._retry_duration = None
        self.discriminator = None

        self.task_name = task_name
        self.agency_name = agency_name
        self.deliver_time_interval = deliver_time_interval
        if consumer_strategy is not None:
            self.consumer_strategy = consumer_strategy
        self.dli_database_name = dli_database_name
        self.dli_table_name = dli_table_name
        self.obs_bucket_path = obs_bucket_path
        if file_prefix is not None:
            self.file_prefix = file_prefix
        if retry_duration is not None:
            self.retry_duration = retry_duration

    @property
    def task_name(self):
        """Gets the task_name of this DliDestinationDescriptorRequest.

        转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。

        :return: The task_name of this DliDestinationDescriptorRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this DliDestinationDescriptorRequest.

        转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。

        :param task_name: The task_name of this DliDestinationDescriptorRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def agency_name(self):
        """Gets the agency_name of this DliDestinationDescriptorRequest.

        在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency

        :return: The agency_name of this DliDestinationDescriptorRequest.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this DliDestinationDescriptorRequest.

        在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency

        :param agency_name: The agency_name of this DliDestinationDescriptorRequest.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def deliver_time_interval(self):
        """Gets the deliver_time_interval of this DliDestinationDescriptorRequest.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒

        :return: The deliver_time_interval of this DliDestinationDescriptorRequest.
        :rtype: int
        """
        return self._deliver_time_interval

    @deliver_time_interval.setter
    def deliver_time_interval(self, deliver_time_interval):
        """Sets the deliver_time_interval of this DliDestinationDescriptorRequest.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒

        :param deliver_time_interval: The deliver_time_interval of this DliDestinationDescriptorRequest.
        :type deliver_time_interval: int
        """
        self._deliver_time_interval = deliver_time_interval

    @property
    def consumer_strategy(self):
        """Gets the consumer_strategy of this DliDestinationDescriptorRequest.

        偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。

        :return: The consumer_strategy of this DliDestinationDescriptorRequest.
        :rtype: str
        """
        return self._consumer_strategy

    @consumer_strategy.setter
    def consumer_strategy(self, consumer_strategy):
        """Sets the consumer_strategy of this DliDestinationDescriptorRequest.

        偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。

        :param consumer_strategy: The consumer_strategy of this DliDestinationDescriptorRequest.
        :type consumer_strategy: str
        """
        self._consumer_strategy = consumer_strategy

    @property
    def dli_database_name(self):
        """Gets the dli_database_name of this DliDestinationDescriptorRequest.

        存储该通道数据的DLI数据库名称。

        :return: The dli_database_name of this DliDestinationDescriptorRequest.
        :rtype: str
        """
        return self._dli_database_name

    @dli_database_name.setter
    def dli_database_name(self, dli_database_name):
        """Sets the dli_database_name of this DliDestinationDescriptorRequest.

        存储该通道数据的DLI数据库名称。

        :param dli_database_name: The dli_database_name of this DliDestinationDescriptorRequest.
        :type dli_database_name: str
        """
        self._dli_database_name = dli_database_name

    @property
    def dli_table_name(self):
        """Gets the dli_table_name of this DliDestinationDescriptorRequest.

        存储该通道数据的DLI表名称。  说明：  仅支持数据位置为DLI的表，且用户需具有该表的插入权限。

        :return: The dli_table_name of this DliDestinationDescriptorRequest.
        :rtype: str
        """
        return self._dli_table_name

    @dli_table_name.setter
    def dli_table_name(self, dli_table_name):
        """Sets the dli_table_name of this DliDestinationDescriptorRequest.

        存储该通道数据的DLI表名称。  说明：  仅支持数据位置为DLI的表，且用户需具有该表的插入权限。

        :param dli_table_name: The dli_table_name of this DliDestinationDescriptorRequest.
        :type dli_table_name: str
        """
        self._dli_table_name = dli_table_name

    @property
    def obs_bucket_path(self):
        """Gets the obs_bucket_path of this DliDestinationDescriptorRequest.

        临时存储该通道数据的OBS桶名称。

        :return: The obs_bucket_path of this DliDestinationDescriptorRequest.
        :rtype: str
        """
        return self._obs_bucket_path

    @obs_bucket_path.setter
    def obs_bucket_path(self, obs_bucket_path):
        """Sets the obs_bucket_path of this DliDestinationDescriptorRequest.

        临时存储该通道数据的OBS桶名称。

        :param obs_bucket_path: The obs_bucket_path of this DliDestinationDescriptorRequest.
        :type obs_bucket_path: str
        """
        self._obs_bucket_path = obs_bucket_path

    @property
    def file_prefix(self):
        """Gets the file_prefix of this DliDestinationDescriptorRequest.

        临时存储该通道数据的OBS桶下的自定义目录，多级目录可用“/”进行分隔，不可以“/”开头。  取值范围：英文字母、数字、下划线和斜杠，最大长度为50个字符。  默认配置为空。

        :return: The file_prefix of this DliDestinationDescriptorRequest.
        :rtype: str
        """
        return self._file_prefix

    @file_prefix.setter
    def file_prefix(self, file_prefix):
        """Sets the file_prefix of this DliDestinationDescriptorRequest.

        临时存储该通道数据的OBS桶下的自定义目录，多级目录可用“/”进行分隔，不可以“/”开头。  取值范围：英文字母、数字、下划线和斜杠，最大长度为50个字符。  默认配置为空。

        :param file_prefix: The file_prefix of this DliDestinationDescriptorRequest.
        :type file_prefix: str
        """
        self._file_prefix = file_prefix

    @property
    def retry_duration(self):
        """Gets the retry_duration of this DliDestinationDescriptorRequest.

        用户数据导入DLI失败的失效重试时间。重试时间超过该配置项配置的值，则将转储失败的数据备份至“OBS桶/ file_prefix/dli_error”目录下。 取值范围：0~7200。 单位：秒。 默认配置为1800。 配置为“0”表示DIS服务不会在转储失败时进行重试。

        :return: The retry_duration of this DliDestinationDescriptorRequest.
        :rtype: str
        """
        return self._retry_duration

    @retry_duration.setter
    def retry_duration(self, retry_duration):
        """Sets the retry_duration of this DliDestinationDescriptorRequest.

        用户数据导入DLI失败的失效重试时间。重试时间超过该配置项配置的值，则将转储失败的数据备份至“OBS桶/ file_prefix/dli_error”目录下。 取值范围：0~7200。 单位：秒。 默认配置为1800。 配置为“0”表示DIS服务不会在转储失败时进行重试。

        :param retry_duration: The retry_duration of this DliDestinationDescriptorRequest.
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
        if not isinstance(other, DliDestinationDescriptorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
