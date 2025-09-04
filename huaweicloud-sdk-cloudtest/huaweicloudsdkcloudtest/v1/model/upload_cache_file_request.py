# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadCacheFileRequest:

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
        'override': 'bool',
        'parent_type': 'str',
        'parent_uri': 'str',
        'body': 'UploadCacheFileRequestBody'
    }

    attribute_map = {
        'project_id': 'project_id',
        'override': 'override',
        'parent_type': 'parent_type',
        'parent_uri': 'parent_uri',
        'body': 'body'
    }

    def __init__(self, project_id=None, override=None, parent_type=None, parent_uri=None, body=None):
        r"""UploadCacheFileRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目uuid
        :type project_id: str
        :param override: 是否覆盖同名文件
        :type override: bool
        :param parent_type: 附件挂载资源类型
        :type parent_type: str
        :param parent_uri: 附件挂载资源Uri
        :type parent_uri: str
        :param body: Body of the UploadCacheFileRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.UploadCacheFileRequestBody`
        """
        
        

        self._project_id = None
        self._override = None
        self._parent_type = None
        self._parent_uri = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        if override is not None:
            self.override = override
        if parent_type is not None:
            self.parent_type = parent_type
        if parent_uri is not None:
            self.parent_uri = parent_uri
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this UploadCacheFileRequest.

        项目uuid

        :return: The project_id of this UploadCacheFileRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UploadCacheFileRequest.

        项目uuid

        :param project_id: The project_id of this UploadCacheFileRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def override(self):
        r"""Gets the override of this UploadCacheFileRequest.

        是否覆盖同名文件

        :return: The override of this UploadCacheFileRequest.
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        r"""Sets the override of this UploadCacheFileRequest.

        是否覆盖同名文件

        :param override: The override of this UploadCacheFileRequest.
        :type override: bool
        """
        self._override = override

    @property
    def parent_type(self):
        r"""Gets the parent_type of this UploadCacheFileRequest.

        附件挂载资源类型

        :return: The parent_type of this UploadCacheFileRequest.
        :rtype: str
        """
        return self._parent_type

    @parent_type.setter
    def parent_type(self, parent_type):
        r"""Sets the parent_type of this UploadCacheFileRequest.

        附件挂载资源类型

        :param parent_type: The parent_type of this UploadCacheFileRequest.
        :type parent_type: str
        """
        self._parent_type = parent_type

    @property
    def parent_uri(self):
        r"""Gets the parent_uri of this UploadCacheFileRequest.

        附件挂载资源Uri

        :return: The parent_uri of this UploadCacheFileRequest.
        :rtype: str
        """
        return self._parent_uri

    @parent_uri.setter
    def parent_uri(self, parent_uri):
        r"""Sets the parent_uri of this UploadCacheFileRequest.

        附件挂载资源Uri

        :param parent_uri: The parent_uri of this UploadCacheFileRequest.
        :type parent_uri: str
        """
        self._parent_uri = parent_uri

    @property
    def body(self):
        r"""Gets the body of this UploadCacheFileRequest.

        :return: The body of this UploadCacheFileRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.UploadCacheFileRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UploadCacheFileRequest.

        :param body: The body of this UploadCacheFileRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.UploadCacheFileRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UploadCacheFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
