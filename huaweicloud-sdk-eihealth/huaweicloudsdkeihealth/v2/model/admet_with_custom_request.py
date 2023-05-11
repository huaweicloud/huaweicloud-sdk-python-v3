# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdmetWithCustomRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'smiles': 'str',
        'custom_props': 'list[CustomProp]'
    }

    attribute_map = {
        'smiles': 'smiles',
        'custom_props': 'custom_props'
    }

    def __init__(self, smiles=None, custom_props=None):
        """AdmetWithCustomRequest

        The model defined in huaweicloud sdk

        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param custom_props: 用户已开启的自定义属性集合
        :type custom_props: list[:class:`huaweicloudsdkeihealth.v2.CustomProp`]
        """
        
        

        self._smiles = None
        self._custom_props = None
        self.discriminator = None

        self.smiles = smiles
        if custom_props is not None:
            self.custom_props = custom_props

    @property
    def smiles(self):
        """Gets the smiles of this AdmetWithCustomRequest.

        分子SMILES表达式

        :return: The smiles of this AdmetWithCustomRequest.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this AdmetWithCustomRequest.

        分子SMILES表达式

        :param smiles: The smiles of this AdmetWithCustomRequest.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def custom_props(self):
        """Gets the custom_props of this AdmetWithCustomRequest.

        用户已开启的自定义属性集合

        :return: The custom_props of this AdmetWithCustomRequest.
        :rtype: list[:class:`huaweicloudsdkeihealth.v2.CustomProp`]
        """
        return self._custom_props

    @custom_props.setter
    def custom_props(self, custom_props):
        """Sets the custom_props of this AdmetWithCustomRequest.

        用户已开启的自定义属性集合

        :param custom_props: The custom_props of this AdmetWithCustomRequest.
        :type custom_props: list[:class:`huaweicloudsdkeihealth.v2.CustomProp`]
        """
        self._custom_props = custom_props

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
        if not isinstance(other, AdmetWithCustomRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
