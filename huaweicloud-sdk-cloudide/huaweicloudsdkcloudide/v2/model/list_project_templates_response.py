# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'templates': 'list[ProjectTemplates]',
        'status': 'str'
    }

    attribute_map = {
        'templates': 'templates',
        'status': 'status'
    }

    def __init__(self, templates=None, status=None):
        """ListProjectTemplatesResponse

        The model defined in huaweicloud sdk

        :param templates: 模板列表
        :type templates: list[:class:`huaweicloudsdkcloudide.v2.ProjectTemplates`]
        :param status: 状态
        :type status: str
        """
        
        super(ListProjectTemplatesResponse, self).__init__()

        self._templates = None
        self._status = None
        self.discriminator = None

        if templates is not None:
            self.templates = templates
        if status is not None:
            self.status = status

    @property
    def templates(self):
        """Gets the templates of this ListProjectTemplatesResponse.

        模板列表

        :return: The templates of this ListProjectTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.ProjectTemplates`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this ListProjectTemplatesResponse.

        模板列表

        :param templates: The templates of this ListProjectTemplatesResponse.
        :type templates: list[:class:`huaweicloudsdkcloudide.v2.ProjectTemplates`]
        """
        self._templates = templates

    @property
    def status(self):
        """Gets the status of this ListProjectTemplatesResponse.

        状态

        :return: The status of this ListProjectTemplatesResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListProjectTemplatesResponse.

        状态

        :param status: The status of this ListProjectTemplatesResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListProjectTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
