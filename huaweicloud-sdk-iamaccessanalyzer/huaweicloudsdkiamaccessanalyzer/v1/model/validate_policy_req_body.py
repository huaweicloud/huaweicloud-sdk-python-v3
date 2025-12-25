# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidatePolicyReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_document': 'str',
        'policy_type': 'str',
        'validate_policy_resource_type': 'str'
    }

    attribute_map = {
        'policy_document': 'policy_document',
        'policy_type': 'policy_type',
        'validate_policy_resource_type': 'validate_policy_resource_type'
    }

    def __init__(self, policy_document=None, policy_type=None, validate_policy_resource_type=None):
        r"""ValidatePolicyReqBody

        The model defined in huaweicloud sdk

        :param policy_document: 该策略JSON格式策略文档。
        :type policy_document: str
        :param policy_type: 要校验的策略类型。 - identity_policy：身份策略 - resource_policy：资源策略 - service_control_policy：服务控制策略 - resource_control_policy：资源控制策略 - network_control_policy：网络控制策略 
        :type policy_type: str
        :param validate_policy_resource_type: 要附加到资源策略的资源类型。 - iam:agency： IAM委托 
        :type validate_policy_resource_type: str
        """
        
        

        self._policy_document = None
        self._policy_type = None
        self._validate_policy_resource_type = None
        self.discriminator = None

        self.policy_document = policy_document
        self.policy_type = policy_type
        if validate_policy_resource_type is not None:
            self.validate_policy_resource_type = validate_policy_resource_type

    @property
    def policy_document(self):
        r"""Gets the policy_document of this ValidatePolicyReqBody.

        该策略JSON格式策略文档。

        :return: The policy_document of this ValidatePolicyReqBody.
        :rtype: str
        """
        return self._policy_document

    @policy_document.setter
    def policy_document(self, policy_document):
        r"""Sets the policy_document of this ValidatePolicyReqBody.

        该策略JSON格式策略文档。

        :param policy_document: The policy_document of this ValidatePolicyReqBody.
        :type policy_document: str
        """
        self._policy_document = policy_document

    @property
    def policy_type(self):
        r"""Gets the policy_type of this ValidatePolicyReqBody.

        要校验的策略类型。 - identity_policy：身份策略 - resource_policy：资源策略 - service_control_policy：服务控制策略 - resource_control_policy：资源控制策略 - network_control_policy：网络控制策略 

        :return: The policy_type of this ValidatePolicyReqBody.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this ValidatePolicyReqBody.

        要校验的策略类型。 - identity_policy：身份策略 - resource_policy：资源策略 - service_control_policy：服务控制策略 - resource_control_policy：资源控制策略 - network_control_policy：网络控制策略 

        :param policy_type: The policy_type of this ValidatePolicyReqBody.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def validate_policy_resource_type(self):
        r"""Gets the validate_policy_resource_type of this ValidatePolicyReqBody.

        要附加到资源策略的资源类型。 - iam:agency： IAM委托 

        :return: The validate_policy_resource_type of this ValidatePolicyReqBody.
        :rtype: str
        """
        return self._validate_policy_resource_type

    @validate_policy_resource_type.setter
    def validate_policy_resource_type(self, validate_policy_resource_type):
        r"""Sets the validate_policy_resource_type of this ValidatePolicyReqBody.

        要附加到资源策略的资源类型。 - iam:agency： IAM委托 

        :param validate_policy_resource_type: The validate_policy_resource_type of this ValidatePolicyReqBody.
        :type validate_policy_resource_type: str
        """
        self._validate_policy_resource_type = validate_policy_resource_type

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
        if not isinstance(other, ValidatePolicyReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
