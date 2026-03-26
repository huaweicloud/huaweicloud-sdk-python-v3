# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkJobConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'main_file_path': 'str',
        'main_class': 'str',
        'main_arguments': 'list[str]',
        'spark_conf': 'str',
        'driver_resource_spec': 'str',
        'executor_resource_spec': 'str',
        'num_executors': 'int',
        'enable_dynamic_allocation': 'bool',
        'min_num_executors': 'int',
        'max_num_executors': 'int',
        'user_log_path': 'str',
        'metastore_id': 'str',
        'metastore_catalog_id': 'str'
    }

    attribute_map = {
        'main_file_path': 'main_file_path',
        'main_class': 'main_class',
        'main_arguments': 'main_arguments',
        'spark_conf': 'spark_conf',
        'driver_resource_spec': 'driver_resource_spec',
        'executor_resource_spec': 'executor_resource_spec',
        'num_executors': 'num_executors',
        'enable_dynamic_allocation': 'enable_dynamic_allocation',
        'min_num_executors': 'min_num_executors',
        'max_num_executors': 'max_num_executors',
        'user_log_path': 'user_log_path',
        'metastore_id': 'metastore_id',
        'metastore_catalog_id': 'metastore_catalog_id'
    }

    def __init__(self, main_file_path=None, main_class=None, main_arguments=None, spark_conf=None, driver_resource_spec=None, executor_resource_spec=None, num_executors=None, enable_dynamic_allocation=None, min_num_executors=None, max_num_executors=None, user_log_path=None, metastore_id=None, metastore_catalog_id=None):
        r"""SparkJobConfig

        The model defined in huaweicloud sdk

        :param main_file_path: Job主文件，obs上的python文件或jar包
        :type main_file_path: str
        :param main_class: Java job需指定主类
        :type main_class: str
        :param main_arguments: Python主文件的运行参数或Java主类的运行参数
        :type main_arguments: list[str]
        :param spark_conf: 自定义的spark配置值
        :type spark_conf: str
        :param driver_resource_spec: driver资源规格
        :type driver_resource_spec: str
        :param executor_resource_spec: executor资源规格
        :type executor_resource_spec: str
        :param num_executors: executor数量
        :type num_executors: int
        :param enable_dynamic_allocation: 是否开启dynamic alocation
        :type enable_dynamic_allocation: bool
        :param min_num_executors: executor最少个数
        :type min_num_executors: int
        :param max_num_executors: executor最多个数
        :type max_num_executors: int
        :param user_log_path: 用户日志obs存储位置
        :type user_log_path: str
        :param metastore_id: Metastore信息，LakeFormation服务的实例Id，即MetaStoreId。
        :type metastore_id: str
        :param metastore_catalog_id: metastore catalog id，即lakeformation catalog id
        :type metastore_catalog_id: str
        """
        
        

        self._main_file_path = None
        self._main_class = None
        self._main_arguments = None
        self._spark_conf = None
        self._driver_resource_spec = None
        self._executor_resource_spec = None
        self._num_executors = None
        self._enable_dynamic_allocation = None
        self._min_num_executors = None
        self._max_num_executors = None
        self._user_log_path = None
        self._metastore_id = None
        self._metastore_catalog_id = None
        self.discriminator = None

        if main_file_path is not None:
            self.main_file_path = main_file_path
        if main_class is not None:
            self.main_class = main_class
        if main_arguments is not None:
            self.main_arguments = main_arguments
        if spark_conf is not None:
            self.spark_conf = spark_conf
        self.driver_resource_spec = driver_resource_spec
        self.executor_resource_spec = executor_resource_spec
        if num_executors is not None:
            self.num_executors = num_executors
        if enable_dynamic_allocation is not None:
            self.enable_dynamic_allocation = enable_dynamic_allocation
        if min_num_executors is not None:
            self.min_num_executors = min_num_executors
        if max_num_executors is not None:
            self.max_num_executors = max_num_executors
        if user_log_path is not None:
            self.user_log_path = user_log_path
        if metastore_id is not None:
            self.metastore_id = metastore_id
        if metastore_catalog_id is not None:
            self.metastore_catalog_id = metastore_catalog_id

    @property
    def main_file_path(self):
        r"""Gets the main_file_path of this SparkJobConfig.

        Job主文件，obs上的python文件或jar包

        :return: The main_file_path of this SparkJobConfig.
        :rtype: str
        """
        return self._main_file_path

    @main_file_path.setter
    def main_file_path(self, main_file_path):
        r"""Sets the main_file_path of this SparkJobConfig.

        Job主文件，obs上的python文件或jar包

        :param main_file_path: The main_file_path of this SparkJobConfig.
        :type main_file_path: str
        """
        self._main_file_path = main_file_path

    @property
    def main_class(self):
        r"""Gets the main_class of this SparkJobConfig.

        Java job需指定主类

        :return: The main_class of this SparkJobConfig.
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        r"""Sets the main_class of this SparkJobConfig.

        Java job需指定主类

        :param main_class: The main_class of this SparkJobConfig.
        :type main_class: str
        """
        self._main_class = main_class

    @property
    def main_arguments(self):
        r"""Gets the main_arguments of this SparkJobConfig.

        Python主文件的运行参数或Java主类的运行参数

        :return: The main_arguments of this SparkJobConfig.
        :rtype: list[str]
        """
        return self._main_arguments

    @main_arguments.setter
    def main_arguments(self, main_arguments):
        r"""Sets the main_arguments of this SparkJobConfig.

        Python主文件的运行参数或Java主类的运行参数

        :param main_arguments: The main_arguments of this SparkJobConfig.
        :type main_arguments: list[str]
        """
        self._main_arguments = main_arguments

    @property
    def spark_conf(self):
        r"""Gets the spark_conf of this SparkJobConfig.

        自定义的spark配置值

        :return: The spark_conf of this SparkJobConfig.
        :rtype: str
        """
        return self._spark_conf

    @spark_conf.setter
    def spark_conf(self, spark_conf):
        r"""Sets the spark_conf of this SparkJobConfig.

        自定义的spark配置值

        :param spark_conf: The spark_conf of this SparkJobConfig.
        :type spark_conf: str
        """
        self._spark_conf = spark_conf

    @property
    def driver_resource_spec(self):
        r"""Gets the driver_resource_spec of this SparkJobConfig.

        driver资源规格

        :return: The driver_resource_spec of this SparkJobConfig.
        :rtype: str
        """
        return self._driver_resource_spec

    @driver_resource_spec.setter
    def driver_resource_spec(self, driver_resource_spec):
        r"""Sets the driver_resource_spec of this SparkJobConfig.

        driver资源规格

        :param driver_resource_spec: The driver_resource_spec of this SparkJobConfig.
        :type driver_resource_spec: str
        """
        self._driver_resource_spec = driver_resource_spec

    @property
    def executor_resource_spec(self):
        r"""Gets the executor_resource_spec of this SparkJobConfig.

        executor资源规格

        :return: The executor_resource_spec of this SparkJobConfig.
        :rtype: str
        """
        return self._executor_resource_spec

    @executor_resource_spec.setter
    def executor_resource_spec(self, executor_resource_spec):
        r"""Sets the executor_resource_spec of this SparkJobConfig.

        executor资源规格

        :param executor_resource_spec: The executor_resource_spec of this SparkJobConfig.
        :type executor_resource_spec: str
        """
        self._executor_resource_spec = executor_resource_spec

    @property
    def num_executors(self):
        r"""Gets the num_executors of this SparkJobConfig.

        executor数量

        :return: The num_executors of this SparkJobConfig.
        :rtype: int
        """
        return self._num_executors

    @num_executors.setter
    def num_executors(self, num_executors):
        r"""Sets the num_executors of this SparkJobConfig.

        executor数量

        :param num_executors: The num_executors of this SparkJobConfig.
        :type num_executors: int
        """
        self._num_executors = num_executors

    @property
    def enable_dynamic_allocation(self):
        r"""Gets the enable_dynamic_allocation of this SparkJobConfig.

        是否开启dynamic alocation

        :return: The enable_dynamic_allocation of this SparkJobConfig.
        :rtype: bool
        """
        return self._enable_dynamic_allocation

    @enable_dynamic_allocation.setter
    def enable_dynamic_allocation(self, enable_dynamic_allocation):
        r"""Sets the enable_dynamic_allocation of this SparkJobConfig.

        是否开启dynamic alocation

        :param enable_dynamic_allocation: The enable_dynamic_allocation of this SparkJobConfig.
        :type enable_dynamic_allocation: bool
        """
        self._enable_dynamic_allocation = enable_dynamic_allocation

    @property
    def min_num_executors(self):
        r"""Gets the min_num_executors of this SparkJobConfig.

        executor最少个数

        :return: The min_num_executors of this SparkJobConfig.
        :rtype: int
        """
        return self._min_num_executors

    @min_num_executors.setter
    def min_num_executors(self, min_num_executors):
        r"""Sets the min_num_executors of this SparkJobConfig.

        executor最少个数

        :param min_num_executors: The min_num_executors of this SparkJobConfig.
        :type min_num_executors: int
        """
        self._min_num_executors = min_num_executors

    @property
    def max_num_executors(self):
        r"""Gets the max_num_executors of this SparkJobConfig.

        executor最多个数

        :return: The max_num_executors of this SparkJobConfig.
        :rtype: int
        """
        return self._max_num_executors

    @max_num_executors.setter
    def max_num_executors(self, max_num_executors):
        r"""Sets the max_num_executors of this SparkJobConfig.

        executor最多个数

        :param max_num_executors: The max_num_executors of this SparkJobConfig.
        :type max_num_executors: int
        """
        self._max_num_executors = max_num_executors

    @property
    def user_log_path(self):
        r"""Gets the user_log_path of this SparkJobConfig.

        用户日志obs存储位置

        :return: The user_log_path of this SparkJobConfig.
        :rtype: str
        """
        return self._user_log_path

    @user_log_path.setter
    def user_log_path(self, user_log_path):
        r"""Sets the user_log_path of this SparkJobConfig.

        用户日志obs存储位置

        :param user_log_path: The user_log_path of this SparkJobConfig.
        :type user_log_path: str
        """
        self._user_log_path = user_log_path

    @property
    def metastore_id(self):
        r"""Gets the metastore_id of this SparkJobConfig.

        Metastore信息，LakeFormation服务的实例Id，即MetaStoreId。

        :return: The metastore_id of this SparkJobConfig.
        :rtype: str
        """
        return self._metastore_id

    @metastore_id.setter
    def metastore_id(self, metastore_id):
        r"""Sets the metastore_id of this SparkJobConfig.

        Metastore信息，LakeFormation服务的实例Id，即MetaStoreId。

        :param metastore_id: The metastore_id of this SparkJobConfig.
        :type metastore_id: str
        """
        self._metastore_id = metastore_id

    @property
    def metastore_catalog_id(self):
        r"""Gets the metastore_catalog_id of this SparkJobConfig.

        metastore catalog id，即lakeformation catalog id

        :return: The metastore_catalog_id of this SparkJobConfig.
        :rtype: str
        """
        return self._metastore_catalog_id

    @metastore_catalog_id.setter
    def metastore_catalog_id(self, metastore_catalog_id):
        r"""Sets the metastore_catalog_id of this SparkJobConfig.

        metastore catalog id，即lakeformation catalog id

        :param metastore_catalog_id: The metastore_catalog_id of this SparkJobConfig.
        :type metastore_catalog_id: str
        """
        self._metastore_catalog_id = metastore_catalog_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SparkJobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
