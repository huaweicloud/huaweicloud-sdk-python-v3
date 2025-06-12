# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsDisableResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'forbiddener': 'str',
        'reson': 'str',
        'disabled': 'int',
        'job_id': 'str',
        'job_name': 'str',
        'forbidden_time': 'float'
    }

    attribute_map = {
        'forbiddener': 'forbiddener',
        'reson': 'reson',
        'disabled': 'disabled',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'forbidden_time': 'forbidden_time'
    }

    def __init__(self, forbiddener=None, reson=None, disabled=None, job_id=None, job_name=None, forbidden_time=None):
        r"""IsDisableResult

        The model defined in huaweicloud sdk

        :param forbiddener: 禁用者
        :type forbiddener: str
        :param reson: 禁用描述
        :type reson: str
        :param disabled: 禁用标识
        :type disabled: int
        :param job_id: 任务ID
        :type job_id: str
        :param job_name: 明文名称
        :type job_name: str
        :param forbidden_time: 禁用时间
        :type forbidden_time: float
        """
        
        

        self._forbiddener = None
        self._reson = None
        self._disabled = None
        self._job_id = None
        self._job_name = None
        self._forbidden_time = None
        self.discriminator = None

        if forbiddener is not None:
            self.forbiddener = forbiddener
        if reson is not None:
            self.reson = reson
        if disabled is not None:
            self.disabled = disabled
        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if forbidden_time is not None:
            self.forbidden_time = forbidden_time

    @property
    def forbiddener(self):
        r"""Gets the forbiddener of this IsDisableResult.

        禁用者

        :return: The forbiddener of this IsDisableResult.
        :rtype: str
        """
        return self._forbiddener

    @forbiddener.setter
    def forbiddener(self, forbiddener):
        r"""Sets the forbiddener of this IsDisableResult.

        禁用者

        :param forbiddener: The forbiddener of this IsDisableResult.
        :type forbiddener: str
        """
        self._forbiddener = forbiddener

    @property
    def reson(self):
        r"""Gets the reson of this IsDisableResult.

        禁用描述

        :return: The reson of this IsDisableResult.
        :rtype: str
        """
        return self._reson

    @reson.setter
    def reson(self, reson):
        r"""Sets the reson of this IsDisableResult.

        禁用描述

        :param reson: The reson of this IsDisableResult.
        :type reson: str
        """
        self._reson = reson

    @property
    def disabled(self):
        r"""Gets the disabled of this IsDisableResult.

        禁用标识

        :return: The disabled of this IsDisableResult.
        :rtype: int
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this IsDisableResult.

        禁用标识

        :param disabled: The disabled of this IsDisableResult.
        :type disabled: int
        """
        self._disabled = disabled

    @property
    def job_id(self):
        r"""Gets the job_id of this IsDisableResult.

        任务ID

        :return: The job_id of this IsDisableResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this IsDisableResult.

        任务ID

        :param job_id: The job_id of this IsDisableResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this IsDisableResult.

        明文名称

        :return: The job_name of this IsDisableResult.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this IsDisableResult.

        明文名称

        :param job_name: The job_name of this IsDisableResult.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def forbidden_time(self):
        r"""Gets the forbidden_time of this IsDisableResult.

        禁用时间

        :return: The forbidden_time of this IsDisableResult.
        :rtype: float
        """
        return self._forbidden_time

    @forbidden_time.setter
    def forbidden_time(self, forbidden_time):
        r"""Sets the forbidden_time of this IsDisableResult.

        禁用时间

        :param forbidden_time: The forbidden_time of this IsDisableResult.
        :type forbidden_time: float
        """
        self._forbidden_time = forbidden_time

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
        if not isinstance(other, IsDisableResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
