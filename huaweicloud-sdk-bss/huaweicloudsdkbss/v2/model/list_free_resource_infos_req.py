# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFreeResourceInfosReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_code': 'str',
        'order_id': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'enterprise_project_id': 'str',
        'status': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'region_code': 'region_code',
        'order_id': 'order_id',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'enterprise_project_id': 'enterprise_project_id',
        'status': 'status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, region_code=None, order_id=None, product_id=None, product_name=None, enterprise_project_id=None, status=None, offset=None, limit=None):
        """ListFreeResourceInfosReq

        The model defined in huaweicloud sdk

        :param region_code: 云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type region_code: str
        :param order_id: 订单ID。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type order_id: str
        :param product_id: 产品ID，即资源包ID。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type product_id: str
        :param product_name: 产品名称，即资源包名称。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type product_name: str
        :param enterprise_project_id: 企业项目ID。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type enterprise_project_id: str
        :param status: 状态： 0：未生效1：生效中2：已用完3：已失效4：已退订 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type status: int
        :param offset: 偏移量，从0开始，默认为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询的记录数，默认为10。
        :type limit: int
        """
        
        

        self._region_code = None
        self._order_id = None
        self._product_id = None
        self._product_name = None
        self._enterprise_project_id = None
        self._status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if region_code is not None:
            self.region_code = region_code
        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if status is not None:
            self.status = status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def region_code(self):
        """Gets the region_code of this ListFreeResourceInfosReq.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The region_code of this ListFreeResourceInfosReq.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this ListFreeResourceInfosReq.

        云服务区编码，例如：“cn-north-1”。具体请参见地区和终端节点对应云服务的“区域”列的值。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param region_code: The region_code of this ListFreeResourceInfosReq.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def order_id(self):
        """Gets the order_id of this ListFreeResourceInfosReq.

        订单ID。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The order_id of this ListFreeResourceInfosReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ListFreeResourceInfosReq.

        订单ID。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param order_id: The order_id of this ListFreeResourceInfosReq.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this ListFreeResourceInfosReq.

        产品ID，即资源包ID。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The product_id of this ListFreeResourceInfosReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ListFreeResourceInfosReq.

        产品ID，即资源包ID。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param product_id: The product_id of this ListFreeResourceInfosReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this ListFreeResourceInfosReq.

        产品名称，即资源包名称。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The product_name of this ListFreeResourceInfosReq.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ListFreeResourceInfosReq.

        产品名称，即资源包名称。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param product_name: The product_name of this ListFreeResourceInfosReq.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListFreeResourceInfosReq.

        企业项目ID。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The enterprise_project_id of this ListFreeResourceInfosReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListFreeResourceInfosReq.

        企业项目ID。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param enterprise_project_id: The enterprise_project_id of this ListFreeResourceInfosReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def status(self):
        """Gets the status of this ListFreeResourceInfosReq.

        状态： 0：未生效1：生效中2：已用完3：已失效4：已退订 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The status of this ListFreeResourceInfosReq.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListFreeResourceInfosReq.

        状态： 0：未生效1：生效中2：已用完3：已失效4：已退订 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param status: The status of this ListFreeResourceInfosReq.
        :type status: int
        """
        self._status = status

    @property
    def offset(self):
        """Gets the offset of this ListFreeResourceInfosReq.

        偏移量，从0开始，默认为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this ListFreeResourceInfosReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFreeResourceInfosReq.

        偏移量，从0开始，默认为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this ListFreeResourceInfosReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListFreeResourceInfosReq.

        每次查询的记录数，默认为10。

        :return: The limit of this ListFreeResourceInfosReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFreeResourceInfosReq.

        每次查询的记录数，默认为10。

        :param limit: The limit of this ListFreeResourceInfosReq.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListFreeResourceInfosReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
