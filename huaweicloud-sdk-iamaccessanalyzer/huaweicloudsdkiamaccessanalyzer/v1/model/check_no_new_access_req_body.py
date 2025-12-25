# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckNoNewAccessReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'existing_policy_document': 'str',
        'new_policy_document': 'str',
        'policy_type': 'str'
    }

    attribute_map = {
        'existing_policy_document': 'existing_policy_document',
        'new_policy_document': 'new_policy_document',
        'policy_type': 'policy_type'
    }

    def __init__(self, existing_policy_document=None, new_policy_document=None, policy_type=None):
        r"""CheckNoNewAccessReqBody

        The model defined in huaweicloud sdk

        :param existing_policy_document: 该策略JSON格式策略文档。
        :type existing_policy_document: str
        :param new_policy_document: 该策略JSON格式策略文档。
        :type new_policy_document: str
        :param policy_type: 要校验的策略类型。 - identity_policy：身份策略 - agency_trust_policy：委托信任策略 - bucket_policy：桶策略 
        :type policy_type: str
        """
        
        

        self._existing_policy_document = None
        self._new_policy_document = None
        self._policy_type = None
        self.discriminator = None

        self.existing_policy_document = existing_policy_document
        self.new_policy_document = new_policy_document
        self.policy_type = policy_type

    @property
    def existing_policy_document(self):
        r"""Gets the existing_policy_document of this CheckNoNewAccessReqBody.

        该策略JSON格式策略文档。

        :return: The existing_policy_document of this CheckNoNewAccessReqBody.
        :rtype: str
        """
        return self._existing_policy_document

    @existing_policy_document.setter
    def existing_policy_document(self, existing_policy_document):
        r"""Sets the existing_policy_document of this CheckNoNewAccessReqBody.

        该策略JSON格式策略文档。

        :param existing_policy_document: The existing_policy_document of this CheckNoNewAccessReqBody.
        :type existing_policy_document: str
        """
        self._existing_policy_document = existing_policy_document

    @property
    def new_policy_document(self):
        r"""Gets the new_policy_document of this CheckNoNewAccessReqBody.

        该策略JSON格式策略文档。

        :return: The new_policy_document of this CheckNoNewAccessReqBody.
        :rtype: str
        """
        return self._new_policy_document

    @new_policy_document.setter
    def new_policy_document(self, new_policy_document):
        r"""Sets the new_policy_document of this CheckNoNewAccessReqBody.

        该策略JSON格式策略文档。

        :param new_policy_document: The new_policy_document of this CheckNoNewAccessReqBody.
        :type new_policy_document: str
        """
        self._new_policy_document = new_policy_document

    @property
    def policy_type(self):
        r"""Gets the policy_type of this CheckNoNewAccessReqBody.

        要校验的策略类型。 - identity_policy：身份策略 - agency_trust_policy：委托信任策略 - bucket_policy：桶策略 

        :return: The policy_type of this CheckNoNewAccessReqBody.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this CheckNoNewAccessReqBody.

        要校验的策略类型。 - identity_policy：身份策略 - agency_trust_policy：委托信任策略 - bucket_policy：桶策略 

        :param policy_type: The policy_type of this CheckNoNewAccessReqBody.
        :type policy_type: str
        """
        self._policy_type = policy_type

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
        if not isinstance(other, CheckNoNewAccessReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
