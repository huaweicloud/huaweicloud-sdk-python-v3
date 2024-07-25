# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailsOfOrchestrationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'orchestration_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'orchestration_id': 'orchestration_id'
    }

    def __init__(self, instance_id=None, orchestration_id=None):
        """ShowDetailsOfOrchestrationRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param orchestration_id: 编排规则编号
        :type orchestration_id: str
        """
        
        

        self._instance_id = None
        self._orchestration_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.orchestration_id = orchestration_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowDetailsOfOrchestrationRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ShowDetailsOfOrchestrationRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowDetailsOfOrchestrationRequest.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ShowDetailsOfOrchestrationRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def orchestration_id(self):
        """Gets the orchestration_id of this ShowDetailsOfOrchestrationRequest.

        编排规则编号

        :return: The orchestration_id of this ShowDetailsOfOrchestrationRequest.
        :rtype: str
        """
        return self._orchestration_id

    @orchestration_id.setter
    def orchestration_id(self, orchestration_id):
        """Sets the orchestration_id of this ShowDetailsOfOrchestrationRequest.

        编排规则编号

        :param orchestration_id: The orchestration_id of this ShowDetailsOfOrchestrationRequest.
        :type orchestration_id: str
        """
        self._orchestration_id = orchestration_id

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
        if not isinstance(other, ShowDetailsOfOrchestrationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
