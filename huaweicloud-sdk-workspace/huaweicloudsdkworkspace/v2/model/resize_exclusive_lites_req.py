# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeExclusiveLitesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'product_id': 'str',
        'new_quantity': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'product_id': 'product_id',
        'new_quantity': 'new_quantity'
    }

    def __init__(self, enterprise_project_id=None, product_id=None, new_quantity=None):
        r"""ResizeExclusiveLitesReq

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID，默认\&quot;0。\&quot;
        :type enterprise_project_id: str
        :param product_id: 产品套餐ID。
        :type product_id: str
        :param new_quantity: 扩容后的桌面个数，单位为个/次。
        :type new_quantity: int
        """
        
        

        self._enterprise_project_id = None
        self._product_id = None
        self._new_quantity = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.product_id = product_id
        self.new_quantity = new_quantity

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ResizeExclusiveLitesReq.

        企业项目ID，默认\"0。\"

        :return: The enterprise_project_id of this ResizeExclusiveLitesReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ResizeExclusiveLitesReq.

        企业项目ID，默认\"0。\"

        :param enterprise_project_id: The enterprise_project_id of this ResizeExclusiveLitesReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def product_id(self):
        r"""Gets the product_id of this ResizeExclusiveLitesReq.

        产品套餐ID。

        :return: The product_id of this ResizeExclusiveLitesReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ResizeExclusiveLitesReq.

        产品套餐ID。

        :param product_id: The product_id of this ResizeExclusiveLitesReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def new_quantity(self):
        r"""Gets the new_quantity of this ResizeExclusiveLitesReq.

        扩容后的桌面个数，单位为个/次。

        :return: The new_quantity of this ResizeExclusiveLitesReq.
        :rtype: int
        """
        return self._new_quantity

    @new_quantity.setter
    def new_quantity(self, new_quantity):
        r"""Sets the new_quantity of this ResizeExclusiveLitesReq.

        扩容后的桌面个数，单位为个/次。

        :param new_quantity: The new_quantity of this ResizeExclusiveLitesReq.
        :type new_quantity: int
        """
        self._new_quantity = new_quantity

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
        if not isinstance(other, ResizeExclusiveLitesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
