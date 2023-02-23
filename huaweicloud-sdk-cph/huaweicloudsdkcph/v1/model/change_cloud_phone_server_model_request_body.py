# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeCloudPhoneServerModelRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'server_model_name': 'str',
        'phone_model_name': 'str',
        'extend_param': 'ChangeCloudPhoneServerModelRequestBodyExtendParam'
    }

    attribute_map = {
        'server_id': 'server_id',
        'server_model_name': 'server_model_name',
        'phone_model_name': 'phone_model_name',
        'extend_param': 'extend_param'
    }

    def __init__(self, server_id=None, server_model_name=None, phone_model_name=None, extend_param=None):
        """ChangeCloudPhoneServerModelRequestBody

        The model defined in huaweicloud sdk

        :param server_id: 云手机服务器的唯一标识。只有特定的服务器才能操作变更规格
        :type server_id: str
        :param server_model_name: 目标云手机服务器规格，不超过64个字节。仅允许相同代系服务器之间的规格切换。
        :type server_model_name: str
        :param phone_model_name: 目标云手机规格。要求与变更前云手机规格路数相同，与目标云手机服务器规格匹配。
        :type phone_model_name: str
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcph.v1.ChangeCloudPhoneServerModelRequestBodyExtendParam`
        """
        
        

        self._server_id = None
        self._server_model_name = None
        self._phone_model_name = None
        self._extend_param = None
        self.discriminator = None

        self.server_id = server_id
        self.server_model_name = server_model_name
        self.phone_model_name = phone_model_name
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def server_id(self):
        """Gets the server_id of this ChangeCloudPhoneServerModelRequestBody.

        云手机服务器的唯一标识。只有特定的服务器才能操作变更规格

        :return: The server_id of this ChangeCloudPhoneServerModelRequestBody.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ChangeCloudPhoneServerModelRequestBody.

        云手机服务器的唯一标识。只有特定的服务器才能操作变更规格

        :param server_id: The server_id of this ChangeCloudPhoneServerModelRequestBody.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def server_model_name(self):
        """Gets the server_model_name of this ChangeCloudPhoneServerModelRequestBody.

        目标云手机服务器规格，不超过64个字节。仅允许相同代系服务器之间的规格切换。

        :return: The server_model_name of this ChangeCloudPhoneServerModelRequestBody.
        :rtype: str
        """
        return self._server_model_name

    @server_model_name.setter
    def server_model_name(self, server_model_name):
        """Sets the server_model_name of this ChangeCloudPhoneServerModelRequestBody.

        目标云手机服务器规格，不超过64个字节。仅允许相同代系服务器之间的规格切换。

        :param server_model_name: The server_model_name of this ChangeCloudPhoneServerModelRequestBody.
        :type server_model_name: str
        """
        self._server_model_name = server_model_name

    @property
    def phone_model_name(self):
        """Gets the phone_model_name of this ChangeCloudPhoneServerModelRequestBody.

        目标云手机规格。要求与变更前云手机规格路数相同，与目标云手机服务器规格匹配。

        :return: The phone_model_name of this ChangeCloudPhoneServerModelRequestBody.
        :rtype: str
        """
        return self._phone_model_name

    @phone_model_name.setter
    def phone_model_name(self, phone_model_name):
        """Sets the phone_model_name of this ChangeCloudPhoneServerModelRequestBody.

        目标云手机规格。要求与变更前云手机规格路数相同，与目标云手机服务器规格匹配。

        :param phone_model_name: The phone_model_name of this ChangeCloudPhoneServerModelRequestBody.
        :type phone_model_name: str
        """
        self._phone_model_name = phone_model_name

    @property
    def extend_param(self):
        """Gets the extend_param of this ChangeCloudPhoneServerModelRequestBody.

        :return: The extend_param of this ChangeCloudPhoneServerModelRequestBody.
        :rtype: :class:`huaweicloudsdkcph.v1.ChangeCloudPhoneServerModelRequestBodyExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this ChangeCloudPhoneServerModelRequestBody.

        :param extend_param: The extend_param of this ChangeCloudPhoneServerModelRequestBody.
        :type extend_param: :class:`huaweicloudsdkcph.v1.ChangeCloudPhoneServerModelRequestBodyExtendParam`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, ChangeCloudPhoneServerModelRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
