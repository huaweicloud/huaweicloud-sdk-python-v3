# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateResultsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_name': 'str',
        'original_shard_num': 'int',
        'after_shard_num': 'int',
        'original_dn_info_list': 'list[MigrateDnInfoOpenResponse]',
        'after_dn_info_list': 'list[MigrateDnInfoOpenResponse]',
        'switch_route_is_manual': 'bool',
        'auto_switch_begin_time': 'str',
        'auto_switch_end_time': 'str',
        'node_id_for_migrate': 'str',
        'is_exclusive': 'bool'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'original_shard_num': 'original_shard_num',
        'after_shard_num': 'after_shard_num',
        'original_dn_info_list': 'original_dn_info_list',
        'after_dn_info_list': 'after_dn_info_list',
        'switch_route_is_manual': 'switch_route_is_manual',
        'auto_switch_begin_time': 'auto_switch_begin_time',
        'auto_switch_end_time': 'auto_switch_end_time',
        'node_id_for_migrate': 'node_id_for_migrate',
        'is_exclusive': 'is_exclusive'
    }

    def __init__(self, instance_name=None, original_shard_num=None, after_shard_num=None, original_dn_info_list=None, after_dn_info_list=None, switch_route_is_manual=None, auto_switch_begin_time=None, auto_switch_end_time=None, node_id_for_migrate=None, is_exclusive=None):
        r"""MigrateResultsResponse

        The model defined in huaweicloud sdk

        :param instance_name: 实例名称。
        :type instance_name: str
        :param original_shard_num: 原始分片数。
        :type original_shard_num: int
        :param after_shard_num: 现分片数。
        :type after_shard_num: int
        :param original_dn_info_list: 分片变更前关联的后端DN信息。
        :type original_dn_info_list: list[:class:`huaweicloudsdkddm.v1.MigrateDnInfoOpenResponse`]
        :param after_dn_info_list: 分片变更后关联的后端DN信息。
        :type after_dn_info_list: list[:class:`huaweicloudsdkddm.v1.MigrateDnInfoOpenResponse`]
        :param switch_route_is_manual: 是否手动切换路由。
        :type switch_route_is_manual: bool
        :param auto_switch_begin_time: 自动切换路由开始时间。
        :type auto_switch_begin_time: str
        :param auto_switch_end_time: 自动切换路由结束时间。
        :type auto_switch_end_time: str
        :param node_id_for_migrate: 分片变更的节点。
        :type node_id_for_migrate: str
        :param is_exclusive: 是否独占式。
        :type is_exclusive: bool
        """
        
        super().__init__()

        self._instance_name = None
        self._original_shard_num = None
        self._after_shard_num = None
        self._original_dn_info_list = None
        self._after_dn_info_list = None
        self._switch_route_is_manual = None
        self._auto_switch_begin_time = None
        self._auto_switch_end_time = None
        self._node_id_for_migrate = None
        self._is_exclusive = None
        self.discriminator = None

        if instance_name is not None:
            self.instance_name = instance_name
        if original_shard_num is not None:
            self.original_shard_num = original_shard_num
        if after_shard_num is not None:
            self.after_shard_num = after_shard_num
        if original_dn_info_list is not None:
            self.original_dn_info_list = original_dn_info_list
        if after_dn_info_list is not None:
            self.after_dn_info_list = after_dn_info_list
        if switch_route_is_manual is not None:
            self.switch_route_is_manual = switch_route_is_manual
        if auto_switch_begin_time is not None:
            self.auto_switch_begin_time = auto_switch_begin_time
        if auto_switch_end_time is not None:
            self.auto_switch_end_time = auto_switch_end_time
        if node_id_for_migrate is not None:
            self.node_id_for_migrate = node_id_for_migrate
        if is_exclusive is not None:
            self.is_exclusive = is_exclusive

    @property
    def instance_name(self):
        r"""Gets the instance_name of this MigrateResultsResponse.

        实例名称。

        :return: The instance_name of this MigrateResultsResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this MigrateResultsResponse.

        实例名称。

        :param instance_name: The instance_name of this MigrateResultsResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def original_shard_num(self):
        r"""Gets the original_shard_num of this MigrateResultsResponse.

        原始分片数。

        :return: The original_shard_num of this MigrateResultsResponse.
        :rtype: int
        """
        return self._original_shard_num

    @original_shard_num.setter
    def original_shard_num(self, original_shard_num):
        r"""Sets the original_shard_num of this MigrateResultsResponse.

        原始分片数。

        :param original_shard_num: The original_shard_num of this MigrateResultsResponse.
        :type original_shard_num: int
        """
        self._original_shard_num = original_shard_num

    @property
    def after_shard_num(self):
        r"""Gets the after_shard_num of this MigrateResultsResponse.

        现分片数。

        :return: The after_shard_num of this MigrateResultsResponse.
        :rtype: int
        """
        return self._after_shard_num

    @after_shard_num.setter
    def after_shard_num(self, after_shard_num):
        r"""Sets the after_shard_num of this MigrateResultsResponse.

        现分片数。

        :param after_shard_num: The after_shard_num of this MigrateResultsResponse.
        :type after_shard_num: int
        """
        self._after_shard_num = after_shard_num

    @property
    def original_dn_info_list(self):
        r"""Gets the original_dn_info_list of this MigrateResultsResponse.

        分片变更前关联的后端DN信息。

        :return: The original_dn_info_list of this MigrateResultsResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.MigrateDnInfoOpenResponse`]
        """
        return self._original_dn_info_list

    @original_dn_info_list.setter
    def original_dn_info_list(self, original_dn_info_list):
        r"""Sets the original_dn_info_list of this MigrateResultsResponse.

        分片变更前关联的后端DN信息。

        :param original_dn_info_list: The original_dn_info_list of this MigrateResultsResponse.
        :type original_dn_info_list: list[:class:`huaweicloudsdkddm.v1.MigrateDnInfoOpenResponse`]
        """
        self._original_dn_info_list = original_dn_info_list

    @property
    def after_dn_info_list(self):
        r"""Gets the after_dn_info_list of this MigrateResultsResponse.

        分片变更后关联的后端DN信息。

        :return: The after_dn_info_list of this MigrateResultsResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.MigrateDnInfoOpenResponse`]
        """
        return self._after_dn_info_list

    @after_dn_info_list.setter
    def after_dn_info_list(self, after_dn_info_list):
        r"""Sets the after_dn_info_list of this MigrateResultsResponse.

        分片变更后关联的后端DN信息。

        :param after_dn_info_list: The after_dn_info_list of this MigrateResultsResponse.
        :type after_dn_info_list: list[:class:`huaweicloudsdkddm.v1.MigrateDnInfoOpenResponse`]
        """
        self._after_dn_info_list = after_dn_info_list

    @property
    def switch_route_is_manual(self):
        r"""Gets the switch_route_is_manual of this MigrateResultsResponse.

        是否手动切换路由。

        :return: The switch_route_is_manual of this MigrateResultsResponse.
        :rtype: bool
        """
        return self._switch_route_is_manual

    @switch_route_is_manual.setter
    def switch_route_is_manual(self, switch_route_is_manual):
        r"""Sets the switch_route_is_manual of this MigrateResultsResponse.

        是否手动切换路由。

        :param switch_route_is_manual: The switch_route_is_manual of this MigrateResultsResponse.
        :type switch_route_is_manual: bool
        """
        self._switch_route_is_manual = switch_route_is_manual

    @property
    def auto_switch_begin_time(self):
        r"""Gets the auto_switch_begin_time of this MigrateResultsResponse.

        自动切换路由开始时间。

        :return: The auto_switch_begin_time of this MigrateResultsResponse.
        :rtype: str
        """
        return self._auto_switch_begin_time

    @auto_switch_begin_time.setter
    def auto_switch_begin_time(self, auto_switch_begin_time):
        r"""Sets the auto_switch_begin_time of this MigrateResultsResponse.

        自动切换路由开始时间。

        :param auto_switch_begin_time: The auto_switch_begin_time of this MigrateResultsResponse.
        :type auto_switch_begin_time: str
        """
        self._auto_switch_begin_time = auto_switch_begin_time

    @property
    def auto_switch_end_time(self):
        r"""Gets the auto_switch_end_time of this MigrateResultsResponse.

        自动切换路由结束时间。

        :return: The auto_switch_end_time of this MigrateResultsResponse.
        :rtype: str
        """
        return self._auto_switch_end_time

    @auto_switch_end_time.setter
    def auto_switch_end_time(self, auto_switch_end_time):
        r"""Sets the auto_switch_end_time of this MigrateResultsResponse.

        自动切换路由结束时间。

        :param auto_switch_end_time: The auto_switch_end_time of this MigrateResultsResponse.
        :type auto_switch_end_time: str
        """
        self._auto_switch_end_time = auto_switch_end_time

    @property
    def node_id_for_migrate(self):
        r"""Gets the node_id_for_migrate of this MigrateResultsResponse.

        分片变更的节点。

        :return: The node_id_for_migrate of this MigrateResultsResponse.
        :rtype: str
        """
        return self._node_id_for_migrate

    @node_id_for_migrate.setter
    def node_id_for_migrate(self, node_id_for_migrate):
        r"""Sets the node_id_for_migrate of this MigrateResultsResponse.

        分片变更的节点。

        :param node_id_for_migrate: The node_id_for_migrate of this MigrateResultsResponse.
        :type node_id_for_migrate: str
        """
        self._node_id_for_migrate = node_id_for_migrate

    @property
    def is_exclusive(self):
        r"""Gets the is_exclusive of this MigrateResultsResponse.

        是否独占式。

        :return: The is_exclusive of this MigrateResultsResponse.
        :rtype: bool
        """
        return self._is_exclusive

    @is_exclusive.setter
    def is_exclusive(self, is_exclusive):
        r"""Sets the is_exclusive of this MigrateResultsResponse.

        是否独占式。

        :param is_exclusive: The is_exclusive of this MigrateResultsResponse.
        :type is_exclusive: bool
        """
        self._is_exclusive = is_exclusive

    def to_dict(self):
        import warnings
        warnings.warn("MigrateResultsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, MigrateResultsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
