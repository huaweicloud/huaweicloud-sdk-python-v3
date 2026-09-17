# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InPlaceMigrate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'str',
        'kind': 'str',
        'spec': 'InPlaceMigratetoNodesSpec',
        'status': 'TaskStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, spec=None, status=None):
        r"""InPlaceMigrate

        The model defined in huaweicloud sdk

        :param api_version: **参数解释**： API版本 **约束限制**： 固定值，不允许修改 **取值范围**： 不涉及 **默认取值**： v3 
        :type api_version: str
        :param kind: **参数解释**： API类型 **约束限制**： 固定值，不允许修改 **取值范围**： 不涉及 **默认取值**： InPlaceMigrateNodesTask 
        :type kind: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.InPlaceMigratetoNodesSpec`
        :param status: 
        :type status: :class:`huaweicloudsdkcce.v3.TaskStatus`
        """
        
        

        self._api_version = None
        self._kind = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        self.spec = spec
        if status is not None:
            self.status = status

    @property
    def api_version(self):
        r"""Gets the api_version of this InPlaceMigrate.

        **参数解释**： API版本 **约束限制**： 固定值，不允许修改 **取值范围**： 不涉及 **默认取值**： v3 

        :return: The api_version of this InPlaceMigrate.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this InPlaceMigrate.

        **参数解释**： API版本 **约束限制**： 固定值，不允许修改 **取值范围**： 不涉及 **默认取值**： v3 

        :param api_version: The api_version of this InPlaceMigrate.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this InPlaceMigrate.

        **参数解释**： API类型 **约束限制**： 固定值，不允许修改 **取值范围**： 不涉及 **默认取值**： InPlaceMigrateNodesTask 

        :return: The kind of this InPlaceMigrate.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this InPlaceMigrate.

        **参数解释**： API类型 **约束限制**： 固定值，不允许修改 **取值范围**： 不涉及 **默认取值**： InPlaceMigrateNodesTask 

        :param kind: The kind of this InPlaceMigrate.
        :type kind: str
        """
        self._kind = kind

    @property
    def spec(self):
        r"""Gets the spec of this InPlaceMigrate.

        :return: The spec of this InPlaceMigrate.
        :rtype: :class:`huaweicloudsdkcce.v3.InPlaceMigratetoNodesSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this InPlaceMigrate.

        :param spec: The spec of this InPlaceMigrate.
        :type spec: :class:`huaweicloudsdkcce.v3.InPlaceMigratetoNodesSpec`
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this InPlaceMigrate.

        :return: The status of this InPlaceMigrate.
        :rtype: :class:`huaweicloudsdkcce.v3.TaskStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InPlaceMigrate.

        :param status: The status of this InPlaceMigrate.
        :type status: :class:`huaweicloudsdkcce.v3.TaskStatus`
        """
        self._status = status

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
        if not isinstance(other, InPlaceMigrate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
