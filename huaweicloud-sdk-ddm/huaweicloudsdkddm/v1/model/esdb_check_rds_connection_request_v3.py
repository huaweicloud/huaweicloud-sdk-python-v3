# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EsdbCheckRdsConnectionRequestV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint': 'str',
        'username': 'str',
        'password': 'str',
        'rds_instance_id': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'username': 'username',
        'password': 'password',
        'rds_instance_id': 'rds_instance_id'
    }

    def __init__(self, endpoint=None, username=None, password=None, rds_instance_id=None):
        r"""EsdbCheckRdsConnectionRequestV3

        The model defined in huaweicloud sdk

        :param endpoint: **参数解释**：  内网地址以及端口号。  格式为xx.xx.xx.xx:xx。  **参数范围**：  不涉及。
        :type endpoint: str
        :param username: **参数解释**：  实例账号名称。  **参数范围**：  不涉及。
        :type username: str
        :param password: **参数解释**：  实例账号密码。  **约束限制**：  - 至少包含三种字符组合：小写字母、大写字母、数字、特殊字符 ~ ! @ # % ^ * - _ + ? - 不能使用简单、强度不够、容易被猜测的密码。 - 不能与账号名称或者倒序的账号名称相同。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type password: str
        :param rds_instance_id: **参数解释**：  rds实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in01，长度为36个字符。  **默认取值**：  不涉及。
        :type rds_instance_id: str
        """
        
        

        self._endpoint = None
        self._username = None
        self._password = None
        self._rds_instance_id = None
        self.discriminator = None

        self.endpoint = endpoint
        self.username = username
        self.password = password
        self.rds_instance_id = rds_instance_id

    @property
    def endpoint(self):
        r"""Gets the endpoint of this EsdbCheckRdsConnectionRequestV3.

        **参数解释**：  内网地址以及端口号。  格式为xx.xx.xx.xx:xx。  **参数范围**：  不涉及。

        :return: The endpoint of this EsdbCheckRdsConnectionRequestV3.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this EsdbCheckRdsConnectionRequestV3.

        **参数解释**：  内网地址以及端口号。  格式为xx.xx.xx.xx:xx。  **参数范围**：  不涉及。

        :param endpoint: The endpoint of this EsdbCheckRdsConnectionRequestV3.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def username(self):
        r"""Gets the username of this EsdbCheckRdsConnectionRequestV3.

        **参数解释**：  实例账号名称。  **参数范围**：  不涉及。

        :return: The username of this EsdbCheckRdsConnectionRequestV3.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this EsdbCheckRdsConnectionRequestV3.

        **参数解释**：  实例账号名称。  **参数范围**：  不涉及。

        :param username: The username of this EsdbCheckRdsConnectionRequestV3.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        r"""Gets the password of this EsdbCheckRdsConnectionRequestV3.

        **参数解释**：  实例账号密码。  **约束限制**：  - 至少包含三种字符组合：小写字母、大写字母、数字、特殊字符 ~ ! @ # % ^ * - _ + ? - 不能使用简单、强度不够、容易被猜测的密码。 - 不能与账号名称或者倒序的账号名称相同。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The password of this EsdbCheckRdsConnectionRequestV3.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this EsdbCheckRdsConnectionRequestV3.

        **参数解释**：  实例账号密码。  **约束限制**：  - 至少包含三种字符组合：小写字母、大写字母、数字、特殊字符 ~ ! @ # % ^ * - _ + ? - 不能使用简单、强度不够、容易被猜测的密码。 - 不能与账号名称或者倒序的账号名称相同。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param password: The password of this EsdbCheckRdsConnectionRequestV3.
        :type password: str
        """
        self._password = password

    @property
    def rds_instance_id(self):
        r"""Gets the rds_instance_id of this EsdbCheckRdsConnectionRequestV3.

        **参数解释**：  rds实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in01，长度为36个字符。  **默认取值**：  不涉及。

        :return: The rds_instance_id of this EsdbCheckRdsConnectionRequestV3.
        :rtype: str
        """
        return self._rds_instance_id

    @rds_instance_id.setter
    def rds_instance_id(self, rds_instance_id):
        r"""Sets the rds_instance_id of this EsdbCheckRdsConnectionRequestV3.

        **参数解释**：  rds实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in01，长度为36个字符。  **默认取值**：  不涉及。

        :param rds_instance_id: The rds_instance_id of this EsdbCheckRdsConnectionRequestV3.
        :type rds_instance_id: str
        """
        self._rds_instance_id = rds_instance_id

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
        if not isinstance(other, EsdbCheckRdsConnectionRequestV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
