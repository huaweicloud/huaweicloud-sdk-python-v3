# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackageResourceMoudle:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'module_name': 'str',
        'module_type': 'str',
        'status': 'str',
        'description': 'str',
        'resources': 'list[str]',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'module_name': 'module_name',
        'module_type': 'module_type',
        'status': 'status',
        'description': 'description',
        'resources': 'resources',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, module_name=None, module_type=None, status=None, description=None, resources=None, create_time=None, update_time=None):
        r"""PackageResourceMoudle

        The model defined in huaweicloud sdk

        :param module_name: 模块名。
        :type module_name: str
        :param module_type: 模块类型。
        :type module_type: str
        :param status: \&quot;UPLOADING\&quot;表示正在上传 \&quot;READY\&quot;表示模块包已上传 \&quot;FAILED\&quot;表示模块包上传失败
        :type status: str
        :param description: 模块描述。
        :type description: str
        :param resources: 该模块包含的资源包名列表。
        :type resources: list[str]
        :param create_time: 模块上传的unix时间。
        :type create_time: int
        :param update_time: 模块更新的unix时间。
        :type update_time: int
        """
        
        

        self._module_name = None
        self._module_type = None
        self._status = None
        self._description = None
        self._resources = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if module_name is not None:
            self.module_name = module_name
        if module_type is not None:
            self.module_type = module_type
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

    @property
    def module_name(self):
        r"""Gets the module_name of this PackageResourceMoudle.

        模块名。

        :return: The module_name of this PackageResourceMoudle.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        r"""Sets the module_name of this PackageResourceMoudle.

        模块名。

        :param module_name: The module_name of this PackageResourceMoudle.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def module_type(self):
        r"""Gets the module_type of this PackageResourceMoudle.

        模块类型。

        :return: The module_type of this PackageResourceMoudle.
        :rtype: str
        """
        return self._module_type

    @module_type.setter
    def module_type(self, module_type):
        r"""Sets the module_type of this PackageResourceMoudle.

        模块类型。

        :param module_type: The module_type of this PackageResourceMoudle.
        :type module_type: str
        """
        self._module_type = module_type

    @property
    def status(self):
        r"""Gets the status of this PackageResourceMoudle.

        \"UPLOADING\"表示正在上传 \"READY\"表示模块包已上传 \"FAILED\"表示模块包上传失败

        :return: The status of this PackageResourceMoudle.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PackageResourceMoudle.

        \"UPLOADING\"表示正在上传 \"READY\"表示模块包已上传 \"FAILED\"表示模块包上传失败

        :param status: The status of this PackageResourceMoudle.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this PackageResourceMoudle.

        模块描述。

        :return: The description of this PackageResourceMoudle.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PackageResourceMoudle.

        模块描述。

        :param description: The description of this PackageResourceMoudle.
        :type description: str
        """
        self._description = description

    @property
    def resources(self):
        r"""Gets the resources of this PackageResourceMoudle.

        该模块包含的资源包名列表。

        :return: The resources of this PackageResourceMoudle.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this PackageResourceMoudle.

        该模块包含的资源包名列表。

        :param resources: The resources of this PackageResourceMoudle.
        :type resources: list[str]
        """
        self._resources = resources

    @property
    def create_time(self):
        r"""Gets the create_time of this PackageResourceMoudle.

        模块上传的unix时间。

        :return: The create_time of this PackageResourceMoudle.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PackageResourceMoudle.

        模块上传的unix时间。

        :param create_time: The create_time of this PackageResourceMoudle.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this PackageResourceMoudle.

        模块更新的unix时间。

        :return: The update_time of this PackageResourceMoudle.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this PackageResourceMoudle.

        模块更新的unix时间。

        :param update_time: The update_time of this PackageResourceMoudle.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, PackageResourceMoudle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
