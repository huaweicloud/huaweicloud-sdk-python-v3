# coding: utf-8

import pprint
import re

import six





class CreateTaskReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_type': 'str',
        'src_node': 'SrcNodeReq',
        'dst_node': 'DstNodeReq',
        'enable_kms': 'bool',
        'description': 'str',
        'migrate_since': 'int',
        'bandwidth_policy': 'list[BandwidthPolicyDto]',
        'source_cdn': 'SourceCdnReq',
        'smn_config': 'SmnConfig',
        'enable_restore': 'bool',
        'enable_failed_object_recording': 'bool'
    }

    attribute_map = {
        'task_type': 'task_type',
        'src_node': 'src_node',
        'dst_node': 'dst_node',
        'enable_kms': 'enable_kms',
        'description': 'description',
        'migrate_since': 'migrate_since',
        'bandwidth_policy': 'bandwidth_policy',
        'source_cdn': 'source_cdn',
        'smn_config': 'smn_config',
        'enable_restore': 'enable_restore',
        'enable_failed_object_recording': 'enable_failed_object_recording'
    }

    def __init__(self, task_type=None, src_node=None, dst_node=None, enable_kms=None, description=None, migrate_since=None, bandwidth_policy=None, source_cdn=None, smn_config=None, enable_restore=None, enable_failed_object_recording=None):
        """CreateTaskReq - a model defined in huaweicloud sdk"""
        
        

        self._task_type = None
        self._src_node = None
        self._dst_node = None
        self._enable_kms = None
        self._description = None
        self._migrate_since = None
        self._bandwidth_policy = None
        self._source_cdn = None
        self._smn_config = None
        self._enable_restore = None
        self._enable_failed_object_recording = None
        self.discriminator = None

        if task_type is not None:
            self.task_type = task_type
        self.src_node = src_node
        self.dst_node = dst_node
        if enable_kms is not None:
            self.enable_kms = enable_kms
        if description is not None:
            self.description = description
        if migrate_since is not None:
            self.migrate_since = migrate_since
        if bandwidth_policy is not None:
            self.bandwidth_policy = bandwidth_policy
        if source_cdn is not None:
            self.source_cdn = source_cdn
        if smn_config is not None:
            self.smn_config = smn_config
        if enable_restore is not None:
            self.enable_restore = enable_restore
        if enable_failed_object_recording is not None:
            self.enable_failed_object_recording = enable_failed_object_recording

    @property
    def task_type(self):
        """Gets the task_type of this CreateTaskReq.

        任务类型，默认为object。  list：对象列表迁移 url_list：URL列表迁移 object：文件/文件夹迁移，默认 prefix：对象前缀迁移

        :return: The task_type of this CreateTaskReq.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this CreateTaskReq.

        任务类型，默认为object。  list：对象列表迁移 url_list：URL列表迁移 object：文件/文件夹迁移，默认 prefix：对象前缀迁移

        :param task_type: The task_type of this CreateTaskReq.
        :type: str
        """
        self._task_type = task_type

    @property
    def src_node(self):
        """Gets the src_node of this CreateTaskReq.


        :return: The src_node of this CreateTaskReq.
        :rtype: SrcNodeReq
        """
        return self._src_node

    @src_node.setter
    def src_node(self, src_node):
        """Sets the src_node of this CreateTaskReq.


        :param src_node: The src_node of this CreateTaskReq.
        :type: SrcNodeReq
        """
        self._src_node = src_node

    @property
    def dst_node(self):
        """Gets the dst_node of this CreateTaskReq.


        :return: The dst_node of this CreateTaskReq.
        :rtype: DstNodeReq
        """
        return self._dst_node

    @dst_node.setter
    def dst_node(self, dst_node):
        """Sets the dst_node of this CreateTaskReq.


        :param dst_node: The dst_node of this CreateTaskReq.
        :type: DstNodeReq
        """
        self._dst_node = dst_node

    @property
    def enable_kms(self):
        """Gets the enable_kms of this CreateTaskReq.

        是否开启KMS加密，默认不开启。

        :return: The enable_kms of this CreateTaskReq.
        :rtype: bool
        """
        return self._enable_kms

    @enable_kms.setter
    def enable_kms(self, enable_kms):
        """Sets the enable_kms of this CreateTaskReq.

        是否开启KMS加密，默认不开启。

        :param enable_kms: The enable_kms of this CreateTaskReq.
        :type: bool
        """
        self._enable_kms = enable_kms

    @property
    def description(self):
        """Gets the description of this CreateTaskReq.

        任务描述，不能超过255个字符，且不能包含^<>&\"'等特殊字符。

        :return: The description of this CreateTaskReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTaskReq.

        任务描述，不能超过255个字符，且不能包含^<>&\"'等特殊字符。

        :param description: The description of this CreateTaskReq.
        :type: str
        """
        self._description = description

    @property
    def migrate_since(self):
        """Gets the migrate_since of this CreateTaskReq.

        以时间戳方式表示的迁移指定时间（单位：秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认不设置迁移指定时间。

        :return: The migrate_since of this CreateTaskReq.
        :rtype: int
        """
        return self._migrate_since

    @migrate_since.setter
    def migrate_since(self, migrate_since):
        """Sets the migrate_since of this CreateTaskReq.

        以时间戳方式表示的迁移指定时间（单位：秒），表示仅迁移在指定时间之后修改的源端待迁移对象。默认不设置迁移指定时间。

        :param migrate_since: The migrate_since of this CreateTaskReq.
        :type: int
        """
        self._migrate_since = migrate_since

    @property
    def bandwidth_policy(self):
        """Gets the bandwidth_policy of this CreateTaskReq.

        配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。

        :return: The bandwidth_policy of this CreateTaskReq.
        :rtype: list[BandwidthPolicyDto]
        """
        return self._bandwidth_policy

    @bandwidth_policy.setter
    def bandwidth_policy(self, bandwidth_policy):
        """Sets the bandwidth_policy of this CreateTaskReq.

        配置流量控制策略。数组中一个元素对应一个时段的最大带宽，最多允许5个时段，且时段不能重叠。

        :param bandwidth_policy: The bandwidth_policy of this CreateTaskReq.
        :type: list[BandwidthPolicyDto]
        """
        self._bandwidth_policy = bandwidth_policy

    @property
    def source_cdn(self):
        """Gets the source_cdn of this CreateTaskReq.


        :return: The source_cdn of this CreateTaskReq.
        :rtype: SourceCdnReq
        """
        return self._source_cdn

    @source_cdn.setter
    def source_cdn(self, source_cdn):
        """Sets the source_cdn of this CreateTaskReq.


        :param source_cdn: The source_cdn of this CreateTaskReq.
        :type: SourceCdnReq
        """
        self._source_cdn = source_cdn

    @property
    def smn_config(self):
        """Gets the smn_config of this CreateTaskReq.


        :return: The smn_config of this CreateTaskReq.
        :rtype: SmnConfig
        """
        return self._smn_config

    @smn_config.setter
    def smn_config(self, smn_config):
        """Sets the smn_config of this CreateTaskReq.


        :param smn_config: The smn_config of this CreateTaskReq.
        :type: SmnConfig
        """
        self._smn_config = smn_config

    @property
    def enable_restore(self):
        """Gets the enable_restore of this CreateTaskReq.

        是否自动解冻归档数据，默认否。  开启后，如果遇到归档类型数据，会自动解冻再进行迁移。

        :return: The enable_restore of this CreateTaskReq.
        :rtype: bool
        """
        return self._enable_restore

    @enable_restore.setter
    def enable_restore(self, enable_restore):
        """Sets the enable_restore of this CreateTaskReq.

        是否自动解冻归档数据，默认否。  开启后，如果遇到归档类型数据，会自动解冻再进行迁移。

        :param enable_restore: The enable_restore of this CreateTaskReq.
        :type: bool
        """
        self._enable_restore = enable_restore

    @property
    def enable_failed_object_recording(self):
        """Gets the enable_failed_object_recording of this CreateTaskReq.

        是否记录失败对象，默认开启。  开启后，如果有迁移失败对象，会在目的端存储失败对象信息。

        :return: The enable_failed_object_recording of this CreateTaskReq.
        :rtype: bool
        """
        return self._enable_failed_object_recording

    @enable_failed_object_recording.setter
    def enable_failed_object_recording(self, enable_failed_object_recording):
        """Sets the enable_failed_object_recording of this CreateTaskReq.

        是否记录失败对象，默认开启。  开启后，如果有迁移失败对象，会在目的端存储失败对象信息。

        :param enable_failed_object_recording: The enable_failed_object_recording of this CreateTaskReq.
        :type: bool
        """
        self._enable_failed_object_recording = enable_failed_object_recording

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
