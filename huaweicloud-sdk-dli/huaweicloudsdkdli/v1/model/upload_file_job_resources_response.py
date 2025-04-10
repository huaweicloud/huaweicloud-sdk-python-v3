# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadFileJobResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'description': 'str',
        'resources': 'list[str]',
        'create_time': 'int',
        'update_time': 'int',
        'group_name': 'str',
        'owner': 'str',
        'is_async': 'bool',
        'details': 'list[UploadJobResourcesDetail]',
        'module_name': 'str',
        'module_type': 'str'
    }

    attribute_map = {
        'status': 'status',
        'description': 'description',
        'resources': 'resources',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'group_name': 'group_name',
        'owner': 'owner',
        'is_async': 'is_async',
        'details': 'details',
        'module_name': 'module_name',
        'module_type': 'module_type'
    }

    def __init__(self, status=None, description=None, resources=None, create_time=None, update_time=None, group_name=None, owner=None, is_async=None, details=None, module_name=None, module_type=None):
        r"""UploadFileJobResourcesResponse

        The model defined in huaweicloud sdk

        :param status: \&quot;UPLOADING\&quot;表示正在上传。 \&quot;READY\&quot;表示模块包已上传。 \&quot;FAILED\&quot;表示模块包上传失败。
        :type status: str
        :param description: 资源模块描述。
        :type description: str
        :param resources: 该资源模块包含的资源包名列表。
        :type resources: list[str]
        :param create_time: 资源模块上传的unix时间戳。
        :type create_time: int
        :param update_time: 资源模块更新的unix时间戳。
        :type update_time: int
        :param group_name: 模块名。
        :type group_name: str
        :param owner: 资源包拥有者
        :type owner: str
        :param is_async: 是否使用异步方式上传资源包。默认值为“false”，表示不使用异步方式。推荐使用异步方式上传资源包。
        :type is_async: bool
        :param details: 分组资源包的详细信息
        :type details: list[:class:`huaweicloudsdkdli.v1.UploadJobResourcesDetail`]
        :param module_name: 资源模块名
        :type module_name: str
        :param module_type: 资源模块类型。jar:用户jar文件;pyFile:用户python文件;file:用户文件
        :type module_type: str
        """
        
        super(UploadFileJobResourcesResponse, self).__init__()

        self._status = None
        self._description = None
        self._resources = None
        self._create_time = None
        self._update_time = None
        self._group_name = None
        self._owner = None
        self._is_async = None
        self._details = None
        self._module_name = None
        self._module_type = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if resources is not None:
            self.resources = resources
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if group_name is not None:
            self.group_name = group_name
        if owner is not None:
            self.owner = owner
        if is_async is not None:
            self.is_async = is_async
        if details is not None:
            self.details = details
        if module_name is not None:
            self.module_name = module_name
        if module_type is not None:
            self.module_type = module_type

    @property
    def status(self):
        r"""Gets the status of this UploadFileJobResourcesResponse.

        \"UPLOADING\"表示正在上传。 \"READY\"表示模块包已上传。 \"FAILED\"表示模块包上传失败。

        :return: The status of this UploadFileJobResourcesResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UploadFileJobResourcesResponse.

        \"UPLOADING\"表示正在上传。 \"READY\"表示模块包已上传。 \"FAILED\"表示模块包上传失败。

        :param status: The status of this UploadFileJobResourcesResponse.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this UploadFileJobResourcesResponse.

        资源模块描述。

        :return: The description of this UploadFileJobResourcesResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UploadFileJobResourcesResponse.

        资源模块描述。

        :param description: The description of this UploadFileJobResourcesResponse.
        :type description: str
        """
        self._description = description

    @property
    def resources(self):
        r"""Gets the resources of this UploadFileJobResourcesResponse.

        该资源模块包含的资源包名列表。

        :return: The resources of this UploadFileJobResourcesResponse.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this UploadFileJobResourcesResponse.

        该资源模块包含的资源包名列表。

        :param resources: The resources of this UploadFileJobResourcesResponse.
        :type resources: list[str]
        """
        self._resources = resources

    @property
    def create_time(self):
        r"""Gets the create_time of this UploadFileJobResourcesResponse.

        资源模块上传的unix时间戳。

        :return: The create_time of this UploadFileJobResourcesResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UploadFileJobResourcesResponse.

        资源模块上传的unix时间戳。

        :param create_time: The create_time of this UploadFileJobResourcesResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UploadFileJobResourcesResponse.

        资源模块更新的unix时间戳。

        :return: The update_time of this UploadFileJobResourcesResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UploadFileJobResourcesResponse.

        资源模块更新的unix时间戳。

        :param update_time: The update_time of this UploadFileJobResourcesResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def group_name(self):
        r"""Gets the group_name of this UploadFileJobResourcesResponse.

        模块名。

        :return: The group_name of this UploadFileJobResourcesResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this UploadFileJobResourcesResponse.

        模块名。

        :param group_name: The group_name of this UploadFileJobResourcesResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def owner(self):
        r"""Gets the owner of this UploadFileJobResourcesResponse.

        资源包拥有者

        :return: The owner of this UploadFileJobResourcesResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this UploadFileJobResourcesResponse.

        资源包拥有者

        :param owner: The owner of this UploadFileJobResourcesResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def is_async(self):
        r"""Gets the is_async of this UploadFileJobResourcesResponse.

        是否使用异步方式上传资源包。默认值为“false”，表示不使用异步方式。推荐使用异步方式上传资源包。

        :return: The is_async of this UploadFileJobResourcesResponse.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        r"""Sets the is_async of this UploadFileJobResourcesResponse.

        是否使用异步方式上传资源包。默认值为“false”，表示不使用异步方式。推荐使用异步方式上传资源包。

        :param is_async: The is_async of this UploadFileJobResourcesResponse.
        :type is_async: bool
        """
        self._is_async = is_async

    @property
    def details(self):
        r"""Gets the details of this UploadFileJobResourcesResponse.

        分组资源包的详细信息

        :return: The details of this UploadFileJobResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.UploadJobResourcesDetail`]
        """
        return self._details

    @details.setter
    def details(self, details):
        r"""Sets the details of this UploadFileJobResourcesResponse.

        分组资源包的详细信息

        :param details: The details of this UploadFileJobResourcesResponse.
        :type details: list[:class:`huaweicloudsdkdli.v1.UploadJobResourcesDetail`]
        """
        self._details = details

    @property
    def module_name(self):
        r"""Gets the module_name of this UploadFileJobResourcesResponse.

        资源模块名

        :return: The module_name of this UploadFileJobResourcesResponse.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this UploadFileJobResourcesResponse.

        资源模块名

        :param module_name: The module_name of this UploadFileJobResourcesResponse.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def module_type(self):
        r"""Gets the module_type of this UploadFileJobResourcesResponse.

        资源模块类型。jar:用户jar文件;pyFile:用户python文件;file:用户文件

        :return: The module_type of this UploadFileJobResourcesResponse.
        :rtype: str
        """
        return self._module_type

    @module_type.setter
    def module_type(self, module_type):
        r"""Sets the module_type of this UploadFileJobResourcesResponse.

        资源模块类型。jar:用户jar文件;pyFile:用户python文件;file:用户文件

        :param module_type: The module_type of this UploadFileJobResourcesResponse.
        :type module_type: str
        """
        self._module_type = module_type

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
        if not isinstance(other, UploadFileJobResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
