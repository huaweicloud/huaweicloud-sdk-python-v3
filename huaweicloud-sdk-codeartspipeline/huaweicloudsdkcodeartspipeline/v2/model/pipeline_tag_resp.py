# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineTagResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_id': 'str',
        'name': 'str',
        'color': 'str',
        'project_id': 'str',
        'project_name': 'str'
    }

    attribute_map = {
        'tag_id': 'tag_id',
        'name': 'name',
        'color': 'color',
        'project_id': 'project_id',
        'project_name': 'project_name'
    }

    def __init__(self, tag_id=None, name=None, color=None, project_id=None, project_name=None):
        r"""PipelineTagResp

        The model defined in huaweicloud sdk

        :param tag_id: **参数解释**： 标签ID。 **取值范围**： 32位字符，由数字和字母组成。 
        :type tag_id: str
        :param name: **参数解释**： 标签名称。 **取值范围**： 不涉及。 
        :type name: str
        :param color: **参数解释**： 标签颜色。 **取值范围**： 不涉及。 
        :type color: str
        :param project_id: **参数解释**： 项目ID。 **取值范围**： 32位字符，由数字和字母组成。 
        :type project_id: str
        :param project_name: **参数解释**： 项目名称。 **取值范围**： 不涉及。 
        :type project_name: str
        """
        
        

        self._tag_id = None
        self._name = None
        self._color = None
        self._project_id = None
        self._project_name = None
        self.discriminator = None

        if tag_id is not None:
            self.tag_id = tag_id
        if name is not None:
            self.name = name
        if color is not None:
            self.color = color
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name

    @property
    def tag_id(self):
        r"""Gets the tag_id of this PipelineTagResp.

        **参数解释**： 标签ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :return: The tag_id of this PipelineTagResp.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        r"""Sets the tag_id of this PipelineTagResp.

        **参数解释**： 标签ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :param tag_id: The tag_id of this PipelineTagResp.
        :type tag_id: str
        """
        self._tag_id = tag_id

    @property
    def name(self):
        r"""Gets the name of this PipelineTagResp.

        **参数解释**： 标签名称。 **取值范围**： 不涉及。 

        :return: The name of this PipelineTagResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PipelineTagResp.

        **参数解释**： 标签名称。 **取值范围**： 不涉及。 

        :param name: The name of this PipelineTagResp.
        :type name: str
        """
        self._name = name

    @property
    def color(self):
        r"""Gets the color of this PipelineTagResp.

        **参数解释**： 标签颜色。 **取值范围**： 不涉及。 

        :return: The color of this PipelineTagResp.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this PipelineTagResp.

        **参数解释**： 标签颜色。 **取值范围**： 不涉及。 

        :param color: The color of this PipelineTagResp.
        :type color: str
        """
        self._color = color

    @property
    def project_id(self):
        r"""Gets the project_id of this PipelineTagResp.

        **参数解释**： 项目ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :return: The project_id of this PipelineTagResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this PipelineTagResp.

        **参数解释**： 项目ID。 **取值范围**： 32位字符，由数字和字母组成。 

        :param project_id: The project_id of this PipelineTagResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this PipelineTagResp.

        **参数解释**： 项目名称。 **取值范围**： 不涉及。 

        :return: The project_name of this PipelineTagResp.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this PipelineTagResp.

        **参数解释**： 项目名称。 **取值范围**： 不涉及。 

        :param project_name: The project_name of this PipelineTagResp.
        :type project_name: str
        """
        self._project_name = project_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PipelineTagResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
