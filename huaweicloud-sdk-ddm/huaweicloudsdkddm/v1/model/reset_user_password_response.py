# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetUserPasswordResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'instance_id': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'success': 'success',
        'instance_id': 'instance_id',
        'user_name': 'user_name'
    }

    def __init__(self, success=None, instance_id=None, user_name=None):
        """ResetUserPasswordResponse

        The model defined in huaweicloud sdk

        :param success: 操作是否成功。
        :type success: bool
        :param instance_id: DDM实例ID。
        :type instance_id: str
        :param user_name: DDM账号名称
        :type user_name: str
        """
        
        super(ResetUserPasswordResponse, self).__init__()

        self._success = None
        self._instance_id = None
        self._user_name = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if instance_id is not None:
            self.instance_id = instance_id
        if user_name is not None:
            self.user_name = user_name

    @property
    def success(self):
        """Gets the success of this ResetUserPasswordResponse.

        操作是否成功。

        :return: The success of this ResetUserPasswordResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ResetUserPasswordResponse.

        操作是否成功。

        :param success: The success of this ResetUserPasswordResponse.
        :type success: bool
        """
        self._success = success

    @property
    def instance_id(self):
        """Gets the instance_id of this ResetUserPasswordResponse.

        DDM实例ID。

        :return: The instance_id of this ResetUserPasswordResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ResetUserPasswordResponse.

        DDM实例ID。

        :param instance_id: The instance_id of this ResetUserPasswordResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def user_name(self):
        """Gets the user_name of this ResetUserPasswordResponse.

        DDM账号名称

        :return: The user_name of this ResetUserPasswordResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ResetUserPasswordResponse.

        DDM账号名称

        :param user_name: The user_name of this ResetUserPasswordResponse.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, ResetUserPasswordResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
