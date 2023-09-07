# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIncrementComponentsDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'update_time': 'str',
        'increment_components_list': 'list[IncreComponentDetail]'
    }

    attribute_map = {
        'update_time': 'update_time',
        'increment_components_list': 'increment_components_list'
    }

    def __init__(self, update_time=None, increment_components_list=None):
        """ShowIncrementComponentsDetailResponse

        The model defined in huaweicloud sdk

        :param update_time: 更新时间。
        :type update_time: str
        :param increment_components_list: 增量组件详情。
        :type increment_components_list: list[:class:`huaweicloudsdkdrs.v5.IncreComponentDetail`]
        """
        
        super(ShowIncrementComponentsDetailResponse, self).__init__()

        self._update_time = None
        self._increment_components_list = None
        self.discriminator = None

        if update_time is not None:
            self.update_time = update_time
        if increment_components_list is not None:
            self.increment_components_list = increment_components_list

    @property
    def update_time(self):
        """Gets the update_time of this ShowIncrementComponentsDetailResponse.

        更新时间。

        :return: The update_time of this ShowIncrementComponentsDetailResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowIncrementComponentsDetailResponse.

        更新时间。

        :param update_time: The update_time of this ShowIncrementComponentsDetailResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def increment_components_list(self):
        """Gets the increment_components_list of this ShowIncrementComponentsDetailResponse.

        增量组件详情。

        :return: The increment_components_list of this ShowIncrementComponentsDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.IncreComponentDetail`]
        """
        return self._increment_components_list

    @increment_components_list.setter
    def increment_components_list(self, increment_components_list):
        """Sets the increment_components_list of this ShowIncrementComponentsDetailResponse.

        增量组件详情。

        :param increment_components_list: The increment_components_list of this ShowIncrementComponentsDetailResponse.
        :type increment_components_list: list[:class:`huaweicloudsdkdrs.v5.IncreComponentDetail`]
        """
        self._increment_components_list = increment_components_list

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
        if not isinstance(other, ShowIncrementComponentsDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
