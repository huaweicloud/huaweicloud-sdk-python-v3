# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'int',
        'limit': 'str',
        'offset': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, limit=None, offset=None):
        r"""ListInstancesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 云堡垒机实例ID。（非必传，需要查询单个实例详情时传入）
        :type instance_id: int
        :param limit: 查询返回的记录数量上限，默认值 1000，即一次最多返回 1000 条实例记录。最小值为1，最大值为1000。
        :type limit: str
        :param offset: 查询的起始偏移量（索引位置），默认值 0，即从第 0 条记录开始查。最小值为0。
        :type offset: str
        """
        
        

        self._instance_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstancesRequest.

        云堡垒机实例ID。（非必传，需要查询单个实例详情时传入）

        :return: The instance_id of this ListInstancesRequest.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstancesRequest.

        云堡垒机实例ID。（非必传，需要查询单个实例详情时传入）

        :param instance_id: The instance_id of this ListInstancesRequest.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ListInstancesRequest.

        查询返回的记录数量上限，默认值 1000，即一次最多返回 1000 条实例记录。最小值为1，最大值为1000。

        :return: The limit of this ListInstancesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstancesRequest.

        查询返回的记录数量上限，默认值 1000，即一次最多返回 1000 条实例记录。最小值为1，最大值为1000。

        :param limit: The limit of this ListInstancesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInstancesRequest.

        查询的起始偏移量（索引位置），默认值 0，即从第 0 条记录开始查。最小值为0。

        :return: The offset of this ListInstancesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstancesRequest.

        查询的起始偏移量（索引位置），默认值 0，即从第 0 条记录开始查。最小值为0。

        :param offset: The offset of this ListInstancesRequest.
        :type offset: str
        """
        self._offset = offset

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
        if not isinstance(other, ListInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
