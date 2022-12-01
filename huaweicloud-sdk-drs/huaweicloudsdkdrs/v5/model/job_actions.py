# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobActions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'available_actions': 'list[str]',
        'unavailable_actions': 'list[str]',
        'current_action': 'str'
    }

    attribute_map = {
        'available_actions': 'available_actions',
        'unavailable_actions': 'unavailable_actions',
        'current_action': 'current_action'
    }

    def __init__(self, available_actions=None, unavailable_actions=None, current_action=None):
        """JobActions

        The model defined in huaweicloud sdk

        :param available_actions: 任务可操作命令集合。
        :type available_actions: list[str]
        :param unavailable_actions: 任务不可操作命令集合。
        :type unavailable_actions: list[str]
        :param current_action: 任务当前操作命令。取值： - API_CONFIGURATION_ACTION：OPEN API配置中的任务能调用。 - CHANGE：修改任务。 - CHANGE_MODE：修改任务模式。 - CHOOSE_OBJECT：选择对象。 - CLONE：克隆任务。 - CONTINUE_APPLY：启动回放，Oracle同步到GaussDB分布式适用。 - CONTINUE_CAPTURE：启动抓取，Oracle同步到GaussDB分布式适用。 - CONTINUE_JOB：启动失败或者停止的任务，Oracle同步到GaussDB分布式适用。 - CREATE：创建任务。 - DELETE：删除任务。 - FREE_RESOURCE：释放资源。 - JUMP_RETRY：跳跃续传任务。 - MODIFY_CONFIGURATION：修改任务配置。 - MODIFY_DB_CONFIG：修改数据库配置。 - MODIFY_TASK_NUMBER：修改线程数配置。 - NODE_FLAVOR_MODIFY：规格变更。 - ORDER_INFO：订单详情。 - PAUSE：暂停任务。 - PAY_ORDER：包年/包月支付订单。 - PRE_CHECK：预检查。 - QUERY_PRE_CHECK：查询预检查结果。 - RESET：重置任务。 - RESET_DB_PWD：重置数据库密码（源库、目标库）。 - RETRY：重试任务。 - START：启动任务。 - START_INCR：启动增量任务。 - STOP_APPLY：停止回放，Oracle同步到GaussDB分布式适用。 - STOP_CAPTURE：停止抓取，Oracle同步到GaussDB分布式适用。 - STOP_JOB：停止任务，Oracle同步到GaussDB分布式适用。 - SWITCH_OVER：灾备倒换。 - TO_PERIOD：转包年/包月任务。 - TO_RENEW：包年/包月任务续费。 - UNSUBSCRIBE：包年/包月任务退订。
        :type current_action: str
        """
        
        

        self._available_actions = None
        self._unavailable_actions = None
        self._current_action = None
        self.discriminator = None

        self.available_actions = available_actions
        self.unavailable_actions = unavailable_actions
        self.current_action = current_action

    @property
    def available_actions(self):
        """Gets the available_actions of this JobActions.

        任务可操作命令集合。

        :return: The available_actions of this JobActions.
        :rtype: list[str]
        """
        return self._available_actions

    @available_actions.setter
    def available_actions(self, available_actions):
        """Sets the available_actions of this JobActions.

        任务可操作命令集合。

        :param available_actions: The available_actions of this JobActions.
        :type available_actions: list[str]
        """
        self._available_actions = available_actions

    @property
    def unavailable_actions(self):
        """Gets the unavailable_actions of this JobActions.

        任务不可操作命令集合。

        :return: The unavailable_actions of this JobActions.
        :rtype: list[str]
        """
        return self._unavailable_actions

    @unavailable_actions.setter
    def unavailable_actions(self, unavailable_actions):
        """Sets the unavailable_actions of this JobActions.

        任务不可操作命令集合。

        :param unavailable_actions: The unavailable_actions of this JobActions.
        :type unavailable_actions: list[str]
        """
        self._unavailable_actions = unavailable_actions

    @property
    def current_action(self):
        """Gets the current_action of this JobActions.

        任务当前操作命令。取值： - API_CONFIGURATION_ACTION：OPEN API配置中的任务能调用。 - CHANGE：修改任务。 - CHANGE_MODE：修改任务模式。 - CHOOSE_OBJECT：选择对象。 - CLONE：克隆任务。 - CONTINUE_APPLY：启动回放，Oracle同步到GaussDB分布式适用。 - CONTINUE_CAPTURE：启动抓取，Oracle同步到GaussDB分布式适用。 - CONTINUE_JOB：启动失败或者停止的任务，Oracle同步到GaussDB分布式适用。 - CREATE：创建任务。 - DELETE：删除任务。 - FREE_RESOURCE：释放资源。 - JUMP_RETRY：跳跃续传任务。 - MODIFY_CONFIGURATION：修改任务配置。 - MODIFY_DB_CONFIG：修改数据库配置。 - MODIFY_TASK_NUMBER：修改线程数配置。 - NODE_FLAVOR_MODIFY：规格变更。 - ORDER_INFO：订单详情。 - PAUSE：暂停任务。 - PAY_ORDER：包年/包月支付订单。 - PRE_CHECK：预检查。 - QUERY_PRE_CHECK：查询预检查结果。 - RESET：重置任务。 - RESET_DB_PWD：重置数据库密码（源库、目标库）。 - RETRY：重试任务。 - START：启动任务。 - START_INCR：启动增量任务。 - STOP_APPLY：停止回放，Oracle同步到GaussDB分布式适用。 - STOP_CAPTURE：停止抓取，Oracle同步到GaussDB分布式适用。 - STOP_JOB：停止任务，Oracle同步到GaussDB分布式适用。 - SWITCH_OVER：灾备倒换。 - TO_PERIOD：转包年/包月任务。 - TO_RENEW：包年/包月任务续费。 - UNSUBSCRIBE：包年/包月任务退订。

        :return: The current_action of this JobActions.
        :rtype: str
        """
        return self._current_action

    @current_action.setter
    def current_action(self, current_action):
        """Sets the current_action of this JobActions.

        任务当前操作命令。取值： - API_CONFIGURATION_ACTION：OPEN API配置中的任务能调用。 - CHANGE：修改任务。 - CHANGE_MODE：修改任务模式。 - CHOOSE_OBJECT：选择对象。 - CLONE：克隆任务。 - CONTINUE_APPLY：启动回放，Oracle同步到GaussDB分布式适用。 - CONTINUE_CAPTURE：启动抓取，Oracle同步到GaussDB分布式适用。 - CONTINUE_JOB：启动失败或者停止的任务，Oracle同步到GaussDB分布式适用。 - CREATE：创建任务。 - DELETE：删除任务。 - FREE_RESOURCE：释放资源。 - JUMP_RETRY：跳跃续传任务。 - MODIFY_CONFIGURATION：修改任务配置。 - MODIFY_DB_CONFIG：修改数据库配置。 - MODIFY_TASK_NUMBER：修改线程数配置。 - NODE_FLAVOR_MODIFY：规格变更。 - ORDER_INFO：订单详情。 - PAUSE：暂停任务。 - PAY_ORDER：包年/包月支付订单。 - PRE_CHECK：预检查。 - QUERY_PRE_CHECK：查询预检查结果。 - RESET：重置任务。 - RESET_DB_PWD：重置数据库密码（源库、目标库）。 - RETRY：重试任务。 - START：启动任务。 - START_INCR：启动增量任务。 - STOP_APPLY：停止回放，Oracle同步到GaussDB分布式适用。 - STOP_CAPTURE：停止抓取，Oracle同步到GaussDB分布式适用。 - STOP_JOB：停止任务，Oracle同步到GaussDB分布式适用。 - SWITCH_OVER：灾备倒换。 - TO_PERIOD：转包年/包月任务。 - TO_RENEW：包年/包月任务续费。 - UNSUBSCRIBE：包年/包月任务退订。

        :param current_action: The current_action of this JobActions.
        :type current_action: str
        """
        self._current_action = current_action

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
        if not isinstance(other, JobActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
