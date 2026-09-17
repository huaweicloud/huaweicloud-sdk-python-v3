# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InPlaceRollingUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_defined_step': 'int',
        'scope': 'str'
    }

    attribute_map = {
        'user_defined_step': 'userDefinedStep',
        'scope': 'scope'
    }

    def __init__(self, user_defined_step=None, scope=None):
        r"""InPlaceRollingUpdate

        The model defined in huaweicloud sdk

        :param user_defined_step: **参数解释：** 每批升级的最大节点数量。升级时节点池之间会依次进行升级。节点池内的节点分批升级，第一批升级1个节点，第二批升级2个节点，后续每批升级节点数以2的幂数增加，直到达到您设置的每批最大升级节点数，并会持续作用在下一个节点池中 **约束限制：** 不涉及 **取值范围：** [1-120] **默认取值：** 不涉及
        :type user_defined_step: int
        :param scope: **参数解释：** 节点升级批次作用域 **约束限制：** 不涉及 **取值范围：** - Cluster：节点升级批次配置应用到整个集群，整个升级过程不重置升级批次 - NodePool：节点升级批次配置应用到节点池，升级每个节点池都会重置升级批次  **默认取值：** Cluster
        :type scope: str
        """
        
        

        self._user_defined_step = None
        self._scope = None
        self.discriminator = None

        self.user_defined_step = user_defined_step
        if scope is not None:
            self.scope = scope

    @property
    def user_defined_step(self):
        r"""Gets the user_defined_step of this InPlaceRollingUpdate.

        **参数解释：** 每批升级的最大节点数量。升级时节点池之间会依次进行升级。节点池内的节点分批升级，第一批升级1个节点，第二批升级2个节点，后续每批升级节点数以2的幂数增加，直到达到您设置的每批最大升级节点数，并会持续作用在下一个节点池中 **约束限制：** 不涉及 **取值范围：** [1-120] **默认取值：** 不涉及

        :return: The user_defined_step of this InPlaceRollingUpdate.
        :rtype: int
        """
        return self._user_defined_step

    @user_defined_step.setter
    def user_defined_step(self, user_defined_step):
        r"""Sets the user_defined_step of this InPlaceRollingUpdate.

        **参数解释：** 每批升级的最大节点数量。升级时节点池之间会依次进行升级。节点池内的节点分批升级，第一批升级1个节点，第二批升级2个节点，后续每批升级节点数以2的幂数增加，直到达到您设置的每批最大升级节点数，并会持续作用在下一个节点池中 **约束限制：** 不涉及 **取值范围：** [1-120] **默认取值：** 不涉及

        :param user_defined_step: The user_defined_step of this InPlaceRollingUpdate.
        :type user_defined_step: int
        """
        self._user_defined_step = user_defined_step

    @property
    def scope(self):
        r"""Gets the scope of this InPlaceRollingUpdate.

        **参数解释：** 节点升级批次作用域 **约束限制：** 不涉及 **取值范围：** - Cluster：节点升级批次配置应用到整个集群，整个升级过程不重置升级批次 - NodePool：节点升级批次配置应用到节点池，升级每个节点池都会重置升级批次  **默认取值：** Cluster

        :return: The scope of this InPlaceRollingUpdate.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this InPlaceRollingUpdate.

        **参数解释：** 节点升级批次作用域 **约束限制：** 不涉及 **取值范围：** - Cluster：节点升级批次配置应用到整个集群，整个升级过程不重置升级批次 - NodePool：节点升级批次配置应用到节点池，升级每个节点池都会重置升级批次  **默认取值：** Cluster

        :param scope: The scope of this InPlaceRollingUpdate.
        :type scope: str
        """
        self._scope = scope

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
        if not isinstance(other, InPlaceRollingUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
