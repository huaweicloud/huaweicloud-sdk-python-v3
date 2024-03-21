# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCatalogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'name': 'str',
        'create_time': 'int',
        'parameters': 'dict(str, str)'
    }

    attribute_map = {
        'is_success': 'is_success',
        'name': 'name',
        'create_time': 'create_time',
        'parameters': 'parameters'
    }

    def __init__(self, is_success=None, name=None, create_time=None, parameters=None):
        """ShowCatalogResponse

        The model defined in huaweicloud sdk

        :param is_success: 是否成功。
        :type is_success: bool
        :param name: DLI侧catalog映射名称。
        :type name: str
        :param create_time: 创建时间
        :type create_time: int
        :param parameters: 
        :type parameters: dict(str, str)
        """
        
        super(ShowCatalogResponse, self).__init__()

        self._is_success = None
        self._name = None
        self._create_time = None
        self._parameters = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if name is not None:
            self.name = name
        if create_time is not None:
            self.create_time = create_time
        if parameters is not None:
            self.parameters = parameters

    @property
    def is_success(self):
        """Gets the is_success of this ShowCatalogResponse.

        是否成功。

        :return: The is_success of this ShowCatalogResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ShowCatalogResponse.

        是否成功。

        :param is_success: The is_success of this ShowCatalogResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def name(self):
        """Gets the name of this ShowCatalogResponse.

        DLI侧catalog映射名称。

        :return: The name of this ShowCatalogResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowCatalogResponse.

        DLI侧catalog映射名称。

        :param name: The name of this ShowCatalogResponse.
        :type name: str
        """
        self._name = name

    @property
    def create_time(self):
        """Gets the create_time of this ShowCatalogResponse.

        创建时间

        :return: The create_time of this ShowCatalogResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowCatalogResponse.

        创建时间

        :param create_time: The create_time of this ShowCatalogResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def parameters(self):
        """Gets the parameters of this ShowCatalogResponse.

        :return: The parameters of this ShowCatalogResponse.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ShowCatalogResponse.

        :param parameters: The parameters of this ShowCatalogResponse.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

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
        if not isinstance(other, ShowCatalogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
