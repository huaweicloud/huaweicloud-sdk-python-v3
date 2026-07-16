# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AffinityType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'required_during_scheduling_ignored_during_execution': 'list[AffinityRule]',
        'preferred_during_scheduling_ignored_during_execution': 'list[AffinityRule]'
    }

    attribute_map = {
        'required_during_scheduling_ignored_during_execution': 'required_during_scheduling_ignored_during_execution',
        'preferred_during_scheduling_ignored_during_execution': 'preferred_during_scheduling_ignored_during_execution'
    }

    def __init__(self, required_during_scheduling_ignored_during_execution=None, preferred_during_scheduling_ignored_during_execution=None):
        r"""AffinityType

        The model defined in huaweicloud sdk

        :param required_during_scheduling_ignored_during_execution: 参数描述： 专属池场景下设置强亲和特性 参数约束： key、values、operator必填
        :type required_during_scheduling_ignored_during_execution: list[:class:`huaweicloudsdkmodelarts.v1.AffinityRule`]
        :param preferred_during_scheduling_ignored_during_execution: 参数描述： 专属池场景下设置弱亲和特性 参数约束： key、values、operator必填，weight选填
        :type preferred_during_scheduling_ignored_during_execution: list[:class:`huaweicloudsdkmodelarts.v1.AffinityRule`]
        """
        
        

        self._required_during_scheduling_ignored_during_execution = None
        self._preferred_during_scheduling_ignored_during_execution = None
        self.discriminator = None

        if required_during_scheduling_ignored_during_execution is not None:
            self.required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution
        if preferred_during_scheduling_ignored_during_execution is not None:
            self.preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

    @property
    def required_during_scheduling_ignored_during_execution(self):
        r"""Gets the required_during_scheduling_ignored_during_execution of this AffinityType.

        参数描述： 专属池场景下设置强亲和特性 参数约束： key、values、operator必填

        :return: The required_during_scheduling_ignored_during_execution of this AffinityType.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AffinityRule`]
        """
        return self._required_during_scheduling_ignored_during_execution

    @required_during_scheduling_ignored_during_execution.setter
    def required_during_scheduling_ignored_during_execution(self, required_during_scheduling_ignored_during_execution):
        r"""Sets the required_during_scheduling_ignored_during_execution of this AffinityType.

        参数描述： 专属池场景下设置强亲和特性 参数约束： key、values、operator必填

        :param required_during_scheduling_ignored_during_execution: The required_during_scheduling_ignored_during_execution of this AffinityType.
        :type required_during_scheduling_ignored_during_execution: list[:class:`huaweicloudsdkmodelarts.v1.AffinityRule`]
        """
        self._required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution

    @property
    def preferred_during_scheduling_ignored_during_execution(self):
        r"""Gets the preferred_during_scheduling_ignored_during_execution of this AffinityType.

        参数描述： 专属池场景下设置弱亲和特性 参数约束： key、values、operator必填，weight选填

        :return: The preferred_during_scheduling_ignored_during_execution of this AffinityType.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AffinityRule`]
        """
        return self._preferred_during_scheduling_ignored_during_execution

    @preferred_during_scheduling_ignored_during_execution.setter
    def preferred_during_scheduling_ignored_during_execution(self, preferred_during_scheduling_ignored_during_execution):
        r"""Sets the preferred_during_scheduling_ignored_during_execution of this AffinityType.

        参数描述： 专属池场景下设置弱亲和特性 参数约束： key、values、operator必填，weight选填

        :param preferred_during_scheduling_ignored_during_execution: The preferred_during_scheduling_ignored_during_execution of this AffinityType.
        :type preferred_during_scheduling_ignored_during_execution: list[:class:`huaweicloudsdkmodelarts.v1.AffinityRule`]
        """
        self._preferred_during_scheduling_ignored_during_execution = preferred_during_scheduling_ignored_during_execution

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
        if not isinstance(other, AffinityType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
