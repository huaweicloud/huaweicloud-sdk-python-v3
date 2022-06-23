# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'status': 'str',
        'resources': 'list[str]',
        'create_time': 'int',
        'update_time': 'int',
        'is_async': 'bool',
        'owner': 'str',
        'details': 'list[UploadPackageGroupDetailsResp]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'status': 'status',
        'resources': 'resources',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'is_async': 'is_async',
        'owner': 'owner',
        'details': 'details'
    }

    def __init__(self, group_name=None, status=None, resources=None, create_time=None, update_time=None, is_async=None, owner=None, details=None):
        """UploadResourcesResponse

        The model defined in huaweicloud sdk

        :param group_name: 模块名。
        :type group_name: str
        :param status: 上传分组资源状态。
        :type status: str
        :param resources: 该模块包含的资源包名列表。
        :type resources: list[str]
        :param create_time: 模块上传的unix时间戳。
        :type create_time: int
        :param update_time: 模块更新的unix时间戳。
        :type update_time: int
        :param is_async: 本次上传是同步还是异步
        :type is_async: bool
        :param owner: 资源包拥有者
        :type owner: str
        :param details: 分组资源包的详细信息。
        :type details: list[:class:`huaweicloudsdkdli.v1.UploadPackageGroupDetailsResp`]
        """
        
        super(UploadResourcesResponse, self).__init__()

        self._group_name = None
        self._status = None
        self._resources = None
        self._create_time = None
        self._update_time = None
        self._is_async = None
        self._owner = None
        self._details = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if status is not None:
            self.status = status
        if resources is not None:
            self.resources = resources
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if is_async is not None:
            self.is_async = is_async
        if owner is not None:
            self.owner = owner
        if details is not None:
            self.details = details

    @property
    def group_name(self):
        """Gets the group_name of this UploadResourcesResponse.

        模块名。

        :return: The group_name of this UploadResourcesResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this UploadResourcesResponse.

        模块名。

        :param group_name: The group_name of this UploadResourcesResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def status(self):
        """Gets the status of this UploadResourcesResponse.

        上传分组资源状态。

        :return: The status of this UploadResourcesResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UploadResourcesResponse.

        上传分组资源状态。

        :param status: The status of this UploadResourcesResponse.
        :type status: str
        """
        self._status = status

    @property
    def resources(self):
        """Gets the resources of this UploadResourcesResponse.

        该模块包含的资源包名列表。

        :return: The resources of this UploadResourcesResponse.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this UploadResourcesResponse.

        该模块包含的资源包名列表。

        :param resources: The resources of this UploadResourcesResponse.
        :type resources: list[str]
        """
        self._resources = resources

    @property
    def create_time(self):
        """Gets the create_time of this UploadResourcesResponse.

        模块上传的unix时间戳。

        :return: The create_time of this UploadResourcesResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UploadResourcesResponse.

        模块上传的unix时间戳。

        :param create_time: The create_time of this UploadResourcesResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this UploadResourcesResponse.

        模块更新的unix时间戳。

        :return: The update_time of this UploadResourcesResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UploadResourcesResponse.

        模块更新的unix时间戳。

        :param update_time: The update_time of this UploadResourcesResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def is_async(self):
        """Gets the is_async of this UploadResourcesResponse.

        本次上传是同步还是异步

        :return: The is_async of this UploadResourcesResponse.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        """Sets the is_async of this UploadResourcesResponse.

        本次上传是同步还是异步

        :param is_async: The is_async of this UploadResourcesResponse.
        :type is_async: bool
        """
        self._is_async = is_async

    @property
    def owner(self):
        """Gets the owner of this UploadResourcesResponse.

        资源包拥有者

        :return: The owner of this UploadResourcesResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UploadResourcesResponse.

        资源包拥有者

        :param owner: The owner of this UploadResourcesResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def details(self):
        """Gets the details of this UploadResourcesResponse.

        分组资源包的详细信息。

        :return: The details of this UploadResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.UploadPackageGroupDetailsResp`]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this UploadResourcesResponse.

        分组资源包的详细信息。

        :param details: The details of this UploadResourcesResponse.
        :type details: list[:class:`huaweicloudsdkdli.v1.UploadPackageGroupDetailsResp`]
        """
        self._details = details

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
        if not isinstance(other, UploadResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
