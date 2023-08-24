# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignatureRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'signature_name': 'str',
        'signature_type': 'str',
        'app_id': 'str',
        'apply_desc': 'str',
        'file_id': 'str',
        'signature_source': 'int',
        'is_involved_third': 'str',
        'power_attorney_file_id': 'str',
        'source_title_content': 'str'
    }

    attribute_map = {
        'signature_name': 'signature_name',
        'signature_type': 'signature_type',
        'app_id': 'app_id',
        'apply_desc': 'apply_desc',
        'file_id': 'file_id',
        'signature_source': 'signature_source',
        'is_involved_third': 'is_involved_third',
        'power_attorney_file_id': 'power_attorney_file_id',
        'source_title_content': 'source_title_content'
    }

    def __init__(self, signature_name=None, signature_type=None, app_id=None, apply_desc=None, file_id=None, signature_source=None, is_involved_third=None, power_attorney_file_id=None, source_title_content=None):
        """SignatureRequest

        The model defined in huaweicloud sdk

        :param signature_name: 签名名称。
        :type signature_name: str
        :param signature_type: 签名类型。
        :type signature_type: str
        :param app_id: 短信应用ID。
        :type app_id: str
        :param apply_desc: 申请说明。
        :type apply_desc: str
        :param file_id: 营业执照文件ID。调用上传申请文件接口获取。
        :type file_id: str
        :param signature_source: 签名来源。
        :type signature_source: int
        :param is_involved_third: 是否涉及第三方权益。若为yes，则还需要传入授权委托书。
        :type is_involved_third: str
        :param power_attorney_file_id: 授权委托书文件ID。调用上传申请文件接口获取。
        :type power_attorney_file_id: str
        :param source_title_content: 签名来源标题内容，填写内容需和签名来源对应，具体如下。 - 网站域名：仅当“签名来源”为“工信部备案网站的全称或简称”时，需要输入工信部备案网站域名，如huawei.com。 - APP应用下载地址：仅当“签名来源”为“APP应用的全称或简称”时，需要填写。 - 公众号或者小程序的全称：仅当“签名来源”为“公众号或小程序的全称或简称”时，需要填写。 - 电商平台店铺地址：仅当“签名来源”为“电商平台店铺名的全称或简称”时，需要填写。
        :type source_title_content: str
        """
        
        

        self._signature_name = None
        self._signature_type = None
        self._app_id = None
        self._apply_desc = None
        self._file_id = None
        self._signature_source = None
        self._is_involved_third = None
        self._power_attorney_file_id = None
        self._source_title_content = None
        self.discriminator = None

        self.signature_name = signature_name
        self.signature_type = signature_type
        self.app_id = app_id
        if apply_desc is not None:
            self.apply_desc = apply_desc
        self.file_id = file_id
        self.signature_source = signature_source
        self.is_involved_third = is_involved_third
        if power_attorney_file_id is not None:
            self.power_attorney_file_id = power_attorney_file_id
        if source_title_content is not None:
            self.source_title_content = source_title_content

    @property
    def signature_name(self):
        """Gets the signature_name of this SignatureRequest.

        签名名称。

        :return: The signature_name of this SignatureRequest.
        :rtype: str
        """
        return self._signature_name

    @signature_name.setter
    def signature_name(self, signature_name):
        """Sets the signature_name of this SignatureRequest.

        签名名称。

        :param signature_name: The signature_name of this SignatureRequest.
        :type signature_name: str
        """
        self._signature_name = signature_name

    @property
    def signature_type(self):
        """Gets the signature_type of this SignatureRequest.

        签名类型。

        :return: The signature_type of this SignatureRequest.
        :rtype: str
        """
        return self._signature_type

    @signature_type.setter
    def signature_type(self, signature_type):
        """Sets the signature_type of this SignatureRequest.

        签名类型。

        :param signature_type: The signature_type of this SignatureRequest.
        :type signature_type: str
        """
        self._signature_type = signature_type

    @property
    def app_id(self):
        """Gets the app_id of this SignatureRequest.

        短信应用ID。

        :return: The app_id of this SignatureRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this SignatureRequest.

        短信应用ID。

        :param app_id: The app_id of this SignatureRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def apply_desc(self):
        """Gets the apply_desc of this SignatureRequest.

        申请说明。

        :return: The apply_desc of this SignatureRequest.
        :rtype: str
        """
        return self._apply_desc

    @apply_desc.setter
    def apply_desc(self, apply_desc):
        """Sets the apply_desc of this SignatureRequest.

        申请说明。

        :param apply_desc: The apply_desc of this SignatureRequest.
        :type apply_desc: str
        """
        self._apply_desc = apply_desc

    @property
    def file_id(self):
        """Gets the file_id of this SignatureRequest.

        营业执照文件ID。调用上传申请文件接口获取。

        :return: The file_id of this SignatureRequest.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this SignatureRequest.

        营业执照文件ID。调用上传申请文件接口获取。

        :param file_id: The file_id of this SignatureRequest.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def signature_source(self):
        """Gets the signature_source of this SignatureRequest.

        签名来源。

        :return: The signature_source of this SignatureRequest.
        :rtype: int
        """
        return self._signature_source

    @signature_source.setter
    def signature_source(self, signature_source):
        """Sets the signature_source of this SignatureRequest.

        签名来源。

        :param signature_source: The signature_source of this SignatureRequest.
        :type signature_source: int
        """
        self._signature_source = signature_source

    @property
    def is_involved_third(self):
        """Gets the is_involved_third of this SignatureRequest.

        是否涉及第三方权益。若为yes，则还需要传入授权委托书。

        :return: The is_involved_third of this SignatureRequest.
        :rtype: str
        """
        return self._is_involved_third

    @is_involved_third.setter
    def is_involved_third(self, is_involved_third):
        """Sets the is_involved_third of this SignatureRequest.

        是否涉及第三方权益。若为yes，则还需要传入授权委托书。

        :param is_involved_third: The is_involved_third of this SignatureRequest.
        :type is_involved_third: str
        """
        self._is_involved_third = is_involved_third

    @property
    def power_attorney_file_id(self):
        """Gets the power_attorney_file_id of this SignatureRequest.

        授权委托书文件ID。调用上传申请文件接口获取。

        :return: The power_attorney_file_id of this SignatureRequest.
        :rtype: str
        """
        return self._power_attorney_file_id

    @power_attorney_file_id.setter
    def power_attorney_file_id(self, power_attorney_file_id):
        """Sets the power_attorney_file_id of this SignatureRequest.

        授权委托书文件ID。调用上传申请文件接口获取。

        :param power_attorney_file_id: The power_attorney_file_id of this SignatureRequest.
        :type power_attorney_file_id: str
        """
        self._power_attorney_file_id = power_attorney_file_id

    @property
    def source_title_content(self):
        """Gets the source_title_content of this SignatureRequest.

        签名来源标题内容，填写内容需和签名来源对应，具体如下。 - 网站域名：仅当“签名来源”为“工信部备案网站的全称或简称”时，需要输入工信部备案网站域名，如huawei.com。 - APP应用下载地址：仅当“签名来源”为“APP应用的全称或简称”时，需要填写。 - 公众号或者小程序的全称：仅当“签名来源”为“公众号或小程序的全称或简称”时，需要填写。 - 电商平台店铺地址：仅当“签名来源”为“电商平台店铺名的全称或简称”时，需要填写。

        :return: The source_title_content of this SignatureRequest.
        :rtype: str
        """
        return self._source_title_content

    @source_title_content.setter
    def source_title_content(self, source_title_content):
        """Sets the source_title_content of this SignatureRequest.

        签名来源标题内容，填写内容需和签名来源对应，具体如下。 - 网站域名：仅当“签名来源”为“工信部备案网站的全称或简称”时，需要输入工信部备案网站域名，如huawei.com。 - APP应用下载地址：仅当“签名来源”为“APP应用的全称或简称”时，需要填写。 - 公众号或者小程序的全称：仅当“签名来源”为“公众号或小程序的全称或简称”时，需要填写。 - 电商平台店铺地址：仅当“签名来源”为“电商平台店铺名的全称或简称”时，需要填写。

        :param source_title_content: The source_title_content of this SignatureRequest.
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
        if not isinstance(other, SignatureRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
