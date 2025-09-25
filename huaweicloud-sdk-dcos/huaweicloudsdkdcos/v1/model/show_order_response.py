# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOrderResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'number': 'str',
        'title': 'str',
        'type': 'str',
        'sub_type': 'str',
        'model_code': 'str',
        'operation_objects': 'list[OperationObject]',
        'operation_attachments': 'list[UploadFileInfo]',
        'access_whitelist': 'AccessWhiteList',
        'delivery_info': 'DeliveryInfo',
        'additional_attachments': 'list[UploadFileInfo]',
        'additional_content': 'str',
        'country_code': 'str',
        'phone': 'str',
        'stage': 'str',
        'status': 'str',
        'logs': 'list[OrderLog]',
        'fields': 'list[FieldEntity]',
        'applicant': 'str',
        'is_accept_terms': 'bool',
        'create_time': 'str',
        'verification': 'OrderVerification'
    }

    attribute_map = {
        'number': 'number',
        'title': 'title',
        'type': 'type',
        'sub_type': 'sub_type',
        'model_code': 'model_code',
        'operation_objects': 'operation_objects',
        'operation_attachments': 'operation_attachments',
        'access_whitelist': 'access_whitelist',
        'delivery_info': 'delivery_info',
        'additional_attachments': 'additional_attachments',
        'additional_content': 'additional_content',
        'country_code': 'country_code',
        'phone': 'phone',
        'stage': 'stage',
        'status': 'status',
        'logs': 'logs',
        'fields': 'fields',
        'applicant': 'applicant',
        'is_accept_terms': 'is_accept_terms',
        'create_time': 'create_time',
        'verification': 'verification'
    }

    def __init__(self, number=None, title=None, type=None, sub_type=None, model_code=None, operation_objects=None, operation_attachments=None, access_whitelist=None, delivery_info=None, additional_attachments=None, additional_content=None, country_code=None, phone=None, stage=None, status=None, logs=None, fields=None, applicant=None, is_accept_terms=None, create_time=None, verification=None):
        r"""ShowOrderResponse

        The model defined in huaweicloud sdk

        :param number: 服务单号
        :type number: str
        :param title: 标题
        :type title: str
        :param type: 服务单类型:IDC运维 设备运维 设备检查 客户陪同
        :type type: str
        :param sub_type: 具体操作类型:设备物理上下电
        :type sub_type: str
        :param model_code: 服务单类型编码
        :type model_code: str
        :param operation_objects: 操作对象
        :type operation_objects: list[:class:`huaweicloudsdkdcos.v1.OperationObject`]
        :param operation_attachments: 操作内容附件
        :type operation_attachments: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        :param access_whitelist: 
        :type access_whitelist: :class:`huaweicloudsdkdcos.v1.AccessWhiteList`
        :param delivery_info: 
        :type delivery_info: :class:`huaweicloudsdkdcos.v1.DeliveryInfo`
        :param additional_attachments: 补充附件
        :type additional_attachments: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        :param additional_content: 补充说明
        :type additional_content: str
        :param country_code: 手机国际码
        :type country_code: str
        :param phone: 联系电话
        :type phone: str
        :param stage: 当前阶段.DRAFT草稿、SUMMITED服务申请、IN_PROGRESS服务处理中、ACCEPTANCE服务验收、CLOSED服务关闭
        :type stage: str
        :param status: 当前状态
        :type status: str
        :param logs: 服务单日志
        :type logs: list[:class:`huaweicloudsdkdcos.v1.OrderLog`]
        :param fields: 扩展字段
        :type fields: list[:class:`huaweicloudsdkdcos.v1.FieldEntity`]
        :param applicant: 申请人
        :type applicant: str
        :param is_accept_terms: 是否同意服务条款
        :type is_accept_terms: bool
        :param create_time: 申请时间/创建时间
        :type create_time: str
        :param verification: 
        :type verification: :class:`huaweicloudsdkdcos.v1.OrderVerification`
        """
        
        super(ShowOrderResponse, self).__init__()

        self._number = None
        self._title = None
        self._type = None
        self._sub_type = None
        self._model_code = None
        self._operation_objects = None
        self._operation_attachments = None
        self._access_whitelist = None
        self._delivery_info = None
        self._additional_attachments = None
        self._additional_content = None
        self._country_code = None
        self._phone = None
        self._stage = None
        self._status = None
        self._logs = None
        self._fields = None
        self._applicant = None
        self._is_accept_terms = None
        self._create_time = None
        self._verification = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if sub_type is not None:
            self.sub_type = sub_type
        if model_code is not None:
            self.model_code = model_code
        if operation_objects is not None:
            self.operation_objects = operation_objects
        if operation_attachments is not None:
            self.operation_attachments = operation_attachments
        if access_whitelist is not None:
            self.access_whitelist = access_whitelist
        if delivery_info is not None:
            self.delivery_info = delivery_info
        if additional_attachments is not None:
            self.additional_attachments = additional_attachments
        if additional_content is not None:
            self.additional_content = additional_content
        if country_code is not None:
            self.country_code = country_code
        if phone is not None:
            self.phone = phone
        if stage is not None:
            self.stage = stage
        if status is not None:
            self.status = status
        if logs is not None:
            self.logs = logs
        if fields is not None:
            self.fields = fields
        if applicant is not None:
            self.applicant = applicant
        if is_accept_terms is not None:
            self.is_accept_terms = is_accept_terms
        if create_time is not None:
            self.create_time = create_time
        if verification is not None:
            self.verification = verification

    @property
    def number(self):
        r"""Gets the number of this ShowOrderResponse.

        服务单号

        :return: The number of this ShowOrderResponse.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this ShowOrderResponse.

        服务单号

        :param number: The number of this ShowOrderResponse.
        :type number: str
        """
        self._number = number

    @property
    def title(self):
        r"""Gets the title of this ShowOrderResponse.

        标题

        :return: The title of this ShowOrderResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ShowOrderResponse.

        标题

        :param title: The title of this ShowOrderResponse.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        r"""Gets the type of this ShowOrderResponse.

        服务单类型:IDC运维 设备运维 设备检查 客户陪同

        :return: The type of this ShowOrderResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowOrderResponse.

        服务单类型:IDC运维 设备运维 设备检查 客户陪同

        :param type: The type of this ShowOrderResponse.
        :type type: str
        """
        self._type = type

    @property
    def sub_type(self):
        r"""Gets the sub_type of this ShowOrderResponse.

        具体操作类型:设备物理上下电

        :return: The sub_type of this ShowOrderResponse.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        r"""Sets the sub_type of this ShowOrderResponse.

        具体操作类型:设备物理上下电

        :param sub_type: The sub_type of this ShowOrderResponse.
        :type sub_type: str
        """
        self._sub_type = sub_type

    @property
    def model_code(self):
        r"""Gets the model_code of this ShowOrderResponse.

        服务单类型编码

        :return: The model_code of this ShowOrderResponse.
        :rtype: str
        """
        return self._model_code

    @model_code.setter
    def model_code(self, model_code):
        r"""Sets the model_code of this ShowOrderResponse.

        服务单类型编码

        :param model_code: The model_code of this ShowOrderResponse.
        :type model_code: str
        """
        self._model_code = model_code

    @property
    def operation_objects(self):
        r"""Gets the operation_objects of this ShowOrderResponse.

        操作对象

        :return: The operation_objects of this ShowOrderResponse.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.OperationObject`]
        """
        return self._operation_objects

    @operation_objects.setter
    def operation_objects(self, operation_objects):
        r"""Sets the operation_objects of this ShowOrderResponse.

        操作对象

        :param operation_objects: The operation_objects of this ShowOrderResponse.
        :type operation_objects: list[:class:`huaweicloudsdkdcos.v1.OperationObject`]
        """
        self._operation_objects = operation_objects

    @property
    def operation_attachments(self):
        r"""Gets the operation_attachments of this ShowOrderResponse.

        操作内容附件

        :return: The operation_attachments of this ShowOrderResponse.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        return self._operation_attachments

    @operation_attachments.setter
    def operation_attachments(self, operation_attachments):
        r"""Sets the operation_attachments of this ShowOrderResponse.

        操作内容附件

        :param operation_attachments: The operation_attachments of this ShowOrderResponse.
        :type operation_attachments: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        self._operation_attachments = operation_attachments

    @property
    def access_whitelist(self):
        r"""Gets the access_whitelist of this ShowOrderResponse.

        :return: The access_whitelist of this ShowOrderResponse.
        :rtype: :class:`huaweicloudsdkdcos.v1.AccessWhiteList`
        """
        return self._access_whitelist

    @access_whitelist.setter
    def access_whitelist(self, access_whitelist):
        r"""Sets the access_whitelist of this ShowOrderResponse.

        :param access_whitelist: The access_whitelist of this ShowOrderResponse.
        :type access_whitelist: :class:`huaweicloudsdkdcos.v1.AccessWhiteList`
        """
        self._access_whitelist = access_whitelist

    @property
    def delivery_info(self):
        r"""Gets the delivery_info of this ShowOrderResponse.

        :return: The delivery_info of this ShowOrderResponse.
        :rtype: :class:`huaweicloudsdkdcos.v1.DeliveryInfo`
        """
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, delivery_info):
        r"""Sets the delivery_info of this ShowOrderResponse.

        :param delivery_info: The delivery_info of this ShowOrderResponse.
        :type delivery_info: :class:`huaweicloudsdkdcos.v1.DeliveryInfo`
        """
        self._delivery_info = delivery_info

    @property
    def additional_attachments(self):
        r"""Gets the additional_attachments of this ShowOrderResponse.

        补充附件

        :return: The additional_attachments of this ShowOrderResponse.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        return self._additional_attachments

    @additional_attachments.setter
    def additional_attachments(self, additional_attachments):
        r"""Sets the additional_attachments of this ShowOrderResponse.

        补充附件

        :param additional_attachments: The additional_attachments of this ShowOrderResponse.
        :type additional_attachments: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        self._additional_attachments = additional_attachments

    @property
    def additional_content(self):
        r"""Gets the additional_content of this ShowOrderResponse.

        补充说明

        :return: The additional_content of this ShowOrderResponse.
        :rtype: str
        """
        return self._additional_content

    @additional_content.setter
    def additional_content(self, additional_content):
        r"""Sets the additional_content of this ShowOrderResponse.

        补充说明

        :param additional_content: The additional_content of this ShowOrderResponse.
        :type additional_content: str
        """
        self._additional_content = additional_content

    @property
    def country_code(self):
        r"""Gets the country_code of this ShowOrderResponse.

        手机国际码

        :return: The country_code of this ShowOrderResponse.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        r"""Sets the country_code of this ShowOrderResponse.

        手机国际码

        :param country_code: The country_code of this ShowOrderResponse.
        :type country_code: str
        """
        self._country_code = country_code

    @property
    def phone(self):
        r"""Gets the phone of this ShowOrderResponse.

        联系电话

        :return: The phone of this ShowOrderResponse.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this ShowOrderResponse.

        联系电话

        :param phone: The phone of this ShowOrderResponse.
        :type phone: str
        """
        self._phone = phone

    @property
    def stage(self):
        r"""Gets the stage of this ShowOrderResponse.

        当前阶段.DRAFT草稿、SUMMITED服务申请、IN_PROGRESS服务处理中、ACCEPTANCE服务验收、CLOSED服务关闭

        :return: The stage of this ShowOrderResponse.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this ShowOrderResponse.

        当前阶段.DRAFT草稿、SUMMITED服务申请、IN_PROGRESS服务处理中、ACCEPTANCE服务验收、CLOSED服务关闭

        :param stage: The stage of this ShowOrderResponse.
        :type stage: str
        """
        self._stage = stage

    @property
    def status(self):
        r"""Gets the status of this ShowOrderResponse.

        当前状态

        :return: The status of this ShowOrderResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowOrderResponse.

        当前状态

        :param status: The status of this ShowOrderResponse.
        :type status: str
        """
        self._status = status

    @property
    def logs(self):
        r"""Gets the logs of this ShowOrderResponse.

        服务单日志

        :return: The logs of this ShowOrderResponse.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.OrderLog`]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        r"""Sets the logs of this ShowOrderResponse.

        服务单日志

        :param logs: The logs of this ShowOrderResponse.
        :type logs: list[:class:`huaweicloudsdkdcos.v1.OrderLog`]
        """
        self._logs = logs

    @property
    def fields(self):
        r"""Gets the fields of this ShowOrderResponse.

        扩展字段

        :return: The fields of this ShowOrderResponse.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.FieldEntity`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ShowOrderResponse.

        扩展字段

        :param fields: The fields of this ShowOrderResponse.
        :type fields: list[:class:`huaweicloudsdkdcos.v1.FieldEntity`]
        """
        self._fields = fields

    @property
    def applicant(self):
        r"""Gets the applicant of this ShowOrderResponse.

        申请人

        :return: The applicant of this ShowOrderResponse.
        :rtype: str
        """
        return self._applicant

    @applicant.setter
    def applicant(self, applicant):
        r"""Sets the applicant of this ShowOrderResponse.

        申请人

        :param applicant: The applicant of this ShowOrderResponse.
        :type applicant: str
        """
        self._applicant = applicant

    @property
    def is_accept_terms(self):
        r"""Gets the is_accept_terms of this ShowOrderResponse.

        是否同意服务条款

        :return: The is_accept_terms of this ShowOrderResponse.
        :rtype: bool
        """
        return self._is_accept_terms

    @is_accept_terms.setter
    def is_accept_terms(self, is_accept_terms):
        r"""Sets the is_accept_terms of this ShowOrderResponse.

        是否同意服务条款

        :param is_accept_terms: The is_accept_terms of this ShowOrderResponse.
        :type is_accept_terms: bool
        """
        self._is_accept_terms = is_accept_terms

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowOrderResponse.

        申请时间/创建时间

        :return: The create_time of this ShowOrderResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowOrderResponse.

        申请时间/创建时间

        :param create_time: The create_time of this ShowOrderResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def verification(self):
        r"""Gets the verification of this ShowOrderResponse.

        :return: The verification of this ShowOrderResponse.
        :rtype: :class:`huaweicloudsdkdcos.v1.OrderVerification`
        """
        return self._verification

    @verification.setter
    def verification(self, verification):
        r"""Sets the verification of this ShowOrderResponse.

        :param verification: The verification of this ShowOrderResponse.
        :type verification: :class:`huaweicloudsdkdcos.v1.OrderVerification`
        """
        self._verification = verification

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
        if not isinstance(other, ShowOrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
