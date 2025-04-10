# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateReleaseReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chart_id': 'str',
        'description': 'str',
        'name': 'str',
        'namespace': 'str',
        'version': 'str',
        'parameters': 'ReleaseReqBodyParams',
        'values': 'CreateReleaseReqBodyValues'
    }

    attribute_map = {
        'chart_id': 'chart_id',
        'description': 'description',
        'name': 'name',
        'namespace': 'namespace',
        'version': 'version',
        'parameters': 'parameters',
        'values': 'values'
    }

    def __init__(self, chart_id=None, description=None, name=None, namespace=None, version=None, parameters=None, values=None):
        r"""CreateReleaseReqBody

        The model defined in huaweicloud sdk

        :param chart_id: 模板ID
        :type chart_id: str
        :param description: 模板实例描述
        :type description: str
        :param name: 模板实例名称
        :type name: str
        :param namespace: 模板实例所在的命名空间
        :type namespace: str
        :param version: 模板实例版本号
        :type version: str
        :param parameters: 
        :type parameters: :class:`huaweicloudsdkcce.v3.ReleaseReqBodyParams`
        :param values: 
        :type values: :class:`huaweicloudsdkcce.v3.CreateReleaseReqBodyValues`
        """
        
        

        self._chart_id = None
        self._description = None
        self._name = None
        self._namespace = None
        self._version = None
        self._parameters = None
        self._values = None
        self.discriminator = None

        self.chart_id = chart_id
        if description is not None:
            self.description = description
        self.name = name
        self.namespace = namespace
        self.version = version
        if parameters is not None:
            self.parameters = parameters
        self.values = values

    @property
    def chart_id(self):
        r"""Gets the chart_id of this CreateReleaseReqBody.

        模板ID

        :return: The chart_id of this CreateReleaseReqBody.
        :rtype: str
        """
        return self._chart_id

    @chart_id.setter
    def chart_id(self, chart_id):
        r"""Sets the chart_id of this CreateReleaseReqBody.

        模板ID

        :param chart_id: The chart_id of this CreateReleaseReqBody.
        :type chart_id: str
        """
        self._chart_id = chart_id

    @property
    def description(self):
        r"""Gets the description of this CreateReleaseReqBody.

        模板实例描述

        :return: The description of this CreateReleaseReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateReleaseReqBody.

        模板实例描述

        :param description: The description of this CreateReleaseReqBody.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this CreateReleaseReqBody.

        模板实例名称

        :return: The name of this CreateReleaseReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateReleaseReqBody.

        模板实例名称

        :param name: The name of this CreateReleaseReqBody.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this CreateReleaseReqBody.

        模板实例所在的命名空间

        :return: The namespace of this CreateReleaseReqBody.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CreateReleaseReqBody.

        模板实例所在的命名空间

        :param namespace: The namespace of this CreateReleaseReqBody.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def version(self):
        r"""Gets the version of this CreateReleaseReqBody.

        模板实例版本号

        :return: The version of this CreateReleaseReqBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this CreateReleaseReqBody.

        模板实例版本号

        :param version: The version of this CreateReleaseReqBody.
        :type version: str
        """
        self._version = version

    @property
    def parameters(self):
        r"""Gets the parameters of this CreateReleaseReqBody.

        :return: The parameters of this CreateReleaseReqBody.
        :rtype: :class:`huaweicloudsdkcce.v3.ReleaseReqBodyParams`
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this CreateReleaseReqBody.

        :param parameters: The parameters of this CreateReleaseReqBody.
        :type parameters: :class:`huaweicloudsdkcce.v3.ReleaseReqBodyParams`
        """
        self._parameters = parameters

    @property
    def values(self):
        r"""Gets the values of this CreateReleaseReqBody.

        :return: The values of this CreateReleaseReqBody.
        :rtype: :class:`huaweicloudsdkcce.v3.CreateReleaseReqBodyValues`
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this CreateReleaseReqBody.

        :param values: The values of this CreateReleaseReqBody.
        :type values: :class:`huaweicloudsdkcce.v3.CreateReleaseReqBodyValues`
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
        if not isinstance(other, CreateReleaseReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
