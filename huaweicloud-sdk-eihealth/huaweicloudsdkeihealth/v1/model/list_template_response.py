# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'templates': 'list[TemplateRsp]'
    }

    attribute_map = {
        'count': 'count',
        'templates': 'templates'
    }

    def __init__(self, count=None, templates=None):
        """ListTemplateResponse

        The model defined in huaweicloud sdk

        :param count: 模板总数
        :type count: int
        :param templates: 模板列表
        :type templates: list[:class:`huaweicloudsdkeihealth.v1.TemplateRsp`]
        """
        
        super(ListTemplateResponse, self).__init__()

        self._count = None
        self._templates = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if templates is not None:
            self.templates = templates

    @property
    def count(self):
        """Gets the count of this ListTemplateResponse.

        模板总数

        :return: The count of this ListTemplateResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListTemplateResponse.

        模板总数

        :param count: The count of this ListTemplateResponse.
        :type count: int
        """
        self._count = count

    @property
    def templates(self):
        """Gets the templates of this ListTemplateResponse.

        模板列表

        :return: The templates of this ListTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.TemplateRsp`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this ListTemplateResponse.

        模板列表

        :param templates: The templates of this ListTemplateResponse.
        :type templates: list[:class:`huaweicloudsdkeihealth.v1.TemplateRsp`]
        """
        self._templates = templates

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
        if not isinstance(other, ListTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
