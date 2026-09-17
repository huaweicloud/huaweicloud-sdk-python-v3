# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowLogTplContrast:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_of_pre_day': 'list[SlowSqlTemplate]',
        'template_of_cur_day': 'list[SlowSqlTemplate]',
        'execute_time_increase': 'bool',
        'lock_wait_increase': 'bool',
        'new_template': 'bool'
    }

    attribute_map = {
        'template_of_pre_day': 'template_of_pre_day',
        'template_of_cur_day': 'template_of_cur_day',
        'execute_time_increase': 'execute_time_increase',
        'lock_wait_increase': 'lock_wait_increase',
        'new_template': 'new_template'
    }

    def __init__(self, template_of_pre_day=None, template_of_cur_day=None, execute_time_increase=None, lock_wait_increase=None, new_template=None):
        r"""SlowLogTplContrast

        The model defined in huaweicloud sdk

        :param template_of_pre_day: 前一日慢日志模板数据列表
        :type template_of_pre_day: list[:class:`huaweicloudsdkdas.v3.SlowSqlTemplate`]
        :param template_of_cur_day: 当日慢日志模板数据列表
        :type template_of_cur_day: list[:class:`huaweicloudsdkdas.v3.SlowSqlTemplate`]
        :param execute_time_increase: 执行耗时是否增长
        :type execute_time_increase: bool
        :param lock_wait_increase: 锁等待耗时是否增长
        :type lock_wait_increase: bool
        :param new_template: 是否新增模板
        :type new_template: bool
        """
        
        

        self._template_of_pre_day = None
        self._template_of_cur_day = None
        self._execute_time_increase = None
        self._lock_wait_increase = None
        self._new_template = None
        self.discriminator = None

        if template_of_pre_day is not None:
            self.template_of_pre_day = template_of_pre_day
        if template_of_cur_day is not None:
            self.template_of_cur_day = template_of_cur_day
        if execute_time_increase is not None:
            self.execute_time_increase = execute_time_increase
        if lock_wait_increase is not None:
            self.lock_wait_increase = lock_wait_increase
        if new_template is not None:
            self.new_template = new_template

    @property
    def template_of_pre_day(self):
        r"""Gets the template_of_pre_day of this SlowLogTplContrast.

        前一日慢日志模板数据列表

        :return: The template_of_pre_day of this SlowLogTplContrast.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowSqlTemplate`]
        """
        return self._template_of_pre_day

    @template_of_pre_day.setter
    def template_of_pre_day(self, template_of_pre_day):
        r"""Sets the template_of_pre_day of this SlowLogTplContrast.

        前一日慢日志模板数据列表

        :param template_of_pre_day: The template_of_pre_day of this SlowLogTplContrast.
        :type template_of_pre_day: list[:class:`huaweicloudsdkdas.v3.SlowSqlTemplate`]
        """
        self._template_of_pre_day = template_of_pre_day

    @property
    def template_of_cur_day(self):
        r"""Gets the template_of_cur_day of this SlowLogTplContrast.

        当日慢日志模板数据列表

        :return: The template_of_cur_day of this SlowLogTplContrast.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowSqlTemplate`]
        """
        return self._template_of_cur_day

    @template_of_cur_day.setter
    def template_of_cur_day(self, template_of_cur_day):
        r"""Sets the template_of_cur_day of this SlowLogTplContrast.

        当日慢日志模板数据列表

        :param template_of_cur_day: The template_of_cur_day of this SlowLogTplContrast.
        :type template_of_cur_day: list[:class:`huaweicloudsdkdas.v3.SlowSqlTemplate`]
        """
        self._template_of_cur_day = template_of_cur_day

    @property
    def execute_time_increase(self):
        r"""Gets the execute_time_increase of this SlowLogTplContrast.

        执行耗时是否增长

        :return: The execute_time_increase of this SlowLogTplContrast.
        :rtype: bool
        """
        return self._execute_time_increase

    @execute_time_increase.setter
    def execute_time_increase(self, execute_time_increase):
        r"""Sets the execute_time_increase of this SlowLogTplContrast.

        执行耗时是否增长

        :param execute_time_increase: The execute_time_increase of this SlowLogTplContrast.
        :type execute_time_increase: bool
        """
        self._execute_time_increase = execute_time_increase

    @property
    def lock_wait_increase(self):
        r"""Gets the lock_wait_increase of this SlowLogTplContrast.

        锁等待耗时是否增长

        :return: The lock_wait_increase of this SlowLogTplContrast.
        :rtype: bool
        """
        return self._lock_wait_increase

    @lock_wait_increase.setter
    def lock_wait_increase(self, lock_wait_increase):
        r"""Sets the lock_wait_increase of this SlowLogTplContrast.

        锁等待耗时是否增长

        :param lock_wait_increase: The lock_wait_increase of this SlowLogTplContrast.
        :type lock_wait_increase: bool
        """
        self._lock_wait_increase = lock_wait_increase

    @property
    def new_template(self):
        r"""Gets the new_template of this SlowLogTplContrast.

        是否新增模板

        :return: The new_template of this SlowLogTplContrast.
        :rtype: bool
        """
        return self._new_template

    @new_template.setter
    def new_template(self, new_template):
        r"""Sets the new_template of this SlowLogTplContrast.

        是否新增模板

        :param new_template: The new_template of this SlowLogTplContrast.
        :type new_template: bool
        """
        self._new_template = new_template

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
        if not isinstance(other, SlowLogTplContrast):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
