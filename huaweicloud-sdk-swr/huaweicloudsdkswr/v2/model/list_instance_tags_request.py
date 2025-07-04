# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'namespace_name': 'str',
        'repository_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'is_accessory': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'namespace_name': 'namespace_name',
        'repository_name': 'repository_name',
        'offset': 'offset',
        'limit': 'limit',
        'is_accessory': 'is_accessory'
    }

    def __init__(self, instance_id=None, namespace_name=None, repository_name=None, offset=None, limit=None, is_accessory=None):
        r"""ListInstanceTagsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param repository_name: 仓库名称
        :type repository_name: str
        :param offset: 起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type offset: int
        :param limit: 返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type limit: int
        :param is_accessory: 是否返回制品附件，默认为true
        :type is_accessory: bool
        """
        
        

        self._instance_id = None
        self._namespace_name = None
        self._repository_name = None
        self._offset = None
        self._limit = None
        self._is_accessory = None
        self.discriminator = None

        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.repository_name = repository_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if is_accessory is not None:
            self.is_accessory = is_accessory

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceTagsRequest.

        企业仓库实例ID

        :return: The instance_id of this ListInstanceTagsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceTagsRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this ListInstanceTagsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ListInstanceTagsRequest.

        命名空间名称

        :return: The namespace_name of this ListInstanceTagsRequest.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ListInstanceTagsRequest.

        命名空间名称

        :param namespace_name: The namespace_name of this ListInstanceTagsRequest.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def repository_name(self):
        r"""Gets the repository_name of this ListInstanceTagsRequest.

        仓库名称

        :return: The repository_name of this ListInstanceTagsRequest.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this ListInstanceTagsRequest.

        仓库名称

        :param repository_name: The repository_name of this ListInstanceTagsRequest.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceTagsRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The offset of this ListInstanceTagsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceTagsRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param offset: The offset of this ListInstanceTagsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceTagsRequest.

        返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The limit of this ListInstanceTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceTagsRequest.

        返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param limit: The limit of this ListInstanceTagsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def is_accessory(self):
        r"""Gets the is_accessory of this ListInstanceTagsRequest.

        是否返回制品附件，默认为true

        :return: The is_accessory of this ListInstanceTagsRequest.
        :rtype: bool
        """
        return self._is_accessory

    @is_accessory.setter
    def is_accessory(self, is_accessory):
        r"""Sets the is_accessory of this ListInstanceTagsRequest.

        是否返回制品附件，默认为true

        :param is_accessory: The is_accessory of this ListInstanceTagsRequest.
        :type is_accessory: bool
        """
        self._is_accessory = is_accessory

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
        if not isinstance(other, ListInstanceTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
