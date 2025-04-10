# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackendRequestPara:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'position': 'str',
        'backend_para_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'position': 'position',
        'backend_para_name': 'backend_para_name'
    }

    def __init__(self, name=None, position=None, backend_para_name=None):
        r"""BackendRequestPara

        The model defined in huaweicloud sdk

        :param name: api请求参数名称
        :type name: str
        :param position: 参数位置
        :type position: str
        :param backend_para_name: 对应的后端参数
        :type backend_para_name: str
        """
        
        

        self._name = None
        self._position = None
        self._backend_para_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if position is not None:
            self.position = position
        if backend_para_name is not None:
            self.backend_para_name = backend_para_name

    @property
    def name(self):
        r"""Gets the name of this BackendRequestPara.

        api请求参数名称

        :return: The name of this BackendRequestPara.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BackendRequestPara.

        api请求参数名称

        :param name: The name of this BackendRequestPara.
        :type name: str
        """
        self._name = name

    @property
    def position(self):
        r"""Gets the position of this BackendRequestPara.

        参数位置

        :return: The position of this BackendRequestPara.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this BackendRequestPara.

        参数位置

        :param position: The position of this BackendRequestPara.
        :type position: str
        """
        self._position = position

    @property
    def backend_para_name(self):
        r"""Gets the backend_para_name of this BackendRequestPara.

        对应的后端参数

        :return: The backend_para_name of this BackendRequestPara.
        :rtype: str
        """
        return self._backend_para_name

    @backend_para_name.setter
    def backend_para_name(self, backend_para_name):
        r"""Sets the backend_para_name of this BackendRequestPara.

        对应的后端参数

        :param backend_para_name: The backend_para_name of this BackendRequestPara.
        :type backend_para_name: str
        """
        self._backend_para_name = backend_para_name

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
        if not isinstance(other, BackendRequestPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
