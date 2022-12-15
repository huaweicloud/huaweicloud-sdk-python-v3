# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportConnectionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'params': 'list[ConnectionParam]',
        'same_name_policy': 'str'
    }

    attribute_map = {
        'path': 'path',
        'params': 'params',
        'same_name_policy': 'sameNamePolicy'
    }

    def __init__(self, path=None, params=None, same_name_policy=None):
        """ImportConnectionReq

        The model defined in huaweicloud sdk

        :param path: 
        :type path: str
        :param params: 连接参数
        :type params: list[:class:`huaweicloudsdkdlf.v1.ConnectionParam`]
        :param same_name_policy: 
        :type same_name_policy: str
        """
        
        

        self._path = None
        self._params = None
        self._same_name_policy = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if params is not None:
            self.params = params
        if same_name_policy is not None:
            self.same_name_policy = same_name_policy

    @property
    def path(self):
        """Gets the path of this ImportConnectionReq.

        :return: The path of this ImportConnectionReq.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ImportConnectionReq.

        :param path: The path of this ImportConnectionReq.
        :type path: str
        """
        self._path = path

    @property
    def params(self):
        """Gets the params of this ImportConnectionReq.

        连接参数

        :return: The params of this ImportConnectionReq.
        :rtype: list[:class:`huaweicloudsdkdlf.v1.ConnectionParam`]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ImportConnectionReq.

        连接参数

        :param params: The params of this ImportConnectionReq.
        :type params: list[:class:`huaweicloudsdkdlf.v1.ConnectionParam`]
        """
        self._params = params

    @property
    def same_name_policy(self):
        """Gets the same_name_policy of this ImportConnectionReq.

        :return: The same_name_policy of this ImportConnectionReq.
        :rtype: str
        """
        return self._same_name_policy

    @same_name_policy.setter
    def same_name_policy(self, same_name_policy):
        """Sets the same_name_policy of this ImportConnectionReq.

        :param same_name_policy: The same_name_policy of this ImportConnectionReq.
        :type same_name_policy: str
        """
        self._same_name_policy = same_name_policy

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
        if not isinstance(other, ImportConnectionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
