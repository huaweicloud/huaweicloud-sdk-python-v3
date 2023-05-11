# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplateViewHistoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'templates': 'list[TemplateViewHistory]',
        'count': 'int'
    }

    attribute_map = {
        'templates': 'templates',
        'count': 'count'
    }

    def __init__(self, templates=None, count=None):
        """CreateTemplateViewHistoriesResponse

        The model defined in huaweicloud sdk

        :param templates: 我浏览的模板。
        :type templates: list[:class:`huaweicloudsdkdevstar.v1.TemplateViewHistory`]
        :param count: 我浏览的模板数量。
        :type count: int
        """
        
        super(CreateTemplateViewHistoriesResponse, self).__init__()

        self._templates = None
        self._count = None
        self.discriminator = None

        if templates is not None:
            self.templates = templates
        if count is not None:
            self.count = count

    @property
    def templates(self):
        """Gets the templates of this CreateTemplateViewHistoriesResponse.

        我浏览的模板。

        :return: The templates of this CreateTemplateViewHistoriesResponse.
        :rtype: list[:class:`huaweicloudsdkdevstar.v1.TemplateViewHistory`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this CreateTemplateViewHistoriesResponse.

        我浏览的模板。

        :param templates: The templates of this CreateTemplateViewHistoriesResponse.
        :type templates: list[:class:`huaweicloudsdkdevstar.v1.TemplateViewHistory`]
        """
        self._templates = templates

    @property
    def count(self):
        """Gets the count of this CreateTemplateViewHistoriesResponse.

        我浏览的模板数量。

        :return: The count of this CreateTemplateViewHistoriesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CreateTemplateViewHistoriesResponse.

        我浏览的模板数量。

        :param count: The count of this CreateTemplateViewHistoriesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, CreateTemplateViewHistoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
