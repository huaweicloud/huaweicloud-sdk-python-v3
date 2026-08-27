# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelGroupResourceItemResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'resource_type': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'created_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'created_time': 'created_time'
    }

    def __init__(self, id=None, resource_type=None, resource_id=None, resource_name=None, created_time=None):
        r"""ModelGroupResourceItemResp

        The model defined in huaweicloud sdk

        :param id: 关联记录id。
        :type id: int
        :param resource_type: 资源类型（DESKTOP-桌面实例，DESKTOP_TAG-桌面标签）。
        :type resource_type: str
        :param resource_id: 资源id（Agent实例id或桌面标签id）。
        :type resource_id: str
        :param resource_name: 资源名称（桌面实例名称或桌面标签key:value格式）。
        :type resource_name: str
        :param created_time: 关联创建时间（ISO8601格式，UTC时区）。
        :type created_time: str
        """
        
        

        self._id = None
        self._resource_type = None
        self._resource_id = None
        self._resource_name = None
        self._created_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if created_time is not None:
            self.created_time = created_time

    @property
    def id(self):
        r"""Gets the id of this ModelGroupResourceItemResp.

        关联记录id。

        :return: The id of this ModelGroupResourceItemResp.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModelGroupResourceItemResp.

        关联记录id。

        :param id: The id of this ModelGroupResourceItemResp.
        :type id: int
        """
        self._id = id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ModelGroupResourceItemResp.

        资源类型（DESKTOP-桌面实例，DESKTOP_TAG-桌面标签）。

        :return: The resource_type of this ModelGroupResourceItemResp.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ModelGroupResourceItemResp.

        资源类型（DESKTOP-桌面实例，DESKTOP_TAG-桌面标签）。

        :param resource_type: The resource_type of this ModelGroupResourceItemResp.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ModelGroupResourceItemResp.

        资源id（Agent实例id或桌面标签id）。

        :return: The resource_id of this ModelGroupResourceItemResp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ModelGroupResourceItemResp.

        资源id（Agent实例id或桌面标签id）。

        :param resource_id: The resource_id of this ModelGroupResourceItemResp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ModelGroupResourceItemResp.

        资源名称（桌面实例名称或桌面标签key:value格式）。

        :return: The resource_name of this ModelGroupResourceItemResp.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ModelGroupResourceItemResp.

        资源名称（桌面实例名称或桌面标签key:value格式）。

        :param resource_name: The resource_name of this ModelGroupResourceItemResp.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def created_time(self):
        r"""Gets the created_time of this ModelGroupResourceItemResp.

        关联创建时间（ISO8601格式，UTC时区）。

        :return: The created_time of this ModelGroupResourceItemResp.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ModelGroupResourceItemResp.

        关联创建时间（ISO8601格式，UTC时区）。

        :param created_time: The created_time of this ModelGroupResourceItemResp.
        :type created_time: str
        """
        self._created_time = created_time

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
        if not isinstance(other, ModelGroupResourceItemResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
