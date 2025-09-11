# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopSessionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_ids': 'list[str]',
        'success': 'bool'
    }

    attribute_map = {
        'session_ids': 'session_ids',
        'success': 'success'
    }

    def __init__(self, session_ids=None, success=None):
        r"""StopSessionResponse

        The model defined in huaweicloud sdk

        :param session_ids: **参数解释**： 查杀指定会话ID列表。
        :type session_ids: list[str]
        :param success: **参数解释**： 结束会话操作执行是否成功。 **取值范围**: - true：成功。 - false：失败。
        :type success: bool
        """
        
        super(StopSessionResponse, self).__init__()

        self._session_ids = None
        self._success = None
        self.discriminator = None

        if session_ids is not None:
            self.session_ids = session_ids
        if success is not None:
            self.success = success

    @property
    def session_ids(self):
        r"""Gets the session_ids of this StopSessionResponse.

        **参数解释**： 查杀指定会话ID列表。

        :return: The session_ids of this StopSessionResponse.
        :rtype: list[str]
        """
        return self._session_ids

    @session_ids.setter
    def session_ids(self, session_ids):
        r"""Sets the session_ids of this StopSessionResponse.

        **参数解释**： 查杀指定会话ID列表。

        :param session_ids: The session_ids of this StopSessionResponse.
        :type session_ids: list[str]
        """
        self._session_ids = session_ids

    @property
    def success(self):
        r"""Gets the success of this StopSessionResponse.

        **参数解释**： 结束会话操作执行是否成功。 **取值范围**: - true：成功。 - false：失败。

        :return: The success of this StopSessionResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this StopSessionResponse.

        **参数解释**： 结束会话操作执行是否成功。 **取值范围**: - true：成功。 - false：失败。

        :param success: The success of this StopSessionResponse.
        :type success: bool
        """
        self._success = success

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
        if not isinstance(other, StopSessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
