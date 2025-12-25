# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCollectorFilesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_id': 'str',
        'file_name': 'str',
        'path': 'str'
    }

    attribute_map = {
        'field_id': 'field_id',
        'file_name': 'file_name',
        'path': 'path'
    }

    def __init__(self, field_id=None, file_name=None, path=None):
        r"""CreateCollectorFilesResponse

        The model defined in huaweicloud sdk

        :param field_id: UUID
        :type field_id: str
        :param file_name: 文件名称
        :type file_name: str
        :param path: 文件路径
        :type path: str
        """
        
        super().__init__()

        self._field_id = None
        self._file_name = None
        self._path = None
        self.discriminator = None

        if field_id is not None:
            self.field_id = field_id
        if file_name is not None:
            self.file_name = file_name
        if path is not None:
            self.path = path

    @property
    def field_id(self):
        r"""Gets the field_id of this CreateCollectorFilesResponse.

        UUID

        :return: The field_id of this CreateCollectorFilesResponse.
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        r"""Sets the field_id of this CreateCollectorFilesResponse.

        UUID

        :param field_id: The field_id of this CreateCollectorFilesResponse.
        :type field_id: str
        """
        self._field_id = field_id

    @property
    def file_name(self):
        r"""Gets the file_name of this CreateCollectorFilesResponse.

        文件名称

        :return: The file_name of this CreateCollectorFilesResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this CreateCollectorFilesResponse.

        文件名称

        :param file_name: The file_name of this CreateCollectorFilesResponse.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def path(self):
        r"""Gets the path of this CreateCollectorFilesResponse.

        文件路径

        :return: The path of this CreateCollectorFilesResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this CreateCollectorFilesResponse.

        文件路径

        :param path: The path of this CreateCollectorFilesResponse.
        :type path: str
        """
        self._path = path

    def to_dict(self):
        import warnings
        warnings.warn("CreateCollectorFilesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateCollectorFilesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
