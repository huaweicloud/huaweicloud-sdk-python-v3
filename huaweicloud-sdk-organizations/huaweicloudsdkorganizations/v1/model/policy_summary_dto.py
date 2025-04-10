# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicySummaryDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_builtin': 'bool',
        'description': 'str',
        'id': 'str',
        'urn': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'is_builtin': 'is_builtin',
        'description': 'description',
        'id': 'id',
        'urn': 'urn',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, is_builtin=None, description=None, id=None, urn=None, name=None, type=None):
        r"""PolicySummaryDto

        The model defined in huaweicloud sdk

        :param is_builtin: 一个布尔值，指示指定的策略是否为系统策略。如果为true，即为系统策略，则可以将策略附加到根、组织单元或账号，但不能编辑它。
        :type is_builtin: bool
        :param description: 策略说明。
        :type description: str
        :param id: 策略的唯一标识符（ID）。
        :type id: str
        :param urn: 策略的统一资源名称。
        :type urn: str
        :param name: 策略的名称。
        :type name: str
        :param type: 策略的类型,service_control_policy：服务控制策略；tag_policy：标签策略。
        :type type: str
        """
        
        

        self._is_builtin = None
        self._description = None
        self._id = None
        self._urn = None
        self._name = None
        self._type = None
        self.discriminator = None

        self.is_builtin = is_builtin
        self.description = description
        self.id = id
        self.urn = urn
        self.name = name
        self.type = type

    @property
    def is_builtin(self):
        r"""Gets the is_builtin of this PolicySummaryDto.

        一个布尔值，指示指定的策略是否为系统策略。如果为true，即为系统策略，则可以将策略附加到根、组织单元或账号，但不能编辑它。

        :return: The is_builtin of this PolicySummaryDto.
        :rtype: bool
        """
        return self._is_builtin

    @is_builtin.setter
    def is_builtin(self, is_builtin):
        r"""Sets the is_builtin of this PolicySummaryDto.

        一个布尔值，指示指定的策略是否为系统策略。如果为true，即为系统策略，则可以将策略附加到根、组织单元或账号，但不能编辑它。

        :param is_builtin: The is_builtin of this PolicySummaryDto.
        :type is_builtin: bool
        """
        self._is_builtin = is_builtin

    @property
    def description(self):
        r"""Gets the description of this PolicySummaryDto.

        策略说明。

        :return: The description of this PolicySummaryDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PolicySummaryDto.

        策略说明。

        :param description: The description of this PolicySummaryDto.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this PolicySummaryDto.

        策略的唯一标识符（ID）。

        :return: The id of this PolicySummaryDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PolicySummaryDto.

        策略的唯一标识符（ID）。

        :param id: The id of this PolicySummaryDto.
        :type id: str
        """
        self._id = id

    @property
    def urn(self):
        r"""Gets the urn of this PolicySummaryDto.

        策略的统一资源名称。

        :return: The urn of this PolicySummaryDto.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this PolicySummaryDto.

        策略的统一资源名称。

        :param urn: The urn of this PolicySummaryDto.
        :type urn: str
        """
        self._urn = urn

    @property
    def name(self):
        r"""Gets the name of this PolicySummaryDto.

        策略的名称。

        :return: The name of this PolicySummaryDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PolicySummaryDto.

        策略的名称。

        :param name: The name of this PolicySummaryDto.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this PolicySummaryDto.

        策略的类型,service_control_policy：服务控制策略；tag_policy：标签策略。

        :return: The type of this PolicySummaryDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PolicySummaryDto.

        策略的类型,service_control_policy：服务控制策略；tag_policy：标签策略。

        :param type: The type of this PolicySummaryDto.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, PolicySummaryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
