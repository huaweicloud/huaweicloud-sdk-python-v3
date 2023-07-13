# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailsOfCustomAuthorizersV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'authorizer_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'authorizer_id': 'authorizer_id'
    }

    def __init__(self, instance_id=None, authorizer_id=None):
        """ShowDetailsOfCustomAuthorizersV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param authorizer_id: 自定义认证的编号
        :type authorizer_id: str
        """
        
        

        self._instance_id = None
        self._authorizer_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.authorizer_id = authorizer_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowDetailsOfCustomAuthorizersV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this ShowDetailsOfCustomAuthorizersV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowDetailsOfCustomAuthorizersV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this ShowDetailsOfCustomAuthorizersV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def authorizer_id(self):
        """Gets the authorizer_id of this ShowDetailsOfCustomAuthorizersV2Request.

        自定义认证的编号

        :return: The authorizer_id of this ShowDetailsOfCustomAuthorizersV2Request.
        :rtype: str
        """
        return self._authorizer_id

    @authorizer_id.setter
    def authorizer_id(self, authorizer_id):
        """Sets the authorizer_id of this ShowDetailsOfCustomAuthorizersV2Request.

        自定义认证的编号

        :param authorizer_id: The authorizer_id of this ShowDetailsOfCustomAuthorizersV2Request.
        :type authorizer_id: str
        """
        self._authorizer_id = authorizer_id

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
        if not isinstance(other, ShowDetailsOfCustomAuthorizersV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
