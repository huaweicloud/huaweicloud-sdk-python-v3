# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsSignatureReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'apply_desc': 'str',
        'file_id': 'str',
        'is_involved_third': 'str',
        'power_attorney_fileid': 'str',
        'signature_name': 'str',
        'signature_source': 'int',
        'signature_type': 'str',
        'source_title_content': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'apply_desc': 'apply_desc',
        'file_id': 'file_id',
        'is_involved_third': 'is_involved_third',
        'power_attorney_fileid': 'power_attorney_fileid',
        'signature_name': 'signature_name',
        'signature_source': 'signature_source',
        'signature_type': 'signature_type',
        'source_title_content': 'source_title_content'
    }

    def __init__(self, app_id=None, apply_desc=None, file_id=None, is_involved_third=None, power_attorney_fileid=None, signature_name=None, signature_source=None, signature_type=None, source_title_content=None):
        """SmsSignatureReq

        The model defined in huaweicloud sdk

        :param app_id: 应用主键ID
        :type app_id: str
        :param apply_desc: 申请说明
        :type apply_desc: str
        :param file_id: 营业执照文件ID
        :type file_id: str
        :param is_involved_third: 是否涉及第三方权益 1. Yes: 是 2. No:
        :type is_involved_third: str
        :param power_attorney_fileid: 授权委托书文件ID
        :type power_attorney_fileid: str
        :param signature_name: 签名名称
        :type signature_name: str
        :param signature_source: 签名来源。支持枚举值： 1. 0：企事业单位的全称或简称 2. 1：工信部备案网站的全称或简称 3. 2： APP应用的全称或简称 4. 3：公众号或小程序的全称或简称 5. 4：电商平台店铺名的全称或简称 6. 5：商标名的全称或简称
        :type signature_source: int
        :param signature_type: 签名类型。支持枚举值： 1. VERIFY_CODE_TYPE: 验证码类 2. PROMOTION_TYPE: 推广类 3. NOTIFY_TYPE: 通知类
        :type signature_type: str
        :param source_title_content: 签名来源标题内容
        :type source_title_content: str
        """
        
        

        self._app_id = None
        self._apply_desc = None
        self._file_id = None
        self._is_involved_third = None
        self._power_attorney_fileid = None
        self._signature_name = None
        self._signature_source = None
        self._signature_type = None
        self._source_title_content = None
        self.discriminator = None

        self.app_id = app_id
        if apply_desc is not None:
            self.apply_desc = apply_desc
        if file_id is not None:
            self.file_id = file_id
        self.is_involved_third = is_involved_third
        if power_attorney_fileid is not None:
            self.power_attorney_fileid = power_attorney_fileid
        self.signature_name = signature_name
        self.signature_source = signature_source
        self.signature_type = signature_type
        if source_title_content is not None:
            self.source_title_content = source_title_content

    @property
    def app_id(self):
        """Gets the app_id of this SmsSignatureReq.

        应用主键ID

        :return: The app_id of this SmsSignatureReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this SmsSignatureReq.

        应用主键ID

        :param app_id: The app_id of this SmsSignatureReq.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def apply_desc(self):
        """Gets the apply_desc of this SmsSignatureReq.

        申请说明

        :return: The apply_desc of this SmsSignatureReq.
        :rtype: str
        """
        return self._apply_desc

    @apply_desc.setter
    def apply_desc(self, apply_desc):
        """Sets the apply_desc of this SmsSignatureReq.

        申请说明

        :param apply_desc: The apply_desc of this SmsSignatureReq.
        :type apply_desc: str
        """
        self._apply_desc = apply_desc

    @property
    def file_id(self):
        """Gets the file_id of this SmsSignatureReq.

        营业执照文件ID

        :return: The file_id of this SmsSignatureReq.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this SmsSignatureReq.

        营业执照文件ID

        :param file_id: The file_id of this SmsSignatureReq.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def is_involved_third(self):
        """Gets the is_involved_third of this SmsSignatureReq.

        是否涉及第三方权益 1. Yes: 是 2. No:

        :return: The is_involved_third of this SmsSignatureReq.
        :rtype: str
        """
        return self._is_involved_third

    @is_involved_third.setter
    def is_involved_third(self, is_involved_third):
        """Sets the is_involved_third of this SmsSignatureReq.

        是否涉及第三方权益 1. Yes: 是 2. No:

        :param is_involved_third: The is_involved_third of this SmsSignatureReq.
        :type is_involved_third: str
        """
        self._is_involved_third = is_involved_third

    @property
    def power_attorney_fileid(self):
        """Gets the power_attorney_fileid of this SmsSignatureReq.

        授权委托书文件ID

        :return: The power_attorney_fileid of this SmsSignatureReq.
        :rtype: str
        """
        return self._power_attorney_fileid

    @power_attorney_fileid.setter
    def power_attorney_fileid(self, power_attorney_fileid):
        """Sets the power_attorney_fileid of this SmsSignatureReq.

        授权委托书文件ID

        :param power_attorney_fileid: The power_attorney_fileid of this SmsSignatureReq.
        :type power_attorney_fileid: str
        """
        self._power_attorney_fileid = power_attorney_fileid

    @property
    def signature_name(self):
        """Gets the signature_name of this SmsSignatureReq.

        签名名称

        :return: The signature_name of this SmsSignatureReq.
        :rtype: str
        """
        return self._signature_name

    @signature_name.setter
    def signature_name(self, signature_name):
        """Sets the signature_name of this SmsSignatureReq.

        签名名称

        :param signature_name: The signature_name of this SmsSignatureReq.
        :type signature_name: str
        """
        self._signature_name = signature_name

    @property
    def signature_source(self):
        """Gets the signature_source of this SmsSignatureReq.

        签名来源。支持枚举值： 1. 0：企事业单位的全称或简称 2. 1：工信部备案网站的全称或简称 3. 2： APP应用的全称或简称 4. 3：公众号或小程序的全称或简称 5. 4：电商平台店铺名的全称或简称 6. 5：商标名的全称或简称

        :return: The signature_source of this SmsSignatureReq.
        :rtype: int
        """
        return self._signature_source

    @signature_source.setter
    def signature_source(self, signature_source):
        """Sets the signature_source of this SmsSignatureReq.

        签名来源。支持枚举值： 1. 0：企事业单位的全称或简称 2. 1：工信部备案网站的全称或简称 3. 2： APP应用的全称或简称 4. 3：公众号或小程序的全称或简称 5. 4：电商平台店铺名的全称或简称 6. 5：商标名的全称或简称

        :param signature_source: The signature_source of this SmsSignatureReq.
        :type signature_source: int
        """
        self._signature_source = signature_source

    @property
    def signature_type(self):
        """Gets the signature_type of this SmsSignatureReq.

        签名类型。支持枚举值： 1. VERIFY_CODE_TYPE: 验证码类 2. PROMOTION_TYPE: 推广类 3. NOTIFY_TYPE: 通知类

        :return: The signature_type of this SmsSignatureReq.
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """Sets the signature_type of this SmsSignatureReq.

        签名类型。支持枚举值： 1. VERIFY_CODE_TYPE: 验证码类 2. PROMOTION_TYPE: 推广类 3. NOTIFY_TYPE: 通知类

        :param signature_type: The signature_type of this SmsSignatureReq.
        :type signature_type: str
        """
        self._signature_type = signature_type

    @property
    def source_title_content(self):
        """Gets the source_title_content of this SmsSignatureReq.

        签名来源标题内容

        :return: The source_title_content of this SmsSignatureReq.
        :rtype: str
        """
        return self._source_title_content

    @source_title_content.setter
    def source_title_content(self, source_title_content):
        """Sets the source_title_content of this SmsSignatureReq.

        签名来源标题内容

        :param source_title_content: The source_title_content of this SmsSignatureReq.
        :type source_title_content: str
        """
        self._source_title_content = source_title_content

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
        if not isinstance(other, SmsSignatureReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
