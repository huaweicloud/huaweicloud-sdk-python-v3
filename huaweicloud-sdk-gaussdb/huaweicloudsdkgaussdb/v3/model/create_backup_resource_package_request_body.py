# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBackupResourcePackageRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'num': 'int',
        'charge_info': 'TaurusDbChargeInfo'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'num': 'num',
        'charge_info': 'charge_info'
    }

    def __init__(self, spec_code=None, num=None, charge_info=None):
        r"""CreateBackupResourcePackageRequestBody

        The model defined in huaweicloud sdk

        :param spec_code: **参数解释**：  备份资源包规格码。  **约束限制**：  不涉及。  **取值范围**：  备份资源包规格码可根据[查询备份资源包规格](https://support.huaweicloud.com/api-taurusdb/ShowBackupResourcePackageFlavors.html)接口获取。  **默认取值**：  不涉及。
        :type spec_code: str
        :param num: **参数解释**：  备份资源包数量。  **约束限制**：  不涉及。  **取值范围**：  1-10。  **默认取值**：  不涉及。
        :type num: int
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkgaussdb.v3.TaurusDbChargeInfo`
        """
        
        

        self._spec_code = None
        self._num = None
        self._charge_info = None
        self.discriminator = None

        self.spec_code = spec_code
        self.num = num
        self.charge_info = charge_info

    @property
    def spec_code(self):
        r"""Gets the spec_code of this CreateBackupResourcePackageRequestBody.

        **参数解释**：  备份资源包规格码。  **约束限制**：  不涉及。  **取值范围**：  备份资源包规格码可根据[查询备份资源包规格](https://support.huaweicloud.com/api-taurusdb/ShowBackupResourcePackageFlavors.html)接口获取。  **默认取值**：  不涉及。

        :return: The spec_code of this CreateBackupResourcePackageRequestBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this CreateBackupResourcePackageRequestBody.

        **参数解释**：  备份资源包规格码。  **约束限制**：  不涉及。  **取值范围**：  备份资源包规格码可根据[查询备份资源包规格](https://support.huaweicloud.com/api-taurusdb/ShowBackupResourcePackageFlavors.html)接口获取。  **默认取值**：  不涉及。

        :param spec_code: The spec_code of this CreateBackupResourcePackageRequestBody.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def num(self):
        r"""Gets the num of this CreateBackupResourcePackageRequestBody.

        **参数解释**：  备份资源包数量。  **约束限制**：  不涉及。  **取值范围**：  1-10。  **默认取值**：  不涉及。

        :return: The num of this CreateBackupResourcePackageRequestBody.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this CreateBackupResourcePackageRequestBody.

        **参数解释**：  备份资源包数量。  **约束限制**：  不涉及。  **取值范围**：  1-10。  **默认取值**：  不涉及。

        :param num: The num of this CreateBackupResourcePackageRequestBody.
        :type num: int
        """
        self._num = num

    @property
    def charge_info(self):
        r"""Gets the charge_info of this CreateBackupResourcePackageRequestBody.

        :return: The charge_info of this CreateBackupResourcePackageRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.TaurusDbChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this CreateBackupResourcePackageRequestBody.

        :param charge_info: The charge_info of this CreateBackupResourcePackageRequestBody.
        :type charge_info: :class:`huaweicloudsdkgaussdb.v3.TaurusDbChargeInfo`
        """
        self._charge_info = charge_info

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
        if not isinstance(other, CreateBackupResourcePackageRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
