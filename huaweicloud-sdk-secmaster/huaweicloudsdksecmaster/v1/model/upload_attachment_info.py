# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadAttachmentInfo:

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
        'file_name': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'file_name': 'file_name',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, id=None, file_name=None, workspace_id=None):
        r"""UploadAttachmentInfo

        The model defined in huaweicloud sdk

        :param id: 附件id
        :type id: str
        :param file_name: 附件名称
        :type file_name: str
        :param workspace_id: 当前的工作空间id
        :type workspace_id: str
        """
        
        

        self._id = None
        self._file_name = None
        self._workspace_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if file_name is not None:
            self.file_name = file_name
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def id(self):
        r"""Gets the id of this UploadAttachmentInfo.

        附件id

        :return: The id of this UploadAttachmentInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UploadAttachmentInfo.

        附件id

        :param id: The id of this UploadAttachmentInfo.
        :type id: str
        """
        self._id = id

    @property
    def file_name(self):
        r"""Gets the file_name of this UploadAttachmentInfo.

        附件名称

        :return: The file_name of this UploadAttachmentInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this UploadAttachmentInfo.

        附件名称

        :param file_name: The file_name of this UploadAttachmentInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UploadAttachmentInfo.

        当前的工作空间id

        :return: The workspace_id of this UploadAttachmentInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UploadAttachmentInfo.

        当前的工作空间id

        :param workspace_id: The workspace_id of this UploadAttachmentInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, UploadAttachmentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
