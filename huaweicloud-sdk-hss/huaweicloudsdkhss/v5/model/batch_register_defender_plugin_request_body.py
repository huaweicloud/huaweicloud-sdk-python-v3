# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRegisterDefenderPluginRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'opt': 'str',
        'instance_ids': 'list[str]'
    }

    attribute_map = {
        'opt': 'opt',
        'instance_ids': 'instance_ids'
    }

    def __init__(self, opt=None, instance_ids=None):
        r"""BatchRegisterDefenderPluginRequestBody

        The model defined in huaweicloud sdk

        :param opt: **参数解释**: 操作类型 **约束限制**: 必填 **取值范围**: - install：安装 - uninstall：卸载  **默认取值**: 不涉及 
        :type opt: str
        :param instance_ids: **参数解释**: 智能体实例ID列表 **约束限制**: 必填 **取值范围**: 1-200个实例ID **默认取值**: 不涉及 
        :type instance_ids: list[str]
        """
        
        

        self._opt = None
        self._instance_ids = None
        self.discriminator = None

        self.opt = opt
        self.instance_ids = instance_ids

    @property
    def opt(self):
        r"""Gets the opt of this BatchRegisterDefenderPluginRequestBody.

        **参数解释**: 操作类型 **约束限制**: 必填 **取值范围**: - install：安装 - uninstall：卸载  **默认取值**: 不涉及 

        :return: The opt of this BatchRegisterDefenderPluginRequestBody.
        :rtype: str
        """
        return self._opt

    @opt.setter
    def opt(self, opt):
        r"""Sets the opt of this BatchRegisterDefenderPluginRequestBody.

        **参数解释**: 操作类型 **约束限制**: 必填 **取值范围**: - install：安装 - uninstall：卸载  **默认取值**: 不涉及 

        :param opt: The opt of this BatchRegisterDefenderPluginRequestBody.
        :type opt: str
        """
        self._opt = opt

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this BatchRegisterDefenderPluginRequestBody.

        **参数解释**: 智能体实例ID列表 **约束限制**: 必填 **取值范围**: 1-200个实例ID **默认取值**: 不涉及 

        :return: The instance_ids of this BatchRegisterDefenderPluginRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this BatchRegisterDefenderPluginRequestBody.

        **参数解释**: 智能体实例ID列表 **约束限制**: 必填 **取值范围**: 1-200个实例ID **默认取值**: 不涉及 

        :param instance_ids: The instance_ids of this BatchRegisterDefenderPluginRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

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
        if not isinstance(other, BatchRegisterDefenderPluginRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
