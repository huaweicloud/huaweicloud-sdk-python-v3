# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationCopyReqV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'copy_para': 'ParaGroupCopy',
        'source_id': 'str'
    }

    attribute_map = {
        'copy_para': 'copy_para',
        'source_id': 'source_id'
    }

    def __init__(self, copy_para=None, source_id=None):
        r"""ConfigurationCopyReqV3

        The model defined in huaweicloud sdk

        :param copy_para: 
        :type copy_para: :class:`huaweicloudsdkddm.v1.ParaGroupCopy`
        :param source_id: **参数解释**：  目标参数组ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。
        :type source_id: str
        """
        
        

        self._copy_para = None
        self._source_id = None
        self.discriminator = None

        if copy_para is not None:
            self.copy_para = copy_para
        if source_id is not None:
            self.source_id = source_id

    @property
    def copy_para(self):
        r"""Gets the copy_para of this ConfigurationCopyReqV3.

        :return: The copy_para of this ConfigurationCopyReqV3.
        :rtype: :class:`huaweicloudsdkddm.v1.ParaGroupCopy`
        """
        return self._copy_para

    @copy_para.setter
    def copy_para(self, copy_para):
        r"""Sets the copy_para of this ConfigurationCopyReqV3.

        :param copy_para: The copy_para of this ConfigurationCopyReqV3.
        :type copy_para: :class:`huaweicloudsdkddm.v1.ParaGroupCopy`
        """
        self._copy_para = copy_para

    @property
    def source_id(self):
        r"""Gets the source_id of this ConfigurationCopyReqV3.

        **参数解释**：  目标参数组ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :return: The source_id of this ConfigurationCopyReqV3.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this ConfigurationCopyReqV3.

        **参数解释**：  目标参数组ID。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :param source_id: The source_id of this ConfigurationCopyReqV3.
        :type source_id: str
        """
        self._source_id = source_id

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
        if not isinstance(other, ConfigurationCopyReqV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
