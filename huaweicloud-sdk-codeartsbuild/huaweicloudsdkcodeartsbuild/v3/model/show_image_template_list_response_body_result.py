# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageTemplateListResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_templates': 'list[ShowImageTemplateListResponseBodyResultImageTemplates]'
    }

    attribute_map = {
        'image_templates': 'image_templates'
    }

    def __init__(self, image_templates=None):
        r"""ShowImageTemplateListResponseBodyResult

        The model defined in huaweicloud sdk

        :param image_templates: 镜像模版列表
        :type image_templates: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowImageTemplateListResponseBodyResultImageTemplates`]
        """
        
        

        self._image_templates = None
        self.discriminator = None

        if image_templates is not None:
            self.image_templates = image_templates

    @property
    def image_templates(self):
        r"""Gets the image_templates of this ShowImageTemplateListResponseBodyResult.

        镜像模版列表

        :return: The image_templates of this ShowImageTemplateListResponseBodyResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowImageTemplateListResponseBodyResultImageTemplates`]
        """
        return self._image_templates

    @image_templates.setter
    def image_templates(self, image_templates):
        r"""Sets the image_templates of this ShowImageTemplateListResponseBodyResult.

        镜像模版列表

        :param image_templates: The image_templates of this ShowImageTemplateListResponseBodyResult.
        :type image_templates: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowImageTemplateListResponseBodyResultImageTemplates`]
        """
        self._image_templates = image_templates

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
        if not isinstance(other, ShowImageTemplateListResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
