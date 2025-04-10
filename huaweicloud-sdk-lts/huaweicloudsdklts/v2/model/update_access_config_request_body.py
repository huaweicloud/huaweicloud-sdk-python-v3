# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAccessConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_config_id': 'str',
        'access_config_name': 'str',
        'access_config_detail': 'AccessConfigDeatilUpdate',
        'host_group_info': 'AccessConfigHostGroupIdList',
        'access_config_tag': 'list[AccessConfigTag]',
        'log_split': 'bool',
        'binary_collect': 'bool',
        'cluster_id': 'str',
        'incremental_collect': 'bool',
        'encoding_format': 'str',
        'processor_type': 'str',
        'demo_log': 'str',
        'demo_fields': 'list[DemoFieldAccess]',
        'processors': 'list[Processor]',
        'application_id': 'str',
        'environment_id': 'str',
        'component_id': 'list[str]'
    }

    attribute_map = {
        'access_config_id': 'access_config_id',
        'access_config_name': 'access_config_name',
        'access_config_detail': 'access_config_detail',
        'host_group_info': 'host_group_info',
        'access_config_tag': 'access_config_tag',
        'log_split': 'log_split',
        'binary_collect': 'binary_collect',
        'cluster_id': 'cluster_id',
        'incremental_collect': 'incremental_collect',
        'encoding_format': 'encoding_format',
        'processor_type': 'processor_type',
        'demo_log': 'demo_log',
        'demo_fields': 'demo_fields',
        'processors': 'processors',
        'application_id': 'application_id',
        'environment_id': 'environment_id',
        'component_id': 'component_id'
    }

    def __init__(self, access_config_id=None, access_config_name=None, access_config_detail=None, host_group_info=None, access_config_tag=None, log_split=None, binary_collect=None, cluster_id=None, incremental_collect=None, encoding_format=None, processor_type=None, demo_log=None, demo_fields=None, processors=None, application_id=None, environment_id=None, component_id=None):
        r"""UpdateAccessConfigRequestBody

        The model defined in huaweicloud sdk

        :param access_config_id: 日志接入ID
        :type access_config_id: str
        :param access_config_name: 日志接入名称。 满足正则表达式：^(?!.)(?!)(?!.*?.$)[\\u4e00-\\u9fa5a-zA-Z0-9-.]{1,64}$
        :type access_config_name: str
        :param access_config_detail: 
        :type access_config_detail: :class:`huaweicloudsdklts.v2.AccessConfigDeatilUpdate`
        :param host_group_info: 
        :type host_group_info: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdList`
        :param access_config_tag: 标签信息。KEY不能重复,最多20个标签
        :type access_config_tag: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        :param log_split: 日志拆分
        :type log_split: bool
        :param binary_collect: 二进制采集
        :type binary_collect: bool
        :param cluster_id: CCE集群ID，CCE类型时，为必填
        :type cluster_id: str
        :param incremental_collect: 是否增量采集 true为是 false为否（全量采集）
        :type incremental_collect: bool
        :param encoding_format: 编码格式，默认UTF-8
        :type encoding_format: str
        :param processor_type: IC结构化解析类型
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
        """
        
        

        self._access_config_id = None
        self._access_config_name = None
        self._access_config_detail = None
        self._host_group_info = None
        self._access_config_tag = None
        self._log_split = None
        self._binary_collect = None
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
        self.discriminator = None

        self.access_config_id = access_config_id
        if access_config_name is not None:
            self.access_config_name = access_config_name
        if access_config_detail is not None:
            self.access_config_detail = access_config_detail
        if host_group_info is not None:
            self.host_group_info = host_group_info
        if access_config_tag is not None:
            self.access_config_tag = access_config_tag
        if log_split is not None:
            self.log_split = log_split
        if binary_collect is not None:
            self.binary_collect = binary_collect
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

    @property
    def access_config_id(self):
        r"""Gets the access_config_id of this UpdateAccessConfigRequestBody.

        日志接入ID

        :return: The access_config_id of this UpdateAccessConfigRequestBody.
        :rtype: str
        """
        return self._access_config_id

    @access_config_id.setter
    def access_config_id(self, access_config_id):
        r"""Sets the access_config_id of this UpdateAccessConfigRequestBody.

        日志接入ID

        :param access_config_id: The access_config_id of this UpdateAccessConfigRequestBody.
        :type access_config_id: str
        """
        self._access_config_id = access_config_id

    @property
    def access_config_name(self):
        r"""Gets the access_config_name of this UpdateAccessConfigRequestBody.

        日志接入名称。 满足正则表达式：^(?!.)(?!)(?!.*?.$)[\\u4e00-\\u9fa5a-zA-Z0-9-.]{1,64}$

        :return: The access_config_name of this UpdateAccessConfigRequestBody.
        :rtype: str
        """
        return self._access_config_name

    @access_config_name.setter
    def access_config_name(self, access_config_name):
        r"""Sets the access_config_name of this UpdateAccessConfigRequestBody.

        日志接入名称。 满足正则表达式：^(?!.)(?!)(?!.*?.$)[\\u4e00-\\u9fa5a-zA-Z0-9-.]{1,64}$

        :param access_config_name: The access_config_name of this UpdateAccessConfigRequestBody.
        :type access_config_name: str
        """
        self._access_config_name = access_config_name

    @property
    def access_config_detail(self):
        r"""Gets the access_config_detail of this UpdateAccessConfigRequestBody.

        :return: The access_config_detail of this UpdateAccessConfigRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigDeatilUpdate`
        """
        return self._access_config_detail

    @access_config_detail.setter
    def access_config_detail(self, access_config_detail):
        r"""Sets the access_config_detail of this UpdateAccessConfigRequestBody.

        :param access_config_detail: The access_config_detail of this UpdateAccessConfigRequestBody.
        :type access_config_detail: :class:`huaweicloudsdklts.v2.AccessConfigDeatilUpdate`
        """
        self._access_config_detail = access_config_detail

    @property
    def host_group_info(self):
        r"""Gets the host_group_info of this UpdateAccessConfigRequestBody.

        :return: The host_group_info of this UpdateAccessConfigRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdList`
        """
        return self._host_group_info

    @host_group_info.setter
    def host_group_info(self, host_group_info):
        r"""Sets the host_group_info of this UpdateAccessConfigRequestBody.

        :param host_group_info: The host_group_info of this UpdateAccessConfigRequestBody.
        :type host_group_info: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdList`
        """
        self._host_group_info = host_group_info

    @property
    def access_config_tag(self):
        r"""Gets the access_config_tag of this UpdateAccessConfigRequestBody.

        标签信息。KEY不能重复,最多20个标签

        :return: The access_config_tag of this UpdateAccessConfigRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        return self._access_config_tag

    @access_config_tag.setter
    def access_config_tag(self, access_config_tag):
        r"""Sets the access_config_tag of this UpdateAccessConfigRequestBody.

        标签信息。KEY不能重复,最多20个标签

        :param access_config_tag: The access_config_tag of this UpdateAccessConfigRequestBody.
        :type access_config_tag: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        self._access_config_tag = access_config_tag

    @property
    def log_split(self):
        r"""Gets the log_split of this UpdateAccessConfigRequestBody.

        日志拆分

        :return: The log_split of this UpdateAccessConfigRequestBody.
        :rtype: bool
        """
        return self._log_split

    @log_split.setter
    def log_split(self, log_split):
        r"""Sets the log_split of this UpdateAccessConfigRequestBody.

        日志拆分

        :param log_split: The log_split of this UpdateAccessConfigRequestBody.
        :type log_split: bool
        """
        self._log_split = log_split

    @property
    def binary_collect(self):
        r"""Gets the binary_collect of this UpdateAccessConfigRequestBody.

        二进制采集

        :return: The binary_collect of this UpdateAccessConfigRequestBody.
        :rtype: bool
        """
        return self._binary_collect

    @binary_collect.setter
    def binary_collect(self, binary_collect):
        r"""Sets the binary_collect of this UpdateAccessConfigRequestBody.

        二进制采集

        :param binary_collect: The binary_collect of this UpdateAccessConfigRequestBody.
        :type binary_collect: bool
        """
        self._binary_collect = binary_collect

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdateAccessConfigRequestBody.

        CCE集群ID，CCE类型时，为必填

        :return: The cluster_id of this UpdateAccessConfigRequestBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdateAccessConfigRequestBody.

        CCE集群ID，CCE类型时，为必填

        :param cluster_id: The cluster_id of this UpdateAccessConfigRequestBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def incremental_collect(self):
        r"""Gets the incremental_collect of this UpdateAccessConfigRequestBody.

        是否增量采集 true为是 false为否（全量采集）

        :return: The incremental_collect of this UpdateAccessConfigRequestBody.
        :rtype: bool
        """
        return self._incremental_collect

    @incremental_collect.setter
    def incremental_collect(self, incremental_collect):
        r"""Sets the incremental_collect of this UpdateAccessConfigRequestBody.

        是否增量采集 true为是 false为否（全量采集）

        :param incremental_collect: The incremental_collect of this UpdateAccessConfigRequestBody.
        :type incremental_collect: bool
        """
        self._incremental_collect = incremental_collect

    @property
    def encoding_format(self):
        r"""Gets the encoding_format of this UpdateAccessConfigRequestBody.

        编码格式，默认UTF-8

        :return: The encoding_format of this UpdateAccessConfigRequestBody.
        :rtype: str
        """
        return self._encoding_format

    @encoding_format.setter
    def encoding_format(self, encoding_format):
        r"""Sets the encoding_format of this UpdateAccessConfigRequestBody.

        编码格式，默认UTF-8

        :param encoding_format: The encoding_format of this UpdateAccessConfigRequestBody.
        :type encoding_format: str
        """
        self._encoding_format = encoding_format

    @property
    def processor_type(self):
        r"""Gets the processor_type of this UpdateAccessConfigRequestBody.

        IC结构化解析类型

        :return: The processor_type of this UpdateAccessConfigRequestBody.
        :rtype: str
        """
        return self._processor_type

    @processor_type.setter
    def processor_type(self, processor_type):
        r"""Sets the processor_type of this UpdateAccessConfigRequestBody.

        IC结构化解析类型

        :param processor_type: The processor_type of this UpdateAccessConfigRequestBody.
        :type processor_type: str
        """
        self._processor_type = processor_type

    @property
    def demo_log(self):
        r"""Gets the demo_log of this UpdateAccessConfigRequestBody.

        示例日志

        :return: The demo_log of this UpdateAccessConfigRequestBody.
        :rtype: str
        """
        return self._demo_log

    @demo_log.setter
    def demo_log(self, demo_log):
        r"""Sets the demo_log of this UpdateAccessConfigRequestBody.

        示例日志

        :param demo_log: The demo_log of this UpdateAccessConfigRequestBody.
        :type demo_log: str
        """
        self._demo_log = demo_log

    @property
    def demo_fields(self):
        r"""Gets the demo_fields of this UpdateAccessConfigRequestBody.

        示例日志解析字段

        :return: The demo_fields of this UpdateAccessConfigRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.DemoFieldAccess`]
        """
        return self._demo_fields

    @demo_fields.setter
    def demo_fields(self, demo_fields):
        r"""Sets the demo_fields of this UpdateAccessConfigRequestBody.

        示例日志解析字段

        :param demo_fields: The demo_fields of this UpdateAccessConfigRequestBody.
        :type demo_fields: list[:class:`huaweicloudsdklts.v2.DemoFieldAccess`]
        """
        self._demo_fields = demo_fields

    @property
    def processors(self):
        r"""Gets the processors of this UpdateAccessConfigRequestBody.

        IC结构化解析器

        :return: The processors of this UpdateAccessConfigRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.Processor`]
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        r"""Sets the processors of this UpdateAccessConfigRequestBody.

        IC结构化解析器

        :param processors: The processors of this UpdateAccessConfigRequestBody.
        :type processors: list[:class:`huaweicloudsdklts.v2.Processor`]
        """
        self._processors = processors

    @property
    def application_id(self):
        r"""Gets the application_id of this UpdateAccessConfigRequestBody.

        ServiceStage应用ID

        :return: The application_id of this UpdateAccessConfigRequestBody.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this UpdateAccessConfigRequestBody.

        ServiceStage应用ID

        :param application_id: The application_id of this UpdateAccessConfigRequestBody.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def environment_id(self):
        r"""Gets the environment_id of this UpdateAccessConfigRequestBody.

        ServiceStage环境ID

        :return: The environment_id of this UpdateAccessConfigRequestBody.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        r"""Sets the environment_id of this UpdateAccessConfigRequestBody.

        ServiceStage环境ID

        :param environment_id: The environment_id of this UpdateAccessConfigRequestBody.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def component_id(self):
        r"""Gets the component_id of this UpdateAccessConfigRequestBody.

        ServiceStage组件ID

        :return: The component_id of this UpdateAccessConfigRequestBody.
        :rtype: list[str]
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this UpdateAccessConfigRequestBody.

        ServiceStage组件ID

        :param component_id: The component_id of this UpdateAccessConfigRequestBody.
        :type component_id: list[str]
        """
        self._component_id = component_id

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
        if not isinstance(other, UpdateAccessConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
