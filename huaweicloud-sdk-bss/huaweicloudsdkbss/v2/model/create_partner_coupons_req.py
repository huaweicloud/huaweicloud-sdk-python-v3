# coding: utf-8

import pprint
import re

import six





class CreatePartnerCouponsReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'quota_id': 'str',
        'customer_ids': 'list[str]',
        'face_value': 'float',
        'valid_time': 'str',
        'expire_time': 'str',
        'cloud_service_types': 'list[str]',
        'product_ids': 'list[str]',
        'memo': 'str',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'quota_id': 'quota_id',
        'customer_ids': 'customer_ids',
        'face_value': 'face_value',
        'valid_time': 'valid_time',
        'expire_time': 'expire_time',
        'cloud_service_types': 'cloud_service_types',
        'product_ids': 'product_ids',
        'memo': 'memo',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, quota_id=None, customer_ids=None, face_value=None, valid_time=None, expire_time=None, cloud_service_types=None, product_ids=None, memo=None, indirect_partner_id=None):
        """CreatePartnerCouponsReq - a model defined in huaweicloud sdk"""
        
        

        self._quota_id = None
        self._customer_ids = None
        self._face_value = None
        self._valid_time = None
        self._expire_time = None
        self._cloud_service_types = None
        self._product_ids = None
        self._memo = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.quota_id = quota_id
        self.customer_ids = customer_ids
        self.face_value = face_value
        if valid_time is not None:
            self.valid_time = valid_time
        if expire_time is not None:
            self.expire_time = expire_time
        if cloud_service_types is not None:
            self.cloud_service_types = cloud_service_types
        if product_ids is not None:
            self.product_ids = product_ids
        if memo is not None:
            self.memo = memo
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def quota_id(self):
        """Gets the quota_id of this CreatePartnerCouponsReq.

        |参数名称：优惠券额度ID优惠券的类型跟随额度中的类型。| |参数约束及描述：优惠券额度ID优惠券的类型跟随额度中的类型。|

        :return: The quota_id of this CreatePartnerCouponsReq.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this CreatePartnerCouponsReq.

        |参数名称：优惠券额度ID优惠券的类型跟随额度中的类型。| |参数约束及描述：优惠券额度ID优惠券的类型跟随额度中的类型。|

        :param quota_id: The quota_id of this CreatePartnerCouponsReq.
        :type: str
        """
        self._quota_id = quota_id

    @property
    def customer_ids(self):
        """Gets the customer_ids of this CreatePartnerCouponsReq.

        |参数名称：客户ID列表| |参数约束以及描述：客户ID列表|

        :return: The customer_ids of this CreatePartnerCouponsReq.
        :rtype: list[str]
        """
        return self._customer_ids

    @customer_ids.setter
    def customer_ids(self, customer_ids):
        """Sets the customer_ids of this CreatePartnerCouponsReq.

        |参数名称：客户ID列表| |参数约束以及描述：客户ID列表|

        :param customer_ids: The customer_ids of this CreatePartnerCouponsReq.
        :type: list[str]
        """
        self._customer_ids = customer_ids

    @property
    def face_value(self):
        """Gets the face_value of this CreatePartnerCouponsReq.

        |参数名称：优惠券的面值：小数点后2位。浮点数精度为：小数点后两位| |参数的约束及描述：优惠券的面值：小数点后2位|

        :return: The face_value of this CreatePartnerCouponsReq.
        :rtype: float
        """
        return self._face_value

    @face_value.setter
    def face_value(self, face_value):
        """Sets the face_value of this CreatePartnerCouponsReq.

        |参数名称：优惠券的面值：小数点后2位。浮点数精度为：小数点后两位| |参数的约束及描述：优惠券的面值：小数点后2位|

        :param face_value: The face_value of this CreatePartnerCouponsReq.
        :type: float
        """
        self._face_value = face_value

    @property
    def valid_time(self):
        """Gets the valid_time of this CreatePartnerCouponsReq.

        |参数名称：优惠券的生效时间,UTC格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：优惠券的生效时间,UTC格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The valid_time of this CreatePartnerCouponsReq.
        :rtype: str
        """
        return self._valid_time

    @valid_time.setter
    def valid_time(self, valid_time):
        """Sets the valid_time of this CreatePartnerCouponsReq.

        |参数名称：优惠券的生效时间,UTC格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：优惠券的生效时间,UTC格式：yyyy-MM-ddTHH:mm:ssZ|

        :param valid_time: The valid_time of this CreatePartnerCouponsReq.
        :type: str
        """
        self._valid_time = valid_time

    @property
    def expire_time(self):
        """Gets the expire_time of this CreatePartnerCouponsReq.

        |参数名称：优惠券的失效时间,UTC格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：优惠券的失效时间,UTC格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The expire_time of this CreatePartnerCouponsReq.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CreatePartnerCouponsReq.

        |参数名称：优惠券的失效时间,UTC格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：优惠券的失效时间,UTC格式：yyyy-MM-ddTHH:mm:ssZ|

        :param expire_time: The expire_time of this CreatePartnerCouponsReq.
        :type: str
        """
        self._expire_time = expire_time

    @property
    def cloud_service_types(self):
        """Gets the cloud_service_types of this CreatePartnerCouponsReq.

        |参数名称：云服务限制| |参数约束以及描述：云服务限制|

        :return: The cloud_service_types of this CreatePartnerCouponsReq.
        :rtype: list[str]
        """
        return self._cloud_service_types

    @cloud_service_types.setter
    def cloud_service_types(self, cloud_service_types):
        """Sets the cloud_service_types of this CreatePartnerCouponsReq.

        |参数名称：云服务限制| |参数约束以及描述：云服务限制|

        :param cloud_service_types: The cloud_service_types of this CreatePartnerCouponsReq.
        :type: list[str]
        """
        self._cloud_service_types = cloud_service_types

    @property
    def product_ids(self):
        """Gets the product_ids of this CreatePartnerCouponsReq.

        |参数名称：产品限制| |参数约束以及描述：产品限制|

        :return: The product_ids of this CreatePartnerCouponsReq.
        :rtype: list[str]
        """
        return self._product_ids

    @product_ids.setter
    def product_ids(self, product_ids):
        """Sets the product_ids of this CreatePartnerCouponsReq.

        |参数名称：产品限制| |参数约束以及描述：产品限制|

        :param product_ids: The product_ids of this CreatePartnerCouponsReq.
        :type: list[str]
        """
        self._product_ids = product_ids

    @property
    def memo(self):
        """Gets the memo of this CreatePartnerCouponsReq.

        |参数名称：发券时的备注信息| |参数约束及描述：发券时的备注信息|

        :return: The memo of this CreatePartnerCouponsReq.
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this CreatePartnerCouponsReq.

        |参数名称：发券时的备注信息| |参数约束及描述：发券时的备注信息|

        :param memo: The memo of this CreatePartnerCouponsReq.
        :type: str
        """
        self._memo = memo

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this CreatePartnerCouponsReq.

        |参数名称：二级经销商ID| |参数约束及描述：如果一级经销商要给二级经销商的子客户设置折扣，需要携带这个字段|

        :return: The indirect_partner_id of this CreatePartnerCouponsReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this CreatePartnerCouponsReq.

        |参数名称：二级经销商ID| |参数约束及描述：如果一级经销商要给二级经销商的子客户设置折扣，需要携带这个字段|

        :param indirect_partner_id: The indirect_partner_id of this CreatePartnerCouponsReq.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreatePartnerCouponsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
