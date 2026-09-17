# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopTrendResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_data_list': 'list[TopDataInfo]'
    }

    attribute_map = {
        'top_data_list': 'top_data_list'
    }

    def __init__(self, top_data_list=None):
        r"""ShowTopTrendResponse

        The model defined in huaweicloud sdk

        :param top_data_list: Top库表数据列表
        :type top_data_list: list[:class:`huaweicloudsdkdas.v3.TopDataInfo`]
        """
        
        super().__init__()

        self._top_data_list = None
        self.discriminator = None

        if top_data_list is not None:
            self.top_data_list = top_data_list

    @property
    def top_data_list(self):
        r"""Gets the top_data_list of this ShowTopTrendResponse.

        Top库表数据列表

        :return: The top_data_list of this ShowTopTrendResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.TopDataInfo`]
        """
        return self._top_data_list

    @top_data_list.setter
    def top_data_list(self, top_data_list):
        r"""Sets the top_data_list of this ShowTopTrendResponse.

        Top库表数据列表

        :param top_data_list: The top_data_list of this ShowTopTrendResponse.
        :type top_data_list: list[:class:`huaweicloudsdkdas.v3.TopDataInfo`]
        """
        self._top_data_list = top_data_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowTopTrendResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTopTrendResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
