# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'instance_group_name': 'str',
        'running_status': 'str',
        'ha_status': 'str',
        'config_status': 'str',
        'role_name': 'str',
        'role_short_name': 'str',
        'role_type': 'str',
        'service_name': 'str',
        'pair_name': 'str',
        'relation_pairs': 'str',
        'support_decom': 'str',
        'support_reinstall': 'str',
        'support_collect_stack_info': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'instance_group_name': 'instance_group_name',
        'running_status': 'running_status',
        'ha_status': 'ha_status',
        'config_status': 'config_status',
        'role_name': 'role_name',
        'role_short_name': 'role_short_name',
        'role_type': 'role_type',
        'service_name': 'service_name',
        'pair_name': 'pair_name',
        'relation_pairs': 'relation_pairs',
        'support_decom': 'support_decom',
        'support_reinstall': 'support_reinstall',
        'support_collect_stack_info': 'support_collect_stack_info'
    }

    def __init__(self, id=None, name=None, instance_group_name=None, running_status=None, ha_status=None, config_status=None, role_name=None, role_short_name=None, role_type=None, service_name=None, pair_name=None, relation_pairs=None, support_decom=None, support_reinstall=None, support_collect_stack_info=None):
        r"""ComponentInfo

        The model defined in huaweicloud sdk

        :param id: 组件ID。
        :type id: str
        :param name: 组件名。
        :type name: str
        :param instance_group_name: 组件所在组名称。
        :type instance_group_name: str
        :param running_status: 运行状态。
        :type running_status: str
        :param ha_status: HA状态。
        :type ha_status: str
        :param config_status: 配置状态。
        :type config_status: str
        :param role_name: 角色。
        :type role_name: str
        :param role_short_name: 角色缩写。
        :type role_short_name: str
        :param role_type: 角色类型。
        :type role_type: str
        :param service_name: 服务名。
        :type service_name: str
        :param pair_name: 对名。
        :type pair_name: str
        :param relation_pairs: 关联对。
        :type relation_pairs: str
        :param support_decom: 是否支持Decom。
        :type support_decom: str
        :param support_reinstall: 是否支持重装。
        :type support_reinstall: str
        :param support_collect_stack_info: 是否支持收集堆栈信息。
        :type support_collect_stack_info: str
        """
        
        

        self._id = None
        self._name = None
        self._instance_group_name = None
        self._running_status = None
        self._ha_status = None
        self._config_status = None
        self._role_name = None
        self._role_short_name = None
        self._role_type = None
        self._service_name = None
        self._pair_name = None
        self._relation_pairs = None
        self._support_decom = None
        self._support_reinstall = None
        self._support_collect_stack_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if instance_group_name is not None:
            self.instance_group_name = instance_group_name
        if running_status is not None:
            self.running_status = running_status
        if ha_status is not None:
            self.ha_status = ha_status
        if config_status is not None:
            self.config_status = config_status
        if role_name is not None:
            self.role_name = role_name
        if role_short_name is not None:
            self.role_short_name = role_short_name
        if role_type is not None:
            self.role_type = role_type
        if service_name is not None:
            self.service_name = service_name
        if pair_name is not None:
            self.pair_name = pair_name
        if relation_pairs is not None:
            self.relation_pairs = relation_pairs
        if support_decom is not None:
            self.support_decom = support_decom
        if support_reinstall is not None:
            self.support_reinstall = support_reinstall
        if support_collect_stack_info is not None:
            self.support_collect_stack_info = support_collect_stack_info

    @property
    def id(self):
        r"""Gets the id of this ComponentInfo.

        组件ID。

        :return: The id of this ComponentInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComponentInfo.

        组件ID。

        :param id: The id of this ComponentInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ComponentInfo.

        组件名。

        :return: The name of this ComponentInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ComponentInfo.

        组件名。

        :param name: The name of this ComponentInfo.
        :type name: str
        """
        self._name = name

    @property
    def instance_group_name(self):
        r"""Gets the instance_group_name of this ComponentInfo.

        组件所在组名称。

        :return: The instance_group_name of this ComponentInfo.
        :rtype: str
        """
        return self._instance_group_name

    @instance_group_name.setter
    def instance_group_name(self, instance_group_name):
        r"""Sets the instance_group_name of this ComponentInfo.

        组件所在组名称。

        :param instance_group_name: The instance_group_name of this ComponentInfo.
        :type instance_group_name: str
        """
        self._instance_group_name = instance_group_name

    @property
    def running_status(self):
        r"""Gets the running_status of this ComponentInfo.

        运行状态。

        :return: The running_status of this ComponentInfo.
        :rtype: str
        """
        return self._running_status

    @running_status.setter
    def running_status(self, running_status):
        r"""Sets the running_status of this ComponentInfo.

        运行状态。

        :param running_status: The running_status of this ComponentInfo.
        :type running_status: str
        """
        self._running_status = running_status

    @property
    def ha_status(self):
        r"""Gets the ha_status of this ComponentInfo.

        HA状态。

        :return: The ha_status of this ComponentInfo.
        :rtype: str
        """
        return self._ha_status

    @ha_status.setter
    def ha_status(self, ha_status):
        r"""Sets the ha_status of this ComponentInfo.

        HA状态。

        :param ha_status: The ha_status of this ComponentInfo.
        :type ha_status: str
        """
        self._ha_status = ha_status

    @property
    def config_status(self):
        r"""Gets the config_status of this ComponentInfo.

        配置状态。

        :return: The config_status of this ComponentInfo.
        :rtype: str
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        r"""Sets the config_status of this ComponentInfo.

        配置状态。

        :param config_status: The config_status of this ComponentInfo.
        :type config_status: str
        """
        self._config_status = config_status

    @property
    def role_name(self):
        r"""Gets the role_name of this ComponentInfo.

        角色。

        :return: The role_name of this ComponentInfo.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this ComponentInfo.

        角色。

        :param role_name: The role_name of this ComponentInfo.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def role_short_name(self):
        r"""Gets the role_short_name of this ComponentInfo.

        角色缩写。

        :return: The role_short_name of this ComponentInfo.
        :rtype: str
        """
        return self._role_short_name

    @role_short_name.setter
    def role_short_name(self, role_short_name):
        r"""Sets the role_short_name of this ComponentInfo.

        角色缩写。

        :param role_short_name: The role_short_name of this ComponentInfo.
        :type role_short_name: str
        """
        self._role_short_name = role_short_name

    @property
    def role_type(self):
        r"""Gets the role_type of this ComponentInfo.

        角色类型。

        :return: The role_type of this ComponentInfo.
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        r"""Sets the role_type of this ComponentInfo.

        角色类型。

        :param role_type: The role_type of this ComponentInfo.
        :type role_type: str
        """
        self._role_type = role_type

    @property
    def service_name(self):
        r"""Gets the service_name of this ComponentInfo.

        服务名。

        :return: The service_name of this ComponentInfo.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ComponentInfo.

        服务名。

        :param service_name: The service_name of this ComponentInfo.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def pair_name(self):
        r"""Gets the pair_name of this ComponentInfo.

        对名。

        :return: The pair_name of this ComponentInfo.
        :rtype: str
        """
        return self._pair_name

    @pair_name.setter
    def pair_name(self, pair_name):
        r"""Sets the pair_name of this ComponentInfo.

        对名。

        :param pair_name: The pair_name of this ComponentInfo.
        :type pair_name: str
        """
        self._pair_name = pair_name

    @property
    def relation_pairs(self):
        r"""Gets the relation_pairs of this ComponentInfo.

        关联对。

        :return: The relation_pairs of this ComponentInfo.
        :rtype: str
        """
        return self._relation_pairs

    @relation_pairs.setter
    def relation_pairs(self, relation_pairs):
        r"""Sets the relation_pairs of this ComponentInfo.

        关联对。

        :param relation_pairs: The relation_pairs of this ComponentInfo.
        :type relation_pairs: str
        """
        self._relation_pairs = relation_pairs

    @property
    def support_decom(self):
        r"""Gets the support_decom of this ComponentInfo.

        是否支持Decom。

        :return: The support_decom of this ComponentInfo.
        :rtype: str
        """
        return self._support_decom

    @support_decom.setter
    def support_decom(self, support_decom):
        r"""Sets the support_decom of this ComponentInfo.

        是否支持Decom。

        :param support_decom: The support_decom of this ComponentInfo.
        :type support_decom: str
        """
        self._support_decom = support_decom

    @property
    def support_reinstall(self):
        r"""Gets the support_reinstall of this ComponentInfo.

        是否支持重装。

        :return: The support_reinstall of this ComponentInfo.
        :rtype: str
        """
        return self._support_reinstall

    @support_reinstall.setter
    def support_reinstall(self, support_reinstall):
        r"""Sets the support_reinstall of this ComponentInfo.

        是否支持重装。

        :param support_reinstall: The support_reinstall of this ComponentInfo.
        :type support_reinstall: str
        """
        self._support_reinstall = support_reinstall

    @property
    def support_collect_stack_info(self):
        r"""Gets the support_collect_stack_info of this ComponentInfo.

        是否支持收集堆栈信息。

        :return: The support_collect_stack_info of this ComponentInfo.
        :rtype: str
        """
        return self._support_collect_stack_info

    @support_collect_stack_info.setter
    def support_collect_stack_info(self, support_collect_stack_info):
        r"""Sets the support_collect_stack_info of this ComponentInfo.

        是否支持收集堆栈信息。

        :param support_collect_stack_info: The support_collect_stack_info of this ComponentInfo.
        :type support_collect_stack_info: str
        """
        self._support_collect_stack_info = support_collect_stack_info

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
        if not isinstance(other, ComponentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
