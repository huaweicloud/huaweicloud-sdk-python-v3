# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchTemplateByIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'share_type': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'share_type': 'share_type'
    }

    def __init__(self, template_id=None, share_type=None):
        """SearchTemplateByIdRequest

        The model defined in huaweicloud sdk

        :param template_id: 方案id。
        :type template_id: str
        :param share_type: 模板共享类型，默认为private。可选public private
        :type share_type: str
        """
        
        

        self._template_id = None
        self._share_type = None
        self.discriminator = None

        self.template_id = template_id
        self.share_type = share_type

    @property
    def template_id(self):
        """Gets the template_id of this SearchTemplateByIdRequest.

        方案id。

        :return: The template_id of this SearchTemplateByIdRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this SearchTemplateByIdRequest.

        方案id。

        :param template_id: The template_id of this SearchTemplateByIdRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def share_type(self):
        """Gets the share_type of this SearchTemplateByIdRequest.

        模板共享类型，默认为private。可选public private

        :return: The share_type of this SearchTemplateByIdRequest.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this SearchTemplateByIdRequest.

        模板共享类型，默认为private。可选public private

        :param share_type: The share_type of this SearchTemplateByIdRequest.
        :type share_type: str
        """
        self._share_type = share_type

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
        if not isinstance(other, SearchTemplateByIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
