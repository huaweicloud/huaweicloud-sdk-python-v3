# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmRestartClusterReqRestart:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restart_delay_time': 'int',
        'restart_mode': 'str',
        'restart_level': 'str',
        'type': 'str',
        'instance': 'str',
        'group': 'str'
    }

    attribute_map = {
        'restart_delay_time': 'restartDelayTime',
        'restart_mode': 'restartMode',
        'restart_level': 'restartLevel',
        'type': 'type',
        'instance': 'instance',
        'group': 'group'
    }

    def __init__(self, restart_delay_time=None, restart_mode=None, restart_level=None, type=None, instance=None, group=None):
        """CdmRestartClusterReqRestart

        The model defined in huaweicloud sdk

        :param restart_delay_time: 重启时延，单位：秒
        :type restart_delay_time: int
        :param restart_mode: 重启类型： - IMMEDIATELY：立即重启。 - FORCELY：强制重启。 - SOFTLY：一般重启。  默认值为“IMMEDIATELY”。强制重启业务进程会中断，并重启集群的虚拟机。
        :type restart_mode: str
        :param restart_level: 重启级别： - SERVICE：重启服务。 - VM：重启虚拟机。  默认值为“SERVICE”。
        :type restart_level: str
        :param type: 集群节点类型，只支持“cdm”
        :type type: str
        :param instance: 预留字段，“restartLevel” 为“SERVICE”时，“instance”必填，填空字串。
        :type instance: str
        :param group: 预留字段，“restartLevel” 为“SERVICE”时，“group”必填，填空字串。
        :type group: str
        """
        
        

        self._restart_delay_time = None
        self._restart_mode = None
        self._restart_level = None
        self._type = None
        self._instance = None
        self._group = None
        self.discriminator = None

        if restart_delay_time is not None:
            self.restart_delay_time = restart_delay_time
        if restart_mode is not None:
            self.restart_mode = restart_mode
        if restart_level is not None:
            self.restart_level = restart_level
        self.type = type
        if instance is not None:
            self.instance = instance
        if group is not None:
            self.group = group

    @property
    def restart_delay_time(self):
        """Gets the restart_delay_time of this CdmRestartClusterReqRestart.

        重启时延，单位：秒

        :return: The restart_delay_time of this CdmRestartClusterReqRestart.
        :rtype: int
        """
        return self._restart_delay_time

    @restart_delay_time.setter
    def restart_delay_time(self, restart_delay_time):
        """Sets the restart_delay_time of this CdmRestartClusterReqRestart.

        重启时延，单位：秒

        :param restart_delay_time: The restart_delay_time of this CdmRestartClusterReqRestart.
        :type restart_delay_time: int
        """
        self._restart_delay_time = restart_delay_time

    @property
    def restart_mode(self):
        """Gets the restart_mode of this CdmRestartClusterReqRestart.

        重启类型： - IMMEDIATELY：立即重启。 - FORCELY：强制重启。 - SOFTLY：一般重启。  默认值为“IMMEDIATELY”。强制重启业务进程会中断，并重启集群的虚拟机。

        :return: The restart_mode of this CdmRestartClusterReqRestart.
        :rtype: str
        """
        return self._restart_mode

    @restart_mode.setter
    def restart_mode(self, restart_mode):
        """Sets the restart_mode of this CdmRestartClusterReqRestart.

        重启类型： - IMMEDIATELY：立即重启。 - FORCELY：强制重启。 - SOFTLY：一般重启。  默认值为“IMMEDIATELY”。强制重启业务进程会中断，并重启集群的虚拟机。

        :param restart_mode: The restart_mode of this CdmRestartClusterReqRestart.
        :type restart_mode: str
        """
        self._restart_mode = restart_mode

    @property
    def restart_level(self):
        """Gets the restart_level of this CdmRestartClusterReqRestart.

        重启级别： - SERVICE：重启服务。 - VM：重启虚拟机。  默认值为“SERVICE”。

        :return: The restart_level of this CdmRestartClusterReqRestart.
        :rtype: str
        """
        return self._restart_level

    @restart_level.setter
    def restart_level(self, restart_level):
        """Sets the restart_level of this CdmRestartClusterReqRestart.

        重启级别： - SERVICE：重启服务。 - VM：重启虚拟机。  默认值为“SERVICE”。

        :param restart_level: The restart_level of this CdmRestartClusterReqRestart.
        :type restart_level: str
        """
        self._restart_level = restart_level

    @property
    def type(self):
        """Gets the type of this CdmRestartClusterReqRestart.

        集群节点类型，只支持“cdm”

        :return: The type of this CdmRestartClusterReqRestart.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CdmRestartClusterReqRestart.

        集群节点类型，只支持“cdm”

        :param type: The type of this CdmRestartClusterReqRestart.
        :type type: str
        """
        self._type = type

    @property
    def instance(self):
        """Gets the instance of this CdmRestartClusterReqRestart.

        预留字段，“restartLevel” 为“SERVICE”时，“instance”必填，填空字串。

        :return: The instance of this CdmRestartClusterReqRestart.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this CdmRestartClusterReqRestart.

        预留字段，“restartLevel” 为“SERVICE”时，“instance”必填，填空字串。

        :param instance: The instance of this CdmRestartClusterReqRestart.
        :type instance: str
        """
        self._instance = instance

    @property
    def group(self):
        """Gets the group of this CdmRestartClusterReqRestart.

        预留字段，“restartLevel” 为“SERVICE”时，“group”必填，填空字串。

        :return: The group of this CdmRestartClusterReqRestart.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this CdmRestartClusterReqRestart.

        预留字段，“restartLevel” 为“SERVICE”时，“group”必填，填空字串。

        :param group: The group of this CdmRestartClusterReqRestart.
        :type group: str
        """
        self._group = group

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
        if not isinstance(other, CdmRestartClusterReqRestart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
