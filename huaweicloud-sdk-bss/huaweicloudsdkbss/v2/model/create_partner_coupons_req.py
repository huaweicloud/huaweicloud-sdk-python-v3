# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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

        优惠券额度ID。该值在查询优惠券额度接口的响应参数中获取。

        :return: The quota_id of this CreatePartnerCouponsReq.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this CreatePartnerCouponsReq.

        优惠券额度ID。该值在查询优惠券额度接口的响应参数中获取。

        :param quota_id: The quota_id of this CreatePartnerCouponsReq.
        :type: str
        """
        self._quota_id = quota_id

    @property
    def customer_ids(self):
        """Gets the customer_ids of this CreatePartnerCouponsReq.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :return: The customer_ids of this CreatePartnerCouponsReq.
        :rtype: list[str]
        """
        return self._customer_ids

    @customer_ids.setter
    def customer_ids(self, customer_ids):
        """Sets the customer_ids of this CreatePartnerCouponsReq.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :param customer_ids: The customer_ids of this CreatePartnerCouponsReq.
        :type: list[str]
        """
        self._customer_ids = customer_ids

    @property
    def face_value(self):
        """Gets the face_value of this CreatePartnerCouponsReq.

        代金券面值。 单位：元。取值大于0且精确到小数点后2位。

        :return: The face_value of this CreatePartnerCouponsReq.
        :rtype: float
        """
        return self._face_value

    @face_value.setter
    def face_value(self, face_value):
        """Sets the face_value of this CreatePartnerCouponsReq.

        代金券面值。 单位：元。取值大于0且精确到小数点后2位。

        :param face_value: The face_value of this CreatePartnerCouponsReq.
        :type: float
        """
        self._face_value = face_value

    @property
    def valid_time(self):
        """Gets the valid_time of this CreatePartnerCouponsReq.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The valid_time of this CreatePartnerCouponsReq.
        :rtype: str
        """
        return self._valid_time

    @valid_time.setter
    def valid_time(self, valid_time):
        """Sets the valid_time of this CreatePartnerCouponsReq.

        生效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param valid_time: The valid_time of this CreatePartnerCouponsReq.
        :type: str
        """
        self._valid_time = valid_time

    @property
    def expire_time(self):
        """Gets the expire_time of this CreatePartnerCouponsReq.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :return: The expire_time of this CreatePartnerCouponsReq.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CreatePartnerCouponsReq.

        失效时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。

        :param expire_time: The expire_time of this CreatePartnerCouponsReq.
        :type: str
        """
        self._expire_time = expire_time

    @property
    def cloud_service_types(self):
        """Gets the cloud_service_types of this CreatePartnerCouponsReq.

        允许使用的云服务列表，您可以调用查询云服务类型列表接口获取。 多个云服务产品以“,”隔开，最多支持10个。 默认：空（继承额度上的限制）  说明： 如果额度上有限制云服务类型列表，则优惠券上的限制不能超过额度的限制。如果额度上没有限制，则优惠券上可以随意指定云服务类型。

        :return: The cloud_service_types of this CreatePartnerCouponsReq.
        :rtype: list[str]
        """
        return self._cloud_service_types

    @cloud_service_types.setter
    def cloud_service_types(self, cloud_service_types):
        """Sets the cloud_service_types of this CreatePartnerCouponsReq.

        允许使用的云服务列表，您可以调用查询云服务类型列表接口获取。 多个云服务产品以“,”隔开，最多支持10个。 默认：空（继承额度上的限制）  说明： 如果额度上有限制云服务类型列表，则优惠券上的限制不能超过额度的限制。如果额度上没有限制，则优惠券上可以随意指定云服务类型。

        :param cloud_service_types: The cloud_service_types of this CreatePartnerCouponsReq.
        :type: list[str]
        """
        self._cloud_service_types = cloud_service_types

    @property
    def product_ids(self):
        """Gets the product_ids of this CreatePartnerCouponsReq.

        允许使用的产品列表。 多个产品以“,”隔开，最多支持10个。 默认：空（继承额度上的限制）  说明： 如果额度上有限制产品列表，则优惠券上的限制不能超过额度的限制。如果额度上没有限制，则优惠券上可以随意指定产品ID。 产品ID需要合作伙伴通过线下获得。

        :return: The product_ids of this CreatePartnerCouponsReq.
        :rtype: list[str]
        """
        return self._product_ids

    @product_ids.setter
    def product_ids(self, product_ids):
        """Sets the product_ids of this CreatePartnerCouponsReq.

        允许使用的产品列表。 多个产品以“,”隔开，最多支持10个。 默认：空（继承额度上的限制）  说明： 如果额度上有限制产品列表，则优惠券上的限制不能超过额度的限制。如果额度上没有限制，则优惠券上可以随意指定产品ID。 产品ID需要合作伙伴通过线下获得。

        :param product_ids: The product_ids of this CreatePartnerCouponsReq.
        :type: list[str]
        """
        self._product_ids = product_ids

    @property
    def memo(self):
        """Gets the memo of this CreatePartnerCouponsReq.

        发券时的备注信息。

        :return: The memo of this CreatePartnerCouponsReq.
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this CreatePartnerCouponsReq.

        发券时的备注信息。

        :param memo: The memo of this CreatePartnerCouponsReq.
        :type: str
        """
        self._memo = memo

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this CreatePartnerCouponsReq.

        精英服务商ID。获取方法请参见查询精英服务商列表。 精英服务商给子客户发放优惠券时，需要携带该参数。

        :return: The indirect_partner_id of this CreatePartnerCouponsReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this CreatePartnerCouponsReq.

        精英服务商ID。获取方法请参见查询精英服务商列表。 精英服务商给子客户发放优惠券时，需要携带该参数。

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
        if not isinstance(other, CreatePartnerCouponsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
