# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddV2XEdgeDataChannelDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'platform_type': 'str',
        'platform_para': 'PlatformPara'
    }

    attribute_map = {
        'platform_type': 'platform_type',
        'platform_para': 'platform_para'
    }

    def __init__(self, platform_type=None, platform_para=None):
        r"""AddV2XEdgeDataChannelDTO

        The model defined in huaweicloud sdk

        :param platform_type: **参数说明**：平台类型。  **取值范围**： - DRIS：华为路网数字化平台 - LITONG：利通 - ZHONGQIYAN：中汽研
        :type platform_type: str
        :param platform_para: 
        :type platform_para: :class:`huaweicloudsdkdris.v1.PlatformPara`
        """
        
        

        self._platform_type = None
        self._platform_para = None
        self.discriminator = None

        self.platform_type = platform_type
        if platform_para is not None:
            self.platform_para = platform_para

    @property
    def platform_type(self):
        r"""Gets the platform_type of this AddV2XEdgeDataChannelDTO.

        **参数说明**：平台类型。  **取值范围**： - DRIS：华为路网数字化平台 - LITONG：利通 - ZHONGQIYAN：中汽研

        :return: The platform_type of this AddV2XEdgeDataChannelDTO.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        r"""Sets the platform_type of this AddV2XEdgeDataChannelDTO.

        **参数说明**：平台类型。  **取值范围**： - DRIS：华为路网数字化平台 - LITONG：利通 - ZHONGQIYAN：中汽研

        :param platform_type: The platform_type of this AddV2XEdgeDataChannelDTO.
        :type platform_type: str
        """
        self._platform_type = platform_type

    @property
    def platform_para(self):
        r"""Gets the platform_para of this AddV2XEdgeDataChannelDTO.

        :return: The platform_para of this AddV2XEdgeDataChannelDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.PlatformPara`
        """
        return self._platform_para

    @platform_para.setter
    def platform_para(self, platform_para):
        r"""Sets the platform_para of this AddV2XEdgeDataChannelDTO.

        :param platform_para: The platform_para of this AddV2XEdgeDataChannelDTO.
        :type platform_para: :class:`huaweicloudsdkdris.v1.PlatformPara`
        """
        self._platform_para = platform_para

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
        if not isinstance(other, AddV2XEdgeDataChannelDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
