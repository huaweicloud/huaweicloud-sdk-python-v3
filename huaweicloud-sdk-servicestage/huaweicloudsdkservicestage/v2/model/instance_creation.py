# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceCreation:

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
        'desc': 'str',
        'diagram': 'str',
        'image': 'str',
        'template_id': 'str',
        'variables': 'InstanceCreationVariables',
        'instance_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'desc': 'desc',
        'diagram': 'diagram',
        'image': 'image',
        'template_id': 'template_id',
        'variables': 'variables',
        'instance_id': 'instance_id'
    }

    def __init__(self, name=None, desc=None, diagram=None, image=None, template_id=None, variables=None, instance_id=None):
        r"""InstanceCreation

        The model defined in huaweicloud sdk

        :param name: 实例名称，必填
        :type name: str
        :param desc: 实例描述，非必填
        :type desc: str
        :param diagram: 架构部署图，通过设计器创建时必填
        :type diagram: str
        :param image: 设计器架构图base64编码,通过设计器创建或更新实例时可选
        :type image: str
        :param template_id: 预置模板id，通过模板创建时必填
        :type template_id: str
        :param variables: 
        :type variables: :class:`huaweicloudsdkservicestage.v2.InstanceCreationVariables`
        :param instance_id: 实例id,更新时必填
        :type instance_id: str
        """
        
        

        self._name = None
        self._desc = None
        self._diagram = None
        self._image = None
        self._template_id = None
        self._variables = None
        self._instance_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if diagram is not None:
            self.diagram = diagram
        if image is not None:
            self.image = image
        if template_id is not None:
            self.template_id = template_id
        if variables is not None:
            self.variables = variables
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this InstanceCreation.

        实例名称，必填

        :return: The name of this InstanceCreation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceCreation.

        实例名称，必填

        :param name: The name of this InstanceCreation.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        r"""Gets the desc of this InstanceCreation.

        实例描述，非必填

        :return: The desc of this InstanceCreation.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this InstanceCreation.

        实例描述，非必填

        :param desc: The desc of this InstanceCreation.
        :type desc: str
        """
        self._desc = desc

    @property
    def diagram(self):
        r"""Gets the diagram of this InstanceCreation.

        架构部署图，通过设计器创建时必填

        :return: The diagram of this InstanceCreation.
        :rtype: str
        """
        return self._diagram

    @diagram.setter
    def diagram(self, diagram):
        r"""Sets the diagram of this InstanceCreation.

        架构部署图，通过设计器创建时必填

        :param diagram: The diagram of this InstanceCreation.
        :type diagram: str
        """
        self._diagram = diagram

    @property
    def image(self):
        r"""Gets the image of this InstanceCreation.

        设计器架构图base64编码,通过设计器创建或更新实例时可选

        :return: The image of this InstanceCreation.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this InstanceCreation.

        设计器架构图base64编码,通过设计器创建或更新实例时可选

        :param image: The image of this InstanceCreation.
        :type image: str
        """
        self._image = image

    @property
    def template_id(self):
        r"""Gets the template_id of this InstanceCreation.

        预置模板id，通过模板创建时必填

        :return: The template_id of this InstanceCreation.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this InstanceCreation.

        预置模板id，通过模板创建时必填

        :param template_id: The template_id of this InstanceCreation.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def variables(self):
        r"""Gets the variables of this InstanceCreation.

        :return: The variables of this InstanceCreation.
        :rtype: :class:`huaweicloudsdkservicestage.v2.InstanceCreationVariables`
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this InstanceCreation.

        :param variables: The variables of this InstanceCreation.
        :type variables: :class:`huaweicloudsdkservicestage.v2.InstanceCreationVariables`
        """
        self._variables = variables

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceCreation.

        实例id,更新时必填

        :return: The instance_id of this InstanceCreation.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceCreation.

        实例id,更新时必填

        :param instance_id: The instance_id of this InstanceCreation.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, InstanceCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
