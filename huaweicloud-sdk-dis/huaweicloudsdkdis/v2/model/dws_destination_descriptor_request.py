# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DWSDestinationDescriptorRequest:

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
        'dws_cluster_name': 'str',
        'dws_cluster_id': 'str',
        'dws_database_name': 'str',
        'dws_schema': 'str',
        'dws_table_name': 'str',
        'dws_delimiter': 'str',
        'user_name': 'str',
        'user_password': 'str',
        'kms_user_key_name': 'str',
        'kms_user_key_id': 'str',
        'obs_bucket_path': 'str',
        'file_prefix': 'str',
        'retry_duration': 'str',
        'dws_table_columns': 'str',
        'options': 'Options'
    }

    attribute_map = {
        'task_name': 'task_name',
        'agency_name': 'agency_name',
        'deliver_time_interval': 'deliver_time_interval',
        'consumer_strategy': 'consumer_strategy',
        'dws_cluster_name': 'dws_cluster_name',
        'dws_cluster_id': 'dws_cluster_id',
        'dws_database_name': 'dws_database_name',
        'dws_schema': 'dws_schema',
        'dws_table_name': 'dws_table_name',
        'dws_delimiter': 'dws_delimiter',
        'user_name': 'user_name',
        'user_password': 'user_password',
        'kms_user_key_name': 'kms_user_key_name',
        'kms_user_key_id': 'kms_user_key_id',
        'obs_bucket_path': 'obs_bucket_path',
        'file_prefix': 'file_prefix',
        'retry_duration': 'retry_duration',
        'dws_table_columns': 'dws_table_columns',
        'options': 'options'
    }

    def __init__(self, task_name=None, agency_name=None, deliver_time_interval=None, consumer_strategy=None, dws_cluster_name=None, dws_cluster_id=None, dws_database_name=None, dws_schema=None, dws_table_name=None, dws_delimiter=None, user_name=None, user_password=None, kms_user_key_name=None, kms_user_key_id=None, obs_bucket_path=None, file_prefix=None, retry_duration=None, dws_table_columns=None, options=None):
        r"""DWSDestinationDescriptorRequest

        The model defined in huaweicloud sdk

        :param task_name: 转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。
        :type task_name: str
        :param agency_name: 在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency
        :type agency_name: str
        :param deliver_time_interval: 根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒
        :type deliver_time_interval: int
        :param consumer_strategy: 偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。
        :type consumer_strategy: str
        :param dws_cluster_name: 存储该通道数据的DWS集群名称。
        :type dws_cluster_name: str
        :param dws_cluster_id: 存储该通道数据的DWS集群ID。
        :type dws_cluster_id: str
        :param dws_database_name: 存储该通道数据的DWS数据库名称。
        :type dws_database_name: str
        :param dws_schema: 存储该通道数据的DWS数据库模式。
        :type dws_schema: str
        :param dws_table_name: 存储该通道数据的DWS数据库模式下的数据表。
        :type dws_table_name: str
        :param dws_delimiter: 用户数据的字段分隔符，根据此分隔符分隔用户数据插入DWS数据表的相应列。  取值范围：“，”、“；”和“|”三种字符中的一个。
        :type dws_delimiter: str
        :param user_name: 存储该通道数据的DWS数据库的用户名。
        :type user_name: str
        :param user_password: 存储该通道数据的DWS数据库的密码。
        :type user_password: str
        :param kms_user_key_name: 用户在密钥管理服务（简称KMS）创建的用户主密钥名称，用于加密存储DWS数据库的密码。
        :type kms_user_key_name: str
        :param kms_user_key_id: 用户在密钥管理服务（简称KMS）创建的用户主密钥ID，用于加密存储DWS数据库的密码。
        :type kms_user_key_id: str
        :param obs_bucket_path: 临时存储该通道数据的OBS桶名称。
        :type obs_bucket_path: str
        :param file_prefix: 临时存储该通道数据的OBS桶下的自定义目录，多级目录可用“/”进行分隔，不可以“/”开头。  取值范围：英文字母、数字、下划线和斜杠，最大长度为50个字符。  默认配置为空。
        :type file_prefix: str
        :param retry_duration: 用户数据导入DWS集群失败的重试失效时间。超出此配置项配置的时间，转储DWS失败的数据将备份至“OBS桶/ file_prefix/dws_error”目录下。  取值范围： 0～7200。  单位：秒。  默认配置为1800。
        :type retry_duration: str
        :param dws_table_columns: 指定要转储到DWS表中的列，为null或者为空则默认全列。比如“c1,c2”表示将Schema中c1和c2这两列转储到DWS。  默认为空。
        :type dws_table_columns: str
        :param options: 
        :type options: :class:`huaweicloudsdkdis.v2.Options`
        """
        
        

        self._task_name = None
        self._agency_name = None
        self._deliver_time_interval = None
        self._consumer_strategy = None
        self._dws_cluster_name = None
        self._dws_cluster_id = None
        self._dws_database_name = None
        self._dws_schema = None
        self._dws_table_name = None
        self._dws_delimiter = None
        self._user_name = None
        self._user_password = None
        self._kms_user_key_name = None
        self._kms_user_key_id = None
        self._obs_bucket_path = None
        self._file_prefix = None
        self._retry_duration = None
        self._dws_table_columns = None
        self._options = None
        self.discriminator = None

        self.task_name = task_name
        self.agency_name = agency_name
        self.deliver_time_interval = deliver_time_interval
        if consumer_strategy is not None:
            self.consumer_strategy = consumer_strategy
        self.dws_cluster_name = dws_cluster_name
        self.dws_cluster_id = dws_cluster_id
        self.dws_database_name = dws_database_name
        self.dws_schema = dws_schema
        self.dws_table_name = dws_table_name
        self.dws_delimiter = dws_delimiter
        self.user_name = user_name
        self.user_password = user_password
        self.kms_user_key_name = kms_user_key_name
        self.kms_user_key_id = kms_user_key_id
        self.obs_bucket_path = obs_bucket_path
        if file_prefix is not None:
            self.file_prefix = file_prefix
        if retry_duration is not None:
            self.retry_duration = retry_duration
        if dws_table_columns is not None:
            self.dws_table_columns = dws_table_columns
        if options is not None:
            self.options = options

    @property
    def task_name(self):
        r"""Gets the task_name of this DWSDestinationDescriptorRequest.

        转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。

        :return: The task_name of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this DWSDestinationDescriptorRequest.

        转储任务的名称。  任务名称由英文字母、数字、中划线和下划线组成。长度为1～64个字符。

        :param task_name: The task_name of this DWSDestinationDescriptorRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def agency_name(self):
        r"""Gets the agency_name of this DWSDestinationDescriptorRequest.

        在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency

        :return: The agency_name of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this DWSDestinationDescriptorRequest.

        在统一身份认证服务(IAM)中创建委托的名称，DIS需要获取IAM委托信息去访问您指定的资源。创建委托的参数设置如下： - 委托类型：云服务 - 云服务：DIS - 持续时间：永久 - “所属区域”为“全局服务”，“项目”为“对象存储服务”对应的“策略”包含“Tenant Administrator”。 如果已经创建过委托，可以使用IAM服务提供的查询委托列表接口，获取有效可用的委托名称。 取值范围：长度不超过64位，且不可配置为空。  如果有在Console控制台使用转储任务，会提示自动创建委托，自动创建的委托名称为：dis_admin_agency

        :param agency_name: The agency_name of this DWSDestinationDescriptorRequest.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def deliver_time_interval(self):
        r"""Gets the deliver_time_interval of this DWSDestinationDescriptorRequest.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒

        :return: The deliver_time_interval of this DWSDestinationDescriptorRequest.
        :rtype: int
        """
        return self._deliver_time_interval

    @deliver_time_interval.setter
    def deliver_time_interval(self, deliver_time_interval):
        r"""Sets the deliver_time_interval of this DWSDestinationDescriptorRequest.

        根据用户配置的时间，周期性的将数据导入OBS，若某个时间段内无数据，则此时间段不会生成打包文件。  单位：秒

        :param deliver_time_interval: The deliver_time_interval of this DWSDestinationDescriptorRequest.
        :type deliver_time_interval: int
        """
        self._deliver_time_interval = deliver_time_interval

    @property
    def consumer_strategy(self):
        r"""Gets the consumer_strategy of this DWSDestinationDescriptorRequest.

        偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。

        :return: The consumer_strategy of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._consumer_strategy

    @consumer_strategy.setter
    def consumer_strategy(self, consumer_strategy):
        r"""Sets the consumer_strategy of this DWSDestinationDescriptorRequest.

        偏移量。  - LATEST：最大偏移量，即获取最新的数据。 - TRIM_HORIZON：最小偏移量，即读取最早的数据。

        :param consumer_strategy: The consumer_strategy of this DWSDestinationDescriptorRequest.
        :type consumer_strategy: str
        """
        self._consumer_strategy = consumer_strategy

    @property
    def dws_cluster_name(self):
        r"""Gets the dws_cluster_name of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS集群名称。

        :return: The dws_cluster_name of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._dws_cluster_name

    @dws_cluster_name.setter
    def dws_cluster_name(self, dws_cluster_name):
        r"""Sets the dws_cluster_name of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS集群名称。

        :param dws_cluster_name: The dws_cluster_name of this DWSDestinationDescriptorRequest.
        :type dws_cluster_name: str
        """
        self._dws_cluster_name = dws_cluster_name

    @property
    def dws_cluster_id(self):
        r"""Gets the dws_cluster_id of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS集群ID。

        :return: The dws_cluster_id of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._dws_cluster_id

    @dws_cluster_id.setter
    def dws_cluster_id(self, dws_cluster_id):
        r"""Sets the dws_cluster_id of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS集群ID。

        :param dws_cluster_id: The dws_cluster_id of this DWSDestinationDescriptorRequest.
        :type dws_cluster_id: str
        """
        self._dws_cluster_id = dws_cluster_id

    @property
    def dws_database_name(self):
        r"""Gets the dws_database_name of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS数据库名称。

        :return: The dws_database_name of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._dws_database_name

    @dws_database_name.setter
    def dws_database_name(self, dws_database_name):
        r"""Sets the dws_database_name of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS数据库名称。

        :param dws_database_name: The dws_database_name of this DWSDestinationDescriptorRequest.
        :type dws_database_name: str
        """
        self._dws_database_name = dws_database_name

    @property
    def dws_schema(self):
        r"""Gets the dws_schema of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS数据库模式。

        :return: The dws_schema of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._dws_schema

    @dws_schema.setter
    def dws_schema(self, dws_schema):
        r"""Sets the dws_schema of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS数据库模式。

        :param dws_schema: The dws_schema of this DWSDestinationDescriptorRequest.
        :type dws_schema: str
        """
        self._dws_schema = dws_schema

    @property
    def dws_table_name(self):
        r"""Gets the dws_table_name of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS数据库模式下的数据表。

        :return: The dws_table_name of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._dws_table_name

    @dws_table_name.setter
    def dws_table_name(self, dws_table_name):
        r"""Sets the dws_table_name of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS数据库模式下的数据表。

        :param dws_table_name: The dws_table_name of this DWSDestinationDescriptorRequest.
        :type dws_table_name: str
        """
        self._dws_table_name = dws_table_name

    @property
    def dws_delimiter(self):
        r"""Gets the dws_delimiter of this DWSDestinationDescriptorRequest.

        用户数据的字段分隔符，根据此分隔符分隔用户数据插入DWS数据表的相应列。  取值范围：“，”、“；”和“|”三种字符中的一个。

        :return: The dws_delimiter of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._dws_delimiter

    @dws_delimiter.setter
    def dws_delimiter(self, dws_delimiter):
        r"""Sets the dws_delimiter of this DWSDestinationDescriptorRequest.

        用户数据的字段分隔符，根据此分隔符分隔用户数据插入DWS数据表的相应列。  取值范围：“，”、“；”和“|”三种字符中的一个。

        :param dws_delimiter: The dws_delimiter of this DWSDestinationDescriptorRequest.
        :type dws_delimiter: str
        """
        self._dws_delimiter = dws_delimiter

    @property
    def user_name(self):
        r"""Gets the user_name of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS数据库的用户名。

        :return: The user_name of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS数据库的用户名。

        :param user_name: The user_name of this DWSDestinationDescriptorRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_password(self):
        r"""Gets the user_password of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS数据库的密码。

        :return: The user_password of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        r"""Sets the user_password of this DWSDestinationDescriptorRequest.

        存储该通道数据的DWS数据库的密码。

        :param user_password: The user_password of this DWSDestinationDescriptorRequest.
        :type user_password: str
        """
        self._user_password = user_password

    @property
    def kms_user_key_name(self):
        r"""Gets the kms_user_key_name of this DWSDestinationDescriptorRequest.

        用户在密钥管理服务（简称KMS）创建的用户主密钥名称，用于加密存储DWS数据库的密码。

        :return: The kms_user_key_name of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._kms_user_key_name

    @kms_user_key_name.setter
    def kms_user_key_name(self, kms_user_key_name):
        r"""Sets the kms_user_key_name of this DWSDestinationDescriptorRequest.

        用户在密钥管理服务（简称KMS）创建的用户主密钥名称，用于加密存储DWS数据库的密码。

        :param kms_user_key_name: The kms_user_key_name of this DWSDestinationDescriptorRequest.
        :type kms_user_key_name: str
        """
        self._kms_user_key_name = kms_user_key_name

    @property
    def kms_user_key_id(self):
        r"""Gets the kms_user_key_id of this DWSDestinationDescriptorRequest.

        用户在密钥管理服务（简称KMS）创建的用户主密钥ID，用于加密存储DWS数据库的密码。

        :return: The kms_user_key_id of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._kms_user_key_id

    @kms_user_key_id.setter
    def kms_user_key_id(self, kms_user_key_id):
        r"""Sets the kms_user_key_id of this DWSDestinationDescriptorRequest.

        用户在密钥管理服务（简称KMS）创建的用户主密钥ID，用于加密存储DWS数据库的密码。

        :param kms_user_key_id: The kms_user_key_id of this DWSDestinationDescriptorRequest.
        :type kms_user_key_id: str
        """
        self._kms_user_key_id = kms_user_key_id

    @property
    def obs_bucket_path(self):
        r"""Gets the obs_bucket_path of this DWSDestinationDescriptorRequest.

        临时存储该通道数据的OBS桶名称。

        :return: The obs_bucket_path of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._obs_bucket_path

    @obs_bucket_path.setter
    def obs_bucket_path(self, obs_bucket_path):
        r"""Sets the obs_bucket_path of this DWSDestinationDescriptorRequest.

        临时存储该通道数据的OBS桶名称。

        :param obs_bucket_path: The obs_bucket_path of this DWSDestinationDescriptorRequest.
        :type obs_bucket_path: str
        """
        self._obs_bucket_path = obs_bucket_path

    @property
    def file_prefix(self):
        r"""Gets the file_prefix of this DWSDestinationDescriptorRequest.

        临时存储该通道数据的OBS桶下的自定义目录，多级目录可用“/”进行分隔，不可以“/”开头。  取值范围：英文字母、数字、下划线和斜杠，最大长度为50个字符。  默认配置为空。

        :return: The file_prefix of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._file_prefix

    @file_prefix.setter
    def file_prefix(self, file_prefix):
        r"""Sets the file_prefix of this DWSDestinationDescriptorRequest.

        临时存储该通道数据的OBS桶下的自定义目录，多级目录可用“/”进行分隔，不可以“/”开头。  取值范围：英文字母、数字、下划线和斜杠，最大长度为50个字符。  默认配置为空。

        :param file_prefix: The file_prefix of this DWSDestinationDescriptorRequest.
        :type file_prefix: str
        """
        self._file_prefix = file_prefix

    @property
    def retry_duration(self):
        r"""Gets the retry_duration of this DWSDestinationDescriptorRequest.

        用户数据导入DWS集群失败的重试失效时间。超出此配置项配置的时间，转储DWS失败的数据将备份至“OBS桶/ file_prefix/dws_error”目录下。  取值范围： 0～7200。  单位：秒。  默认配置为1800。

        :return: The retry_duration of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._retry_duration

    @retry_duration.setter
    def retry_duration(self, retry_duration):
        r"""Sets the retry_duration of this DWSDestinationDescriptorRequest.

        用户数据导入DWS集群失败的重试失效时间。超出此配置项配置的时间，转储DWS失败的数据将备份至“OBS桶/ file_prefix/dws_error”目录下。  取值范围： 0～7200。  单位：秒。  默认配置为1800。

        :param retry_duration: The retry_duration of this DWSDestinationDescriptorRequest.
        :type retry_duration: str
        """
        self._retry_duration = retry_duration

    @property
    def dws_table_columns(self):
        r"""Gets the dws_table_columns of this DWSDestinationDescriptorRequest.

        指定要转储到DWS表中的列，为null或者为空则默认全列。比如“c1,c2”表示将Schema中c1和c2这两列转储到DWS。  默认为空。

        :return: The dws_table_columns of this DWSDestinationDescriptorRequest.
        :rtype: str
        """
        return self._dws_table_columns

    @dws_table_columns.setter
    def dws_table_columns(self, dws_table_columns):
        r"""Sets the dws_table_columns of this DWSDestinationDescriptorRequest.

        指定要转储到DWS表中的列，为null或者为空则默认全列。比如“c1,c2”表示将Schema中c1和c2这两列转储到DWS。  默认为空。

        :param dws_table_columns: The dws_table_columns of this DWSDestinationDescriptorRequest.
        :type dws_table_columns: str
        """
        self._dws_table_columns = dws_table_columns

    @property
    def options(self):
        r"""Gets the options of this DWSDestinationDescriptorRequest.

        :return: The options of this DWSDestinationDescriptorRequest.
        :rtype: :class:`huaweicloudsdkdis.v2.Options`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this DWSDestinationDescriptorRequest.

        :param options: The options of this DWSDestinationDescriptorRequest.
        :type options: :class:`huaweicloudsdkdis.v2.Options`
        """
        self._options = options

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
        if not isinstance(other, DWSDestinationDescriptorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
