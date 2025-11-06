# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWatermarkRuleResponse(SdkResponse):

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
        'rules_infos': 'list[WatermarkRule]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'rules_infos': 'rules_infos',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, total=None, rules_infos=None, x_request_id=None):
        r"""ListWatermarkRuleResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param rules_infos: 响应数据
        :type rules_infos: list[:class:`huaweicloudsdklive.v1.WatermarkRule`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._total = None
        self._rules_infos = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if rules_infos is not None:
            self.rules_infos = rules_infos
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        r"""Gets the total of this ListWatermarkRuleResponse.

        总数

        :return: The total of this ListWatermarkRuleResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListWatermarkRuleResponse.

        总数

        :param total: The total of this ListWatermarkRuleResponse.
        :type total: int
        """
        self._total = total

    @property
    def rules_infos(self):
        r"""Gets the rules_infos of this ListWatermarkRuleResponse.

        响应数据

        :return: The rules_infos of this ListWatermarkRuleResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.WatermarkRule`]
        """
        return self._rules_infos

    @rules_infos.setter
    def rules_infos(self, rules_infos):
        r"""Sets the rules_infos of this ListWatermarkRuleResponse.

        响应数据

        :param rules_infos: The rules_infos of this ListWatermarkRuleResponse.
        :type rules_infos: list[:class:`huaweicloudsdklive.v1.WatermarkRule`]
        """
        self._rules_infos = rules_infos

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListWatermarkRuleResponse.

        :return: The x_request_id of this ListWatermarkRuleResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListWatermarkRuleResponse.

        :param x_request_id: The x_request_id of this ListWatermarkRuleResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListWatermarkRuleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListWatermarkRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
