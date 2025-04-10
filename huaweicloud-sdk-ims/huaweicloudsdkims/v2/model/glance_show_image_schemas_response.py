# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlanceShowImageSchemasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'additional_properties': 'AdditionalProperties',
        'name': 'str',
        'properties': 'object',
        'links': 'list[Links]'
    }

    attribute_map = {
        'additional_properties': 'additionalProperties',
        'name': 'name',
        'properties': 'properties',
        'links': 'links'
    }

    def __init__(self, additional_properties=None, name=None, properties=None, links=None):
        r"""GlanceShowImageSchemasResponse

        The model defined in huaweicloud sdk

        :param additional_properties: 
        :type additional_properties: :class:`huaweicloudsdkims.v2.AdditionalProperties`
        :param name: 视图名称。
        :type name: str
        :param properties: 镜像属性说明，主要是对基础属性的说明，包含每个属性的取值类型、用途等。
        :type properties: object
        :param links: 视图链接。
        :type links: list[:class:`huaweicloudsdkims.v2.Links`]
        """
        
        super(GlanceShowImageSchemasResponse, self).__init__()

        self._additional_properties = None
        self._name = None
        self._properties = None
        self._links = None
        self.discriminator = None

        if additional_properties is not None:
            self.additional_properties = additional_properties
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties
        if links is not None:
            self.links = links

    @property
    def additional_properties(self):
        r"""Gets the additional_properties of this GlanceShowImageSchemasResponse.

        :return: The additional_properties of this GlanceShowImageSchemasResponse.
        :rtype: :class:`huaweicloudsdkims.v2.AdditionalProperties`
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        r"""Sets the additional_properties of this GlanceShowImageSchemasResponse.

        :param additional_properties: The additional_properties of this GlanceShowImageSchemasResponse.
        :type additional_properties: :class:`huaweicloudsdkims.v2.AdditionalProperties`
        """
        self._additional_properties = additional_properties

    @property
    def name(self):
        r"""Gets the name of this GlanceShowImageSchemasResponse.

        视图名称。

        :return: The name of this GlanceShowImageSchemasResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GlanceShowImageSchemasResponse.

        视图名称。

        :param name: The name of this GlanceShowImageSchemasResponse.
        :type name: str
        """
        self._name = name

    @property
    def properties(self):
        r"""Gets the properties of this GlanceShowImageSchemasResponse.

        镜像属性说明，主要是对基础属性的说明，包含每个属性的取值类型、用途等。

        :return: The properties of this GlanceShowImageSchemasResponse.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this GlanceShowImageSchemasResponse.

        镜像属性说明，主要是对基础属性的说明，包含每个属性的取值类型、用途等。

        :param properties: The properties of this GlanceShowImageSchemasResponse.
        :type properties: object
        """
        self._properties = properties

    @property
    def links(self):
        r"""Gets the links of this GlanceShowImageSchemasResponse.

        视图链接。

        :return: The links of this GlanceShowImageSchemasResponse.
        :rtype: list[:class:`huaweicloudsdkims.v2.Links`]
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this GlanceShowImageSchemasResponse.

        视图链接。

        :param links: The links of this GlanceShowImageSchemasResponse.
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
        if not isinstance(other, GlanceShowImageSchemasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
