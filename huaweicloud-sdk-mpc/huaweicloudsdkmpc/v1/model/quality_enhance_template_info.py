# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QualityEnhanceTemplateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'int',
        'template': 'QualityEnhanceTemplate',
        'error': 'XCodeError'
    }

    attribute_map = {
        'template_id': 'template_id',
        'template': 'template',
        'error': 'error'
    }

    def __init__(self, template_id=None, template=None, error=None):
        """QualityEnhanceTemplateInfo

        The model defined in huaweicloud sdk

        :param template_id: 模板ID。 
        :type template_id: int
        :param template: 
        :type template: :class:`huaweicloudsdkmpc.v1.QualityEnhanceTemplate`
        :param error: 
        :type error: :class:`huaweicloudsdkmpc.v1.XCodeError`
        """
        
        

        self._template_id = None
        self._template = None
        self._error = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if template is not None:
            self.template = template
        if error is not None:
            self.error = error

    @property
    def template_id(self):
        """Gets the template_id of this QualityEnhanceTemplateInfo.

        模板ID。 

        :return: The template_id of this QualityEnhanceTemplateInfo.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this QualityEnhanceTemplateInfo.

        模板ID。 

        :param template_id: The template_id of this QualityEnhanceTemplateInfo.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def template(self):
        """Gets the template of this QualityEnhanceTemplateInfo.

        :return: The template of this QualityEnhanceTemplateInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.QualityEnhanceTemplate`
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this QualityEnhanceTemplateInfo.

        :param template: The template of this QualityEnhanceTemplateInfo.
        :type template: :class:`huaweicloudsdkmpc.v1.QualityEnhanceTemplate`
        """
        self._template = template

    @property
    def error(self):
        """Gets the error of this QualityEnhanceTemplateInfo.

        :return: The error of this QualityEnhanceTemplateInfo.
        :rtype: :class:`huaweicloudsdkmpc.v1.XCodeError`
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this QualityEnhanceTemplateInfo.

        :param error: The error of this QualityEnhanceTemplateInfo.
        :type error: :class:`huaweicloudsdkmpc.v1.XCodeError`
        """
        self._error = error

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
        if not isinstance(other, QualityEnhanceTemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
