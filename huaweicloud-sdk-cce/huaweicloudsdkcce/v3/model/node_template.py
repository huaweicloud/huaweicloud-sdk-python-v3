# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os': 'str',
        'image_id': 'str',
        'login': 'NodeTemplateLogin',
        'life_cycle': 'NodeTemplateLifeCycle',
        'runtime_config': 'NodeTemplateRuntimeConfig',
        'extend_param': 'NodeTemplateExtendParam'
    }

    attribute_map = {
        'os': 'os',
        'image_id': 'imageID',
        'login': 'login',
        'life_cycle': 'lifeCycle',
        'runtime_config': 'runtimeConfig',
        'extend_param': 'extendParam'
    }

    def __init__(self, os=None, image_id=None, login=None, life_cycle=None, runtime_config=None, extend_param=None):
        r"""NodeTemplate

        The model defined in huaweicloud sdk

        :param os: 
        :type os: str
        :param image_id: 
        :type image_id: str
        :param login: 
        :type login: :class:`huaweicloudsdkcce.v3.NodeTemplateLogin`
        :param life_cycle: 
        :type life_cycle: :class:`huaweicloudsdkcce.v3.NodeTemplateLifeCycle`
        :param runtime_config: 
        :type runtime_config: :class:`huaweicloudsdkcce.v3.NodeTemplateRuntimeConfig`
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.NodeTemplateExtendParam`
        """
        
        

        self._os = None
        self._image_id = None
        self._login = None
        self._life_cycle = None
        self._runtime_config = None
        self._extend_param = None
        self.discriminator = None

        if os is not None:
            self.os = os
        if image_id is not None:
            self.image_id = image_id
        if login is not None:
            self.login = login
        if life_cycle is not None:
            self.life_cycle = life_cycle
        if runtime_config is not None:
            self.runtime_config = runtime_config
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def os(self):
        r"""Gets the os of this NodeTemplate.

        :return: The os of this NodeTemplate.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this NodeTemplate.

        :param os: The os of this NodeTemplate.
        :type os: str
        """
        self._os = os

    @property
    def image_id(self):
        r"""Gets the image_id of this NodeTemplate.

        :return: The image_id of this NodeTemplate.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this NodeTemplate.

        :param image_id: The image_id of this NodeTemplate.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def login(self):
        r"""Gets the login of this NodeTemplate.

        :return: The login of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeTemplateLogin`
        """
        return self._login

    @login.setter
    def login(self, login):
        r"""Sets the login of this NodeTemplate.

        :param login: The login of this NodeTemplate.
        :type login: :class:`huaweicloudsdkcce.v3.NodeTemplateLogin`
        """
        self._login = login

    @property
    def life_cycle(self):
        r"""Gets the life_cycle of this NodeTemplate.

        :return: The life_cycle of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeTemplateLifeCycle`
        """
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        r"""Sets the life_cycle of this NodeTemplate.

        :param life_cycle: The life_cycle of this NodeTemplate.
        :type life_cycle: :class:`huaweicloudsdkcce.v3.NodeTemplateLifeCycle`
        """
        self._life_cycle = life_cycle

    @property
    def runtime_config(self):
        r"""Gets the runtime_config of this NodeTemplate.

        :return: The runtime_config of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeTemplateRuntimeConfig`
        """
        return self._runtime_config

    @runtime_config.setter
    def runtime_config(self, runtime_config):
        r"""Sets the runtime_config of this NodeTemplate.

        :param runtime_config: The runtime_config of this NodeTemplate.
        :type runtime_config: :class:`huaweicloudsdkcce.v3.NodeTemplateRuntimeConfig`
        """
        self._runtime_config = runtime_config

    @property
    def extend_param(self):
        r"""Gets the extend_param of this NodeTemplate.

        :return: The extend_param of this NodeTemplate.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeTemplateExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this NodeTemplate.

        :param extend_param: The extend_param of this NodeTemplate.
        :type extend_param: :class:`huaweicloudsdkcce.v3.NodeTemplateExtendParam`
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
        if not isinstance(other, NodeTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
