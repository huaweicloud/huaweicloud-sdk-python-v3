# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBussinessScene:

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
        'status': 'str',
        'selector': 'GovSelector',
        'spec': 'CreateBussinessSceneSpec'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'selector': 'selector',
        'spec': 'spec'
    }

    def __init__(self, name=None, status=None, selector=None, spec=None):
        r"""CreateBussinessScene

        The model defined in huaweicloud sdk

        :param name: 流量名称
        :type name: str
        :param status: 启用状态，支持enabled和disabled
        :type status: str
        :param selector: 
        :type selector: :class:`huaweicloudsdkcse.v1.GovSelector`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcse.v1.CreateBussinessSceneSpec`
        """
        
        

        self._name = None
        self._status = None
        self._selector = None
        self._spec = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if selector is not None:
            self.selector = selector
        if spec is not None:
            self.spec = spec

    @property
    def name(self):
        r"""Gets the name of this CreateBussinessScene.

        流量名称

        :return: The name of this CreateBussinessScene.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateBussinessScene.

        流量名称

        :param name: The name of this CreateBussinessScene.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this CreateBussinessScene.

        启用状态，支持enabled和disabled

        :return: The status of this CreateBussinessScene.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateBussinessScene.

        启用状态，支持enabled和disabled

        :param status: The status of this CreateBussinessScene.
        :type status: str
        """
        self._status = status

    @property
    def selector(self):
        r"""Gets the selector of this CreateBussinessScene.

        :return: The selector of this CreateBussinessScene.
        :rtype: :class:`huaweicloudsdkcse.v1.GovSelector`
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        r"""Sets the selector of this CreateBussinessScene.

        :param selector: The selector of this CreateBussinessScene.
        :type selector: :class:`huaweicloudsdkcse.v1.GovSelector`
        """
        self._selector = selector

    @property
    def spec(self):
        r"""Gets the spec of this CreateBussinessScene.

        :return: The spec of this CreateBussinessScene.
        :rtype: :class:`huaweicloudsdkcse.v1.CreateBussinessSceneSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this CreateBussinessScene.

        :param spec: The spec of this CreateBussinessScene.
        :type spec: :class:`huaweicloudsdkcse.v1.CreateBussinessSceneSpec`
        """
        self._spec = spec

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
        if not isinstance(other, CreateBussinessScene):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
