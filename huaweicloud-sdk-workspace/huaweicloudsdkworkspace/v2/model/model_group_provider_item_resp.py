# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelGroupProviderItemResp:

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
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'group_id',
        'provider_id': 'provider_id',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, group_id=None, provider_id=None, create_time=None, update_time=None):
        r"""ModelGroupProviderItemResp

        The model defined in huaweicloud sdk

        :param id: 关联记录id。
        :type id: str
        :param group_id: 模型组id。
        :type group_id: str
        :param provider_id: 供应商id。
        :type provider_id: str
        :param create_time: 创建时间（ISO8601格式，UTC时区）。
        :type create_time: str
        :param update_time: 更新时间（ISO8601格式，UTC时区）。
        :type update_time: str
        """
        
        

        self._id = None
        self._group_id = None
        self._provider_id = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if group_id is not None:
            self.group_id = group_id
        if provider_id is not None:
            self.provider_id = provider_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ModelGroupProviderItemResp.

        关联记录id。

        :return: The id of this ModelGroupProviderItemResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModelGroupProviderItemResp.

        关联记录id。

        :param id: The id of this ModelGroupProviderItemResp.
        :type id: str
        """
        self._id = id

    @property
    def group_id(self):
        r"""Gets the group_id of this ModelGroupProviderItemResp.

        模型组id。

        :return: The group_id of this ModelGroupProviderItemResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ModelGroupProviderItemResp.

        模型组id。

        :param group_id: The group_id of this ModelGroupProviderItemResp.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def provider_id(self):
        r"""Gets the provider_id of this ModelGroupProviderItemResp.

        供应商id。

        :return: The provider_id of this ModelGroupProviderItemResp.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this ModelGroupProviderItemResp.

        供应商id。

        :param provider_id: The provider_id of this ModelGroupProviderItemResp.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ModelGroupProviderItemResp.

        创建时间（ISO8601格式，UTC时区）。

        :return: The create_time of this ModelGroupProviderItemResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ModelGroupProviderItemResp.

        创建时间（ISO8601格式，UTC时区）。

        :param create_time: The create_time of this ModelGroupProviderItemResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ModelGroupProviderItemResp.

        更新时间（ISO8601格式，UTC时区）。

        :return: The update_time of this ModelGroupProviderItemResp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ModelGroupProviderItemResp.

        更新时间（ISO8601格式，UTC时区）。

        :param update_time: The update_time of this ModelGroupProviderItemResp.
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
        if not isinstance(other, ModelGroupProviderItemResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
