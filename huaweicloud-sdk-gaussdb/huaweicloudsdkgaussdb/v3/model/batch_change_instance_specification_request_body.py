# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchChangeInstanceSpecificationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'spec_code': 'str',
        'is_auto_pay': 'str'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'spec_code': 'spec_code',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, instance_ids=None, spec_code=None, is_auto_pay=None):
        r"""BatchChangeInstanceSpecificationRequestBody

        The model defined in huaweicloud sdk

        :param instance_ids: **参数解释**：  批量规格变更的实例ID列表。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  实例ID只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_ids: list[str]
        :param spec_code: **参数解释**：  规格码。  获取方法请参见[查询数据库规格](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlFlavors.html)中的响应参数\&quot;spec_code\&quot;。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type spec_code: str
        :param is_auto_pay: **参数解释**：  批量变更包年/包月实例规格时可指定，表示是否自动从客户的账户中支付。  **约束限制**：  不涉及。  **取值范围**： - true：自动支付，默认该方式。 - false：手动支付。  **默认取值**：  true。
        :type is_auto_pay: str
        """
        
        

        self._instance_ids = None
        self._spec_code = None
        self._is_auto_pay = None
        self.discriminator = None

        self.instance_ids = instance_ids
        self.spec_code = spec_code
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this BatchChangeInstanceSpecificationRequestBody.

        **参数解释**：  批量规格变更的实例ID列表。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  实例ID只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_ids of this BatchChangeInstanceSpecificationRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this BatchChangeInstanceSpecificationRequestBody.

        **参数解释**：  批量规格变更的实例ID列表。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  实例ID只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_ids: The instance_ids of this BatchChangeInstanceSpecificationRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def spec_code(self):
        r"""Gets the spec_code of this BatchChangeInstanceSpecificationRequestBody.

        **参数解释**：  规格码。  获取方法请参见[查询数据库规格](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlFlavors.html)中的响应参数\"spec_code\"。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The spec_code of this BatchChangeInstanceSpecificationRequestBody.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this BatchChangeInstanceSpecificationRequestBody.

        **参数解释**：  规格码。  获取方法请参见[查询数据库规格](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlFlavors.html)中的响应参数\"spec_code\"。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param spec_code: The spec_code of this BatchChangeInstanceSpecificationRequestBody.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this BatchChangeInstanceSpecificationRequestBody.

        **参数解释**：  批量变更包年/包月实例规格时可指定，表示是否自动从客户的账户中支付。  **约束限制**：  不涉及。  **取值范围**： - true：自动支付，默认该方式。 - false：手动支付。  **默认取值**：  true。

        :return: The is_auto_pay of this BatchChangeInstanceSpecificationRequestBody.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this BatchChangeInstanceSpecificationRequestBody.

        **参数解释**：  批量变更包年/包月实例规格时可指定，表示是否自动从客户的账户中支付。  **约束限制**：  不涉及。  **取值范围**： - true：自动支付，默认该方式。 - false：手动支付。  **默认取值**：  true。

        :param is_auto_pay: The is_auto_pay of this BatchChangeInstanceSpecificationRequestBody.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, BatchChangeInstanceSpecificationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
