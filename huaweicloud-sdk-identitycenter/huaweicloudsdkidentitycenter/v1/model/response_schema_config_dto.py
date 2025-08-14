# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseSchemaConfigDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'properties': 'dict(str, ResponseSchemaPropertiesDetailsDto)',
        'subject': 'ResponseSchemaSubjectDetailsDto',
        'supported_name_id_formats': 'list[str]'
    }

    attribute_map = {
        'properties': 'properties',
        'subject': 'subject',
        'supported_name_id_formats': 'supported_name_id_formats'
    }

    def __init__(self, properties=None, subject=None, supported_name_id_formats=None):
        r"""ResponseSchemaConfigDto

        The model defined in huaweicloud sdk

        :param properties: 额外添加的属性映射Schema配置
        :type properties: dict(str, ResponseSchemaPropertiesDetailsDto)
        :param subject: 
        :type subject: :class:`huaweicloudsdkidentitycenter.v1.ResponseSchemaSubjectDetailsDto`
        :param supported_name_id_formats: 应用程序支持的Subject NameID格式
        :type supported_name_id_formats: list[str]
        """
        
        

        self._properties = None
        self._subject = None
        self._supported_name_id_formats = None
        self.discriminator = None

        if properties is not None:
            self.properties = properties
        self.subject = subject
        if supported_name_id_formats is not None:
            self.supported_name_id_formats = supported_name_id_formats

    @property
    def properties(self):
        r"""Gets the properties of this ResponseSchemaConfigDto.

        额外添加的属性映射Schema配置

        :return: The properties of this ResponseSchemaConfigDto.
        :rtype: dict(str, ResponseSchemaPropertiesDetailsDto)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ResponseSchemaConfigDto.

        额外添加的属性映射Schema配置

        :param properties: The properties of this ResponseSchemaConfigDto.
        :type properties: dict(str, ResponseSchemaPropertiesDetailsDto)
        """
        self._properties = properties

    @property
    def subject(self):
        r"""Gets the subject of this ResponseSchemaConfigDto.

        :return: The subject of this ResponseSchemaConfigDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ResponseSchemaSubjectDetailsDto`
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this ResponseSchemaConfigDto.

        :param subject: The subject of this ResponseSchemaConfigDto.
        :type subject: :class:`huaweicloudsdkidentitycenter.v1.ResponseSchemaSubjectDetailsDto`
        """
        self._subject = subject

    @property
    def supported_name_id_formats(self):
        r"""Gets the supported_name_id_formats of this ResponseSchemaConfigDto.

        应用程序支持的Subject NameID格式

        :return: The supported_name_id_formats of this ResponseSchemaConfigDto.
        :rtype: list[str]
        """
        return self._supported_name_id_formats

    @supported_name_id_formats.setter
    def supported_name_id_formats(self, supported_name_id_formats):
        r"""Sets the supported_name_id_formats of this ResponseSchemaConfigDto.

        应用程序支持的Subject NameID格式

        :param supported_name_id_formats: The supported_name_id_formats of this ResponseSchemaConfigDto.
        :type supported_name_id_formats: list[str]
        """
        self._supported_name_id_formats = supported_name_id_formats

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
        if not isinstance(other, ResponseSchemaConfigDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
