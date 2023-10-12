# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSessionTypeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_types': 'list[SessionTypeEntity]'
    }

    attribute_map = {
        'session_types': 'session_types'
    }

    def __init__(self, session_types=None):
        """ListSessionTypeResponse

        The model defined in huaweicloud sdk

        :param session_types: 会话列表
        :type session_types: list[:class:`huaweicloudsdkworkspaceapp.v1.SessionTypeEntity`]
        """
        
        super(ListSessionTypeResponse, self).__init__()

        self._session_types = None
        self.discriminator = None

        if session_types is not None:
            self.session_types = session_types

    @property
    def session_types(self):
        """Gets the session_types of this ListSessionTypeResponse.

        会话列表

        :return: The session_types of this ListSessionTypeResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.SessionTypeEntity`]
        """
        return self._session_types

    @session_types.setter
    def session_types(self, session_types):
        """Sets the session_types of this ListSessionTypeResponse.

        会话列表

        :param session_types: The session_types of this ListSessionTypeResponse.
        :type session_types: list[:class:`huaweicloudsdkworkspaceapp.v1.SessionTypeEntity`]
        """
        self._session_types = session_types

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
        if not isinstance(other, ListSessionTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
