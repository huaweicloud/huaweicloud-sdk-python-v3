# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorInfoResponse:

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
        'name': 'str',
        'vcpus': 'str',
        'ram': 'str',
        'is_current_flavor': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'is_current_flavor': 'is_current_flavor'
    }

    def __init__(self, id=None, name=None, vcpus=None, ram=None, is_current_flavor=None):
        r"""FlavorInfoResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 规格ID。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 规格编码。 **取值范围**： 不涉及。
        :type name: str
        :param vcpus: **参数解释**： CPU数。 **取值范围**： 不涉及。
        :type vcpus: str
        :param ram: **参数解释**： 内存数。 **取值范围**： 不涉及。
        :type ram: str
        :param is_current_flavor: **参数解释**： 是否是当前规格。 **取值范围**： 不涉及。
        :type is_current_flavor: bool
        """
        
        

        self._id = None
        self._name = None
        self._vcpus = None
        self._ram = None
        self._is_current_flavor = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if is_current_flavor is not None:
            self.is_current_flavor = is_current_flavor

    @property
    def id(self):
        r"""Gets the id of this FlavorInfoResponse.

        **参数解释**： 规格ID。 **取值范围**： 不涉及。

        :return: The id of this FlavorInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FlavorInfoResponse.

        **参数解释**： 规格ID。 **取值范围**： 不涉及。

        :param id: The id of this FlavorInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this FlavorInfoResponse.

        **参数解释**： 规格编码。 **取值范围**： 不涉及。

        :return: The name of this FlavorInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FlavorInfoResponse.

        **参数解释**： 规格编码。 **取值范围**： 不涉及。

        :param name: The name of this FlavorInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def vcpus(self):
        r"""Gets the vcpus of this FlavorInfoResponse.

        **参数解释**： CPU数。 **取值范围**： 不涉及。

        :return: The vcpus of this FlavorInfoResponse.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this FlavorInfoResponse.

        **参数解释**： CPU数。 **取值范围**： 不涉及。

        :param vcpus: The vcpus of this FlavorInfoResponse.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this FlavorInfoResponse.

        **参数解释**： 内存数。 **取值范围**： 不涉及。

        :return: The ram of this FlavorInfoResponse.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this FlavorInfoResponse.

        **参数解释**： 内存数。 **取值范围**： 不涉及。

        :param ram: The ram of this FlavorInfoResponse.
        :type ram: str
        """
        self._ram = ram

    @property
    def is_current_flavor(self):
        r"""Gets the is_current_flavor of this FlavorInfoResponse.

        **参数解释**： 是否是当前规格。 **取值范围**： 不涉及。

        :return: The is_current_flavor of this FlavorInfoResponse.
        :rtype: bool
        """
        return self._is_current_flavor

    @is_current_flavor.setter
    def is_current_flavor(self, is_current_flavor):
        r"""Sets the is_current_flavor of this FlavorInfoResponse.

        **参数解释**： 是否是当前规格。 **取值范围**： 不涉及。

        :param is_current_flavor: The is_current_flavor of this FlavorInfoResponse.
        :type is_current_flavor: bool
        """
        self._is_current_flavor = is_current_flavor

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
        if not isinstance(other, FlavorInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
