# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TenantV2Agreement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agreement_name': 'str',
        'version': 'str',
        'create_time': 'datetime'
    }

    attribute_map = {
        'agreement_name': 'agreement_name',
        'version': 'version',
        'create_time': 'create_time'
    }

    def __init__(self, agreement_name=None, version=None, create_time=None):
        r"""TenantV2Agreement

        The model defined in huaweicloud sdk

        :param agreement_name: **参数解释**：协议名称。 **取值范围**：长度为1~128的英文字母、数字、下划线和中划线的组合。
        :type agreement_name: str
        :param version: **参数解释**：协议版本号。 **取值范围**：长度为1~128的英文字母、数字、下划线、中划线和小数点的组合。
        :type version: str
        :param create_time: **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type create_time: datetime
        """
        
        

        self._agreement_name = None
        self._version = None
        self._create_time = None
        self.discriminator = None

        if agreement_name is not None:
            self.agreement_name = agreement_name
        if version is not None:
            self.version = version
        if create_time is not None:
            self.create_time = create_time

    @property
    def agreement_name(self):
        r"""Gets the agreement_name of this TenantV2Agreement.

        **参数解释**：协议名称。 **取值范围**：长度为1~128的英文字母、数字、下划线和中划线的组合。

        :return: The agreement_name of this TenantV2Agreement.
        :rtype: str
        """
        return self._agreement_name

    @agreement_name.setter
    def agreement_name(self, agreement_name):
        r"""Sets the agreement_name of this TenantV2Agreement.

        **参数解释**：协议名称。 **取值范围**：长度为1~128的英文字母、数字、下划线和中划线的组合。

        :param agreement_name: The agreement_name of this TenantV2Agreement.
        :type agreement_name: str
        """
        self._agreement_name = agreement_name

    @property
    def version(self):
        r"""Gets the version of this TenantV2Agreement.

        **参数解释**：协议版本号。 **取值范围**：长度为1~128的英文字母、数字、下划线、中划线和小数点的组合。

        :return: The version of this TenantV2Agreement.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this TenantV2Agreement.

        **参数解释**：协议版本号。 **取值范围**：长度为1~128的英文字母、数字、下划线、中划线和小数点的组合。

        :param version: The version of this TenantV2Agreement.
        :type version: str
        """
        self._version = version

    @property
    def create_time(self):
        r"""Gets the create_time of this TenantV2Agreement.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The create_time of this TenantV2Agreement.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TenantV2Agreement.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param create_time: The create_time of this TenantV2Agreement.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, TenantV2Agreement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
