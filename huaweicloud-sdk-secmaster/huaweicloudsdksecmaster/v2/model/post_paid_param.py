# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPaidParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'domain_id': 'str',
        'tag_list': 'list[TagInfo]',
        'product_list': 'list[ProductPostPaid]',
        'operate_type': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'domain_id': 'domain_id',
        'tag_list': 'tag_list',
        'product_list': 'product_list',
        'operate_type': 'operate_type'
    }

    def __init__(self, region_id=None, domain_id=None, tag_list=None, product_list=None, operate_type=None):
        r"""PostPaidParam

        The model defined in huaweicloud sdk

        :param region_id: 区域ID
        :type region_id: str
        :param domain_id: domainId
        :type domain_id: str
        :param tag_list: 计费标签
        :type tag_list: list[:class:`huaweicloudsdksecmaster.v2.TagInfo`]
        :param product_list: 商品列表
        :type product_list: list[:class:`huaweicloudsdksecmaster.v2.ProductPostPaid`]
        :param operate_type: 操作类型：create新购, addition增加配额
        :type operate_type: str
        """
        
        

        self._region_id = None
        self._domain_id = None
        self._tag_list = None
        self._product_list = None
        self._operate_type = None
        self.discriminator = None

        self.region_id = region_id
        self.domain_id = domain_id
        if tag_list is not None:
            self.tag_list = tag_list
        if product_list is not None:
            self.product_list = product_list
        if operate_type is not None:
            self.operate_type = operate_type

    @property
    def region_id(self):
        r"""Gets the region_id of this PostPaidParam.

        区域ID

        :return: The region_id of this PostPaidParam.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this PostPaidParam.

        区域ID

        :param region_id: The region_id of this PostPaidParam.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this PostPaidParam.

        domainId

        :return: The domain_id of this PostPaidParam.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this PostPaidParam.

        domainId

        :param domain_id: The domain_id of this PostPaidParam.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def tag_list(self):
        r"""Gets the tag_list of this PostPaidParam.

        计费标签

        :return: The tag_list of this PostPaidParam.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.TagInfo`]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        r"""Sets the tag_list of this PostPaidParam.

        计费标签

        :param tag_list: The tag_list of this PostPaidParam.
        :type tag_list: list[:class:`huaweicloudsdksecmaster.v2.TagInfo`]
        """
        self._tag_list = tag_list

    @property
    def product_list(self):
        r"""Gets the product_list of this PostPaidParam.

        商品列表

        :return: The product_list of this PostPaidParam.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.ProductPostPaid`]
        """
        return self._product_list

    @product_list.setter
    def product_list(self, product_list):
        r"""Sets the product_list of this PostPaidParam.

        商品列表

        :param product_list: The product_list of this PostPaidParam.
        :type product_list: list[:class:`huaweicloudsdksecmaster.v2.ProductPostPaid`]
        """
        self._product_list = product_list

    @property
    def operate_type(self):
        r"""Gets the operate_type of this PostPaidParam.

        操作类型：create新购, addition增加配额

        :return: The operate_type of this PostPaidParam.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this PostPaidParam.

        操作类型：create新购, addition增加配额

        :param operate_type: The operate_type of this PostPaidParam.
        :type operate_type: str
        """
        self._operate_type = operate_type

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
        if not isinstance(other, PostPaidParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
