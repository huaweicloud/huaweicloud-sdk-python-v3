# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadJobResourcesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'paths': 'list[str]',
        'kind': 'str',
        'group': 'str',
        'is_async': 'bool',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'paths': 'paths',
        'kind': 'kind',
        'group': 'group',
        'is_async': 'is_async',
        'tags': 'tags'
    }

    def __init__(self, paths=None, kind=None, group=None, is_async=None, tags=None):
        """UploadJobResourcesRequestBody

        The model defined in huaweicloud sdk

        :param paths: 用户OBS对象路径列表，OBS对象路径为OBS对象URL。
        :type paths: list[str]
        :param kind: 分组资源文件的类型。 说明：上传的同一组资源包含不同文件类型时，均选择“file”类型作为这次上传文件的类型。
        :type kind: str
        :param group: 将要创建的分组名。
        :type group: str
        :param is_async: 是否异步上传资源包
        :type is_async: bool
        :param tags: 资源标签。具体请参考表tags。
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        
        

        self._paths = None
        self._kind = None
        self._group = None
        self._is_async = None
        self._tags = None
        self.discriminator = None

        self.paths = paths
        self.kind = kind
        self.group = group
        if is_async is not None:
            self.is_async = is_async
        if tags is not None:
            self.tags = tags

    @property
    def paths(self):
        """Gets the paths of this UploadJobResourcesRequestBody.

        用户OBS对象路径列表，OBS对象路径为OBS对象URL。

        :return: The paths of this UploadJobResourcesRequestBody.
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this UploadJobResourcesRequestBody.

        用户OBS对象路径列表，OBS对象路径为OBS对象URL。

        :param paths: The paths of this UploadJobResourcesRequestBody.
        :type paths: list[str]
        """
        self._paths = paths

    @property
    def kind(self):
        """Gets the kind of this UploadJobResourcesRequestBody.

        分组资源文件的类型。 说明：上传的同一组资源包含不同文件类型时，均选择“file”类型作为这次上传文件的类型。

        :return: The kind of this UploadJobResourcesRequestBody.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this UploadJobResourcesRequestBody.

        分组资源文件的类型。 说明：上传的同一组资源包含不同文件类型时，均选择“file”类型作为这次上传文件的类型。

        :param kind: The kind of this UploadJobResourcesRequestBody.
        :type kind: str
        """
        self._kind = kind

    @property
    def group(self):
        """Gets the group of this UploadJobResourcesRequestBody.

        将要创建的分组名。

        :return: The group of this UploadJobResourcesRequestBody.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this UploadJobResourcesRequestBody.

        将要创建的分组名。

        :param group: The group of this UploadJobResourcesRequestBody.
        :type group: str
        """
        self._group = group

    @property
    def is_async(self):
        """Gets the is_async of this UploadJobResourcesRequestBody.

        是否异步上传资源包

        :return: The is_async of this UploadJobResourcesRequestBody.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        """Sets the is_async of this UploadJobResourcesRequestBody.

        是否异步上传资源包

        :param is_async: The is_async of this UploadJobResourcesRequestBody.
        :type is_async: bool
        """
        self._is_async = is_async

    @property
    def tags(self):
        """Gets the tags of this UploadJobResourcesRequestBody.

        资源标签。具体请参考表tags。

        :return: The tags of this UploadJobResourcesRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UploadJobResourcesRequestBody.

        资源标签。具体请参考表tags。

        :param tags: The tags of this UploadJobResourcesRequestBody.
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, UploadJobResourcesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
