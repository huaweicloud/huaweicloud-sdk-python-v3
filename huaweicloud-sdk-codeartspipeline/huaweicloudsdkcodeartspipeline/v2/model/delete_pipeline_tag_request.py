# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePipelineTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'tag_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'tag_id': 'tagId'
    }

    def __init__(self, project_id=None, tag_id=None):
        r"""DeletePipelineTagRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param tag_id: 标签ID
        :type tag_id: str
        """
        
        

        self._project_id = None
        self._tag_id = None
        self.discriminator = None

        self.project_id = project_id
        self.tag_id = tag_id

    @property
    def project_id(self):
        r"""Gets the project_id of this DeletePipelineTagRequest.

        项目ID

        :return: The project_id of this DeletePipelineTagRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DeletePipelineTagRequest.

        项目ID

        :param project_id: The project_id of this DeletePipelineTagRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tag_id(self):
        r"""Gets the tag_id of this DeletePipelineTagRequest.

        标签ID

        :return: The tag_id of this DeletePipelineTagRequest.
        :rtype: str
        """
        return self._tag_id

    @tag_id.setter
    def tag_id(self, tag_id):
        r"""Sets the tag_id of this DeletePipelineTagRequest.

        标签ID

        :param tag_id: The tag_id of this DeletePipelineTagRequest.
        :type tag_id: str
        """
        self._tag_id = tag_id

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
        if not isinstance(other, DeletePipelineTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
