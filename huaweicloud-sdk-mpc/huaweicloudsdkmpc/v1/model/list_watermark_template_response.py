# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWatermarkTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'templates': 'list[WatermarkTemplate]'
    }

    attribute_map = {
        'total': 'total',
        'templates': 'templates'
    }

    def __init__(self, total=None, templates=None):
        r"""ListWatermarkTemplateResponse

        The model defined in huaweicloud sdk

        :param total: 水印模板总数。
        :type total: int
        :param templates: 水印模板
        :type templates: list[:class:`huaweicloudsdkmpc.v1.WatermarkTemplate`]
        """
        
        super(ListWatermarkTemplateResponse, self).__init__()

        self._total = None
        self._templates = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if templates is not None:
            self.templates = templates

    @property
    def total(self):
        r"""Gets the total of this ListWatermarkTemplateResponse.

        水印模板总数。

        :return: The total of this ListWatermarkTemplateResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListWatermarkTemplateResponse.

        水印模板总数。

        :param total: The total of this ListWatermarkTemplateResponse.
        :type total: int
        """
        self._total = total

    @property
    def templates(self):
        r"""Gets the templates of this ListWatermarkTemplateResponse.

        水印模板

        :return: The templates of this ListWatermarkTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.WatermarkTemplate`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        r"""Sets the templates of this ListWatermarkTemplateResponse.

        水印模板

        :param templates: The templates of this ListWatermarkTemplateResponse.
        :type templates: list[:class:`huaweicloudsdkmpc.v1.WatermarkTemplate`]
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
        if not isinstance(other, ListWatermarkTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
