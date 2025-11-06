# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogTransferDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_period': 'int',
        'obs_period_unit': 'str',
        'obs_bucket_name': 'str',
        'obs_encrypted_id': 'str',
        'obs_dir_pre_fix_name': 'str',
        'obs_prefix_name': 'str',
        'obs_time_zone': 'str',
        'obs_time_zone_id': 'str',
        'dis_id': 'str',
        'dis_name': 'str',
        'kafka_id': 'str',
        'kafka_topic': 'str',
        'obs_eps_id': 'str',
        'obs_encrypted_enable': 'bool',
        'tags': 'list[str]',
        'lts_tags': 'list[str]',
        'stream_tags': 'list[str]',
        'struct_fields': 'list[str]',
        'invalid_field_value': 'str'
    }

    attribute_map = {
        'obs_period': 'obs_period',
        'obs_period_unit': 'obs_period_unit',
        'obs_bucket_name': 'obs_bucket_name',
        'obs_encrypted_id': 'obs_encrypted_id',
        'obs_dir_pre_fix_name': 'obs_dir_pre_fix_name',
        'obs_prefix_name': 'obs_prefix_name',
        'obs_time_zone': 'obs_time_zone',
        'obs_time_zone_id': 'obs_time_zone_id',
        'dis_id': 'dis_id',
        'dis_name': 'dis_name',
        'kafka_id': 'kafka_id',
        'kafka_topic': 'kafka_topic',
        'obs_eps_id': 'obs_eps_id',
        'obs_encrypted_enable': 'obs_encrypted_enable',
        'tags': 'tags',
        'lts_tags': 'lts_tags',
        'stream_tags': 'stream_tags',
        'struct_fields': 'struct_fields',
        'invalid_field_value': 'invalid_field_value'
    }

    def __init__(self, obs_period=None, obs_period_unit=None, obs_bucket_name=None, obs_encrypted_id=None, obs_dir_pre_fix_name=None, obs_prefix_name=None, obs_time_zone=None, obs_time_zone_id=None, dis_id=None, dis_name=None, kafka_id=None, kafka_topic=None, obs_eps_id=None, obs_encrypted_enable=None, tags=None, lts_tags=None, stream_tags=None, struct_fields=None, invalid_field_value=None):
        r"""LogTransferDetail

        The model defined in huaweicloud sdk

        :param obs_period: **参数解释：**  OBS转储时间。当创建OBS转储时，必填此参数。与obs_period_unit组合，即\&quot;obs_period\&quot;+\&quot;obs_period_unit\&quot;，必须是\&quot;2min\&quot;, \&quot;5min\&quot;, \&quot;30min\&quot;, \&quot;1hour\&quot;, \&quot;3hour\&quot;, \&quot;6hour\&quot;,\&quot;12hour\&quot;。 **约束限制：**  不涉及。  **取值范围：**  1,2,3,5,6,12,30
        :type obs_period: int
        :param obs_period_unit: **参数解释：**  OBS转储单位。当创建OBS转储时，必填此参数。与obs_period组合，即\&quot;obs_period\&quot;+\&quot;obs_period_unit\&quot;，必须是\&quot;2min\&quot;, \&quot;5min\&quot;, \&quot;30min\&quot;, \&quot;1hour\&quot;, \&quot;3hour\&quot;, \&quot;6hour\&quot;,\&quot;12hour\&quot;。 **约束限制：**  不涉及。  **取值范围：**  min,hour
        :type obs_period_unit: str
        :param obs_bucket_name: **参数解释：**  OBS转储日志桶名称。当创建OBS转储时，必填此参数。 **约束限制：**  不涉及
        :type obs_bucket_name: str
        :param obs_encrypted_id: **参数解释：**  OBS转储KMS密钥ID。根据OBS转储日志桶是否加密判断，若OBS转储日志加密桶则必须填写该参数，若OBS转储日志桶则不需要此参数 **约束限制：**  不涉及
        :type obs_encrypted_id: str
        :param obs_dir_pre_fix_name: **参数解释：**  OBS转储自定义转储路径。当创建OBS转储时，根据需要选填此参数。 **约束限制：**  不涉及
        :type obs_dir_pre_fix_name: str
        :param obs_prefix_name: **参数解释：**  OBS转储日志文件前缀。当创建OBS转储时，根据需要选填此参数。 **约束限制：**  不涉及
        :type obs_prefix_name: str
        :param obs_time_zone: **参数解释：**  OBS转储时区。参数选择参考OBS转储时区表。如果选择该参数，则必须选择obs_time_zone_id。 **约束限制：**  不涉及
        :type obs_time_zone: str
        :param obs_time_zone_id: **参数解释：**  OBS转储时区ID。参数选择参考OBS转储时区表。如果选择该参数，则必须选择obs_time_zone。 **约束限制：**  不涉及
        :type obs_time_zone_id: str
        :param dis_id: **参数解释：**  DIS转储通道ID。当创建DIS转储时，必填此参数。 **约束限制：**  不涉及
        :type dis_id: str
        :param dis_name: **参数解释：**  DIS转储通道名称。当创建DIS转储时，必填此参数。 **约束限制：**  不涉及
        :type dis_name: str
        :param kafka_id: **参数解释：**  DMS转储kafka ID。当创建DMS转储时，必填此参数。创建DMS转储前，需要使用kafka ID以及kafka Topic进行实例注册。详情见接口注册DMSkafka实例 **约束限制：**  不涉及
        :type kafka_id: str
        :param kafka_topic: **参数解释：**  DMS转储kafka topic。当创建DMS转储时，必填此参数。创建DMS转储前，需要使用kafka ID以及kafka Topic进行实例注册。详情见接口注册DMSkafka实例 **约束限制：**  不涉及
        :type kafka_topic: str
        :param obs_eps_id: **参数解释：**  OBS企业项目ID。 **约束限制：**  不涉及
        :type obs_eps_id: str
        :param obs_encrypted_enable: **参数解释：**  OBS是否开启加密。 **约束限制：**  不涉及
        :type obs_encrypted_enable: bool
        :param tags: **参数解释：**  若开启tag投递，该字段必须包含主机信息：hostIP、hostId、hostName、pathFile、collectTime； 公共字段有：logStreamName、regionName、logGroupName、projectId，为可选填；开启转储标签：streamTag，可选填 **约束限制：**  不涉及
        :type tags: list[str]
        :param lts_tags: **参数解释：**  dms转储JSON格式选填，可以转储tag字段 **约束限制：**  不涉及
        :type lts_tags: list[str]
        :param stream_tags: **参数解释：**  dms转储JSON格式选填，可以转储日志流标签字段 **约束限制：**  不涉及
        :type stream_tags: list[str]
        :param struct_fields: **参数解释：**  dms转储JSON格式选填，可以转储结构化字段 **约束限制：**  不涉及
        :type struct_fields: list[str]
        :param invalid_field_value: **参数解释：**  dms转储JSON格式选填，无效字段填充 **约束限制：**  不涉及
        :type invalid_field_value: str
        """
        
        

        self._obs_period = None
        self._obs_period_unit = None
        self._obs_bucket_name = None
        self._obs_encrypted_id = None
        self._obs_dir_pre_fix_name = None
        self._obs_prefix_name = None
        self._obs_time_zone = None
        self._obs_time_zone_id = None
        self._dis_id = None
        self._dis_name = None
        self._kafka_id = None
        self._kafka_topic = None
        self._obs_eps_id = None
        self._obs_encrypted_enable = None
        self._tags = None
        self._lts_tags = None
        self._stream_tags = None
        self._struct_fields = None
        self._invalid_field_value = None
        self.discriminator = None

        self.obs_period = obs_period
        self.obs_period_unit = obs_period_unit
        self.obs_bucket_name = obs_bucket_name
        if obs_encrypted_id is not None:
            self.obs_encrypted_id = obs_encrypted_id
        if obs_dir_pre_fix_name is not None:
            self.obs_dir_pre_fix_name = obs_dir_pre_fix_name
        if obs_prefix_name is not None:
            self.obs_prefix_name = obs_prefix_name
        if obs_time_zone is not None:
            self.obs_time_zone = obs_time_zone
        if obs_time_zone_id is not None:
            self.obs_time_zone_id = obs_time_zone_id
        if dis_id is not None:
            self.dis_id = dis_id
        if dis_name is not None:
            self.dis_name = dis_name
        if kafka_id is not None:
            self.kafka_id = kafka_id
        if kafka_topic is not None:
            self.kafka_topic = kafka_topic
        if obs_eps_id is not None:
            self.obs_eps_id = obs_eps_id
        if obs_encrypted_enable is not None:
            self.obs_encrypted_enable = obs_encrypted_enable
        if tags is not None:
            self.tags = tags
        if lts_tags is not None:
            self.lts_tags = lts_tags
        if stream_tags is not None:
            self.stream_tags = stream_tags
        if struct_fields is not None:
            self.struct_fields = struct_fields
        if invalid_field_value is not None:
            self.invalid_field_value = invalid_field_value

    @property
    def obs_period(self):
        r"""Gets the obs_period of this LogTransferDetail.

        **参数解释：**  OBS转储时间。当创建OBS转储时，必填此参数。与obs_period_unit组合，即\"obs_period\"+\"obs_period_unit\"，必须是\"2min\", \"5min\", \"30min\", \"1hour\", \"3hour\", \"6hour\",\"12hour\"。 **约束限制：**  不涉及。  **取值范围：**  1,2,3,5,6,12,30

        :return: The obs_period of this LogTransferDetail.
        :rtype: int
        """
        return self._obs_period

    @obs_period.setter
    def obs_period(self, obs_period):
        r"""Sets the obs_period of this LogTransferDetail.

        **参数解释：**  OBS转储时间。当创建OBS转储时，必填此参数。与obs_period_unit组合，即\"obs_period\"+\"obs_period_unit\"，必须是\"2min\", \"5min\", \"30min\", \"1hour\", \"3hour\", \"6hour\",\"12hour\"。 **约束限制：**  不涉及。  **取值范围：**  1,2,3,5,6,12,30

        :param obs_period: The obs_period of this LogTransferDetail.
        :type obs_period: int
        """
        self._obs_period = obs_period

    @property
    def obs_period_unit(self):
        r"""Gets the obs_period_unit of this LogTransferDetail.

        **参数解释：**  OBS转储单位。当创建OBS转储时，必填此参数。与obs_period组合，即\"obs_period\"+\"obs_period_unit\"，必须是\"2min\", \"5min\", \"30min\", \"1hour\", \"3hour\", \"6hour\",\"12hour\"。 **约束限制：**  不涉及。  **取值范围：**  min,hour

        :return: The obs_period_unit of this LogTransferDetail.
        :rtype: str
        """
        return self._obs_period_unit

    @obs_period_unit.setter
    def obs_period_unit(self, obs_period_unit):
        r"""Sets the obs_period_unit of this LogTransferDetail.

        **参数解释：**  OBS转储单位。当创建OBS转储时，必填此参数。与obs_period组合，即\"obs_period\"+\"obs_period_unit\"，必须是\"2min\", \"5min\", \"30min\", \"1hour\", \"3hour\", \"6hour\",\"12hour\"。 **约束限制：**  不涉及。  **取值范围：**  min,hour

        :param obs_period_unit: The obs_period_unit of this LogTransferDetail.
        :type obs_period_unit: str
        """
        self._obs_period_unit = obs_period_unit

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this LogTransferDetail.

        **参数解释：**  OBS转储日志桶名称。当创建OBS转储时，必填此参数。 **约束限制：**  不涉及

        :return: The obs_bucket_name of this LogTransferDetail.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this LogTransferDetail.

        **参数解释：**  OBS转储日志桶名称。当创建OBS转储时，必填此参数。 **约束限制：**  不涉及

        :param obs_bucket_name: The obs_bucket_name of this LogTransferDetail.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def obs_encrypted_id(self):
        r"""Gets the obs_encrypted_id of this LogTransferDetail.

        **参数解释：**  OBS转储KMS密钥ID。根据OBS转储日志桶是否加密判断，若OBS转储日志加密桶则必须填写该参数，若OBS转储日志桶则不需要此参数 **约束限制：**  不涉及

        :return: The obs_encrypted_id of this LogTransferDetail.
        :rtype: str
        """
        return self._obs_encrypted_id

    @obs_encrypted_id.setter
    def obs_encrypted_id(self, obs_encrypted_id):
        r"""Sets the obs_encrypted_id of this LogTransferDetail.

        **参数解释：**  OBS转储KMS密钥ID。根据OBS转储日志桶是否加密判断，若OBS转储日志加密桶则必须填写该参数，若OBS转储日志桶则不需要此参数 **约束限制：**  不涉及

        :param obs_encrypted_id: The obs_encrypted_id of this LogTransferDetail.
        :type obs_encrypted_id: str
        """
        self._obs_encrypted_id = obs_encrypted_id

    @property
    def obs_dir_pre_fix_name(self):
        r"""Gets the obs_dir_pre_fix_name of this LogTransferDetail.

        **参数解释：**  OBS转储自定义转储路径。当创建OBS转储时，根据需要选填此参数。 **约束限制：**  不涉及

        :return: The obs_dir_pre_fix_name of this LogTransferDetail.
        :rtype: str
        """
        return self._obs_dir_pre_fix_name

    @obs_dir_pre_fix_name.setter
    def obs_dir_pre_fix_name(self, obs_dir_pre_fix_name):
        r"""Sets the obs_dir_pre_fix_name of this LogTransferDetail.

        **参数解释：**  OBS转储自定义转储路径。当创建OBS转储时，根据需要选填此参数。 **约束限制：**  不涉及

        :param obs_dir_pre_fix_name: The obs_dir_pre_fix_name of this LogTransferDetail.
        :type obs_dir_pre_fix_name: str
        """
        self._obs_dir_pre_fix_name = obs_dir_pre_fix_name

    @property
    def obs_prefix_name(self):
        r"""Gets the obs_prefix_name of this LogTransferDetail.

        **参数解释：**  OBS转储日志文件前缀。当创建OBS转储时，根据需要选填此参数。 **约束限制：**  不涉及

        :return: The obs_prefix_name of this LogTransferDetail.
        :rtype: str
        """
        return self._obs_prefix_name

    @obs_prefix_name.setter
    def obs_prefix_name(self, obs_prefix_name):
        r"""Sets the obs_prefix_name of this LogTransferDetail.

        **参数解释：**  OBS转储日志文件前缀。当创建OBS转储时，根据需要选填此参数。 **约束限制：**  不涉及

        :param obs_prefix_name: The obs_prefix_name of this LogTransferDetail.
        :type obs_prefix_name: str
        """
        self._obs_prefix_name = obs_prefix_name

    @property
    def obs_time_zone(self):
        r"""Gets the obs_time_zone of this LogTransferDetail.

        **参数解释：**  OBS转储时区。参数选择参考OBS转储时区表。如果选择该参数，则必须选择obs_time_zone_id。 **约束限制：**  不涉及

        :return: The obs_time_zone of this LogTransferDetail.
        :rtype: str
        """
        return self._obs_time_zone

    @obs_time_zone.setter
    def obs_time_zone(self, obs_time_zone):
        r"""Sets the obs_time_zone of this LogTransferDetail.

        **参数解释：**  OBS转储时区。参数选择参考OBS转储时区表。如果选择该参数，则必须选择obs_time_zone_id。 **约束限制：**  不涉及

        :param obs_time_zone: The obs_time_zone of this LogTransferDetail.
        :type obs_time_zone: str
        """
        self._obs_time_zone = obs_time_zone

    @property
    def obs_time_zone_id(self):
        r"""Gets the obs_time_zone_id of this LogTransferDetail.

        **参数解释：**  OBS转储时区ID。参数选择参考OBS转储时区表。如果选择该参数，则必须选择obs_time_zone。 **约束限制：**  不涉及

        :return: The obs_time_zone_id of this LogTransferDetail.
        :rtype: str
        """
        return self._obs_time_zone_id

    @obs_time_zone_id.setter
    def obs_time_zone_id(self, obs_time_zone_id):
        r"""Sets the obs_time_zone_id of this LogTransferDetail.

        **参数解释：**  OBS转储时区ID。参数选择参考OBS转储时区表。如果选择该参数，则必须选择obs_time_zone。 **约束限制：**  不涉及

        :param obs_time_zone_id: The obs_time_zone_id of this LogTransferDetail.
        :type obs_time_zone_id: str
        """
        self._obs_time_zone_id = obs_time_zone_id

    @property
    def dis_id(self):
        r"""Gets the dis_id of this LogTransferDetail.

        **参数解释：**  DIS转储通道ID。当创建DIS转储时，必填此参数。 **约束限制：**  不涉及

        :return: The dis_id of this LogTransferDetail.
        :rtype: str
        """
        return self._dis_id

    @dis_id.setter
    def dis_id(self, dis_id):
        r"""Sets the dis_id of this LogTransferDetail.

        **参数解释：**  DIS转储通道ID。当创建DIS转储时，必填此参数。 **约束限制：**  不涉及

        :param dis_id: The dis_id of this LogTransferDetail.
        :type dis_id: str
        """
        self._dis_id = dis_id

    @property
    def dis_name(self):
        r"""Gets the dis_name of this LogTransferDetail.

        **参数解释：**  DIS转储通道名称。当创建DIS转储时，必填此参数。 **约束限制：**  不涉及

        :return: The dis_name of this LogTransferDetail.
        :rtype: str
        """
        return self._dis_name

    @dis_name.setter
    def dis_name(self, dis_name):
        r"""Sets the dis_name of this LogTransferDetail.

        **参数解释：**  DIS转储通道名称。当创建DIS转储时，必填此参数。 **约束限制：**  不涉及

        :param dis_name: The dis_name of this LogTransferDetail.
        :type dis_name: str
        """
        self._dis_name = dis_name

    @property
    def kafka_id(self):
        r"""Gets the kafka_id of this LogTransferDetail.

        **参数解释：**  DMS转储kafka ID。当创建DMS转储时，必填此参数。创建DMS转储前，需要使用kafka ID以及kafka Topic进行实例注册。详情见接口注册DMSkafka实例 **约束限制：**  不涉及

        :return: The kafka_id of this LogTransferDetail.
        :rtype: str
        """
        return self._kafka_id

    @kafka_id.setter
    def kafka_id(self, kafka_id):
        r"""Sets the kafka_id of this LogTransferDetail.

        **参数解释：**  DMS转储kafka ID。当创建DMS转储时，必填此参数。创建DMS转储前，需要使用kafka ID以及kafka Topic进行实例注册。详情见接口注册DMSkafka实例 **约束限制：**  不涉及

        :param kafka_id: The kafka_id of this LogTransferDetail.
        :type kafka_id: str
        """
        self._kafka_id = kafka_id

    @property
    def kafka_topic(self):
        r"""Gets the kafka_topic of this LogTransferDetail.

        **参数解释：**  DMS转储kafka topic。当创建DMS转储时，必填此参数。创建DMS转储前，需要使用kafka ID以及kafka Topic进行实例注册。详情见接口注册DMSkafka实例 **约束限制：**  不涉及

        :return: The kafka_topic of this LogTransferDetail.
        :rtype: str
        """
        return self._kafka_topic

    @kafka_topic.setter
    def kafka_topic(self, kafka_topic):
        r"""Sets the kafka_topic of this LogTransferDetail.

        **参数解释：**  DMS转储kafka topic。当创建DMS转储时，必填此参数。创建DMS转储前，需要使用kafka ID以及kafka Topic进行实例注册。详情见接口注册DMSkafka实例 **约束限制：**  不涉及

        :param kafka_topic: The kafka_topic of this LogTransferDetail.
        :type kafka_topic: str
        """
        self._kafka_topic = kafka_topic

    @property
    def obs_eps_id(self):
        r"""Gets the obs_eps_id of this LogTransferDetail.

        **参数解释：**  OBS企业项目ID。 **约束限制：**  不涉及

        :return: The obs_eps_id of this LogTransferDetail.
        :rtype: str
        """
        return self._obs_eps_id

    @obs_eps_id.setter
    def obs_eps_id(self, obs_eps_id):
        r"""Sets the obs_eps_id of this LogTransferDetail.

        **参数解释：**  OBS企业项目ID。 **约束限制：**  不涉及

        :param obs_eps_id: The obs_eps_id of this LogTransferDetail.
        :type obs_eps_id: str
        """
        self._obs_eps_id = obs_eps_id

    @property
    def obs_encrypted_enable(self):
        r"""Gets the obs_encrypted_enable of this LogTransferDetail.

        **参数解释：**  OBS是否开启加密。 **约束限制：**  不涉及

        :return: The obs_encrypted_enable of this LogTransferDetail.
        :rtype: bool
        """
        return self._obs_encrypted_enable

    @obs_encrypted_enable.setter
    def obs_encrypted_enable(self, obs_encrypted_enable):
        r"""Sets the obs_encrypted_enable of this LogTransferDetail.

        **参数解释：**  OBS是否开启加密。 **约束限制：**  不涉及

        :param obs_encrypted_enable: The obs_encrypted_enable of this LogTransferDetail.
        :type obs_encrypted_enable: bool
        """
        self._obs_encrypted_enable = obs_encrypted_enable

    @property
    def tags(self):
        r"""Gets the tags of this LogTransferDetail.

        **参数解释：**  若开启tag投递，该字段必须包含主机信息：hostIP、hostId、hostName、pathFile、collectTime； 公共字段有：logStreamName、regionName、logGroupName、projectId，为可选填；开启转储标签：streamTag，可选填 **约束限制：**  不涉及

        :return: The tags of this LogTransferDetail.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this LogTransferDetail.

        **参数解释：**  若开启tag投递，该字段必须包含主机信息：hostIP、hostId、hostName、pathFile、collectTime； 公共字段有：logStreamName、regionName、logGroupName、projectId，为可选填；开启转储标签：streamTag，可选填 **约束限制：**  不涉及

        :param tags: The tags of this LogTransferDetail.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def lts_tags(self):
        r"""Gets the lts_tags of this LogTransferDetail.

        **参数解释：**  dms转储JSON格式选填，可以转储tag字段 **约束限制：**  不涉及

        :return: The lts_tags of this LogTransferDetail.
        :rtype: list[str]
        """
        return self._lts_tags

    @lts_tags.setter
    def lts_tags(self, lts_tags):
        r"""Sets the lts_tags of this LogTransferDetail.

        **参数解释：**  dms转储JSON格式选填，可以转储tag字段 **约束限制：**  不涉及

        :param lts_tags: The lts_tags of this LogTransferDetail.
        :type lts_tags: list[str]
        """
        self._lts_tags = lts_tags

    @property
    def stream_tags(self):
        r"""Gets the stream_tags of this LogTransferDetail.

        **参数解释：**  dms转储JSON格式选填，可以转储日志流标签字段 **约束限制：**  不涉及

        :return: The stream_tags of this LogTransferDetail.
        :rtype: list[str]
        """
        return self._stream_tags

    @stream_tags.setter
    def stream_tags(self, stream_tags):
        r"""Sets the stream_tags of this LogTransferDetail.

        **参数解释：**  dms转储JSON格式选填，可以转储日志流标签字段 **约束限制：**  不涉及

        :param stream_tags: The stream_tags of this LogTransferDetail.
        :type stream_tags: list[str]
        """
        self._stream_tags = stream_tags

    @property
    def struct_fields(self):
        r"""Gets the struct_fields of this LogTransferDetail.

        **参数解释：**  dms转储JSON格式选填，可以转储结构化字段 **约束限制：**  不涉及

        :return: The struct_fields of this LogTransferDetail.
        :rtype: list[str]
        """
        return self._struct_fields

    @struct_fields.setter
    def struct_fields(self, struct_fields):
        r"""Sets the struct_fields of this LogTransferDetail.

        **参数解释：**  dms转储JSON格式选填，可以转储结构化字段 **约束限制：**  不涉及

        :param struct_fields: The struct_fields of this LogTransferDetail.
        :type struct_fields: list[str]
        """
        self._struct_fields = struct_fields

    @property
    def invalid_field_value(self):
        r"""Gets the invalid_field_value of this LogTransferDetail.

        **参数解释：**  dms转储JSON格式选填，无效字段填充 **约束限制：**  不涉及

        :return: The invalid_field_value of this LogTransferDetail.
        :rtype: str
        """
        return self._invalid_field_value

    @invalid_field_value.setter
    def invalid_field_value(self, invalid_field_value):
        r"""Sets the invalid_field_value of this LogTransferDetail.

        **参数解释：**  dms转储JSON格式选填，无效字段填充 **约束限制：**  不涉及

        :param invalid_field_value: The invalid_field_value of this LogTransferDetail.
        :type invalid_field_value: str
        """
        self._invalid_field_value = invalid_field_value

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
        if not isinstance(other, LogTransferDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
