# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAiOpsRequestBody:

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
        'description': 'str',
        'alarm': 'CreateAiOpsRequestBodyAlarm'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'alarm': 'alarm'
    }

    def __init__(self, name=None, description=None, alarm=None):
        r"""CreateAiOpsRequestBody

        The model defined in huaweicloud sdk

        :param name: 检测任务名称。
        :type name: str
        :param description: 检测任务描述。
        :type description: str
        :param alarm: 
        :type alarm: :class:`huaweicloudsdkcss.v1.CreateAiOpsRequestBodyAlarm`
        """
        
        

        self._name = None
        self._description = None
        self._alarm = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if alarm is not None:
            self.alarm = alarm

    @property
    def name(self):
        r"""Gets the name of this CreateAiOpsRequestBody.

        检测任务名称。

        :return: The name of this CreateAiOpsRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAiOpsRequestBody.

        检测任务名称。

        :param name: The name of this CreateAiOpsRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateAiOpsRequestBody.

        检测任务描述。

        :return: The description of this CreateAiOpsRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAiOpsRequestBody.

        检测任务描述。

        :param description: The description of this CreateAiOpsRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def alarm(self):
        r"""Gets the alarm of this CreateAiOpsRequestBody.

        :return: The alarm of this CreateAiOpsRequestBody.
        :rtype: :class:`huaweicloudsdkcss.v1.CreateAiOpsRequestBodyAlarm`
        """
        return self._alarm

    @alarm.setter
    def alarm(self, alarm):
        r"""Sets the alarm of this CreateAiOpsRequestBody.

        :param alarm: The alarm of this CreateAiOpsRequestBody.
        :type alarm: :class:`huaweicloudsdkcss.v1.CreateAiOpsRequestBodyAlarm`
        """
        self._alarm = alarm

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
        if not isinstance(other, CreateAiOpsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
