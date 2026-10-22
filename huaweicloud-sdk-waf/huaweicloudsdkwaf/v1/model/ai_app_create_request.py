# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiAppCreateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'policy_id': 'str',
        'api_sign': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'policy_id': 'policy_id',
        'api_sign': 'api_sign'
    }

    def __init__(self, name=None, description=None, policy_id=None, api_sign=None):
        r"""AiAppCreateRequest

        The model defined in huaweicloud sdk

        :param name: AI应用名称
        :type name: str
        :param description: 应用描述
        :type description: str
        :param policy_id: 要与应用关联的策略ID
        :type policy_id: str
        :param api_sign: API签名
        :type api_sign: str
        """
        
        

        self._name = None
        self._description = None
        self._policy_id = None
        self._api_sign = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if policy_id is not None:
            self.policy_id = policy_id
        if api_sign is not None:
            self.api_sign = api_sign

    @property
    def name(self):
        r"""Gets the name of this AiAppCreateRequest.

        AI应用名称

        :return: The name of this AiAppCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AiAppCreateRequest.

        AI应用名称

        :param name: The name of this AiAppCreateRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AiAppCreateRequest.

        应用描述

        :return: The description of this AiAppCreateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AiAppCreateRequest.

        应用描述

        :param description: The description of this AiAppCreateRequest.
        :type description: str
        """
        self._description = description

    @property
    def policy_id(self):
        r"""Gets the policy_id of this AiAppCreateRequest.

        要与应用关联的策略ID

        :return: The policy_id of this AiAppCreateRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this AiAppCreateRequest.

        要与应用关联的策略ID

        :param policy_id: The policy_id of this AiAppCreateRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def api_sign(self):
        r"""Gets the api_sign of this AiAppCreateRequest.

        API签名

        :return: The api_sign of this AiAppCreateRequest.
        :rtype: str
        """
        return self._api_sign

    @api_sign.setter
    def api_sign(self, api_sign):
        r"""Sets the api_sign of this AiAppCreateRequest.

        API签名

        :param api_sign: The api_sign of this AiAppCreateRequest.
        :type api_sign: str
        """
        self._api_sign = api_sign

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
        if not isinstance(other, AiAppCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
