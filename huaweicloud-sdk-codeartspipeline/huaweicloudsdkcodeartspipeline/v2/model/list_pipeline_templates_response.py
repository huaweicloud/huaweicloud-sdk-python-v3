# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelineTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'total': 'int',
        'templates': 'list[PipelineTemplateSimpleVO]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total',
        'templates': 'templates'
    }

    def __init__(self, offset=None, limit=None, total=None, templates=None):
        r"""ListPipelineTemplatesResponse

        The model defined in huaweicloud sdk

        :param offset: 起始偏移
        :type offset: int
        :param limit: 每页大小
        :type limit: int
        :param total: 总数
        :type total: int
        :param templates: 
        :type templates: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTemplateSimpleVO`]
        """
        
        super(ListPipelineTemplatesResponse, self).__init__()

        self._offset = None
        self._limit = None
        self._total = None
        self._templates = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total
        if templates is not None:
            self.templates = templates

    @property
    def offset(self):
        r"""Gets the offset of this ListPipelineTemplatesResponse.

        起始偏移

        :return: The offset of this ListPipelineTemplatesResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPipelineTemplatesResponse.

        起始偏移

        :param offset: The offset of this ListPipelineTemplatesResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPipelineTemplatesResponse.

        每页大小

        :return: The limit of this ListPipelineTemplatesResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPipelineTemplatesResponse.

        每页大小

        :param limit: The limit of this ListPipelineTemplatesResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this ListPipelineTemplatesResponse.

        总数

        :return: The total of this ListPipelineTemplatesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListPipelineTemplatesResponse.

        总数

        :param total: The total of this ListPipelineTemplatesResponse.
        :type total: int
        """
        self._total = total

    @property
    def templates(self):
        r"""Gets the templates of this ListPipelineTemplatesResponse.

        :return: The templates of this ListPipelineTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTemplateSimpleVO`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        r"""Sets the templates of this ListPipelineTemplatesResponse.

        :param templates: The templates of this ListPipelineTemplatesResponse.
        :type templates: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTemplateSimpleVO`]
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
        if not isinstance(other, ListPipelineTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
