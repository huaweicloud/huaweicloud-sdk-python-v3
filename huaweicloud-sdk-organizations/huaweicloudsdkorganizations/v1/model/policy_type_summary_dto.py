# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyTypeSummaryDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, status=None, type=None):
        """PolicyTypeSummaryDto

        The model defined in huaweicloud sdk

        :param status: 与根关联的策略类型状态。要将指定类型的策略绑定到根或该根中的组织单元或帐号，该策略必须在组织中可用，并在该根已启用。enabled：启用；pending_enable：启用中；disabled：禁用；pending_disable：禁用中。
        :type status: str
        :param type: 策略类型的名称，service_control_policy：服务控制策略；tag_policy：标签策略。
        :type type: str
        """
        
        

        self._status = None
        self._type = None
        self.discriminator = None

        self.status = status
        self.type = type

    @property
    def status(self):
        """Gets the status of this PolicyTypeSummaryDto.

        与根关联的策略类型状态。要将指定类型的策略绑定到根或该根中的组织单元或帐号，该策略必须在组织中可用，并在该根已启用。enabled：启用；pending_enable：启用中；disabled：禁用；pending_disable：禁用中。

        :return: The status of this PolicyTypeSummaryDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PolicyTypeSummaryDto.

        与根关联的策略类型状态。要将指定类型的策略绑定到根或该根中的组织单元或帐号，该策略必须在组织中可用，并在该根已启用。enabled：启用；pending_enable：启用中；disabled：禁用；pending_disable：禁用中。

        :param status: The status of this PolicyTypeSummaryDto.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this PolicyTypeSummaryDto.

        策略类型的名称，service_control_policy：服务控制策略；tag_policy：标签策略。

        :return: The type of this PolicyTypeSummaryDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyTypeSummaryDto.

        策略类型的名称，service_control_policy：服务控制策略；tag_policy：标签策略。

        :param type: The type of this PolicyTypeSummaryDto.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, PolicyTypeSummaryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
