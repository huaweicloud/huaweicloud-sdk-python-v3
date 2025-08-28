# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RDMParamVOVersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'params': 'VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO',
        'application_id': 'str'
    }

    attribute_map = {
        'params': 'params',
        'application_id': 'applicationId'
    }

    def __init__(self, params=None, application_id=None):
        r"""RDMParamVOVersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO

        The model defined in huaweicloud sdk

        :param params: 
        :type params: :class:`huaweicloudsdkidmeclassicapi.v1.VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO`
        :param application_id: **参数解释**：  应用ID。  **约束限制**：  不涉及。  **取值范围**：  由英文字母和数字组成，且长度为32个字符。  **默认取值**：  不涉及。
        :type application_id: str
        """
        
        

        self._params = None
        self._application_id = None
        self.discriminator = None

        self.params = params
        if application_id is not None:
            self.application_id = application_id

    @property
    def params(self):
        r"""Gets the params of this RDMParamVOVersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.

        :return: The params of this RDMParamVOVersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO`
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this RDMParamVOVersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.

        :param params: The params of this RDMParamVOVersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.
        :type params: :class:`huaweicloudsdkidmeclassicapi.v1.VersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO`
        """
        self._params = params

    @property
    def application_id(self):
        r"""Gets the application_id of this RDMParamVOVersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.

        **参数解释**：  应用ID。  **约束限制**：  不涉及。  **取值范围**：  由英文字母和数字组成，且长度为32个字符。  **默认取值**：  不涉及。

        :return: The application_id of this RDMParamVOVersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this RDMParamVOVersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.

        **参数解释**：  应用ID。  **约束限制**：  不涉及。  **取值范围**：  由英文字母和数字组成，且长度为32个字符。  **默认取值**：  不涉及。

        :param application_id: The application_id of this RDMParamVOVersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO.
        :type application_id: str
        """
        self._application_id = application_id

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
        if not isinstance(other, RDMParamVOVersionUpdateViewDTOMultiViewModelViewUpdateAttrDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
