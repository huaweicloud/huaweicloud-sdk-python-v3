# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSeveritiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'show': 'bool',
        'severity_list': 'list[SeverityV2Do]'
    }

    attribute_map = {
        'show': 'show',
        'severity_list': 'severity_list'
    }

    def __init__(self, show=None, severity_list=None):
        """ListSeveritiesResponse

        The model defined in huaweicloud sdk

        :param show: 是否展示
        :type show: bool
        :param severity_list: 严重性列表
        :type severity_list: list[:class:`huaweicloudsdkosm.v2.SeverityV2Do`]
        """
        
        super(ListSeveritiesResponse, self).__init__()

        self._show = None
        self._severity_list = None
        self.discriminator = None

        if show is not None:
            self.show = show
        if severity_list is not None:
            self.severity_list = severity_list

    @property
    def show(self):
        """Gets the show of this ListSeveritiesResponse.

        是否展示

        :return: The show of this ListSeveritiesResponse.
        :rtype: bool
        """
        return self._show

    @show.setter
    def show(self, show):
        """Sets the show of this ListSeveritiesResponse.

        是否展示

        :param show: The show of this ListSeveritiesResponse.
        :type show: bool
        """
        self._show = show

    @property
    def severity_list(self):
        """Gets the severity_list of this ListSeveritiesResponse.

        严重性列表

        :return: The severity_list of this ListSeveritiesResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.SeverityV2Do`]
        """
        return self._severity_list

    @severity_list.setter
    def severity_list(self, severity_list):
        """Sets the severity_list of this ListSeveritiesResponse.

        严重性列表

        :param severity_list: The severity_list of this ListSeveritiesResponse.
        :type severity_list: list[:class:`huaweicloudsdkosm.v2.SeverityV2Do`]
        """
        self._severity_list = severity_list

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
        if not isinstance(other, ListSeveritiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
