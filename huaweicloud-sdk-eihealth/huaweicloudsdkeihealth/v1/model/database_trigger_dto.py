# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseTriggerDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'judge_mode': 'TriggerJudgeMode',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'judge_mode': 'judge_mode',
        'value': 'value'
    }

    def __init__(self, name=None, judge_mode=None, value=None):
        r"""DatabaseTriggerDto

        The model defined in huaweicloud sdk

        :param name: 触发器的列名，取值范围：[1,63]
        :type name: str
        :param judge_mode: 
        :type judge_mode: :class:`huaweicloudsdkeihealth.v1.TriggerJudgeMode`
        :param value: 触发器的取值，取值范围：[1,128]
        :type value: str
        """
        
        

        self._name = None
        self._judge_mode = None
        self._value = None
        self.discriminator = None

        self.name = name
        self.judge_mode = judge_mode
        self.value = value

    @property
    def name(self):
        r"""Gets the name of this DatabaseTriggerDto.

        触发器的列名，取值范围：[1,63]

        :return: The name of this DatabaseTriggerDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DatabaseTriggerDto.

        触发器的列名，取值范围：[1,63]

        :param name: The name of this DatabaseTriggerDto.
        :type name: str
        """
        self._name = name

    @property
    def judge_mode(self):
        r"""Gets the judge_mode of this DatabaseTriggerDto.

        :return: The judge_mode of this DatabaseTriggerDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TriggerJudgeMode`
        """
        return self._judge_mode

    @judge_mode.setter
    def judge_mode(self, judge_mode):
        r"""Sets the judge_mode of this DatabaseTriggerDto.

        :param judge_mode: The judge_mode of this DatabaseTriggerDto.
        :type judge_mode: :class:`huaweicloudsdkeihealth.v1.TriggerJudgeMode`
        """
        self._judge_mode = judge_mode

    @property
    def value(self):
        r"""Gets the value of this DatabaseTriggerDto.

        触发器的取值，取值范围：[1,128]

        :return: The value of this DatabaseTriggerDto.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this DatabaseTriggerDto.

        触发器的取值，取值范围：[1,128]

        :param value: The value of this DatabaseTriggerDto.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, DatabaseTriggerDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
