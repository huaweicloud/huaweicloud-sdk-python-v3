# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceInstanceInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'SourceRef',
        'name': 'str',
        'description': 'str',
        'endpoint_id': 'str',
        'config': 'ServiceInstanceConfig'
    }

    attribute_map = {
        'source': 'source',
        'name': 'name',
        'description': 'description',
        'endpoint_id': 'endpoint_id',
        'config': 'config'
    }

    def __init__(self, source=None, name=None, description=None, endpoint_id=None, config=None):
        r"""ServiceInstanceInput

        The model defined in huaweicloud sdk

        :param source: 
        :type source: :class:`huaweicloudsdkdataartsfabricep.v1.SourceRef`
        :param name: 一个Service Instance的名称，只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param description: 描述信息
        :type description: str
        :param endpoint_id: endpoint空间id
        :type endpoint_id: str
        :param config: 
        :type config: :class:`huaweicloudsdkdataartsfabricep.v1.ServiceInstanceConfig`
        """
        
        

        self._source = None
        self._name = None
        self._description = None
        self._endpoint_id = None
        self._config = None
        self.discriminator = None

        self.source = source
        self.name = name
        if description is not None:
            self.description = description
        self.endpoint_id = endpoint_id
        if config is not None:
            self.config = config

    @property
    def source(self):
        r"""Gets the source of this ServiceInstanceInput.

        :return: The source of this ServiceInstanceInput.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.SourceRef`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ServiceInstanceInput.

        :param source: The source of this ServiceInstanceInput.
        :type source: :class:`huaweicloudsdkdataartsfabricep.v1.SourceRef`
        """
        self._source = source

    @property
    def name(self):
        r"""Gets the name of this ServiceInstanceInput.

        一个Service Instance的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this ServiceInstanceInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServiceInstanceInput.

        一个Service Instance的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this ServiceInstanceInput.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ServiceInstanceInput.

        描述信息

        :return: The description of this ServiceInstanceInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ServiceInstanceInput.

        描述信息

        :param description: The description of this ServiceInstanceInput.
        :type description: str
        """
        self._description = description

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ServiceInstanceInput.

        endpoint空间id

        :return: The endpoint_id of this ServiceInstanceInput.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ServiceInstanceInput.

        endpoint空间id

        :param endpoint_id: The endpoint_id of this ServiceInstanceInput.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def config(self):
        r"""Gets the config of this ServiceInstanceInput.

        :return: The config of this ServiceInstanceInput.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.ServiceInstanceConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this ServiceInstanceInput.

        :param config: The config of this ServiceInstanceInput.
        :type config: :class:`huaweicloudsdkdataartsfabricep.v1.ServiceInstanceConfig`
        """
        self._config = config

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
        if not isinstance(other, ServiceInstanceInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
