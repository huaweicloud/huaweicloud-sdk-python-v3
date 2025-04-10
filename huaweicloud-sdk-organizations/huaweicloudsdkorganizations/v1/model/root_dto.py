# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RootDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'urn': 'str',
        'name': 'str',
        'policy_types': 'list[PolicyTypeSummaryDto]',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'urn': 'urn',
        'name': 'name',
        'policy_types': 'policy_types',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, urn=None, name=None, policy_types=None, created_at=None):
        r"""RootDto

        The model defined in huaweicloud sdk

        :param id: 根的唯一标识符（ID）。
        :type id: str
        :param urn: 根的统一资源名称。
        :type urn: str
        :param name: 根的名称。
        :type name: str
        :param policy_types: 策略类型在当前根已启用，则该类型策略可以绑定到根或其组织单元或账号。
        :type policy_types: list[:class:`huaweicloudsdkorganizations.v1.PolicyTypeSummaryDto`]
        :param created_at: 根的创建时间。
        :type created_at: datetime
        """
        
        

        self._id = None
        self._urn = None
        self._name = None
        self._policy_types = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.urn = urn
        self.name = name
        self.policy_types = policy_types
        self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this RootDto.

        根的唯一标识符（ID）。

        :return: The id of this RootDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RootDto.

        根的唯一标识符（ID）。

        :param id: The id of this RootDto.
        :type id: str
        """
        self._id = id

    @property
    def urn(self):
        r"""Gets the urn of this RootDto.

        根的统一资源名称。

        :return: The urn of this RootDto.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this RootDto.

        根的统一资源名称。

        :param urn: The urn of this RootDto.
        :type urn: str
        """
        self._urn = urn

    @property
    def name(self):
        r"""Gets the name of this RootDto.

        根的名称。

        :return: The name of this RootDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RootDto.

        根的名称。

        :param name: The name of this RootDto.
        :type name: str
        """
        self._name = name

    @property
    def policy_types(self):
        r"""Gets the policy_types of this RootDto.

        策略类型在当前根已启用，则该类型策略可以绑定到根或其组织单元或账号。

        :return: The policy_types of this RootDto.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.PolicyTypeSummaryDto`]
        """
        return self._policy_types

    @policy_types.setter
    def policy_types(self, policy_types):
        r"""Sets the policy_types of this RootDto.

        策略类型在当前根已启用，则该类型策略可以绑定到根或其组织单元或账号。

        :param policy_types: The policy_types of this RootDto.
        :type policy_types: list[:class:`huaweicloudsdkorganizations.v1.PolicyTypeSummaryDto`]
        """
        self._policy_types = policy_types

    @property
    def created_at(self):
        r"""Gets the created_at of this RootDto.

        根的创建时间。

        :return: The created_at of this RootDto.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RootDto.

        根的创建时间。

        :param created_at: The created_at of this RootDto.
        :type created_at: datetime
        """
        self._created_at = created_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RootDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
