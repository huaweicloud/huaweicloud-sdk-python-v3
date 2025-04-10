# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotifiedHistoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notified_histories': 'list[NotifiedHistoriesResult]'
    }

    attribute_map = {
        'notified_histories': 'notified_histories'
    }

    def __init__(self, notified_histories=None):
        r"""ListNotifiedHistoriesResponse

        The model defined in huaweicloud sdk

        :param notified_histories: 通知历史列表。
        :type notified_histories: list[:class:`huaweicloudsdkaom.v2.NotifiedHistoriesResult`]
        """
        
        super(ListNotifiedHistoriesResponse, self).__init__()

        self._notified_histories = None
        self.discriminator = None

        if notified_histories is not None:
            self.notified_histories = notified_histories

    @property
    def notified_histories(self):
        r"""Gets the notified_histories of this ListNotifiedHistoriesResponse.

        通知历史列表。

        :return: The notified_histories of this ListNotifiedHistoriesResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.NotifiedHistoriesResult`]
        """
        return self._notified_histories

    @notified_histories.setter
    def notified_histories(self, notified_histories):
        r"""Sets the notified_histories of this ListNotifiedHistoriesResponse.

        通知历史列表。

        :param notified_histories: The notified_histories of this ListNotifiedHistoriesResponse.
        :type notified_histories: list[:class:`huaweicloudsdkaom.v2.NotifiedHistoriesResult`]
        """
        self._notified_histories = notified_histories

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
        if not isinstance(other, ListNotifiedHistoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
