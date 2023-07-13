# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MaterialAssetMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'components': 'list[MaterialComponentInfo]'
    }

    attribute_map = {
        'components': 'components'
    }

    def __init__(self, components=None):
        """MaterialAssetMeta

        The model defined in huaweicloud sdk

        :param components: 可替换的素材组件列表。
        :type components: list[:class:`huaweicloudsdkmetastudio.v1.MaterialComponentInfo`]
        """
        
        

        self._components = None
        self.discriminator = None

        if components is not None:
            self.components = components

    @property
    def components(self):
        """Gets the components of this MaterialAssetMeta.

        可替换的素材组件列表。

        :return: The components of this MaterialAssetMeta.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.MaterialComponentInfo`]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this MaterialAssetMeta.

        可替换的素材组件列表。

        :param components: The components of this MaterialAssetMeta.
        :type components: list[:class:`huaweicloudsdkmetastudio.v1.MaterialComponentInfo`]
        """
        self._components = components

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
        if not isinstance(other, MaterialAssetMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
