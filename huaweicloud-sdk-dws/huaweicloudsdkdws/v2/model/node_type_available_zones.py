# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeTypeAvailableZones:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'status': 'str'
    }

    attribute_map = {
        'code': 'code',
        'status': 'status'
    }

    def __init__(self, code=None, status=None):
        r"""NodeTypeAvailableZones

        The model defined in huaweicloud sdk

        :param code: **参数解释**： 可用区ID。 **取值范围**： 不涉及。
        :type code: str
        :param status: **参数解释**： 规格可用状态。 **取值范围**： - normal：可用 - sellout：售罄 - abandon：不可用
        :type status: str
        """
        
        

        self._code = None
        self._status = None
        self.discriminator = None

        self.code = code
        self.status = status

    @property
    def code(self):
        r"""Gets the code of this NodeTypeAvailableZones.

        **参数解释**： 可用区ID。 **取值范围**： 不涉及。

        :return: The code of this NodeTypeAvailableZones.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this NodeTypeAvailableZones.

        **参数解释**： 可用区ID。 **取值范围**： 不涉及。

        :param code: The code of this NodeTypeAvailableZones.
        :type code: str
        """
        self._code = code

    @property
    def status(self):
        r"""Gets the status of this NodeTypeAvailableZones.

        **参数解释**： 规格可用状态。 **取值范围**： - normal：可用 - sellout：售罄 - abandon：不可用

        :return: The status of this NodeTypeAvailableZones.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NodeTypeAvailableZones.

        **参数解释**： 规格可用状态。 **取值范围**： - normal：可用 - sellout：售罄 - abandon：不可用

        :param status: The status of this NodeTypeAvailableZones.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, NodeTypeAvailableZones):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
