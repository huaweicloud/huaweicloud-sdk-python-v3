# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteDatabaseOmUserActionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'om_user_info': 'DatabaseOmUserInfo'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'om_user_info': 'om_user_info'
    }

    def __init__(self, error_code=None, error_msg=None, om_user_info=None):
        """ExecuteDatabaseOmUserActionResponse

        The model defined in huaweicloud sdk

        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        :param om_user_info: 
        :type om_user_info: :class:`huaweicloudsdkdws.v2.DatabaseOmUserInfo`
        """
        
        super(ExecuteDatabaseOmUserActionResponse, self).__init__()

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
        """Gets the error_code of this ExecuteDatabaseOmUserActionResponse.

        错误码

        :return: The error_code of this ExecuteDatabaseOmUserActionResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ExecuteDatabaseOmUserActionResponse.

        错误码

        :param error_code: The error_code of this ExecuteDatabaseOmUserActionResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ExecuteDatabaseOmUserActionResponse.

        错误信息

        :return: The error_msg of this ExecuteDatabaseOmUserActionResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ExecuteDatabaseOmUserActionResponse.

        错误信息

        :param error_msg: The error_msg of this ExecuteDatabaseOmUserActionResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def om_user_info(self):
        """Gets the om_user_info of this ExecuteDatabaseOmUserActionResponse.

        :return: The om_user_info of this ExecuteDatabaseOmUserActionResponse.
        :rtype: :class:`huaweicloudsdkdws.v2.DatabaseOmUserInfo`
        """
        return self._om_user_info

    @om_user_info.setter
    def om_user_info(self, om_user_info):
        """Sets the om_user_info of this ExecuteDatabaseOmUserActionResponse.

        :param om_user_info: The om_user_info of this ExecuteDatabaseOmUserActionResponse.
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
        if not isinstance(other, ExecuteDatabaseOmUserActionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
