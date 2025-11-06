# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventOperatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_accept_list': 'list[str]'
    }

    attribute_map = {
        'operate_accept_list': 'operate_accept_list'
    }

    def __init__(self, operate_accept_list=None):
        r"""ListEventOperatesResponse

        The model defined in huaweicloud sdk

        :param operate_accept_list: 支持的处理操作
        :type operate_accept_list: list[str]
        """
        
        super().__init__()

        self._operate_accept_list = None
        self.discriminator = None

        if operate_accept_list is not None:
            self.operate_accept_list = operate_accept_list

    @property
    def operate_accept_list(self):
        r"""Gets the operate_accept_list of this ListEventOperatesResponse.

        支持的处理操作

        :return: The operate_accept_list of this ListEventOperatesResponse.
        :rtype: list[str]
        """
        return self._operate_accept_list

    @operate_accept_list.setter
    def operate_accept_list(self, operate_accept_list):
        r"""Sets the operate_accept_list of this ListEventOperatesResponse.

        支持的处理操作

        :param operate_accept_list: The operate_accept_list of this ListEventOperatesResponse.
        :type operate_accept_list: list[str]
        """
        self._operate_accept_list = operate_accept_list

    def to_dict(self):
        import warnings
        warnings.warn("ListEventOperatesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListEventOperatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
