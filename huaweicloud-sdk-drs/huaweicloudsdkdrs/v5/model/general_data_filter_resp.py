# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeneralDataFilterResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_filter_condition': 'str',
        'target_filter_condition': 'str',
        'condition_separated': 'str'
    }

    attribute_map = {
        'source_filter_condition': 'source_filter_condition',
        'target_filter_condition': 'target_filter_condition',
        'condition_separated': 'condition_separated'
    }

    def __init__(self, source_filter_condition=None, target_filter_condition=None, condition_separated=None):
        r"""GeneralDataFilterResp

        The model defined in huaweicloud sdk

        :param source_filter_condition: 源数据库的过滤条件SQL表达式。
        :type source_filter_condition: str
        :param target_filter_condition: 目标数据库的过滤条件SQL表达式。
        :type target_filter_condition: str
        :param condition_separated: 标记源库和目标库过滤条件是否分开配置。
        :type condition_separated: str
        """
        
        

        self._source_filter_condition = None
        self._target_filter_condition = None
        self._condition_separated = None
        self.discriminator = None

        if source_filter_condition is not None:
            self.source_filter_condition = source_filter_condition
        if target_filter_condition is not None:
            self.target_filter_condition = target_filter_condition
        if condition_separated is not None:
            self.condition_separated = condition_separated

    @property
    def source_filter_condition(self):
        r"""Gets the source_filter_condition of this GeneralDataFilterResp.

        源数据库的过滤条件SQL表达式。

        :return: The source_filter_condition of this GeneralDataFilterResp.
        :rtype: str
        """
        return self._source_filter_condition

    @source_filter_condition.setter
    def source_filter_condition(self, source_filter_condition):
        r"""Sets the source_filter_condition of this GeneralDataFilterResp.

        源数据库的过滤条件SQL表达式。

        :param source_filter_condition: The source_filter_condition of this GeneralDataFilterResp.
        :type source_filter_condition: str
        """
        self._source_filter_condition = source_filter_condition

    @property
    def target_filter_condition(self):
        r"""Gets the target_filter_condition of this GeneralDataFilterResp.

        目标数据库的过滤条件SQL表达式。

        :return: The target_filter_condition of this GeneralDataFilterResp.
        :rtype: str
        """
        return self._target_filter_condition

    @target_filter_condition.setter
    def target_filter_condition(self, target_filter_condition):
        r"""Sets the target_filter_condition of this GeneralDataFilterResp.

        目标数据库的过滤条件SQL表达式。

        :param target_filter_condition: The target_filter_condition of this GeneralDataFilterResp.
        :type target_filter_condition: str
        """
        self._target_filter_condition = target_filter_condition

    @property
    def condition_separated(self):
        r"""Gets the condition_separated of this GeneralDataFilterResp.

        标记源库和目标库过滤条件是否分开配置。

        :return: The condition_separated of this GeneralDataFilterResp.
        :rtype: str
        """
        return self._condition_separated

    @condition_separated.setter
    def condition_separated(self, condition_separated):
        r"""Sets the condition_separated of this GeneralDataFilterResp.

        标记源库和目标库过滤条件是否分开配置。

        :param condition_separated: The condition_separated of this GeneralDataFilterResp.
        :type condition_separated: str
        """
        self._condition_separated = condition_separated

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
        if not isinstance(other, GeneralDataFilterResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
