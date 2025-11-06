# coding: utf-8

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
        'template_infos': 'list[WatermarkTemplate]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'template_infos': 'template_infos',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, total=None, template_infos=None, x_request_id=None):
        r"""ListWatermarkTemplateResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param template_infos: 响应数据
        :type template_infos: list[:class:`huaweicloudsdklive.v1.WatermarkTemplate`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._total = None
        self._template_infos = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if template_infos is not None:
            self.template_infos = template_infos
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        r"""Gets the total of this ListWatermarkTemplateResponse.

        总数

        :return: The total of this ListWatermarkTemplateResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListWatermarkTemplateResponse.

        总数

        :param total: The total of this ListWatermarkTemplateResponse.
        :type total: int
        """
        self._total = total

    @property
    def template_infos(self):
        r"""Gets the template_infos of this ListWatermarkTemplateResponse.

        响应数据

        :return: The template_infos of this ListWatermarkTemplateResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.WatermarkTemplate`]
        """
        return self._template_infos

    @template_infos.setter
    def template_infos(self, template_infos):
        r"""Sets the template_infos of this ListWatermarkTemplateResponse.

        响应数据

        :param template_infos: The template_infos of this ListWatermarkTemplateResponse.
        :type template_infos: list[:class:`huaweicloudsdklive.v1.WatermarkTemplate`]
        """
        self._template_infos = template_infos

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListWatermarkTemplateResponse.

        :return: The x_request_id of this ListWatermarkTemplateResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListWatermarkTemplateResponse.

        :param x_request_id: The x_request_id of this ListWatermarkTemplateResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListWatermarkTemplateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
