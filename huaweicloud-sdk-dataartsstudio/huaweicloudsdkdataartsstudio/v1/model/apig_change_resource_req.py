# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApigChangeResourceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'change_mode': 'int',
        'resource_id': 'str',
        'resource_spec_code': 'str',
        'product_id': 'str',
        'promotion_info': 'str'
    }

    attribute_map = {
        'change_mode': 'change_mode',
        'resource_id': 'resource_id',
        'resource_spec_code': 'resource_spec_code',
        'product_id': 'product_id',
        'promotion_info': 'promotion_info'
    }

    def __init__(self, change_mode=None, resource_id=None, resource_spec_code=None, product_id=None, promotion_info=None):
        """ApigChangeResourceReq

        The model defined in huaweicloud sdk

        :param change_mode: 规格变更类型：10：升配；30：降配；40：续费；60：扩容；70：切换操作系统
        :type change_mode: int
        :param resource_id: 资源id
        :type resource_id: str
        :param resource_spec_code: 资源规格编码
        :type resource_spec_code: str
        :param product_id: 产品id
        :type product_id: str
        :param promotion_info: 促销信息
        :type promotion_info: str
        """
        
        

        self._change_mode = None
        self._resource_id = None
        self._resource_spec_code = None
        self._product_id = None
        self._promotion_info = None
        self.discriminator = None

        self.change_mode = change_mode
        self.resource_id = resource_id
        self.resource_spec_code = resource_spec_code
        if product_id is not None:
            self.product_id = product_id
        if promotion_info is not None:
            self.promotion_info = promotion_info

    @property
    def change_mode(self):
        """Gets the change_mode of this ApigChangeResourceReq.

        规格变更类型：10：升配；30：降配；40：续费；60：扩容；70：切换操作系统

        :return: The change_mode of this ApigChangeResourceReq.
        :rtype: int
        """
        return self._change_mode

    @change_mode.setter
    def change_mode(self, change_mode):
        """Sets the change_mode of this ApigChangeResourceReq.

        规格变更类型：10：升配；30：降配；40：续费；60：扩容；70：切换操作系统

        :param change_mode: The change_mode of this ApigChangeResourceReq.
        :type change_mode: int
        """
        self._change_mode = change_mode

    @property
    def resource_id(self):
        """Gets the resource_id of this ApigChangeResourceReq.

        资源id

        :return: The resource_id of this ApigChangeResourceReq.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ApigChangeResourceReq.

        资源id

        :param resource_id: The resource_id of this ApigChangeResourceReq.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this ApigChangeResourceReq.

        资源规格编码

        :return: The resource_spec_code of this ApigChangeResourceReq.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this ApigChangeResourceReq.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this ApigChangeResourceReq.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def product_id(self):
        """Gets the product_id of this ApigChangeResourceReq.

        产品id

        :return: The product_id of this ApigChangeResourceReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ApigChangeResourceReq.

        产品id

        :param product_id: The product_id of this ApigChangeResourceReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def promotion_info(self):
        """Gets the promotion_info of this ApigChangeResourceReq.

        促销信息

        :return: The promotion_info of this ApigChangeResourceReq.
        :rtype: str
        """
        return self._promotion_info

    @promotion_info.setter
    def promotion_info(self, promotion_info):
        """Sets the promotion_info of this ApigChangeResourceReq.

        促销信息

        :param promotion_info: The promotion_info of this ApigChangeResourceReq.
        :type promotion_info: str
        """
        self._promotion_info = promotion_info

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
        if not isinstance(other, ApigChangeResourceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
