# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowExecutionTimeTemplateTrendResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interval_millis': 'int',
        'item_list': 'list[ExTimeTrendItem]'
    }

    attribute_map = {
        'interval_millis': 'interval_millis',
        'item_list': 'item_list'
    }

    def __init__(self, interval_millis=None, item_list=None):
        r"""ShowExecutionTimeTemplateTrendResponse

        The model defined in huaweicloud sdk

        :param interval_millis: 趋势图的时间间隔
        :type interval_millis: int
        :param item_list: SQL趋势列表
        :type item_list: list[:class:`huaweicloudsdkdas.v3.ExTimeTrendItem`]
        """
        
        super().__init__()

        self._interval_millis = None
        self._item_list = None
        self.discriminator = None

        if interval_millis is not None:
            self.interval_millis = interval_millis
        if item_list is not None:
            self.item_list = item_list

    @property
    def interval_millis(self):
        r"""Gets the interval_millis of this ShowExecutionTimeTemplateTrendResponse.

        趋势图的时间间隔

        :return: The interval_millis of this ShowExecutionTimeTemplateTrendResponse.
        :rtype: int
        """
        return self._interval_millis

    @interval_millis.setter
    def interval_millis(self, interval_millis):
        r"""Sets the interval_millis of this ShowExecutionTimeTemplateTrendResponse.

        趋势图的时间间隔

        :param interval_millis: The interval_millis of this ShowExecutionTimeTemplateTrendResponse.
        :type interval_millis: int
        """
        self._interval_millis = interval_millis

    @property
    def item_list(self):
        r"""Gets the item_list of this ShowExecutionTimeTemplateTrendResponse.

        SQL趋势列表

        :return: The item_list of this ShowExecutionTimeTemplateTrendResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ExTimeTrendItem`]
        """
        return self._item_list

    @item_list.setter
    def item_list(self, item_list):
        r"""Sets the item_list of this ShowExecutionTimeTemplateTrendResponse.

        SQL趋势列表

        :param item_list: The item_list of this ShowExecutionTimeTemplateTrendResponse.
        :type item_list: list[:class:`huaweicloudsdkdas.v3.ExTimeTrendItem`]
        """
        self._item_list = item_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowExecutionTimeTemplateTrendResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowExecutionTimeTemplateTrendResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
