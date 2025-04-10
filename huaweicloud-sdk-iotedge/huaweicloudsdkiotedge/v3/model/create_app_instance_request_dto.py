# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppInstanceRequestDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'namespace': 'str',
        'app_id': 'str',
        'app_version': 'str',
        'values': 'object'
    }

    attribute_map = {
        'id': 'id',
        'namespace': 'namespace',
        'app_id': 'app_id',
        'app_version': 'app_version',
        'values': 'values'
    }

    def __init__(self, id=None, namespace=None, app_id=None, app_version=None, values=None):
        r"""CreateAppInstanceRequestDTO

        The model defined in huaweicloud sdk

        :param id: 应用实例ID
        :type id: str
        :param namespace: 边缘集群命名空间
        :type namespace: str
        :param app_id: 应用ID
        :type app_id: str
        :param app_version: 应用版本
        :type app_version: str
        :param values: 应用实例chart配置
        :type values: object
        """
        
        

        self._id = None
        self._namespace = None
        self._app_id = None
        self._app_version = None
        self._values = None
        self.discriminator = None

        self.id = id
        if namespace is not None:
            self.namespace = namespace
        self.app_id = app_id
        self.app_version = app_version
        if values is not None:
            self.values = values

    @property
    def id(self):
        r"""Gets the id of this CreateAppInstanceRequestDTO.

        应用实例ID

        :return: The id of this CreateAppInstanceRequestDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateAppInstanceRequestDTO.

        应用实例ID

        :param id: The id of this CreateAppInstanceRequestDTO.
        :type id: str
        """
        self._id = id

    @property
    def namespace(self):
        r"""Gets the namespace of this CreateAppInstanceRequestDTO.

        边缘集群命名空间

        :return: The namespace of this CreateAppInstanceRequestDTO.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CreateAppInstanceRequestDTO.

        边缘集群命名空间

        :param namespace: The namespace of this CreateAppInstanceRequestDTO.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def app_id(self):
        r"""Gets the app_id of this CreateAppInstanceRequestDTO.

        应用ID

        :return: The app_id of this CreateAppInstanceRequestDTO.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this CreateAppInstanceRequestDTO.

        应用ID

        :param app_id: The app_id of this CreateAppInstanceRequestDTO.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_version(self):
        r"""Gets the app_version of this CreateAppInstanceRequestDTO.

        应用版本

        :return: The app_version of this CreateAppInstanceRequestDTO.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this CreateAppInstanceRequestDTO.

        应用版本

        :param app_version: The app_version of this CreateAppInstanceRequestDTO.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def values(self):
        r"""Gets the values of this CreateAppInstanceRequestDTO.

        应用实例chart配置

        :return: The values of this CreateAppInstanceRequestDTO.
        :rtype: object
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this CreateAppInstanceRequestDTO.

        应用实例chart配置

        :param values: The values of this CreateAppInstanceRequestDTO.
        :type values: object
        """
        self._values = values

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
        if not isinstance(other, CreateAppInstanceRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
