# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionMasterIdsDtoVersionModelVersionMasterDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_ids': 'list[VersionModelMasterIdsDTO]',
        'modifier': 'str'
    }

    attribute_map = {
        'master_ids': 'masterIds',
        'modifier': 'modifier'
    }

    def __init__(self, master_ids=None, modifier=None):
        r"""VersionMasterIdsDtoVersionModelVersionMasterDTO

        The model defined in huaweicloud sdk

        :param master_ids: **参数解释：**  主对象集合。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type master_ids: list[:class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMasterIdsDTO`]
        :param modifier: **参数解释：**  更新者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type modifier: str
        """
        
        

        self._master_ids = None
        self._modifier = None
        self.discriminator = None

        self.master_ids = master_ids
        if modifier is not None:
            self.modifier = modifier

    @property
    def master_ids(self):
        r"""Gets the master_ids of this VersionMasterIdsDtoVersionModelVersionMasterDTO.

        **参数解释：**  主对象集合。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The master_ids of this VersionMasterIdsDtoVersionModelVersionMasterDTO.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMasterIdsDTO`]
        """
        return self._master_ids

    @master_ids.setter
    def master_ids(self, master_ids):
        r"""Sets the master_ids of this VersionMasterIdsDtoVersionModelVersionMasterDTO.

        **参数解释：**  主对象集合。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param master_ids: The master_ids of this VersionMasterIdsDtoVersionModelVersionMasterDTO.
        :type master_ids: list[:class:`huaweicloudsdkidmeclassicapi.v1.VersionModelMasterIdsDTO`]
        """
        self._master_ids = master_ids

    @property
    def modifier(self):
        r"""Gets the modifier of this VersionMasterIdsDtoVersionModelVersionMasterDTO.

        **参数解释：**  更新者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The modifier of this VersionMasterIdsDtoVersionModelVersionMasterDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this VersionMasterIdsDtoVersionModelVersionMasterDTO.

        **参数解释：**  更新者。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param modifier: The modifier of this VersionMasterIdsDtoVersionModelVersionMasterDTO.
        :type modifier: str
        """
        self._modifier = modifier

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
        if not isinstance(other, VersionMasterIdsDtoVersionModelVersionMasterDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
