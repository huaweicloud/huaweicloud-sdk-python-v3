# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProduct:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'resource_size': 'int',
        'resource_id': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'resource_size': 'resource_size',
        'resource_id': 'resource_id'
    }

    def __init__(self, resource_type=None, resource_spec_code=None, resource_size=None, resource_id=None):
        r"""UpdateProduct

        The model defined in huaweicloud sdk

        :param resource_type: 变更后的资源类型
        :type resource_type: str
        :param resource_spec_code: 变更后的商品规格编码
        :type resource_spec_code: str
        :param resource_size: 变更后的资源配额 如果operate_type为addition时，resource_size必须要大于原来的resource_id，decrease时要小于原来的resource_size，并且大于等于当前project下的ecs数量
        :type resource_size: int
        :param resource_id: 要进行变更的资源ID
        :type resource_id: str
        """
        
        

        self._resource_type = None
        self._resource_spec_code = None
        self._resource_size = None
        self._resource_id = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_spec_code = resource_spec_code
        self.resource_size = resource_size
        self.resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this UpdateProduct.

        变更后的资源类型

        :return: The resource_type of this UpdateProduct.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this UpdateProduct.

        变更后的资源类型

        :param resource_type: The resource_type of this UpdateProduct.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this UpdateProduct.

        变更后的商品规格编码

        :return: The resource_spec_code of this UpdateProduct.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this UpdateProduct.

        变更后的商品规格编码

        :param resource_spec_code: The resource_spec_code of this UpdateProduct.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_size(self):
        r"""Gets the resource_size of this UpdateProduct.

        变更后的资源配额 如果operate_type为addition时，resource_size必须要大于原来的resource_id，decrease时要小于原来的resource_size，并且大于等于当前project下的ecs数量

        :return: The resource_size of this UpdateProduct.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        r"""Sets the resource_size of this UpdateProduct.

        变更后的资源配额 如果operate_type为addition时，resource_size必须要大于原来的resource_id，decrease时要小于原来的resource_size，并且大于等于当前project下的ecs数量

        :param resource_size: The resource_size of this UpdateProduct.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def resource_id(self):
        r"""Gets the resource_id of this UpdateProduct.

        要进行变更的资源ID

        :return: The resource_id of this UpdateProduct.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this UpdateProduct.

        要进行变更的资源ID

        :param resource_id: The resource_id of this UpdateProduct.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, UpdateProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
