# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomProp:

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
        'prop_definition': 'PropDefinition'
    }

    attribute_map = {
        'id': 'id',
        'prop_definition': 'prop_definition'
    }

    def __init__(self, id=None, prop_definition=None):
        r"""CustomProp

        The model defined in huaweicloud sdk

        :param id: 自定义属性的ID（API侧）
        :type id: str
        :param prop_definition: 
        :type prop_definition: :class:`huaweicloudsdkeihealth.v2.PropDefinition`
        """
        
        

        self._id = None
        self._prop_definition = None
        self.discriminator = None

        self.id = id
        if prop_definition is not None:
            self.prop_definition = prop_definition

    @property
    def id(self):
        r"""Gets the id of this CustomProp.

        自定义属性的ID（API侧）

        :return: The id of this CustomProp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CustomProp.

        自定义属性的ID（API侧）

        :param id: The id of this CustomProp.
        :type id: str
        """
        self._id = id

    @property
    def prop_definition(self):
        r"""Gets the prop_definition of this CustomProp.

        :return: The prop_definition of this CustomProp.
        :rtype: :class:`huaweicloudsdkeihealth.v2.PropDefinition`
        """
        return self._prop_definition

    @prop_definition.setter
    def prop_definition(self, prop_definition):
        r"""Sets the prop_definition of this CustomProp.

        :param prop_definition: The prop_definition of this CustomProp.
        :type prop_definition: :class:`huaweicloudsdkeihealth.v2.PropDefinition`
        """
        self._prop_definition = prop_definition

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
        if not isinstance(other, CustomProp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
