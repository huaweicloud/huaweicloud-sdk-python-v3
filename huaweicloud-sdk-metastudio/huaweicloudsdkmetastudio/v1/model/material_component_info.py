# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MaterialComponentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_name': 'str',
        'component_type': 'str',
        'component_desc': 'str'
    }

    attribute_map = {
        'component_name': 'component_name',
        'component_type': 'component_type',
        'component_desc': 'component_desc'
    }

    def __init__(self, component_name=None, component_type=None, component_desc=None):
        """MaterialComponentInfo

        The model defined in huaweicloud sdk

        :param component_name: 素材组件名称。
        :type component_name: str
        :param component_type: 素材组件类型。 * CLOTHES：衣服 * PANTS：裤子 * SHOES：鞋子 * HAIR：头发 * EYELASH：睫毛 * EYEBROW：眉毛
        :type component_type: str
        :param component_desc: 素材组件描述。
        :type component_desc: str
        """
        
        

        self._component_name = None
        self._component_type = None
        self._component_desc = None
        self.discriminator = None

        self.component_name = component_name
        self.component_type = component_type
        if component_desc is not None:
            self.component_desc = component_desc

    @property
    def component_name(self):
        """Gets the component_name of this MaterialComponentInfo.

        素材组件名称。

        :return: The component_name of this MaterialComponentInfo.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """Sets the component_name of this MaterialComponentInfo.

        素材组件名称。

        :param component_name: The component_name of this MaterialComponentInfo.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def component_type(self):
        """Gets the component_type of this MaterialComponentInfo.

        素材组件类型。 * CLOTHES：衣服 * PANTS：裤子 * SHOES：鞋子 * HAIR：头发 * EYELASH：睫毛 * EYEBROW：眉毛

        :return: The component_type of this MaterialComponentInfo.
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """Sets the component_type of this MaterialComponentInfo.

        素材组件类型。 * CLOTHES：衣服 * PANTS：裤子 * SHOES：鞋子 * HAIR：头发 * EYELASH：睫毛 * EYEBROW：眉毛

        :param component_type: The component_type of this MaterialComponentInfo.
        :type component_type: str
        """
        self._component_type = component_type

    @property
    def component_desc(self):
        """Gets the component_desc of this MaterialComponentInfo.

        素材组件描述。

        :return: The component_desc of this MaterialComponentInfo.
        :rtype: str
        """
        return self._component_desc

    @component_desc.setter
    def component_desc(self, component_desc):
        """Sets the component_desc of this MaterialComponentInfo.

        素材组件描述。

        :param component_desc: The component_desc of this MaterialComponentInfo.
        :type component_desc: str
        """
        self._component_desc = component_desc

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
        if not isinstance(other, MaterialComponentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
