# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EsdbCheckRdsConnectionsRequestV3:

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
        'infos': 'list[EsdbCheckRdsConnectionRequestV3]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'infos': 'infos'
    }

    def __init__(self, instance_id=None, infos=None):
        r"""EsdbCheckRdsConnectionsRequestV3

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in09，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param infos: **参数解释**：  rds连通性检查相关信息的集合。  **参数范围**：  不涉及。
        :type infos: list[:class:`huaweicloudsdkddm.v1.EsdbCheckRdsConnectionRequestV3`]
        """
        
        

        self._instance_id = None
        self._infos = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if infos is not None:
            self.infos = infos

    @property
    def instance_id(self):
        r"""Gets the instance_id of this EsdbCheckRdsConnectionsRequestV3.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in09，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this EsdbCheckRdsConnectionsRequestV3.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this EsdbCheckRdsConnectionsRequestV3.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in09，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this EsdbCheckRdsConnectionsRequestV3.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def infos(self):
        r"""Gets the infos of this EsdbCheckRdsConnectionsRequestV3.

        **参数解释**：  rds连通性检查相关信息的集合。  **参数范围**：  不涉及。

        :return: The infos of this EsdbCheckRdsConnectionsRequestV3.
        :rtype: list[:class:`huaweicloudsdkddm.v1.EsdbCheckRdsConnectionRequestV3`]
        """
        return self._infos

    @infos.setter
    def infos(self, infos):
        r"""Sets the infos of this EsdbCheckRdsConnectionsRequestV3.

        **参数解释**：  rds连通性检查相关信息的集合。  **参数范围**：  不涉及。

        :param infos: The infos of this EsdbCheckRdsConnectionsRequestV3.
        :type infos: list[:class:`huaweicloudsdkddm.v1.EsdbCheckRdsConnectionRequestV3`]
        """
        self._infos = infos

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
        if not isinstance(other, EsdbCheckRdsConnectionsRequestV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
