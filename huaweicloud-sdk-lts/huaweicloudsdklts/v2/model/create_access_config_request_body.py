# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccessConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_config_name': 'str',
        'access_config_type': 'str',
        'access_config_detail': 'AccessConfigDeatilCreate',
        'log_info': 'AccessConfigBaseLogInfoCreate',
        'host_group_info': 'AccessConfigHostGroupIdListCreate',
        'access_config_tag': 'list[AccessConfigTag]',
        'binary_collect': 'bool',
        'log_split': 'bool',
        'cluster_id': 'str',
        'incremental_collect': 'bool',
        'encoding_format': 'str',
        'processor_type': 'str',
        'demo_log': 'str',
        'demo_fields': 'list[DemoFieldAccess]',
        'processors': 'list[Processor]',
        'application_id': 'str',
        'environment_id': 'str',
        'component_id': 'list[str]',
        'access_config_type_source': 'str'
    }

    attribute_map = {
        'access_config_name': 'access_config_name',
        'access_config_type': 'access_config_type',
        'access_config_detail': 'access_config_detail',
        'log_info': 'log_info',
        'host_group_info': 'host_group_info',
        'access_config_tag': 'access_config_tag',
        'binary_collect': 'binary_collect',
        'log_split': 'log_split',
        'cluster_id': 'cluster_id',
        'incremental_collect': 'incremental_collect',
        'encoding_format': 'encoding_format',
        'processor_type': 'processor_type',
        'demo_log': 'demo_log',
        'demo_fields': 'demo_fields',
        'processors': 'processors',
        'application_id': 'application_id',
        'environment_id': 'environment_id',
        'component_id': 'component_id',
        'access_config_type_source': 'access_config_type_source'
    }

    def __init__(self, access_config_name=None, access_config_type=None, access_config_detail=None, log_info=None, host_group_info=None, access_config_tag=None, binary_collect=None, log_split=None, cluster_id=None, incremental_collect=None, encoding_format=None, processor_type=None, demo_log=None, demo_fields=None, processors=None, application_id=None, environment_id=None, component_id=None, access_config_type_source=None):
        r"""CreateAccessConfigRequestBody

        The model defined in huaweicloud sdk

        :param access_config_name: 日志接入名称。 满足正则表达式：^(?!\\.)(?!_)(?!.*?\\.$)[\\u4e00-\\u9fa5a-zA-Z0-9-_.]{1,64}$
        :type access_config_name: str
        :param access_config_type: 日志接入类型。AGENT：ECS接入,K8S_CCE:CCE接入
        :type access_config_type: str
        :param access_config_detail: 
        :type access_config_detail: :class:`huaweicloudsdklts.v2.AccessConfigDeatilCreate`
        :param log_info: 
        :type log_info: :class:`huaweicloudsdklts.v2.AccessConfigBaseLogInfoCreate`
        :param host_group_info: 
        :type host_group_info: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdListCreate`
        :param access_config_tag: 标签信息。KEY不能重复,最多20个标签
        :type access_config_tag: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        :param binary_collect: 二进制采集
        :type binary_collect: bool
        :param log_split: 日志拆分
        :type log_split: bool
        :param cluster_id: CCE集群ID，当CCE类型时，为必填
        :type cluster_id: str
        :param incremental_collect: 是否增量采集 true 为是   false为否（全量采集）
        :type incremental_collect: bool
        :param encoding_format: 编码格式，支持UTF-8，GDB默认UTF-8
        :type encoding_format: str
        :param processor_type: IC结构化解析类型包括 ：SINGLE_LINE 单行全文，MULTI_LINE 多行全文，REGEX 单行正则，MULTI_REGEX 多行正则，SPLIT 分隔符，JSON JSON解析，NGINX nginx解析， COMPOSE组合解析
        :type processor_type: str
        :param demo_log: 示例日志
        :type demo_log: str
        :param demo_fields: 示例日志解析字段
        :type demo_fields: list[:class:`huaweicloudsdklts.v2.DemoFieldAccess`]
        :param processors: IC结构化解析器
        :type processors: list[:class:`huaweicloudsdklts.v2.Processor`]
        :param application_id: ServiceStage应用ID
        :type application_id: str
        :param environment_id: ServiceStage环境ID
        :type environment_id: str
        :param component_id: ServiceStage组件ID
        :type component_id: list[str]
        :param access_config_type_source: 日志接入自建软件来源
        :type access_config_type_source: str
        """
        
        

        self._access_config_name = None
        self._access_config_type = None
        self._access_config_detail = None
        self._log_info = None
        self._host_group_info = None
        self._access_config_tag = None
        self._binary_collect = None
        self._log_split = None
        self._cluster_id = None
        self._incremental_collect = None
        self._encoding_format = None
        self._processor_type = None
        self._demo_log = None
        self._demo_fields = None
        self._processors = None
        self._application_id = None
        self._environment_id = None
        self._component_id = None
        self._access_config_type_source = None
        self.discriminator = None

        self.access_config_name = access_config_name
        self.access_config_type = access_config_type
        self.access_config_detail = access_config_detail
        self.log_info = log_info
        if host_group_info is not None:
            self.host_group_info = host_group_info
        if access_config_tag is not None:
            self.access_config_tag = access_config_tag
        if binary_collect is not None:
            self.binary_collect = binary_collect
        if log_split is not None:
            self.log_split = log_split
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if incremental_collect is not None:
            self.incremental_collect = incremental_collect
        if encoding_format is not None:
            self.encoding_format = encoding_format
        if processor_type is not None:
            self.processor_type = processor_type
        if demo_log is not None:
            self.demo_log = demo_log
        if demo_fields is not None:
            self.demo_fields = demo_fields
        if processors is not None:
            self.processors = processors
        if application_id is not None:
            self.application_id = application_id
        if environment_id is not None:
            self.environment_id = environment_id
        if component_id is not None:
            self.component_id = component_id
        if access_config_type_source is not None:
            self.access_config_type_source = access_config_type_source

    @property
    def access_config_name(self):
        r"""Gets the access_config_name of this CreateAccessConfigRequestBody.

        日志接入名称。 满足正则表达式：^(?!\\.)(?!_)(?!.*?\\.$)[\\u4e00-\\u9fa5a-zA-Z0-9-_.]{1,64}$

        :return: The access_config_name of this CreateAccessConfigRequestBody.
        :rtype: str
        """
        return self._access_config_name

    @access_config_name.setter
    def access_config_name(self, access_config_name):
        r"""Sets the access_config_name of this CreateAccessConfigRequestBody.

        日志接入名称。 满足正则表达式：^(?!\\.)(?!_)(?!.*?\\.$)[\\u4e00-\\u9fa5a-zA-Z0-9-_.]{1,64}$

        :param access_config_name: The access_config_name of this CreateAccessConfigRequestBody.
        :type access_config_name: str
        """
        self._access_config_name = access_config_name

    @property
    def access_config_type(self):
        r"""Gets the access_config_type of this CreateAccessConfigRequestBody.

        日志接入类型。AGENT：ECS接入,K8S_CCE:CCE接入

        :return: The access_config_type of this CreateAccessConfigRequestBody.
        :rtype: str
        """
        return self._access_config_type

    @access_config_type.setter
    def access_config_type(self, access_config_type):
        r"""Sets the access_config_type of this CreateAccessConfigRequestBody.

        日志接入类型。AGENT：ECS接入,K8S_CCE:CCE接入

        :param access_config_type: The access_config_type of this CreateAccessConfigRequestBody.
        :type access_config_type: str
        """
        self._access_config_type = access_config_type

    @property
    def access_config_detail(self):
        r"""Gets the access_config_detail of this CreateAccessConfigRequestBody.

        :return: The access_config_detail of this CreateAccessConfigRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigDeatilCreate`
        """
        return self._access_config_detail

    @access_config_detail.setter
    def access_config_detail(self, access_config_detail):
        r"""Sets the access_config_detail of this CreateAccessConfigRequestBody.

        :param access_config_detail: The access_config_detail of this CreateAccessConfigRequestBody.
        :type access_config_detail: :class:`huaweicloudsdklts.v2.AccessConfigDeatilCreate`
        """
        self._access_config_detail = access_config_detail

    @property
    def log_info(self):
        r"""Gets the log_info of this CreateAccessConfigRequestBody.

        :return: The log_info of this CreateAccessConfigRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigBaseLogInfoCreate`
        """
        return self._log_info

    @log_info.setter
    def log_info(self, log_info):
        r"""Sets the log_info of this CreateAccessConfigRequestBody.

        :param log_info: The log_info of this CreateAccessConfigRequestBody.
        :type log_info: :class:`huaweicloudsdklts.v2.AccessConfigBaseLogInfoCreate`
        """
        self._log_info = log_info

    @property
    def host_group_info(self):
        r"""Gets the host_group_info of this CreateAccessConfigRequestBody.

        :return: The host_group_info of this CreateAccessConfigRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdListCreate`
        """
        return self._host_group_info

    @host_group_info.setter
    def host_group_info(self, host_group_info):
        r"""Sets the host_group_info of this CreateAccessConfigRequestBody.

        :param host_group_info: The host_group_info of this CreateAccessConfigRequestBody.
        :type host_group_info: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdListCreate`
        """
        self._host_group_info = host_group_info

    @property
    def access_config_tag(self):
        r"""Gets the access_config_tag of this CreateAccessConfigRequestBody.

        标签信息。KEY不能重复,最多20个标签

        :return: The access_config_tag of this CreateAccessConfigRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        return self._access_config_tag

    @access_config_tag.setter
    def access_config_tag(self, access_config_tag):
        r"""Sets the access_config_tag of this CreateAccessConfigRequestBody.

        标签信息。KEY不能重复,最多20个标签

        :param access_config_tag: The access_config_tag of this CreateAccessConfigRequestBody.
        :type access_config_tag: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        self._access_config_tag = access_config_tag

    @property
    def binary_collect(self):
        r"""Gets the binary_collect of this CreateAccessConfigRequestBody.

        二进制采集

        :return: The binary_collect of this CreateAccessConfigRequestBody.
        :rtype: bool
        """
        return self._binary_collect

    @binary_collect.setter
    def binary_collect(self, binary_collect):
        r"""Sets the binary_collect of this CreateAccessConfigRequestBody.

        二进制采集

        :param binary_collect: The binary_collect of this CreateAccessConfigRequestBody.
        :type binary_collect: bool
        """
        self._binary_collect = binary_collect

    @property
    def log_split(self):
        r"""Gets the log_split of this CreateAccessConfigRequestBody.

        日志拆分

        :return: The log_split of this CreateAccessConfigRequestBody.
        :rtype: bool
        """
        return self._log_split

    @log_split.setter
    def log_split(self, log_split):
        r"""Sets the log_split of this CreateAccessConfigRequestBody.

        日志拆分

        :param log_split: The log_split of this CreateAccessConfigRequestBody.
        :type log_split: bool
        """
        self._log_split = log_split

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CreateAccessConfigRequestBody.

        CCE集群ID，当CCE类型时，为必填

        :return: The cluster_id of this CreateAccessConfigRequestBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CreateAccessConfigRequestBody.

        CCE集群ID，当CCE类型时，为必填

        :param cluster_id: The cluster_id of this CreateAccessConfigRequestBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def incremental_collect(self):
        r"""Gets the incremental_collect of this CreateAccessConfigRequestBody.

        是否增量采集 true 为是   false为否（全量采集）

        :return: The incremental_collect of this CreateAccessConfigRequestBody.
        :rtype: bool
        """
        return self._incremental_collect

    @incremental_collect.setter
    def incremental_collect(self, incremental_collect):
        r"""Sets the incremental_collect of this CreateAccessConfigRequestBody.

        是否增量采集 true 为是   false为否（全量采集）

        :param incremental_collect: The incremental_collect of this CreateAccessConfigRequestBody.
        :type incremental_collect: bool
        """
        self._incremental_collect = incremental_collect

    @property
    def encoding_format(self):
        r"""Gets the encoding_format of this CreateAccessConfigRequestBody.

        编码格式，支持UTF-8，GDB默认UTF-8

        :return: The encoding_format of this CreateAccessConfigRequestBody.
        :rtype: str
        """
        return self._encoding_format

    @encoding_format.setter
    def encoding_format(self, encoding_format):
        r"""Sets the encoding_format of this CreateAccessConfigRequestBody.

        编码格式，支持UTF-8，GDB默认UTF-8

        :param encoding_format: The encoding_format of this CreateAccessConfigRequestBody.
        :type encoding_format: str
        """
        self._encoding_format = encoding_format

    @property
    def processor_type(self):
        r"""Gets the processor_type of this CreateAccessConfigRequestBody.

        IC结构化解析类型包括 ：SINGLE_LINE 单行全文，MULTI_LINE 多行全文，REGEX 单行正则，MULTI_REGEX 多行正则，SPLIT 分隔符，JSON JSON解析，NGINX nginx解析， COMPOSE组合解析

        :return: The processor_type of this CreateAccessConfigRequestBody.
        :rtype: str
        """
        return self._processor_type

    @processor_type.setter
    def processor_type(self, processor_type):
        r"""Sets the processor_type of this CreateAccessConfigRequestBody.

        IC结构化解析类型包括 ：SINGLE_LINE 单行全文，MULTI_LINE 多行全文，REGEX 单行正则，MULTI_REGEX 多行正则，SPLIT 分隔符，JSON JSON解析，NGINX nginx解析， COMPOSE组合解析

        :param processor_type: The processor_type of this CreateAccessConfigRequestBody.
        :type processor_type: str
        """
        self._processor_type = processor_type

    @property
    def demo_log(self):
        r"""Gets the demo_log of this CreateAccessConfigRequestBody.

        示例日志

        :return: The demo_log of this CreateAccessConfigRequestBody.
        :rtype: str
        """
        return self._demo_log

    @demo_log.setter
    def demo_log(self, demo_log):
        r"""Sets the demo_log of this CreateAccessConfigRequestBody.

        示例日志

        :param demo_log: The demo_log of this CreateAccessConfigRequestBody.
        :type demo_log: str
        """
        self._demo_log = demo_log

    @property
    def demo_fields(self):
        r"""Gets the demo_fields of this CreateAccessConfigRequestBody.

        示例日志解析字段

        :return: The demo_fields of this CreateAccessConfigRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.DemoFieldAccess`]
        """
        return self._demo_fields

    @demo_fields.setter
    def demo_fields(self, demo_fields):
        r"""Sets the demo_fields of this CreateAccessConfigRequestBody.

        示例日志解析字段

        :param demo_fields: The demo_fields of this CreateAccessConfigRequestBody.
        :type demo_fields: list[:class:`huaweicloudsdklts.v2.DemoFieldAccess`]
        """
        self._demo_fields = demo_fields

    @property
    def processors(self):
        r"""Gets the processors of this CreateAccessConfigRequestBody.

        IC结构化解析器

        :return: The processors of this CreateAccessConfigRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.Processor`]
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        r"""Sets the processors of this CreateAccessConfigRequestBody.

        IC结构化解析器

        :param processors: The processors of this CreateAccessConfigRequestBody.
        :type processors: list[:class:`huaweicloudsdklts.v2.Processor`]
        """
        self._processors = processors

    @property
    def application_id(self):
        r"""Gets the application_id of this CreateAccessConfigRequestBody.

        ServiceStage应用ID

        :return: The application_id of this CreateAccessConfigRequestBody.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this CreateAccessConfigRequestBody.

        ServiceStage应用ID

        :param application_id: The application_id of this CreateAccessConfigRequestBody.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def environment_id(self):
        r"""Gets the environment_id of this CreateAccessConfigRequestBody.

        ServiceStage环境ID

        :return: The environment_id of this CreateAccessConfigRequestBody.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        r"""Sets the environment_id of this CreateAccessConfigRequestBody.

        ServiceStage环境ID

        :param environment_id: The environment_id of this CreateAccessConfigRequestBody.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def component_id(self):
        r"""Gets the component_id of this CreateAccessConfigRequestBody.

        ServiceStage组件ID

        :return: The component_id of this CreateAccessConfigRequestBody.
        :rtype: list[str]
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this CreateAccessConfigRequestBody.

        ServiceStage组件ID

        :param component_id: The component_id of this CreateAccessConfigRequestBody.
        :type component_id: list[str]
        """
        self._component_id = component_id

    @property
    def access_config_type_source(self):
        r"""Gets the access_config_type_source of this CreateAccessConfigRequestBody.

        日志接入自建软件来源

        :return: The access_config_type_source of this CreateAccessConfigRequestBody.
        :rtype: str
        """
        return self._access_config_type_source

    @access_config_type_source.setter
    def access_config_type_source(self, access_config_type_source):
        r"""Sets the access_config_type_source of this CreateAccessConfigRequestBody.

        日志接入自建软件来源

        :param access_config_type_source: The access_config_type_source of this CreateAccessConfigRequestBody.
        :type access_config_type_source: str
        """
        self._access_config_type_source = access_config_type_source

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
        if not isinstance(other, CreateAccessConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
