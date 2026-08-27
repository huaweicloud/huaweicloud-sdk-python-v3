# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelGroupProviderDetailResp:

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
        'group_id': 'str',
        'provider_id': 'str',
        'provider_name': 'str',
        'provider_type': 'str',
        'base_url': 'str',
        'connection_status': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'group_id',
        'provider_id': 'provider_id',
        'provider_name': 'provider_name',
        'provider_type': 'provider_type',
        'base_url': 'base_url',
        'connection_status': 'connection_status',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, group_id=None, provider_id=None, provider_name=None, provider_type=None, base_url=None, connection_status=None, create_time=None, update_time=None):
        r"""ModelGroupProviderDetailResp

        The model defined in huaweicloud sdk

        :param id: 关联记录id。
        :type id: str
        :param group_id: 分组id。
        :type group_id: str
        :param provider_id: 供应商id。
        :type provider_id: str
        :param provider_name: 供应商名称。
        :type provider_name: str
        :param provider_type: 供应商类型。
        :type provider_type: str
        :param base_url: 供应商base_url。
        :type base_url: str
        :param connection_status: 连接状态。
        :type connection_status: str
        :param create_time: 创建时间（ISO8601格式，UTC时区）。
        :type create_time: str
        :param update_time: 更新时间（ISO8601格式，UTC时区）。
        :type update_time: str
        """
        
        

        self._id = None
        self._group_id = None
        self._provider_id = None
        self._provider_name = None
        self._provider_type = None
        self._base_url = None
        self._connection_status = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if group_id is not None:
            self.group_id = group_id
        if provider_id is not None:
            self.provider_id = provider_id
        if provider_name is not None:
            self.provider_name = provider_name
        if provider_type is not None:
            self.provider_type = provider_type
        if base_url is not None:
            self.base_url = base_url
        if connection_status is not None:
            self.connection_status = connection_status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ModelGroupProviderDetailResp.

        关联记录id。

        :return: The id of this ModelGroupProviderDetailResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModelGroupProviderDetailResp.

        关联记录id。

        :param id: The id of this ModelGroupProviderDetailResp.
        :type id: str
        """
        self._id = id

    @property
    def group_id(self):
        r"""Gets the group_id of this ModelGroupProviderDetailResp.

        分组id。

        :return: The group_id of this ModelGroupProviderDetailResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ModelGroupProviderDetailResp.

        分组id。

        :param group_id: The group_id of this ModelGroupProviderDetailResp.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def provider_id(self):
        r"""Gets the provider_id of this ModelGroupProviderDetailResp.

        供应商id。

        :return: The provider_id of this ModelGroupProviderDetailResp.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this ModelGroupProviderDetailResp.

        供应商id。

        :param provider_id: The provider_id of this ModelGroupProviderDetailResp.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def provider_name(self):
        r"""Gets the provider_name of this ModelGroupProviderDetailResp.

        供应商名称。

        :return: The provider_name of this ModelGroupProviderDetailResp.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        r"""Sets the provider_name of this ModelGroupProviderDetailResp.

        供应商名称。

        :param provider_name: The provider_name of this ModelGroupProviderDetailResp.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def provider_type(self):
        r"""Gets the provider_type of this ModelGroupProviderDetailResp.

        供应商类型。

        :return: The provider_type of this ModelGroupProviderDetailResp.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this ModelGroupProviderDetailResp.

        供应商类型。

        :param provider_type: The provider_type of this ModelGroupProviderDetailResp.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def base_url(self):
        r"""Gets the base_url of this ModelGroupProviderDetailResp.

        供应商base_url。

        :return: The base_url of this ModelGroupProviderDetailResp.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        r"""Sets the base_url of this ModelGroupProviderDetailResp.

        供应商base_url。

        :param base_url: The base_url of this ModelGroupProviderDetailResp.
        :type base_url: str
        """
        self._base_url = base_url

    @property
    def connection_status(self):
        r"""Gets the connection_status of this ModelGroupProviderDetailResp.

        连接状态。

        :return: The connection_status of this ModelGroupProviderDetailResp.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        r"""Sets the connection_status of this ModelGroupProviderDetailResp.

        连接状态。

        :param connection_status: The connection_status of this ModelGroupProviderDetailResp.
        :type connection_status: str
        """
        self._connection_status = connection_status

    @property
    def create_time(self):
        r"""Gets the create_time of this ModelGroupProviderDetailResp.

        创建时间（ISO8601格式，UTC时区）。

        :return: The create_time of this ModelGroupProviderDetailResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ModelGroupProviderDetailResp.

        创建时间（ISO8601格式，UTC时区）。

        :param create_time: The create_time of this ModelGroupProviderDetailResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ModelGroupProviderDetailResp.

        更新时间（ISO8601格式，UTC时区）。

        :return: The update_time of this ModelGroupProviderDetailResp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ModelGroupProviderDetailResp.

        更新时间（ISO8601格式，UTC时区）。

        :param update_time: The update_time of this ModelGroupProviderDetailResp.
        :type update_time: str
        """
        self._update_time = update_time

    def to_dict(self):
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
        if not isinstance(other, ModelGroupProviderDetailResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
