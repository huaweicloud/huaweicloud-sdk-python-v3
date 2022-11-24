# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchApplicationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_info_list': 'list[AppInfo]',
        'app_total_count': 'int',
        'app_info_map': 'dict(str, AppInfo)'
    }

    attribute_map = {
        'app_info_list': 'app_info_list',
        'app_total_count': 'app_total_count',
        'app_info_map': 'app_info_map'
    }

    def __init__(self, app_info_list=None, app_total_count=None, app_info_map=None):
        """SearchApplicationResponse

        The model defined in huaweicloud sdk

        :param app_info_list: 组件列表。
        :type app_info_list: list[:class:`huaweicloudsdkapm.v1.AppInfo`]
        :param app_total_count: 组件总数目。
        :type app_total_count: int
        :param app_info_map: 组件名称和组件详情map表。
        :type app_info_map: dict(str, AppInfo)
        """
        
        super(SearchApplicationResponse, self).__init__()

        self._app_info_list = None
        self._app_total_count = None
        self._app_info_map = None
        self.discriminator = None

        if app_info_list is not None:
            self.app_info_list = app_info_list
        if app_total_count is not None:
            self.app_total_count = app_total_count
        if app_info_map is not None:
            self.app_info_map = app_info_map

    @property
    def app_info_list(self):
        """Gets the app_info_list of this SearchApplicationResponse.

        组件列表。

        :return: The app_info_list of this SearchApplicationResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.AppInfo`]
        """
        return self._app_info_list

    @app_info_list.setter
    def app_info_list(self, app_info_list):
        """Sets the app_info_list of this SearchApplicationResponse.

        组件列表。

        :param app_info_list: The app_info_list of this SearchApplicationResponse.
        :type app_info_list: list[:class:`huaweicloudsdkapm.v1.AppInfo`]
        """
        self._app_info_list = app_info_list

    @property
    def app_total_count(self):
        """Gets the app_total_count of this SearchApplicationResponse.

        组件总数目。

        :return: The app_total_count of this SearchApplicationResponse.
        :rtype: int
        """
        return self._app_total_count

    @app_total_count.setter
    def app_total_count(self, app_total_count):
        """Sets the app_total_count of this SearchApplicationResponse.

        组件总数目。

        :param app_total_count: The app_total_count of this SearchApplicationResponse.
        :type app_total_count: int
        """
        self._app_total_count = app_total_count

    @property
    def app_info_map(self):
        """Gets the app_info_map of this SearchApplicationResponse.

        组件名称和组件详情map表。

        :return: The app_info_map of this SearchApplicationResponse.
        :rtype: dict(str, AppInfo)
        """
        return self._app_info_map

    @app_info_map.setter
    def app_info_map(self, app_info_map):
        """Sets the app_info_map of this SearchApplicationResponse.

        组件名称和组件详情map表。

        :param app_info_map: The app_info_map of this SearchApplicationResponse.
        :type app_info_map: dict(str, AppInfo)
        """
        self._app_info_map = app_info_map

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
        if not isinstance(other, SearchApplicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
