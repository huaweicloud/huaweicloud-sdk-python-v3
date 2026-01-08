# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadStepImageNewRequest:

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
        'parent': 'str',
        'sub': 'str',
        'file_name': 'str',
        'file_type': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'parent': 'parent',
        'sub': 'sub',
        'file_name': 'file_name',
        'file_type': 'file_type'
    }

    def __init__(self, project_id=None, parent=None, sub=None, file_name=None, file_type=None):
        r"""DownloadStepImageNewRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param parent: 父级目录名称
        :type parent: str
        :param sub: 子级目录名称
        :type sub: str
        :param file_name: 文件名
        :type file_name: str
        :param file_type: 文件类型
        :type file_type: str
        """
        
        

        self._project_id = None
        self._parent = None
        self._sub = None
        self._file_name = None
        self._file_type = None
        self.discriminator = None

        self.project_id = project_id
        self.parent = parent
        self.sub = sub
        self.file_name = file_name
        self.file_type = file_type

    @property
    def project_id(self):
        r"""Gets the project_id of this DownloadStepImageNewRequest.

        项目id

        :return: The project_id of this DownloadStepImageNewRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DownloadStepImageNewRequest.

        项目id

        :param project_id: The project_id of this DownloadStepImageNewRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def parent(self):
        r"""Gets the parent of this DownloadStepImageNewRequest.

        父级目录名称

        :return: The parent of this DownloadStepImageNewRequest.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        r"""Sets the parent of this DownloadStepImageNewRequest.

        父级目录名称

        :param parent: The parent of this DownloadStepImageNewRequest.
        :type parent: str
        """
        self._parent = parent

    @property
    def sub(self):
        r"""Gets the sub of this DownloadStepImageNewRequest.

        子级目录名称

        :return: The sub of this DownloadStepImageNewRequest.
        :rtype: str
        """
        return self._sub

    @sub.setter
    def sub(self, sub):
        r"""Sets the sub of this DownloadStepImageNewRequest.

        子级目录名称

        :param sub: The sub of this DownloadStepImageNewRequest.
        :type sub: str
        """
        self._sub = sub

    @property
    def file_name(self):
        r"""Gets the file_name of this DownloadStepImageNewRequest.

        文件名

        :return: The file_name of this DownloadStepImageNewRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this DownloadStepImageNewRequest.

        文件名

        :param file_name: The file_name of this DownloadStepImageNewRequest.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        r"""Gets the file_type of this DownloadStepImageNewRequest.

        文件类型

        :return: The file_type of this DownloadStepImageNewRequest.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this DownloadStepImageNewRequest.

        文件类型

        :param file_type: The file_type of this DownloadStepImageNewRequest.
        :type file_type: str
        """
        self._file_type = file_type

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
        if not isinstance(other, DownloadStepImageNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
