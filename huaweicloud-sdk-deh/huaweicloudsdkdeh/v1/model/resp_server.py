# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RespServer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'addresses': 'dict(str, list[RespAddr])',
        'created': 'str',
        'flavor': 'RespFlavor',
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'tenant_id': 'str',
        'updated': 'str',
        'user_id': 'str',
        'task_state': 'str',
        'image': 'RespImage',
        'metadata': 'RespMetadata'
    }

    attribute_map = {
        'addresses': 'addresses',
        'created': 'created',
        'flavor': 'flavor',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'updated': 'updated',
        'user_id': 'user_id',
        'task_state': 'task_state',
        'image': 'image',
        'metadata': 'metadata'
    }

    def __init__(self, addresses=None, created=None, flavor=None, id=None, name=None, status=None, tenant_id=None, updated=None, user_id=None, task_state=None, image=None, metadata=None):
        r"""RespServer

        The model defined in huaweicloud sdk

        :param addresses: 弹性云服务器的网络属性。
        :type addresses: dict(str, list[RespAddr])
        :param created: 弹性云服务器创建时间。
        :type created: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkdeh.v1.RespFlavor`
        :param id: 弹性云服务器ID，格式为UUID。
        :type id: str
        :param name: 弹性云服务器名称。
        :type name: str
        :param status: 弹性云服务器状态。  取值范围：ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PASSWORD、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE
        :type status: str
        :param tenant_id: 弹性云服务器所属租户ID，格式为UUID。
        :type tenant_id: str
        :param updated: 弹性云服务器更新时间。
        :type updated: str
        :param user_id: 创建弹性云服务器的用户ID，格式为UUID。
        :type user_id: str
        :param task_state: 弹性云服务器当前任务的状态。
        :type task_state: str
        :param image: 
        :type image: :class:`huaweicloudsdkdeh.v1.RespImage`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkdeh.v1.RespMetadata`
        """
        
        

        self._addresses = None
        self._created = None
        self._flavor = None
        self._id = None
        self._name = None
        self._status = None
        self._tenant_id = None
        self._updated = None
        self._user_id = None
        self._task_state = None
        self._image = None
        self._metadata = None
        self.discriminator = None

        self.addresses = addresses
        self.created = created
        self.flavor = flavor
        self.id = id
        self.name = name
        self.status = status
        self.tenant_id = tenant_id
        self.updated = updated
        self.user_id = user_id
        self.task_state = task_state
        self.image = image
        self.metadata = metadata

    @property
    def addresses(self):
        r"""Gets the addresses of this RespServer.

        弹性云服务器的网络属性。

        :return: The addresses of this RespServer.
        :rtype: dict(str, list[RespAddr])
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        r"""Sets the addresses of this RespServer.

        弹性云服务器的网络属性。

        :param addresses: The addresses of this RespServer.
        :type addresses: dict(str, list[RespAddr])
        """
        self._addresses = addresses

    @property
    def created(self):
        r"""Gets the created of this RespServer.

        弹性云服务器创建时间。

        :return: The created of this RespServer.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this RespServer.

        弹性云服务器创建时间。

        :param created: The created of this RespServer.
        :type created: str
        """
        self._created = created

    @property
    def flavor(self):
        r"""Gets the flavor of this RespServer.

        :return: The flavor of this RespServer.
        :rtype: :class:`huaweicloudsdkdeh.v1.RespFlavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this RespServer.

        :param flavor: The flavor of this RespServer.
        :type flavor: :class:`huaweicloudsdkdeh.v1.RespFlavor`
        """
        self._flavor = flavor

    @property
    def id(self):
        r"""Gets the id of this RespServer.

        弹性云服务器ID，格式为UUID。

        :return: The id of this RespServer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RespServer.

        弹性云服务器ID，格式为UUID。

        :param id: The id of this RespServer.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RespServer.

        弹性云服务器名称。

        :return: The name of this RespServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RespServer.

        弹性云服务器名称。

        :param name: The name of this RespServer.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this RespServer.

        弹性云服务器状态。  取值范围：ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PASSWORD、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE

        :return: The status of this RespServer.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RespServer.

        弹性云服务器状态。  取值范围：ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PASSWORD、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE

        :param status: The status of this RespServer.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this RespServer.

        弹性云服务器所属租户ID，格式为UUID。

        :return: The tenant_id of this RespServer.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this RespServer.

        弹性云服务器所属租户ID，格式为UUID。

        :param tenant_id: The tenant_id of this RespServer.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def updated(self):
        r"""Gets the updated of this RespServer.

        弹性云服务器更新时间。

        :return: The updated of this RespServer.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this RespServer.

        弹性云服务器更新时间。

        :param updated: The updated of this RespServer.
        :type updated: str
        """
        self._updated = updated

    @property
    def user_id(self):
        r"""Gets the user_id of this RespServer.

        创建弹性云服务器的用户ID，格式为UUID。

        :return: The user_id of this RespServer.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this RespServer.

        创建弹性云服务器的用户ID，格式为UUID。

        :param user_id: The user_id of this RespServer.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def task_state(self):
        r"""Gets the task_state of this RespServer.

        弹性云服务器当前任务的状态。

        :return: The task_state of this RespServer.
        :rtype: str
        """
        return self._task_state

    @task_state.setter
    def task_state(self, task_state):
        r"""Sets the task_state of this RespServer.

        弹性云服务器当前任务的状态。

        :param task_state: The task_state of this RespServer.
        :type task_state: str
        """
        self._task_state = task_state

    @property
    def image(self):
        r"""Gets the image of this RespServer.

        :return: The image of this RespServer.
        :rtype: :class:`huaweicloudsdkdeh.v1.RespImage`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this RespServer.

        :param image: The image of this RespServer.
        :type image: :class:`huaweicloudsdkdeh.v1.RespImage`
        """
        self._image = image

    @property
    def metadata(self):
        r"""Gets the metadata of this RespServer.

        :return: The metadata of this RespServer.
        :rtype: :class:`huaweicloudsdkdeh.v1.RespMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this RespServer.

        :param metadata: The metadata of this RespServer.
        :type metadata: :class:`huaweicloudsdkdeh.v1.RespMetadata`
        """
        self._metadata = metadata

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
        if not isinstance(other, RespServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
