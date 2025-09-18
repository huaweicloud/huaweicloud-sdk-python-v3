# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Workflow:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parameter': 'list[PipelineParam]',
        'source': 'list[Source]',
        'name': 'str',
        'project_id': 'str',
        'project_name': 'str'
    }

    attribute_map = {
        'parameter': 'parameter',
        'source': 'source',
        'name': 'name',
        'project_id': 'project_id',
        'project_name': 'project_name'
    }

    def __init__(self, parameter=None, source=None, name=None, project_id=None, project_name=None):
        r"""Workflow

        The model defined in huaweicloud sdk

        :param parameter: **参数解释**： 任务类型，list类型数据。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type parameter: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineParam`]
        :param source: **参数解释**： 源码仓，list类型数据。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type source: list[:class:`huaweicloudsdkcodeartspipeline.v2.Source`]
        :param name: **参数解释**： 流水线名字 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type name: str
        :param project_id: **参数解释**： 项目ID **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type project_id: str
        :param project_name: **参数解释**： 项目名字 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type project_name: str
        """
        
        

        self._parameter = None
        self._source = None
        self._name = None
        self._project_id = None
        self._project_name = None
        self.discriminator = None

        self.parameter = parameter
        self.source = source
        self.name = name
        self.project_id = project_id
        self.project_name = project_name

    @property
    def parameter(self):
        r"""Gets the parameter of this Workflow.

        **参数解释**： 任务类型，list类型数据。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The parameter of this Workflow.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineParam`]
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        r"""Sets the parameter of this Workflow.

        **参数解释**： 任务类型，list类型数据。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param parameter: The parameter of this Workflow.
        :type parameter: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineParam`]
        """
        self._parameter = parameter

    @property
    def source(self):
        r"""Gets the source of this Workflow.

        **参数解释**： 源码仓，list类型数据。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The source of this Workflow.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.Source`]
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this Workflow.

        **参数解释**： 源码仓，list类型数据。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param source: The source of this Workflow.
        :type source: list[:class:`huaweicloudsdkcodeartspipeline.v2.Source`]
        """
        self._source = source

    @property
    def name(self):
        r"""Gets the name of this Workflow.

        **参数解释**： 流水线名字 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The name of this Workflow.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Workflow.

        **参数解释**： 流水线名字 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param name: The name of this Workflow.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this Workflow.

        **参数解释**： 项目ID **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The project_id of this Workflow.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Workflow.

        **参数解释**： 项目ID **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param project_id: The project_id of this Workflow.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this Workflow.

        **参数解释**： 项目名字 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The project_name of this Workflow.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this Workflow.

        **参数解释**： 项目名字 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param project_name: The project_name of this Workflow.
        :type project_name: str
        """
        self._project_name = project_name

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
        if not isinstance(other, Workflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
