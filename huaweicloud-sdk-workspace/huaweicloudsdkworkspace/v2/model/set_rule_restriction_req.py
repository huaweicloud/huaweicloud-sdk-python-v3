# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetRuleRestrictionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_restrict_rule_switch': 'bool',
        'app_control_mode': 'int',
        'app_periodic_switch': 'bool',
        'app_periodic_interval': 'int',
        'app_force_kill_proc_switch': 'bool'
    }

    attribute_map = {
        'app_restrict_rule_switch': 'app_restrict_rule_switch',
        'app_control_mode': 'app_control_mode',
        'app_periodic_switch': 'app_periodic_switch',
        'app_periodic_interval': 'app_periodic_interval',
        'app_force_kill_proc_switch': 'app_force_kill_proc_switch'
    }

    def __init__(self, app_restrict_rule_switch=None, app_control_mode=None, app_periodic_switch=None, app_periodic_interval=None, app_force_kill_proc_switch=None):
        r"""SetRuleRestrictionReq

        The model defined in huaweicloud sdk

        :param app_restrict_rule_switch: 应用管控开关，false：关闭，true：打开
        :type app_restrict_rule_switch: bool
        :param app_control_mode: 应用管控方式，0：禁止列表应用程序运行
        :type app_control_mode: int
        :param app_periodic_switch: 周期性监控开关，false：关闭，true：打开
        :type app_periodic_switch: bool
        :param app_periodic_interval: 周期性监控间隔时间，单位分钟
        :type app_periodic_interval: int
        :param app_force_kill_proc_switch: 强制kill应用开关，false：关闭，true：打开
        :type app_force_kill_proc_switch: bool
        """
        
        

        self._app_restrict_rule_switch = None
        self._app_control_mode = None
        self._app_periodic_switch = None
        self._app_periodic_interval = None
        self._app_force_kill_proc_switch = None
        self.discriminator = None

        self.app_restrict_rule_switch = app_restrict_rule_switch
        if app_control_mode is not None:
            self.app_control_mode = app_control_mode
        if app_periodic_switch is not None:
            self.app_periodic_switch = app_periodic_switch
        if app_periodic_interval is not None:
            self.app_periodic_interval = app_periodic_interval
        if app_force_kill_proc_switch is not None:
            self.app_force_kill_proc_switch = app_force_kill_proc_switch

    @property
    def app_restrict_rule_switch(self):
        r"""Gets the app_restrict_rule_switch of this SetRuleRestrictionReq.

        应用管控开关，false：关闭，true：打开

        :return: The app_restrict_rule_switch of this SetRuleRestrictionReq.
        :rtype: bool
        """
        return self._app_restrict_rule_switch

    @app_restrict_rule_switch.setter
    def app_restrict_rule_switch(self, app_restrict_rule_switch):
        r"""Sets the app_restrict_rule_switch of this SetRuleRestrictionReq.

        应用管控开关，false：关闭，true：打开

        :param app_restrict_rule_switch: The app_restrict_rule_switch of this SetRuleRestrictionReq.
        :type app_restrict_rule_switch: bool
        """
        self._app_restrict_rule_switch = app_restrict_rule_switch

    @property
    def app_control_mode(self):
        r"""Gets the app_control_mode of this SetRuleRestrictionReq.

        应用管控方式，0：禁止列表应用程序运行

        :return: The app_control_mode of this SetRuleRestrictionReq.
        :rtype: int
        """
        return self._app_control_mode

    @app_control_mode.setter
    def app_control_mode(self, app_control_mode):
        r"""Sets the app_control_mode of this SetRuleRestrictionReq.

        应用管控方式，0：禁止列表应用程序运行

        :param app_control_mode: The app_control_mode of this SetRuleRestrictionReq.
        :type app_control_mode: int
        """
        self._app_control_mode = app_control_mode

    @property
    def app_periodic_switch(self):
        r"""Gets the app_periodic_switch of this SetRuleRestrictionReq.

        周期性监控开关，false：关闭，true：打开

        :return: The app_periodic_switch of this SetRuleRestrictionReq.
        :rtype: bool
        """
        return self._app_periodic_switch

    @app_periodic_switch.setter
    def app_periodic_switch(self, app_periodic_switch):
        r"""Sets the app_periodic_switch of this SetRuleRestrictionReq.

        周期性监控开关，false：关闭，true：打开

        :param app_periodic_switch: The app_periodic_switch of this SetRuleRestrictionReq.
        :type app_periodic_switch: bool
        """
        self._app_periodic_switch = app_periodic_switch

    @property
    def app_periodic_interval(self):
        r"""Gets the app_periodic_interval of this SetRuleRestrictionReq.

        周期性监控间隔时间，单位分钟

        :return: The app_periodic_interval of this SetRuleRestrictionReq.
        :rtype: int
        """
        return self._app_periodic_interval

    @app_periodic_interval.setter
    def app_periodic_interval(self, app_periodic_interval):
        r"""Sets the app_periodic_interval of this SetRuleRestrictionReq.

        周期性监控间隔时间，单位分钟

        :param app_periodic_interval: The app_periodic_interval of this SetRuleRestrictionReq.
        :type app_periodic_interval: int
        """
        self._app_periodic_interval = app_periodic_interval

    @property
    def app_force_kill_proc_switch(self):
        r"""Gets the app_force_kill_proc_switch of this SetRuleRestrictionReq.

        强制kill应用开关，false：关闭，true：打开

        :return: The app_force_kill_proc_switch of this SetRuleRestrictionReq.
        :rtype: bool
        """
        return self._app_force_kill_proc_switch

    @app_force_kill_proc_switch.setter
    def app_force_kill_proc_switch(self, app_force_kill_proc_switch):
        r"""Sets the app_force_kill_proc_switch of this SetRuleRestrictionReq.

        强制kill应用开关，false：关闭，true：打开

        :param app_force_kill_proc_switch: The app_force_kill_proc_switch of this SetRuleRestrictionReq.
        :type app_force_kill_proc_switch: bool
        """
        self._app_force_kill_proc_switch = app_force_kill_proc_switch

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
        if not isinstance(other, SetRuleRestrictionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
