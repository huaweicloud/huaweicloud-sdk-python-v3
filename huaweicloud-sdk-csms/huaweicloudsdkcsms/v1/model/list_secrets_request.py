# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecretsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'marker': 'str',
        'event_name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'event_name': 'event_name'
    }

    def __init__(self, limit=None, marker=None, event_name=None):
        r"""ListSecretsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。  默认值：50。
        :type limit: str
        :param marker: 分页查询起始的凭据名称，为空时为查询第一页
        :type marker: str
        :param event_name: 指定事件名称时，仅返回关联该事件的凭据
        :type event_name: str
        """
        
        

        self._limit = None
        self._marker = None
        self._event_name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if event_name is not None:
            self.event_name = event_name

    @property
    def limit(self):
        r"""Gets the limit of this ListSecretsRequest.

        每页返回的个数。  默认值：50。

        :return: The limit of this ListSecretsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecretsRequest.

        每页返回的个数。  默认值：50。

        :param limit: The limit of this ListSecretsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListSecretsRequest.

        分页查询起始的凭据名称，为空时为查询第一页

        :return: The marker of this ListSecretsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListSecretsRequest.

        分页查询起始的凭据名称，为空时为查询第一页

        :param marker: The marker of this ListSecretsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def event_name(self):
        r"""Gets the event_name of this ListSecretsRequest.

        指定事件名称时，仅返回关联该事件的凭据

        :return: The event_name of this ListSecretsRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ListSecretsRequest.

        指定事件名称时，仅返回关联该事件的凭据

        :param event_name: The event_name of this ListSecretsRequest.
        :type event_name: str
        """
        self._event_name = event_name

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
        if not isinstance(other, ListSecretsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
