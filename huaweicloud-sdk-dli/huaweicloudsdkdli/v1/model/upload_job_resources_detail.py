# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadJobResourcesDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'update_time': 'int',
        'resource_type': 'str',
        'is_async': 'bool',
        'resource_name': 'str',
        'status': 'str',
        'underlying_name': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'update_time': 'update_time',
        'resource_type': 'resource_type',
        'is_async': 'is_async',
        'resource_name': 'resource_name',
        'status': 'status',
        'underlying_name': 'underlying_name'
    }

    def __init__(self, create_time=None, update_time=None, resource_type=None, is_async=None, resource_name=None, status=None, underlying_name=None):
        r"""UploadJobResourcesDetail

        The model defined in huaweicloud sdk

        :param create_time: 资源包上传的unix时间。是单位为“毫秒”的时间戳。
        :type create_time: int
        :param update_time: 更新已上传资源包的unix时间。是单位为“毫秒”的时间戳
        :type update_time: int
        :param resource_type: 资源类型。
        :type resource_type: str
        :param is_async: 是否异步上传资源包
        :type is_async: bool
        :param resource_name: 资源名。
        :type resource_name: str
        :param status: \&quot;UPLOADING\&quot;表示正在上传。\&quot;READY\&quot;表示资源包已上传。\&quot;FAILED\&quot;表示资源包上传失败。
        :type status: str
        :param underlying_name: 资源包在队列中的名字。
        :type underlying_name: str
        """
        
        

        self._create_time = None
        self._update_time = None
        self._resource_type = None
        self._is_async = None
        self._resource_name = None
        self._status = None
        self._underlying_name = None
        self.discriminator = None

        self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        self.resource_type = resource_type
        if is_async is not None:
            self.is_async = is_async
        if resource_name is not None:
            self.resource_name = resource_name
        if status is not None:
            self.status = status
        if underlying_name is not None:
            self.underlying_name = underlying_name

    @property
    def create_time(self):
        r"""Gets the create_time of this UploadJobResourcesDetail.

        资源包上传的unix时间。是单位为“毫秒”的时间戳。

        :return: The create_time of this UploadJobResourcesDetail.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UploadJobResourcesDetail.

        资源包上传的unix时间。是单位为“毫秒”的时间戳。

        :param create_time: The create_time of this UploadJobResourcesDetail.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UploadJobResourcesDetail.

        更新已上传资源包的unix时间。是单位为“毫秒”的时间戳

        :return: The update_time of this UploadJobResourcesDetail.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UploadJobResourcesDetail.

        更新已上传资源包的unix时间。是单位为“毫秒”的时间戳

        :param update_time: The update_time of this UploadJobResourcesDetail.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def resource_type(self):
        r"""Gets the resource_type of this UploadJobResourcesDetail.

        资源类型。

        :return: The resource_type of this UploadJobResourcesDetail.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this UploadJobResourcesDetail.

        资源类型。

        :param resource_type: The resource_type of this UploadJobResourcesDetail.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def is_async(self):
        r"""Gets the is_async of this UploadJobResourcesDetail.

        是否异步上传资源包

        :return: The is_async of this UploadJobResourcesDetail.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        r"""Sets the is_async of this UploadJobResourcesDetail.

        是否异步上传资源包

        :param is_async: The is_async of this UploadJobResourcesDetail.
        :type is_async: bool
        """
        self._is_async = is_async

    @property
    def resource_name(self):
        r"""Gets the resource_name of this UploadJobResourcesDetail.

        资源名。

        :return: The resource_name of this UploadJobResourcesDetail.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this UploadJobResourcesDetail.

        资源名。

        :param resource_name: The resource_name of this UploadJobResourcesDetail.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def status(self):
        r"""Gets the status of this UploadJobResourcesDetail.

        \"UPLOADING\"表示正在上传。\"READY\"表示资源包已上传。\"FAILED\"表示资源包上传失败。

        :return: The status of this UploadJobResourcesDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UploadJobResourcesDetail.

        \"UPLOADING\"表示正在上传。\"READY\"表示资源包已上传。\"FAILED\"表示资源包上传失败。

        :param status: The status of this UploadJobResourcesDetail.
        :type status: str
        """
        self._status = status

    @property
    def underlying_name(self):
        r"""Gets the underlying_name of this UploadJobResourcesDetail.

        资源包在队列中的名字。

        :return: The underlying_name of this UploadJobResourcesDetail.
        :rtype: str
        """
        return self._underlying_name

    @underlying_name.setter
    def underlying_name(self, underlying_name):
        r"""Sets the underlying_name of this UploadJobResourcesDetail.

        资源包在队列中的名字。

        :param underlying_name: The underlying_name of this UploadJobResourcesDetail.
        :type underlying_name: str
        """
        self._underlying_name = underlying_name

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
        if not isinstance(other, UploadJobResourcesDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
