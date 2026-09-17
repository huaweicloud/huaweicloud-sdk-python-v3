# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSlowLogTopInfoNewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_user_list': 'list[SlowLogTopInfo]',
        'top_ip_list': 'list[SlowLogTopInfo]',
        'top_db_list': 'list[SlowLogTopInfo]'
    }

    attribute_map = {
        'top_user_list': 'top_user_list',
        'top_ip_list': 'top_ip_list',
        'top_db_list': 'top_db_list'
    }

    def __init__(self, top_user_list=None, top_ip_list=None, top_db_list=None):
        r"""ShowSlowLogTopInfoNewResponse

        The model defined in huaweicloud sdk

        :param top_user_list: Top用户列表
        :type top_user_list: list[:class:`huaweicloudsdkdas.v3.SlowLogTopInfo`]
        :param top_ip_list: Top IP列表
        :type top_ip_list: list[:class:`huaweicloudsdkdas.v3.SlowLogTopInfo`]
        :param top_db_list: Top数据库列表
        :type top_db_list: list[:class:`huaweicloudsdkdas.v3.SlowLogTopInfo`]
        """
        
        super().__init__()

        self._top_user_list = None
        self._top_ip_list = None
        self._top_db_list = None
        self.discriminator = None

        if top_user_list is not None:
            self.top_user_list = top_user_list
        if top_ip_list is not None:
            self.top_ip_list = top_ip_list
        if top_db_list is not None:
            self.top_db_list = top_db_list

    @property
    def top_user_list(self):
        r"""Gets the top_user_list of this ShowSlowLogTopInfoNewResponse.

        Top用户列表

        :return: The top_user_list of this ShowSlowLogTopInfoNewResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowLogTopInfo`]
        """
        return self._top_user_list

    @top_user_list.setter
    def top_user_list(self, top_user_list):
        r"""Sets the top_user_list of this ShowSlowLogTopInfoNewResponse.

        Top用户列表

        :param top_user_list: The top_user_list of this ShowSlowLogTopInfoNewResponse.
        :type top_user_list: list[:class:`huaweicloudsdkdas.v3.SlowLogTopInfo`]
        """
        self._top_user_list = top_user_list

    @property
    def top_ip_list(self):
        r"""Gets the top_ip_list of this ShowSlowLogTopInfoNewResponse.

        Top IP列表

        :return: The top_ip_list of this ShowSlowLogTopInfoNewResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowLogTopInfo`]
        """
        return self._top_ip_list

    @top_ip_list.setter
    def top_ip_list(self, top_ip_list):
        r"""Sets the top_ip_list of this ShowSlowLogTopInfoNewResponse.

        Top IP列表

        :param top_ip_list: The top_ip_list of this ShowSlowLogTopInfoNewResponse.
        :type top_ip_list: list[:class:`huaweicloudsdkdas.v3.SlowLogTopInfo`]
        """
        self._top_ip_list = top_ip_list

    @property
    def top_db_list(self):
        r"""Gets the top_db_list of this ShowSlowLogTopInfoNewResponse.

        Top数据库列表

        :return: The top_db_list of this ShowSlowLogTopInfoNewResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SlowLogTopInfo`]
        """
        return self._top_db_list

    @top_db_list.setter
    def top_db_list(self, top_db_list):
        r"""Sets the top_db_list of this ShowSlowLogTopInfoNewResponse.

        Top数据库列表

        :param top_db_list: The top_db_list of this ShowSlowLogTopInfoNewResponse.
        :type top_db_list: list[:class:`huaweicloudsdkdas.v3.SlowLogTopInfo`]
        """
        self._top_db_list = top_db_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowSlowLogTopInfoNewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSlowLogTopInfoNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
