# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlanceListImageSchemasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'properties': 'object',
        'links': 'list[Links]'
    }

    attribute_map = {
        'name': 'name',
        'properties': 'properties',
        'links': 'links'
    }

    def __init__(self, name=None, properties=None, links=None):
        r"""GlanceListImageSchemasResponse

        The model defined in huaweicloud sdk

        :param name: 视图名称。
        :type name: str
        :param properties: 镜像属性说明，主要是对基础属性的说明，包含每个属性的取值类型、用途等。
        :type properties: object
        :param links: 视图链接。
        :type links: list[:class:`huaweicloudsdkims.v2.Links`]
        """
        
        super(GlanceListImageSchemasResponse, self).__init__()

        self._name = None
        self._properties = None
        self._links = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties
        if links is not None:
            self.links = links

    @property
    def name(self):
        r"""Gets the name of this GlanceListImageSchemasResponse.

        视图名称。

        :return: The name of this GlanceListImageSchemasResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GlanceListImageSchemasResponse.

        视图名称。

        :param name: The name of this GlanceListImageSchemasResponse.
        :type name: str
        """
        self._name = name

    @property
    def properties(self):
        r"""Gets the properties of this GlanceListImageSchemasResponse.

        镜像属性说明，主要是对基础属性的说明，包含每个属性的取值类型、用途等。

        :return: The properties of this GlanceListImageSchemasResponse.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this GlanceListImageSchemasResponse.

        镜像属性说明，主要是对基础属性的说明，包含每个属性的取值类型、用途等。

        :param properties: The properties of this GlanceListImageSchemasResponse.
        :type properties: object
        """
        self._properties = properties

    @property
    def links(self):
        r"""Gets the links of this GlanceListImageSchemasResponse.

        视图链接。

        :return: The links of this GlanceListImageSchemasResponse.
        :rtype: list[:class:`huaweicloudsdkims.v2.Links`]
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this GlanceListImageSchemasResponse.

        视图链接。

        :param links: The links of this GlanceListImageSchemasResponse.
        :type links: list[:class:`huaweicloudsdkims.v2.Links`]
        """
        self._links = links

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
        if not isinstance(other, GlanceListImageSchemasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
