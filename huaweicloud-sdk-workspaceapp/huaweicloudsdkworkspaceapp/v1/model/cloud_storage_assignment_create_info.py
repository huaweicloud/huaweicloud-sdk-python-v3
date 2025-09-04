# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudStorageAssignmentCreateInfo:

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
        'region_id': 'str',
        'tenant_id': 'str',
        'domain_id': 'str',
        'folder_name': 'str',
        'attach': 'str',
        'attach_id': 'str',
        'attach_type': 'AttachType',
        'error_message': 'str',
        'is_success': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'region_id': 'region_id',
        'tenant_id': 'tenant_id',
        'domain_id': 'domain_id',
        'folder_name': 'folder_name',
        'attach': 'attach',
        'attach_id': 'attach_id',
        'attach_type': 'attach_type',
        'error_message': 'error_message',
        'is_success': 'is_success'
    }

    def __init__(self, id=None, region_id=None, tenant_id=None, domain_id=None, folder_name=None, attach=None, attach_id=None, attach_type=None, error_message=None, is_success=None):
        r"""CloudStorageAssignmentCreateInfo

        The model defined in huaweicloud sdk

        :param id: 存储分配的唯一标识符。
        :type id: str
        :param region_id: 区域ID。
        :type region_id: str
        :param tenant_id: 租户ID。
        :type tenant_id: str
        :param domain_id: 域ID。
        :type domain_id: str
        :param folder_name: 文件夹名称。
        :type folder_name: str
        :param attach: 用户名称。
        :type attach: str
        :param attach_id: 用户ID。
        :type attach_id: str
        :param attach_type: 
        :type attach_type: :class:`huaweicloudsdkworkspaceapp.v1.AttachType`
        :param error_message: 错误信息。
        :type error_message: str
        :param is_success: 是否创建成功。
        :type is_success: bool
        """
        
        

        self._id = None
        self._region_id = None
        self._tenant_id = None
        self._domain_id = None
        self._folder_name = None
        self._attach = None
        self._attach_id = None
        self._attach_type = None
        self._error_message = None
        self._is_success = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if region_id is not None:
            self.region_id = region_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if domain_id is not None:
            self.domain_id = domain_id
        if folder_name is not None:
            self.folder_name = folder_name
        if attach is not None:
            self.attach = attach
        if attach_id is not None:
            self.attach_id = attach_id
        if attach_type is not None:
            self.attach_type = attach_type
        if error_message is not None:
            self.error_message = error_message
        if is_success is not None:
            self.is_success = is_success

    @property
    def id(self):
        r"""Gets the id of this CloudStorageAssignmentCreateInfo.

        存储分配的唯一标识符。

        :return: The id of this CloudStorageAssignmentCreateInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CloudStorageAssignmentCreateInfo.

        存储分配的唯一标识符。

        :param id: The id of this CloudStorageAssignmentCreateInfo.
        :type id: str
        """
        self._id = id

    @property
    def region_id(self):
        r"""Gets the region_id of this CloudStorageAssignmentCreateInfo.

        区域ID。

        :return: The region_id of this CloudStorageAssignmentCreateInfo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CloudStorageAssignmentCreateInfo.

        区域ID。

        :param region_id: The region_id of this CloudStorageAssignmentCreateInfo.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CloudStorageAssignmentCreateInfo.

        租户ID。

        :return: The tenant_id of this CloudStorageAssignmentCreateInfo.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CloudStorageAssignmentCreateInfo.

        租户ID。

        :param tenant_id: The tenant_id of this CloudStorageAssignmentCreateInfo.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CloudStorageAssignmentCreateInfo.

        域ID。

        :return: The domain_id of this CloudStorageAssignmentCreateInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CloudStorageAssignmentCreateInfo.

        域ID。

        :param domain_id: The domain_id of this CloudStorageAssignmentCreateInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def folder_name(self):
        r"""Gets the folder_name of this CloudStorageAssignmentCreateInfo.

        文件夹名称。

        :return: The folder_name of this CloudStorageAssignmentCreateInfo.
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        r"""Sets the folder_name of this CloudStorageAssignmentCreateInfo.

        文件夹名称。

        :param folder_name: The folder_name of this CloudStorageAssignmentCreateInfo.
        :type folder_name: str
        """
        self._folder_name = folder_name

    @property
    def attach(self):
        r"""Gets the attach of this CloudStorageAssignmentCreateInfo.

        用户名称。

        :return: The attach of this CloudStorageAssignmentCreateInfo.
        :rtype: str
        """
        return self._attach

    @attach.setter
    def attach(self, attach):
        r"""Sets the attach of this CloudStorageAssignmentCreateInfo.

        用户名称。

        :param attach: The attach of this CloudStorageAssignmentCreateInfo.
        :type attach: str
        """
        self._attach = attach

    @property
    def attach_id(self):
        r"""Gets the attach_id of this CloudStorageAssignmentCreateInfo.

        用户ID。

        :return: The attach_id of this CloudStorageAssignmentCreateInfo.
        :rtype: str
        """
        return self._attach_id

    @attach_id.setter
    def attach_id(self, attach_id):
        r"""Sets the attach_id of this CloudStorageAssignmentCreateInfo.

        用户ID。

        :param attach_id: The attach_id of this CloudStorageAssignmentCreateInfo.
        :type attach_id: str
        """
        self._attach_id = attach_id

    @property
    def attach_type(self):
        r"""Gets the attach_type of this CloudStorageAssignmentCreateInfo.

        :return: The attach_type of this CloudStorageAssignmentCreateInfo.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AttachType`
        """
        return self._attach_type

    @attach_type.setter
    def attach_type(self, attach_type):
        r"""Sets the attach_type of this CloudStorageAssignmentCreateInfo.

        :param attach_type: The attach_type of this CloudStorageAssignmentCreateInfo.
        :type attach_type: :class:`huaweicloudsdkworkspaceapp.v1.AttachType`
        """
        self._attach_type = attach_type

    @property
    def error_message(self):
        r"""Gets the error_message of this CloudStorageAssignmentCreateInfo.

        错误信息。

        :return: The error_message of this CloudStorageAssignmentCreateInfo.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this CloudStorageAssignmentCreateInfo.

        错误信息。

        :param error_message: The error_message of this CloudStorageAssignmentCreateInfo.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def is_success(self):
        r"""Gets the is_success of this CloudStorageAssignmentCreateInfo.

        是否创建成功。

        :return: The is_success of this CloudStorageAssignmentCreateInfo.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this CloudStorageAssignmentCreateInfo.

        是否创建成功。

        :param is_success: The is_success of this CloudStorageAssignmentCreateInfo.
        :type is_success: bool
        """
        self._is_success = is_success

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
        if not isinstance(other, CloudStorageAssignmentCreateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
