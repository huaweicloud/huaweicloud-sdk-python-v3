# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowPoolOrder:

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
        'sku': 'SkuInfo',
        'sku_count': 'str'
    }

    attribute_map = {
        'id': 'id',
        'sku': 'sku',
        'sku_count': 'sku_count'
    }

    def __init__(self, id=None, sku=None, sku_count=None):
        r"""WorkflowPoolOrder

        The model defined in huaweicloud sdk

        :param id: 订阅ID。
        :type id: str
        :param sku: 
        :type sku: :class:`huaweicloudsdkmodelarts.v1.SkuInfo`
        :param sku_count: 订阅计数。
        :type sku_count: str
        """
        
        

        self._id = None
        self._sku = None
        self._sku_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.sku = sku
        self.sku_count = sku_count

    @property
    def id(self):
        r"""Gets the id of this WorkflowPoolOrder.

        订阅ID。

        :return: The id of this WorkflowPoolOrder.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkflowPoolOrder.

        订阅ID。

        :param id: The id of this WorkflowPoolOrder.
        :type id: str
        """
        self._id = id

    @property
    def sku(self):
        r"""Gets the sku of this WorkflowPoolOrder.

        :return: The sku of this WorkflowPoolOrder.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.SkuInfo`
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        r"""Sets the sku of this WorkflowPoolOrder.

        :param sku: The sku of this WorkflowPoolOrder.
        :type sku: :class:`huaweicloudsdkmodelarts.v1.SkuInfo`
        """
        self._sku = sku

    @property
    def sku_count(self):
        r"""Gets the sku_count of this WorkflowPoolOrder.

        订阅计数。

        :return: The sku_count of this WorkflowPoolOrder.
        :rtype: str
        """
        return self._sku_count

    @sku_count.setter
    def sku_count(self, sku_count):
        r"""Sets the sku_count of this WorkflowPoolOrder.

        订阅计数。

        :param sku_count: The sku_count of this WorkflowPoolOrder.
        :type sku_count: str
        """
        self._sku_count = sku_count

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
        if not isinstance(other, WorkflowPoolOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
