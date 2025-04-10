# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyIndividualRealnameAuthsReq:

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
        'verified_type': 'int',
        'verified_file_url': 'list[str]',
        'name': 'str',
        'verified_number': 'str',
        'change_type': 'int',
        'xaccount_type': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'identify_type': 'identify_type',
        'verified_type': 'verified_type',
        'verified_file_url': 'verified_file_url',
        'name': 'name',
        'verified_number': 'verified_number',
        'change_type': 'change_type',
        'xaccount_type': 'xaccount_type'
    }

    def __init__(self, customer_id=None, identify_type=None, verified_type=None, verified_file_url=None, name=None, verified_number=None, change_type=None, xaccount_type=None):
        r"""ApplyIndividualRealnameAuthsReq

        The model defined in huaweicloud sdk

        :param customer_id: 客户账号ID。您可以调用查询客户列表接口获取customer_id。
        :type customer_id: str
        :param identify_type: 认证方案： 0：个人证件认证
        :type identify_type: int
        :param verified_type: |参数名称：证件类型：0：身份证，上传的附件为3张，第1张是身份证人像面，第2张是身份证国徽面，第3张是个人手持身份证人像面；3：护照，上传的附件为3张，第1张是护照个人资料页，第2张是，护照入境盖章页，第3张是手持护照个人资料页；3：护照，上传的附件为2张，第1张是护照个人资料页，第2张是手持护照个人资料页；5：港澳通行证，上传的附件为3张，第1张是港澳居民来往内地通行证正面（人像面），第2张是港澳居民来往内地通行证反面，第3张是手持港澳居民来往内地通行证人像面；6：台湾通行证，上传的附件为3张，第1张是台湾居民来往大陆通行证正面（人像面），第2张是台湾居民来往大陆通行证反面，第3张是手持台湾居民来往大陆通行证人像面；9：港澳居民居住证，上传的附件为3张，第1张是港澳居民居住证人像面，第2张是，港澳居民居住证国徽面，第3张是手持港澳居民居住证人像面照片；10：台湾居民居住证，上传的附件为3张，第1张是台湾居民居住证人像面，第2张是台湾居民居住证国徽面，第3张是手持台湾居民居住证人像面照片。当identifyType&#x3D;0的时候，该字段需要填写，否则忽略该字段的取值。| |参数的约束及描述：证件类型：0：身份证，上传的附件为3张，第1张是身份证人像面，第2张是身份证国徽面，第3张是个人手持身份证人像面；3：护照，上传的附件为3张，第1张是护照个人资料页，第2张是，护照入境盖章页，第3张是手持护照个人资料页；3：护照，上传的附件为2张，第1张是护照个人资料页，第2张是手持护照个人资料页；5：港澳通行证，上传的附件为3张，第1张是港澳居民来往内地通行证正面（人像面），第2张是港澳居民来往内地通行证反面，第3张是手持港澳居民来往内地通行证人像面；6：台湾通行证，上传的附件为3张，第1张是台湾居民来往大陆通行证正面（人像面），第2张是台湾居民来往大陆通行证反面，第3张是手持台湾居民来往大陆通行证人像面；7：海外驾照，上传的附件为2张，第1张是中国以外驾照正面照片（人像面），第2张是手持中国以外驾照人像面照片；9：港澳居民居住证，上传的附件为3张，第1张是港澳居民居住证人像面，第2张是，港澳居民居住证国徽面，第3张是手持港澳居民居住证人像面照片；10：台湾居民居住证，上传的附件为3张，第1张是台湾居民居住证人像面，第2张是台湾居民居住证国徽面，第3张是手持台湾居民居住证人像面照片。当identifyType&#x3D;0的时候，该字段需要填写，否则忽略该字段的取值。|
        :type verified_type: int
        :param verified_file_url: 个人证件认证时证件附件的文件URL，该URL地址必须按照顺序填写。以护照举例，譬如护照个人资料页文件名称是abc023，手持护照个人资料页是def004，那么这个地方需要按照 abc023 def004 的顺序填写URL（文件名称区分大小写）。 证件附件目前仅仅支持jpg、jpeg、bmp、png、gif、pdf格式，单个文件最大不超过10M。这个URL是相对URL，不需要包含桶名和download目录，只要包含download目录下的子目录和对应文件名称即可。举例如下：如果上传的证件附件在桶中的位置是：https://bucketname.obs.Endpoint.myhuaweicloud.com/download/abc023.jpg，该字段填写abc023.jpg； 如果上传的证件附件在桶中的位置是：https://bucketname.obs.Endpoint.myhuaweicloud.com/download/test/abc023.jpg，该字段填写test/abc023.jpg。
        :type verified_file_url: list[str]
        :param name: 姓名。
        :type name: str
        :param verified_number: 证件号码。
        :type verified_number: str
        :param change_type: 变更类型： -1：首次实名认证
        :type change_type: int
        :param xaccount_type: 华为分给合作伙伴的平台标识。 该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值。
        :type xaccount_type: str
        """
        
        

        self._customer_id = None
        self._identify_type = None
        self._verified_type = None
        self._verified_file_url = None
        self._name = None
        self._verified_number = None
        self._change_type = None
        self._xaccount_type = None
        self.discriminator = None

        self.customer_id = customer_id
        self.identify_type = identify_type
        if verified_type is not None:
            self.verified_type = verified_type
        self.verified_file_url = verified_file_url
        self.name = name
        self.verified_number = verified_number
        if change_type is not None:
            self.change_type = change_type
        self.xaccount_type = xaccount_type

    @property
    def customer_id(self):
        r"""Gets the customer_id of this ApplyIndividualRealnameAuthsReq.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :return: The customer_id of this ApplyIndividualRealnameAuthsReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this ApplyIndividualRealnameAuthsReq.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :param customer_id: The customer_id of this ApplyIndividualRealnameAuthsReq.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def identify_type(self):
        r"""Gets the identify_type of this ApplyIndividualRealnameAuthsReq.

        认证方案： 0：个人证件认证

        :return: The identify_type of this ApplyIndividualRealnameAuthsReq.
        :rtype: int
        """
        return self._identify_type

    @identify_type.setter
    def identify_type(self, identify_type):
        r"""Sets the identify_type of this ApplyIndividualRealnameAuthsReq.

        认证方案： 0：个人证件认证

        :param identify_type: The identify_type of this ApplyIndividualRealnameAuthsReq.
        :type identify_type: int
        """
        self._identify_type = identify_type

    @property
    def verified_type(self):
        r"""Gets the verified_type of this ApplyIndividualRealnameAuthsReq.

        |参数名称：证件类型：0：身份证，上传的附件为3张，第1张是身份证人像面，第2张是身份证国徽面，第3张是个人手持身份证人像面；3：护照，上传的附件为3张，第1张是护照个人资料页，第2张是，护照入境盖章页，第3张是手持护照个人资料页；3：护照，上传的附件为2张，第1张是护照个人资料页，第2张是手持护照个人资料页；5：港澳通行证，上传的附件为3张，第1张是港澳居民来往内地通行证正面（人像面），第2张是港澳居民来往内地通行证反面，第3张是手持港澳居民来往内地通行证人像面；6：台湾通行证，上传的附件为3张，第1张是台湾居民来往大陆通行证正面（人像面），第2张是台湾居民来往大陆通行证反面，第3张是手持台湾居民来往大陆通行证人像面；9：港澳居民居住证，上传的附件为3张，第1张是港澳居民居住证人像面，第2张是，港澳居民居住证国徽面，第3张是手持港澳居民居住证人像面照片；10：台湾居民居住证，上传的附件为3张，第1张是台湾居民居住证人像面，第2张是台湾居民居住证国徽面，第3张是手持台湾居民居住证人像面照片。当identifyType=0的时候，该字段需要填写，否则忽略该字段的取值。| |参数的约束及描述：证件类型：0：身份证，上传的附件为3张，第1张是身份证人像面，第2张是身份证国徽面，第3张是个人手持身份证人像面；3：护照，上传的附件为3张，第1张是护照个人资料页，第2张是，护照入境盖章页，第3张是手持护照个人资料页；3：护照，上传的附件为2张，第1张是护照个人资料页，第2张是手持护照个人资料页；5：港澳通行证，上传的附件为3张，第1张是港澳居民来往内地通行证正面（人像面），第2张是港澳居民来往内地通行证反面，第3张是手持港澳居民来往内地通行证人像面；6：台湾通行证，上传的附件为3张，第1张是台湾居民来往大陆通行证正面（人像面），第2张是台湾居民来往大陆通行证反面，第3张是手持台湾居民来往大陆通行证人像面；7：海外驾照，上传的附件为2张，第1张是中国以外驾照正面照片（人像面），第2张是手持中国以外驾照人像面照片；9：港澳居民居住证，上传的附件为3张，第1张是港澳居民居住证人像面，第2张是，港澳居民居住证国徽面，第3张是手持港澳居民居住证人像面照片；10：台湾居民居住证，上传的附件为3张，第1张是台湾居民居住证人像面，第2张是台湾居民居住证国徽面，第3张是手持台湾居民居住证人像面照片。当identifyType=0的时候，该字段需要填写，否则忽略该字段的取值。|

        :return: The verified_type of this ApplyIndividualRealnameAuthsReq.
        :rtype: int
        """
        return self._verified_type

    @verified_type.setter
    def verified_type(self, verified_type):
        r"""Sets the verified_type of this ApplyIndividualRealnameAuthsReq.

        |参数名称：证件类型：0：身份证，上传的附件为3张，第1张是身份证人像面，第2张是身份证国徽面，第3张是个人手持身份证人像面；3：护照，上传的附件为3张，第1张是护照个人资料页，第2张是，护照入境盖章页，第3张是手持护照个人资料页；3：护照，上传的附件为2张，第1张是护照个人资料页，第2张是手持护照个人资料页；5：港澳通行证，上传的附件为3张，第1张是港澳居民来往内地通行证正面（人像面），第2张是港澳居民来往内地通行证反面，第3张是手持港澳居民来往内地通行证人像面；6：台湾通行证，上传的附件为3张，第1张是台湾居民来往大陆通行证正面（人像面），第2张是台湾居民来往大陆通行证反面，第3张是手持台湾居民来往大陆通行证人像面；9：港澳居民居住证，上传的附件为3张，第1张是港澳居民居住证人像面，第2张是，港澳居民居住证国徽面，第3张是手持港澳居民居住证人像面照片；10：台湾居民居住证，上传的附件为3张，第1张是台湾居民居住证人像面，第2张是台湾居民居住证国徽面，第3张是手持台湾居民居住证人像面照片。当identifyType=0的时候，该字段需要填写，否则忽略该字段的取值。| |参数的约束及描述：证件类型：0：身份证，上传的附件为3张，第1张是身份证人像面，第2张是身份证国徽面，第3张是个人手持身份证人像面；3：护照，上传的附件为3张，第1张是护照个人资料页，第2张是，护照入境盖章页，第3张是手持护照个人资料页；3：护照，上传的附件为2张，第1张是护照个人资料页，第2张是手持护照个人资料页；5：港澳通行证，上传的附件为3张，第1张是港澳居民来往内地通行证正面（人像面），第2张是港澳居民来往内地通行证反面，第3张是手持港澳居民来往内地通行证人像面；6：台湾通行证，上传的附件为3张，第1张是台湾居民来往大陆通行证正面（人像面），第2张是台湾居民来往大陆通行证反面，第3张是手持台湾居民来往大陆通行证人像面；7：海外驾照，上传的附件为2张，第1张是中国以外驾照正面照片（人像面），第2张是手持中国以外驾照人像面照片；9：港澳居民居住证，上传的附件为3张，第1张是港澳居民居住证人像面，第2张是，港澳居民居住证国徽面，第3张是手持港澳居民居住证人像面照片；10：台湾居民居住证，上传的附件为3张，第1张是台湾居民居住证人像面，第2张是台湾居民居住证国徽面，第3张是手持台湾居民居住证人像面照片。当identifyType=0的时候，该字段需要填写，否则忽略该字段的取值。|

        :param verified_type: The verified_type of this ApplyIndividualRealnameAuthsReq.
        :type verified_type: int
        """
        self._verified_type = verified_type

    @property
    def verified_file_url(self):
        r"""Gets the verified_file_url of this ApplyIndividualRealnameAuthsReq.

        个人证件认证时证件附件的文件URL，该URL地址必须按照顺序填写。以护照举例，譬如护照个人资料页文件名称是abc023，手持护照个人资料页是def004，那么这个地方需要按照 abc023 def004 的顺序填写URL（文件名称区分大小写）。 证件附件目前仅仅支持jpg、jpeg、bmp、png、gif、pdf格式，单个文件最大不超过10M。这个URL是相对URL，不需要包含桶名和download目录，只要包含download目录下的子目录和对应文件名称即可。举例如下：如果上传的证件附件在桶中的位置是：https://bucketname.obs.Endpoint.myhuaweicloud.com/download/abc023.jpg，该字段填写abc023.jpg； 如果上传的证件附件在桶中的位置是：https://bucketname.obs.Endpoint.myhuaweicloud.com/download/test/abc023.jpg，该字段填写test/abc023.jpg。

        :return: The verified_file_url of this ApplyIndividualRealnameAuthsReq.
        :rtype: list[str]
        """
        return self._verified_file_url

    @verified_file_url.setter
    def verified_file_url(self, verified_file_url):
        r"""Sets the verified_file_url of this ApplyIndividualRealnameAuthsReq.

        个人证件认证时证件附件的文件URL，该URL地址必须按照顺序填写。以护照举例，譬如护照个人资料页文件名称是abc023，手持护照个人资料页是def004，那么这个地方需要按照 abc023 def004 的顺序填写URL（文件名称区分大小写）。 证件附件目前仅仅支持jpg、jpeg、bmp、png、gif、pdf格式，单个文件最大不超过10M。这个URL是相对URL，不需要包含桶名和download目录，只要包含download目录下的子目录和对应文件名称即可。举例如下：如果上传的证件附件在桶中的位置是：https://bucketname.obs.Endpoint.myhuaweicloud.com/download/abc023.jpg，该字段填写abc023.jpg； 如果上传的证件附件在桶中的位置是：https://bucketname.obs.Endpoint.myhuaweicloud.com/download/test/abc023.jpg，该字段填写test/abc023.jpg。

        :param verified_file_url: The verified_file_url of this ApplyIndividualRealnameAuthsReq.
        :type verified_file_url: list[str]
        """
        self._verified_file_url = verified_file_url

    @property
    def name(self):
        r"""Gets the name of this ApplyIndividualRealnameAuthsReq.

        姓名。

        :return: The name of this ApplyIndividualRealnameAuthsReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApplyIndividualRealnameAuthsReq.

        姓名。

        :param name: The name of this ApplyIndividualRealnameAuthsReq.
        :type name: str
        """
        self._name = name

    @property
    def verified_number(self):
        r"""Gets the verified_number of this ApplyIndividualRealnameAuthsReq.

        证件号码。

        :return: The verified_number of this ApplyIndividualRealnameAuthsReq.
        :rtype: str
        """
        return self._verified_number

    @verified_number.setter
    def verified_number(self, verified_number):
        r"""Sets the verified_number of this ApplyIndividualRealnameAuthsReq.

        证件号码。

        :param verified_number: The verified_number of this ApplyIndividualRealnameAuthsReq.
        :type verified_number: str
        """
        self._verified_number = verified_number

    @property
    def change_type(self):
        r"""Gets the change_type of this ApplyIndividualRealnameAuthsReq.

        变更类型： -1：首次实名认证

        :return: The change_type of this ApplyIndividualRealnameAuthsReq.
        :rtype: int
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this ApplyIndividualRealnameAuthsReq.

        变更类型： -1：首次实名认证

        :param change_type: The change_type of this ApplyIndividualRealnameAuthsReq.
        :type change_type: int
        """
        self._change_type = change_type

    @property
    def xaccount_type(self):
        r"""Gets the xaccount_type of this ApplyIndividualRealnameAuthsReq.

        华为分给合作伙伴的平台标识。 该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值。

        :return: The xaccount_type of this ApplyIndividualRealnameAuthsReq.
        :rtype: str
        """
        return self._xaccount_type

    @xaccount_type.setter
    def xaccount_type(self, xaccount_type):
        r"""Sets the xaccount_type of this ApplyIndividualRealnameAuthsReq.

        华为分给合作伙伴的平台标识。 该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值。

        :param xaccount_type: The xaccount_type of this ApplyIndividualRealnameAuthsReq.
        :type xaccount_type: str
        """
        self._xaccount_type = xaccount_type

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
        if not isinstance(other, ApplyIndividualRealnameAuthsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
