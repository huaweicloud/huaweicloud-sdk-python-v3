# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWarmPoolInstancesNewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_info': 'PageInfo',
        'warm_pool_instances': 'list[WarmPoolInstance]'
    }

    attribute_map = {
        'page_info': 'page_info',
        'warm_pool_instances': 'warm_pool_instances'
    }

    def __init__(self, page_info=None, warm_pool_instances=None):
        r"""ListWarmPoolInstancesNewResponse

        The model defined in huaweicloud sdk

        :param page_info: 
        :type page_info: :class:`huaweicloudsdkas.v1.PageInfo`
        :param warm_pool_instances: 暖池实例列表
        :type warm_pool_instances: list[:class:`huaweicloudsdkas.v1.WarmPoolInstance`]
        """
        
        super().__init__()

        self._page_info = None
        self._warm_pool_instances = None
        self.discriminator = None

        if page_info is not None:
            self.page_info = page_info
        if warm_pool_instances is not None:
            self.warm_pool_instances = warm_pool_instances

    @property
    def page_info(self):
        r"""Gets the page_info of this ListWarmPoolInstancesNewResponse.

        :return: The page_info of this ListWarmPoolInstancesNewResponse.
        :rtype: :class:`huaweicloudsdkas.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListWarmPoolInstancesNewResponse.

        :param page_info: The page_info of this ListWarmPoolInstancesNewResponse.
        :type page_info: :class:`huaweicloudsdkas.v1.PageInfo`
        """
        self._page_info = page_info

    @property
    def warm_pool_instances(self):
        r"""Gets the warm_pool_instances of this ListWarmPoolInstancesNewResponse.

        暖池实例列表

        :return: The warm_pool_instances of this ListWarmPoolInstancesNewResponse.
        :rtype: list[:class:`huaweicloudsdkas.v1.WarmPoolInstance`]
        """
        return self._warm_pool_instances

    @warm_pool_instances.setter
    def warm_pool_instances(self, warm_pool_instances):
        r"""Sets the warm_pool_instances of this ListWarmPoolInstancesNewResponse.

        暖池实例列表

        :param warm_pool_instances: The warm_pool_instances of this ListWarmPoolInstancesNewResponse.
        :type warm_pool_instances: list[:class:`huaweicloudsdkas.v1.WarmPoolInstance`]
        """
        self._warm_pool_instances = warm_pool_instances

    def to_dict(self):
        import warnings
        warnings.warn("ListWarmPoolInstancesNewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListWarmPoolInstancesNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
