# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnosisTaskSubmitBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_ids': 'list[str]',
        'type': 'str',
        'extra_properties': 'list[str]'
    }

    attribute_map = {
        'resource_ids': 'resource_ids',
        'type': 'type',
        'extra_properties': 'extra_properties'
    }

    def __init__(self, resource_ids=None, type=None, extra_properties=None):
        r"""DiagnosisTaskSubmitBody

        The model defined in huaweicloud sdk

        :param resource_ids: 待诊断的实例ID
        :type resource_ids: list[str]
        :param type: 被诊断实例的类型
        :type type: str
        :param extra_properties: 适用于RDS、DMS、DCS、ELB等的额外参数（JSON字符串），该数组长度应与提交的实例数组长度对应
        :type extra_properties: list[str]
        """
        
        

        self._resource_ids = None
        self._type = None
        self._extra_properties = None
        self.discriminator = None

        if resource_ids is not None:
            self.resource_ids = resource_ids
        if type is not None:
            self.type = type
        if extra_properties is not None:
            self.extra_properties = extra_properties

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this DiagnosisTaskSubmitBody.

        待诊断的实例ID

        :return: The resource_ids of this DiagnosisTaskSubmitBody.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this DiagnosisTaskSubmitBody.

        待诊断的实例ID

        :param resource_ids: The resource_ids of this DiagnosisTaskSubmitBody.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def type(self):
        r"""Gets the type of this DiagnosisTaskSubmitBody.

        被诊断实例的类型

        :return: The type of this DiagnosisTaskSubmitBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DiagnosisTaskSubmitBody.

        被诊断实例的类型

        :param type: The type of this DiagnosisTaskSubmitBody.
        :type type: str
        """
        self._type = type

    @property
    def extra_properties(self):
        r"""Gets the extra_properties of this DiagnosisTaskSubmitBody.

        适用于RDS、DMS、DCS、ELB等的额外参数（JSON字符串），该数组长度应与提交的实例数组长度对应

        :return: The extra_properties of this DiagnosisTaskSubmitBody.
        :rtype: list[str]
        """
        return self._extra_properties

    @extra_properties.setter
    def extra_properties(self, extra_properties):
        r"""Sets the extra_properties of this DiagnosisTaskSubmitBody.

        适用于RDS、DMS、DCS、ELB等的额外参数（JSON字符串），该数组长度应与提交的实例数组长度对应

        :param extra_properties: The extra_properties of this DiagnosisTaskSubmitBody.
        :type extra_properties: list[str]
        """
        self._extra_properties = extra_properties

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
        if not isinstance(other, DiagnosisTaskSubmitBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
