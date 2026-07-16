# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachDynamicStorageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'id': 'str',
        'mount_path': 'str',
        'status': 'str',
        'uri': 'str',
        'failure_reason': 'str',
        'efs_id': 'str',
        'mount_type': 'str'
    }

    attribute_map = {
        'category': 'category',
        'id': 'id',
        'mount_path': 'mount_path',
        'status': 'status',
        'uri': 'uri',
        'failure_reason': 'failure_reason',
        'efs_id': 'efs_id',
        'mount_type': 'mount_type'
    }

    def __init__(self, category=None, id=None, mount_path=None, status=None, uri=None, failure_reason=None, efs_id=None, mount_type=None):
        r"""AttachDynamicStorageResponse

        The model defined in huaweicloud sdk

        :param category: **参数解释**：存储类型。可选值为OBS/OBSFS/EFS。 **取值范围**：不涉及。
        :type category: str
        :param id: **参数解释**：动态挂载实例ID。 **取值范围**：不涉及。
        :type id: str
        :param mount_path: **参数解释**：在Notebook实例中挂载的路径。 **取值范围**：不涉及。
        :type mount_path: str
        :param status: **参数解释**：动态挂载状态。 **取值范围**：枚举类型，取值如下： - MOUNTING：挂载中 - MOUNT_FAILED：挂载失败 - MOUNTED：已挂载 - UNMOUNTING：卸载中 - UNMOUNT_FAILED：卸载失败 - UNMOUNTED：卸载完成
        :type status: str
        :param uri: **参数解释**：存储路径。 **取值范围**：不涉及。
        :type uri: str
        :param failure_reason: **参数解释**：挂载失败原因，动态挂载状态为MOUNT_FAILED时返回。 **取值范围**：不涉及。
        :type failure_reason: str
        :param efs_id: **参数解释**：EFS存储实例ID。 **取值范围**：不涉及。
        :type efs_id: str
        :param mount_type: **参数解释**：存储挂载类型。 **取值范围**：枚举类型，取值如下：  - STATIC:不支持在实例运行期间挂载以及卸载的存储 - DYNAMIC:支持在实例运行期间挂载以及卸载的存储
        :type mount_type: str
        """
        
        super().__init__()

        self._category = None
        self._id = None
        self._mount_path = None
        self._status = None
        self._uri = None
        self._failure_reason = None
        self._efs_id = None
        self._mount_type = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if id is not None:
            self.id = id
        if mount_path is not None:
            self.mount_path = mount_path
        if status is not None:
            self.status = status
        if uri is not None:
            self.uri = uri
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if efs_id is not None:
            self.efs_id = efs_id
        if mount_type is not None:
            self.mount_type = mount_type

    @property
    def category(self):
        r"""Gets the category of this AttachDynamicStorageResponse.

        **参数解释**：存储类型。可选值为OBS/OBSFS/EFS。 **取值范围**：不涉及。

        :return: The category of this AttachDynamicStorageResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this AttachDynamicStorageResponse.

        **参数解释**：存储类型。可选值为OBS/OBSFS/EFS。 **取值范围**：不涉及。

        :param category: The category of this AttachDynamicStorageResponse.
        :type category: str
        """
        self._category = category

    @property
    def id(self):
        r"""Gets the id of this AttachDynamicStorageResponse.

        **参数解释**：动态挂载实例ID。 **取值范围**：不涉及。

        :return: The id of this AttachDynamicStorageResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AttachDynamicStorageResponse.

        **参数解释**：动态挂载实例ID。 **取值范围**：不涉及。

        :param id: The id of this AttachDynamicStorageResponse.
        :type id: str
        """
        self._id = id

    @property
    def mount_path(self):
        r"""Gets the mount_path of this AttachDynamicStorageResponse.

        **参数解释**：在Notebook实例中挂载的路径。 **取值范围**：不涉及。

        :return: The mount_path of this AttachDynamicStorageResponse.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this AttachDynamicStorageResponse.

        **参数解释**：在Notebook实例中挂载的路径。 **取值范围**：不涉及。

        :param mount_path: The mount_path of this AttachDynamicStorageResponse.
        :type mount_path: str
        """
        self._mount_path = mount_path

    @property
    def status(self):
        r"""Gets the status of this AttachDynamicStorageResponse.

        **参数解释**：动态挂载状态。 **取值范围**：枚举类型，取值如下： - MOUNTING：挂载中 - MOUNT_FAILED：挂载失败 - MOUNTED：已挂载 - UNMOUNTING：卸载中 - UNMOUNT_FAILED：卸载失败 - UNMOUNTED：卸载完成

        :return: The status of this AttachDynamicStorageResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AttachDynamicStorageResponse.

        **参数解释**：动态挂载状态。 **取值范围**：枚举类型，取值如下： - MOUNTING：挂载中 - MOUNT_FAILED：挂载失败 - MOUNTED：已挂载 - UNMOUNTING：卸载中 - UNMOUNT_FAILED：卸载失败 - UNMOUNTED：卸载完成

        :param status: The status of this AttachDynamicStorageResponse.
        :type status: str
        """
        self._status = status

    @property
    def uri(self):
        r"""Gets the uri of this AttachDynamicStorageResponse.

        **参数解释**：存储路径。 **取值范围**：不涉及。

        :return: The uri of this AttachDynamicStorageResponse.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this AttachDynamicStorageResponse.

        **参数解释**：存储路径。 **取值范围**：不涉及。

        :param uri: The uri of this AttachDynamicStorageResponse.
        :type uri: str
        """
        self._uri = uri

    @property
    def failure_reason(self):
        r"""Gets the failure_reason of this AttachDynamicStorageResponse.

        **参数解释**：挂载失败原因，动态挂载状态为MOUNT_FAILED时返回。 **取值范围**：不涉及。

        :return: The failure_reason of this AttachDynamicStorageResponse.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        r"""Sets the failure_reason of this AttachDynamicStorageResponse.

        **参数解释**：挂载失败原因，动态挂载状态为MOUNT_FAILED时返回。 **取值范围**：不涉及。

        :param failure_reason: The failure_reason of this AttachDynamicStorageResponse.
        :type failure_reason: str
        """
        self._failure_reason = failure_reason

    @property
    def efs_id(self):
        r"""Gets the efs_id of this AttachDynamicStorageResponse.

        **参数解释**：EFS存储实例ID。 **取值范围**：不涉及。

        :return: The efs_id of this AttachDynamicStorageResponse.
        :rtype: str
        """
        return self._efs_id

    @efs_id.setter
    def efs_id(self, efs_id):
        r"""Sets the efs_id of this AttachDynamicStorageResponse.

        **参数解释**：EFS存储实例ID。 **取值范围**：不涉及。

        :param efs_id: The efs_id of this AttachDynamicStorageResponse.
        :type efs_id: str
        """
        self._efs_id = efs_id

    @property
    def mount_type(self):
        r"""Gets the mount_type of this AttachDynamicStorageResponse.

        **参数解释**：存储挂载类型。 **取值范围**：枚举类型，取值如下：  - STATIC:不支持在实例运行期间挂载以及卸载的存储 - DYNAMIC:支持在实例运行期间挂载以及卸载的存储

        :return: The mount_type of this AttachDynamicStorageResponse.
        :rtype: str
        """
        return self._mount_type

    @mount_type.setter
    def mount_type(self, mount_type):
        r"""Sets the mount_type of this AttachDynamicStorageResponse.

        **参数解释**：存储挂载类型。 **取值范围**：枚举类型，取值如下：  - STATIC:不支持在实例运行期间挂载以及卸载的存储 - DYNAMIC:支持在实例运行期间挂载以及卸载的存储

        :param mount_type: The mount_type of this AttachDynamicStorageResponse.
        :type mount_type: str
        """
        self._mount_type = mount_type

    def to_dict(self):
        import warnings
        warnings.warn("AttachDynamicStorageResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, AttachDynamicStorageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
