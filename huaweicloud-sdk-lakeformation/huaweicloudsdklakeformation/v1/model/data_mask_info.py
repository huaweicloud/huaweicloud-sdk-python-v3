# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataMaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_mask_type': 'str',
        'data_mask': 'str'
    }

    attribute_map = {
        'data_mask_type': 'data_mask_type',
        'data_mask': 'data_mask'
    }

    def __init__(self, data_mask_type=None, data_mask=None):
        r"""DataMaskInfo

        The model defined in huaweicloud sdk

        :param data_mask_type: data mask type：REDACT修订， HASH哈希加密，PARTIAL_MASK部分掩码，NULLIFY用NULL值替换原值，UNMASKED原样显示，DATA_ONLY_SHOW_YEAR仅显示日期字符串的年份部分，CUSTOM自定义脱敏规则。
        :type data_mask_type: str
        :param data_mask: 遮掩规则选项。
        :type data_mask: str
        """
        
        

        self._data_mask_type = None
        self._data_mask = None
        self.discriminator = None

        self.data_mask_type = data_mask_type
        self.data_mask = data_mask

    @property
    def data_mask_type(self):
        r"""Gets the data_mask_type of this DataMaskInfo.

        data mask type：REDACT修订， HASH哈希加密，PARTIAL_MASK部分掩码，NULLIFY用NULL值替换原值，UNMASKED原样显示，DATA_ONLY_SHOW_YEAR仅显示日期字符串的年份部分，CUSTOM自定义脱敏规则。

        :return: The data_mask_type of this DataMaskInfo.
        :rtype: str
        """
        return self._data_mask_type

    @data_mask_type.setter
    def data_mask_type(self, data_mask_type):
        r"""Sets the data_mask_type of this DataMaskInfo.

        data mask type：REDACT修订， HASH哈希加密，PARTIAL_MASK部分掩码，NULLIFY用NULL值替换原值，UNMASKED原样显示，DATA_ONLY_SHOW_YEAR仅显示日期字符串的年份部分，CUSTOM自定义脱敏规则。

        :param data_mask_type: The data_mask_type of this DataMaskInfo.
        :type data_mask_type: str
        """
        self._data_mask_type = data_mask_type

    @property
    def data_mask(self):
        r"""Gets the data_mask of this DataMaskInfo.

        遮掩规则选项。

        :return: The data_mask of this DataMaskInfo.
        :rtype: str
        """
        return self._data_mask

    @data_mask.setter
    def data_mask(self, data_mask):
        r"""Sets the data_mask of this DataMaskInfo.

        遮掩规则选项。

        :param data_mask: The data_mask of this DataMaskInfo.
        :type data_mask: str
        """
        self._data_mask = data_mask

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
        if not isinstance(other, DataMaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
