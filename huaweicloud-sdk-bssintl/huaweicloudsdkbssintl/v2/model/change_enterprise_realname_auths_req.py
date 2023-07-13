# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeEnterpriseRealnameAuthsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'identify_type': 'int',
        'certificate_type': 'int',
        'verified_file_url': 'list[str]',
        'corp_name': 'str',
        'verified_number': 'str',
        'reg_country': 'str',
        'reg_address': 'str',
        'change_type': 'int',
        'xaccount_type': 'str',
        'enterprise_person': 'EnterprisePersonNew'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'identify_type': 'identify_type',
        'certificate_type': 'certificate_type',
        'verified_file_url': 'verified_file_url',
        'corp_name': 'corp_name',
        'verified_number': 'verified_number',
        'reg_country': 'reg_country',
        'reg_address': 'reg_address',
        'change_type': 'change_type',
        'xaccount_type': 'xaccount_type',
        'enterprise_person': 'enterprise_person'
    }

    def __init__(self, customer_id=None, identify_type=None, certificate_type=None, verified_file_url=None, corp_name=None, verified_number=None, reg_country=None, reg_address=None, change_type=None, xaccount_type=None, enterprise_person=None):
        """ChangeEnterpriseRealnameAuthsReq

        The model defined in huaweicloud sdk

        :param customer_id: 客户账号ID。您可以调用查询客户列表接口获取customer_id。
        :type customer_id: str
        :param identify_type: 认证方案： 1：单位证件扫描
        :type identify_type: int
        :param certificate_type: 单位证件类型： 0：企业营业执照 1：事业单位法人证书 2：社会团体法人登记证书 3：行政执法主体资格证 4：组织机构代码证 99：其他
        :type certificate_type: int
        :param verified_file_url: 单位证件认证时证件附件的文件URL。 附件地址必须按照顺序填写，先填写单位证件的附件，如果存在单位人员信息，再填写单位人员的身份证附件。 单位证件顺序为： 第1张单位证件照正面， 第2张单位证件照反面， 个人证件顺序为： 第1张个人证件的人像面 第2张个人证件的国徽面 假设不存在法人的情况下，第1张上传的是单位证件正面扫描件abc.023，第2张上传的是单位证件反面扫描件def004，那么上传顺序需要是： abc023 def004 的顺序填写URL（文件名称区分大小写） 证件附件目前仅仅支持jpg、jpeg、bmp、png、gif、pdf格式，单个文件最大不超过10M。 这个URL是相对URL，不需要包含桶名和download目录，只要包含download目录下的子目录和对应文件名称即可。举例如下： 如果上传的证件附件在桶中的位置是： https://bucketname.obs.Endpoint.myhuaweicloud.com/download/abc023.jpg，该字段填写abc023.jpg； 如果上传的证件附件在桶中的位置是： https://bucketname.obs.Endpoint.myhuaweicloud.com/download/test/abc023.jpg，该字段填写test/abc023.jpg。
        :type verified_file_url: list[str]
        :param corp_name: 单位名称。 不能全是数字、特殊字符、空格。
        :type corp_name: str
        :param verified_number: 单位证件号码。
        :type verified_number: str
        :param reg_country: 实名认证填写的注册国家。国家的两位字母简码。 例如：注册国家为“中国”请填写“CN”。
        :type reg_country: str
        :param reg_address: 实名认证企业注册地址。
        :type reg_address: str
        :param change_type: 变更类型： 1：个人变企业
        :type change_type: int
        :param xaccount_type: 华为分给合作伙伴的平台标识。 该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值。
        :type xaccount_type: str
        :param enterprise_person: 
        :type enterprise_person: :class:`huaweicloudsdkbssintl.v2.EnterprisePersonNew`
        """
        
        

        self._customer_id = None
        self._identify_type = None
        self._certificate_type = None
        self._verified_file_url = None
        self._corp_name = None
        self._verified_number = None
        self._reg_country = None
        self._reg_address = None
        self._change_type = None
        self._xaccount_type = None
        self._enterprise_person = None
        self.discriminator = None

        self.customer_id = customer_id
        self.identify_type = identify_type
        if certificate_type is not None:
            self.certificate_type = certificate_type
        self.verified_file_url = verified_file_url
        self.corp_name = corp_name
        self.verified_number = verified_number
        if reg_country is not None:
            self.reg_country = reg_country
        if reg_address is not None:
            self.reg_address = reg_address
        self.change_type = change_type
        self.xaccount_type = xaccount_type
        if enterprise_person is not None:
            self.enterprise_person = enterprise_person

    @property
    def customer_id(self):
        """Gets the customer_id of this ChangeEnterpriseRealnameAuthsReq.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :return: The customer_id of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ChangeEnterpriseRealnameAuthsReq.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :param customer_id: The customer_id of this ChangeEnterpriseRealnameAuthsReq.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def identify_type(self):
        """Gets the identify_type of this ChangeEnterpriseRealnameAuthsReq.

        认证方案： 1：单位证件扫描

        :return: The identify_type of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: int
        """
        return self._identify_type

    @identify_type.setter
    def identify_type(self, identify_type):
        """Sets the identify_type of this ChangeEnterpriseRealnameAuthsReq.

        认证方案： 1：单位证件扫描

        :param identify_type: The identify_type of this ChangeEnterpriseRealnameAuthsReq.
        :type identify_type: int
        """
        self._identify_type = identify_type

    @property
    def certificate_type(self):
        """Gets the certificate_type of this ChangeEnterpriseRealnameAuthsReq.

        单位证件类型： 0：企业营业执照 1：事业单位法人证书 2：社会团体法人登记证书 3：行政执法主体资格证 4：组织机构代码证 99：其他

        :return: The certificate_type of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: int
        """
        return self._certificate_type

    @certificate_type.setter
    def certificate_type(self, certificate_type):
        """Sets the certificate_type of this ChangeEnterpriseRealnameAuthsReq.

        单位证件类型： 0：企业营业执照 1：事业单位法人证书 2：社会团体法人登记证书 3：行政执法主体资格证 4：组织机构代码证 99：其他

        :param certificate_type: The certificate_type of this ChangeEnterpriseRealnameAuthsReq.
        :type certificate_type: int
        """
        self._certificate_type = certificate_type

    @property
    def verified_file_url(self):
        """Gets the verified_file_url of this ChangeEnterpriseRealnameAuthsReq.

        单位证件认证时证件附件的文件URL。 附件地址必须按照顺序填写，先填写单位证件的附件，如果存在单位人员信息，再填写单位人员的身份证附件。 单位证件顺序为： 第1张单位证件照正面， 第2张单位证件照反面， 个人证件顺序为： 第1张个人证件的人像面 第2张个人证件的国徽面 假设不存在法人的情况下，第1张上传的是单位证件正面扫描件abc.023，第2张上传的是单位证件反面扫描件def004，那么上传顺序需要是： abc023 def004 的顺序填写URL（文件名称区分大小写） 证件附件目前仅仅支持jpg、jpeg、bmp、png、gif、pdf格式，单个文件最大不超过10M。 这个URL是相对URL，不需要包含桶名和download目录，只要包含download目录下的子目录和对应文件名称即可。举例如下： 如果上传的证件附件在桶中的位置是： https://bucketname.obs.Endpoint.myhuaweicloud.com/download/abc023.jpg，该字段填写abc023.jpg； 如果上传的证件附件在桶中的位置是： https://bucketname.obs.Endpoint.myhuaweicloud.com/download/test/abc023.jpg，该字段填写test/abc023.jpg。

        :return: The verified_file_url of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: list[str]
        """
        return self._verified_file_url

    @verified_file_url.setter
    def verified_file_url(self, verified_file_url):
        """Sets the verified_file_url of this ChangeEnterpriseRealnameAuthsReq.

        单位证件认证时证件附件的文件URL。 附件地址必须按照顺序填写，先填写单位证件的附件，如果存在单位人员信息，再填写单位人员的身份证附件。 单位证件顺序为： 第1张单位证件照正面， 第2张单位证件照反面， 个人证件顺序为： 第1张个人证件的人像面 第2张个人证件的国徽面 假设不存在法人的情况下，第1张上传的是单位证件正面扫描件abc.023，第2张上传的是单位证件反面扫描件def004，那么上传顺序需要是： abc023 def004 的顺序填写URL（文件名称区分大小写） 证件附件目前仅仅支持jpg、jpeg、bmp、png、gif、pdf格式，单个文件最大不超过10M。 这个URL是相对URL，不需要包含桶名和download目录，只要包含download目录下的子目录和对应文件名称即可。举例如下： 如果上传的证件附件在桶中的位置是： https://bucketname.obs.Endpoint.myhuaweicloud.com/download/abc023.jpg，该字段填写abc023.jpg； 如果上传的证件附件在桶中的位置是： https://bucketname.obs.Endpoint.myhuaweicloud.com/download/test/abc023.jpg，该字段填写test/abc023.jpg。

        :param verified_file_url: The verified_file_url of this ChangeEnterpriseRealnameAuthsReq.
        :type verified_file_url: list[str]
        """
        self._verified_file_url = verified_file_url

    @property
    def corp_name(self):
        """Gets the corp_name of this ChangeEnterpriseRealnameAuthsReq.

        单位名称。 不能全是数字、特殊字符、空格。

        :return: The corp_name of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: str
        """
        return self._corp_name

    @corp_name.setter
    def corp_name(self, corp_name):
        """Sets the corp_name of this ChangeEnterpriseRealnameAuthsReq.

        单位名称。 不能全是数字、特殊字符、空格。

        :param corp_name: The corp_name of this ChangeEnterpriseRealnameAuthsReq.
        :type corp_name: str
        """
        self._corp_name = corp_name

    @property
    def verified_number(self):
        """Gets the verified_number of this ChangeEnterpriseRealnameAuthsReq.

        单位证件号码。

        :return: The verified_number of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: str
        """
        return self._verified_number

    @verified_number.setter
    def verified_number(self, verified_number):
        """Sets the verified_number of this ChangeEnterpriseRealnameAuthsReq.

        单位证件号码。

        :param verified_number: The verified_number of this ChangeEnterpriseRealnameAuthsReq.
        :type verified_number: str
        """
        self._verified_number = verified_number

    @property
    def reg_country(self):
        """Gets the reg_country of this ChangeEnterpriseRealnameAuthsReq.

        实名认证填写的注册国家。国家的两位字母简码。 例如：注册国家为“中国”请填写“CN”。

        :return: The reg_country of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: str
        """
        return self._reg_country

    @reg_country.setter
    def reg_country(self, reg_country):
        """Sets the reg_country of this ChangeEnterpriseRealnameAuthsReq.

        实名认证填写的注册国家。国家的两位字母简码。 例如：注册国家为“中国”请填写“CN”。

        :param reg_country: The reg_country of this ChangeEnterpriseRealnameAuthsReq.
        :type reg_country: str
        """
        self._reg_country = reg_country

    @property
    def reg_address(self):
        """Gets the reg_address of this ChangeEnterpriseRealnameAuthsReq.

        实名认证企业注册地址。

        :return: The reg_address of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: str
        """
        return self._reg_address

    @reg_address.setter
    def reg_address(self, reg_address):
        """Sets the reg_address of this ChangeEnterpriseRealnameAuthsReq.

        实名认证企业注册地址。

        :param reg_address: The reg_address of this ChangeEnterpriseRealnameAuthsReq.
        :type reg_address: str
        """
        self._reg_address = reg_address

    @property
    def change_type(self):
        """Gets the change_type of this ChangeEnterpriseRealnameAuthsReq.

        变更类型： 1：个人变企业

        :return: The change_type of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: int
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """Sets the change_type of this ChangeEnterpriseRealnameAuthsReq.

        变更类型： 1：个人变企业

        :param change_type: The change_type of this ChangeEnterpriseRealnameAuthsReq.
        :type change_type: int
        """
        self._change_type = change_type

    @property
    def xaccount_type(self):
        """Gets the xaccount_type of this ChangeEnterpriseRealnameAuthsReq.

        华为分给合作伙伴的平台标识。 该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值。

        :return: The xaccount_type of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: str
        """
        return self._xaccount_type

    @xaccount_type.setter
    def xaccount_type(self, xaccount_type):
        """Sets the xaccount_type of this ChangeEnterpriseRealnameAuthsReq.

        华为分给合作伙伴的平台标识。 该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值。

        :param xaccount_type: The xaccount_type of this ChangeEnterpriseRealnameAuthsReq.
        :type xaccount_type: str
        """
        self._xaccount_type = xaccount_type

    @property
    def enterprise_person(self):
        """Gets the enterprise_person of this ChangeEnterpriseRealnameAuthsReq.

        :return: The enterprise_person of this ChangeEnterpriseRealnameAuthsReq.
        :rtype: :class:`huaweicloudsdkbssintl.v2.EnterprisePersonNew`
        """
        return self._enterprise_person

    @enterprise_person.setter
    def enterprise_person(self, enterprise_person):
        """Sets the enterprise_person of this ChangeEnterpriseRealnameAuthsReq.

        :param enterprise_person: The enterprise_person of this ChangeEnterpriseRealnameAuthsReq.
        :type enterprise_person: :class:`huaweicloudsdkbssintl.v2.EnterprisePersonNew`
        """
        self._enterprise_person = enterprise_person

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
        if not isinstance(other, ChangeEnterpriseRealnameAuthsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
