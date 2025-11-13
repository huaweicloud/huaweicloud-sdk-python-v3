# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UsageStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'user_id': 'str',
        'job_type': 'str',
        'charge_sum': 'float'
    }

    attribute_map = {
        'user_name': 'user_name',
        'user_id': 'user_id',
        'job_type': 'job_type',
        'charge_sum': 'charge_sum'
    }

    def __init__(self, user_name=None, user_id=None, job_type=None, charge_sum=None):
        r"""UsageStatistics

        The model defined in huaweicloud sdk

        :param user_name: **参数解释**： 用户名。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type user_name: str
        :param user_id: **参数解释**： 用户id。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type user_id: str
        :param job_type: **参数解释**： 作业类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type job_type: str
        :param charge_sum: **参数解释**： 作业使用量。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type charge_sum: float
        """
        
        

        self._user_name = None
        self._user_id = None
        self._job_type = None
        self._charge_sum = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if user_id is not None:
            self.user_id = user_id
        if job_type is not None:
            self.job_type = job_type
        if charge_sum is not None:
            self.charge_sum = charge_sum

    @property
    def user_name(self):
        r"""Gets the user_name of this UsageStatistics.

        **参数解释**： 用户名。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The user_name of this UsageStatistics.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this UsageStatistics.

        **参数解释**： 用户名。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param user_name: The user_name of this UsageStatistics.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_id(self):
        r"""Gets the user_id of this UsageStatistics.

        **参数解释**： 用户id。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The user_id of this UsageStatistics.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UsageStatistics.

        **参数解释**： 用户id。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param user_id: The user_id of this UsageStatistics.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def job_type(self):
        r"""Gets the job_type of this UsageStatistics.

        **参数解释**： 作业类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The job_type of this UsageStatistics.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this UsageStatistics.

        **参数解释**： 作业类型。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param job_type: The job_type of this UsageStatistics.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def charge_sum(self):
        r"""Gets the charge_sum of this UsageStatistics.

        **参数解释**： 作业使用量。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The charge_sum of this UsageStatistics.
        :rtype: float
        """
        return self._charge_sum

    @charge_sum.setter
    def charge_sum(self, charge_sum):
        r"""Sets the charge_sum of this UsageStatistics.

        **参数解释**： 作业使用量。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param charge_sum: The charge_sum of this UsageStatistics.
        :type charge_sum: float
        """
        self._charge_sum = charge_sum

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
        if not isinstance(other, UsageStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
