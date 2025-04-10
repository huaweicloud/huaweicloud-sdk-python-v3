# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResolveTaskResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'tpl_id': 'str',
        'sms_signs': 'list[str]',
        'resolving_times': 'int',
        'resolved_times': 'int',
        'aim_code_type': 'str',
        'domain': 'str',
        'expiration_time': 'int',
        'params': 'list[ListResolveTaskResultParam]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'tpl_id': 'tpl_id',
        'sms_signs': 'sms_signs',
        'resolving_times': 'resolving_times',
        'resolved_times': 'resolved_times',
        'aim_code_type': 'aim_code_type',
        'domain': 'domain',
        'expiration_time': 'expiration_time',
        'params': 'params'
    }

    def __init__(self, task_id=None, task_name=None, tpl_id=None, sms_signs=None, resolving_times=None, resolved_times=None, aim_code_type=None, domain=None, expiration_time=None, params=None):
        r"""ListResolveTaskResult

        The model defined in huaweicloud sdk

        :param task_id: 任务ID。
        :type task_id: str
        :param task_name: 任务名称。
        :type task_name: str
        :param tpl_id: 智能信息模板ID，由9位数字组成。
        :type tpl_id: str
        :param sms_signs: 短信签名列表。
        :type sms_signs: list[str]
        :param resolving_times: 用户创建时提交的最大解析次数。
        :type resolving_times: int
        :param resolved_times: 实际已解析数量统计。 
        :type resolved_times: int
        :param aim_code_type: 智能信息编码类型。 - group：群发 - individual：个性化 
        :type aim_code_type: str
        :param domain: 自定义短链域名，由大小写字母和数字组成的二级域名。
        :type domain: str
        :param expiration_time: 失效时间（天）。
        :type expiration_time: int
        :param params: 短链列表。该列表中只会有一条短链记录，如果一个任务中生成多个短链，则需要客户端基于任务ID（task_id）自己去合并。  &gt; 建议使用查询解析明细接口查询此字段信息，未来版本有计划移除该字段。 
        :type params: list[:class:`huaweicloudsdkkoomessage.v1.ListResolveTaskResultParam`]
        """
        
        

        self._task_id = None
        self._task_name = None
        self._tpl_id = None
        self._sms_signs = None
        self._resolving_times = None
        self._resolved_times = None
        self._aim_code_type = None
        self._domain = None
        self._expiration_time = None
        self._params = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if tpl_id is not None:
            self.tpl_id = tpl_id
        if sms_signs is not None:
            self.sms_signs = sms_signs
        if resolving_times is not None:
            self.resolving_times = resolving_times
        if resolved_times is not None:
            self.resolved_times = resolved_times
        if aim_code_type is not None:
            self.aim_code_type = aim_code_type
        if domain is not None:
            self.domain = domain
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if params is not None:
            self.params = params

    @property
    def task_id(self):
        r"""Gets the task_id of this ListResolveTaskResult.

        任务ID。

        :return: The task_id of this ListResolveTaskResult.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListResolveTaskResult.

        任务ID。

        :param task_id: The task_id of this ListResolveTaskResult.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ListResolveTaskResult.

        任务名称。

        :return: The task_name of this ListResolveTaskResult.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListResolveTaskResult.

        任务名称。

        :param task_name: The task_name of this ListResolveTaskResult.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def tpl_id(self):
        r"""Gets the tpl_id of this ListResolveTaskResult.

        智能信息模板ID，由9位数字组成。

        :return: The tpl_id of this ListResolveTaskResult.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        r"""Sets the tpl_id of this ListResolveTaskResult.

        智能信息模板ID，由9位数字组成。

        :param tpl_id: The tpl_id of this ListResolveTaskResult.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def sms_signs(self):
        r"""Gets the sms_signs of this ListResolveTaskResult.

        短信签名列表。

        :return: The sms_signs of this ListResolveTaskResult.
        :rtype: list[str]
        """
        return self._sms_signs

    @sms_signs.setter
    def sms_signs(self, sms_signs):
        r"""Sets the sms_signs of this ListResolveTaskResult.

        短信签名列表。

        :param sms_signs: The sms_signs of this ListResolveTaskResult.
        :type sms_signs: list[str]
        """
        self._sms_signs = sms_signs

    @property
    def resolving_times(self):
        r"""Gets the resolving_times of this ListResolveTaskResult.

        用户创建时提交的最大解析次数。

        :return: The resolving_times of this ListResolveTaskResult.
        :rtype: int
        """
        return self._resolving_times

    @resolving_times.setter
    def resolving_times(self, resolving_times):
        r"""Sets the resolving_times of this ListResolveTaskResult.

        用户创建时提交的最大解析次数。

        :param resolving_times: The resolving_times of this ListResolveTaskResult.
        :type resolving_times: int
        """
        self._resolving_times = resolving_times

    @property
    def resolved_times(self):
        r"""Gets the resolved_times of this ListResolveTaskResult.

        实际已解析数量统计。 

        :return: The resolved_times of this ListResolveTaskResult.
        :rtype: int
        """
        return self._resolved_times

    @resolved_times.setter
    def resolved_times(self, resolved_times):
        r"""Sets the resolved_times of this ListResolveTaskResult.

        实际已解析数量统计。 

        :param resolved_times: The resolved_times of this ListResolveTaskResult.
        :type resolved_times: int
        """
        self._resolved_times = resolved_times

    @property
    def aim_code_type(self):
        r"""Gets the aim_code_type of this ListResolveTaskResult.

        智能信息编码类型。 - group：群发 - individual：个性化 

        :return: The aim_code_type of this ListResolveTaskResult.
        :rtype: str
        """
        return self._aim_code_type

    @aim_code_type.setter
    def aim_code_type(self, aim_code_type):
        r"""Sets the aim_code_type of this ListResolveTaskResult.

        智能信息编码类型。 - group：群发 - individual：个性化 

        :param aim_code_type: The aim_code_type of this ListResolveTaskResult.
        :type aim_code_type: str
        """
        self._aim_code_type = aim_code_type

    @property
    def domain(self):
        r"""Gets the domain of this ListResolveTaskResult.

        自定义短链域名，由大小写字母和数字组成的二级域名。

        :return: The domain of this ListResolveTaskResult.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListResolveTaskResult.

        自定义短链域名，由大小写字母和数字组成的二级域名。

        :param domain: The domain of this ListResolveTaskResult.
        :type domain: str
        """
        self._domain = domain

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this ListResolveTaskResult.

        失效时间（天）。

        :return: The expiration_time of this ListResolveTaskResult.
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this ListResolveTaskResult.

        失效时间（天）。

        :param expiration_time: The expiration_time of this ListResolveTaskResult.
        :type expiration_time: int
        """
        self._expiration_time = expiration_time

    @property
    def params(self):
        r"""Gets the params of this ListResolveTaskResult.

        短链列表。该列表中只会有一条短链记录，如果一个任务中生成多个短链，则需要客户端基于任务ID（task_id）自己去合并。  > 建议使用查询解析明细接口查询此字段信息，未来版本有计划移除该字段。 

        :return: The params of this ListResolveTaskResult.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.ListResolveTaskResultParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this ListResolveTaskResult.

        短链列表。该列表中只会有一条短链记录，如果一个任务中生成多个短链，则需要客户端基于任务ID（task_id）自己去合并。  > 建议使用查询解析明细接口查询此字段信息，未来版本有计划移除该字段。 

        :param params: The params of this ListResolveTaskResult.
        :type params: list[:class:`huaweicloudsdkkoomessage.v1.ListResolveTaskResultParam`]
        """
        self._params = params

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
        if not isinstance(other, ListResolveTaskResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
