# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferDetail:

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
        'obs_encrypted_id': 'str',
        'obs_prefix_name': 'str',
        'obs_period_unit': 'str',
        'obs_transfer_path': 'str',
        'obs_eps_id': 'str',
        'obs_bucket_name': 'str',
        'obs_encrypted_enable': 'bool',
        'obs_dir_pre_fix_name': 'str',
        'dis_id': 'str',
        'dis_name': 'str',
        'kafka_id': 'str',
        'kafka_topic': 'str',
        'obs_time_zone': 'str',
        'obs_time_zone_id': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'obs_period': 'obs_period',
        'obs_encrypted_id': 'obs_encrypted_id',
        'obs_prefix_name': 'obs_prefix_name',
        'obs_period_unit': 'obs_period_unit',
        'obs_transfer_path': 'obs_transfer_path',
        'obs_eps_id': 'obs_eps_id',
        'obs_bucket_name': 'obs_bucket_name',
        'obs_encrypted_enable': 'obs_encrypted_enable',
        'obs_dir_pre_fix_name': 'obs_dir_pre_fix_name',
        'dis_id': 'dis_id',
        'dis_name': 'dis_name',
        'kafka_id': 'kafka_id',
        'kafka_topic': 'kafka_topic',
        'obs_time_zone': 'obs_time_zone',
        'obs_time_zone_id': 'obs_time_zone_id',
        'tags': 'tags'
    }

    def __init__(self, obs_period=None, obs_encrypted_id=None, obs_prefix_name=None, obs_period_unit=None, obs_transfer_path=None, obs_eps_id=None, obs_bucket_name=None, obs_encrypted_enable=None, obs_dir_pre_fix_name=None, dis_id=None, dis_name=None, kafka_id=None, kafka_topic=None, obs_time_zone=None, obs_time_zone_id=None, tags=None):
        """TransferDetail

        The model defined in huaweicloud sdk

        :param obs_period: OBS转储时间
        :type obs_period: int
        :param obs_encrypted_id: OBS转储KMS秘钥ID。若OBS转储未加密则不返回此字段
        :type obs_encrypted_id: str
        :param obs_prefix_name: OBS转储日志文件前缀
        :type obs_prefix_name: str
        :param obs_period_unit: OBS转储单位
        :type obs_period_unit: str
        :param obs_transfer_path: OBS转储路径，指OBS日志桶中的路径
        :type obs_transfer_path: str
        :param obs_eps_id: OBS企业项目ID
        :type obs_eps_id: str
        :param obs_bucket_name: OBS日志桶名称
        :type obs_bucket_name: str
        :param obs_encrypted_enable: OBS是否开启加密。
        :type obs_encrypted_enable: bool
        :param obs_dir_pre_fix_name: OBS转储自定义转储路径
        :type obs_dir_pre_fix_name: str
        :param dis_id: DIS转储通道ID
        :type dis_id: str
        :param dis_name: DIS转储通道名称
        :type dis_name: str
        :param kafka_id: DMS转储kafka ID
        :type kafka_id: str
        :param kafka_topic: DMS转储kafka topic
        :type kafka_topic: str
        :param obs_time_zone: OBS转储时区。如果选择该参数，则必须选择obs_time_zone_id。
        :type obs_time_zone: str
        :param obs_time_zone_id: OBS转储时区ID。参数选择参考OBS转储时区表。如果选择该参数，则必须选择obs_time_zone。
        :type obs_time_zone_id: str
        :param tags: 若开启tag投递，该字段必须包含主机信息：hostIP、hostId、hostName、pathFile、collectTime；  公共字段有：logStreamName、regionName、logGroupName、projectId，为可选填；  开启转储标签：streamTag，可选填
        :type tags: list[str]
        """
        
        

        self._obs_period = None
        self._obs_encrypted_id = None
        self._obs_prefix_name = None
        self._obs_period_unit = None
        self._obs_transfer_path = None
        self._obs_eps_id = None
        self._obs_bucket_name = None
        self._obs_encrypted_enable = None
        self._obs_dir_pre_fix_name = None
        self._dis_id = None
        self._dis_name = None
        self._kafka_id = None
        self._kafka_topic = None
        self._obs_time_zone = None
        self._obs_time_zone_id = None
        self._tags = None
        self.discriminator = None

        self.obs_period = obs_period
        if obs_encrypted_id is not None:
            self.obs_encrypted_id = obs_encrypted_id
        if obs_prefix_name is not None:
            self.obs_prefix_name = obs_prefix_name
        self.obs_period_unit = obs_period_unit
        if obs_transfer_path is not None:
            self.obs_transfer_path = obs_transfer_path
        if obs_eps_id is not None:
            self.obs_eps_id = obs_eps_id
        self.obs_bucket_name = obs_bucket_name
        if obs_encrypted_enable is not None:
            self.obs_encrypted_enable = obs_encrypted_enable
        if obs_dir_pre_fix_name is not None:
            self.obs_dir_pre_fix_name = obs_dir_pre_fix_name
        if dis_id is not None:
            self.dis_id = dis_id
        if dis_name is not None:
            self.dis_name = dis_name
        if kafka_id is not None:
            self.kafka_id = kafka_id
        if kafka_topic is not None:
            self.kafka_topic = kafka_topic
        if obs_time_zone is not None:
            self.obs_time_zone = obs_time_zone
        if obs_time_zone_id is not None:
            self.obs_time_zone_id = obs_time_zone_id
        if tags is not None:
            self.tags = tags

    @property
    def obs_period(self):
        """Gets the obs_period of this TransferDetail.

        OBS转储时间

        :return: The obs_period of this TransferDetail.
        :rtype: int
        """
        return self._obs_period

    @obs_period.setter
    def obs_period(self, obs_period):
        """Sets the obs_period of this TransferDetail.

        OBS转储时间

        :param obs_period: The obs_period of this TransferDetail.
        :type obs_period: int
        """
        self._obs_period = obs_period

    @property
    def obs_encrypted_id(self):
        """Gets the obs_encrypted_id of this TransferDetail.

        OBS转储KMS秘钥ID。若OBS转储未加密则不返回此字段

        :return: The obs_encrypted_id of this TransferDetail.
        :rtype: str
        """
        return self._obs_encrypted_id

    @obs_encrypted_id.setter
    def obs_encrypted_id(self, obs_encrypted_id):
        """Sets the obs_encrypted_id of this TransferDetail.

        OBS转储KMS秘钥ID。若OBS转储未加密则不返回此字段

        :param obs_encrypted_id: The obs_encrypted_id of this TransferDetail.
        :type obs_encrypted_id: str
        """
        self._obs_encrypted_id = obs_encrypted_id

    @property
    def obs_prefix_name(self):
        """Gets the obs_prefix_name of this TransferDetail.

        OBS转储日志文件前缀

        :return: The obs_prefix_name of this TransferDetail.
        :rtype: str
        """
        return self._obs_prefix_name

    @obs_prefix_name.setter
    def obs_prefix_name(self, obs_prefix_name):
        """Sets the obs_prefix_name of this TransferDetail.

        OBS转储日志文件前缀

        :param obs_prefix_name: The obs_prefix_name of this TransferDetail.
        :type obs_prefix_name: str
        """
        self._obs_prefix_name = obs_prefix_name

    @property
    def obs_period_unit(self):
        """Gets the obs_period_unit of this TransferDetail.

        OBS转储单位

        :return: The obs_period_unit of this TransferDetail.
        :rtype: str
        """
        return self._obs_period_unit

    @obs_period_unit.setter
    def obs_period_unit(self, obs_period_unit):
        """Sets the obs_period_unit of this TransferDetail.

        OBS转储单位

        :param obs_period_unit: The obs_period_unit of this TransferDetail.
        :type obs_period_unit: str
        """
        self._obs_period_unit = obs_period_unit

    @property
    def obs_transfer_path(self):
        """Gets the obs_transfer_path of this TransferDetail.

        OBS转储路径，指OBS日志桶中的路径

        :return: The obs_transfer_path of this TransferDetail.
        :rtype: str
        """
        return self._obs_transfer_path

    @obs_transfer_path.setter
    def obs_transfer_path(self, obs_transfer_path):
        """Sets the obs_transfer_path of this TransferDetail.

        OBS转储路径，指OBS日志桶中的路径

        :param obs_transfer_path: The obs_transfer_path of this TransferDetail.
        :type obs_transfer_path: str
        """
        self._obs_transfer_path = obs_transfer_path

    @property
    def obs_eps_id(self):
        """Gets the obs_eps_id of this TransferDetail.

        OBS企业项目ID

        :return: The obs_eps_id of this TransferDetail.
        :rtype: str
        """
        return self._obs_eps_id

    @obs_eps_id.setter
    def obs_eps_id(self, obs_eps_id):
        """Sets the obs_eps_id of this TransferDetail.

        OBS企业项目ID

        :param obs_eps_id: The obs_eps_id of this TransferDetail.
        :type obs_eps_id: str
        """
        self._obs_eps_id = obs_eps_id

    @property
    def obs_bucket_name(self):
        """Gets the obs_bucket_name of this TransferDetail.

        OBS日志桶名称

        :return: The obs_bucket_name of this TransferDetail.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        """Sets the obs_bucket_name of this TransferDetail.

        OBS日志桶名称

        :param obs_bucket_name: The obs_bucket_name of this TransferDetail.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def obs_encrypted_enable(self):
        """Gets the obs_encrypted_enable of this TransferDetail.

        OBS是否开启加密。

        :return: The obs_encrypted_enable of this TransferDetail.
        :rtype: bool
        """
        return self._obs_encrypted_enable

    @obs_encrypted_enable.setter
    def obs_encrypted_enable(self, obs_encrypted_enable):
        """Sets the obs_encrypted_enable of this TransferDetail.

        OBS是否开启加密。

        :param obs_encrypted_enable: The obs_encrypted_enable of this TransferDetail.
        :type obs_encrypted_enable: bool
        """
        self._obs_encrypted_enable = obs_encrypted_enable

    @property
    def obs_dir_pre_fix_name(self):
        """Gets the obs_dir_pre_fix_name of this TransferDetail.

        OBS转储自定义转储路径

        :return: The obs_dir_pre_fix_name of this TransferDetail.
        :rtype: str
        """
        return self._obs_dir_pre_fix_name

    @obs_dir_pre_fix_name.setter
    def obs_dir_pre_fix_name(self, obs_dir_pre_fix_name):
        """Sets the obs_dir_pre_fix_name of this TransferDetail.

        OBS转储自定义转储路径

        :param obs_dir_pre_fix_name: The obs_dir_pre_fix_name of this TransferDetail.
        :type obs_dir_pre_fix_name: str
        """
        self._obs_dir_pre_fix_name = obs_dir_pre_fix_name

    @property
    def dis_id(self):
        """Gets the dis_id of this TransferDetail.

        DIS转储通道ID

        :return: The dis_id of this TransferDetail.
        :rtype: str
        """
        return self._dis_id

    @dis_id.setter
    def dis_id(self, dis_id):
        """Sets the dis_id of this TransferDetail.

        DIS转储通道ID

        :param dis_id: The dis_id of this TransferDetail.
        :type dis_id: str
        """
        self._dis_id = dis_id

    @property
    def dis_name(self):
        """Gets the dis_name of this TransferDetail.

        DIS转储通道名称

        :return: The dis_name of this TransferDetail.
        :rtype: str
        """
        return self._dis_name

    @dis_name.setter
    def dis_name(self, dis_name):
        """Sets the dis_name of this TransferDetail.

        DIS转储通道名称

        :param dis_name: The dis_name of this TransferDetail.
        :type dis_name: str
        """
        self._dis_name = dis_name

    @property
    def kafka_id(self):
        """Gets the kafka_id of this TransferDetail.

        DMS转储kafka ID

        :return: The kafka_id of this TransferDetail.
        :rtype: str
        """
        return self._kafka_id

    @kafka_id.setter
    def kafka_id(self, kafka_id):
        """Sets the kafka_id of this TransferDetail.

        DMS转储kafka ID

        :param kafka_id: The kafka_id of this TransferDetail.
        :type kafka_id: str
        """
        self._kafka_id = kafka_id

    @property
    def kafka_topic(self):
        """Gets the kafka_topic of this TransferDetail.

        DMS转储kafka topic

        :return: The kafka_topic of this TransferDetail.
        :rtype: str
        """
        return self._kafka_topic

    @kafka_topic.setter
    def kafka_topic(self, kafka_topic):
        """Sets the kafka_topic of this TransferDetail.

        DMS转储kafka topic

        :param kafka_topic: The kafka_topic of this TransferDetail.
        :type kafka_topic: str
        """
        self._kafka_topic = kafka_topic

    @property
    def obs_time_zone(self):
        """Gets the obs_time_zone of this TransferDetail.

        OBS转储时区。如果选择该参数，则必须选择obs_time_zone_id。

        :return: The obs_time_zone of this TransferDetail.
        :rtype: str
        """
        return self._obs_time_zone

    @obs_time_zone.setter
    def obs_time_zone(self, obs_time_zone):
        """Sets the obs_time_zone of this TransferDetail.

        OBS转储时区。如果选择该参数，则必须选择obs_time_zone_id。

        :param obs_time_zone: The obs_time_zone of this TransferDetail.
        :type obs_time_zone: str
        """
        self._obs_time_zone = obs_time_zone

    @property
    def obs_time_zone_id(self):
        """Gets the obs_time_zone_id of this TransferDetail.

        OBS转储时区ID。参数选择参考OBS转储时区表。如果选择该参数，则必须选择obs_time_zone。

        :return: The obs_time_zone_id of this TransferDetail.
        :rtype: str
        """
        return self._obs_time_zone_id

    @obs_time_zone_id.setter
    def obs_time_zone_id(self, obs_time_zone_id):
        """Sets the obs_time_zone_id of this TransferDetail.

        OBS转储时区ID。参数选择参考OBS转储时区表。如果选择该参数，则必须选择obs_time_zone。

        :param obs_time_zone_id: The obs_time_zone_id of this TransferDetail.
        :type obs_time_zone_id: str
        """
        self._obs_time_zone_id = obs_time_zone_id

    @property
    def tags(self):
        """Gets the tags of this TransferDetail.

        若开启tag投递，该字段必须包含主机信息：hostIP、hostId、hostName、pathFile、collectTime；  公共字段有：logStreamName、regionName、logGroupName、projectId，为可选填；  开启转储标签：streamTag，可选填

        :return: The tags of this TransferDetail.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TransferDetail.

        若开启tag投递，该字段必须包含主机信息：hostIP、hostId、hostName、pathFile、collectTime；  公共字段有：logStreamName、regionName、logGroupName、projectId，为可选填；  开启转储标签：streamTag，可选填

        :param tags: The tags of this TransferDetail.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, TransferDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
