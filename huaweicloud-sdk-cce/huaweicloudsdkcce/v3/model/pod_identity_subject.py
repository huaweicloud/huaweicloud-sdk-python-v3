# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PodIdentitySubject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'service_account': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'service_account': 'serviceAccount'
    }

    def __init__(self, namespace=None, service_account=None):
        r"""PodIdentitySubject

        The model defined in huaweicloud sdk

        :param namespace: **参数解释**： ServiceAccount所属的命名空间 **约束限制**： 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type namespace: str
        :param service_account: **参数解释：** ServiceAccount名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type service_account: str
        """
        
        

        self._namespace = None
        self._service_account = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if service_account is not None:
            self.service_account = service_account

    @property
    def namespace(self):
        r"""Gets the namespace of this PodIdentitySubject.

        **参数解释**： ServiceAccount所属的命名空间 **约束限制**： 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The namespace of this PodIdentitySubject.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this PodIdentitySubject.

        **参数解释**： ServiceAccount所属的命名空间 **约束限制**： 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param namespace: The namespace of this PodIdentitySubject.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def service_account(self):
        r"""Gets the service_account of this PodIdentitySubject.

        **参数解释：** ServiceAccount名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The service_account of this PodIdentitySubject.
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        r"""Sets the service_account of this PodIdentitySubject.

        **参数解释：** ServiceAccount名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param service_account: The service_account of this PodIdentitySubject.
        :type service_account: str
        """
        self._service_account = service_account

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
        if not isinstance(other, PodIdentitySubject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
