# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSessionByUserNameResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_info_list': 'list[AppSession]'
    }

    attribute_map = {
        'session_info_list': 'session_info_list'
    }

    def __init__(self, session_info_list=None):
        r"""ListSessionByUserNameResponse

        The model defined in huaweicloud sdk

        :param session_info_list: 会话信息列表。
        :type session_info_list: list[:class:`huaweicloudsdkworkspaceapp.v1.AppSession`]
        """
        
        super(ListSessionByUserNameResponse, self).__init__()

        self._session_info_list = None
        self.discriminator = None

        if session_info_list is not None:
            self.session_info_list = session_info_list

    @property
    def session_info_list(self):
        r"""Gets the session_info_list of this ListSessionByUserNameResponse.

        会话信息列表。

        :return: The session_info_list of this ListSessionByUserNameResponse.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.AppSession`]
        """
        return self._session_info_list

    @session_info_list.setter
    def session_info_list(self, session_info_list):
        r"""Sets the session_info_list of this ListSessionByUserNameResponse.

        会话信息列表。

        :param session_info_list: The session_info_list of this ListSessionByUserNameResponse.
        :type session_info_list: list[:class:`huaweicloudsdkworkspaceapp.v1.AppSession`]
        """
        self._session_info_list = session_info_list

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
        if not isinstance(other, ListSessionByUserNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
