# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAsyncHistoryCommandsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'commands': 'list[AsyncDeviceListCommand]',
        'page': 'HistoryCommandPage'
    }

    attribute_map = {
        'commands': 'commands',
        'page': 'page'
    }

    def __init__(self, commands=None, page=None):
        r"""ListAsyncHistoryCommandsResponse

        The model defined in huaweicloud sdk

        :param commands: 设备历史命令列表。
        :type commands: list[:class:`huaweicloudsdkiotda.v5.AsyncDeviceListCommand`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.HistoryCommandPage`
        """
        
        super(ListAsyncHistoryCommandsResponse, self).__init__()

        self._commands = None
        self._page = None
        self.discriminator = None

        if commands is not None:
            self.commands = commands
        if page is not None:
            self.page = page

    @property
    def commands(self):
        r"""Gets the commands of this ListAsyncHistoryCommandsResponse.

        设备历史命令列表。

        :return: The commands of this ListAsyncHistoryCommandsResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.AsyncDeviceListCommand`]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        r"""Sets the commands of this ListAsyncHistoryCommandsResponse.

        设备历史命令列表。

        :param commands: The commands of this ListAsyncHistoryCommandsResponse.
        :type commands: list[:class:`huaweicloudsdkiotda.v5.AsyncDeviceListCommand`]
        """
        self._commands = commands

    @property
    def page(self):
        r"""Gets the page of this ListAsyncHistoryCommandsResponse.

        :return: The page of this ListAsyncHistoryCommandsResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.HistoryCommandPage`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListAsyncHistoryCommandsResponse.

        :param page: The page of this ListAsyncHistoryCommandsResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.HistoryCommandPage`
        """
        self._page = page

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
        if not isinstance(other, ListAsyncHistoryCommandsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
