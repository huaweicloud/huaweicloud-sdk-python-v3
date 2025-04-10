# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationPrimitiveTypeHolderConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_stacks': 'str',
        'failure_mode': 'str'
    }

    attribute_map = {
        'target_stacks': 'target_stacks',
        'failure_mode': 'failure_mode'
    }

    def __init__(self, target_stacks=None, failure_mode=None):
        r"""ConfigurationPrimitiveTypeHolderConfiguration

        The model defined in huaweicloud sdk

        :param target_stacks: 指定私有hook生效的目标资源栈，有效值为NONE或ALL。  NONE：指定此私有hook不会作用于任何资源栈 ALL：指定此私有hook将会应用于账号下的所有资源栈
        :type target_stacks: str
        :param failure_mode: 指定私有hook校验失败后的行为，有效值为FAIL或WARN。  FAIL：指定此私有hook校验失败后资源栈将停止部署，资源栈状态将更新为DEPLOYMENT_FAILED。 WARN：指定此私有hook校验失败后仅通过资源栈事件展示警告消息，但不影响资源栈部署。
        :type failure_mode: str
        """
        
        

        self._target_stacks = None
        self._failure_mode = None
        self.discriminator = None

        if target_stacks is not None:
            self.target_stacks = target_stacks
        if failure_mode is not None:
            self.failure_mode = failure_mode

    @property
    def target_stacks(self):
        r"""Gets the target_stacks of this ConfigurationPrimitiveTypeHolderConfiguration.

        指定私有hook生效的目标资源栈，有效值为NONE或ALL。  NONE：指定此私有hook不会作用于任何资源栈 ALL：指定此私有hook将会应用于账号下的所有资源栈

        :return: The target_stacks of this ConfigurationPrimitiveTypeHolderConfiguration.
        :rtype: str
        """
        return self._target_stacks

    @target_stacks.setter
    def target_stacks(self, target_stacks):
        r"""Sets the target_stacks of this ConfigurationPrimitiveTypeHolderConfiguration.

        指定私有hook生效的目标资源栈，有效值为NONE或ALL。  NONE：指定此私有hook不会作用于任何资源栈 ALL：指定此私有hook将会应用于账号下的所有资源栈

        :param target_stacks: The target_stacks of this ConfigurationPrimitiveTypeHolderConfiguration.
        :type target_stacks: str
        """
        self._target_stacks = target_stacks

    @property
    def failure_mode(self):
        r"""Gets the failure_mode of this ConfigurationPrimitiveTypeHolderConfiguration.

        指定私有hook校验失败后的行为，有效值为FAIL或WARN。  FAIL：指定此私有hook校验失败后资源栈将停止部署，资源栈状态将更新为DEPLOYMENT_FAILED。 WARN：指定此私有hook校验失败后仅通过资源栈事件展示警告消息，但不影响资源栈部署。

        :return: The failure_mode of this ConfigurationPrimitiveTypeHolderConfiguration.
        :rtype: str
        """
        return self._failure_mode

    @failure_mode.setter
    def failure_mode(self, failure_mode):
        r"""Sets the failure_mode of this ConfigurationPrimitiveTypeHolderConfiguration.

        指定私有hook校验失败后的行为，有效值为FAIL或WARN。  FAIL：指定此私有hook校验失败后资源栈将停止部署，资源栈状态将更新为DEPLOYMENT_FAILED。 WARN：指定此私有hook校验失败后仅通过资源栈事件展示警告消息，但不影响资源栈部署。

        :param failure_mode: The failure_mode of this ConfigurationPrimitiveTypeHolderConfiguration.
        :type failure_mode: str
        """
        self._failure_mode = failure_mode

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
        if not isinstance(other, ConfigurationPrimitiveTypeHolderConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
