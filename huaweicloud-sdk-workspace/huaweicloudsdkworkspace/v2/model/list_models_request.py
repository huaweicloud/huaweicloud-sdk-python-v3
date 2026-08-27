# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModelsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'group_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'provider_id': 'provider_id',
        'limit': 'limit',
        'offset': 'offset',
        'group_id': 'group_id',
        'name': 'name'
    }

    def __init__(self, provider_id=None, limit=None, offset=None, group_id=None, name=None):
        r"""ListModelsRequest

        The model defined in huaweicloud sdk

        :param provider_id: 供应商id。
        :type provider_id: str
        :param limit: 每页数量，默认10。
        :type limit: int
        :param offset: 偏移量，默认0。
        :type offset: int
        :param group_id: 分组ID筛选。
        :type group_id: str
        :param name: 名称模糊搜索。
        :type name: str
        """
        
        

        self._provider_id = None
        self._limit = None
        self._offset = None
        self._group_id = None
        self._name = None
        self.discriminator = None

        self.provider_id = provider_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name

    @property
    def provider_id(self):
        r"""Gets the provider_id of this ListModelsRequest.

        供应商id。

        :return: The provider_id of this ListModelsRequest.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this ListModelsRequest.

        供应商id。

        :param provider_id: The provider_id of this ListModelsRequest.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def limit(self):
        r"""Gets the limit of this ListModelsRequest.

        每页数量，默认10。

        :return: The limit of this ListModelsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListModelsRequest.

        每页数量，默认10。

        :param limit: The limit of this ListModelsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListModelsRequest.

        偏移量，默认0。

        :return: The offset of this ListModelsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListModelsRequest.

        偏移量，默认0。

        :param offset: The offset of this ListModelsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def group_id(self):
        r"""Gets the group_id of this ListModelsRequest.

        分组ID筛选。

        :return: The group_id of this ListModelsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListModelsRequest.

        分组ID筛选。

        :param group_id: The group_id of this ListModelsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def name(self):
        r"""Gets the name of this ListModelsRequest.

        名称模糊搜索。

        :return: The name of this ListModelsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListModelsRequest.

        名称模糊搜索。

        :param name: The name of this ListModelsRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListModelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
