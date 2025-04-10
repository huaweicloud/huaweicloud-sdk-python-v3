# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineGroupCreateDTO:

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
        'project_id': 'str',
        'parent_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'project_id': 'project_id',
        'parent_id': 'parent_id'
    }

    def __init__(self, name=None, project_id=None, parent_id=None):
        r"""PipelineGroupCreateDTO

        The model defined in huaweicloud sdk

        :param name: 流水线分组名
        :type name: str
        :param project_id: 项目名
        :type project_id: str
        :param parent_id: 父分组ID
        :type parent_id: str
        """
        
        

        self._name = None
        self._project_id = None
        self._parent_id = None
        self.discriminator = None

        self.name = name
        self.project_id = project_id
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def name(self):
        r"""Gets the name of this PipelineGroupCreateDTO.

        流水线分组名

        :return: The name of this PipelineGroupCreateDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PipelineGroupCreateDTO.

        流水线分组名

        :param name: The name of this PipelineGroupCreateDTO.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this PipelineGroupCreateDTO.

        项目名

        :return: The project_id of this PipelineGroupCreateDTO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this PipelineGroupCreateDTO.

        项目名

        :param project_id: The project_id of this PipelineGroupCreateDTO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this PipelineGroupCreateDTO.

        父分组ID

        :return: The parent_id of this PipelineGroupCreateDTO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this PipelineGroupCreateDTO.

        父分组ID

        :param parent_id: The parent_id of this PipelineGroupCreateDTO.
        :type parent_id: str
        """
        self._parent_id = parent_id

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
        if not isinstance(other, PipelineGroupCreateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
