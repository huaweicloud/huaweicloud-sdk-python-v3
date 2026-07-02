# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBackupResourcePackageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'spec_code': 'str',
        'num': 'int',
        'period_type': 'str',
        'period_num': 'int'
    }

    attribute_map = {
        'order_id': 'order_id',
        'spec_code': 'spec_code',
        'num': 'num',
        'period_type': 'period_type',
        'period_num': 'period_num'
    }

    def __init__(self, order_id=None, spec_code=None, num=None, period_type=None, period_num=None):
        r"""CreateBackupResourcePackageResponse

        The model defined in huaweicloud sdk

        :param order_id: **参数解释**：  创建备份资源包订单ID。  **取值范围**：  不涉及。
        :type order_id: str
        :param spec_code: **参数解释**：  备份资源包规格码。  **取值范围**：  不涉及。
        :type spec_code: str
        :param num: **参数解释**：  备份资源包数量。  **取值范围**：  1-10。
        :type num: int
        :param period_type: **参数解释**：  订购周期类型。  **取值范围**：  - month：包月。 - year：包年。
        :type period_type: str
        :param period_num: **参数解释**：  订购时间长度。  **取值范围**：  - \&quot;period_type\&quot;为\&quot;month\&quot;时，取值为1~9。 - \&quot;period_type\&quot;为\&quot;year\&quot;时，取值为1~3。
        :type period_num: int
        """
        
        super().__init__()

        self._order_id = None
        self._spec_code = None
        self._num = None
        self._period_type = None
        self._period_num = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if spec_code is not None:
            self.spec_code = spec_code
        if num is not None:
            self.num = num
        if period_type is not None:
            self.period_type = period_type
        if period_num is not None:
            self.period_num = period_num

    @property
    def order_id(self):
        r"""Gets the order_id of this CreateBackupResourcePackageResponse.

        **参数解释**：  创建备份资源包订单ID。  **取值范围**：  不涉及。

        :return: The order_id of this CreateBackupResourcePackageResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreateBackupResourcePackageResponse.

        **参数解释**：  创建备份资源包订单ID。  **取值范围**：  不涉及。

        :param order_id: The order_id of this CreateBackupResourcePackageResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def spec_code(self):
        r"""Gets the spec_code of this CreateBackupResourcePackageResponse.

        **参数解释**：  备份资源包规格码。  **取值范围**：  不涉及。

        :return: The spec_code of this CreateBackupResourcePackageResponse.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this CreateBackupResourcePackageResponse.

        **参数解释**：  备份资源包规格码。  **取值范围**：  不涉及。

        :param spec_code: The spec_code of this CreateBackupResourcePackageResponse.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def num(self):
        r"""Gets the num of this CreateBackupResourcePackageResponse.

        **参数解释**：  备份资源包数量。  **取值范围**：  1-10。

        :return: The num of this CreateBackupResourcePackageResponse.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this CreateBackupResourcePackageResponse.

        **参数解释**：  备份资源包数量。  **取值范围**：  1-10。

        :param num: The num of this CreateBackupResourcePackageResponse.
        :type num: int
        """
        self._num = num

    @property
    def period_type(self):
        r"""Gets the period_type of this CreateBackupResourcePackageResponse.

        **参数解释**：  订购周期类型。  **取值范围**：  - month：包月。 - year：包年。

        :return: The period_type of this CreateBackupResourcePackageResponse.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this CreateBackupResourcePackageResponse.

        **参数解释**：  订购周期类型。  **取值范围**：  - month：包月。 - year：包年。

        :param period_type: The period_type of this CreateBackupResourcePackageResponse.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def period_num(self):
        r"""Gets the period_num of this CreateBackupResourcePackageResponse.

        **参数解释**：  订购时间长度。  **取值范围**：  - \"period_type\"为\"month\"时，取值为1~9。 - \"period_type\"为\"year\"时，取值为1~3。

        :return: The period_num of this CreateBackupResourcePackageResponse.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        r"""Sets the period_num of this CreateBackupResourcePackageResponse.

        **参数解释**：  订购时间长度。  **取值范围**：  - \"period_type\"为\"month\"时，取值为1~9。 - \"period_type\"为\"year\"时，取值为1~3。

        :param period_num: The period_num of this CreateBackupResourcePackageResponse.
        :type period_num: int
        """
        self._period_num = period_num

    def to_dict(self):
        import warnings
        warnings.warn("CreateBackupResourcePackageResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateBackupResourcePackageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
