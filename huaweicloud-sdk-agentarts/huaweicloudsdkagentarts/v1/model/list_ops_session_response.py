# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsSessionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'session_list': 'list[OpsSessionDetail]'
    }

    attribute_map = {
        'total': 'total',
        'session_list': 'session_list'
    }

    def __init__(self, total=None, session_list=None):
        r"""ListOpsSessionResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param session_list: 会话列表
        :type session_list: list[:class:`huaweicloudsdkagentarts.v1.OpsSessionDetail`]
        """
        
        super().__init__()

        self._total = None
        self._session_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if session_list is not None:
            self.session_list = session_list

    @property
    def total(self):
        r"""Gets the total of this ListOpsSessionResponse.

        总数

        :return: The total of this ListOpsSessionResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListOpsSessionResponse.

        总数

        :param total: The total of this ListOpsSessionResponse.
        :type total: int
        """
        self._total = total

    @property
    def session_list(self):
        r"""Gets the session_list of this ListOpsSessionResponse.

        会话列表

        :return: The session_list of this ListOpsSessionResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsSessionDetail`]
        """
        return self._session_list

    @session_list.setter
    def session_list(self, session_list):
        r"""Sets the session_list of this ListOpsSessionResponse.

        会话列表

        :param session_list: The session_list of this ListOpsSessionResponse.
        :type session_list: list[:class:`huaweicloudsdkagentarts.v1.OpsSessionDetail`]
        """
        self._session_list = session_list

    def to_dict(self):
        import warnings
        warnings.warn("ListOpsSessionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOpsSessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
