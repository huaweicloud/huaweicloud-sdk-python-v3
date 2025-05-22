# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatabaseOmUserStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'int',
        'error_msg': 'str',
        'om_user_info': 'DatabaseOmUserInfo'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'om_user_info': 'om_user_info'
    }

    def __init__(self, error_code=None, error_msg=None, om_user_info=None):
        r"""ShowDatabaseOmUserStatusResponse

        The model defined in huaweicloud sdk

        :param error_code: **参数解释**： 错误码。非0皆为异常场景。 **取值范围**： 不涉及。
        :type error_code: int
        :param error_msg: **参数解释**： 错误信息。 **取值范围**： 不涉及。
        :type error_msg: str
        :param om_user_info: 
        :type om_user_info: :class:`huaweicloudsdkdws.v2.DatabaseOmUserInfo`
        """
        
        super(ShowDatabaseOmUserStatusResponse, self).__init__()

        self._error_code = None
        self._error_msg = None
        self._om_user_info = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if om_user_info is not None:
            self.om_user_info = om_user_info

    @property
    def error_code(self):
        r"""Gets the error_code of this ShowDatabaseOmUserStatusResponse.

        **参数解释**： 错误码。非0皆为异常场景。 **取值范围**： 不涉及。

        :return: The error_code of this ShowDatabaseOmUserStatusResponse.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ShowDatabaseOmUserStatusResponse.

        **参数解释**： 错误码。非0皆为异常场景。 **取值范围**： 不涉及。

        :param error_code: The error_code of this ShowDatabaseOmUserStatusResponse.
        :type error_code: int
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ShowDatabaseOmUserStatusResponse.

        **参数解释**： 错误信息。 **取值范围**： 不涉及。

        :return: The error_msg of this ShowDatabaseOmUserStatusResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ShowDatabaseOmUserStatusResponse.

        **参数解释**： 错误信息。 **取值范围**： 不涉及。

        :param error_msg: The error_msg of this ShowDatabaseOmUserStatusResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def om_user_info(self):
        r"""Gets the om_user_info of this ShowDatabaseOmUserStatusResponse.

        :return: The om_user_info of this ShowDatabaseOmUserStatusResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.DatabaseOmUserInfo`
        """
        return self._om_user_info

    @om_user_info.setter
    def om_user_info(self, om_user_info):
        r"""Sets the om_user_info of this ShowDatabaseOmUserStatusResponse.

        :param om_user_info: The om_user_info of this ShowDatabaseOmUserStatusResponse.
        :type om_user_info: :class:`huaweicloudsdkdws.v2.DatabaseOmUserInfo`
        """
        self._om_user_info = om_user_info

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
        if not isinstance(other, ShowDatabaseOmUserStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
