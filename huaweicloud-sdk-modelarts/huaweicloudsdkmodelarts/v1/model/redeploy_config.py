# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedeployConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'auto_flow': 'str'
    }

    attribute_map = {
        'type': 'type',
        'auto_flow': 'autoFlow'
    }

    def __init__(self, type=None, auto_flow=None):
        r"""RedeployConfig

        The model defined in huaweicloud sdk

        :param type: 节点的重部署类型。若节点状态为不可用，将无法进行SOFT模式，只能进行HARD模式，HARD模式包含节点重置操作，会导致本地盘及云盘上的全部数据丢失，请谨慎操作
        :type type: str
        :param auto_flow: 静默修复开关。开启autoFlow开关时，如重部署失败系统将自动流转至\&quot;系统维护\&quot;或发起\&quot;二次重部署\&quot;，并产生新的计划事件，该过程自动授权，无需二次授权
        :type auto_flow: str
        """
        
        

        self._type = None
        self._auto_flow = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if auto_flow is not None:
            self.auto_flow = auto_flow

    @property
    def type(self):
        r"""Gets the type of this RedeployConfig.

        节点的重部署类型。若节点状态为不可用，将无法进行SOFT模式，只能进行HARD模式，HARD模式包含节点重置操作，会导致本地盘及云盘上的全部数据丢失，请谨慎操作

        :return: The type of this RedeployConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RedeployConfig.

        节点的重部署类型。若节点状态为不可用，将无法进行SOFT模式，只能进行HARD模式，HARD模式包含节点重置操作，会导致本地盘及云盘上的全部数据丢失，请谨慎操作

        :param type: The type of this RedeployConfig.
        :type type: str
        """
        self._type = type

    @property
    def auto_flow(self):
        r"""Gets the auto_flow of this RedeployConfig.

        静默修复开关。开启autoFlow开关时，如重部署失败系统将自动流转至\"系统维护\"或发起\"二次重部署\"，并产生新的计划事件，该过程自动授权，无需二次授权

        :return: The auto_flow of this RedeployConfig.
        :rtype: str
        """
        return self._auto_flow

    @auto_flow.setter
    def auto_flow(self, auto_flow):
        r"""Sets the auto_flow of this RedeployConfig.

        静默修复开关。开启autoFlow开关时，如重部署失败系统将自动流转至\"系统维护\"或发起\"二次重部署\"，并产生新的计划事件，该过程自动授权，无需二次授权

        :param auto_flow: The auto_flow of this RedeployConfig.
        :type auto_flow: str
        """
        self._auto_flow = auto_flow

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
        if not isinstance(other, RedeployConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
